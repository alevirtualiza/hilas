# Curadoria de fontes — Hilas

*Biblioteca vazia no momento da geração deste projeto (27/09/2026). Este
arquivo já traz, porém, o **protocolo de reaproveitamento** herdado do
projeto-irmão `Dikaiosyne Theou` e o **inventário do que ele já mediu** como
disponível ou ausente para exatamente esta tríade — para que a aquisição
comece informada, não do zero absoluto.*

## ✅ Primeira fonte real recebida e aprovada (28/09/2026)

| Arquivo | Portas | Tier | Palavras |
|---|---|---|---|
| `biblioteca/NA28_Novum-Testamentum-Graece.md` | 1 ✅ (metadado do epub: Aland, ISBN 978-3-438-07236-8) · 2 ✅ (0 imagens de alfabeto) · 3 ✅ (`buscar_grego.py --teste` aprovado, 6/6) · 4 ✅ (leitura direta das 6 ocorrências, aparato legível) · 6 ✅ | **S** | 638.153 |

Enviado pelo usuário como `.epub` original (não reaproveitado de projeto
irmão), extraído nesta sessão com `ebooklib`+`BeautifulSoup`. **Acima do
teto usual de upload ao NotebookLM (450-525 mil palavras)** — dividir com
`dividir_md.py` (a escrever) antes de subir a um caderno; para uso local
(grep, `dossie.py`, `buscar_grego.py`) o arquivo único está correto.

As seis ocorrências da tríade foram lidas integralmente nesta sessão — ver
`_artifacts/sentinelas_HILAS.md`, sentinelas 1-4 da tabela oficial, agora
**verificadas neste projeto**, não mais só "achado do projeto-irmão".

---

## ✅ Segundo lote recebido e aprovado (28/09/2026) — o núcleo do debate central

| Arquivo | Tier | Papel |
|---|---|---|
| `biblioteca/Morris_Apostolic_Preaching_of_the_Cross.md` | S | resposta clássica a Dodd — dois capítulos inteiros (V-VI) sobre propiciação, **cita Dodd e Nicole diretamente com trechos literais** |
| `biblioteca/Nicole_Our_Sovereign_Saviour.md` | S | 1Jo 2.2, extensão da propiciação — classe "só argumento" (grego quase ausente, política/OCR) |
| `biblioteca/Packer_KnowingGod.md` | S | Rm 3.24-25 e 1Jo 2.2, cap. 18 "The Heart of the Gospel" — classe "só argumento" |
| `biblioteca/Harrison_Levitico_Introducao_e_Comentario_PT.md` | A1 | **edição em português** (Série Cultura Bíblica, distinta da TNTC inglesa) — discute diretamente a etimologia de *kipper* e a tradução da LXX por ἱλαστήριον |

**Achado que fecha 2 sentinelas sozinho:** Morris, no capítulo "The work of
C. H. Dodd", cita o **método real de Dodd em 3 passos** (não a versão
achatada) com nota de rodapé, e **cita e resume o artigo de Roger Nicole,
"C. H. Dodd and the Doctrine of Propitiation"**, com a estatística exata
("Dodd leva em conta apenas 36% da evidência"). Isso confirma o conteúdo
real do artigo de Nicole mesmo sem o texto integral em mãos — ver
`_artifacts/sentinelas_HILAS.md`, sentinelas 5 e 6.

**Estado das sentinelas: 6/6 — Fase 0 (etapa de sentinelas) CONCLUÍDA.**
`verificar_sentinelas.py` retorna exit 0 [PRONTO]. A trava de escrita em
`fase1-introducao/saidas/` e `fase2-unidades/*/saidas/` está liberada.

---

## ✅ Terceiro lote recebido e aprovado (28/09/2026) — léxico hebraico

