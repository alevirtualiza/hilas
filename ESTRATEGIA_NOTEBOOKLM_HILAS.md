# Estratégia de cadernos e artefatos no NotebookLM — Hilas

> **Estado em 27/09/2026: nenhuma operação executada.** Nenhum caderno
> criado, nenhuma fonte enviada, nenhuma autenticação feita. Esta página
> descreve o *quando* e o *como*; a execução é passo posterior, com login
> manual do dono e com a biblioteca já povoada (ver `FASE_0_CHECKLIST.md`).
>
> **Adaptado de `ESTRATEGIA_NOTEBOOKLM.md` de um projeto irmão (ISA-PAU,
> Isaías↔Paulo).** A arquitetura, os gatilhos, as quatro portas, as regras
> invioláveis, o esquema de verificação e o achado central sobre o
> NotebookLM são **agnósticos ao tema** e transferem inteiros. O que muda é
> o número de cadernos (4 unidades aqui, não 14), as vozes (adaptadas ao
> debate Dodd/Morris, não Isaías/Paulo) e a quinta trava de rótulo
> (aqui: objeto gramatical do verbo, não grau de dependência literária).

**Conta:** `<definir — ver §9, decisão do dono>` · **Perfil CLI:** `hilas-pro`
**Queries:** `_artifacts/MEMORIA_DE_QUERIES.md` — escritas **antes** de disparar

---

## 1. A decisão de arquitetura

**6 cadernos, não um.** Mesmo achado medido nos projetos-irmãos: com ~10-15
fontes curtas por caderno, uma consulta alcança o corpus inteiro; com
dezenas de PDFs, o RAG toca poucas por consulta, e **as que não tocou
produzem falso negativo indistinguível de ausência**. Num projeto cuja tese
central é uma disputa de leitura sobre poucos versículos (Rm 3.25; 1Jo 2.2,
4.10; Lc 18.13; Hb 2.17, 9.5), diluir o corpus é o erro mais caro possível.

| Caderno | Papel | Entrada permitida | Saída |
|---|---|---|---|
| `HILAS F1 - Introducao` | os 12 prompts da Fase 1 | lexical hebraico/grego · LXX · gramática · história da questão | 12 saídas + relatório |
| `HILAS U01 - Hilasterion` | dossiê de Rm 3.25 / Hb 9.5 | NA28, BDAG, TDNT, Morris, Dodd (o que houver), comentários de Romanos/Hebreus sobre esses versos | 1 relatório |
| `HILAS U02 - Hilasmos` | dossiê de 1Jo 2.2 / 4.10 | idem + comentários joaninos, a nota de Dodd em *The Johannine Epistles* | 1 relatório |
| `HILAS U03 - Hilaskomai` | dossiê de Lc 18.13 / Hb 2.17 | idem + comentários de Lucas e Hebreus sobre esses versos | 1 relatório |
| `HILAS U04 - Sintese` | coerência transversal | 🔴 **somente os 3 relatórios auditados** — nunca corpus bruto | mapa de consistência |

**Nomenclatura sem acento** (mesma cautela do `.ps1` original: a CLI não
trata UTF-8 de forma uniforme em todo ambiente) e **prefixo `HILAS`
obrigatório** — numa conta com cadernos de outros projetos, é o único
filtro visual que existe.

### Cadernos de círculo (C0-C5) — ver `ESTRATEGIA_CIRCULOS_HILAS.md`

Além dos cinco acima, o projeto tem **seis cadernos de aprofundamento**,
um por círculo concêntrico do `ESCOPO_HILAS.md` §4 — `HILAS C0 - Nucleo
Lexical` até `HILAS C5 - Historia da Interpretacao`. Diferente dos
U01-U04 (exegese fechada dos 6 versículos-âncora), os cadernos de círculo
**aprofundam o entorno** via Deep Research própria e **geram mídia
diretamente** (6 áudios, 4 vídeos, mapa mental, relatório, infográfico,
flashcards, por caderno) — ver `ESTRATEGIA_CIRCULOS_HILAS.md` para a
pauta de Deep Research de cada um e o pacote completo de mídia.
**Total de cadernos do projeto: 11.**

### O caderno de síntese não recebe os PDFs

Recebe **os relatórios já auditados** das U01-U03. Mesma razão medida nos
dois projetos-irmãos: (1) os rótulos de certeza e o rótulo de objeto
gramatical sobrevivem; (2) o retrieval alcança tudo com poucas fontes
curtas; (3) é onde a coerência transversal aparece — *"as três unidades
concordam sobre como a ira de Deus e o sacrifício se relacionam?"* só é
respondível contra os relatórios, não contra o corpus bruto.

**Regra decorrente:** a síntese **não decide questões novas**. Detecta
contradição e devolve à unidade de origem.

