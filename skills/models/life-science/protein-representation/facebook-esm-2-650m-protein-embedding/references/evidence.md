# Evidence

- Research status: `reviewed`
- Policy: Forge runtime latency/throughput evidence is operational placement data, not model-quality evidence.

## Deep research

- Research key: `huggingface-co-facebook-esm2-t33-650m-ur50d-e087b68cac`
- Independent audit: `revised`
- Full checkpoint-scoped selection, input/output, benchmark, comparison, limitation, and safety evidence: `research.md`.

## Reviewed public benchmark claims

### Evolutionary-scale prediction of atomic-level protein structure with a language model

- Primary source: https://www.biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text
- Checked: 2026-07-23
- Model/checkpoint scope: The paper's 15B-parameter ESM-2 plus its structure module, not the Forge 650M pooled-embedding endpoint.
- Dataset and split: CAMEO and CASP14 structure benchmarks / Public benchmark sets reported in the paper
- Metric and value: TM-score / 71.3 on CAMEO and 53.9 on CASP14 for the reported 15B ESM-2 structure module
- Direction: higher-is-better
- Provenance: reported
- Conditions: Paper-reported structure-module evaluation; no Forge reproduction is claimed.
- Caveat: This establishes model-family representation context, not embedding quality for the 650M pooled endpoint.
- Caveat: Do not compare these structure scores with retrieval, clustering, or classification metrics.

## Sources

- Exact model source/model card: https://huggingface.co/facebook/esm2_t33_650M_UR50D
- ESM-2 650M model card: https://huggingface.co/facebook/esm2_t33_650M_UR50D (model-card)
- Evolutionary-scale prediction of atomic-level protein structure with a language model: https://www.biorxiv.org/content/10.1101/2022.07.20.500902v1.full-text (paper)

The complete public Forge model and exact-skill snapshots are in `forge-model.json` and `forge-skill.json`.
