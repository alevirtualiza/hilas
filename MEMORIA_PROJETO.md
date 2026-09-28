# Memória do projeto — Hilas

**Estado em 28/09/2026:** projeto gerado a partir do molde de pesquisa
exegética (ver `ANATOMIA_DO_MOLDE.md`), adaptado ao recorte lexical dos
três `hilas` (ἱλαστήριον / ἱλασμός / ἱλάσκομαι). **Fase 0 concluída. O
núcleo bibliográfico do debate central está completo, incluindo Dodd na
íntegra. Fases 1 e 2 concluídas** — os 12 prompts introdutórios
(`fase1-introducao/saidas/01-12.md` + `RELATORIO_FASE1.md`) e as quatro
unidades (U01-U04) estão redigidos e auditados.

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
- ✅ **U03 (ἱλάσκομαι) redigida** — `fase2-unidades/U03_hilaskomai/saidas/RELATORIO_U03.md`.
  Cobre Lc 18.13 (sem objeto de pecado, sujeito=Deus) e Hb 2.17 (objeto de
  pecado explícito, sentinela nº2). Achado: a tensão gramatical entre os
  dois textos é o próprio par que Dodd usa como prova dupla; resposta
  não nega a transitividade de Hb 2.17 (Stott concede), argumenta que ela
  não decide sozinha a questão. Achado novo (candidato a sentinela):
  Caragounis mostra que os três léxicos gregos gerais (LSJ, Demetrakos,
  Montanari) citam Hb 2.17 como único exemplo do sentido "expiação" em
  toda a literatura helênica — circularidade lexicográfica no argumento
  de Dodd.
- ✅ **U02 (ἱλασμός) redigida** — `fase2-unidades/U02_hilasmos/saidas/RELATORIO_U02.md`.
  Cobre 1Jo 2.2/4.10. Achado: Dodd concede que o dado do adversário
  (παράκλητος πρὸς τὸν Πατέρα em 2.1) "poderia apoiar" a leitura
  propiciatória-pessoal antes de descartá-lo via a fórmula sacrificial
  da LXX — resposta mostra que essa fórmula pressupõe destinatário
  pessoal (Deus aceita a oferta). Sentinela R6 avançada (Packer confirma,
  de forma independente, a filiação Sócino→Ritschl→Dodd). Debate sobre o
  alcance ("todo o mundo") tratado como divergência legítima
  calvinista×arminiana, distinta do eixo Dodd — Nicole (particularista)
  bem representado, posição arminiana declarada como lacuna.
  Correção registrada: a construção `περὶ τῶν ἁμαρτιῶν` não é genitivo
  objetivo (como a tabela do `CLAUDE.md` §1 descreve), é περί+genitivo —
  não muda a pergunta teológica, mas deve ser corrigido no `CLAUDE.md`
  numa próxima revisão editorial.
- ✅ **U04 (síntese) redigida** — `fase2-unidades/U04_sintese/saidas/RELATORIO_U04.md`.
  **A Fase 2 está completa (U01-U04).** Não consultou a biblioteca
  diretamente (regra `CLAUDE.md` §1) — usou só os três relatórios de
  unidade já auditados. Contribuição própria: mostrar que os três
  "ataques ao pressuposto" das unidades (estatístico/U01, circular/U03,
  seletivo-quanto-ao-contexto/U02) são a mesma crítica metodológica única
  — Dodd decide o léxico geral antes do contexto local, depois subordina
  o contexto à decisão prévia. Lacuna nova declarada: καταλλαγή e
  ἀπολύτρωσις não foram objeto de exegese lexical própria em nenhuma
  unidade (só adjacência textual notada em Rm 3.24-25) — fora do escopo
  desta síntese, que não pode consultar a biblioteca diretamente.

## Fase 1 — 12 prompts introdutórios

- ✅ **Todos os 12 prompts respondidos** —
  `fase1-introducao/saidas/01.md` a `12.md` + `RELATORIO_FASE1.md`.
  Achados principais: BDB confirma etimologia de כפר disputada desde
  1906 (Prompt 1); `ἐξιλάσκομαι` em BDAG fecha parcialmente uma lacuna
  da U03 (1 Clemente/Hermas, Prompt 5); Rm 1.18/1.24/1.26 confirmados
  diretamente no NA28 (Prompt 10); `dossie.py --listar` subconta grego
  por não normalizar Unicode — achado sobre o próprio ferramental,
  registrado sem esconder (Prompt 6); Calvino, Travis e Cremer (na
  ligação específica com ἱλασκ-) confirmados como lacunas reais por
  dupla checagem formal (Prompts 11-12); Carson (HillJames) responde à
  "nova perspectiva sobre Paulo", não a Dodd diretamente — achado novo
  para o Círculo C5.

## Próxima ação

1. **Fases 1 e 2 encerradas.** Considerar a Fase 3 (síntese doutrinal e
   homilética, que reaproveita a U04) — ver `CLAUDE.md` §1.
2. NotebookLM: usar o plugin real `notebooklm-py` — sintaxe conferida,
   nada executado contra conta real ainda.
3. Mídia: o pré-requisito de `ESTRATEGIA_MIDIA_HILAS.md` para o módulo
   `HILAS-M1` está satisfeito (U01-U03 auditadas) — falta apenas execução
   real contra conta NotebookLM (não possível nesta sessão sandboxed).
4. Se o projeto quiser fechar a lacuna de καταλλαγή/ἀπολύτρωσις (U04
   §2.3): abrir dossiê dedicado, possivelmente no Círculo C3 (Loci
   Teológicos) de `ESTRATEGIA_CIRCULOS_HILAS.md`.
5. Considerar promover a observação de Caragounis (circularidade
   lexicográfica de Hb 2.17 em LSJ/Demetrakos/Montanari, U03) a rascunho
   formal em `_artifacts/sentinelas_HILAS.md` na próxima manutenção de
   sentinelas.
6. Corrigir a tabela do `CLAUDE.md` §1 (U02): "genitivo objetivo" →
   περί+genitivo (achado da U02, não muda a pergunta teológica).
7. Registrar em `_artifacts/sentinelas_HILAS.md` a observação sobre
   `dossie.py --listar` não normalizar grego (Fase 1, Prompt 6) — como
   nota de uso do ferramental, não necessariamente sentinela numerada.
8. Priorizar aquisição de Travis e do artigo de Nicole (1955) — os itens
   de maior recorrência nas lacunas declaradas entre Fase 1 e as
   quatro unidades.

## Decisões pendentes (ver `ESCOPO_HILAS.md` §9)

1. Se vale a pena localizar o artigo de Nicole 1955 e o de Morris 1951,
   dado que ambos já estão citados/resumidos com precisão em cinco fontes
   independentes já presentes.
2. Se Hebreus entra como corpus unificado ou ocorrências isoladas.
3. Se Filo/Josefo sobre o Dia da Expiação entram como Círculo 4 pleno.
