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

- Research key: `huggingface-co-baai-bge-small-en-v1-5-58bedb4dd7`
- Independent audit: `revised`
- Researched: `2026-07-24T00:08:38.631682+00:00`

I audited the canonical Hugging Face repository locators for BAAI/bge-small-en-v1.5 and extracted checkpoint-scoped facts present in those locators (config.json, model page, commit page, vocab.txt). The config.json (blob commit) reports model_type "bert", architecture "BertModel", hidden_size 384, num_hidden_layers 12, max_position_embeddings 512, torch_dtype "float32", and vocab_size 30522. The Hugging Face model page for BAAI/bge-small-en-v1.5 reports multiple per-task benchmark numbers (MTEB-style aggregates and per-task groups) and documents embedding+reranker example workflows. The repository contains vocab.txt. I could not verify a tokenizer.json content at the inspected tokenizer path (see evidence gaps). I could not find an explicit license file or model-weight license text in the inspected commit/model-page facts included in the findings; therefore license-level distinction is not reported. Quantized/ONNX artifacts and parameter-count metadata are not confirmed in the inspected canonical HF locators in the provided findings; where primary locators lack explicit claims I recorded evidence gaps and limited recommendations to checkpoint-scoped claims supported by the documented config.json and model page numbers.

## Identity

- Upstream name: BAAI/bge-small-en-v1.5
- Checkpoint/version: v1.5
- Immutable revision: b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c
- Parameter scale: not reported
- Architecture/head: BertModel
- License: not reported
- Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c

## Selection

### Recommended

- **Semantic search / similarity search in vector databases** — The Hugging Face model page documents embedding extraction and an embedding-first retrieval workflow; the config.json and model page report a 384-dimensional embedding hidden size suitable for fixed-length vector similarity workflows.
  Scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
  Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md
- **Clustering of document embeddings** — The config.json reports hidden_size = 384 (fixed-length embeddings) and the model page describes embedding extraction; fixed-size vectors of that dimensionality are appropriate inputs for vector clustering algorithms.
  Scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
  Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json, https://huggingface.co/BAAI/bge-small-en-v1.5
- **Low-cost passage ranking (embedding stage for retrieval followed by a reranker)** — The model page and commit-level notes document an embedding+reranker workflow where a BGE embedding model retrieves candidates and a cross-encoder reranker re-ranks them; the README examples demonstrate loading a reranker with AutoModelForSequenceClassification.
  Scope: BAAI/bge-small-en-v1.5 (embedding stage; reranker is a separate model)
  Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md

### Conditional

- **CPU or quantized/ONNX builds for lower-latency/footprint inference** — Evidence gap: I did not find checkpoint-published quantized, ONNX, or alternative-format artifacts in the inspected canonical HF locators included in the findings; any downstream quantized/ONNX build must be validated by regression testing against the upstream checkpoint files listed in the repository before assuming behavior parity.
  Scope: BAAI/bge-small-en-v1.5 (downstream quantized/ONNX artifacts must be validated separately)
  Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c

### Avoid

- **High-stakes clinical decision-making or processing of PHI without documented risk controls** — Evidence gap: The inspected canonical v1.5 locators (README, commit, config.json, vocab) do not provide checkpoint-specific clinical/PHI handling, privacy, or deployment guidance; do not deploy for PHI/clinical decision tasks without expert review and documented controls.
  Scope: BAAI/bge-small-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c

## Input preparation

### Semantic inputs

- Text sequences (English) supplied as single strings or batches for embedding extraction. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md

### Accepted formats

- Plain text input accepted via Transformers / AutoTokenizer workflows as shown in the v1.5 README examples. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5

### Preprocessing

- The repository contains vocabulary/token artifacts (vocab.txt) and README usage examples; explicit upstream preprocessing rules (lowercasing, punctuation normalization, sentence splitting) are not exhaustively enumerated in the inspected README/vocab locators. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/vocab.txt, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md

### Pre-submit validation

- The config.json reports embedding dimensionality (hidden_size = 384) and maximum sequence length (max_position_embeddings = 512); validate input lengths and batching to these bounds in downstream code. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json
- Evidence gap: I did not find a tokenizer.json content listing special tokens or explicit tokenization type at the inspected tokenizer path; inspect tokenizer.json for tokenization-type and special-token behavior before deployment. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/tokenizer.json
- Evidence gap: The inspected locators do not publish a checkpoint-level list of invalid or ambiguous input cases; implement application-level input validation and test coverage. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c

### Task-specific formatting

- No official per-task prompt templates for embeddings are published in the inspected v1.5 README; embedding workflows rely on supplying plain text sequences to the tokenizer/model as shown in examples. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md

## Output interpretation

