#!/usr/bin/env python3
"""Baixa um artefato de Studio e confere: existência, assinatura binária,
e (para áudio/vídeo) presença de conteúdo mínimo -- nunca confia em
`status: completed` sozinho como prova de conteúdo correto.

Usa `notebooklm artifact list/get/export` e `notebooklm download`
(comandos reais do pacote `notebooklm-py`, conferidos nesta sessão contra
o código-fonte v0.8.3).

⚠️ NÃO TESTADO contra conta real. A checagem de CONTEÚDO (o artefato bate
com a linha editorial do CLAUDE.md §2-B, o desfecho é explícito, os
rótulos [OBJETO=DEUS]/[OBJETO=PECADOS] sobrevivem) exige leitura humana
da transcrição -- este script só automatiza a parte mecânica (existência,
assinatura, tamanho).

Uso:
    python3 verificar_artefato.py --perfil hilas-pro --caderno <id> --artefato <id>
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ASSINATURAS = {
    b"ftyp": "MP4/M4A (áudio ou vídeo)",
    b"%PDF-": "PDF",
    b"PK\x03\x04": "ZIP (pode ser .pptx/.docx)",
}


def rodar(args_cli: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["notebooklm", *args_cli], capture_output=True, text=True, check=False)


def checar_assinatura(caminho: Path) -> str:
    cabeca = caminho.read_bytes()[:16]
    for marca, tipo in ASSINATURAS.items():
        if marca in cabeca:
            return tipo
    return f"DESCONHECIDA (primeiros bytes: {cabeca[:8]!r})"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--caderno", required=True, help="notebook id (-n)")
    ap.add_argument("--artefato", required=True, help="artifact id, de `artifact list`")
    ap.add_argument("--destino", default="midia/_saida")
    args = ap.parse_args()

    print("== artifact get (metadados) ==")
    r = rodar(["-p", args.perfil, "artifact", "get", args.artefato, "-n", args.caderno, "--json"])
    if r.returncode != 0:
        print(f"[ERRO] {r.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    try:
        meta = json.loads(r.stdout)
    except json.JSONDecodeError:
        meta = {}
        print("[AVISO] metadados não vieram em JSON puro.", file=sys.stderr)
    print(json.dumps(meta, indent=2, ensure_ascii=False)[:2000])

    status = meta.get("status")
    if status != "completed":
        print(f"[REPROVADO] status='{status}' -- não é 'completed'. "
              "`artifact list`/`get` são a fonte de verdade, não o retorno de `generate`.")
        sys.exit(1)

    destino = Path(args.destino)
    destino.mkdir(parents=True, exist_ok=True)
    print("\n== download ==")
    r = rodar(["-p", args.perfil, "download", args.artefato, "-n", args.caderno,
               "--output", str(destino)])
    print(r.stdout, r.stderr)

    arquivos = list(destino.glob(f"*{args.artefato}*")) or list(destino.iterdir())
    if not arquivos:
        print("[REPROVADO] nenhum arquivo apareceu em destino após download.", file=sys.stderr)
        sys.exit(1)

    for arq in arquivos:
        if not arq.is_file():
            continue
        tamanho = arq.stat().st_size
        assinatura = checar_assinatura(arq) if tamanho > 16 else "ARQUIVO MUITO PEQUENO"
        print(f"{arq.name}: {tamanho} bytes, assinatura={assinatura}")
        if tamanho < 1024:
            print(f"  [REPROVADO] {arq.name} tem menos de 1 KB -- arquivo provavelmente vazio/corrompido.")

    print("\n⚠️ Checagem de CONTEÚDO (desfecho explícito, rótulos preservados, "
          "fontes citadas existem no caderno) exige leitura/audição humana — "
          "ver ESTRATEGIA_MIDIA_HILAS.md §5. Este script só cobre a camada mecânica.")


if __name__ == "__main__":
    main()
