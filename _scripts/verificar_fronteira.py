#!/usr/bin/env python3
"""Confirma que toda fonte citada nas saídas (fase1-introducao/saidas,
fase2-unidades/*/saidas, fase3-*/saidas) está dentro de `biblioteca/` --
a trava de fronteira do `CLAUDE.md` §0 ("o projeto não empresta fontes de
outros projetos temáticos sem que a obra seja copiada primeiro para
biblioteca/").

Dois tipos de achado:
  1. Referência a `biblioteca/<arquivo>` que NÃO existe em disco --
     citação a um arquivo que nunca foi de fato colocado no acervo.
  2. Referência a um caminho de fonte que aponta para FORA de
     `biblioteca/` (outro projeto, pasta absoluta, etc.) -- violação da
     fronteira em si.

Não confirma que a citação é fiel ao conteúdo do arquivo (isso é tarefa
de `conferir_citacoes.py` e de leitura humana) -- só que o arquivo citado
existe e está dentro do limite fronteiriço.
"""
import argparse
import re
from pathlib import Path

# Caminho estilo `biblioteca/Nome_Do_Arquivo.md` ou `biblioteca/Nome.txt`,
# como o projeto sempre cita (ver qualquer RELATORIO_*.md já redigido).
PADRAO_BIBLIOTECA = re.compile(r"`?(biblioteca/[\w\-./]+\.(?:md|txt|pdf))`?")

# Caminho de fonte que aponta para fora de `biblioteca/` -- outro projeto,
# pasta absoluta do usuário, ou caminho de rede local (sinal de que uma
# obra foi citada sem antes ser copiada para dentro do acervo).
PADRAO_FORA = re.compile(
    r"[A-Za-z]:\\Users\\[\w\-\\ ]+|/home/[\w\-/]+/Projetos?/[\w\-/]+|"
    r"(?<!bib)(?<!a )(?<!/)\b(?:Justica-de-Deus|TABERNACULO|Dikaiosyne[ _-]Theou)/biblioteca"
)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--saidas",
        nargs="*",
        default=["fase1-introducao/saidas", "fase2-unidades", "fase3-sintese-final/saidas"],
    )
    ap.add_argument("--biblioteca", default="biblioteca")
    args = ap.parse_args()

    raiz_biblioteca = Path(args.biblioteca)
    ausentes: list[tuple[Path, str]] = []
    fora: list[tuple[Path, str]] = []
    total_refs = 0

    for base in args.saidas:
        base_path = Path(base)
        if not base_path.exists():
            continue
        for arq in base_path.rglob("*.md"):
            texto = arq.read_text(encoding="utf-8", errors="replace")

            for m in PADRAO_BIBLIOTECA.finditer(texto):
                total_refs += 1
                caminho_citado = Path(m.group(1))
                if not caminho_citado.exists():
                    ausentes.append((arq, m.group(1)))

            for m in PADRAO_FORA.finditer(texto):
                fora.append((arq, m.group(0)))

    print(f"TOTAL de referências a `biblioteca/...` nas saídas: {total_refs}")

    if ausentes:
        print(f"\n🔴 {len(ausentes)} referência(s) a arquivo que NÃO existe em biblioteca/:")
        for arq, ref in ausentes:
            print(f"  {arq}: {ref}")
    else:
        print("Nenhuma referência a arquivo ausente de biblioteca/.")

    if fora:
        print(f"\n🔴 {len(fora)} referência(s) apontando para FORA de biblioteca/ "
              "(violação de fronteira -- ver CLAUDE.md §0):")
        for arq, ref in fora:
            print(f"  {arq}: {ref}")
    else:
        print("Nenhuma referência a fonte fora da fronteira do projeto.")

    if ausentes or fora:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
