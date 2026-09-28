#!/usr/bin/env python3
"""Conta as linhas da TABELA OFICIAL de sentinelas (não os rascunhos) em
_artifacts/sentinelas_HILAS.md e devolve o estado por código de saída:

    0 = PRONTO      (>= 6 sentinelas na tabela oficial)
    1 = INCOMPLETO  (1-5 sentinelas)
    2 = VAZIO       (0 sentinelas -- trava ativa, bloqueia Write/Edit em saidas/)
    3 = AUSENTE     (arquivo de sentinelas não encontrado)

Usado pelo hook PreToolUse em .claude/settings.json.
"""
import re
import sys
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent / "_artifacts" / "sentinelas_HILAS.md"
LIMIAR_PRONTO = 6

# A tabela oficial é a primeira tabela markdown depois do cabeçalho
# "## Tabela oficial" -- linhas no formato "| N | ... |" com N numérico.
PADRAO_LINHA_TABELA = re.compile(r"^\|\s*(\d+)\s*\|")


def contar_tabela_oficial(texto: str) -> int:
    secao = texto.split("## Tabela oficial", 1)
    if len(secao) < 2:
        return 0
    bloco_oficial = secao[1].split("\n## ", 1)[0]  # até o próximo cabeçalho ##
    return sum(1 for linha in bloco_oficial.splitlines() if PADRAO_LINHA_TABELA.match(linha))


def main():
    if not ARQUIVO.exists():
        print(f"[AUSENTE] {ARQUIVO} não encontrado.")
        sys.exit(3)

    texto = ARQUIVO.read_text(encoding="utf-8")
    n = contar_tabela_oficial(texto)

    if n >= LIMIAR_PRONTO:
        print(f"[PRONTO] {n} sentinelas verificadas na tabela oficial.")
        sys.exit(0)
    elif n > 0:
        print(f"[INCOMPLETO] {n}/{LIMIAR_PRONTO} sentinelas verificadas -- pode escrever, com aviso.")
        sys.exit(1)
    else:
        print("[VAZIO] 0 sentinelas na tabela oficial -- nenhuma unidade pode ser fechada. "
              "Migrar um rascunho de _artifacts/sentinelas_HILAS.md para a tabela oficial "
              "só depois da consulta de verificação contra fonte primária.")
        sys.exit(2)


if __name__ == "__main__":
    main()