---

## 2. Os três gatilhos

```
Unidade escolhida (U01, U02 ou U03)
      |
Nucleo tecnico identificado PELO MIOLO (Regra 12) e triado    <- gatilho 1
      |
CADERNO DA UNIDADE criado; fontes Tier S/A, UMA A UMA
      |
Ciclo de consultas roda DENTRO do caderno
   exegetica -> verificacao -> refutacao dirigida -> controle
      |
Ficha auditada e dossie FECHADO                               <- gatilho 2
      |
ARTEFATOS DE MIDIA, a partir do dossie fechado
      |
RELATORIO auditado (nao o corpus) entra na SINTESE            <- gatilho 3
```

### Gatilho 1 — quando um caderno de unidade é criado

Duas condições, nenhuma delas "está listado em `CURADORIA_FONTES_HILAS.md`":

1. o núcleo técnico (Tier S/A) foi **identificado pelo miolo** — leitura
   real, não tier proposto por nome de arquivo (Regra 12);
2. as **Portas 1 e 2** (abaixo) passaram — autenticação real, conta correta.

> **Abrir os três cadernos de unidade de uma vez é permitido** se o núcleo
> técnico de todas já estiver pronto — mas povoar e trabalhar o dossiê é
> sequencial (ver ordem recomendada em `FASE_0_CHECKLIST.md`: U01 → U03 →
> U02 → U04). O que não é permitido: nenhum artefato antes do gatilho 2, e
> nenhum corpus bruto na síntese.

### Gatilho 2 — quando um artefato é gerado

**Nunca antes do dossiê estar fechado E auditado.** Uma unidade com uma
objeção sem resposta delimitada ainda pode gerar artefato — **desde que a
limitação esteja declarada dentro do próprio artefato**, nunca escondida.

### Gatilho 3 — o que entra na síntese

Só relatórios auditados de unidades fechadas, e **só depois que pelo menos
duas** tiverem dossiê fechado — comparação exige dois pontos.

---

## 3. As quatro portas — a primeira que reprovar aborta

| Porta | Verifica | Critério |
|---|---|---|
| **1** | Autenticação real | `auth check --test` — **não** `profile list` (pode dizer "authenticated" com token vencido) |
| **2** | Conta correta | conta é a definida em `projeto.config.txt`, **e** não existe caderno com o **mesmo nome exato** a criar (checar na listagem real, não só no config) |
| **3** | Fontes elegíveis | existem em `biblioteca/` e ficam **abaixo do teto medido** — não presumir 450 mil/500 mil/525 mil de memória; **medir nesta conta** (ver `CLAUDE.md` — o mesmo alerta do molde original: número redondo de precaução gera alarme falso sobre obra que já passou) |
| **4** | Resultado | contar as fontes **na listagem do caderno**, nunca na saída do comando de envio |

⚠️ **Numa conta compartilhada com outros projetos** (cenário mais provável
aqui, dado que os projetos-irmãos já usam contas com múltiplos cadernos):
ver **algum** caderno pré-existente na listagem é **esperado**, não sinal de
falha — a Porta 2 verifica **nome exato duplicado**, não ausência total de
outros cadernos. Se a conta for nova e exclusiva, aí sim listagem vazia é o
estado esperado — **confirmar qual dos dois cenários se aplica antes de
interpretar o resultado da Porta 2** (achado real do projeto-irmão ISA-PAU:
a premissa "conta nova e exclusiva" caiu por medição depois de escrita).

**Ao fim:** UUID em `projeto.config.txt`, resultado em `_LOG_EXECUCAO.md`.

---

## 4. Regras invioláveis

1. ⛔ **`notebooklm use` é PROIBIDO.** Grava estado **global**, compartilhado
   entre todas as janelas. `-p <perfil>` e `-n <id>` **explícitos em todo
   comando**; `-p` é opção global e vem **antes** do subcomando.
2. **Fonte por vez**, todas `ready` antes de consultar.
3. **`source delete` manual ANTES** de qualquer `source clean` — a limpeza
   automática pode remover fonte aprovada, e **remoção não tem desfazer**.
4. **Sempre `-Simular`/`--dry-run`** antes de enviar ou remover.
5. **Saídas de IA e Tier D não entram** em caderno nenhum.
6. **NUNCA** `notebooklm ask > arquivo.md` — risco de despejo em encoding
   errado. Redigir a resposta e usar a ferramenta Write.
7. **Consulta de verificação obrigatória** após cada bloco — audita a
   consulta anterior, não só busca o contraditório.
8. **Injetar o aviso de limitação de OCR, depois dividir — nesta ordem.**
   Invertido, a parte 2 sai sem aviso. O aviso vai **no corpo do `.md`**:
   assim o RAG o recupera junto com o trecho.

