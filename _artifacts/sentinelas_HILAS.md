# Sentinelas factuais — Hilas (ἱλαστήριον / ἱλασμός / ἱλάσκομαι)

> **Atualizado em 27/09/2026** a partir de três documentos do projeto-irmão
> mais avançado (`Dikaiosyne Theou`, que trata a mesma tríade como parte de
> um recorte maior — δικαιοσύνη θεοῦ + sacerdócio): `PLANO_DIKAIOSYNE_THEOU.md`,
> `LOG_QUERIES.md` e `PROTOCOLO_REAPROVEITAMENTO_MD.md`. Lá, várias destas
> sentinelas **já foram conferidas contra o texto grego real** (NA28) e contra
> léxicos primários (BDAG, Thayer, Moulton-Milligan). **Isso não as torna
> verificadas aqui** — mesma regra do molde original: *"sentinela verificada
> em outro corpus não é sentinela verificada neste"* (`PROTOCOLO_REAPROVEITAMENTO_MD.md`
> §4). Mas entram como rascunho **com evidência anexada**, não mais como
> hipótese nua — a reconferência aqui é mais rápida por isso.

**Critério de saída:** 6 sentinelas migradas e verificadas. Restam como
reserva, sujeitas a poda.

---

## Tabela oficial (verificada, NESTE projeto)

*Verificação real feita em 28/09/2026: `biblioteca/NA28_Novum-Testamentum-Graece.md`
(NA28, epub original enviado pelo usuário, extraído e conferido nesta
sessão — ver `_LOG_EXECUCAO.md`). Não é mais "achado do projeto-irmão" —
é conferência própria contra a fonte primária.*

| N | Sentinela | O que não fazer | Classificação |
|---|---|---|---|
| 1 | **ἱλαστήριον em Rm 3.25 é anartro** (`ὃν προέθετο ὁ θεὸς ✝ ἱλαστήριον`) — Hb 9.5 traz o mesmo termo com artigo, referindo-se ao móvel do santuário (`τὸ ἱλαστήριον`) | tratar as duas ocorrências como univocamente a mesma referência, ou usar o anartro de Rm 3.25 para *decidir* que não há alusão ao *kapporet* | **[FATO TEXTUAL]** a diferença de artigo entre os dois versos, conferida no NA28. **[HIPÓTESE DEBATIDA]** se isso decide contra a alusão tipológica — a identificação com o *kapporet* continua sendo inferência (Manson, Morris), disputada (Deissmann: leitura adjetiva) |
| 2 | **Hb 2.17 tem "os pecados" como objeto gramatical do verbo** ἱλάσκεσθαι (`εἰς τὸ ἱλάσκεσθαι ⸂τὰς ἁμαρτίας⸃ τοῦ λαοῦ`), diferente de Lc 18.13, onde ὁ θεός é vocativo/objeto do apaziguamento (`ὁ θεός, ἱλάσθητί μοι τῷ ἁμαρτωλῷ`) | usar Hb 2.17 sozinho para provar que o NT nunca tem Deus como alvo do verbo, ignorando Lc 18.13; ou usar Lc 18.13 sozinho para negar que o verbo trate de remoção de pecado | **[FATO TEXTUAL]** ambas as regências, conferidas no NA28. **[INFERÊNCIA FORTE]** que a síntese (U04) precisa harmonizar as duas construções, não escolher uma |
| 3 | **1Jo 2.2 tem a extensão explícita** "não somente pelos nossos, mas também pelos de todo o mundo" (`οὐ περὶ τῶν ἡμετέρων δὲ μόνον ἀλλὰ καὶ περὶ ὅλου τοῦ κόσμου`), confirmada por completo no NA28 | usar essa extensão para decidir sozinha o debate lexical Dodd/Morris (propiciação × expiação), que é questão distinta da extensão do alcance | **[FATO TEXTUAL]** a oração completa, conferida no NA28. **[HIPÓTESE DEBATIDA]** entre tradições confessionais quanto ao alcance (particular × universal) — debate diferente do debate lexical central deste projeto |
| 4 | **Busca literal por grego acentuado pode dar falso negativo** — ferramenta, não achado teológico | declarar ausência de ἱλαστήριον/ἱλασμός/ἱλάσκομαι num arquivo por `grep` simples que não bata | **[DADO HISTÓRICO/OPERACIONAL]** confirmado nesta sessão: `buscar_grego.py --teste` aprovou corretamente contra o arquivo real deste projeto (`biblioteca/NA28_Novum-Testamentum-Graece.md`), inclusive num teste sintético com NFC/NFD misto. Regra: busca literal em grego acentuado é proibida — todo grep passa pelo script |

