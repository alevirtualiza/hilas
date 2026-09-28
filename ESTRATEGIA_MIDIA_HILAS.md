# Estratégia de mídia — Hilas

> **Base empírica real, não hipótese:** o projeto-irmão `Tabernáculo` já
> rodou um piloto (11/09/2026, auditado em 18/09/2026) no caderno
> `TAB-95-TRIADE-HILASMOS` — que tem **as quatro fontes exatas do debate
> central deste projeto**: Dodd (adversário), Morris, Nicole, Packer
> (conservadores). Os resultados desse piloto **são diretamente
> aplicáveis aqui**, porque é o mesmo debate, quase a mesma pergunta.

---

## 0. Decisão em uma frase

**Mídia pública só sai de um caderno de módulo alimentado com material já
auditado** (os relatórios das unidades U01-U03, não os PDFs brutos), e
**cada artefato é verificado contra a Regra Zero** antes de ser aceito —
integridade técnica (`ffprobe`, assinatura, idioma) não prova conteúdo.

---

## 1. O que o piloto do `TAB-95` já provou

Os 6 artefatos foram gerados com as quatro fontes já no caderno, **sem
prompt de direção editorial** — o pior caso, e o mais instrutivo:

| Artefato | Integridade técnica | Linha editorial |
|---|---|---|
| Vídeo (9min42s, H.264 1280×720) | ✅ | ❌ **declarou resumir "de forma bem neutra" e fechou numa pergunta em aberto** — fere a Regra Zero e o item 5 (desfecho explícito) |
| Áudio (24min30s, AAC) | ✅ | ✅ desfecho explícito pela propiciação ("o perdão sem uma justiça prévia não é amor, é só conivência"); citou Morris, Packer e Nicole nominalmente |
| Relatório (1.188 palavras) | ✅ | ❌ **só citou Dodd** — zero menção a Morris/Nicole/Packer, conclusão adotou a tese de Dodd como "legado" |
| Mapa mental | ✅ | ✅ as quatro posições, atribuídas corretamente |
| Flashcards (50) | ✅ | ⚠️ posições corretas, mas ~10 cartões fora do tema; **grego saiu em LaTeX sem acento nem transliteração** (`$\iota \lambda \alpha \sigma \kappa \omicron \mu \alpha \iota$`) |
| Quiz (10) | ✅ | ⚠️ mesmo defeito do grego em LaTeX |
| Slides | ❌ falhou em todas as tentativas (`RPC invalid argument`) | — |

**Três lições que viram regra, herdadas diretamente para este projeto:**

1. **O NotebookLM tende à neutralidade** e, com a fonte adversária
   presente (Dodd), pode até concluir por ela. **Sem direção editorial
   explícita em cada prompt, a mídia viola a Regra Zero deste projeto.**
2. **Integridade técnica não prova conteúdo.** Do mesmo caderno saiu um
   áudio aprovado e um vídeo/relatório reprovados — cada artefato exige
   auditoria própria.
3. **Grego precisa de instrução explícita** (Unicode com acentos +
   transliteração + tradução), senão sai em LaTeX ilegível — regra que já
   está em `ESTRATEGIA_NOTEBOOKLM_HILAS.md` §6, agora com evidência
   concreta do próprio debate Dodd/Morris.

---

## 2. Escala deste projeto — um módulo, não cinco

O projeto `Tabernáculo` tem 5 anéis e 5 módulos de mídia. `Hilas` tem
**3 lexemas + 1 síntese** — cabe **um único módulo**, com uma série de 3
episódios (mesma lógica de série de `ESTRATEGIA_DE_USO.md` §4-B, aplicada
na escala certa):

| Módulo | Cobertura | Fonte auditada |
|---|---|---|
| **HILAS-M1** | ἱλαστήριον → ἱλασμός → ἱλάσκομαι, como série progressiva | relatórios de U01, U02, U03 (nunca corpus bruto) |

### Regra de série — 3 episódios, não 3 sorteios independentes

| Episódio | Papel | Subtema | Personas (fixas, ver §3) |
|---|---|---|---|
| **1 — ἱλαστήριον** | fundação: introduz o vocabulário, Rm 3.25/Hb 9.5 | o *kapporet*, o anartro, a alusão ao Dia da Expiação | Lexicógrafo + Adversário fiel apresentam; Historiador da recepção ainda não entra |
| **2 — ἱλασμός** | aprofundamento: **cita explicitamente o que o Episódio 1 já estabeleceu** | 1Jo 2.2/4.10, a extensão universal, a resposta de Morris/Nicole/Packer ponto a ponto | os mesmos + Historiador da recepção entra em diálogo técnico com o Adversário fiel |
| **3 — ἱλάσκομαι** | síntese: recapitula os dois anteriores, fecha com Hb 2.17/Lc 18.13 e a Regra Zero | as duas construções verbais (objeto=Deus vs. objeto=pecados) harmonizadas; desfecho explícito da série inteira | volta o Guardião da Regra Zero, agora perguntando o que só faz sentido depois dos dois episódios anteriores |