| Arquivo | Tier | Papel |
|---|---|---|
| `biblioteca/BDB_Hebrew_Lexicon_1906_P1de3.md` | S | léxico hebraico-inglês (Brown-Driver-Briggs, 1906) |
| `biblioteca/BDB_Hebrew_Lexicon_1906_P2de3.md` | S | idem — contém o verbete de כַּפֹּרֶת |
| `biblioteca/BDB_Hebrew_Lexicon_1906_P3de3.md` | S | idem |

**Achado central:** o verbete nº4616, כַּפֹּרֶת (kapporet, Strong 3727), diz
literalmente: *"propitiatory, late techn. word from כפר cover over sin:
the older explan. 'cover, lid' has no justification in usage; LXX
ἱλαστήριον"* — com a lista exaustiva de ocorrências (Êx 25, 26, 30, 31, 35,
37, 39, 40; Lv 16; Nm 7.89; 1Cr 28.11) e a descrição física do objeto
(placa de ouro com querubins, sobre a arca). **Confirma diretamente, em
léxico primário, que a LXX traduz כַּפֹּרֶת por ἱλαστήριον** — dado central
para a Unidade 01. Também rejeita a etimologia "cobrir/tampa" — um
terceiro polo na disputa da sentinela 4 (rascunho, ver `sentinelas_HILAS.md`).

---

## ✅ Quarto lote recebido e aprovado (28/09/2026) — Milgrom e UBS5

| Arquivo | Tier | Papel |
|---|---|---|
| `biblioteca/Milgrom_Leviticus1-16_P1de2.md` | S | comentário técnico máximo sobre Lv 1-16 (Anchor Yale Bible) — discussão extensa da etimologia e uso de *kipper* |
| `biblioteca/Milgrom_Leviticus1-16_P2de2.md` | S | continuação |
| `biblioteca/UBS5_The-Greek-New-Testament.md` | S | texto grego alternativo ao NA28 |

**Achado técnico importante — o veto ao UBS5 dos projetos-irmãos NÃO se
aplica a esta conversão.** Os projetos-irmãos vetaram *suas* cópias de
UBS5 (reprovadas 0/4 no teste lexical). **Esta cópia, de conversão
própria, foi testada de forma independente e reprovou por um motivo
diferente e específico**: esta edição grafa theta como **ϑ** (U+03D1,
GREEK THETA SYMBOL) em vez de **θ** padrão (U+03B8) — `ἱλάσϑητί` em Lc
18.13, não `ἱλάσθητί`. É variante tipográfica genuína da edição impressa
(comum em edições críticas alemãs/UBS antigas), não erro de OCR. **O
`buscar_grego.py` foi corrigido nesta sessão** (mapeamento das 5 letras
gregas com variante "symbol": θ/φ/π/κ/ρ) e agora aprova esta cópia
4/4 — ver sentinela 7 em `sentinelas_HILAS.md`.

**Regra prática:** o veto documentado a "UBS5" nos projetos-irmãos vale
para as cópias *deles*, não para toda e qualquer conversão de UBS5 —
cada conversão precisa do próprio teste, nunca herdar veto por nome de
edição.