> 🔴 **O achado que governa tudo isto, medido em dois projetos-irmãos
> independentes:** *o NotebookLM completa o corpus com conhecimento externo,
> sem avisar.* Em ambos os casos a atribuição era plausível, específica,
> vinha com número de citação, e era **falsa quanto ao corpus** — e em
> ambos houve **retratação por escrito** na consulta seguinte, quando
> auditada. Não parece alucinação — **parece pesquisa**.

**Como formular a auditoria** (funcionou nos dois projetos): pedir, para
cada autor citado, a classificação `[FONTE PRIMÁRIA NO CORPUS]` /
`[CITADO POR TERCEIROS — quem?]` / `[NÃO ENCONTRADO]`, avisando
explicitamente que numa consulta anterior a ferramenta afirmou presença e
precisou se retratar. A distinção a forçar: *"a posição do autor é
discutida no corpus"* ≠ *"a obra do autor está no corpus"*.

---

## 5. As consultas por unidade

| # | Consulta | O que pega |
|---|---|---|
| 1 | **Exegética** | o material da unidade |
| 2 | **Verificação** — *quem, no dossiê, sustenta a leitura de Dodd para este texto?* | atribuições erradas; **e audita a consulta 1** |
| 3 | **Refutação dirigida** — *quem responde a esta objeção, e com quais textos da LXX?* | evita refutar por decreto |
| 4 | 🔑 **Controle** — *o que neste versículo específico NÃO decide sozinho entre propiciação e expiação?* | a petição de princípio — ver Eixo B do `ESCOPO_HILAS.md`: gramática nem sempre resolve teologia |

🔑 **Antes de qualquer uma delas:** `python3 _scripts/dossie.py "<termo>"
--listar` (custo zero) e, para termos gregos, `python3
_scripts/buscar_grego.py --listar "<raiz>" biblioteca/*.md` — dizem se a
obra sequer trata do assunto, sem gastar consulta. **Regra 11: RAG para
descobrir, disco para conferir.**

---

## 6. Artefatos — as quatro travas

*Detalhe e formulação das queries: `_artifacts/MEMORIA_DE_QUERIES.md`.*

| # | Trava | O erro que ela impede |
|---|---|---|
| 1 | **A query existe antes do artefato**, salva em arquivo | artefato sem query dirigida extrapola o dossiê e mistura o debate de uma unidade com o de outra |
| 2 | **Trava anti-alucinação em toda query**: "estritamente nas fontes carregadas neste caderno" + declarar ausência + citar fonte exata | o modelo completar o corpus sem avisar |
| 3 | 🔑 **Exigir que o artefato LISTE as fontes que usou** | proibição nominal sozinha não bastou nos projetos-irmãos — vários artefatos extrapolaram mesmo com a instrução "só as fontes" |
| 4 | **Uma geração por vez no mesmo caderno** | gerações em sequência tiveram prompts cruzados no servidor em casos medidos alhures |

### As cinco vozes deste projeto

| Voz | Papel |
|---|---|
| **Lexicógrafo** | BDAG, TDNT, LSJ, Louw-Nida — a faixa semântica pura |
| **Adversário fiel** | representa Dodd (e herdeiros) na sua **melhor formulação**, nunca espantalho |
| **Historiador da recepção** | Morris, Nicole, Stott, Carson, Travis — a resposta e a linhagem |
| **Pastor/Apologista** | a implicação para a fé e a prática |
| 🔑 **Guardião da Regra Zero** | *"este artefato terminou com desfecho explícito, ou ficou em 'há debate'?"* |

> **A quinta voz não é decorativa.** Em todo artefato que trate a disputa
> Dodd/Morris, ela recebe resposta nomeada dentro do próprio artefato,
> nunca deixada em aberto — é a aplicação, em mídia, da regra do desnível
> do `CLAUDE.md` §2-B. Um artefato que apresenta a objeção de Dodd sem
> fechar com a resposta de Morris/Nicole **viola a Regra Zero em mídia**,
> que é onde ela circula mais.

⚠️ **Nota de formato, medida em projetos-irmãos:** mesmo pedindo "narrado
sozinho, sem debate", o Audio Overview costuma sair no formato padrão de
dois apresentadores. A instrução de persona não controla o formato — só
influencia o conteúdo. Não gastar cota tentando forçar o formato.

### 🔴 A exigência própria deste projeto: o rótulo de objeto gramatical sobrevive ao artefato

Todo artefato sobre ἱλάσκομαι (U03) preserva a distinção `[OBJETO = DEUS]`
(Lc 18.13) vs. `[OBJETO = PECADOS]` (Hb 2.17) vs. `[AMBÍGUO/DISPUTADO]`
(ἱλαστήριον em Rm 3.25, quanto à alusão ao *kapporet*).

