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

| 7 | **Variante tipográfica de theta (e outras letras) pode dar falso negativo, mesmo depois de resolvido o problema de acento/NFC-NFD** | assumir que uma busca "sem acento" (R11) já é suficiente para grego robusto | **Medido nesta sessão (28/09/2026):** uma conversão própria de UBS5 grafa theta como **ϑ** (U+03D1, GREEK THETA SYMBOL) em vez de **θ** (U+03B8) padrão — `ἱλάσϑητί` (Lc 18.13) em vez de `ἱλάσθητί`. São **duas letras Unicode diferentes**, não uma letra + diacrítico — por isso NFD não resolve. `buscar_grego.py --teste` reprovava (3/4) até a correção; depois de mapear as 5 variantes "symbol" (θ/φ/π/κ/ρ) para a forma padrão, aprovou 4/4. **Regra decorrente: toda edição crítica alemã/UBS antiga merece checagem de variante de glifo antes de declarar ausência** |
| 8 | **Citação precisa de Dodd e Nicole — confirmada de forma quádrupla e independente** | misturar o artigo de Dodd (1931) com o livro (1935); confundir os dois Morris (livro de 1955 × artigo de 1951) | **Confirmado nesta sessão em quatro fontes independentes** (Morris cap. IV.a; o próprio BDAG, verbete ἱλάσκομαι, `biblioteca/BDAG_Greek_English_Lexicon_NT.md`; e agora Stott, `biblioteca/Stott_The_Cross_of_Christ.md`): Dodd, *JTS* 32 (1931), pp. 352-360 — o artigo original, **hoje disponível** como capítulo V ("Atonement") de *The Bible and the Greeks* (1935), **também já no projeto** (`biblioteca/Dodd_-_The_Bible_and_the_Greeks_texto.md`). Nicole, *WTJ* 17 (1955), pp. 117-157 — citação **idêntica** em Morris, BDAG **e** Stott; ainda não localizado o texto integral do artigo. **Achado novo:** há um **terceiro texto de Morris**, mais antigo e distinto do livro de 1955 — Leon Morris, *Expository Times* 62 (1951), pp. 227-233 — também ainda não localizado |

| 9 | **Grego "cifrado" (fonte-símbolo corrompida) é uma terceira classe de falha, distinta de imagem (sentinela 6/Wenham) e de variante de glifo (sentinela 7)** | tratar `buscar_grego.py` retornando 0 como prova de ausência sem inspecionar o texto em busca de sequências Latin1 suspeitas | **Medido nesta sessão (28/09/2026)** em `biblioteca/HillJames_The_Glory_of_the_Atonement.md`: o PDF de origem usava uma fonte grega mapeada para codepoints Latin1; a conversão herdou o mapeamento errado como texto Latin1 genuíno — `ἱλαστήριον` virou `1XaoTrjplov`, `ἱλασμός` virou `iAaoios`/`1Xaoµ6s`. **Não é OCR, não é imagem, não é variante de glifo** — é um terceiro tipo de corrupção que nenhuma ferramenta atual detecta automaticamente. Mesmo padrão já registrado nos projetos-irmãos como "Regra 17 candidata" (Ellingworth, Cockerill). **Regra decorrente: ler uma amostra do texto à procura de maiúsculas no meio de palavra (`XQL`, `1Xa`, `iAa`) antes de aceitar grego "ausente" de um epub convertido** |

*(9 sentinelas verificadas — acima do critério de saída de 6.
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
| R7 | ✅ **MIGRADA para a tabela oficial (nº8), 28/09/2026** — ver acima. **Dodd já está no projeto na íntegra** (`biblioteca/Dodd_-_The_Bible_and_the_Greeks_texto.md`) | — | — |
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