### Outputs

- Fixed-length embedding vector with dimensionality reported as 384 in the config.json and model page for bge-small-en-v1.5. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json, https://huggingface.co/BAAI/bge-small-en-v1.5

### Interpretation

- Similarity comparisons are interpreted as relative similarities between fixed-length vectors; the model page reports suggested similarity thresholds and notes that relative ordering is more important than absolute values (i.e., thresholds are model- and calibration-dependent). Sources: https://huggingface.co/BAAI/bge-small-en-v1.5
- The README examples set normalize_embeddings = True in example code (implying normalized embeddings are used in the example workflow); however, the repository does not prescribe a single canonical normalization or similarity metric for all uses. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5

### Post-inference validation

- Evidence gap: The inspected locators do not publish post-inference calibration thresholds or recommended downstream classifier/regressor head compatibility notes for this checkpoint; validate downstream models on held-out data. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c

## Public benchmarks

### MTEB - Average (56)

- Dataset/split: MTEB (average over 56 tasks) / not reported
- Metric/value: score (average) / 62.17 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details and exact splits not specified on the inspected page.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / reported aggregates
- Caveat: Protocol details (dataset splits, evaluation harness) are not reported on the inspected page; assume reported numbers are as-published on the model page without protocol detail.

### MTEB - Retrieval (15)

- Dataset/split: MTEB - Retrieval (15 tasks) / not reported
- Metric/value: score (average over retrieval subgroup) / 51.68 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / Retrieval (15)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

### MTEB - Clustering (11)

- Dataset/split: MTEB - Clustering (11 tasks) / not reported
- Metric/value: score (average over clustering subgroup) / 43.82 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / Clustering (11)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

### MTEB - Pair Classification (3)

- Dataset/split: MTEB - Pair Classification (3 tasks) / not reported
- Metric/value: score (average over pair classification subgroup) / 84.92 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / Pair Classification (3)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

### MTEB - Reranking (4)

- Dataset/split: MTEB - Reranking (4 tasks) / not reported
- Metric/value: score (average over reranking subgroup) / 58.36 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / Reranking (4)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

### MTEB - STS (10)

- Dataset/split: MTEB - STS (10 tasks) / not reported
- Metric/value: score (average over STS subgroup) / 81.59 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / STS (10)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

### MTEB - Summarization (1)

- Dataset/split: MTEB - Summarization (1 task) / not reported
- Metric/value: score / 30.12 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / Summarization (1)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

### MTEB - Classification (12)

- Dataset/split: MTEB - Classification (12 tasks) / not reported
- Metric/value: score (average over classification subgroup) / 74.14 (`higher-is-better`)
- Model scope: BAAI/bge-small-en-v1.5 (checkpoint v1.5)
- Conditions: As reported on the model page 'Benchmarks' section; protocol details not specified.
- Source: https://huggingface.co/BAAI/bge-small-en-v1.5
- Locator: model card 'Benchmarks' section / Classification (12)
- Caveat: Exact dataset splits and evaluation harness not specified on the inspected page.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: MTEB average (56 tasks) comparison between bge-small-en-v1.5 and other BGE variants
- Criteria: Per-checkpoint, per-task numeric comparison requires matching evaluation protocols and explicit per-checkpoint rows; the inspected model-page and config.json do not contain matching protocol detail for direct per-checkpoint protocol-matched comparisons.
- Rationale: While the model page lists per-group MTEB-style scores for bge-small-en-v1.5 and the page lists hidden sizes for other variants, the inspected locators do not provide the required protocol-level detail to perform a protocol-matched numeric comparison across checkpoints.
- Comparison conditions: Requires exact protocol (datasets, splits, metrics, evaluation harness) for each checkpoint; not specified on the inspected model page/config.json.
- Evidence: https://huggingface.co/BAAI/bge-small-en-v1.5, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json

## Limitations and safety

### Limitations

- Evidence gap: Explicit documentation of training data provenance, per-split evaluation protocol, and per-task evaluation harness for the exact v1.5 checkpoint is not provided in the inspected v1.5 README/commit/config locators. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c
- Evidence gap: The inspected v1.5 README/config locators do not provide an exhaustive list of known failure modes or per-domain performance degradation tables for this exact checkpoint; perform domain-specific validation prior to deployment. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json

### Safety

- Evidence gap: Canonical primary sources for this exact checkpoint (README, commit, config.json, vocab) do not publish checkpoint-specific privacy, PHI-handling, clinical-use, or biosecurity guidance; apply conservative data-handling and expert review for sensitive domains. Sources: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c, https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### BAAI/bge-small-en-v1.5 — model card / model page

