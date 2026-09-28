#!/usr/bin/env python3
"""Busca grega tolerante a acento/espírito/caixa, normalização Unicode
mista, E variantes de glifo grego (theta/phi/pi/kappa/rho "symbol" vs.
forma padrão).

Nasceu de um bug medido no projeto-irmao "Dikaiosyne Theou" (01/09/2026,
sentinela S20): um .md convertido de NA28 grego nao estava nem em NFC nem em
NFD -- normalizacao mista. `grep "ilastērion"` (com acento) devolvia 0
ocorrencias num arquivo que tinha a palavra visivel na tela seis vezes. Foi
falso negativo do buscador, nao do acervo.

Segundo bug, medido nesta sessao (28/09/2026) contra uma conversao propria
de UBS5: o teste reprovava por faltar "ιλασθ" (Lc 18.13), mas a palavra
ESTAVA la -- `ἱλάσϑητί`, grafada com **ϑ** (U+03D1, GREEK THETA SYMBOL),
nao **θ** (U+03B8, GREEK SMALL LETTER THETA). NFD nao resolve isso: as duas
sao letras DIFERENTES no Unicode, nao uma letra + diacritico. E' uma
variante tipografica antiga (comum em edicoes criticas alemas/UBS), nao um
erro de OCR. Corrigido normalizando as 5 letras gregas que tem variante
"symbol" para a forma padrao antes de comparar.

Uso:
    buscar_grego.py "ἱλαστήριον" biblioteca/NA28.md
    buscar_grego.py --listar "ἱλασ" biblioteca/*.md
    buscar_grego.py --teste biblioteca/NA28.md
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

# Letras gregas com uma variante "symbol" de mesmo valor fonetico/lexical,
# usada de forma intercambiavel em edicoes criticas mais antigas (UBS, alguns
# fontes academicas alemas). Mapear para a forma padrao antes de comparar.
VARIANTES_GREGAS = {
    "ϑ": "θ",  # ϑ theta symbol      -> θ
    "ϕ": "φ",  # ϕ phi symbol        -> φ
    "ϖ": "π",  # ϖ pi symbol         -> π
    "ϰ": "κ",  # ϰ kappa symbol      -> κ
    "ϱ": "ρ",  # ϱ rho symbol        -> ρ
    "ς": "σ",  # ς sigma final       -> σ (por simetria/robustez)
}

# As seis ocorrências da tríade no NT -- teste de aceitação para qualquer
# edição grega que este projeto adquira ou reaproveite. Formas exatas, não
# stem genérico: hilasmos (nom./acus. sem -n) e hilasmon (acus. com -n) são
# flexões distintas da mesma palavra; hilastheti (Lc 18.13, aor. pass. imper.)
# e hilaskesthai (Hb 2.17, pres. inf.) são flexões distintas do mesmo verbo.
TESTE_MINIMO = {
    "ιλαστηριον": 2,  # Rm 3.25 · Hb 9.5
    "ιλασμ": 2,       # 1Jo 2.2 (hilasmos) · 1Jo 4.10 (hilasmon) -- raiz comum
    "ιλασθ": 1,       # Lc 18.13 -- hilastheti
    "ιλασκ": 1,       # Hb 2.17 -- hilaskesthai
}


def dobra(texto: str) -> str:
    """Remove acento, espírito, iota subscrito e normaliza caixa.

    NFD decompõe a letra base dos diacríticos combinantes; filtramos toda
    categoria Unicode "Mn" (marca não-espaçante, onde vivem acento e
    espírito gregos) e comparamos em minúsculas. Isso torna a busca
    imune a arquivos em NFC, NFD, ou mistura das duas -- exatamente o
    defeito que a sentinela R11 documenta.
    """
    nfd = unicodedata.normalize("NFD", texto)
    sem_diacritico = "".join(c for c in nfd if unicodedata.category(c) != "Mn")
    minusculo = sem_diacritico.lower()
    for variante, padrao in VARIANTES_GREGAS.items():
        minusculo = minusculo.replace(variante, padrao)
    return minusculo


def buscar(termo: str, caminho: Path, contexto: int = 60):
    bruto = caminho.read_text(encoding="utf-8", errors="replace")
    alvo = dobra(termo)
    achatado = dobra(bruto)

    achados = []
    for m in re.finditer(re.escape(alvo), achatado):
        ini = max(0, m.start() - contexto)
        fim = min(len(bruto), m.end() + contexto)
        achados.append(bruto[ini:fim].replace("\n", " "))
    return achados


def rodar_teste(caminho: Path) -> bool:
    print(f"--teste em {caminho}")
    ok = True
    for raiz, esperado in TESTE_MINIMO.items():
        achados = buscar(raiz, caminho)
        n = len(achados)
        estado = "OK" if n >= esperado else "FALHA"
        if n < esperado:
            ok = False
        print(f"  {raiz:16s} esperado>={esperado:<2d} achado={n:<3d} [{estado}]")
    print("APROVADO" if ok else "REPROVADO -- não usar esta conversão para citação lexical")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("termo", nargs="?", help="raiz ou palavra grega a buscar (acento opcional, ignorado)")
    ap.add_argument("arquivos", nargs="*", help="arquivo(s) .md a varrer")
    ap.add_argument("--listar", action="store_true", help="só conta ocorrências, custo zero, sem imprimir trecho")
    ap.add_argument("--teste", metavar="ARQUIVO", help="roda o teste de aceitação das 6 ocorrências da tríade")
    ap.add_argument("--contexto", type=int, default=60, help="caracteres de contexto ao redor do achado (default 60)")
    args = ap.parse_args()

    if args.teste:
        ok = rodar_teste(Path(args.teste))
        sys.exit(0 if ok else 1)

    if not args.termo or not args.arquivos:
        ap.error("informe termo e ao menos um arquivo, ou use --teste ARQUIVO")

    total = 0
    for nome in args.arquivos:
        caminho = Path(nome)
        if not caminho.exists():
            print(f"[AUSENTE] {caminho}")
            continue
        achados = buscar(args.termo, caminho, args.contexto)
        total += len(achados)
        if args.listar:
            print(f"{caminho}: {len(achados)} ocorrência(s)")
            continue
        for trecho in achados:
            print(f"{caminho}: ...{trecho}...")

    if args.listar:
        print(f"TOTAL: {total} ocorrência(s) de '{args.termo}' (busca cega a acento/espírito/caixa/NFC-NFD)")


if __name__ == "__main__":
    main()
