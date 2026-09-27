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