- URL: https://huggingface.co/BAAI/bge-small-en-v1.5
- Publisher: HuggingFace (BAAI repository page)
- Type: `model-card`
- Primary because: Canonical Hugging Face model page for the exact v1.5 checkpoint; contains reported benchmarks and usage examples.
- Scope: BAAI/bge-small-en-v1.5
- Supports: reported MTEB-style benchmark aggregates and subgroup scores for bge-small-en-v1.5
- Supports: embedding+reranker example workflow and usage guidance

### BAAI/bge-small-en-v1.5 — README

- URL: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md
- Publisher: HuggingFace (BAAI repository page)
- Type: `model-card`
- Primary because: Repository README for the v1.5 checkpoint; contains example code and workflow descriptions.
- Scope: BAAI/bge-small-en-v1.5
- Supports: example embedding extraction and example code (normalize_embeddings usage)
- Supports: embedding+reranker workflow demonstration

### BAAI/bge-small-en-v1.5 — config.json (blob)

- URL: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json
- Publisher: HuggingFace (BAAI repository page)
- Type: `repository`
- Primary because: Exact config.json blob present in the repository for the v1.5 checkpoint; contains model architecture and hyperparameter keys.
- Scope: BAAI/bge-small-en-v1.5 (config blob)
- Supports: model_type and architecture
- Supports: num_hidden_layers, hidden_size, max_position_embeddings, torch_dtype, vocab_size and other config keys

### BAAI/bge-small-en-v1.5 — commit b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c

- URL: https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c
- Publisher: HuggingFace (BAAI repository page)
- Type: `repository`
- Primary because: Exact repository commit/revision referenced for the v1.5 checkpoint; used to anchor revision-level provenance.
- Scope: BAAI/bge-small-en-v1.5 (revision b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c)
- Supports: revision-level provenance and commit metadata as inspected

### BAAI/bge-small-en-v1.5 — vocab.txt

- URL: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/vocab.txt
- Publisher: HuggingFace (BAAI repository page)
- Type: `repository`
- Primary because: Vocabulary artifact present in the repository for the v1.5 checkpoint; supports tokenizer presence and token inventory inspection.
- Scope: BAAI/bge-small-en-v1.5
- Supports: token inventory and presence of vocabulary for the checkpoint tokenizer

### BAAI/bge-small-en-v1.5 — tokenizer.json (inspected path; content not reported in findings)

- URL: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/tokenizer.json
- Publisher: HuggingFace (BAAI repository page)
- Type: `repository`
- Primary because: Canonical tokenizer path for the v1.5 checkpoint; included here to indicate the inspected tokenizer location (tokenizer content not reported in the provided findings).
- Scope: BAAI/bge-small-en-v1.5
- Supports: tokenizer artifact path for inspection (content not supplied in the research findings)

## Evidence gaps

- Evidence gap: The research findings do not report an explicit license text or a model-weight vs code-license distinction at the inspected Hugging Face commit or model-page locators; I inspected: https://huggingface.co/BAAI/bge-small-en-v1.5 and https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c (no license text reported in provided findings).
- Evidence gap: Tokenizer JSON content (tokenization type and special tokens) at https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/tokenizer.json was not reported in the provided findings; inspect tokenizer.json to verify tokenization type and special-token keys.
- Evidence gap: The provided findings do not include explicit parameter-count metadata for the exact bge-small-en-v1.5 checkpoint in the inspected canonical HF locators; parameter count is not reported in the config.json/model page facts supplied.
- Evidence gap: The config.json and model page do not include evaluation-protocol details (dataset splits, harness, seed) necessary to fully reproduce the reported benchmark numbers; I inspected https://huggingface.co/BAAI/bge-small-en-v1.5 and https://huggingface.co/BAAI/bge-small-en-v1.5/blob/88885630388d6249d876a3ab145b78b34665b79a/config.json and found protocol details not reported in the provided findings.
- Evidence gap: The inspected canonical locators in the provided findings do not publish checkpoint-published quantized or ONNX artifacts at the canonical HF paths reported; verify downstream packaged artifacts separately before assuming identical accuracy/behavior. Inspected: https://huggingface.co/BAAI/bge-small-en-v1.5/blob/main/README.md and https://huggingface.co/BAAI/bge-small-en-v1.5/commit/b49342cba6a5914c1760cd4aae1d75a6f2e8fc4c.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 17 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].caveats: $.benchmarks[0].caveats: expected array, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].caveats: $.benchmarks[1].caveats: expected array, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].caveats: $.benchmarks[2].caveats: expected array, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'alibaba-nlp' for this exact model scope: $.sources[8] uses unapproved repository owner 'alibaba-nlp' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/RedHatAI/bge-small-en-v1.5-quant Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
