# Memória de queries — Hilas

*Toda query de consulta (`ask`) ou de geração de artefato de Studio
(`generate`) é **escrita aqui antes de disparar** — Regra 1 de
`ESTRATEGIA_NOTEBOOKLM_HILAS.md` §6/§4. Nenhuma query dispara direto na
CLI sem passar por este arquivo primeiro.*

## Modelo de entrada

```
### <N>. <ASK|GENERATE tipo> — <data> <hora> UTC — caderno: <HILAS ...>

<texto exato da query, em português, com a trava anti-alucinação incluída>

Resultado: <PENDENTE | ver saída em fase.../saidas/NN.md | reprovado, motivo>
```

## Trava anti-alucinação obrigatória em toda query

Todo `ask` e todo `generate` inclui, no próprio texto da query:

> "Responda estritamente com as fontes carregadas neste caderno. Se a
> pergunta pedir algo que as fontes não cobrem, declare a ausência
> explicitamente em vez de completar com conhecimento externo. Ao final,
> liste as fontes específicas (arquivo/autor) que sustentam cada
> afirmação."

---

## Queries registradas

*(vazio — nenhuma query disparada ainda, ver `ESTRATEGIA_NOTEBOOKLM_HILAS.md`
§1: nenhuma operação de NotebookLM foi executada neste projeto)*
