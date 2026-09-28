# Anatomia do molde — o que este projeto herdou, e de onde

*Este projeto (`hilas`) foi gerado a partir de um conjunto de quatro
documentos de outro projeto de pesquisa exegética (tema: "Justiça de
Deus" — δικαιοσύνη θεοῦ), que por sua vez documentava um método destilado
de projetos ainda anteriores (João, Jeremias, Hebreus, Romanos). Este
arquivo separa o que é **método agnóstico ao objeto de estudo** — e
portanto se aplica aqui, aos três lexemas ἱλασ- — do que era **específico
daquele projeto** e não se aplica.*

---

## 1. O que se herdou sem alteração

| Componente | Onde vive aqui | Por quê é agnóstico |
|---|---|---|
| A arquitetura em fases (fundamentos → exegese unidade a unidade → síntese) | `CLAUDE.md` §1 | qualquer objeto de estudo bíblico se beneficia de separar fundamento de exegese de síntese |
| A Regra Zero como *padrão estrutural* (nunca equiparar tese e antítese sem desfecho) | `CLAUDE.md` §2-B — aqui aplicada ao par Dodd/Morris em vez de conservador/progressista | o padrão importa mais que o conteúdo específico; qualquer debate teológico com um lado que a linha editorial sustenta precisa dessa disciplina |
| O padrão de refutação de cinco itens | `CLAUDE.md` §2-B | genérico: fonte primária · melhor versão · pressuposto · ancoragem tripla · desfecho |
| A escala de certeza (6 níveis) | `_artifacts/escala_certeza.md` | integral, sem mudança |
| O protocolo anti-alucinação | `_artifacts/sistema_erudito.md` | integral, menos o bloco de sentinelas (que é sempre específico) |
| A dupla checagem anti-falha (nunca declarar ausência com um método só) | `CLAUDE.md` §0 | vale para qualquer corpus pequeno o bastante para "parecer" totalmente lido |
| Sentinelas como mecanismo (trava + tabela contada + rascunho fora da contagem) | `CLAUDE.md` §4, `_artifacts/sentinelas_HILAS.md` | o *mecanismo* é agnóstico; as dez sentinelas em si são específicas deste tema |
| As três consultas por unidade (exegética · verificação · refutação dirigida) | `CLAUDE.md` §3 | a verificação audita a consulta anterior, não só busca o contraditório — vale para qualquer tema |
| Scripts de dossiê/sentinela/citação, como *padrão* de automação local | `_scripts/` | reescritos em Python puro (sem PowerShell, sem OCR em lote, sem NotebookLM) porque este corpus é pequeno e não exige pipeline de conversão pesado |

## 2. O que foi descartado ou substituído

| Componente do projeto-origem | Por que não se aplica aqui |
|---|---|
| Pipeline de OCR em lote (`converter_lote.ps1`, `pdf_to_md.py --ocr --grego`) | O corpus deste projeto é ~10 obras, a maioria com camada de texto nativa ou em domínio público já digitalizado (BDAG, TDNT em módulos eletrônicos). Se algum PDF exigir OCR, tratar caso a caso, sem infraestrutura de lote |
| NotebookLM / gestão de perfis e notebooks | Ferramenta específica de outra sessão de trabalho (Windows, contas Google). Este projeto usa os arquivos em `biblioteca/` diretamente, com os scripts locais |
| Backup remoto via `rclone` para Google Drive | Este projeto vive em repositório git; versionamento é o próprio `git` |
| As 14 (depois 13) unidades temáticas de "Justiça de Deus" | Substituídas pelas 3+1 unidades lexicais deste projeto — ver `ESCOPO_HILAS.md` |
| Sentinelas sobre a Nova Perspectiva sobre Paulo, Käsemann, Sanders, Wright | Não são o tema aqui. O debate central deste projeto é Dodd ↔ Morris/Nicole, não NPP — embora ambos os debates se toquem na periferia (justificação forense e propiciação são categorias irmãs) |
| Hooks em PowerShell (`.ps1`) | Reescritos como script Python + `.claude/settings.json` com hook em `python3`, portável para Linux |

## 3. Lição de método que se aplica de imediato, sem esperar erro próprio

O projeto-origem registrou, em `_LOG_EXECUCAO.md`, **quatro falsos negativos
do mesmo padrão**: uma obra dentro de coletânea invisível pelo nome do
arquivo, uma citação alemã perdida por OCR em Fraktur (ſ lido como f),
Apocalipse escondido dentro de um comentário ao NT inteiro (Bengel), e
hebraico preservado como imagem em vez de texto num `.epub` convertido.

**A regra consolidada por esses quatro casos vale aqui desde o primeiro dia:**
antes de declarar que uma obra "não trata" de ἱλαστήριον/ἱλασμός/ἱλάσκομαι,
buscar por **conteúdo**, não por nome de arquivo — e, se a obra vier de
digitalização (scan, OCR, conversão de e-book), verificar se o grego não
sobreviveu apenas como imagem ou run de OCR corrompido antes de contar
como ausência.

---

*A separação acima existe para que, se um quinto projeto temático nascer
deste molde, este arquivo (e não o `CLAUDE.md` inteiro) seja o primeiro a
ser lido para decidir o que herdar.*
