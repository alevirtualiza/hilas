# Checklist de auditoria — Hilas

*Adaptado de `CHECKLIST_AUDITORIA.md` do projeto-irmão `Tabernáculo`
(escala de 32 lóci) para a escala deste projeto (3 unidades + síntese).
Rodar antes de consolidar qualquer relatório de unidade ou o relatório
final.*

## Por unidade (U01, U02, U03), antes de fechar

- [ ] Toda afirmação tem rótulo de certeza (ver `_artifacts/escala_certeza.md`)?
- [ ] Toda forma grega/hebraica vem com transliteração e tradução?
- [ ] Nenhuma forma acentuada foi afirmada a partir de OCR sem confirmação
      no original (ver Regra 14 do `CLAUDE.md`)?
- [ ] A objeção de Dodd (e herdeiros) fecha com resposta pelo padrão de
      cinco itens — nunca "há debate"?
- [ ] As sentinelas que incidem nesta unidade (`sentinelas_HILAS.md`) foram
      conferidas — e, se tocadas, a formulação está correta?
- [ ] Toda citação foi conferida contra fonte primária (`conferir_citacoes.py`),
      nunca aceita de resumo de terceiros ou de saída de IA?
- [ ] A distinção `[OBJETO=DEUS]` / `[OBJETO=PECADOS]` / `[HIPÓTESE
      DEBATIDA]` está presente e não foi apagada por diagramação?
- [ ] Alguma lacuna real foi declarada em vez de preenchida por inferência?
- [ ] `buscar_grego.py --teste` foi rodado na fonte grega usada, e não
      houve declaração de ausência a partir de busca literal acentuada?

## Antes da síntese (U04)

- [ ] U01, U02 e U03 têm relatório, ou lacuna declarada com o que falta
      nomeado?
- [ ] O caderno de síntese (`HILAS-U04-Sintese`, se usado) recebeu os
      **relatórios auditados**, não os PDFs?
- [ ] Alguma contradição entre unidades foi detectada e devolvida à
      unidade de origem, não decidida na síntese?
- [ ] A harmonização entre Lc 18.13 (objeto=Deus) e Hb 2.17
      (objeto=pecados) foi feita sem descartar nenhuma das duas
      construções (ver sentinela R10)?

## Antes de qualquer mídia (ver `ESTRATEGIA_MIDIA_HILAS.md`)

- [ ] Todo artefato foi verificado por `verificar_artefato.py`
      (`status: completed`, assinatura, tamanho) — não apenas por existir?
- [ ] O áudio/vídeo saiu de fato em `pt_BR`?
- [ ] A regra de série de 3 episódios (progressão, citação do episódio
      anterior) foi cumprida ou a exceção está declarada?
- [ ] Nenhum artefato terminou em desfecho neutro ou favorável a Dodd sem
      a resposta de Morris/Nicole/Packer?
