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

- Research key: `huggingface-co-nomic-ai-nomic-embed-text-v2-moe-6010f512ca`
- Independent audit: `revised`
- Researched: `2026-08-06T13:17:22.138263+00:00`

I verified the upstream Hugging Face checkpoint nomic-ai/nomic-embed-text-v2-moe and the canonical preprint in the provided primary sources. The checkpoint is presented as a Mixture-of-Experts (MoE) transformer‑based text embedding model; the checkpoint config and README commit-level view report MoE parameters (num_experts=8 and moe_top_k=2) and n_embd=768. Primary upstream artifacts report embedding dimension 768 and Matryoshka flexible-dimension outputs down to 256, and report BEIR=52.86 and MIRACL=65.80 on the model page / README. I found a conflict in reported parameter counts: the model page reports 305M while a commit/blame view of the README reports total=475M and active=305M; no immutable artifact in the provided sources resolves that discrepancy. I was unable to find an authoritative immutable locator tying the Forge TEI variant label tei-cuda-1-9-3 to a specific upstream artifact in the verified primary sources (evidence gap). Multiple operational/runtime details (exact tokenizer identity/vocabulary, canonical pooling/normalization and recommended similarity metric, detailed BEIR/MIRACL evaluation protocol and splits, and a canonical runtime JSON/API contract) are not specified in the supplied primary sources; I record exact evidence gaps below and cite the primary URLs I inspected.

## Identity

- Upstream name: nomic-embed-text-v2-moe
- Checkpoint/version: nomic-ai/nomic-embed-text-v2-moe
- Immutable revision: not reported
- Parameter scale: Conflicting primary reports: Hugging Face model page reports 305M parameters; a model README commit/blame view reports total=475M with 305M active at inference (both are recorded below).
- Architecture/head: Mixture-of-Experts (MoE); primary sources report MoE with num_experts=8 and moe_top_k=2 as specified in the checkpoint config/README.
- License: Apache-2.0 (model card / README on the Hugging Face model page)
- Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/commit/10c3f19872f1e5b090ea7ca44b33592bf34f08b3, https://github.com/huggingface/text-embeddings-inference/releases, https://github.com/huggingface/text-embeddings-inference/issues/502

## Selection

### Recommended

- **Multilingual retrieval** — The upstream model card and README describe the checkpoint as a multilingual embedding model and report multilingual retrieval benchmarks (BEIR and MIRACL) for this checkpoint.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- **Embedding generation for RAG indexing (feature extraction for retrieval-augmented-generation pipelines)** — The model card and README indicate the checkpoint is intended for sentence-similarity/feature-extraction and embedding-generation tasks suitable for RAG-style indexing.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- **Semantic search and clustering using dense embeddings** — The upstream model page and README report dense embedding outputs (default dim=768) and list sentence-similarity / feature-extraction usage suitable for semantic search and clustering.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md

### Conditional

- **Storage- or compute-constrained embedding deployment using Matryoshka (reduced-dimension) representations** — Primary sources document Matryoshka embeddings and flexible embedding dimensions (768 down to 256) but do not provide a measured, primary-source numeric claim of a specific storage reduction or per-dimension task calibration; evaluate downstream task performance at each reduced dimension before production deployment.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe` (Matryoshka reduced-dimension outputs)
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md
- **Multilingual deployment validation** — Primary sources report wide multilingual support and aggregate multilingual benchmarks but do not provide per-language quality guarantees in the supplied evidence; validate target-language performance in downstream contexts.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf
- **General text embedding beyond retrieval** — Primary sources provide prompt/formatting guidance primarily for retrieval-style inputs; broader task-formatting patterns and per-task calibration are not specified and should be validated downstream.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe

### Avoid

- **Using unprefixed retrieval inputs for search tasks (omitting documented task/document/query prefixes)** — The checkpoint README documents retrieval-style formatting that includes a task-instruction prefix and explicit query/document prefixes; omitting those documented prefixes is not aligned with the documented usage.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
- **Inputs longer than the supported maximum without truncation awareness** — A commit/blame view of the README and the checkpoint config indicate maximum sequence settings (max_trained_positions or README-specified) that require validation; exceeding the documented maximum can invalidate tokenization/embedding behavior.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json
- **Assuming uniform per-language performance without per-language validation** — Primary sources report aggregate multilingual benchmarks but do not provide per-language guarantees in the supplied evidence; do not assume uniform quality across all languages without downstream validation.
  Scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe`
  Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf

