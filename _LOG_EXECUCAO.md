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
