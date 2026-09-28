#!/usr/bin/env python3
"""Livro-razão de cota antes de gerar artefatos de Studio.

Usa `notebooklm usage --json` (comando real do pacote `notebooklm-py`,
conferido nesta sessão contra o código-fonte v0.8.3) -- não inventa
contagem própria. Grava cada leitura em _artifacts/LIVRO_RAZAO_COTA.csv
para detectar consumo entre sessões (o servidor não expõe histórico).

⚠️ NÃO TESTADO contra conta real -- ver aviso em montar_caderno.py.

Uso:
    python3 prevoo_cota.py --perfil hilas-pro
    python3 prevoo_cota.py --perfil hilas-pro --fila audio audio video report
"""
import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LIVRO_RAZAO = RAIZ / "_artifacts" / "LIVRO_RAZAO_COTA.csv"


def ler_uso(perfil: str) -> dict | None:
    r = subprocess.run(["notebooklm", "-p", perfil, "usage", "--json"],
                        capture_output=True, text=True, check=False)
    if r.returncode != 0:
        print(f"[ERRO] `notebooklm usage --json` falhou: {r.stderr.strip()}", file=sys.stderr)
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        print("[ERRO] saída de `usage --json` não é JSON puro.", file=sys.stderr)
        return None


def gravar_livro_razao(dados: dict):
    novo = not LIVRO_RAZAO.exists()
    with LIVRO_RAZAO.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(["timestamp_utc", "dados_json"])
        w.writerow([datetime.now(timezone.utc).isoformat(), json.dumps(dados, ensure_ascii=False)])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--fila", nargs="*", default=[],
                     help="tipos de artefato que se pretende gerar em sequência "
                          "(ex.: audio audio video report) -- só para lembrete visual, "
                          "não decrementa cota localmente (o servidor é a única fonte de verdade)")
    args = ap.parse_args()

    dados = ler_uso(args.perfil)
    if dados is None:
        sys.exit(1)

    print(json.dumps(dados, indent=2, ensure_ascii=False))
    gravar_livro_razao(dados)

    if args.fila:
        print(f"\nFila pretendida: {args.fila} ({len(args.fila)} chamada(s) de `generate`)")
        print("⚠️ Cota é da conta inteira, não deste caderno -- se a conta for "
              "compartilhada com outros projetos, reconferir premissa antes de "
              "assumir orçamento (ver ESTRATEGIA_NOTEBOOKLM_HILAS.md §7).")
        print("⚠️ Gerar sempre o que FECHA um par objeção/resposta primeiro, "
              "nunca o que só abre (Regra Zero em mídia).")


if __name__ == "__main__":
    main()
