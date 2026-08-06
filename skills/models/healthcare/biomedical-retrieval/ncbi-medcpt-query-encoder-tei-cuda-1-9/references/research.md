# Audited model research

## Contents

- [Identity](#identity)
- [Selection](#selection)
- [Input preparation](#input-preparation)
- [Output interpretation](#output-interpretation)
- [Public benchmarks](#public-benchmarks)
- [Comparisons](#comparisons)
- [Limitations and safety](#limitations-and-safety)
- [Related upstream agent skills](#related-upstream-agent-skills)
- [Primary sources](#primary-sources)
- [Evidence gaps](#evidence-gaps)

- Research key: `huggingface-co-ncbi-medcpt-query-encoder-5de2774603`
- Independent audit: `revised`
- Researched: `2026-08-06T13:07:55.926382+00:00`

Primary upstream sources (Hugging Face model card, upstream config/README, the authors' arXiv preprint and PMC article) show that ncbi/MedCPT-Query-Encoder is the MedCPT Query Encoder checkpoint intended to produce biomedical text embeddings for semantic search / dense retrieval. The model family is a dual-encoder design (query encoder + article encoder) initialized from PubMedBERT; the authors report contrastive pre-training on large-scale PubMed search logs (stated as 255 million query-article pairs in both the model card and the paper). The PMC/arXiv publications report zero-shot evaluation results on BIOSSES and MedSTS (Pearson correlations reported in the provided findings), but the primary sources as provided do not include an immutable checkpoint revision mapping to a precise published parameter count nor the exact table/figure locators for the two sentence-similarity benchmark rows in the findings. Important operational details for the exact Hugging Face checkpoint remain unspecified in the primary sources provided: immutable checkpoint metadata beyond a model-card commit, definitive checkpoint parameter count, pooling/extraction call signature, official normalization behavior, explicit tokenizer call signature, and per-output calibration metrics.

## Identity

- Upstream name: ncbi/MedCPT-Query-Encoder
- Checkpoint/version: ncbi/MedCPT-Query-Encoder
- Immutable revision: https://huggingface.co/ncbi/MedCPT-Query-Encoder/commit/851f0757800ee18a280b65514ecb57ed302d82db
- Parameter scale: Evidence gap: primary upstream sources provided do not report an immutable checkpoint-specific parameter count. A secondary/third-party claim of 109M exists in the research findings but is not present in the primary sources; primary paper/config do not report a definitive checkpoint parameter total.
- Architecture/head: BERT-based Transformer query encoder (Query Encoder initialized from PubMedBERT; dual-encoder MedCPT design with a Query Encoder and an Article Encoder)
- License: Public domain / United States Government Work per repository LICENSE files (model weights and code/database declared U.S. Government Work)
- Evidence: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json, https://huggingface.co/ncbi/MedCPT-Query-Encoder/commit/851f0757800ee18a280b65514ecb57ed302d82db, https://github.com/ncbi/MedCPT/blob/main/LICENSE, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/LICENSE, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md

## Selection

### Recommended

- **Biomedical semantic search and dense retrieval for short biomedical texts (queries, questions, sentences)** — Hugging Face model card and README identify the checkpoint as the MedCPT Query Encoder producing embeddings for semantic search; the paper/arXiv frame MedCPT as contrastively pre-trained for retrieval and report zero-shot embedding-based retrieval and sentence-similarity evaluations that support this use.
  Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder (Query Encoder only); applies to embedding generation and pairing with an Article Encoder for retrieval.
  Evidence: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md, https://arxiv.org/pdf/2307.00589, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430
- **Biomedical sentence-similarity representation (zero-shot evaluation contexts)** — The authors report BIOSSES and MedSTS Pearson correlation scores for the MedCPT query encoder in their primary paper/preprint, indicating the checkpoint produces embeddings applicable to sentence-similarity evaluation, subject to the protocol caveats below.
  Scope: MedCPT query encoder as reported in the authors' paper (zero-shot evaluation); confirm alignment with the exact Hugging Face checkpoint before production deployment.
  Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

### Conditional

- **Zero-shot biomedical information retrieval pipelines (query embedding → index retrieval → document ranking using Article Encoder and/or reranker)** — Use only when pipeline includes (a) the paired Article Encoder or compatible document encoder for similarity scoring, and (b) downstream validation on the target corpus/protocol. Authors' evaluations are zero-shot and rely on a paired retriever setup; do not assume retrieval results without the Article Encoder or a verified reranker.
  Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder paired with MedCPT Article Encoder (paper describes dual-encoder retriever and a separate cross-encoder re-ranker).
  Evidence: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589
- **Use in healthcare-adjacent literature support workflows (non-diagnostic retrieval, literature search assistance)** — Human expert review required; do not treat embeddings or retrieved documents as independently validated clinical recommendations. Authors do not provide clinical deployment validation or PHI handling guidance in the primary sources provided.
  Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder (Query Encoder only) used for retrieval/representation tasks.
  Evidence: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430

### Avoid

- **Using the model as a standalone clinical decision-maker or diagnostic system** — Primary sources do not report clinical validation, regulatory approval, or decision-making clinical evaluation for the checkpoint; the model is presented for semantic search / retrieval tasks and evaluated in zero-shot retrieval and sentence-similarity benchmarks, not as a diagnostic system.
  Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder
  Evidence: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430
- **Treating retrieval or similarity outputs as calibrated probabilities or confidence scores** — Primary sources do not report per-output confidence, calibration, or uncertainty outputs for the checkpoint; benchmark scores are aggregated Pearson correlations and do not supply per-output calibration.
  Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder
  Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

## Input preparation

### Semantic inputs

- Short biomedical text inputs (queries, questions, sentences) are the intended semantic input for the Query Encoder. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md
- The MedCPT system is dual-tower: a Query Encoder for short texts and an Article Encoder for documents (titles/abstracts). The Query Encoder is intended to generate embeddings to be compared with Article Encoder embeddings. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md

### Accepted formats

- Plain text input for embedding generation (text strings representing queries or short biomedical sentences). The model card identifies text input and embedding output for semantic search. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder

### Preprocessing

- Authors report contrastive pre-training on large-scale PubMed search logs (stated training corpus size: 255 million query-article pairs) in the paper and model card; however, explicit checkpoint-level tokenization/truncation/normalization preprocessing steps for runtime embedding extraction are not documented in the provided primary sources. Sources: https://arxiv.org/pdf/2307.00589, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://huggingface.co/ncbi/MedCPT-Query-Encoder
- The model's config.json in the upstream Hugging Face repository lists architecture and model hyperparameters (e.g., hidden_size) but does not specify pooling or embedding-extraction call semantics. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json

### Pre-submit validation

- Evidence gap: The provided primary sources do not state an official input-validation or malformed-input behavior schema for the upstream checkpoint (e.g., max token handling beyond config 'max_position_embeddings' and no explicit runtime error/exception contract). Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json

### Task-specific formatting

- Evidence gap: The primary sources do not provide an official prompt template, paired-input order, or task-specific text-formatting instructions for the Query Encoder; the model card and paper describe embedding use for retrieval but not a canonical input formatting template for the checkpoint. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

## Output interpretation

### Outputs

- The upstream checkpoint emits vector embeddings representing input biomedical text; intended usage is semantic similarity / dense retrieval. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md
- Embedding dimensionality: 768 (hidden_size reported in the upstream config.json). Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json

### Interpretation

- Embeddings are for representation and similarity scoring; reported benchmark metrics are aggregate (Pearson correlation on sentence-similarity datasets) and do not imply per-output calibrated probabilities. Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

### Post-inference validation

- Post-inference validation should include downstream evaluation on the target corpus and protocol (the authors evaluate in zero-shot settings; reproduce evaluation settings and verify retrieval/ranking when pairing the Query Encoder with the Article Encoder or an appropriate reranker). Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589, https://huggingface.co/ncbi/MedCPT-Query-Encoder
- Evidence gap: The primary sources do not provide checkpoint-level guidance on embedding normalization (L2 or otherwise) to be applied prior to similarity computation; implementer must validate expected normalization when reproducing authors' experiments. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://arxiv.org/pdf/2307.00589

## Public benchmarks

### Sentence similarity

- Dataset/split: BIOSSES / not reported
- Metric/value: Pearson correlation / 0.893 (`higher-is-better`)
- Model scope: MedCPT query encoder as reported in the authors' paper/preprint (zero-shot evaluation)
- Conditions: Reported as a zero-shot (unsupervised) evaluation of the MedCPT query encoder in the authors' paper; the provided primary sources do not include further checklist-level protocol details (exact split, preprocessing, or table locator) in the research findings.
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430
- Locator: Evidence gap: the exact table/figure/section/page locator for the BIOSSES Pearson correlation value is not provided in the supplied primary-source facts; PMC/arXiv report the numeric result but the findings do not include an exact locator string.
- Caveat: Benchmark reported as zero-shot Pearson correlation; the supplied primary sources do not provide explicit split or preprocessing protocol details for strict comparability.
- Caveat: ModelScope ambiguity: the paper reports results for the MedCPT query encoder, but the primary sources do not map an immutable checkpoint revision to a published parameter count; implementers should validate checkpoint identity when reproducing the reported result.

### Sentence similarity

- Dataset/split: MedSTS / not reported
- Metric/value: Pearson correlation / 0.765 (`higher-is-better`)
- Model scope: MedCPT query encoder as reported in the authors' paper/preprint (zero-shot evaluation)
- Conditions: Reported as a zero-shot (unsupervised) evaluation of the MedCPT query encoder in the authors' paper; the provided primary sources do not include further checklist-level protocol details (exact split, preprocessing, or table locator) in the research findings.
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430
- Locator: Evidence gap: the exact table/figure/section/page locator for the MedSTS Pearson correlation value is not provided in the supplied primary-source facts; PMC/arXiv report the numeric result but the findings do not include an exact locator string.
- Caveat: Benchmark reported as zero-shot Pearson correlation; the supplied primary sources do not provide explicit split or preprocessing protocol details for strict comparability.
- Caveat: ModelScope ambiguity: the paper reports results for the MedCPT query encoder; confirm exact checkpoint mapping before using reported numbers for runtime selection.

## Comparisons

### SciNCL — `prefer-this`

- Task: BIOSSES sentence similarity
- Criteria: Reported BIOSSES Pearson correlation value in the authors' primary paper shows a higher value for MedCPT versus SciNCL in the supplied findings.
- Rationale: The supplied primary-source facts report MedCPT Pearson=0.893 and SciNCL Pearson=0.847 on BIOSSES as stated in the paper/preprint.
- Comparison conditions: Evidence gap: the supplied primary-source facts do not include the exact table/figure/section locator or full protocol alignment details for both rows in a single table; comparability is based on the reported numeric values in the paper/preprint.
- Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

### BioSentVec — `tradeoff`

- Task: MedSTS sentence similarity
- Criteria: Reported MedSTS Pearson correlation values are near-parity in the supplied primary-source facts (MedCPT 0.765 vs BioSentVec 0.767).
- Rationale: The authors' reported MedSTS Pearson correlation values place MedCPT slightly below BioSentVec in the supplied facts; this supports a near-parity conclusion rather than a clear preference.
- Comparison conditions: Evidence gap: the supplied primary-source facts do not include the exact table/figure/section locator or any split/protocol specifics that would fully validate strict comparability.
- Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

### Google's GTR-XXL (4.8B) — `insufficient-evidence`

- Task: Biomedical document retrieval
- Criteria: Evidence gap: the supplied primary-source facts do not contain a direct, verifiable comparison row or protocol-aligned numeric result for GTR-XXL in the provided primary sources.
- Rationale: A comparison to very large proprietary models is not documented in the supplied primary-source facts; the paper/preprint facts included in the research findings do not provide an authoritative table/locator comparing MedCPT and GTR-XXL under the same protocol in the supplied evidence.
- Comparison conditions: Evidence gap: no primary-source locator or protocol alignment provided for this alternative in the supplied findings.
- Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

### OpenAI's cpt-text-XL (175B) — `insufficient-evidence`

- Task: Biomedical document retrieval
- Criteria: Evidence gap: the supplied primary-source facts do not contain a direct, verifiable comparison row or protocol-aligned numeric result for OpenAI cpt-text-XL in the provided primary sources.
- Rationale: The provided primary-source facts (paper and model card) do not include a table/locator comparing MedCPT with OpenAI's cpt-text-XL under a shared protocol; therefore a protocol-aligned preference cannot be supported from the supplied evidence.
- Comparison conditions: Evidence gap: no primary-source locator or protocol alignment provided for this alternative in the supplied findings.
- Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589

## Limitations and safety

### Limitations

- Evidence gap: The supplied primary sources do not report an immutable, published checkpoint revision or release tag that definitively maps the paper's reported results to a single persistent Hugging Face artifact beyond a repository commit URL. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/commit/851f0757800ee18a280b65514ecb57ed302d82db
- Evidence gap: The supplied primary sources do not provide a definitive checkpoint-specific parameter count for ncbi/MedCPT-Query-Encoder; the research findings include an unverified secondary claim of 109M but no authoritative primary-source parameter total. Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430, https://arxiv.org/pdf/2307.00589, https://huggingface.co/ncbi/MedCPT-Query-Encoder
- Evidence gap: The supplied primary sources do not document official pooling/pooling-module behavior (e.g., CLS token pooling vs mean pooling) or the exact embedding-extraction call signature for the checkpoint; implementers must inspect the upstream model code/serving wrapper to determine extraction behavior. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json, https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md
- Evidence gap: The supplied primary sources do not specify whether embeddings are implicitly L2-normalized by the official upstream code or model-card recommendation; normalization behavior must be validated by implementers. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://arxiv.org/pdf/2307.00589
- Evidence gap: The supplied primary sources do not provide explicit PHI handling, de-identification, or data-retention guidance for deployments involving protected health information. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://github.com/ncbi/MedCPT/blob/main/LICENSE

### Safety

- Evidence gap: The supplied primary sources do not assert that model outputs are clinically validated; treat outputs as retrieval/representation artifacts and require human expert review before clinical use. Sources: https://huggingface.co/ncbi/MedCPT-Query-Encoder, https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430
- Evidence gap: The supplied primary sources do not provide workflow-level PHI handling, de-identification procedures, or data-retention policies for deployments processing protected health information; organizational controls are required for sensitive-data deployments. Sources: https://github.com/ncbi/MedCPT/blob/main/LICENSE, https://huggingface.co/ncbi/MedCPT-Query-Encoder

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: ncbi/MedCPT-Query-Encoder

- URL: https://huggingface.co/ncbi/MedCPT-Query-Encoder
- Publisher: Hugging Face / NCBI
- Type: `model-card`
- Primary because: Official upstream model card and hosted checkpoint page for the exact checkpoint in scope.
- Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder.
- Supports: checkpoint identity
- Supports: intended use for semantic search / dense retrieval
- Supports: query-encoder scope
- Supports: training-data summary (255 million query-article pairs reported on model card)
- Supports: README/config references for architecture and hyperparameters

### Hugging Face checkpoint config.json (upstream)

- URL: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/config.json
- Publisher: Hugging Face / NCBI
- Type: `repository`
- Primary because: Upstream checkpoint configuration file listing architecture type and hyperparameter values (e.g., hidden_size).
- Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder (config.json).
- Supports: architecture (BertModel)
- Supports: embedding dimensionality (hidden_size=768)
- Supports: max_position_embeddings (512)
- Supports: vocabulary size metadata

### Hugging Face checkpoint README (upstream)

- URL: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/README.md
- Publisher: Hugging Face / NCBI
- Type: `model-card`
- Primary because: Upstream README describing the Query Encoder, intended inputs, and pairing with Article Encoder.
- Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder (README).
- Supports: query vs article encoder division
- Supports: intended use cases (semantic search / embeddings)
- Supports: training-data summary claim

### Hugging Face checkpoint repository commit (referenced)

- URL: https://huggingface.co/ncbi/MedCPT-Query-Encoder/commit/851f0757800ee18a280b65514ecb57ed302d82db
- Publisher: Hugging Face / NCBI
- Type: `repository`
- Primary because: Upstream repository commit visible in the hosted checkpoint repository (used as the best-available revision locator in the supplied primary sources).
- Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder (specific commit).
- Supports: repository-level revision evidence (commit URL)

### NCBI MedCPT repository LICENSE (GitHub)

- URL: https://github.com/ncbi/MedCPT/blob/main/LICENSE
- Publisher: NCBI (GitHub repository)
- Type: `repository`
- Primary because: Official LICENSE file from the model authors' repository indicating U.S. Government Work / public-domain status.
- Scope: MedCPT repository licensing.
- Supports: license (public-domain / U.S. Government Work)

### Hugging Face LICENSE file for MedCPT-Query-Encoder

- URL: https://huggingface.co/ncbi/MedCPT-Query-Encoder/blob/main/LICENSE
- Publisher: Hugging Face / NCBI
- Type: `repository`
- Primary because: LICENSE file co-located with the hosted checkpoint confirming license assertions on the Hugging Face hosting page.
- Scope: Upstream checkpoint ncbi/MedCPT-Query-Encoder licensing.
- Supports: license (public-domain / U.S. Government Work)

### MedCPT published article (PMC12478430)

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478430
- Publisher: PubMed Central / article authors
- Type: `paper`
- Primary because: Peer-reviewed article (PMC) by the model authors reporting benchmark numeric results and training framing used in the dossier.
- Scope: MedCPT paper-reported benchmark and comparison results (as provided in the research findings).
- Supports: BIOSSES and MedSTS reported Pearson correlations for MedCPT query encoder
- Supports: zero-shot/unsupervised evaluation framing
- Supports: high-level comparisons reported in the paper facts included in the research findings

### MedCPT arXiv preprint PDF

- URL: https://arxiv.org/pdf/2307.00589
- Publisher: arXiv / article authors
- Type: `paper`
- Primary because: Authors' preprint describing training approach, dataset-size claim (255M query-article pairs) and zero-shot evaluation that supports use-case framing.
- Scope: MedCPT training and task framing (preprint).
- Supports: contrastive pre-training on PubMed search logs (255M query-article pairs reported in the findings)
- Supports: zero-shot evaluation protocol statements in the supplied facts

## Evidence gaps

- Exact immutable upstream checkpoint revision mapping the paper's reported results to a single persistent release tag is not provided in the supplied primary sources (commit URL is the best-available locator).
- Exact checkpoint-specific parameter count for ncbi/MedCPT-Query-Encoder is not reported in the supplied primary sources; a secondary claim of 109M exists in the research findings but is not present in the primary sources and therefore is an evidence gap for checkpoint-level parameter reporting.
- Exact sourceLocator (table/figure/section/page) for the BIOSSES Pearson correlation value (0.893) is not included in the supplied primary-source facts; the numeric value is present in the findings but the precise locator string is missing.
- Exact sourceLocator (table/figure/section/page) for the MedSTS Pearson correlation value (0.765) is not included in the supplied primary-source facts; the numeric value is present in the findings but the precise locator string is missing.
- Official pooling/extraction behavior (CLS pooling vs mean pooling) and the embedding-extraction call signature are not documented in the supplied primary sources and must be inferred from code or validated by implementers.
- Official embedding normalization behavior (e.g., L2 normalization) is not specified in the supplied primary sources.
- Tokenization call signature, tokenizer configuration file semantics, and explicit runtime tokenizer usage guidance are not fully documented in the supplied primary sources (config.json shows vocabulary size and max position embeddings but does not provide a full tokenizer runtime contract).
- Per-output confidence, uncertainty, or calibration measures for embeddings are not reported in the supplied primary sources.
- Benchmark split and full protocol details (e.g., exact data splits, preprocessing steps) for BIOSSES and MedSTS as used in the reported results are not provided in the supplied primary facts; strict comparability cannot be validated without these protocol details.
- PHI handling, de-identification, and data-retention guidance for healthcare deployments are not provided in the supplied primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ncbi/MedCPT-Article-Encoder Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
