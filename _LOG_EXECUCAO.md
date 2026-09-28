# Log de execução — Hilas

*Histórico técnico: decisões, armadilhas medidas, testes rodados.*

## 1. Geração do projeto (27/09/2026)

Projeto gerado a pedido do usuário, a partir da análise de quatro
documentos de um projeto de pesquisa exegética anterior ("Justiça de
Deus", tema δικαιοσύνη θεοῦ): `_LOG_EXECUCAO.md`, `ANATOMIA_DO_PROJETO.md`,
`CLAUDE.md`, `CURADORIA_FONTES_JUSTICA-DE-DEUS.md`, `ESCOPO_JUSTICA_DE_DEUS.md`.

**Separação feita (ver `ANATOMIA_DO_MOLDE.md`):** o que é método agnóstico
ao objeto de estudo (arquitetura em fases, Regra Zero como padrão
estrutural, padrão de cinco itens, escala de certeza, protocolo
anti-alucinação, dupla checagem anti-falha, mecanismo de sentinelas) foi
herdado; o que é específico do tema anterior (NPP, Käsemann/Sanders/Wright,
infraestrutura Windows/PowerShell/NotebookLM/rclone) foi descartado ou
substituído por equivalente portável (scripts Python, git em vez de rclone).

## 2. Enriquecimento a partir do projeto-irmão `Dikaiosyne Theou` (mesma sessão)

Durante a geração, o usuário forneceu três documentos adicionais de um
projeto **mais avançado e mais amplo**, que trata δικαιοσύνη θεοῦ **e** o
sacerdócio de Cristo, com a tríade ἱλασ- como "Regra do Projeto" (ali,
§0-B) obrigatória em toda unidade: `PLANO_DIKAIOSYNE_THEOU.md`,
`LOG_QUERIES.md` (319 queries reais catalogadas, extraídas
programaticamente de transcritos de sessão) e
`PROTOCOLO_REAPROVEITAMENTO_MD.md`.

**Achado crítico herdado (sentinela S20 lá, R11 aqui):** um `.md`
convertido de NA28 grego não estava em NFC nem NFD — normalização mista.
Busca literal por `ἱλαστήριον` (acentuado) devolvia 0 ocorrências num
arquivo que tinha a palavra visível seis vezes na tela. Foi **falso
negativo do buscador, não do acervo**. A ferramenta corretiva
(`buscar_grego.py`, que remove diacríticos via NFD antes de comparar) foi
reescrita aqui em Python puro (o original certamente era Python também,
mas específico daquele projeto) e **testada nesta sessão**:

```
python3 _scripts/buscar_grego.py --teste /tmp/t/teste_acentuado.md
```

com um arquivo de teste contendo as seis formas em NFC/NFD misturados —
resultado: **APROVADO**, todas as quatro raízes (`ιλαστηριον`, `ιλασμ`,
`ιλασθ`, `ιλασκ`) encontradas corretamente.

**Dados verificados no NA28 pelo projeto-irmão, herdados como evidência
anexada às sentinelas (não como sentinela já verificada aqui — regra do
próprio protocolo: "sentinela verificada em outro corpus não é sentinela
verificada neste"):**
- Rm 3.25: ἱλαστήριον **anartro** (`προέθετο ὁ θεὸς ἱλαστήριον`).
- Hb 2.17: `εἰς τὸ ἱλάσκεσθαι ⸂τὰς ἁμαρτίας⸃ τοῦ λαοῦ` — objeto = pecados,
  variante marcada no aparato.
- 1Jo 2.2: `οὐ περὶ τῶν ἡμετέρων δὲ μόνον ἀλλὰ καὶ περὶ ὅλου τοῦ κόσμου`.

**Estado do acervo, herdado como referência de aquisição:** NA28 aprovado
no teste lexical; UBS5 (duas cópias) reprovado e vetado; BDAG aprovado com
ressalva (ruído de colunas bleeding); Thayer e Moulton-Milligan aprovados;
Abbott-Smith e Robertson reprovados (OCR corrompido); Dodd (1931 artigo,
1935 livro) e Nicole (1955) **ausentes em todos os acervos irmãos
verificados** — permanecem prioridade máxima de aquisição.

## 3. Scripts escritos e testados nesta sessão

| Script | Teste rodado | Resultado |
|---|---|---|
| `buscar_grego.py` | `--teste` com grego puro e com NFC/NFD misto | ambos aprovados corretamente; teste de rejeição (arquivo com só 1 ocorrência de cada) reprovou corretamente antes do ajuste de stems |
| `verificar_sentinelas.py` | rodado contra `sentinelas_HILAS.md` real (0 linhas na tabela oficial) | retornou `[VAZIO]`, exit 2 — trava ativa, como esperado |
| `checagem_retomada.py` | rodado na raiz do projeto | relatório completo, sinalizou biblioteca vazia e MEMORIA_PROJETO.md ausente (na primeira rodada) corretamente |
| `dossie.py`, `conferir_citacoes.py` | escritos, não rodados contra dados reais (biblioteca vazia) | pendente de teste com acervo real |

## Pendências abertas

1. Rodar `dossie.py` e `conferir_citacoes.py` contra acervo real assim que
   `biblioteca/` receber arquivos.
2. Decidir a fonte de acesso a Dodd 1931/1935 e Nicole 1955.
3. `.claude/settings.json` com hook `PreToolUse` — escrito, não testado
   dentro de uma sessão real do Claude Code (só a lógica do script
   subjacente foi testada via linha de comando).

## 4. Camada NotebookLM: cadernos, mídia e ferramenta real (27-28/09/2026)

### Achados de projetos-irmãos incorporados

- **`ESTRATEGIA_NOTEBOOKLM.md`** (ISA-PAU): arquitetura de cadernos,
  gatilhos, quatro portas, regras invioláveis, cinco vozes — adaptado em
  `ESTRATEGIA_NOTEBOOKLM_HILAS.md` para 4 cadernos (F1 + U01-U03) + síntese.
- **`ESTRATEGIA_DE_MIDIA.md`** e **`ESTRATEGIA_DE_USO.md`** (Tabernáculo):
  o piloto real do caderno `TAB-95-TRIADE-HILASMOS` — que tem **as quatro
  fontes exatas do debate central deste projeto** (Dodd, Morris, Nicole,
  Packer) — foi auditado e documentado com resultados concretos: vídeo e
  relatório reprovaram (violaram a Regra Zero, terminaram neutros/a favor
  de Dodd); áudio e mapa mental aprovaram; flashcards/quiz tiveram grego
  em LaTeX (defeito a evitar aqui); slides falharam sempre. Incorporado em
  `ESTRATEGIA_MIDIA_HILAS.md`, com um módulo único de 3 episódios (um por
  lexema), em vez dos 5 módulos do projeto maior.
- **`ESTRATEGIA_POPULACAO_NOTEBOOKLM.md`**: funil genérico (camada local →
  auditoria de adversários antes de montar → montagem → Deep Research cara
  → verificação por contagem real, duas vezes) — referenciado em
  `ESTRATEGIA_NOTEBOOKLM_HILAS.md`.
- **`CATALOGO_DE_FONTES.md`, `INVENTARIO_AQUISICOES_2026-09-17.md`,
  `LISTA_DE_AQUISICOES.md`** (Tabernáculo): confirmaram o título exato de
  Packer (*Knowing God*, cap. "The Heart of the Gospel", não *In My Place
  Condemned He Stood* como uma nota anterior supunha) e revelaram que
  Harrison, *Levítico* (TNTC), já discute a etimologia de kipper e a
  tradução de ἱλαστήριον na LXX — candidato de apoio à Unidade 01.
- **`AUDITORIA_MECANICA_FASE3.md`, `CHECKLIST_AUDITORIA.md`,
  `RASTREABILIDADE_CONSULTAS.md`**: o padrão de auditoria mecânica (V1-V6,
  checklist por unidade/antes-da-síntese/antes-da-entrega, rastreabilidade
  de cada citação até a fonte real) — adaptado, na escala menor deste
  projeto, em `_artifacts/CHECKLIST_AUDITORIA_HILAS.md`.

### Ferramenta real do NotebookLM — verificação de sintaxe

Baixado e inspecionado o código-fonte do pacote `notebooklm-py`
(https://github.com/teng-lin/notebooklm-py, `pip install notebooklm-py`,
versão 0.8.3) via `pip download` + `unzip`, para confirmar a sintaxe real
da CLI antes de escrever os scripts de automação — não apenas por
documentação, mas por leitura do código (`cli/*_cmd.py`).

**Confirmado exatamente como os projetos-irmãos já documentavam:**
`-p`/`--profile` é opção **global** (antes do subcomando);
`-n`/`--notebook` é opção **do subcomando**; `notebooklm auth check --test`;
`notebooklm source add <conteúdo> -n <id> --type file`; `notebooklm
source add-research <query> --from web --mode deep --import-all
--cited-only --timeout <n>`; `notebooklm generate audio/video/report/
quiz/flashcards/mind-map/slide-deck`; `notebooklm artifact list/get/wait/
poll`; `notebooklm usage --json`. Os comandos de caderno (`create`,
`list`, `copy`, `delete`, `rename`) são de **topo**, não um subgrupo
`notebook`.

Corrigido em `montar_caderno.py` um erro que eu mesmo tinha cometido antes
desta verificação: `source add --file <caminho>` (flag inexistente) →
`source add <caminho> --type file` (conteúdo é argumento posicional).

**Não executado contra conta real** — este ambiente não tem `notebooklm
login` feito nem credenciais de longo prazo.

### Scripts escritos nesta rodada

`prevoo_cota.py` (livro-razão via `notebooklm usage --json`),
`verificar_artefato.py` (download + assinatura binária + checagem de
status `completed`) — ambos seguindo o mesmo padrão de `montar_caderno.py`:
sintaxe conferida contra o código-fonte real, execução não testada.

## 5. Primeira fonte real recebida e aprovada — NA28 (28/09/2026)

Usuário anexou o `.epub` original do NA28 (Novum Testamentum Graece,
Nestle-Aland). Como este ambiente não tinha ferramentas de extração de
PDF/EPUB, instalados nesta sessão: `pymupdf`, `ebooklib`, `beautifulsoup4`,
`lxml` (via `pip install`).

**Processo, seguindo as seis portas de `CURADORIA_FONTES_HILAS.md` §1:**

1. **Porta 1 (identidade):** metadado do epub confirma "Barbara und Kurt
   Aland, Institut für Neutestamentliche Textforschung, Münster",
   ISBN 978-3-438-07236-8, editora readbox/Deutsche Bibelgesellschaft —
   bate exatamente com a identificação que os projetos-irmãos descreviam
   ("Vorwort... Barbara Aland, Kurt Aland").
2. **Porta 2 (alfabeto como imagem):** apenas 1 `<img>` em todo o epub (a
   capa) — sem hebraico/grego preservado como imagem.
3. **Porta 3 (teste lexical):** `buscar_grego.py --teste` — **APROVADO**,
   as quatro raízes (ιλαστηριον, ιλασμ, ιλασθ, ιλασκ) todas encontradas
   com a contagem mínima exigida.
4. **Porta 4 (sanidade do corpo):** as seis ocorrências foram lidas
   integralmente com contexto — grego limpo, aparato crítico consistente
   (✝, ⸂⸃, ⸀). Confirmado ao vivo, nesta sessão:
   - Rm 3.25: `ὃν προέθετο ὁ θεὸς ✝ ἱλαστήριον ⸂διὰ [τῆς] πίστεως⸃` — **anartro confirmado**
   - Hb 9.5: `τὸ ✝ ἱλαστήριον` — com artigo, referência ao móvel
   - 1Jo 2.2: `αὐτὸς ✝ ἱλασμός ἐστιν περὶ τῶν ἁμαρτιῶν ἡμῶν, οὐ περὶ τῶν ἡμετέρων δὲ μόνον ἀλλὰ καὶ περὶ ὅλου τοῦ κόσμου` — **extensão confirmada por completo**
   - 1Jo 4.10: `ἀπέστειλεν τὸν υἱὸν αὐτοῦ ✝ ἱλασμὸν περὶ τῶν ἁμαρτιῶν ἡμῶν`
   - Lc 18.13: `ὁ θεός, ✝ ἱλάσθητί μοι τῷ ἁμαρτωλῷ`
   - Hb 2.17: `εἰς τὸ ✝ ἱλάσκεσθαι ⸂τὰς ἁμαρτίας⸃ τοῦ λαοῦ` — **objeto = pecados confirmado**
5. **Porta 5:** não necessária — sem defeito a avisar.
6. **Porta 6:** Tier S.

**Arquivo gravado:** `biblioteca/NA28_Novum-Testamentum-Graece.md`
(638.153 palavras, frontmatter com autor/ISBN/sha256 do epub de origem,
portas conferidas documentadas no próprio cabeçalho).

**Sentinelas migradas para a tabela oficial** (`_artifacts/sentinelas_HILAS.md`),
pela primeira vez com verificação própria deste projeto, não mais só
"achado do projeto-irmão": nº1 (anartro em Rm 3.25), nº2 (objeto de
Hb 2.17), nº3 (extensão de 1Jo 2.2), nº4 (o buscador funciona). **Estado:
4/6 — `verificar_sentinelas.py` retorna [INCOMPLETO], exit 1** (antes era
[VAZIO], exit 2). Trava de escrita em `saidas/` menos severa agora, mas
ainda não liberada.

**Pendência declarada:** o arquivo está acima do teto usual de upload ao
NotebookLM (450-525 mil palavras, conforme a conta) — dividir antes de
subir a um caderno; `dividir_md.py` ainda não foi escrito neste projeto
(existe nos projetos-irmãos, não portado ainda).

## 6. Segundo lote de fontes reais — fecha a Fase 0 (28/09/2026)

Usuário anexou quatro `.md` já convertidos (não PDFs — conversão feita
pelo próprio pipeline local do usuário, com frontmatter e, em dois casos,
aviso de OCR já embutido): Morris (*Apostolic Preaching of the Cross*),
Nicole (*Our Sovereign Saviour*), Packer (*Knowing God*), Harrison
(*Levítico — Introdução e Comentário*, **edição em português**, Série
Cultura Bíblica — distinta da edição inglesa TNTC que os documentos dos
projetos-irmãos mencionavam).

**Portas rodadas nos quatro** (ver `CURADORIA_FONTES_HILAS.md`):
- Porta 1 (identidade): Morris confirmado pelo sumário batendo com a
  estrutura conhecida da obra (caps. V-VI "Propitiation"); Nicole/Packer
  por frontmatter próprio; Harrison por menção ao autor no corpo (p. 40+)
  e identificação da edição em português.
- Porta 2 (imagem): 0 em todos os quatro.
- Porta 3 (teste lexical): Morris tem grego real (97 ocorrências de
  `ιλασ`, com ruído de OCR letra a letra — ex. `iAaopos` por ἱλασμός); os
  outros três são classe "só argumento" (Nicole/Packer já vinham com
  aviso do pipeline do usuário; Harrison em português, não se aplica).
- Porta 4 (sanidade do corpo): lida em todos — Morris (cap. V completo,
  discussão fiel de todos os 6 versículos da tríade + Mt 16.22 + Hb 8.12);
  Nicole (trecho sobre extensão de 1Jo 2.2); Packer (cap. 18 completo,
  "The Heart of the Gospel"); Harrison (miolo em pp. 40-45, e o trecho
  específico sobre etimologia de kipper/ἱλαστήριον).

**Achado que fechou duas sentinelas de uma vez:** o capítulo de Morris
"The work of C. H. Dodd" (`biblioteca/Morris_Apostolic_Preaching_of_the_Cross.md`,
linhas ~5966-6030) cita **o método real de Dodd em 3 passos**, com nota de
rodapé numerada — não a versão achatada que a sentinela original
alertava contra. E cita e resume, com precisão, o artigo de **Roger
Nicole, "C. H. Dodd and the Doctrine of Propitiation"** ("Dodd leva em
conta não mais que 36% da evidência"). Isso confirma o conteúdo real do
artigo de Nicole mesmo sem o texto integral em mãos.

**Sentinelas migradas:** nº5 (o método real de Dodd) e nº6 (propiciação ≠
expiação, decorrente diretamente do nº5). **Estado final: 6/6 —
`verificar_sentinelas.py` retorna exit 0 [PRONTO].** Testado também o
hook `hook_sentinelas.py` contra um caminho simulado em
`fase2-unidades/U01_hilasterion/saidas/teste.md` — passa livre agora
(antes bloqueava com exit 2).

**🎉 Fase 0 (etapa de sentinelas) concluída.** Critério de saída atingido
com verificação própria deste projeto (não emprestada de projeto irmão)
em 100% das sentinelas oficiais.

## 7. BDB (léxico hebraico) — terceiro lote (28/09/2026)

Usuário anexou os 3 volumes do BDB (Brown-Driver-Briggs, *Hebrew and
English Lexicon*, 1906), já convertidos com aviso de OCR do próprio
pipeline do usuário marcando classe "CONFIÁVEL" (361 palavras hebraicas
por 10 mil).

**Portas:** identidade confirmada pelo frontmatter (autores corretos);
0 imagens de alfabeto; hebraico real presente (não testável por
`buscar_grego.py`, que é específico para grego — conferido por leitura
direta); sanidade confirmada em dois pontos (o verbete de כַּפֹּרֶת e um
spot-check aleatório distante, verbete גֵּב/גבב, ambos legíveis apesar de
ruído de OCR típico de 1906).

**Achado central:** verbete nº4616 (כַּפֹּרֶת, "propiciatório") cita
**explicitamente a tradução da LXX por ἱλαστήριον** e rejeita a etimologia
"cobrir/tampa" para כפר — dado lexical primário direto para a Unidade 01,
e evidência nova para a sentinela R4 (etimologia disputada em 3 polos,
não 2). Não migrada para tabela oficial (a disputa etimológica continua
aberta, isso apenas a documenta melhor).

**Estado da biblioteca: 8 arquivos.** Sentinelas seguem 6/6 [PRONTO].

## 8. Milgrom, UBS5 e correção de bug de glifo grego (28/09/2026)

Usuário anexou Milgrom (*Leviticus 1-16*, AYB, 2 partes) e uma conversão
própria de UBS5.

**Bug real encontrado e corrigido:** `buscar_grego.py --teste` reprovava
esta cópia de UBS5 (3/4 — faltava `ιλασθ`, Lc 18.13). Investigação por
leitura direta (busca por `Φαρισαῖος`/`τελώνης` até achar o versículo)
revelou a palavra presente, mas grafada `ἱλάσϑητί` com **ϑ** (U+03D1,
GREEK THETA SYMBOL) em vez de **θ** (U+03B8) padrão — variante tipográfica
real da edição, não erro de OCR. NFD (que resolve acento/espírito) não
resolve isso, porque são **letras Unicode diferentes**, não uma letra +
diacrítico.

**Correção:** `buscar_grego.py` agora mapeia as 5 letras gregas com
variante "symbol" (θ, φ, π, κ, ρ) para a forma padrão antes de comparar,
além do sigma final (ς→σ). Testado contra: (a) a cópia de UBS5 real —
passou a 4/4; (b) o NA28 já aprovado — sem regressão; (c) os dois arquivos
sintéticos de teste anteriores — sem regressão.

**Sentinela nº7 registrada** em `sentinelas_HILAS.md` — variante de glifo
como segunda classe de falso negativo, distinta da normalização NFC/NFD
(sentinela nº4/R11).

**Achado de curadoria:** o veto ao "UBS5" documentado nos projetos-irmãos
era específico às cópias deles (reprovadas por perda de conteúdo, 0/4).
Esta cópia, de conversão independente, reprova por um motivo totalmente
diferente (glifo) e, corrigido o buscador, aprova. **Lição: vetos a uma
edição por nome não se herdam entre conversões diferentes — cada arquivo
precisa do próprio teste.**

**Milgrom:** aprovado, Tier S, classe "só argumento" (convenção Anchor
Bible de transliteração). Ressalva de leitura: ocasional intercalação de
corpo com nota de rodapé (Regra 11-B), argumento recuperável com atenção.

**Estado da biblioteca: 11 arquivos.** Sentinelas: 7/6 — acima do
critério de saída, `verificar_sentinelas.py` [PRONTO].

## 9. Listagem real de `Justiça-de-Deus\_processados_md` (28/09/2026)

Usuário colou a listagem de 118 arquivos dessa pasta. Cruzamento contra
o que este projeto precisa:

- ✅ **`BDAG_Greek_English_Lexicon_NT_OCRv2.md` está lá** — pedir a
  seguir, é a peça que faltava do núcleo de léxicos.
- 🔴 **Não aparecem:** Dodd (nenhum arquivo com esse nome), Thayer,
  Moulton-Milligan. Não estão nesta pasta — permanecem como lacuna real
  (ver `ESCOPO_HILAS.md` §9, atualizado).
- Demais 116 arquivos são do escopo de "Justiça de Deus" (NPP, Käsemann,
  Sanders, Wright, patrística/Reforma sobre δικαιοσύνη θεοῦ) — fora do
  recorte lexical deste projeto, não solicitados.

## 10. Dodd, BDAG e Wenham — a lacuna mais importante fechada (28/09/2026)

Usuário anexou os três arquivos que faltavam do núcleo bibliográfico:
BDAG (já reOCR'd pelo pipeline de origem em 25/08/2026), Wenham
(*Leviticus*, NICOT) e — o mais importante — **Dodd, *The Bible and the
Greeks*, na íntegra**.

**Dodd:** capítulo V ("Atonement") é literalmente o ensaio de 1931 (*JTS*
32, 352-60) incorporado ao livro de 1935. Lido diretamente: o método
completo de Dodd de classificar as traduções da LXX para כפר (Dn 9.24,
Êx 30.10, Dt 32.43, Is 6.11, Jr 18.23, todos com grego e hebraico
originais). **Grego de alta densidade e confiável** (1077 palavras
gregas/10k). Isso substitui a mitigação parcial que o projeto tinha até
agora (citação de Dodd via Morris) pela fonte primária real — os itens
(1) e (2) do padrão de refutação estão satisfeitos sem intermediário.

**BDAG:** verbetes de ἱλάσκομαι/ἱλασμός/ἱλαστήριον lidos por completo.
Confirma de forma **independente** (terceira fonte, depois de Morris e do
próprio texto de Dodd) a bibliografia exata do debate: Dodd *JTS* 32
('31, 352-60), Nicole *WTJ* 17 ('55, 117-57), e revela **um terceiro texto
de Morris** — *Expository Times* 62 ('51, 227-33), mais antigo que o
livro de 1955 e ainda não localizado. Também cita Manson (*JTS* 46, '45,
1-10) sobre ἱλαστήριον como "lugar de propiciação" em Rm 3.25, e
Breytenbach (1989) contra essa leitura — debate direto para a Unidade 01.

**Wenham:** reprova parcial na Porta 2 — 649 imagens, 0 caracteres
hebraicos/gregos reais no arquivo inteiro. **Mesmo padrão já medido em
`Wenham_Genesis_1-15_WBC` nos projetos-irmãos** (hebraico/grego
preservados como imagem, não como texto, em conversões de EPUB desta
série). Entra como Tier A1, classe "SEM FORMA ORIGINAL" — usar o
argumento, nunca citar forma hebraica/grega dele diretamente.

**Sentinela migrada:** nº8 (citação de Dodd/Nicole/Morris, agora com
tripla confirmação independente — Morris, o próprio Dodd, e o BDAG).
Estado: 8/6 sentinelas verificadas.

**Estado da biblioteca: 14 arquivos.**

## 11. Stott e Hill/James — Carson localizado, quarta confirmação de Nicole (28/09/2026)

Usuário anexou dois `.epub`: Stott, *The Cross of Christ*, e Hill & James
(eds.), *The Glory of the Atonement*. Extraídos com o mesmo pipeline
ebooklib+BeautifulSoup do NA28.

**Stott:** identidade confirmada por metadado (ISBN, editora IVP).
Seção "Propitiation" lida por completo — trata Dodd, Morris, Nicole e
Büchsel (TDNT) com precisão, incluindo um dado novo (1 Clemente e o
Pastor de Hermas usam ἱλάσκομαι claramente para propiciar Deus,
argumento de Büchsel contra Dodd). **Confirma a citação de Nicole pela
quarta vez, de forma totalmente independente**: "Nicole, Roger R., 'C. H.
Dodd and the Doctrine of Propitiation', *Westminster Theological Journal*
xvii.2 (1955), pp. 117-157" — idêntica a Morris e ao BDAG.

**Hill & James:** metadado do epub estava corrompido (título "B004JLM6FI
EBOK", artefato do Calibre) — identidade confirmada pelo **corpo**
(sumário interno lista os editores e o título real). **Achado**: o livro
é dedicado a Roger Nicole. O capítulo 6, de **D. A. Carson**, "Atonement
in Romans 3:21-26", fecha um item pendente da pauta de aquisição.

**Bug de conversão identificado (terceira classe, distinta de imagem e de
variante de glifo):** o grego neste arquivo está **cifrado** — mapeamento
de fonte-símbolo do PDF original herdado como Latin1 genuíno na
conversão (`ἱλαστήριον` → `1XaoTrjplov`, `ἱλασμός` → `iAaoios`). Mesmo
padrão documentado nos projetos-irmãos como "Regra 17 candidata"
(Ellingworth, Cockerill). **Não é detectável por `buscar_grego.py`** (não
há erro de acento/glifo — é substituição de caractere). Registrado como
**sentinela nº9**, com a regra prática de inspecionar visualmente
sequências como maiúscula-no-meio-de-palavra antes de aceitar "grego
ausente" de um epub convertido. Arquivo entra como Tier S, mas com aviso
explícito: nunca citar forma grega exata dele.

**Estado: 16 arquivos na biblioteca, 9/6 sentinelas [PRONTO].**

## 12. Caragounis — quinta confirmação independente (28/09/2026)

Usuário anexou o artigo de Chrys C. Caragounis (Lund University),
"Expiation-Propitiation-Reconciliation" (2020), e um segundo envio de
Stott (SHA-256 idêntico ao já processado — descartado como duplicata,
não reprocessado).

**Caragounis é, até agora, a fonte mais precisa do projeto sobre a
bibliografia do debate.** Dá o título completo do artigo de Dodd —
"Ἱλάσκεσθαι, its cognates, derivatives and synonyms in the Septuagint",
*JTS* 32 (1931), pp. 352-360 — confirma que foi reimpresso como capítulo
5 ("Atonement") de *The Bible and the Greeks*, e cita ainda Dodd, *The
Epistle to the Romans* (Moffatt NTC, 1932) *ad loc*. **Quinta confirmação
independente e idêntica** da citação de Nicole (*WTJ* 17, 1955, pp.
117-157). Dois dados novos: Cranfield também criticou Dodd; e a
referência exata de Büchsel em TDNT vol. III, p. 311f (paginação exata,
ainda não localizado na íntegra).

**Sentinela 8 atualizada com a quinta fonte.** Estado: 17 arquivos na
biblioteca, 9/6 sentinelas [PRONTO].

## 13. Seis cadernos de círculo + upgrade da persona de pesquisa (28/09/2026)

A pedido do usuário: um caderno NotebookLM por círculo concêntrico
(`ESCOPO_HILAS.md` §4, C0-C5), cada um com Deep Research própria para
fechar lacunas e pacote de mídia (6 áudios — 3 debates alternando
personas + 3 solo —, 4 vídeos, 1 mapa mental, 1 relatório aprofundado, 1
infográfico, 1 flashcards = 14 artefatos por caderno, 84 no total).

**Documentos criados:**
- `ESTRATEGIA_CIRCULOS_HILAS.md` — os 6 cadernos, pauta de Deep Research
  específica por caderno (mirando as sentinelas ainda abertas: R4
  etimologia de כפר, R6 Ritschl, R8 RSV 1946, R9 4 Macabeus 17.22), e o
  pacote de mídia completo com preenchimento dos parâmetros de debate por
  caderno.
- `_artifacts/PERSONAS_MIDIA_HILAS.md` — os cinco templates de persona de
  mídia (A1 Erudito, A2 Pastor, A3 Apologética-N3, A4 Apologética-N1, A5
  Aluno), adaptados de templates de outro projeto (Rm 1.16-17) para a
  Regra Zero deste projeto (ira pessoal de Deus, propiciação objetiva),
  parametrizados por `{TEMA}`/`{TEXTOS}`/`{ADVERSARIO_N3}`/`{DEBATE_N1}`.

**Documento atualizado:** `_artifacts/persona_notebooklm.txt` —
substituído por uma persona de pesquisa muito mais completa (fornecida
pelo usuário, genérica para pesquisa bíblica erudita), com as adições
específicas deste projeto preservadas: classificação obrigatória
`[FONTE PRIMÁRIA NO CORPUS]`/`[CITADO POR TERCEIROS]`/`[NÃO ENCONTRADO]`,
referência às sentinelas abertas, e a Regra Zero como limite explícito
(equiparar Dodd à leitura reformada nunca é "reconhecer divergência
legítima").

**Tensão identificada e resolvida:** o método já documentado
(`ESTRATEGIA_MIDIA_HILAS.md`, baseado no piloto real do `TAB-95`) diz que
mídia só deve sair de cadernos alimentados com conteúdo **auditado**,
nunca de cadernos de fonte bruta — porque geração sem curadoria viola a
Regra Zero (vídeo saiu neutro, relatório só citou Dodd). Os cadernos de
círculo, por pedido explícito, geram mídia diretamente. Resolvido
adaptando o Gatilho 2 (`ESTRATEGIA_NOTEBOOKLM_HILAS.md`): nenhuma mídia
antes de (a) a Deep Research rodar e as fontes ficarem `ready`, (b) o
`GUIA_EDITORIAL_HILAS.md` estar dentro do caderno como fonte, (c) uma
consulta de verificação ter auditado o que a Deep Research trouxe.

**Cota:** 84 chamadas de `generate` só para os círculos, muito acima do
teto de ~40/dia medido nos projetos-irmãos — um caderno de círculo por
dia, ordem sugerida priorizando fechar sentinelas (C0→C1→C4→C5→C2→C3).

**Nada executado** — mesma ressalva de sempre, este ambiente não tem CLI
autenticada.

## 14. Unidade 01 (ἱλαστήριον) redigida (28/09/2026)

Primeira unidade exegética do projeto, `fase2-unidades/U01_hilasterion/saidas/RELATORIO_U01.md`.
Fontes usadas: NA28 (texto grego, conferido com `buscar_grego.py`), BDB
(verbete de כַּפֹּרֶת), Dodd (cap. V, citação literal do argumento sobre
Rm 3.25), Morris (pp. 197f, 208-209 — argumento sobre 4 Macabeus 17.22 e
o contexto de Rm 1-3), Caragounis (citação de Cranfield, *Romans I*,
pp. 216-217), BDAG (bibliografia Manson/Breytenbach/Fitzer).

**Achado de redação:** revelou-se uma divergência real entre dois
defensores da mesma linha editorial — Cranfield/Caragounis (ἱλαστήριον
alude ao *kapporet*/Dia da Expiação) × Morris (alude antes a 4 Macabeus
17.22, rejeitando a conexão com o *kapporet* porque este era oculto e
Cristo foi exposto publicamente). Tratada como exceção legítima da Regra
Zero (`CLAUDE.md` §2-B, exceção 2) — divergência entre aliados, não
concessão a Dodd, já que ambos rejeitam a leitura de expiação impessoal.

**Sentinela R9 avançada substancialmente:** Morris cita 4 Macabeus 17.22
diretamente (`τὸν ἱλαστήριον θανάτου αὐτῶν`) — confirma que é o adjetivo
ἱλαστήριος concordando com θάνατος, cognato mas não idêntico ao
substantivo de Rm 3.25/Hb 9.5. R9 permanece formalmente aberta (falta o
texto primário de 4 Macabeus no acervo), mas a pergunta "é a mesma raiz?"
está respondida.

**`conferir_citacoes.py` não encontrou citações** porque o relatório usa
citação em prosa (autor + página + obra) em vez do padrão exato `(Autor,
p. N)` que o regex do script busca — as citações foram conferidas
manualmente contra o disco durante a redação (grep direto nos arquivos
antes de cada citação). Considerar ajustar o script para aceitar mais
formatos, ou manter a disciplina manual documentada aqui.

**Lacunas declaradas no relatório:** Cranfield (ICC) só via citação de
segunda mão; 4 Macabeus sem texto primário; Manson/Breytenbach só via
BDAG.

## 16. Redação da Unidade 03 — ἱλάσκομαι (28/09/2026)

Redigido `fase2-unidades/U03_hilaskomai/saidas/RELATORIO_U03.md`, cobrindo
Lc 18.13 e Hb 2.17, seguindo a ordem recomendada no
`FASE_0_CHECKLIST.md` (U01 → U03 → U02 → U04). Fontes conferidas
diretamente no disco antes de cada citação: NA28 (Lc 18.13 e Hb 2.17,
via `buscar_grego.py`, sem regressão), Dodd (cap. V, citação literal dos
dois parágrafos que tratam os dois textos lado a lado), BDAG (verbete
ἱλάσκομαι completo, os dois sentidos e a bibliografia do debate), Stott
(pp. 3895-4024 região — a seção mais longa e detalhada do acervo sobre
este par de textos), Caragounis (pp. 22-23, 27, 30).

**Achado de redação — a tensão gramatical Lc 18.13 × Hb 2.17 é o próprio
par de textos que Dodd usa como prova dupla:** Lc 18.13 (sem objeto de
pecado, sujeito=Deus) e Hb 2.17 (com "as pecados" como objeto direto
explícito) parecem, à primeira vista, empurrar em direções opostas —
Dodd os une sob o mesmo "modelo" (a ideia de propiciar pessoa já teria
"evaporado" em ambos). A resposta não nega a assimetria gramatical (Stott
concede explicitamente que Hb 2.17 é transitivo com objeto de pecado);
argumenta que a transitividade não decide sozinha entre "aplacar a ira
relativa ao pecado" e "cancelar o pecado" — a decisão depende do contexto
de Hebreus (sacerdócio, ira mencionada em 3.11/4.3).

**Achado novo, candidato a sentinela:** Caragounis (pp. 22-23, notas
69-70) observa que os três léxicos gregos gerais (LSJ, Demetrakos,
Montanari) citam **Hb 2.17 como único exemplo**, em toda a literatura
helênica catalogada, do sentido "expiação" para o grupo ἱλασκ- — o que
torna circular usar Hb 2.17 para provar que a palavra "pode" significar
expiar. Documentado em §2.3 e §4.1 do relatório; recomendado promover a
rascunho formal de sentinela na próxima manutenção de
`_artifacts/sentinelas_HILAS.md` — nenhum dos três léxicos gerais está no
acervo, então a citação permanece `[CITADO POR TERCEIROS]`.

**Lacunas declaradas no relatório:** LSJ/Demetrakos/Montanari (léxicos
gregos gerais) não estão no acervo, só citados via Caragounis; 1 Clemente,
Pastor de Hermas, Josefo e Filo (evidência pós-NT/intertestamentária de
uso propiciatório, citados por Stott via Büchsel) sem texto primário no
acervo — relevantes para o futuro Círculo C5 (História da Interpretação).

## 17. Redação da Unidade 02 — ἱλασμός (28/09/2026)

Redigido `fase2-unidades/U02_hilasmos/saidas/RELATORIO_U02.md`, cobrindo
1Jo 2.2 e 4.10 — última unidade lexical antes da síntese (U04). Fontes
conferidas diretamente no disco: NA28 (1Jo 2.2 e 4.10 via
`buscar_grego.py`), Dodd (cap. V, citação literal do parágrafo sobre os
dois textos joaninos, incluindo a concessão que ele mesmo faz ao dado do
παράκλητος antes de descartá-lo), BDAG (verbete ἱλασμός completo, os dois
sentidos e os paralelos Ez 44.27/Nm 5.8), Stott (pp. 3994-3996), Packer
(pp. 3390-3392 "PROPITIATION DESCRIBED" e 3404-3408 "NOT MERELY
EXPIATION"), Nicole (pp. 2345-2404, tratamento extenso do alcance de
"todo o mundo").

**Correção de nomenclatura gramatical:** a construção `περὶ τῶν
ἁμαρτιῶν ἡμῶν` não é um "genitivo objetivo" (como a tabela do
`CLAUDE.md` §1 descreve), é **περί + genitivo** — mesmo padrão
preposicional da fórmula sacrificial da LXX para "oferta pelo pecado".
A pergunta teológica de fundo (remoção vs. aplacamento) não muda, mas a
categoria gramatical estava imprecisa. Registrado como observação em
§1 e §5 do relatório; recomenda-se ajustar a tabela do `CLAUDE.md` numa
próxima revisão editorial (não fiz a edição agora para não misturar
correção estrutural do `CLAUDE.md` com a redação de uma unidade).

**Achado de redação — Dodd concede o dado do adversário antes de
descartá-lo:** diferente das outras unidades, aqui Dodd reconhece
explicitamente que o contexto de ἱλασμός junto a παράκλητος πρὸς τὸν
Πατέρα (1Jo 2.1) "poderia apoiar" a leitura propiciatória-pessoal — e
mesmo assim conclui pela leitura de "oferta pelo pecado"/purificação,
apoiado na fórmula `ἱλασμὸς περὶ ἁμαρτιῶν` da LXX. A resposta (§4.1)
argumenta que a própria fórmula sacrificial da LXX pressupõe um
destinatário pessoal (Deus, que aceita a oferta), não apenas remoção.

**Sentinela R6 avançada:** Packer (`Knowing God`, seção "NOT MERELY
EXPIATION") confirma, de forma independente de outras menções já
registradas no projeto, a filiação histórica Sócino (séc. XVI) →
Albrecht Ritschl → C. H. Dodd. R6 permanece formalmente aberta (nenhuma
obra de Ritschl no acervo, nenhuma das fontes secundárias cita
Ritschl com paginação direta), mas agora tem duas fontes independentes
convergentes.

**Achado sobre o alcance de "todo o mundo" (1Jo 2.2):** tratado como
debate legítimo e distinto do eixo Dodd×conservadores (`CLAUDE.md` §2-B,
exceções 1 e 3) — Nicole defende a leitura particularista/reformada com
três sub-opções não conflitantes, todas afirmando propiciação pessoal e
efetiva (é precisamente *por* levar o termo a sério como efeito real que
Nicole não pode aceitar "todo o mundo" = universalismo da salvação).
Lacuna real declarada: o acervo não tem uma defesa formal da posição
arminiana/de expiação universal-efetiva para contrapor.

**Lacunas declaradas no relatório:** posição arminiana sobre o alcance,
não representada no acervo com a mesma profundidade que Nicole; Ritschl,
texto primário, ainda não localizado; 2 Macabeus 3.33 (paralelo de
ἱλασμός citado por BDAG), sem texto primário no acervo.

## 18. Redação da Unidade 04 — síntese (28/09/2026)

Redigido `fase2-unidades/U04_sintese/saidas/RELATORIO_U04.md`, fechando a
Fase 2 (as quatro unidades — U01, U02, U03, U04 — estão completas).
Seguida à risca a regra do `CLAUDE.md` §1: **este dossiê não recebeu
consulta nova à `biblioteca/`** — toda citação remonta aos três
relatórios de unidade já auditados (U01, U02, U03), nunca a um arquivo
da biblioteca diretamente. O relatório abre com uma nota metodológica
explícita registrando essa restrição, para que auditorias futuras
possam verificar a disciplina.

**Contribuição específica da síntese:** mostrar que os "ataques ao
pressuposto" já feitos separadamente em cada unidade (U01 §4.1 —
estatístico, via Nicole/Morris; U03 §4.1 — circularidade lexicográfica,
achado próprio de Caragounis; U02 §4.1 — Dodd concede o dado do
adversário antes de subordiná-lo) são, na verdade, **a mesma crítica
metodológica única** aplicada em três pontos: Dodd decide o sentido
lexical geral da LXX antes de examinar o peso do contexto imediato de
cada texto do NT, e trata essa decisão prévia como mais forte que a
evidência textual local que a contradiz. Nomeado como o pressuposto
central atacado por todo o projeto, não apenas por uma unidade.

**Lacuna declarada de escopo (nova, não presente nas unidades
anteriores):** o `CLAUDE.md` pede que a síntese relacione a propiciação
com καταλλαγή (reconciliação) e ἀπολύτρωσις (redenção), mas nenhuma das
três unidades tratou desses termos como objeto de exegese lexical
própria — apenas nota-se a adjacência textual de ἀπολύτρωσις em Rm 3.24,
na mesma sentença de ἱλαστήριον (3.25). Como a síntese não pode consultar
a biblioteca diretamente (regra do `CLAUDE.md` §1), essa exegese fica
fora do escopo desta unidade — declarada como lacuna, não preenchida por
inferência. Recomenda-se um dossiê dedicado (Círculo C3, Loci Teológicos)
se o projeto quiser fechar essa lacuna com o mesmo rigor lexical das
quatro unidades.

**Sentinelas:** nenhuma sentinela nova foi aberta ou fechada nesta
síntese — ela reúne e nomeia explicitamente a sentinela nº5 (método de
Dodd em 3 passos) como o pressuposto unificado, e menciona R6/R9/a
observação da U03 apenas para registro de estado, sem reabri-las.