| 5 | **A tese de Dodd, no seu método real (3 passos), não é "a LXX nunca fala de aplacar"** — é uma classificação de traduções: (i) onde a LXX NÃO usa ἱλάσκομαι/cognatos para verter כפר, usa palavras de "santificar/purificar" ou "cancelar/perdoar"; (ii) onde ἱλάσκομαι/cognatos NÃO traduzem כפר, vertem palavras de "limpar do pecado" (sujeito humano) ou "ter misericórdia" (sujeito divino); (iii) onde ἱλάσκομαι/cognatos TRADUZEM כφר, a LXX não estaria pensando em "aplacar a Divindade", mas em "realizar um ato pelo qual culpa/impureza é removida" | espantalho: "Dodd nega que a Bíblia fale em ira/aplacar" sem citar o método real | **[FONTE PRIMÁRIA, via citação direta em Morris]** — Morris, *Apostolic Preaching of the Cross*, cap. IV.a "The work of C. H. Dodd" (`biblioteca/Morris_Apostolic_Preaching_of_the_Cross.md`, linhas ~5966-5990), cita Dodd literalmente nos três passos, com nota de rodapé numerada. **A crítica de Nicole também está lá, citada com precisão**: "Roger R. Nicole, num artigo importante sobre 'C. H. Dodd and the Doctrine of Propitiation', aponta que Dodd não levou em conta um grande grupo de palavras que traduzem כפר... Nicole sustenta que Dodd leva em conta não mais que 36% da evidência." Isso **confirma a existência e o conteúdo real do artigo de Nicole** (ver R7) mesmo sem o texto completo do artigo em mãos |

| 6 | **"Propiciação" e "expiação" não são duas traduções neutras da mesma palavra** — são as duas conclusões *opostas* que o próprio método de Dodd (sentinela 5) tenta decidir. Escolher uma das duas em português, ao traduzir ἱλαστήριον/ἱλασμός, já é tomar partido no debate, não uma escolha de estilo | tratar a escolha de palavra em português como estilística ou neutra | **[INFERÊNCIA FORTE]**, decorrente diretamente da sentinela 5: o próprio Dodd organiza sua evidência para concluir que o grupo ἱλασκ- na LXX significa "remover/purgar" (expiação), não "aplacar" (propiciação) — as duas palavras portuguesas **traduzem as duas teses rivais**, não a mesma coisa. Confirmado por leitura direta do método de Dodd em `biblioteca/Morris_Apostolic_Preaching_of_the_Cross.md` |

*(6 sentinelas verificadas — critério de saída atingido.
`_scripts/verificar_sentinelas.py` deve retornar exit 0 [PRONTO].)*

---

## Rascunhos — com evidência do projeto-irmão anexada

