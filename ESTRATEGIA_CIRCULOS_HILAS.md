# Estratégia de cadernos por círculo — Hilas

> Complementa `ESTRATEGIA_NOTEBOOKLM_HILAS.md` (cadernos F1/U01-U04) e
> `ESTRATEGIA_MIDIA_HILAS.md` (piloto real, travas de mídia). Este
> documento acrescenta **seis cadernos**, um por círculo concêntrico
> (`ESCOPO_HILAS.md` §4), cada um com sua própria pauta de **Deep
> Research** para fechar lacunas e seu próprio **pacote de mídia**.

**Diferença de função em relação aos cadernos U01-U04:** os cadernos de
unidade (U01-U03) fazem a exegese fechada dos 6 versículos-âncora; os
cadernos de círculo **aprofundam o entorno** de cada um (léxico, campo
semântico, teologia sistemática, corpus bíblico ponderado, Segundo
Templo, história da interpretação) e **geram mídia própria**, com o
cuidado adicional descrito em §3 abaixo — porque mídia gerada de caderno
não-exegético é exatamente o cenário que o piloto do `TAB-95` mostrou
falhar (ver `ESTRATEGIA_MIDIA_HILAS.md` §1).

---

## 1. Os seis cadernos

| Caderno | Círculo | Conteúdo (`ESCOPO_HILAS.md` §4) |
|---|---|---|
| `HILAS C0 - Nucleo Lexical` | 0 | as ocorrências do grupo ἱλασκ- no NT, contadas exaustivamente (não de memória) |
| `HILAS C1 - Campo Semantico` | 1 | ἱλαστήριον/ἱλασμός/ἱλάσκομαι/ἵλεως · καταλλαγή/καταλλάσσω · ἀπολύτρωσις · כפר/כפרת/כפורים |
| `HILAS C2 - Loci Teologicos` | 2 | Dia da Expiação (Lv 16) · sangue (Lv 17.11) · ira de Deus · substituição penal · sacerdócio de Cristo |
| `HILAS C3 - Corpora Biblicos` | 3 | o corpus ponderado inteiro (núcleo/forte/médio/baixo) — Rm, 1Jo, Hb, Lc, Lv, Gn, Êx, Salmos, Nm, Ez, 2Co, Jo |
| `HILAS C4 - Segundo Templo` | 4 | uso homérico/clássico de ἱλάσκομαι · Filo e Josefo sobre o Dia da Expiação · 4 Macabeus 17.22 |
| `HILAS C5 - Historia da Interpretacao` | 5 | Vulgata · Calvino · Ritschl · Dodd · RSV 1946 · Morris/Nicole · Stott/Carson · Travis |

**Total de cadernos do projeto agora: 11** (F1, U01-U04, C0-C5).

---

## 2. Pauta de Deep Research por caderno — fechar lacunas específicas

*Cada pauta segue `ESTRATEGIA_POPULACAO_NOTEBOOKLM.md` §4: query em
inglês, ancorada em nomes/obras específicos, carregando a regra editorial
no final. Antes de cada Deep Research, `dossie.py`/`buscar_grego.py` na
biblioteca local — custo zero, evita gastar Deep Research no que já
temos (ver `CURADORIA_FONTES_HILAS.md` para o que já está aprovado).*

### C0 — Núcleo Lexical

1. Confirmar exaustivamente as ocorrências do grupo ἱλασκ- (incluindo
   ἐξιλάσκομαι, ἵλεως, ἱλατεύομαι) no NT grego, cruzando NA28 e UBS5 —
   `buscar_grego.py` já cobre isso localmente; Deep Research só se o
   `dossie.py` não bastar para casos duvidosos (ex. variantes textuais).
2. **Localizar Thayer**, *A Greek-English Lexicon of the New Testament*
   (1889) — verbetes de ἱλάσκομαι/ἱλασμός/ἱλαστήριον/ἵλεως, texto integral.
3. **Localizar Moulton-Milligan**, *The Vocabulary of the Greek Testament*
   (1914-1929) — uso do grupo nos papiros não-bíblicos (Círculo 4 se
   sobrepõe aqui; registrar duplicidade).

### C1 — Campo Semântico

