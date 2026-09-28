#!/usr/bin/env python3
"""Varre biblioteca/ por termo e emite dossiê pequeno: arquivo, autor
(frontmatter, se houver), e trechos de contexto. --listar só conta,
custo zero -- rodar antes de qualquer consulta que gaste crédito de IA.
"""
import argparse
import re
import sys
from pathlib import Path

FRONT_AUTOR = re.compile(r"^autor:\s*(.+)$", re.MULTILINE | re.IGNORECASE)


def autor_de(texto: str) -> str:
    m = FRONT_AUTOR.search(texto[:2000])
    return m.group(1).strip() if m else "[autor não identificado no frontmatter]"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("termo", help="termo a buscar (case-insensitive, substring simples -- para grego use buscar_grego.py)")
    ap.add_argument("--pasta", default="biblioteca", help="pasta a varrer (default: biblioteca/)")
    ap.add_argument("--listar", action="store_true", help="só conta ocorrências por arquivo, custo zero")
    ap.add_argument("--contexto", type=int, default=80)
    args = ap.parse_args()

    raiz = Path(args.pasta)
    if not raiz.exists():
        print(f"[AUSENTE] pasta '{raiz}' não existe.")
        sys.exit(1)

    arquivos = sorted(raiz.rglob("*.md")) + sorted(raiz.rglob("*.txt"))
    if not arquivos:
        print(f"[VAZIO] nenhum .md/.txt em '{raiz}' -- biblioteca ainda não populada.")
        return

    termo_low = args.termo.lower()
    total_arquivos_com_termo = 0
    for caminho in arquivos:
        texto = caminho.read_text(encoding="utf-8", errors="replace")
        idxs = [m.start() for m in re.finditer(re.escape(termo_low), texto.lower())]
        if not idxs:
            continue
        total_arquivos_com_termo += 1
        autor = autor_de(texto)
        if args.listar:
            print(f"{caminho.name}  [{autor}]  {len(idxs)} ocorrência(s)")
            continue
        print(f"\n=== {caminho.name}  [{autor}] — {len(idxs)} ocorrência(s) ===")
        for i in idxs[:5]:
            ini, fim = max(0, i - args.contexto), min(len(texto), i + args.contexto)
            print(f"  ...{texto[ini:fim].strip()}...")

    print(f"\nTOTAL: {total_arquivos_com_termo}/{len(arquivos)} arquivo(s) com '{args.termo}'.")
    if total_arquivos_com_termo == 0:
        print("⚠️  Zero não é ausência confirmada — ver dupla checagem em CLAUDE.md §0. "
              "Se o termo for grego/hebraico, refazer com buscar_grego.py antes de declarar ausência.")


if __name__ == "__main__":
    main()
