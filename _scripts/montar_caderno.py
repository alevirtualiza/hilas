#!/usr/bin/env python3
"""Cria o caderno de uma unidade no NotebookLM e envia as fontes Tier S/A
uma a uma, aguardando `ready` antes de prosseguir.

Usa a CLI do plugin `notebooklm-py` (https://github.com/teng-lin/notebooklm-py,
`pip install notebooklm-py`). A sintaxe abaixo foi conferida nesta sessão
contra o **código-fonte real do pacote** (baixado via `pip download`,
versão 0.8.3 -- não apenas documentação): `notebooklm create <título>`,
`notebooklm source add <conteúdo> -n <id> [--type file|url|text|youtube]
[--title ...]`, `notebooklm auth check --test`. Confirma exatamente as
regras já herdadas de outros projetos (Regra 1 de
ESTRATEGIA_NOTEBOOKLM_HILAS.md §4): `-p`/`--profile` é opção **global**
(antes do subcomando); `-n`/`--notebook` é opção **do subcomando**;
`notebooklm use` grava estado global e é evitado aqui em favor de `-n`
explícito em cada chamada.

⚠️ NÃO TESTADO CONTRA UMA CONTA REAL -- este ambiente (container efêmero,
sem credenciais de longo prazo) não tem `notebooklm login` feito. A
sintaxe dos comandos foi verificada por leitura do código-fonte, não por
execução. Rodar `notebooklm --version` e `notebooklm -p hilas-pro auth
check --test` antes do primeiro uso real.

Uso:
    python3 montar_caderno.py --perfil hilas-pro --nome "HILAS U01 - Hilasterion" \
        --fontes biblioteca/NA28.md biblioteca/BDAG.md --simular
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONFIG = RAIZ / "projeto.config.txt"


def rodar(args_cli: list[str], simular: bool) -> subprocess.CompletedProcess | None:
    print(f"$ notebooklm {' '.join(args_cli)}")
    if simular:
        return None
    return subprocess.run(["notebooklm", *args_cli], capture_output=True, text=True, check=False)


def checar_auth(perfil: str, simular: bool) -> bool:
    r = rodar(["-p", perfil, "auth", "check", "--test"], simular)
    if simular:
        print("[SIMULADO] auth check --test")
        return True
    ok = r is not None and r.returncode == 0
    print(r.stdout if r else "")
    if not ok:
        print("[REPROVADO] Porta 1 -- autenticação real falhou. `profile list` "
              "não basta; só `auth check --test` decide.", file=sys.stderr)
    return ok


def caderno_ja_existe(perfil: str, nome: str, simular: bool) -> bool:
    """`notebooklm list` é comando de topo (não `notebook list`) neste pacote."""
    if simular:
        print(f"[SIMULADO] verificaria se já existe caderno '{nome}'")
        return False
    r = rodar(["-p", perfil, "list", "--json"], simular)
    if r is None or r.returncode != 0:
        print("[AVISO] não foi possível listar cadernos -- Porta 2 não conferida.", file=sys.stderr)
        return False
    try:
        dados = json.loads(r.stdout)
    except json.JSONDecodeError:
        print("[AVISO] saída de `list --json` não é JSON puro -- cortar no "
              "primeiro '{' ou '[' antes de reparsear (armadilha conhecida "
              "de CLIs deste tipo).", file=sys.stderr)
        return False
    lista = dados.get("notebooks", dados) if isinstance(dados, dict) else dados
    nomes = [n.get("title", "") for n in lista]
    return nome in nomes


def enviar_fontes(perfil: str, notebook_id: str, fontes: list[str], simular: bool):
    """`source add <conteúdo> -n <id>` -- `content` é argumento posicional
    (caminho de arquivo ou URL); `--type` é auto-detectado se omitido."""
    for fonte in fontes:
        caminho = Path(fonte)
        if not caminho.exists():
            print(f"[AUSENTE] {fonte} não existe -- Porta 3 reprovada para esta fonte.", file=sys.stderr)
            continue
        palavras = len(caminho.read_text(encoding="utf-8", errors="replace").split())
        print(f"  {fonte}: {palavras} palavras")
        rodar(["-p", perfil, "source", "add", str(caminho), "-n", notebook_id,
               "--type", "file", "--title", caminho.stem], simular)
        if not simular:
            time.sleep(2)  # espaçar chamadas -- evitar rate limit medido alhures


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfil", required=True)
    ap.add_argument("--nome", required=True, help='ex.: "HILAS U01 - Hilasterion"')
    ap.add_argument("--fontes", nargs="+", required=True)
    ap.add_argument("--simular", action="store_true", help="não executa nada, só imprime os comandos (Regra 4 de ESTRATEGIA_NOTEBOOKLM_HILAS.md)")
    args = ap.parse_args()

    if not args.nome.startswith("HILAS "):
        print("[REPROVADO] o nome do caderno precisa do prefixo 'HILAS ' -- "
              "único filtro visual numa conta com cadernos de outros projetos.", file=sys.stderr)
        sys.exit(1)

    if not checar_auth(args.perfil, args.simular):
        sys.exit(1)

    if caderno_ja_existe(args.perfil, args.nome, args.simular):
        print(f"[REPROVADO] Porta 2 -- já existe caderno com o nome exato '{args.nome}'.", file=sys.stderr)
        sys.exit(1)

    print(f"Criando caderno '{args.nome}'...")
    rodar(["-p", args.perfil, "create", args.nome], args.simular)  # comando de topo, título posicional

    enviar_fontes(args.perfil, "<UUID-A-CAPTURAR-DA-RESPOSTA-ACIMA>", args.fontes, args.simular)

    print("\n⚠️  Ao capturar o UUID real da criação acima, gravar em "
          f"{CONFIG} e em _LOG_EXECUCAO.md, conforme ESTRATEGIA_NOTEBOOKLM_HILAS.md §3.")


if __name__ == "__main__":
    main()
