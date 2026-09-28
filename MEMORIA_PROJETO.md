# Memória do projeto — Hilas

**Estado em 28/09/2026:** projeto gerado a partir do molde de pesquisa
exegética (ver `ANATOMIA_DO_MOLDE.md`), adaptado ao recorte lexical dos
três `hilas` (ἱλαστήριον / ἱλασμός / ἱλάσκομαι). **Fase 0 concluída. O
núcleo bibliográfico do debate central está completo, incluindo Dodd na
íntegra.**

## O que já está pronto

- Estrutura completa de pastas, `CLAUDE.md`, `ESCOPO_HILAS.md`.
- `_artifacts/sentinelas_HILAS.md` — **8/6 sentinelas na tabela oficial**,
  todas verificadas contra fonte primária real deste projeto: dado
  gramatical do NA28 lido ao vivo; o método real de Dodd (agora lido
  diretamente do próprio livro, não mais via citação em Morris) e a
  crítica de Nicole confirmados de forma **tripla e independente**
  (Morris, o texto de Dodd, e o BDAG); o bug de variante de glifo grego
  (ϑ/θ) corrigido no `buscar_grego.py`.
- `_scripts/`: todos testados — `buscar_grego.py` (robusto a NFC/NFD misto
  e a variantes de glifo grego), `verificar_sentinelas.py`,
  `hook_sentinelas.py`, `dossie.py`, `conferir_citacoes.py`,
  `checagem_retomada.py`, `montar_caderno.py`, `prevoo_cota.py`,
  `verificar_artefato.py` (os três últimos com sintaxe conferida contra o
  código-fonte real do `notebooklm-py`, não executados contra conta real).
- `CURADORIA_FONTES_HILAS.md` — protocolo de seis portas + registro de
  todas as aprovações reais.
- `ESTRATEGIA_NOTEBOOKLM_HILAS.md`, `ESTRATEGIA_MIDIA_HILAS.md`.
- `.claude/settings.json` — hook `PreToolUse` ligado a `hook_sentinelas.py`.

## Biblioteca — 14 arquivos aprovados

| Arquivo | Tier |
|---|---|
| `NA28_Novum-Testamentum-Graece.md` | S |
| `UBS5_The-Greek-New-Testament.md` | S |
| `Dodd_-_The_Bible_and_the_Greeks_texto.md` | S — **fonte primária do adversário, na íntegra** |
| `Morris_Apostolic_Preaching_of_the_Cross.md` | S |
| `Nicole_Our_Sovereign_Saviour.md` | S |
| `Packer_KnowingGod.md` | S |
| `BDAG_Greek_English_Lexicon_NT.md` | S |
| `BDB_Hebrew_Lexicon_1906_P1de3.md` / `P2de3.md` / `P3de3.md` | S |
| `Milgrom_Leviticus1-16_P1de2.md` / `P2de2.md` | S |
| `Harrison_Levitico_Introducao_e_Comentario_PT.md` | A1 |
| `Wenham_Leviticus_NICOT.md` | A1 (SEM FORMA ORIGINAL — hebraico/grego como imagem) |

**🎉 Núcleo bibliográfico do debate central COMPLETO.** Todos os itens do
padrão de refutação (fonte primária do adversário, melhor formulação,
resposta clássica, ancoragem lexical) estão satisfeitos com texto
primário real, não mais mitigação.

## Ainda não localizado em nenhuma das duas pastas irmãs verificadas

- Thayer, *A Greek-English Lexicon of the New Testament* (1889)
- Moulton-Milligan, *Vocabulary of the Greek Testament* (1914-1929)
- Roger Nicole, "C. H. Dodd and the Doctrine of Propitiation", *WTJ* 17 (1955), pp. 117-157 — artigo (distinto do livro já no projeto)
- Leon Morris, artigo em *Expository Times* 62 (1951), pp. 227-233 — **achado novo**, distinto do livro de 1955 já no projeto
- TDNT (Kittel/Friedrich), verbete de Büchsel
- John Stott, *The Cross of Christ* (1986)
- D. A. Carson, ensaios sobre Rm 3.21-26
- Stephen Travis, *Christ and the Judgment of God* (1986/2008)
- Louw-Nida, *Greek-English Lexicon... Based on Semantic Domains*
- Albrecht Ritschl, *Die christliche Lehre von der Rechtfertigung und Versöhnung*

Nenhum destes bloqueia o início da redação — são aprofundamento, não
corpus mínimo.

## Próxima ação

1. **Abrir a Unidade 01 (ἱλαστήριον)** — corpus mais que suficiente: NA28,
   UBS5, BDAG, BDB, Dodd, Morris, Milgrom, Harrison, Wenham.
2. Rodar os 12 prompts da Fase 1 (`fase1-introducao/prompts_HILAS.md`).
3. NotebookLM: usar o plugin real `notebooklm-py` — sintaxe conferida,
   nada executado contra conta real ainda.
4. Mídia: só depois de U01-U03 auditadas — ver `ESTRATEGIA_MIDIA_HILAS.md`.

## Decisões pendentes (ver `ESCOPO_HILAS.md` §9)

1. Se vale a pena localizar o artigo de Nicole 1955 e o de Morris 1951,
   dado que ambos já estão citados/resumidos com precisão em fontes já
   presentes (BDAG, e o próprio Morris 1955 no caso de Nicole).
2. Se Hebreus entra como corpus unificado ou ocorrências isoladas.
3. Se Filo/Josefo sobre o Dia da Expiação entram como Círculo 4 pleno.