> **Infográfico e mapa mental tendem a apagar essa gradação visualmente.**
> Um diagrama que trata as duas construções verbais como equivalentes
> resolve por diagramação a própria disputa que a Unidade 04 existe para
> sintetizar com cuidado (ver `ESCOPO_HILAS.md` §3, Unidade 03). **Pedir
> explicitamente** que o artefato não iguale as duas construções.

---

## 7. Cota e saúde da geração

Comportamento medido em projetos-irmãos, transferível: **cota de Audio
Overview é diária e por conta inteira** (não por caderno), corte à meia-noite
UTC — **numa conta compartilhada com outros projetos, a cota é dividida**,
não exclusiva deste (ver Porta 2, a mesma premissa "conta nova e exclusiva"
caiu por medição alhures — reconferir aqui antes de assumir orçamento).

> ⚠️ **Sob escassez, gerar primeiro o que FECHA um par objeção/resposta,
> nunca o que só abre.** Um artefato que apresenta a leitura de Dodd e não
> entrega a de Morris/Nicole é pior que nenhum artefato.

⛔ **`CREATE_ARTIFACT timeout` é FALSO NEGATIVO** (Regra 11-D, herdada). O
RPC estoura aos 30s; o artefato quase sempre existe. **Não repetir o
comando** — fazer `artifact list`, depois `artifact wait <id>`. Idioma
`pt_BR`, com underscore, e **conferir o resultado** — já saiu áudio em
inglês mesmo com o parâmetro enviado.

| Controle | O que evita |
|---|---|
| `.lock` + idade do log | execução concorrente; lock órfão passando por ativo |
| Livro-razão de cota (`prevoo_cota.py`) | consumo invisível — o servidor não expõe uso restante |
| Checagem antes de gerar | regerar o que já existe |
| Espera por contagem, nunca por `poll`/`wait` sozinhos | esses comandos já mentiram alhures sobre estado |

---

## 8. Verificação — arquivo existir não prova conteúdo

1. **Cadernos** — contagem por título exato na listagem.
2. **Fontes** — contagem na listagem do caderno, uma a uma.
3. **Artefatos** — contagem com estado `completed`.
4. **Mídia** — inspeção do contêiner (`ffprobe`; revela `.m4a` que é outro
   formato) e assinatura binária.
5. **Idioma** — conferir que o áudio saiu em português.
6. 🔑 **Conteúdo** — transcrição integral conferida contra a ficha
   auditada da unidade. É o único passo que pega extrapolação; sem ele,
   um artefato errado passa por todos os outros cinco.

**Geração reprovada não se apaga** — sufixo `_v1-reprovado-<motivo>` ao
lado da versão aprovada. Mesmo princípio de "achado refutado se marca, não
se apaga" (ver `_artifacts/sentinelas_HILAS.md`).

---

## 9. O que continua manual, e por quê

**O login e a escolha da conta.** Autenticação não é automatizada, por
decisão de segurança — este projeto (rodando num container efêmero em
nuvem) não guarda credenciais de longo prazo. A decisão de qual conta
Google usar (nova e dedicada, ou uma conta já usada por projetos-irmãos)
é do dono; ver `MEMORIA_PROJETO.md` "decisões pendentes".

**Os tetos do plano se MEDEM, não se supõem.** Projetos-irmãos já
documentaram tetos diferentes (450 mil, 500 mil, 525 mil palavras/fonte,
conforme a conta e o momento) — nenhum deles vale por suposição aqui.
Calibrar entre o maior aprovado e o menor reprovado **nesta conta**, e
registrar o número em `_LOG_EXECUCAO.md`.

---

## 10. Scripts de apoio (ver `_scripts/`)

| Script | Função | Estado |
|---|---|---|
| `montar_caderno.py` | cria o caderno da unidade, envia fontes uma a uma, aguarda `ready`, grava UUID | ✅ escrito nesta sessão — **não testado** (requer CLI `notebooklm` e conta autenticada, ausentes neste ambiente) |
| `prevoo_cota.py` | livro-razão de cota antes de gerar artefato | ✅ escrito — mesma ressalva |
| `verificar_artefato.py` | baixa a transcrição/relatório e confere contra a ficha auditada da unidade | ✅ escrito — mesma ressalva |

⚠️ **Todos os três chamam a CLI `notebooklm` via subprocesso** com `-p` e
`-n` explícitos, seguindo a Regra 1 de §4. **Nenhum foi executado de
verdade** — este ambiente não tem a CLI instalada nem credenciais. Antes
do primeiro uso real: `notebooklm --version` e `notebooklm -p hilas-pro
auth check --test` têm de passar primeiro.