**Milgrom — ressalva de leitura (Regra 11-B):** o texto tem ocasionalmente
palavras fundidas com fragmentos de nota de rodapé (ex. "kipper
o'pffuerrgien'g" no lugar de "kipper 'purge'... [nota]"), típico de PDF
denso em duas colunas. O argumento continua recuperável com atenção; não
copiar trecho colado sem reler o contexto.

---

## ✅ Quinto lote recebido e aprovado (28/09/2026) — Dodd, BDAG, Wenham

**A lacuna mais importante do projeto está fechada: Dodd na íntegra.**

| Arquivo | Tier | Papel |
|---|---|---|
| `biblioteca/Dodd_-_The_Bible_and_the_Greeks_texto.md` | S | **fonte primária do adversário** — cap. V "Atonement" é o próprio ensaio de 1931 (*JTS* 32), com o método completo de classificação das traduções da LXX, grego real de alta densidade |
| `biblioteca/BDAG_Greek_English_Lexicon_NT.md` | S | léxico grego primário — verbetes de ἱλάσκομαι/ἱλασμός/ἱλαστήριον citam a bibliografia acadêmica exata do debate, de forma independente |
| `biblioteca/Wenham_Leviticus_NICOT.md` | A1 (SEM FORMA ORIGINAL) | comentário técnico de Levítico — hebraico/grego preservados como imagem (mesmo padrão já medido em `Wenham_Genesis_1-15_WBC` nos projetos-irmãos); usar só o argumento |

**Achado que fecha a sentinela 8 (citação de Dodd/Nicole) com tripla
confirmação independente:** o BDAG cita, no próprio verbete de
ἱλάσκομαι, a bibliografia exata do debate — `CDodd, JTS 32, '31, 352-60`
(o artigo original), `LMorris, ET 62, '51, 227-33` (**um terceiro texto de
Morris, mais antigo, ainda não localizado — distinto do livro de 1955**),
`RNicole, WTJ 17, '55, 117-57` (confirma as páginas exatas do artigo,
ainda não localizado na íntegra), e ainda `TManson, JTS 46, '45, 1-10`
(a leitura de ἱλαστήριον como "lugar de propiciação" em Rm 3.25, contra a
qual Breytenbach 1989 argumenta) — **material direto para a Unidade 01**
sobre a disputa Manson × Breytenbach.

**Item (1) e (2) do padrão de refutação estão agora satisfeitos na
íntegra para Dodd** — não mais mitigação parcial via citação em Morris,
mas o próprio texto primário do adversário, disponível para leitura
direta e citação exata.

---

## ✅ Sexto lote recebido e aprovado (28/09/2026) — Stott e Hill/James (Carson)

| Arquivo | Tier | Papel |
|---|---|---|
| `biblioteca/Stott_The_Cross_of_Christ.md` | S | síntese pastoral-acadêmica clássica — confirma a citação de Nicole pela **quarta vez**, de forma independente |
| `biblioteca/HillJames_The_Glory_of_the_Atonement.md` | S | contém o capítulo de **D. A. Carson**, "Atonement in Romans 3:21-26" — item da pauta de aquisição fechado; **também contém citação direta em alemão de Ritschl** (*Die christliche Lehre von der Rechtfertigung und Versöhnung*, 1889, 1.217 e outras) e sua classificação explícita como teórico da influência moral/subjetiva — avança a sentinela R6 (30/09/2026), ver `_artifacts/sentinelas_HILAS.md` |

**Stott** trata Dodd, Morris, Nicole e Büchsel (TDNT) com precisão —
inclusive um dado novo: Büchsel aponta que 1 Clemente e o Pastor de
Hermas usam ἱλάσκομαι claramente para propiciar Deus, algo que Dodd não
considerou. Bibliografia de Dodd também confirmada: *The Bible and the
Greeks* (Hodder & Stoughton, 1935) e *The Epistle of Paul to the Romans*
(Moffatt NTC, 1932).

**Hill & James** — o livro é **dedicado a Roger Nicole** ("A Tribute to
Roger Nicole" por Timothy George). O capítulo 6 de Carson discute
diretamente Rm 3.21-26. ⚠️ **Achado técnico:** o grego neste arquivo está
**cifrado**, não ausente — mapeamento de fonte-símbolo corrompido durante
a conversão do epub (`1XaoTrjplov` no lugar de ἱλαστήριον, `iAaoios` no
lugar de ἱλασμός) — o mesmo padrão já medido em Ellingworth/Cockerill nos
projetos-irmãos ("Regra 17 candidata"). **Nunca citar forma grega exata
deste arquivo** — só o argumento em inglês, que está intacto e é rico
(discussão extensa de Dodd × Nicole sobre 1Jo 2.2, incluindo o comentário
de I. Howard Marshall).

---

## ✅ Sétimo lote recebido e aprovado (28/09/2026) — Caragounis (quinta confirmação)

| Arquivo | Tier | Papel |
|---|---|---|
| `biblioteca/Caragounis_Expiation-Propitiation-Reconciliation.md` | S | artigo moderno (2020), filólogo grego (Lund University) — grego real de alta qualidade, sempre com transliteração |

**(Duplicata descartada:** um segundo envio de `Stott_The_Cross_of_Christ.epub`
tinha SHA-256 idêntico ao já processado — não reprocessado.)

**Caragounis é a fonte mais precisa do projeto até agora sobre a
bibliografia do debate** — dá o **título completo** do artigo de Dodd:
"Ἱλάσκεσθαι, its cognates, derivatives and synonyms in the Septuagint",
*JTS* 32 (1931), pp. 352-360, confirma que foi reimpresso como capítulo 5
("Atonement") de *The Bible and the Greeks*, e cita ainda Dodd, *The
Epistle to the Romans* (Moffatt NTC, 1932), *ad loc*. **Quinta
confirmação independente** da citação de Nicole (*WTJ* 17, 1955, pp.
117-157). Acrescenta dois dados novos: **Cranfield** também criticou Dodd
("failed to pay adequate attention to the context"), e a referência exata
de **Büchsel em TDNT vol. III, p. 311f** (ainda não localizado na íntegra,
mas agora com paginação exata para busca dirigida).

---

## 1. O protocolo de seis portas (herdado de `PROTOCOLO_REAPROVEITAMENTO_MD.md`)

Se este projeto reaproveitar um `.md` já convertido de outro projeto (em vez
de converter do PDF/EPUB original), a obra passa pelas seis portas **nesta
ordem** — a primeira que reprovar, para, em vez de seguir no escuro:

| Porta | O que checa | Reprova quando |
|---|---|---|
| **1 — identidade pelo miolo** (Regra 12) | autor e obra pelo **conteúdo**, não pelo nome do arquivo | frontmatter com `Usuario`/`Unknown`; nome de arquivo divergente do miolo |
| **2 — alfabeto como imagem** (Regra 15) | `grep -c '!\[\](images/' <arquivo>.md` deve ser 0 | qualquer ocorrência — obra entra com marca `SEM FORMA ORIGINAL` (usa-se o argumento, nunca a forma grega/hebraica citada dela) |
| **3 — teste lexical grego** (Regra 16, este projeto) | `python3 _scripts/buscar_grego.py --teste <arquivo>.md` deve aprovar | qualquer contagem abaixo do mínimo — falso negativo do buscador ou defeito real de OCR |
| **4 — sanidade do corpo** (Regra 11-B/13) | ler uma página do **miolo** (não a abertura) | caracteres alternando entre frases; palavras impossíveis no idioma; nota intercalada no corpo |
| **5 — aviso de limitação no corpo** | toda obra reprovada parcial na Porta 2 ou 4 recebe `<!-- AVISO-OCR-INICIO -->` no corpo do `.md` | — |
| **6 — tier e cobertura, decididos AQUI** | classificar contra o escopo **deste** projeto, não copiar tier de outro | copiar tier de `Justica-de-Deus` ou `Dikaiosyne Theou` sem reclassificar |

**Regra permanente:** *o que se herda é o arquivo; o julgamento, nunca.*
Nenhum tier, sentinela verificada ou trecho citado atravessa de outro
projeto sem passar pelas seis portas aqui.

---

## 2. O que já foi medido em acervos irmãos — referência para aquisição

*Estas obras não estão em `biblioteca/` deste projeto. A tabela documenta
o que o projeto-irmão `Dikaiosyne Theou` já testou, para que a aquisição
aqui comece sabendo o que vale a pena buscar primeiro e o que já provou ser
armadilha.*

### Fontes de texto grego — resultado do teste lexical (Porta 3)

| Fonte | Resultado medido lá | Ação aqui |
|---|---|---|
| NA28 (conversão a partir de epub, três cópias independentes) | ✅ aprovado — grego íntegro, todas as ocorrências recuperáveis com `buscar_grego.py` | preferir esta edição se/quando adquirida |
| UBS5 (duas cópias) | 🔴 **reprovado e vetado** — perde 5 das 6 ocorrências da tríade | não usar sem reconversão testada |

### Léxicos — resultado do teste (Portas 1-4)

| Léxico | Resultado medido lá |
|---|---|
| **BDAG** (Bauer-Danker-Arndt-Gingrich) | ✅ aprovado com ressalva — verbete de ἱλαστήριον legível e correto (cita Rm 3.25, Hb 9.5, discute "expiation"/"propitiatory"), mas o PDF de origem é em colunas densas e por vezes emenda trecho de uma entrada à vizinha. **Conferir cada citação isolada antes de usar em prosa** |
| **Thayer**, *Greek-English Lexicon of the NT* (1889) | ✅ aprovado — 29 ocorrências de `ιλασ`, grego íntegro; ruído de OCR típico de 1889 em palavras inglesas ao redor (não no grego) |
| **Moulton-Milligan**, *Vocabulary of the Greek Testament* (1914) | ✅ aprovado — 33 ocorrências de `ιλασ`, grego íntegro; base documental em papiros não-bíblicos, valiosa para o Círculo 4 (uso extrabíblico) |
| **Abbott-Smith**, *Manual Greek Lexicon* (1922) | 🔴 reprovado — grego saiu corrompido pelo OCR (`ἐξιλάσκομαι` → `e&iAdoxopa`); precisa reconversão testada antes de qualquer uso |
| **Robertson**, *Grammar of the Greek NT* (1914) | 🔴 reprovado — mesmo defeito (`ἱλαστήριον` → `iKaariiputv`) |

### Achado adicional (projeto-irmão `Tabernáculo`) — Harrison sobre Levítico já discute a etimologia

**R. K. Harrison, *Levítico* (TNTC), re-OCR concluído** — traduz sistematicamente
o vocabulário sacrificial (`nepes`, `hatta't`, `kippurim`, `kappōret`) e **discute
diretamente a etimologia de kipper e a tradução de ἱλαστήριον na LXX** (dado
relevante às sentinelas R1/R4 deste projeto). Classe "só argumento" — 0
hebraico/grego por política editorial da série Tyndale, não falha de OCR;
usar a posição do autor, nunca citar dele a forma exata sem conferir o
original. Candidato de apoio para a Unidade 01.

### A literatura do debate central

> ✅ **Atualização (achado do projeto-irmão `Tabernáculo`, caderno
> `TAB-95-TRIADE-HILASMOS`, criado em 11/09/2026 por pedido explícito do
> dono daquele projeto para sustentar exatamente este mesmo debate):** as
> **quatro fontes centrais já estão convertidas e testadas** em `.md`,
> reaproveitáveis por este projeto via as seis portas de `§1`. Isto muda a
> prioridade de aquisição — de "localizar e comprar" para "reaproveitar e
> reconferir".

| Obra | Estado medido lá | Arquivo (se reaproveitado) |
|---|---|---|
| **Morris**, *The Apostolic Preaching of the Cross* (1955) | ✅ localizado, convertido, `ready` em `TAB-95` | `Morris - The Apostolic Preaching of the Cross (texto).md` |
| **Dodd**, *The Bible and the Greeks* (1935) — **o próprio ensaio de 1931 sobre ἱλάσκεσθαι na LXX, incluído neste volume** | ✅ **localizado e convertido, com grego real preservado** — deixa de ser a lacuna prioritária que este documento registrava antes. Fonte primária do adversário, item (1) do padrão, **satisfeita** | `Dodd - The Bible and the Greeks (texto).md` |
| **Dodd**, nota sobre ἱλασμός em *The Johannine Epistles* (Moffatt NTC) | localizado e convertido (achado anterior, via `Dikaiosyne Theou`) — expõe a tese aplicada diretamente a 1Jo 2.2/4.10 | (ver entrada anterior deste documento) |
| **Nicole**, ***Our Sovereign Saviour*** | ✅ **localizado e convertido** (re-OCR próprio do projeto-irmão) — discute 1Jo 2.2 e a extensão da propiciação. **Nota bibliográfica:** este é um livro diferente do artigo "C. H. Dodd and the Doctrine of Propitiation" (*WTJ* 17, 1955) citado em `ESCOPO_HILAS.md` §8 — **os dois títulos de Nicole não devem ser confundidos**; o artigo de periódico permanece não localizado | `Nicole_Our_Sovereign_Saviour.md` |
| **J. I. Packer**, *Knowing God* — cap. "The Heart of the Gospel" | ✅ localizado — o capítulo discute Rm 3.24-25 e 1Jo 2.2 diretamente. Título bibliográfico completo confirmado (não é *In My Place Condemned He Stood*, como uma nota anterior deste documento supunha) | `TAB-95`, quarta fonte |
| Nicole, "C. H. Dodd and the Doctrine of Propitiation" (*WTJ* 17, 1955), o **artigo** | 🔴 ainda não localizado — distinto do livro acima, permanece prioridade menor (o livro já cumpre o item 1 do padrão) |

### Comentários técnicos que fecham a "espinha verso-a-verso" cultual

| Obra | Estado |
|---|---|
| Comentário técnico de **Levítico** (Milgrom AB / Wenham NICOT / Hartley WBC / Sklar) | 🔴 **ausente em todos os acervos irmãos verificados** — trava direta da Unidade 01 (Rm 3.25 remete a Lv 16) |
| Comentário técnico de **Hebreus** (Lane WBC / Attridge Hermeneia / Cockerill NICNT / Ellingworth NIGTC) | 🔴 ausente — só existem volumes de divulgação |
| Wenham, *Genesis 1-15* (WBC) | localizado, **mas com hebraico preservado como imagem** (Porta 2 reprova parcial — 950 palavras-imagem) — usar o argumento, não citar a forma hebraica dele diretamente |

---

## 3. Tiers deste projeto (a preencher conforme a biblioteca receber arquivos)

| Tier | Critério |
|---|---|
| S | os textos-fonte gregos/hebraicos e os léxicos primários (NA28/Rahlfs, BDAG, LSJ, TDNT, Louw-Nida) + as obras centrais do debate (Dodd, Morris, Nicole) |
| A1 | crítica acadêmica de peso sobre os textos específicos (comentários técnicos de Romanos, Hebreus, 1João, Levítico) |
| A2 | patrística, medieval, Reforma sobre estes textos especificamente |
| B | monografias temáticas (Stott, Carson, Travis, teologias sistemáticas) |
| C | pastorais e introduções |
| D | sai — sem valor exegético para este recorte específico |

*(vazia até a primeira aquisição — ver `ESCOPO_HILAS.md` §8 para a pauta)*

---

## Próximo passo

1. ~~Adquirir ou localizar Dodd 1931/1935 e Nicole 1955~~ — **superado**:
   Dodd (*The Bible and the Greeks*, com o ensaio de 1931) e Nicole (*Our
   Sovereign Saviour*) já estão convertidos no caderno `TAB-95` do
   projeto-irmão `Tabernáculo`. Reaproveitar, não adquirir do zero.
2. Se este projeto tiver acesso aos acervos irmãos, reaproveitar NA28
   (não UBS5), BDAG, Thayer, Moulton-Milligan, a nota de Dodd em
   *The Johannine Epistles*, e as quatro fontes de `TAB-95` (Dodd, Morris,
   Nicole, Packer) — todas já aprovadas nas seis portas ou pré-testadas lá,
   pendente apenas de reconferência aqui (Porta 6, tier próprio).
3. Não copiar tier, sentinela verificada ou trecho citado de nenhum
   projeto irmão sem passar pelas seis portas.
4. O artigo de periódico de Nicole (*WTJ* 17, 1955) — distinto do livro
   *Our Sovereign Saviour* — continua sendo a única peça do núcleo
   bibliográfico genuinamente ausente em todos os acervos irmãos
   verificados. Prioridade de aquisição rebaixada, mas não fechada.
