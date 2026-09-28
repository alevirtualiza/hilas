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