1. **Localizar TDNT vol. 3**, verbete ἵλεως κτλ. de Friedrich Büchsel —
   página exata já confirmada por Caragounis (p. 311f) — Deep Research
   dirigida a essa paginação específica.
2. Levantar tratamento técnico de καταλλαγή/καταλλάσσω e ἀπολύτρωσις como
   categorias distintas (quem muda de disposição — Deus ou o homem?) —
   nenhuma fonte dedicada ainda no acervo.
3. Fechar a **sentinela R4** (etimologia de כפר): localizar Milgrom e
   Sklar especificamente sobre *purgar* vs. *resgatar* (já parcialmente
   coberto por Milgrom no acervo — conferir se a obra já resolve ou se
   falta Sklar).

### C2 — Loci Teológicos

1. Substituição penal: localizar defesas e críticas contemporâneas
   dedicadas (Packer, Green & Baker) — nenhuma no acervo ainda.
2. Sacerdócio de Cristo em Hebreus, ligado a ἱλάσκομαι (Hb 2.17) — um
   comentário técnico dedicado de Hebreus (Lane, Attridge, Ellingworth,
   Cockerill — nenhum no acervo).
3. A ira de Deus como *locus* de teologia sistemática — Stott já cobre
   parcialmente; verificar se falta uma monografia dedicada.

### C3 — Corpora Bíblicos

1. Comentários técnicos específicos para cada texto de peso "médio" do
   Círculo 3 que ainda não têm cobertura dedicada: Gn 32.20 (Jacó/Esaú),
   Êx 32.14 (intercessão de Moisés), Salmos 24/78/129 nas numerações LXX.
2. 2Co 5.18-21 (καταλλαγή) como categoria vizinha — comentário técnico de
   2 Coríntios ainda ausente.

### C4 — Segundo Templo e Grego Secular

1. **Fechar a sentinela R9**: confirmar a palavra exata em 4 Macabeus
   17.22 (ἱλαστήριον ou cognato?) contra uma edição crítica do texto grego
   — prioridade alta, sentinela aberta há várias sessões.
2. Localizar Filo e Josefo sobre o Dia da Expiação, tradução com aparato
   (Loeb ou equivalente) — Caragounis já cita Filo/Josefo lateralmente,
   mas sem os textos primários no acervo.
3. Uso homérico/clássico de ἱλάσκομαι — Dodd e Morris já discutem isso
   extensamente (Platão, *Leis* 862c; inscrição de Men Tyrannus); Deep
   Research só para achados adicionais além dos dois já cobertos.

### C5 — História da Interpretação

1. **Fechar a sentinela R6**: localizar Ritschl, *Die christliche Lehre
   von der Rechtfertigung und Versöhnung* (1870-1874) — verificar se Dodd
   o cita e em que termos, antes de tratá-los como a mesma posição.
2. **Fechar a sentinela R8**: verificar edição por edição se a RSV (1946)
   e revisões posteriores (NRSV, ESV) mantiveram ou reverteram a troca de
   "propitiation" por "expiation" em Rm 3.25 e 1Jo 2.2.
3. Localizar Cremer (já referenciado no projeto-irmão "Justiça de Deus"
   como precursor da leitura relacional) e Aulén, *Christus Victor* —
   ambos tocam o mesmo padrão de dissolver a leitura forense/pessoal.
4. Localizar o artigo de periódico de Nicole (*WTJ* 17, 1955) e de Morris
   (*ET* 62, 1951) — já citados/resumidos 5× de forma indireta; baixa
   prioridade, mas fecha o círculo se aparecerem.
5. Travis, *Christ and the Judgment of God* — ainda não localizado;
   mapear com cuidado se é posição intermediária genuína (não presumir).

---

## 3. Pacote de mídia — igual para os seis cadernos

**Pré-requisito (adaptação do Gatilho 2 de `ESTRATEGIA_NOTEBOOKLM_HILAS.md`
§2 para estes cadernos):** nenhuma mídia antes de (a) a Deep Research da
§2 ter rodado e as fontes entrado `ready`; (b) `GUIA_EDITORIAL_HILAS.md`
(ver `ESTRATEGIA_MIDIA_HILAS.md` §4) estar **dentro do caderno** como
fonte; (c) pelo menos uma consulta de verificação ter auditado o que a
Deep Research trouxe (Regra do achado central de §4 da estratégia de
NotebookLM — o RAG completa corpus sem avisar).

