# CLAUDE.md — Projeto Hilas (ἱλαστήριον · ἱλασμός · ἱλάσκομαι)

> **Leia este arquivo inteiro antes de qualquer ação.** É o mapa de tudo.
> Gerado em 27/09/2026, adaptado do molde de pesquisa exegética (ver
> `ANATOMIA_DO_MOLDE.md`) para um recorte **lexical-temático**, não um livro.

---

## 0. TL;DR — Retomada em 90 segundos

> ### ⛔ REGRA ZERO, antes de qualquer redação
>
> **Jamais equiparar a leitura que esvazia a ira de Deus (propiciação como
> mero "processo impessoal") à leitura que a mantém pessoal e judicial.**
> Quando divergirem, a leitura que dissolve a ira em consequência automática
> do pecado — sem sujeito ofendido — é **objeção a ser refutada**, com base
> lexical, veterotestamentária e histórica — nunca "uma leitura possível
> entre outras".
>
> **Isto não é ataque a um autor: é o próprio objeto do projeto.** As três
> palavras existem porque **C. H. Dodd (1931, 1935)** argumentou que, no
> grego bíblico, o grupo ἱλασκ- não significa "propiciar" (aplacar alguém),
> mas "expiar" (remover algo) — e que por isso a ira de Deus, onde aparece,
> é processo despersonalizado, não reação pessoal. **Representar essa tese
> com precisão é dever do item (2) do padrão de cinco (ver §2-B); refutá-la
> sem espantalho é o projeto inteiro.**
>
> **Detalhe e padrão de cinco itens: §2-B.**

> ### 🔁 DUPLA CHECAGEM ANTI-FALHA (herdada do molde, ver `_LOG_EXECUCAO.md` do
> projeto-origem — oito falsos negativos lá registrados, todos por checagem única)
>
> **Nenhuma afirmação de ausência vale com uma única verificação.** "Não há
> fonte primária de X", "o léxico não registra Y", "nenhum comentário trata
> disso" — sempre dois métodos independentes antes de afirmar ao usuário:
>
> | Método | O que ele NÃO enxerga |
> |---|---|
> | consulta a IA/RAG sobre o acervo | o que o retrieval não recuperou |
> | `grep`/busca de conteúdo no `.md`/PDF em disco | OCR corrompido; grego como imagem |
> | listagem de arquivos (`ls`) | obra dentro de coletânea, sem nome no título |
> | conferência do léxico primário (BDAG, TDNT, LSJ) | tradução de segunda mão que já filtrou o problema |
>
> **Combinação mínima:** um método de conteúdo + um método de léxico/fonte
> primária. `ls` sozinho nunca basta. Uma paráfrase de dicionário de bolso
> nunca basta onde BDAG/TDNT/LSJ estão disponíveis.

> ### 🔒 FRONTEIRA — rótulo e clausura
>
> **Rótulo do projeto: `HILAS`.** Escopo fechado nos dois sentidos: (1) o
> projeto não empresta fontes de outros projetos temáticos sem que a obra
> seja **copiada primeiro** para `biblioteca/` (o ato de cópia é o ato de
> entrada — depois dele a proveniência de origem deixa de importar, mas
> **fica registrada** em `CURADORIA_FONTES_HILAS.md`); (2) nenhuma sessão
> escreve fora de `fase1-introducao/saidas/`, `fase2-unidades/*/saidas/` sem
> que a trava de sentinela (§4) esteja satisfeita.

**Projeto:** pesquisa exegética e lexicográfica de **ἱλαστήριον / ἱλασμός /
ἱλάσκομαι** — o grupo de palavras que o NT usa para a obra de Cristo na cruz
em relação ao pecado e à ira de Deus (tradicionalmente "propiciação"; a
tradução do grupo é, ela mesma, o objeto do estudo).
**Rótulo:** `HILAS`
**Pasta:** raiz deste repositório
**Biblioteca:** `biblioteca/` — única origem legítima de fontes primárias e
secundárias (PDFs, `.md`, `.txt`)
**Idiomas originais:** grego (NT e LXX) — hebraico (TM, para o pano de fundo
de כפר/כפרת) — alemão e inglês para a literatura secundária central
(Büchsel, Ritschl, Dodd, Morris, Nicole, Stott, Travis)