| # | Sentinela | O que NÃO fazer | Evidência já levantada (a reconferir aqui) |
|---|---|---|---|
| R1 | ✅ **MIGRADA para a tabela oficial (nº6), 28/09/2026** — ver acima | — | — |
| R2 | ✅ **MIGRADA para a tabela oficial (nº5), 28/09/2026** — ver acima, agora com o método de Dodd em 3 passos, citado literalmente via Morris | — | — |
| R3 | ✅ **MIGRADA para a tabela oficial (nº1), 28/09/2026** — ver acima | — | — |
| R4 | **A etimologia de כפר não tem consenso fechado** | escolher uma hipótese sem rótulo | Mesmo o projeto-irmão trata como disputa aberta entre *purgar* (Milgrom) e *resgatar* (Sklar), marcado `[a conferir em primária]` — nenhuma das duas dada como resolvida. **Novo dado (28/09/2026):** BDB, verbete כַּפֹּרֶת nº4616 (`biblioteca/BDB_Hebrew_Lexicon_1906_P2de3.md`), rejeita explicitamente a hipótese "cobrir/tampa" ("the older explan. 'cover, lid' has no justification in usage") — **isso é um terceiro polo na disputa**, não resolve a favor de Milgrom nem de Sklar; reforça que a etimologia é genuinamente disputada, não presume-se |
| R5 | ✅ **MIGRADA para a tabela oficial (nº3), 28/09/2026** — ver acima | — | — |
| R6 | **Não presumir que Ritschl antecipa exatamente Dodd** | citar como a mesma posição sem checar | ainda **não conferido** em nenhum dos dois projetos — permanece aberto |
| R7 | **Citação precisa de Dodd — dois textos, não um** | misturar artigo (1931) e livro (1935) | *JTS* 32 (1931), pp. 352-360 — artigo; *The Bible and the Greeks* (1935) — capítulo. **Achado do projeto-irmão (10-B item 3):** a obra de 1935 **não está no acervo disponível**; o que está, convertido e pronto, é a **nota de Dodd em *The Johannine Epistles* (Moffatt NTC)**, que expõe a mesma tese aplicada a 1Jo 2.2/4.10 — mitigação parcial, não substituição |
| R8 | **A mudança da RSV (1946) não se estende automaticamente a revisões posteriores** | afirmar "as Bíblias modernas usam expiação" sem checar edição por edição | não conferido — permanece pauta |
| R9 | **4 Macabeus 17.22 — confirmar a palavra exata** | citar de memória | não conferido — permanece pauta |
| R10 | ✅ **MIGRADA para a tabela oficial (nº2), 28/09/2026** — ver acima | — | — |

## Sentinela adicional, herdada como bug de ferramenta — crítica para este projeto

✅ **MIGRADA para a tabela oficial (nº4), 28/09/2026** — testada nesta
sessão contra o arquivo real do projeto, não só contra o achado do
projeto-irmão. Ver tabela oficial acima.

---

## Ferramenta e teste de aceitação (já herdados, ver `_scripts/buscar_grego.py`)

```bash
python3 _scripts/buscar_grego.py --teste biblioteca/<arquivo_grego>.md
```

Exige as **seis** ocorrências da tríade (ἱλαστήριον ×2, ἱλασμός ×2,
ἱλάσκομαι ×2) e sai com código 0 (aprovado) ou 1 (reprovado). **Resultado
medido no projeto-irmão, referência para quando este projeto adquirir uma
edição grega:**

| Edição | Resultado medido lá |
|---|---|
| NA28 (três cópias convertidas independentes) | ✅ 4/4 (o teste do irmão cobria 4 formas; adaptar para 6 aqui — ver script) |
| UBS5 (duas cópias) | 🔴 0/4 **reprovado e vetado** |

**Regra decorrente:** se este projeto reaproveitar ou adquirir uma conversão
de NT grego, rodar o teste **antes** de citar qualquer ocorrência — e nunca
usar uma edição UBS5 sem primeiro checar se a conversão específica passa.

---

## Oitava fonte de erro (nomeada por analogia ao molde)

**Atribuição de posição a autor num debate de várias gerações** (Ritschl →
Dodd → Morris/Nicole → Stott/Carson/Travis). Ver R2, R6.