**Cada prompt de geração do episódio 2+ cita o que os episódios anteriores
já cobriram** — evita que o Overview repita do zero, produz efeito de
progressão real.

---

## 3. O que o caderno de módulo recebe

Nunca corpus bruto. Kit de fontes montado do disco local:

1. Os `RELATORIO_TEMPLATE.md` preenchidos de U01, U02, U03 (`fase2-unidades/*/saidas/`).
2. **`GUIA_EDITORIAL_HILAS.md`** (a escrever, ver §4) — uma fonte curta,
   igual para os três episódios, com a linha editorial completa. Uma
   fonte *dentro* do caderno pesa em toda geração — o prompt sozinho não
   bastou no piloto do `TAB-95` (o vídeo saiu neutro apesar da instrução
   verbal).
3. Se reaproveitadas, as quatro fontes de `TAB-95` (Dodd, Morris, Nicole,
   Packer) — mas **só depois das seis portas** de `CURADORIA_FONTES_HILAS.md` §1.

## 4. `GUIA_EDITORIAL_HILAS.md` — conteúdo obrigatório (a escrever antes do primeiro `generate`)

- **A Regra Zero** (`CLAUDE.md` §2-B): a ira de Deus é pessoal, o
  sacrifício a satisfaz objetivamente; a leitura de Dodd que a esvazia é
  objeção a refutar, nunca "leitura alternativa igualmente válida".
  **Proibido "resumir de forma neutra"; proibido terminar em pergunta
  aberta** — desfecho explícito sempre.
- **Divergências internas legítimas** (o debate entre reformados,
  wesleyanos, pentecostais sobre a extensão de 1Jo 2.2, ver R5 de
  `sentinelas_HILAS.md`) aparecem **abertas entre autores conservadores**,
  sem refutação — não confundir com a Regra Zero, que vale só contra Dodd.
- **Grego:** alfabeto Unicode com acentos, seguido de transliteração e
  tradução. **Nunca LaTeX** — regra existe porque já falhou exatamente
  neste debate no piloto do `TAB-95`.
- **Só o que está nas fontes do caderno** — não acrescentar autores.
- **Rótulos preservados:** `[OBJETO=DEUS]` vs. `[OBJETO=PECADOS]` vs.
  `[HIPÓTESE DEBATIDA]` (ver `ESTRATEGIA_NOTEBOOKLM_HILAS.md` §6) não
  podem ser apagados por diagramação em mapa mental ou infográfico.

---

## 5. Verificação de cada artefato — nenhum é "pronto" por `completed`

| Camada | Como | Reprova se |
|---|---|---|
| Conclusão no servidor | `notebooklm artifact list -n <id> --json` | status ≠ `completed` |
| Arquivo | `verificar_artefato.py` (`_scripts/`) — assinatura binária, tamanho | assinatura errada, < 1 KB |
| Técnica (áudio/vídeo) | `ffprobe` — codec, duração | duração anormalmente curta |
| Idioma | ouvir/checar amostra | não é `pt_BR` |
| **Conteúdo (áudio/vídeo)** | **transcrição completa**, leitura do início, das transições e dos **últimos 2 minutos** | conclusão neutra ou a favor de Dodd sem resposta; autor citado que não está no caderno |
| **Conteúdo (texto)** | leitura integral (relatório, quiz, flashcards, mapa) | grego em LaTeX; rótulo `[OBJETO=...]` apagado; cartão fora do tema |
| Sentinelas | `_artifacts/sentinelas_HILAS.md` contra a transcrição | sentinela violada |
| Registro | `_artifacts/MEMORIA_DE_QUERIES.md` (query) + livro-razão do artefato | — |

**Reprovado → uma regeneração** com o prompt corrigido (conta na cota);
reprovado de novo → registrar e decidir com o usuário, nunca insistir em
laço. **Aprovado → só então considerado entregável.**

---

## 6. Ordem de execução

| Passo | O que | Pré-requisito |
|---|---|---|
| 1 | U01, U02, U03 escritas e auditadas (Fase 2 completa) | ver `FASE_0_CHECKLIST.md` |
| 2 | Escrever `GUIA_EDITORIAL_HILAS.md` e os 3 prompts de episódio | passo 1 concluído |
| 3 | Montar o caderno `HILAS-M1` com o kit de fontes (relatórios + guia) | `montar_caderno.py` |
| 4 | Gerar o **Episódio 1** primeiro (áudio + vídeo + relatório + quiz + flashcards + mapa mental + 1 tentativa de slide) | `prevoo_cota.py` antes |
| 5 | Auditar o Episódio 1 (§5) **antes** de gerar o Episódio 2 — ajustar o guia se algo reprovar | — |
| 6 | Episódios 2 e 3, um por dia (regra de cota, `ESTRATEGIA_NOTEBOOKLM_HILAS.md` §7) | — |

**Nunca gerar os três episódios no mesmo dia** — nem por cota, nem porque
o Episódio 2 depende do 1 já estar auditado (a citação "o que já
estabelecemos" só faz sentido se o que foi estabelecido está correto).