> ⚠️ **Este projeto não é de um livro nem de um capítulo.** É lexical: três
> lexemas cognatos, ~20 ocorrências no NT, um fundo de dezenas na LXX. A
> unidade de trabalho não é "capítulo", é **lexema** (Unidades 01–03) mais
> uma **síntese teológica** (Unidade 04). Onde documentação herdada do molde
> disser "capítulo", leia **unidade**; onde disser "livro", leia **lexema**.

---

## 1. ARQUITETURA

| Fase | Escopo | Notebook/dossiê | Entregável |
|---|---|---|---|
| **1** | Fundamentos: LSJ/BDAG/TDNT, LXX (כפר), história pré-Dodd, o debate Dodd↔Morris↔Nicole, teologia sistemática da propiciação | 1 dossiê | 12 saídas + relatório consolidado |
| **2** | Exegese lexema a lexema (3) + síntese (1) | 1 por unidade | 1 relatório por unidade |
| **3** | Síntese doutrinal e homilética | reaproveita a U04 | Relatório completo |

### As 4 unidades

| # | Unidade | Textos-chave | Pergunta que decide |
|---|---|---|---|
| **U01** | ἱλαστήριον | Rm 3.25 · Hb 9.5 (cf. LXX Êx 25.17-22; Lv 16.2,13-15) | substantivo ("propiciatório", o *kapporet*) ou adjetivo substantivado ("sacrifício propiciatório")? A alusão é ao mobiliário do Dia da Expiação ou ao *sentido* de sacrifício, sem o móvel em vista? |
| **U02** | ἱλασμός | 1Jo 2.2 · 1Jo 4.10 (cf. LXX Nm 5.8; Sl 129.4 [130.4 TM]; Ez 44.27) | a construção περί + genitivo ("propiciação **a respeito** dos pecados" — não genitivo objetivo puro, correção registrada em `fase2-unidades/U02_hilasmos/saidas/RELATORIO_U02.md` §1) remove pecado (expiação, Dodd) ou aplaca ira (propiciação, Morris/Nicole)? O alcance — "não somente pelos nossos, mas pelos de todo o mundo" (1Jo 2.2) — é universal em extensão ou em oferta? |
| **U03** | ἱλάσκομαι (verbo) | Lc 18.13 · Hb 2.17 (cf. LXX Gn 32.20; Êx 32.14; Sl 24.11 [25.11]; 78.9 [79.9]) | o uso em Lc 18.13 (oração do publicano) é evidência de "seja propício" pessoal-relacional, contra a leitura de Dodd de processo impessoal? Hb 2.17 (ligado a "sumo sacerdote... para expiar", εἰς τὸ ἱλάσκεσθαι) fecha o círculo cultual |
| **U04** | Síntese: ira, sacrifício, substituição | Rm 1.18; 3.21-26 como painel completo · relação com καταλλαγή (reconciliação) e ἀπολύτρωσις (redenção) | a ira de Deus é pessoal e o sacrifício a satisfaz, ou é processo impessoal que o sacrifício apenas neutraliza? **A resposta da linha editorial: pessoal, judicial, satisfeita objetivamente — ver Regra Zero** |

**O dossiê de síntese (U04) não recebe os PDFs.** Recebe os relatórios já
auditados das U01–U03 — mesma razão do molde: os rótulos de certeza
sobrevivem; com poucas fontes curtas o retrieval alcança tudo; é onde a
coerência transversal (as três palavras dizem a mesma coisa?) aparece.

---

## 2. ESTRUTURA DE PASTAS

```
hilas/
├── CLAUDE.md                        ← este arquivo
├── MEMORIA_PROJETO.md               ← estado e próxima ação
├── ESCOPO_HILAS.md                  ← delimitação, eixos de decisão, círculos
├── FASE_0_CHECKLIST.md              ← do zero ao primeiro relatório
├── LACUNAS_REFUTACAO.md             ← pauta de refutação (objeções a cobrir)
├── CURADORIA_FONTES_HILAS.md        ← tiers da biblioteca
├── _LOG_EXECUCAO.md                 ← histórico técnico, decisões, armadilhas
├── ANATOMIA_DO_MOLDE.md             ← o método herdado e o que é agnóstico
│
├── _artifacts/
│   ├── sistema_erudito.md           ← protocolo anti-alucinação
│   ├── sentinelas_HILAS.md          ← 🚩 armadilhas factuais — rascunho a verificar
│   ├── escala_certeza.md            ← os 6 níveis de certeza
│   └── persona_notebooklm.txt       ← persona para consulta a IA/RAG
│
├── _scripts/                        ← automação local (ver §5)
├── biblioteca/                      ← PDFs, .md, .txt das fontes
├── fase1-introducao/
│   ├── prompts_HILAS.md
│   └── saidas/                      ← 01..12 + relatório
└── fase2-unidades/
    ├── _TEMPLATE/
    ├── U01_hilasterion/saidas/
    ├── U02_hilasmos/saidas/
    ├── U03_hilaskomai/saidas/
    └── U04_sintese/saidas/
```