Cada caderno gera, nesta ordem:

| # | Artefato | Formato/parâmetro | Personas |
|---|---|---|---|
| 1 | Áudio — Debate 1 | `generate audio --format debate` | A1 × A3 (ver `PERSONAS_MIDIA_HILAS.md`) |
| 2 | Áudio — Debate 2 | `generate audio --format debate` | A1 × A4 |
| 3 | Áudio — Debate 3 | `generate audio --format debate` | A2 × A5 |
| 4 | Áudio — solo Erudito | `generate audio --format deep-dive` | A1 |
| 5 | Áudio — solo Pastor | `generate audio --format deep-dive` | A2 |
| 6 | Áudio — solo Aluno | `generate audio --format deep-dive --length short` | A5 |
| 7-8 | Vídeo — versões dos Debates 1 e 2 | `generate video --format explainer` | A1×A3, A1×A4 |
| 9-10 | Vídeo — solo Erudito e solo Aluno | `generate video --format explainer` | A1, A5 |
| 11 | Mapa mental | `generate mind-map --instructions "<guia editorial>"` | — |
| 12 | Relatório aprofundado | `generate report --format study-guide --append "<regra zero>"` | — |
| 13 | Infográfico | `generate infographic` | — |
| 14 | Flashcards | `generate flashcards --quantity standard` | — |

**14 artefatos por caderno × 6 cadernos = 84 chamadas de `generate`.**

### Preenchimento dos parâmetros por caderno

| Caderno | `{ADVERSARIO_N3}` (Debate 1) | `{DEBATE_N1}` (Debate 2) |
|---|---|---|
| C0 | Dodd — o grupo ἱλασκ- na LXX não tem Deus como objeto | extensão de 1Jo 2.2 entre tradições (ver sentinela 3/nº3 oficial) |
| C1 | Dodd sobre a classificação em 3 passos das traduções LXX (sentinela 5) | καταλλαγή aponta para mudança de disposição de Deus ou do homem? |
| C2 | críticas contemporâneas à substituição penal (Green & Baker, se localizado) | extensão da propiciação (particular × universal) |
| C3 | leitura de Rm 1.18-32 como "processo impessoal" (Dodd, Stott cap. sobre wrath) | harmonização de Gn 32.20/Êx 32.14 como propiciação "interpessoal" — debate lexical interno |
| C4 | uso pagão de ἱλάσκομαι como prova de que o NT herdaria sentido impessoal | se 4 Macabeus 17.22 é ou não o mesmo termo (sentinela R9) |
| C5 | Ritschl como precursor de Dodd (sentinela R6) | Aulén (*Christus Victor*) × leitura forense — dissolvem ou complementam? |

⚠️ **Nenhuma célula acima é fixa até a Deep Research correspondente (§2)
rodar** — se a pauta não encontrar fonte primária suficiente para um dos
lados, a query do debate **declara a lacuna** em vez de fabricar as duas
pontas (mesma regra dos itens 1-2 do padrão de refutação).

---

## 4. Cota — antes de disparar qualquer coisa

84 chamadas de `generate` (círculos) + as chamadas já previstas para
F1/U01-U04 excedem em muito o teto de ~40 chamadas/dia medido nos
projetos-irmãos (`ESTRATEGIA_NOTEBOOKLM_HILAS.md` §7). **Um caderno de
círculo por dia, no máximo** — nunca dois no mesmo dia, e sempre depois
de `prevoo_cota.py`. Ordem sugerida: **C0 → C1 → C4 (fecha R9) → C5
(fecha R6/R8) → C2 → C3** — prioriza fechar sentinelas abertas cedo.

---

## 5. Verificação

Mesma tabela de `ESTRATEGIA_MIDIA_HILAS.md` §5, sem exceção — inclusive
para os cadernos de círculo. **Atenção redobrada aqui**: como estes
cadernos recebem material de Deep Research (não só biblioteca curada
manualmente), o risco do achado central (RAG completa corpus sem avisar)
é maior. Toda atribuição em qualquer artefato passa pela classificação
`[FONTE PRIMÁRIA NO CORPUS]` / `[CITADO POR TERCEIROS]` / `[NÃO
ENCONTRADO]` antes de aceitar o artefato como pronto.
