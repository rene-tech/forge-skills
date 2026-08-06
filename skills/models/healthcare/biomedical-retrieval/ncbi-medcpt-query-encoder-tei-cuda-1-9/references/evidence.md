# Evidence

- Research status: `reviewed`
- Policy: Forge runtime latency/throughput evidence is operational placement data, not model-quality evidence.

## Deep research

- Research key: `huggingface-co-ncbi-medcpt-query-encoder-5de2774603`
- Independent audit: `revised`
- Full checkpoint-scoped selection, input/output, benchmark, comparison, limitation, and safety evidence: `research.md`.

## Reviewed public benchmark claims

### MedCPT: Contrastive Pre-trained Transformers with large-scale PubMed search logs for zero-shot biomedical information retrieval

- Primary source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430/
- Checked: 2026-07-23
- Model/checkpoint scope: The full 330M-parameter MedCPT dual-encoder retrieval system, not the Forge query encoder in isolation.
- Dataset and split: Five biomedical BEIR tasks reported in the MedCPT paper / Paper-defined zero-shot evaluation
- Metric and value: nDCG@10 / The paper reports best performance on three of five tasks and the best average among compared dense retrievers
- Direction: higher-is-better
- Provenance: reported
- Conditions: Full paired query/article system trained from 255 million PubMed query-article pairs; no Forge scientific-benchmark reproduction is claimed.
- Caveat: The result depends on the compatible article encoder, corpus preparation, indexing, and similarity pipeline.
- Caveat: Do not attribute the full-system ranking result to the single query-embedding endpoint.

## Sources

- Exact model source/model card: https://huggingface.co/ncbi/MedCPT-Query-Encoder
- MedCPT paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430/ (paper)
- MedCPT repository: https://github.com/ncbi/MedCPT (repository)
- MedCPT Query Encoder model card: https://huggingface.co/ncbi/MedCPT-Query-Encoder (model-card)

The complete public Forge model and exact-skill snapshots are in `forge-model.json` and `forge-skill.json`.
