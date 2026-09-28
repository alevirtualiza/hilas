# Fase 0 — do zero ao primeiro relatório

## Etapas

1. ✅ **Estrutura gerada** (27/09/2026) — `CLAUDE.md`, `ESCOPO_HILAS.md`,
   `ANATOMIA_DO_MOLDE.md`, `_artifacts/`, `_scripts/`, `fase1-introducao/`,
   `fase2-unidades/`.
2. ⬜ **Aquisição Tier S mínima** — ver `ESCOPO_HILAS.md` §8 e
   `CURADORIA_FONTES_HILAS.md` §2. Prioridade: Dodd (1931/1935), Nicole
   (1955), Morris (1955, se não reaproveitado), BDAG, TDNT.
3. ⬜ **Reaproveitamento, se aplicável** — se este projeto tiver acesso aos
   acervos dos projetos irmãos (`Dikaiosyne Theou`, `Justica-de-Deus`),
   rodar as seis portas de `CURADORIA_FONTES_HILAS.md` §1 sobre NA28, BDAG,
   Thayer, Moulton-Milligan e a nota de Dodd em *The Johannine Epistles* —
   todos já pré-aprovados lá, faltando só a Porta 6 (tier próprio).
4. ⬜ **Validar `buscar_grego.py`** contra a edição grega adquirida —
   `python3 _scripts/buscar_grego.py --teste biblioteca/<arquivo>.md` deve
   aprovar antes de qualquer citação lexical.
5. ✅ **Etapa de sentinelas concluída em 28/09/2026** — 6/6 migradas para a
   tabela oficial, cada uma verificada contra fonte primária real (NA28 +
   Morris, que cita Dodd e Nicole diretamente). `verificar_sentinelas.py`
   retorna exit 0 [PRONTO]. A trava de escrita em `saidas/` está liberada.
6. ⬜ **Fase 1** — rodar os 12 prompts de `fase1-introducao/prompts_HILAS.md`,
   com auditoria em pelo menos 8 deles (consulta de verificação depois de
   cada resposta).
7. ⬜ **Fase 2** — abrir U01 (ἱλαστήριον) primeiro por ser o texto mais
   citado (Rm 3.25) e o que já tem mais dado gramatical confirmado
   (anartro). Ordem recomendada: **U01 → U03 → U02 → U04** (a síntese por
   último, com os três relatórios na mesa).

## Critério de saída da Fase 0

`verificar_sentinelas.py` retorna exit 0 **e** ao menos uma edição grega do
NT passou no teste de `buscar_grego.py` **e** as obras Tier S mínimas
(Dodd, Nicole) estão em `biblioteca/` ou a lacuna está declarada em
`CURADORIA_FONTES_HILAS.md`.