---

## 2-B. LINHA EDITORIAL

O relatório é obra confessional de nível acadêmico, na tradição de Leon
Morris, Roger Nicole, John Stott e D.A. Carson. Não é exposição neutra entre
"propiciação" e "expiação" como se fossem estilos equivalentes de tradução.

### A regra do desnível (não negociável)

**A ira de Deus é pessoal, e o sacrifício de Cristo a satisfaz objetivamente
— não apenas remove uma mancha ou neutraliza um processo impessoal.** Onde a
leitura de Dodd (e seus herdeiros — RSV 1946, muitos comentários
pós-1950) divergir desse eixo, ela é **objeção a ser respondida**, nunca
"tradução alternativa igualmente legítima".

### O padrão da refutação: cinco itens

| # | Exigência | O que reprova |
|---|---|---|
| 1 | **Fonte primária citada**, localizável | resumo de resumo — citar Dodd de segunda mão |
| 2 | **A melhor versão** do argumento de Dodd | espantalho ("Dodd nega que Deus se ira") |
| 3 | **Ataque ao pressuposto** — o que Dodd assume sobre o uso da LXX de כפר | responder só a conclusão sem tocar a base filológica |
| 4 | **Ancoragem tripla:** uso lexical (LXX/NT) · contexto veterotestamentário (culto, Dia da Expiação) · recepção (Morris 1955, Nicole 1955, Stott, Carson) | só autoridade sem os outros dois |
| 5 | **Desfecho explícito** | terminar em "ambas as traduções são possíveis" |

**Sem espaço para os cinco itens, não se abre a objeção.**

### Exceções (o que NÃO viola a regra do desnível)

1. **Aliado que parece adversário.** Autores que preferem traduzir por
   "expiação" por razões de recepção do termo em inglês/português (a palavra
   soa como magia pagã para leitor moderno), **mas mantêm a ira pessoal e a
   substituição penal** — não são a mesma posição de Dodd. Exemplo a
   verificar: alguns usos de "expiatory sacrifice" em comentaristas
   conservadores recentes. **Rotular a diferença, não tratá-los como Dodd.**
2. **Ressalva legítima sobre o mobiliário do Templo.** Discutir se
   ἱλαστήριον em Rm 3.25 evoca ou não o *kapporet* concreto é questão
   filológica interna, não concessão à tese de Dodd sobre o sentido geral do
   grupo lexical. As duas perguntas são independentes.
3. **Lacuna real — declarar, não preencher.** Se o corpus não tiver fonte
   primária para um lado de um subdebate (p.ex. a réplica alemã pré-Dodd),
   declarar a lacuna.

### Deep Research: pauta obrigatória de refutação

Toda pesquisa nova sobre um destes lexemas abre com: **qual é a leitura de
Dodd/seus herdeiros para este texto específico, e quem responde?**
Ver `LACUNAS_REFUTACAO.md`.

---

## 3. PROTOCOLO DE SESSÃO

**Início:**
```bash
python3 _scripts/checagem_retomada.py
```

**Durante:**
- **Máximo 4 investigações exegéticas por sessão** — evita truncamento de contexto.
- Antes de qualquer alegação de ausência: `python3 _scripts/dossie.py "<termo>" --listar` (custo zero, só conta).
- Rótulos de certeza obrigatórios em toda afirmação (ver `_artifacts/escala_certeza.md`).
- Conferir `_artifacts/sentinelas_HILAS.md` antes de fechar qualquer unidade.

**Fim:** atualizar `MEMORIA_PROJETO.md` ("Próxima ação") e `_LOG_EXECUCAO.md`
a cada sessão que muda o estado — não só quando alguém notar o atraso.

---

