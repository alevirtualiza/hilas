# Relatório consolidado — Fase 1 (12 prompts introdutórios)

**Data:** 28/09/2026
**Base:** `fase1-introducao/prompts_HILAS.md`, saídas `01.md` a `12.md`
neste mesmo diretório.

---

## 1. O que os 12 prompts estabeleceram

### Bloco A — lexical hebraico (1-3)

1. **A raiz כפר** tem etimologia genuinamente disputada desde o próprio
   BDB (1906: "orig. mng. dub."), entre "cobrir" (árabe *kafara*) e
   "lavar/remover" (aramaico, via Robertson Smith) — confirmando a Regra
   14 do `CLAUDE.md`. O uso concreto no texto (Gn 32.21 pessoal; Lv 4.20
   cultual; Nu 35.33 jurídico-territorial) decide o sentido em cada
   ocorrência, não a raiz. **Sentinela R4 permanece aberta**, agora com
   base textual mais precisa (a citação exata do BDB).
2. **כַּפֹּרֶת** é o móvel concreto do santuário, mas seu nome deriva da
   função cultual, não da forma física — BDB rejeita explicitamente a
   etimologia "tampa/cobertura". A LXX traduz por ἱλαστήριον de forma
   **concreta** (o objeto), não abstrata — confirmando a base lexical
   para (mas não decidindo) a divergência Cranfield×Morris já
   documentada na U01.
3. **אָשָׁם e חַטָּאת** — Milgrom prefere "reparation offering" e
   "purification offering" às traduções tradicionais. A ligação com Is
   53.10 **não pôde ser confirmada no acervo** (Milgrom cobre só Lv
   1-16) — lacuna real declarada, primeira do relatório.

### Bloco B — lexical grego e a ponte da LXX (4-7)

4. **Dossiê Dodd × Morris** sobre grego pagão, Filo e Josefo, lado a
   lado: ambos concordam que o grego pagão comum usa o sentido pessoal
   ("aplacar"); divergem sobre se a LXX/Judaísmo helenístico rompe com
   esse padrão. Filo e Josefo, segundo Büchsel (via Stott), preservam o
   sentido "aplacar" — mas **nenhum dos dois autores está no acervo como
   fonte primária**.
5. **ἐξιλάσκομαι na LXX** — BDAG confirma, com fonte lexicográfica
   primária (não apenas resumo de terceiros), que a divindade é o objeto
   mais frequente do verbo em toda a literatura grega, incluindo Filo,
   Josefo, 1 Clemente e o Pastor de Hermas — **avanço direto sobre uma
   lacuna da U03** (a "ilha linguística" de Dodd, agora com confirmação
   lexicográfica independente de Stott).
6. **Inventário fechado em seis ocorrências** da tríade no NT, todas
   reconfirmadas contra o NA28. **Achado colateral relevante:**
   `dossie.py --listar`, usado sem `buscar_grego.py`, subconta essas
   ocorrências (4 de 6) por não normalizar acentuação — comportamento já
   documentado no próprio `--help` do script, mas nunca destacado em uma
   saída antes. Recomenda-se nota explícita no `CLAUDE.md`.
7. **ἱλαστήριον em Rm 3.25** — resumo com remissão à U01 (evitando
   duplicar); reafirma que o anartro "pesa mas não decide".

### Bloco C — a disputa central em fonte primária (8-10)

8. **O método de Dodd**, reunido pela primeira vez como um argumento de
   sistema completo (não apenas texto por texto): separar o uso pagão do
   uso da LXX por decreto teológico-metodológico, depois aplicar essa
   classificação retroativamente aos cinco textos do NT — a sentinela
   oficial nº5, agora nomeada e documentada como o núcleo do programa
   inteiro de Dodd, não apenas de uma unidade.
9. **A resposta de Morris/Nicole**, com um dado novo não citado nas
   Unidades 01-04: os episódios de Arão e Finéias (via Stott) como casos
   da LXX em que a ira de Yahweh é objeto explícito da ação sacerdotal —
   referências exatas de versículo **não confirmadas nesta sessão**
   (lacuna).
10. **A ira em Rm 1.18-32** — confirmada gramaticalmente, direto do
    NA28 (ἀποκαλύπτεται ... ἀπ' οὐρανοῦ, e o παρέδωκεν αὐτοὺς ὁ θεός
    repetido em 1.24 e 1.26): a ira tem origem locativa celeste e Deus
    como sujeito gramatical ativo em cada ato de julgamento — não um
    processo impessoal. Reforça, com base gramatical direta (não apenas
    citação de comentarista), o ataque ao pressuposto já usado nas
    Unidades 01-04.

### Bloco D — história da interpretação (11-12)

11. **Calvino** — nenhuma obra no acervo; lacuna real declarada, não
    preenchida por reconstrução de memória (Regra 13). **Ritschl** —
    confirmado apenas via Packer (uma única fonte secundária, com um
    possível erro de impressão na própria citação — "late 1900s" em vez
    de "late 1800s" — a verificar). R6 permanece aberta.
