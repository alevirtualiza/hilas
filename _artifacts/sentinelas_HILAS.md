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

*(4 sentinelas verificadas — 2 abaixo do critério de saída de 6.
`_scripts/verificar_sentinelas.py` deve retornar exit 1 [INCOMPLETO], não
mais exit 2 [VAZIO].)*

---

## Rascunhos — com evidência do projeto-irmão anexada

| # | Sentinela | O que NÃO fazer | Evidência já levantada (a reconferir aqui) |
|---|---|---|---|
| R1 | **"Propiciação" e "expiação" não são sinônimos de tradução neutra** | tratá-las como estilo, não tese | — (analítico, não depende de conferência textual) |
| R2 | **Dodd não nega a ira de Deus como conceito** | espantalho: "Dodd apaga a ira" | `LOG_QUERIES.md` DIKA-92 #4-5: a formulação correta de Dodd, extraída **da própria obra dele** (*The Johannine Epistles*, Moffatt NTC, já no acervo do projeto-irmão) é: ele distingue o **grego pagão extrabíblico** (onde aceita sentido propiciatório) do **uso bíblico** (onde nega que Deus seja objeto do verbo, preferindo expiar/purificar). Isto é o argumento real, não a versão achatada |
| R3 | ✅ **MIGRADA para a tabela oficial (nº1), 28/09/2026** — ver acima | — | — |
| R4 | **A etimologia de כפר não tem consenso fechado** | escolher uma hipótese sem rótulo | Mesmo o projeto-irmão trata como disputa aberta entre *purgar* (Milgrom) e *resgatar* (Sklar), marcado `[a conferir em primária]` — nenhuma das duas dada como resolvida |
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