## 3-B. AS REGRAS QUE CUSTARAM CARO (herdadas do molde, aplicáveis aqui)

**Regra 11 — RAG/IA para descobrir, fonte primária para conferir.**
Se a obra existe em disco, ler o arquivo em vez de confiar só na memória do
assistente ou num resumo de terceira mão. A consulta **confirma presença,
nunca estabelece ausência**.

**Regra 12 — o nome do arquivo não é evidência de autoria.** Conferir o
frontmatter e a página de créditos antes de citar (a classe de erro que
custou 16 atribuições falsas no projeto de origem: um PDF de Stephenson
distribuído com nome trocado por conter um capítulo inteiro sobre outro
autor).

**Regra 13 — não caricaturar Dodd por citação de segunda mão.** O artigo
original é Dodd, C.H., *"IΛΑΣΚΕΣΘΑΙ, its Cognates, Derivatives, and Synonyms
in the Septuagint"*, **Journal of Theological Studies 32 (1931), pp.
352-360**, e o capítulo em *The Bible and the Greeks* (1935). **Localizar e
ler o argumento no próprio Dodd antes de resumi-lo** — muita literatura
secundária resume a tese de forma já achatada em direção ao espantalho.

**Regra 14 — כפר no TM não tem consenso etimológico fechado.** As três
hipóteses correntes (cobrir, a partir do árabe *kafara*; apagar/remover,
Levine; resgatar/pagar resgate, Gese-Janowski) **coexistem na literatura
recente**. Escolher uma como "a" etimologia sem rótulo de certeza reprova a
Regra Zero pelo item 3 (ataque ao pressuposto exige saber qual é o
pressuposto real, não o simplificado).

---

## 4. SENTINELAS FACTUAIS

Ver `_artifacts/sentinelas_HILAS.md`.

🚩 **Enquanto aquele arquivo estiver com sentinelas só em rascunho (fora da
tabela contada), nenhuma unidade pode ser dada por fechada** — mesma lógica
do molde: migrar rascunho para a tabela oficial é o ato de dar por
verificado, e isso só acontece depois da consulta de verificação.

**Estado em 27/09/2026: 10 rascunhos (R1–R10), 0 na tabela oficial — trava
ativa, intencional.**

---

## 5. SCRIPTS

| Script | O que faz |
|---|---|
| `_scripts/checagem_retomada.py` | consistência do projeto + relatório de retomada |
| `_scripts/dossie.py` | varre `biblioteca/` por termo, emite dossiê pequeno (autor, arquivo, trecho) — `--listar` só conta, custo zero |
| `_scripts/verificar_sentinelas.py` | conta linhas da tabela oficial de sentinelas; exit 0 pronto · 1 incompleto · 2 vazio · 3 ausente |
| `_scripts/conferir_citacoes.py` | audita toda citação `Autor, p. N` das saídas contra o disco |
| `_scripts/verificar_fronteira.py` | confirma que toda fonte citada está dentro de `biblioteca/` |

**Hook local (`.claude/settings.json`):** `PreToolUse` em `Write|Edit` chama
`hook_sentinelas.py`, que filtra pelo `file_path` do próprio payload do
hook — só roda `verificar_sentinelas.py` quando o alvo é
`fase1-introducao/saidas/*` ou `fase2-unidades/*/saidas/*`; fora disso
(CLAUDE.md, scripts, este arquivo) passa livre. Vazio bloqueia (exit 2),
incompleto avisa e passa, pronto fica em silêncio.

**`buscar_grego.py` — obrigatório para qualquer busca em grego.** Testado
nesta sessão contra grego em normalização Unicode mista (NFC/NFD) — o
mesmo defeito que produziu um falso negativo real no projeto-irmão
`Dikaiosyne Theou` (sentinela S20/R11). Busca literal por forma acentuada
em grego está **proibida**; toda consulta lexical passa por este script.

---

## 6. FONTES — estado em 27/09/2026

Ver `CURADORIA_FONTES_HILAS.md`. **Biblioteca vazia no momento da geração
deste projeto** — a Fase 0 começa pela aquisição das obras Tier S (ver
pauta em `ESCOPO_HILAS.md` §8).

---

## 7. PRÓXIMA AÇÃO

Ver `FASE_0_CHECKLIST.md` e `MEMORIA_PROJETO.md`.

---

*Este arquivo substitui qualquer chat anterior como fonte de verdade.*