12. **Cremer** — presente no acervo (via BDAG), mas **não** ligado ao
    debate ἱλασκ- em nenhuma das citações localizadas — seu papel na
    linhagem não pode ser confirmado. **Travis** — ausência total
    confirmada por dois métodos independentes (grep + listagem) — lacuna
    de alta prioridade. **Achado novo:** o capítulo de Carson em
    HillJames responde primariamente à "nova perspectiva sobre Paulo"
    (Sanders, Dunn, Wright), não a Dodd diretamente — sugere que a
    linhagem do `CLAUDE.md` trata dois adversários relacionados mas
    distintos como um só.

---

## 2. Achados que avançam sentinelas ou merecem promoção

| Item | Situação |
|---|---|
| **Sentinela nº5** (método de Dodd) | Consolidada como o programa único por trás dos cinco textos (Prompt 8) — não um novo achado, mas a primeira formulação explícita do "todo" |
| **Sentinela R4** (etimologia כפר) | Avançada com a citação exata do BDB (verbete 4612) — ainda aberta |
| **Sentinela R6** (Ritschl) | Reforçada com a mesma fonte (Packer) já usada na U02, mais uma nota sobre possível erro de impressão a verificar — ainda aberta |
| **Lacuna da U03** (1 Clemente/Hermas "ilha linguística") | **Fechada parcialmente** — BDAG (fonte primária lexicográfica) confirma o mesmo dado, de forma independente de Stott (Prompt 5) |
| **`dossie.py` subconta grego** | **Achado novo, não uma sentinela** — comportamento do script já documentado no seu próprio `--help`, mas nunca destacado numa saída. Recomenda-se nota no `CLAUDE.md` §3 ou §5 |
| **Carson responde à "nova perspectiva", não só a Dodd** | **Achado novo** — recomendado para o Círculo C5 (História da Interpretação) |

---

## 3. Lacunas declaradas (consolidado dos 12 prompts)

1. Nenhuma fonte sobre Is 53.10 (Prompt 3).
2. Filo e Josefo, texto primário, ausentes (Prompts 4, 5, 9).
3. Büchsel, texto primário, ausente (Prompt 4).
4. O artigo de Nicole (*WTJ* 17, 1955), texto primário, ausente
   (Prompt 9 — já registrado em `ESCOPO_HILAS.md`).
5. Referências exatas de Nu 16.46-48 (Arão) e Nu 25.11-13 (Finéias) não
   confirmadas contra a LXX (Prompt 9).
6. Rm 1.28 não reconferido diretamente contra o NA28 (Prompt 10 —
   1.18, 1.24, 1.26 já confirmados).
7. John Murray, *The Epistle to the Romans* vol. I, ausente (Prompt 10).
8. Calvino, qualquer obra, ausente (Prompt 11).
9. Ritschl, texto primário, ausente (Prompt 11 — já era R6).
10. Cremer, obra específica sobre o grupo ἱλασκ- (se existir), ausente
    (Prompt 12).
11. Travis, *Christ and the Judgment of God*, ausente (Prompt 12 — já
    registrado em `ESCOPO_HILAS.md`, agora com dupla checagem formal).

**Nenhuma destas lacunas bloqueia o uso das Unidades 01-04 já
redigidas** — todas foram descobertas ao aprofundar além do que as
quatro unidades exigiam, não ao questionar o que já foi auditado.

---

## 4. Checkpoint factual da Fase 1

- [x] Os 12 prompts foram respondidos com base no acervo já curado
      (nenhuma nova fonte foi necessária para os pontos centrais; as
      lacunas identificadas são aprofundamentos, não bloqueios)
- [x] Toda afirmação de ausência passou por dupla checagem (conteúdo +
      listagem, ou conteúdo + léxico primário, conforme o caso)
- [x] Toda citação de página/verbete conferida diretamente no disco
      nesta sessão (BDB verbete 4612/4616, BDAG verbetes ἱλάσκομαι/
      ἱλασμός/ἱλαστήριον/ἐξιλάσκομαι, NA28 Rm 1.18/1.24/1.26 e as seis
      ocorrências da tríade, Milgrom, Stott, Packer, HillJames)
- [x] Nenhuma afirmação sobre Calvino, Travis ou Cremer foi feita sem
      declarar a ausência da fonte primária (Regra 13 do `CLAUDE.md`)
- [x] Um achado sobre o próprio ferramental do projeto (`dossie.py`)
      foi registrado com honestidade, não escondido

---

## 5. Recomendação de próxima ação

1. Registrar formalmente, em `_artifacts/sentinelas_HILAS.md`, a
   observação sobre `dossie.py --listar` não normalizar grego (Prompt 6)
   — como nota de uso, não necessariamente como sentinela numerada.
2. Priorizar a aquisição de Travis e do artigo de Nicole (1955) — os
   dois itens de maior recorrência nas lacunas declaradas entre os 12
   prompts e as quatro unidades.
3. Considerar se Calvino e Cremer entram no escopo do Círculo C5
   (História da Interpretação) antes de tentar fechar R6/R4 com mais
   profundidade.
4. Com a Fase 1 e a Fase 2 completas, o projeto está pronto para a Fase
   3 (síntese doutrinal e homilética) ou para a execução da estratégia
   de mídia NotebookLM.
