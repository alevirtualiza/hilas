# Memória do projeto — Hilas

**Estado em 27/09/2026:** projeto gerado a partir do molde de pesquisa
exegética (ver `ANATOMIA_DO_MOLDE.md`), adaptado ao recorte lexical dos
três `hilas` (ἱλαστήριον / ἱλασμός / ἱλάσκομαι), e enriquecido com dados
já verificados por um projeto-irmão mais avançado (`Dikaiosyne Theou`),
que trata a mesma tríade como parte de um recorte maior.

## O que já está pronto

- Estrutura completa de pastas, `CLAUDE.md`, `ESCOPO_HILAS.md`.
- `_artifacts/sentinelas_HILAS.md` — 11 rascunhos, 3 deles já com dado
  gramatical confirmado no NA28 pelo projeto-irmão (anartro em Rm 3.25;
  objeto = pecados em Hb 2.17; extensão universal em 1Jo 2.2) — mas
  **nenhuma migrada para a tabela oficial ainda** (trava ativa por design).
- `_scripts/buscar_grego.py` — testado, aprova grego em NFC/NFD misto.
- `_scripts/verificar_sentinelas.py`, `dossie.py`, `conferir_citacoes.py`,
  `checagem_retomada.py` — todos testados e funcionando.
- `CURADORIA_FONTES_HILAS.md` — protocolo de seis portas + inventário do
  que já foi medido em acervos irmãos (NA28 aprovado, UBS5 vetado, BDAG
  aprovado com ressalva, Dodd 1931/1935 e Nicole 1955 ainda ausentes em
  qualquer acervo verificado).
- `LACUNAS_REFUTACAO.md` — 5 objeções mapeadas, nenhuma conferida ainda.
- `.claude/settings.json` — hook `PreToolUse` ligado a `verificar_sentinelas.py`.

## Biblioteca

**1 arquivo aprovado:** `NA28_Novum-Testamentum-Graece.md` (638.153
palavras, Tier S) — enviado pelo usuário em 28/09/2026, extraído e
conferido nesta sessão pelas seis portas. As seis ocorrências da tríade
foram lidas e confirmadas ao vivo.

**Em espera, aguardando upload do usuário** (confirmados em listagem real
do `biblioteca/` do projeto-irmão `Tabernáculo`, 28/09/2026): Morris
(*Apostolic Preaching of the Cross*), Nicole (*Our Sovereign Saviour*),
Packer (*Knowing God*), Harrison (*Levítico*, TNTC), Milgrom (*Leviticus
1-16*), Wenham (*Leviticus*, NICOT), BDB (léxico hebraico), UBS5 (só para
reconfirmar o veto).

**Ainda não localizados em nenhum acervo:** Dodd (*The Bible and the
Greeks*), BDAG, Thayer, Moulton-Milligan — não apareceram na listagem do
`Tabernáculo`; aguardando listagem da pasta `Justiça-de-Deus\biblioteca`.

## Próxima ação

1. Decidir se este projeto terá acesso aos acervos dos projetos irmãos
   para reaproveitamento (ver `FASE_0_CHECKLIST.md` etapa 3) — em
   particular o caderno `TAB-95-TRIADE-HILASMOS` do `Tabernáculo`, que já
   tem Dodd, Morris, Nicole e Packer convertidos e testados — ou se a
   aquisição será feita do zero.
2. Adquirir/localizar ao menos uma edição grega do NT e validá-la com
   `buscar_grego.py --teste`.
3. Começar a migrar sentinelas para a tabela oficial — R3 (anartro em
   Rm 3.25) e R10 (objeto de Hb 2.17) já têm dado gramatical confirmado
   e são as mais rápidas de fechar.
4. Abrir a Fase 1 (12 prompts, `fase1-introducao/prompts_HILAS.md`).
5. NotebookLM: usar o plugin real `notebooklm-py`
   (github.com/teng-lin/notebooklm-py, `pip install notebooklm-py`) — a
   sintaxe dos três scripts em `_scripts/` (`montar_caderno.py`,
   `prevoo_cota.py`, `verificar_artefato.py`) foi conferida contra o
   código-fonte real (v0.8.3), mas nenhum foi executado contra conta real.
   Login e escolha de conta são manuais (`ESTRATEGIA_NOTEBOOKLM_HILAS.md` §9).
6. Mídia: só depois de U01-U03 auditadas — ver `ESTRATEGIA_MIDIA_HILAS.md`,
   que já incorpora o piloto real e auditado do `TAB-95` (vídeo e relatório
   reprovaram por violar a Regra Zero; áudio e mapa mental aprovaram).

## Decisões pendentes (ver `ESCOPO_HILAS.md` §9)

1. Fonte de acesso a Dodd 1931 (artigo de periódico).
2. Se Hebreus entra como corpus unificado ou ocorrências isoladas.
3. Se Filo/Josefo sobre o Dia da Expiação entram como Círculo 4 pleno.
