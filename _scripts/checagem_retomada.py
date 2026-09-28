#!/usr/bin/env python3
"""Checagem de retomada -- roda no início de toda sessão (CLAUDE.md §3).
Relatório de consistência: sentinelas, biblioteca, estrutura de pastas.
Não depende de rede, NotebookLM ou qualquer serviço externo.
"""
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def secao(titulo: str):
    print(f"\n=== {titulo} ===")


def main():
    secao("Sentinelas")
    resultado = subprocess.run(
        [sys.executable, str(RAIZ / "_scripts" / "verificar_sentinelas.py")],
        capture_output=True, text=True,
    )
    print(resultado.stdout.strip())

    secao("Biblioteca")
    biblioteca = RAIZ / "biblioteca"
    arquivos = list(biblioteca.rglob("*.md")) + list(biblioteca.rglob("*.pdf")) + list(biblioteca.rglob("*.txt"))
    print(f"{len(arquivos)} arquivo(s) em biblioteca/.")
    if not arquivos:
        print("⚠️  Biblioteca vazia — Fase 0 ainda não iniciou a aquisição (ver ESCOPO_HILAS.md §8).")

    secao("Unidades")
    for unidade in sorted((RAIZ / "fase2-unidades").iterdir()):
        if not unidade.is_dir() or unidade.name.startswith("_"):
            continue
        saidas = list((unidade / "saidas").glob("*.md")) if (unidade / "saidas").exists() else []
        print(f"  {unidade.name}: {len(saidas)} saída(s)")

    secao("Próxima ação")
    memoria = RAIZ / "MEMORIA_PROJETO.md"
    if memoria.exists():
        linhas = memoria.read_text(encoding="utf-8").splitlines()
        try:
            i = next(n for n, l in enumerate(linhas) if "Próxima ação" in l)
            print("\n".join(linhas[i:i + 8]))
        except StopIteration:
            print("(seção 'Próxima ação' não encontrada em MEMORIA_PROJETO.md)")
    else:
        print("⚠️  MEMORIA_PROJETO.md não encontrado.")

    secao("Regra Zero (lembrete)")
    print("Ver CLAUDE.md §0/§2-B — a ira de Deus é pessoal e o sacrifício a satisfaz\n"
          "objetivamente. A leitura de Dodd que a esvazia é objeção a refutar, não\n"
          "alternativa a registrar.")


if __name__ == "__main__":
    main()
