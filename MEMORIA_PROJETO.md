# Memória do projeto — Hilas

**Estado em 28/09/2026:** projeto gerado a partir do molde de pesquisa
exegética (ver `ANATOMIA_DO_MOLDE.md`), adaptado ao recorte lexical dos
três `hilas` (ἱλαστήριον / ἱλασμός / ἱλάσκομαι). **Fase 0 concluída. O
núcleo bibliográfico do debate central está completo, incluindo Dodd na
íntegra.**

## O que já está pronto

- Estrutura completa de pastas, `CLAUDE.md`, `ESCOPO_HILAS.md`.
- `_artifacts/sentinelas_HILAS.md` — **9/6 sentinelas na tabela oficial**,
  todas verificadas contra fonte primária real deste projeto. A citação
  de Dodd/Nicole está confirmada de forma **quíntupla e independente**
  (Morris, BDAG, Stott, Caragounis, e o próprio Dodd); o bug de variante
  de glifo grego (ϑ/θ) e a classe de "grego cifrado" (fonte-símbolo
  corrompida) foram documentados e corrigidos/registrados.
- `_scripts/`: todos testados — `buscar_grego.py` (robusto a NFC/NFD misto
  e a variantes de glifo grego), `verificar_sentinelas.py`,
  `hook_sentinelas.py`, `dossie.py`, `conferir_citacoes.py`,
  `checagem_retomada.py`, `montar_caderno.py`, `prevoo_cota.py`,
  `verificar_artefato.py` (os três últimos com sintaxe conferida contra o
  código-fonte real do `notebooklm-py`, não executados contra conta real).
- `CURADORIA_FONTES_HILAS.md` — protocolo de seis portas + registro de
  todas as aprovações reais.
- `ESTRATEGIA_NOTEBOOKLM_HILAS.md`, `ESTRATEGIA_MIDIA_HILAS.md`.
- `ESTRATEGIA_CIRCULOS_HILAS.md` — 6 cadernos novos (C0-C5, um por
  círculo concêntrico), cada um com Deep Research própria e pacote de
  mídia (14 artefatos/caderno). Total de cadernos do projeto: 11.
- `_artifacts/PERSONAS_MIDIA_HILAS.md` — 5 templates de persona de mídia.
- `_artifacts/persona_notebooklm.txt` — persona de pesquisa upgradeada.
- `.claude/settings.json` — hook `PreToolUse` ligado a `hook_sentinelas.py`.

## Biblioteca — 17 arquivos aprovados

| Arquivo | Tier |
|---|---|
| `NA28_Novum-Testamentum-Graece.md` | S |
| `UBS5_The-Greek-New-Testament.md` | S |
| `Dodd_-_The_Bible_and_the_Greeks_texto.md` | S — **fonte primária do adversário, na íntegra** |
| `Morris_Apostolic_Preaching_of_the_Cross.md` | S |
| `Nicole_Our_Sovereign_Saviour.md` | S |
| `Packer_KnowingGod.md` | S |
| `Stott_The_Cross_of_Christ.md` | S |
| `HillJames_The_Glory_of_the_Atonement.md` | S (⚠️ grego cifrado — só argumento) |
| `Caragounis_Expiation-Propitiation-Reconciliation.md` | S |
| `BDAG_Greek_English_Lexicon_NT.md` | S |
| `BDB_Hebrew_Lexicon_1906_P1de3.md` / `P2de3.md` / `P3de3.md` | S |
| `Milgrom_Leviticus1-16_P1de2.md` / `P2de2.md` | S |
| `Harrison_Levitico_Introducao_e_Comentario_PT.md` | A1 |
| `Wenham_Leviticus_NICOT.md` | A1 (SEM FORMA ORIGINAL — hebraico/grego como imagem) |

**🎉 Núcleo bibliográfico do debate central COMPLETO.** Todos os itens do
padrão de refutação (fonte primária do adversário, melhor formulação,
resposta clássica, ancoragem lexical) estão satisfeitos com texto
primário real, não mais mitigação.

## Ainda não localizado

Ver referência bibliográfica completa em `ESCOPO_HILAS.md` §8: Thayer,
Moulton-Milligan, o artigo de Nicole 1955, TDNT/Büchsel na íntegra,
Travis, Louw-Nida, Ritschl, o artigo de Morris 1951. Nenhum bloqueia o
início da redação — são aprofundamento, não corpus mínimo.

## Unidades

- ✅ **U01 (ἱλαστήριον) redigida** — `fase2-unidades/U01_hilasterion/saidas/RELATORIO_U01.md`.
  Achado: divergência legítima entre Cranfield/Caragounis (alusão ao
  *kapporet*) e Morris (alusão a 4 Macabeus 17.22) — ambos rejeitam Dodd,
  tratada como exceção da Regra Zero, não como concessão. Sentinela R9
  avançada (4 Macabeus citado por Morris, forma confirmada como cognata).
- ⬜ U02 (ἱλασμός), U03 (ἱλάσκομαι), U04 (síntese) — não iniciadas.

## Próxima ação

1. **Redigir U03 (ἱλάσκομαι)** — segunda unidade, corpus já suficiente
   (NA28, UBS5, BDAG, Morris, Dodd cap. V já discute Lc 18.13/Hb 2.17).
   Ordem recomendada no `FASE_0_CHECKLIST.md`: U01 → U03 → U02 → U04.
2. Depois, U02 (ἱλασμός) — Nicole e Packer já cobrem 1Jo 2.2/4.10 diretamente.
3. Rodar os 12 prompts da Fase 1 (`fase1-introducao/prompts_HILAS.md`), se
   ainda não feitos — podem rodar em paralelo à Fase 2.
4. NotebookLM: usar o plugin real `notebooklm-py` — sintaxe conferida,
   nada executado contra conta real ainda.
5. Mídia: só depois de U01-U03 auditadas — ver `ESTRATEGIA_MIDIA_HILAS.md`.

## Decisões pendentes (ver `ESCOPO_HILAS.md` §9)

1. Se vale a pena localizar o artigo de Nicole 1955 e o de Morris 1951,
   dado que ambos já estão citados/resumidos com precisão em cinco fontes
   independentes já presentes.
2. Se Hebreus entra como corpus unificado ou ocorrências isoladas.
3. Se Filo/Josefo sobre o Dia da Expiação entram como Círculo 4 pleno.
