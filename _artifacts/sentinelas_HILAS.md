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

## Tabela oficial (verificada, NESTE projeto) — VAZIA

| N | Sentinela | O que não fazer | Classificação |
|---|---|---|---|

*(0 linhas — trava ativa por design. `_scripts/verificar_sentinelas.py`
retorna exit 2 enquanto esta tabela estiver vazia.)*

---

## Rascunhos — com evidência do projeto-irmão anexada

| # | Sentinela | O que NÃO fazer | Evidência já levantada (a reconferir aqui) |
|---|---|---|---|
| R1 | **"Propiciação" e "expiação" não são sinônimos de tradução neutra** | tratá-las como estilo, não tese | — (analítico, não depende de conferência textual) |
| R2 | **Dodd não nega a ira de Deus como conceito** | espantalho: "Dodd apaga a ira" | `LOG_QUERIES.md` DIKA-92 #4-5: a formulação correta de Dodd, extraída **da própria obra dele** (*The Johannine Epistles*, Moffatt NTC, já no acervo do projeto-irmão) é: ele distingue o **grego pagão extrabíblico** (onde aceita sentido propiciatório) do **uso bíblico** (onde nega que Deus seja objeto do verbo, preferindo expiar/purificar). Isto é o argumento real, não a versão achatada |
| R3 | **ἱλαστήριον em Rm 3.25 e Hb 9.5 não são a mesma referência sem mais** | assumir univocidade | **Conferido no NA28 em 01/09/2026** (projeto-irmão, S11): Rm 3.25 traz ἱλαστήριον **anartro** (sem artigo — `προέθετο ὁ θεὸς ἱλαστήριον`). O anartro é **dado a pesar, não a decidir** — a identificação com o *kapporet* continua sendo inferência (Manson, Morris), disputada (Deissmann: adjetivo/objeto votivo) |
| R4 | **A etimologia de כפר não tem consenso fechado** | escolher uma hipótese sem rótulo | Mesmo o projeto-irmão trata como disputa aberta entre *purgar* (Milgrom) e *resgatar* (Sklar), marcado `[a conferir em primária]` — nenhuma das duas dada como resolvida |
| R5 | **Extensão (1Jo 2.2) ≠ eficácia** | usar "todo o mundo" para decidir sozinho o debate lexical | **Conferido no NA28** (S19 do projeto-irmão): 1Jo 2.2 lê `οὐ περὶ τῶν ἡμετέρων δὲ μόνον ἀλλὰ καὶ περὶ ὅλου τοῦ κόσμου`. Lá, isto é tratado como debate **N1** (entre tradições confessionais que aceitam a mesma inerrância), com **três desfechos legítimos** (reformado, wesleyano, pentecostal), refutação **proibida** entre eles — só refutável a leitura que nega objeto pessoal (Dodd) |
| R6 | **Não presumir que Ritschl antecipa exatamente Dodd** | citar como a mesma posição sem checar | ainda **não conferido** em nenhum dos dois projetos — permanece aberto |
| R7 | **Citação precisa de Dodd — dois textos, não um** | misturar artigo (1931) e livro (1935) | *JTS* 32 (1931), pp. 352-360 — artigo; *The Bible and the Greeks* (1935) — capítulo. **Achado do projeto-irmão (10-B item 3):** a obra de 1935 **não está no acervo disponível**; o que está, convertido e pronto, é a **nota de Dodd em *The Johannine Epistles* (Moffatt NTC)**, que expõe a mesma tese aplicada a 1Jo 2.2/4.10 — mitigação parcial, não substituição |
| R8 | **A mudança da RSV (1946) não se estende automaticamente a revisões posteriores** | afirmar "as Bíblias modernas usam expiação" sem checar edição por edição | não conferido — permanece pauta |
| R9 | **4 Macabeus 17.22 — confirmar a palavra exata** | citar de memória | não conferido — permanece pauta |
| R10 | **Hb 2.17 (objeto = pecados) não decide sozinho contra Lc 18.13 (objeto = Deus)** | usar um para anular o outro | **Conferido no NA28** (S13 do projeto-irmão): Hb 2.17 lê `εἰς τὸ ἱλάσκεσθαι ⸂τὰς ἁμαρτίας⸃ τοῦ λαοῦ` — objeto **são os pecados**, com variante marcada no aparato. O argumento propiciatório para Hb 2.17 se faz **por contexto** (2.17 + Hb 9–10 + a doutrina da ira em Hebreus), **nunca pela regência sintática sozinha** |

## Sentinela adicional, herdada como bug de ferramenta — crítica para este projeto

| # | Sentinela | O que NÃO fazer | Evidência |
|---|---|---|---|
| R11 | **Busca literal por grego acentuado pode dar falso negativo** | declarar ausência de ἱλαστήριον/ἱλασμός/ἱλάσκομαι num arquivo por `grep` simples não bater | **Medido no projeto-irmão em 01/09/2026 (S20):** o `.md` de uma conversão de NA28 não estava em NFC nem NFD — normalização mista. `grep "ἱλαστήριον"` devolvia **0**; `grep "λαστ"` (sem acento) devolvia **6**, com o termo inteiro visível no contexto. **Foi falso negativo do buscador, não do acervo.** A ferramenta corretiva (`_scripts/buscar_grego.py`, ver abaixo) já existe e tem teste de aceitação embutido. **Regra decorrente: busca literal em grego acentuado é proibida neste projeto — todo grep passa por `buscar_grego.py`.** |

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
