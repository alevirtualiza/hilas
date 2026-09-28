# Memória do projeto — Hilas

**Estado em 28/09/2026:** projeto gerado a partir do molde de pesquisa
exegética (ver `ANATOMIA_DO_MOLDE.md`), adaptado ao recorte lexical dos
três `hilas` (ἱλαστήριον / ἱλασμός / ἱλάσκομαι). **Fase 0 concluída.**

## O que já está pronto

- Estrutura completa de pastas, `CLAUDE.md`, `ESCOPO_HILAS.md`.
- `_artifacts/sentinelas_HILAS.md` — **7/6 sentinelas na tabela oficial**,
  todas verificadas contra fonte primária real deste projeto (não mais
  "achado de projeto-irmão"): dado gramatical do NA28 lido ao vivo (anartro
  em Rm 3.25; objeto=pecados em Hb 2.17; extensão de 1Jo 2.2); o método
  real de Dodd e a crítica de Nicole citados literalmente por Morris; e o
  bug de variante de glifo grego (ϑ/θ) corrigido no `buscar_grego.py`.
- `_scripts/`: `buscar_grego.py` (testado, robusto a NFC/NFD misto e a
  variantes de glifo grego), `verificar_sentinelas.py`, `hook_sentinelas.py`,
  `dossie.py`, `conferir_citacoes.py`, `checagem_retomada.py`,
  `montar_caderno.py`, `prevoo_cota.py`, `verificar_artefato.py` (os três
  últimos com sintaxe conferida contra o código-fonte real do
  `notebooklm-py`, não executados contra conta real).
- `CURADORIA_FONTES_HILAS.md` — protocolo de seis portas + registro de
  todas as aprovações reais feitas nesta sessão.
- `ESTRATEGIA_NOTEBOOKLM_HILAS.md`, `ESTRATEGIA_MIDIA_HILAS.md` — cadernos
  e mídia, incorporando o piloto real do `TAB-95` (projeto-irmão).
- `LACUNAS_REFUTACAO.md` — 5 objeções mapeadas, nenhuma conferida ainda.
- `.claude/settings.json` — hook `PreToolUse` ligado a `hook_sentinelas.py`.

## Biblioteca — 11 arquivos aprovados

| Arquivo | Tier |
|---|---|
| `NA28_Novum-Testamentum-Graece.md` | S |
| `Morris_Apostolic_Preaching_of_the_Cross.md` | S |
| `Nicole_Our_Sovereign_Saviour.md` | S |
| `Packer_KnowingGod.md` | S |
| `Harrison_Levitico_Introducao_e_Comentario_PT.md` | A1 |
| `BDB_Hebrew_Lexicon_1906_P1de3.md` / `P2de3.md` / `P3de3.md` | S |
| `Milgrom_Leviticus1-16_P1de2.md` / `P2de2.md` | S |
| `UBS5_The-Greek-New-Testament.md` | S |

**🎉 Fase 0 (etapa de sentinelas) CONCLUÍDA.** `verificar_sentinelas.py`
retorna exit 0 [PRONTO] — a trava de escrita em `saidas/` está liberada.

**Pendente, localizado, falta só pedir:**
- BDAG — confirmado em `Justiça-de-Deus\_processados_md\BDAG_Greek_English_Lexicon_NT_OCRv2.md`.
- Wenham, *The Book of Leviticus* (NICOT) — confirmado em `Tabernáculo\biblioteca`.

**Ainda não localizado em nenhuma das duas pastas irmãs verificadas:**
Dodd (*The Bible and the Greeks* — mitigado: Morris cita seu método e o
artigo de Nicole extensamente), Thayer, Moulton-Milligan, o artigo de
Nicole de 1955 (distinto do livro já no projeto), TDNT, Stott, Carson,
Travis, Louw-Nida, Ritschl.

## Próxima ação

1. **Pedir BDAG e Wenham** (localizados, só falta o upload).
2. **Abrir a Fase 1** (12 prompts, `fase1-introducao/prompts_HILAS.md`) —
   já há material para responder aos blocos A, B e C.
3. Considerar abrir a Unidade 01 (ἱλαστήριον) — já tem NA28, UBS5, BDB,
   Morris, Milgrom e Harrison como corpus mínimo, mais que suficiente.
4. NotebookLM: usar o plugin real `notebooklm-py`
   (github.com/teng-lin/notebooklm-py, `pip install notebooklm-py`) — a
   sintaxe dos três scripts foi conferida contra o código-fonte real
   (v0.8.3), mas nenhum foi executado contra conta real. Login e escolha
   de conta são manuais (`ESTRATEGIA_NOTEBOOKLM_HILAS.md` §9).
5. Mídia: só depois de U01-U03 auditadas — ver `ESTRATEGIA_MIDIA_HILAS.md`.

## Decisões pendentes (ver `ESCOPO_HILAS.md` §9)

1. Fonte de acesso a Dodd 1931/1935 e ao artigo de Nicole 1955.
2. Se Hebreus entra como corpus unificado ou ocorrências isoladas.
3. Se Filo/Josefo sobre o Dia da Expiação entram como Círculo 4 pleno.
