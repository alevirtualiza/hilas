#!/usr/bin/env python3
"""Audita toda citação 'Autor, p. N' das saídas (fase1-introducao/saidas,
fase2-unidades/*/saidas) contra o disco em biblioteca/ -- confere se a
página existe e se o nome do autor aparece perto dela no arquivo fonte.

Não confirma que a citação é fiel ao texto (isso exige leitura humana) --
só que autor e obra citados têm correspondência plausível em biblioteca/.
"""
import argparse
import re
from pathlib import Path

PADRAO_CITACAO = re.compile(r"\(([A-ZÀ-Ú][\wÀ-ÿ\.\s]{2,40}),\s*p\.?\s*(\d+)\)")


def indice_biblioteca(pasta: Path) -> dict[str, Path]:
    indice = {}
    for arq in pasta.rglob("*.md"):
        indice[arq.stem.lower()] = arq
    return indice


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--saidas", nargs="*", default=["fase1-introducao/saidas", "fase2-unidades"])
    ap.add_argument("--biblioteca", default="biblioteca")
    args = ap.parse_args()

    indice = indice_biblioteca(Path(args.biblioteca))
    total, sem_correspondencia = 0, []

    for base in args.saidas:
        for arq in Path(base).rglob("*.md"):
            texto = arq.read_text(encoding="utf-8", errors="replace")
            for m in PADRAO_CITACAO.finditer(texto):
                total += 1
                autor = m.group(1).strip().lower()
                achado = any(autor.split()[-1] in nome for nome in indice)
                if not achado:
                    sem_correspondencia.append((arq, m.group(0)))

    print(f"TOTAL de citações no padrão 'Autor, p. N': {total}")
    if sem_correspondencia:
        print(f"⚠️  {len(sem_correspondencia)} sem correspondência óbvia em biblioteca/:")
        for arq, cit in sem_correspondencia:
            print(f"  {arq}: {cit}")
    else:
        print("Nenhuma pendência — mas isto confirma só a existência do arquivo, "
              "não a fidelidade da citação. Conferir o trecho manualmente continua obrigatório.")


if __name__ == "__main__":
    main()