## Input preparation

### Semantic inputs

- The checkpoint consumes text inputs (sentences/strings) as its semantic input. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- For retrieval-style use, inputs are treated as distinct queries and documents with documented prefixes and a task-instruction prefix. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md

### Accepted formats

- Primary usage notes indicate the model is intended for sentence-similarity/feature-extraction tasks and is usable via the Hugging Face model card instructions. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- Inputs are plain text strings; no non-text modalities are documented in the supplied primary sources. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md

### Preprocessing

- The model uses the checkpoint's tokenizer and follows tokenization conventions implied by the Hugging Face model files and README; users should follow the Hugging Face / model README guidance for tokenization when preparing text. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json
- The checkpoint supports Matryoshka flexible embedding dimensions (768 down to 256) as described in the README/commit-level README evidence; choosing reduced dimensions affects output representation. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- Evidence gap: The precise tokenizer identity (tokenizer class name), tokenizer vocabulary files, and any required trust_remote_code setting are not fully documented in the supplied primary-source artifacts; I checked the model page, README, commit-level README, and config.json but did not find an explicit tokenizer class/vocab file listing. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json

### Pre-submit validation

- Validate that text inputs do not exceed the documented maximum sequence length (max_trained_positions or README-specified maximum) reported in the checkpoint config/README. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md
- Validate that retrieval inputs follow the documented prompt formatting: include an explicit task-instruction prefix and prefix queries/documents with the documented strings when following the README guidance. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- Evidence gap: No primary-source guidance was found in the supplied artifacts for input normalization steps (e.g., lowercasing, punctuation stripping), allowed character encodings, or exact handling of extremely long documents beyond noting a maximum token length; I checked the model page, README, commit-level README, and config.json. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json

### Task-specific formatting

- The README documents retrieval-format guidance: prompts should include a task-instruction prefix; queries and documents are indicated with documented prefixes. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- Evidence gap: The supplied primary sources do not include additional official prompt templates, paired-input order conventions for batch embedding, or a canonical runtime API request/response JSON example; I inspected the model page, README (main and commit-level), and config.json and did not find such runtime contract examples. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json

## Output interpretation

### Outputs

- The upstream checkpoint emits dense embedding vectors; the default embedding dimension is reported as 768 and Matryoshka mechanisms support reduced embedding dimensions down to 256. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json

### Interpretation

- Evidence gap: The supplied primary sources do not specify canonical similarity metrics, pooling, or normalization steps (e.g., L2 normalization vs raw dot product) to interpret embedding scores; do not assume a default metric without downstream verification. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf

### Post-inference validation

- Evidence gap: No primary-source post-inference validation checks (sanity checks, calibration steps, or recommended thresholding for similarity scores) were found in the supplied artifacts; I inspected the model page, README, commit-level README, and preprint. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf

## Public benchmarks

### retrieval (BEIR)

- Dataset/split: BEIR / not reported
- Metric/value: aggregate BEIR score (as reported on model page) / 52.86 (`higher-is-better`)
- Model scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe` (model card / README reported value)
- Conditions: Detailed evaluation protocol (dataset splits, retrieval configuration, pooling/normalization, evaluation script) not specified in the supplied primary sources.
- Source: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
- Locator: model card / README benchmarks section
- Caveat: Primary findings list the numeric result but do not include the detailed evaluation protocol or per-split rows in the supplied artifacts; see benchmark-specific evidence gap.

### retrieval (MIRACL)

- Dataset/split: MIRACL / not reported
- Metric/value: MIRACL score (as reported on model page) / 65.80 (`higher-is-better`)
- Model scope: Upstream checkpoint `nomic-ai/nomic-embed-text-v2-moe` (model card / README reported value)
- Conditions: Detailed evaluation protocol (dataset split, retrieval setup, evaluation script) not specified in the supplied primary sources.
- Source: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
- Locator: model card / README benchmarks section
- Caveat: Primary findings list the numeric result but do not include detailed evaluation protocol text in the supplied artifacts; see benchmark-specific evidence gap.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: general multilingual retrieval benchmarking
- Criteria: No primary-source side-by-side table or figure with matched protocol details comparing this checkpoint to a named alternative was found in the supplied artifacts; protocol parity cannot be established from the available sources.
- Rationale: The provided primary findings include aggregate numeric results for this checkpoint (BEIR, MIRACL) but do not include direct, primary-source controlled comparison tables against specific alternative checkpoints with matched protocols.
- Comparison conditions: Checked the model page, README (main and commit-level), and the canonical preprint; no side-by-side primary comparison with matched protocol details was available in those artifacts.
- Evidence: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf

## Limitations and safety

### Limitations

- Primary-source reporting is inconsistent on total parameter count: the Hugging Face model page reports 305M parameters while a commit-level README/blame view reports total=475M with 305M active during inference; this ambiguity limits precise resource planning and must be resolved by inspecting the authoritative checkpoint artifact. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md
- The supplied primary findings do not include detailed benchmark evaluation protocols (per-dataset split, retrieval configuration, pooling/normalization), limiting reproducibility of the reported BEIR and MIRACL numbers. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf
- Evidence gap: The canonical mapping from the Forge TEI variant label tei-cuda-1-9-3 to a specific immutable upstream commit or artifact for this checkpoint was not found in the supplied primary sources; I inspected the text-embeddings-inference releases and issue artifacts and the Hugging Face model page but did not find a binding locator. Sources: https://github.com/huggingface/text-embeddings-inference/releases, https://github.com/huggingface/text-embeddings-inference/issues/502, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe

### Safety

- Evidence gap: The supplied primary sources do not include explicit safety, privacy, PII-handling, clinical, or biosecurity guidance for this checkpoint; no primary-source usage restrictions or mandatory human-review guidance were located in the model card, README, commit-level README, or canonical preprint. Sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### nomic-ai/nomic-embed-text-v2-moe (model page)

- URL: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Official Hugging Face model card and files for the exact upstream checkpoint; includes reported embedding dimension, benchmark numbers, parameter-count statement, and README files.
- Scope: nomic-ai-nomic-embed-text-v2-moe
- Supports: Reported embedding dimension = 768
- Supports: Reported BEIR = 52.86 and MIRACL = 65.80
- Supports: Model license = Apache-2.0
- Supports: General model identity and intended retrieval/embedding use cases

### Nomic Embed v2 preprint (canonical preprint PDF)

- URL: https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf
- Publisher: nomic.ai (static hosting)
- Type: `paper`
- Primary because: Canonical preprint describing Nomic Embed v2 architecture and multilingual evaluation claims included in the provided findings.
- Scope: Nomic Embed v2 family / paper
- Supports: MoE characterization of Nomic Embed v2
- Supports: Claims about multilingual retrieval performance
- Supports: Discussion of research limitations and future work

### Model README (main branch)

- URL: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Primary README hosted on the Hugging Face model page describing usage, Matryoshka embeddings, and benchmarking statements.
- Scope: nomic-ai-nomic-embed-text-v2-moe (README main)
- Supports: Prompt-formatting guidance for retrieval (task/document/query prefixes)
- Supports: Matryoshka flexible-dimension embedding claims
- Supports: Reported benchmark aggregate numbers referenced on the model page

### Model README (commit-level view / specific README blob)

- URL: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Commit-scoped README blob used to extract commit-level facts (parameter counts, reported benchmarks) provided in the findings.
- Scope: nomic-ai-nomic-embed-text-v2-moe (README at commit ac3a5fe)
- Supports: Reported BEIR = 52.86 and MIRACL = 65.80 in the README blob
- Supports: Reported parameter count = 305M in this README blob

### Model config (config.json) hosted in the model files

- URL: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Checkpoint configuration file in the model repository files containing exact architecture and MoE configuration parameters used by the checkpoint.
- Scope: nomic-ai-nomic-embed-text-v2-moe (config.json)
- Supports: moe_top_k = 2
- Supports: num_experts = 8
- Supports: n_embd = 768
- Supports: moe_every_n_layers = 2
- Supports: max_trained_positions = 2048 (config field)

### Model commit (commit view used in findings)

- URL: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/commit/10c3f19872f1e5b090ea7ca44b33592bf34f08b3
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Commit-level view included in the provided findings that documents loader/runtime notes and a trust_remote_code mention.
- Scope: nomic-ai-nomic-embed-text-v2-moe (commit 10c3f198)
- Supports: Loader guidance mentioning trust_remote_code requirement in commit notes (as reported in findings)
- Supports: Commit-level limitations and usage notes

### Hugging Face text-embeddings-inference (TEI) releases

- URL: https://github.com/huggingface/text-embeddings-inference/releases
- Publisher: github.com/huggingface
- Type: `repository`
- Primary because: Repository releases page referenced in the provided findings for TEI release metadata relevant to Forge runtime mapping checks.
- Scope: text-embeddings-inference repository (releases)
- Supports: TEI release v1.9.3 metadata (release listing as reported in the findings)

### Hugging Face text-embeddings-inference issue referenced in findings

- URL: https://github.com/huggingface/text-embeddings-inference/issues/502
- Publisher: github.com/huggingface
- Type: `repository`
- Primary because: Repository issue referenced in the provided findings documenting a TEI load attempt and associated logs used to evaluate Forge/TEI mapping evidence.
- Scope: text-embeddings-inference repository (issue #502)
- Supports: Reported TEI load attempt and logs when attempting to load nomic-ai/nomic-embed-text-v2-moe into a TEI container (as recorded in the findings)

## Evidence gaps

- Evidence gap: I did not find an authoritative immutable upstream locator (commit SHA, artifact hash, or explicit model-card revision note) that binds the Forge TEI variant label tei-cuda-1-9-3 to a specific upstream artifact for nomic-ai/nomic-embed-text-v2-moe. URLs I inspected: https://github.com/huggingface/text-embeddings-inference/releases, https://github.com/huggingface/text-embeddings-inference/issues/502, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe.
- Evidence gap: The precise tokenizer identity (tokenizer class name), tokenizer vocabulary files, and an explicit tokenizer repo/file listing were not present in the supplied primary sources. I inspected: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/config.json, and the commit-level README blob.
- Evidence gap: Detailed benchmark evaluation protocols (per-dataset splits, exact retrieval configuration, pooling/normalization, evaluation scripts) underpinning the reported BEIR=52.86 and MIRACL=65.80 numbers were not present in the supplied primary artifacts; I inspected: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md, and https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf.
- Evidence gap: The supplied primary sources do not document pooling, normalization, or the canonical similarity metric (cosine vs dot-product) to interpret embedding scores; I inspected: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, and https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf.
- Evidence gap: No canonical runtime contract (request/response JSON shapes or official API example) for serving this upstream checkpoint via a NIM/server wrapper was found in the supplied primary sources; I inspected the model page, README (main and commit-level), and the TEI repository releases/issues: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe, https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/main/README.md, https://github.com/huggingface/text-embeddings-inference/releases, https://github.com/huggingface/text-embeddings-inference/issues/502.
- Evidence gap: The supplied primary findings do not include prescriptive safety/privacy/PII-handling or clinical-use prohibitions for this checkpoint; I inspected: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe and https://static.nomic.ai/nomic_embed_multilingual_preprint.pdf.
- Evidence gap: The precise authoritative artifact reconciling parameter-count reports (305M vs 475M total / 305M active) was not found in the supplied primary sources; I inspected: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe and https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/blob/ac3a5fe40e73300ece22e3a5d25f40d597e9dc33/README.md.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2] uses forbidden secondary host ollama.com: $.sources[2] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary host hub.docker.com: $.sources[4] uses forbidden secondary host hub.docker.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe-GGUF/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'anush008' for this exact model scope: $.sources[8] uses unapproved repository owner 'anush008' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'ajmcclary' for this exact model scope: $.sources[9] uses unapproved repository owner 'ajmcclary' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
