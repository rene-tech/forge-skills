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

- Research key: `huggingface-co-snowflake-snowflake-arctic-embed-m-v2-0-0afc1336c2`
- Independent audit: `revised`
- Researched: `2026-08-06T10:27:50.917571+00:00`

Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0 is documented on Hugging Face as an Apache-2.0 multilingual text-embedding checkpoint (model card and README). The upstream README and model card report a 768-dimensional embedding output and list benchmark summary numbers (BEIR 55.4; MIRACL 55.2; CLEF Focused 51.7; CLEF Full 53.9) in the checkpoint README. The model card/README usage examples show pooling using the CLS token and set normalize=true in example code, indicating L2-normalized embeddings for retrieval use. Tokenizer/config facts available in the upstream HF repository include a vocab_size of 30,522 (configuration file) and example tokenizer usage with padding=True, truncation=True, return_tensors='pt', and max_length=512 in a code snippet on the Hugging Face pages. Several low-level items required for strict reproducibility and immutable artifact provenance are not present in the examined upstream Hugging Face files: no immutable upstream revision mapping to the Forge-served slug was reported, no safetensors file-size or verified SHA-256 checksum artifact locator was found in the checked files, and special-token definitions and an explicit tokenizer class name beyond use of AutoTokenizer.from_pretrained were not documented. The README lists comparative numeric rows for several other models (me5 base, bge-m3, gte) but does not provide separate protocol appendices or reproducibility tables in the inspected README that establish matched head-to-head protocol descriptions; therefore head-to-head superiority claims require additional protocol documentation to be verifiable.

## Identity

- Upstream name: Snowflake/snowflake-arctic-embed-m-v2.0
- Checkpoint/version: Snowflake/snowflake-arctic-embed-m-v2.0
- Immutable revision: not reported
- Parameter scale: 305 million total parameters (as reported in the README.md at the upstream checkpoint)
- Architecture/head: Text embedding model; upstream checkpoint and README describe Arctic-Embed 2.0 family-level multilingual embedding design and recommend using the final hidden state of the CLS token as the embedding vector (family/checkpoint-level description derived from the Hugging Face model card and README).
- License: Apache 2.0 (model weights license reported in the Hugging Face model card/README). No separate code-license statement was found in the checked upstream Hugging Face files.
- Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md, https://huggingface.co/Snowflake/snowflake-arctic-embed-m, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blame/df87782f77b62df285ebf49a13cd16900cca23b3/configuration_hf_alibaba_nlp_gte.py

## Selection

### Recommended

- **Multilingual semantic search and retrieval over text queries and documents** — The Hugging Face model card and README position the checkpoint for retrieval and embedding workloads and include retrieval-oriented guidance (CLS pooling recommendation and normalized-embeddings usage in example code).
  Scope: Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- **Embedding text for nearest-neighbor ranking or semantic-similarity workflows using dot-product scoring between normalized embeddings** — The model card/README provide example code computing dot-product similarity between query and document embeddings and set normalize=true in usage examples, and the README reports 768-dimensional embeddings intended for dot-product similarity of normalized vectors.
  Scope: Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md

### Conditional

- **Integrations with sentence-transformers or Transformers.js for client libraries** — Validate end-to-end parity for your task: the model card and README indicate compatibility but do not provide exhaustive low-level tokenizer special-token definitions or an immutable artifact-to-serving mapping needed to guarantee exact numeric parity with a specific serving revision. Downstream validation on target corpora is recommended.
  Scope: Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0

### Avoid

- **Use for high-stakes clinical or life-critical decision making without separate domain validation and human oversight** — Evidence gap: The checked upstream Hugging Face model card and README do not provide clinical validation, healthcare deployment guidance, or life‑critical decision‑support evidence for this exact checkpoint.
  Scope: Snowflake/snowflake-arctic-embed-m-v2.0
  Evidence: documented evidence gap
- **Rely on this dossier for exact tokenizer internals, token limits, truncation/padding policies, or immutable upstream-to-Forge revision mapping when strict reproducibility is required** — Evidence gap: The checked upstream sources do not document special-token definitions, an immutable upstream artifact-to-serving mapping, or a safetensors checksum locator for this exact checkpoint.
  Scope: Snowflake/snowflake-arctic-embed-m-v2.0 (Upstream checkpoint evidence only)
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- The model consumes text inputs for embedding. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0
- Intended retrieval setting uses text queries and text documents/passages. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0

### Accepted formats

- Plain text strings are accepted by the upstream usage examples via the Transformers feature-extraction pipeline and tokenizer examples. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m

### Preprocessing

- Upstream usage examples and README recommend using the CLS token embedding (pooling='cls') for retrieval. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- Upstream example code sets normalize=true in feature-extraction/embedding examples, indicating L2 normalization of returned embeddings in example usage. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0
- Repository/example code demonstrates a query prefix when embedding queries; two different prefixes appear in inspected upstream files, creating an ambiguity between recommended query-prefix strings. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m

### Pre-submit validation

- The example tokenizer usage in the upstream repository shows padding=True, truncation=True, return_tensors='pt', and max_length=512 in a code snippet. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m
- The upstream configuration file lists vocab_size = 30,522. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blame/df87782f77b62df285ebf49a13cd16900cca23b3/configuration_hf_alibaba_nlp_gte.py
- Evidence gap: The checked upstream files do not document special-token definitions (e.g., CLS/SEP token id values) for this exact checkpoint; special-token mappings are not present in the inspected configuration or README.
- Evidence gap: The checked upstream files do not provide an explicit canonical tokenizer class name beyond use of AutoTokenizer.from_pretrained in an example; the exact tokenizer implementation class (e.g., specific tokenizer type) is not documented explicitly in the inspected files.
- Evidence gap: The inspected upstream files do not provide an immutable artifact-to-Forge-serving mapping (no safetensors checksum or explicit revision mapping to the Forge-served slug was found in the examined files).

### Task-specific formatting

- The model card/README indicate asymmetric formatting by adding a query prefix on queries in recommended examples; the model card README shows the prefix "query: " in one example. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- Ambiguity: a separate code snippet on the related Hugging Face page uses a different query prefix string ("Represent this sentence for searching relevant passages: "), creating a conflict between example prefixes in upstream files; both upstream locations are cited. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m
- Evidence gap: No other official prompt template, paired-input ordering rule, or control-field schema is documented in the inspected upstream README or code snippets beyond the query-prefix examples cited.

## Output interpretation

### Outputs

- The model outputs text embeddings via the Transformers feature-extraction pipeline in the upstream usage examples. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0
- The output embedding dimensionality is 768 as reported in the upstream README for snowflake-arctic-m-v2.0. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md

### Interpretation

- Embeddings are normalized to unit length (L2 norm) in the upstream example usage (normalize=true) and are intended for retrieval/semantic-matching workflows rather than as calibrated probabilities. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0

### Post-inference validation

- Evidence gap: The inspected upstream files do not provide explicit post-inference numerical thresholds, calibration procedures, or acceptance criteria for production retrieval decisions; downstream validation is recommended.

## Public benchmarks

### Retrieval / BEIR (MTEB family)

- Dataset/split: BEIR (15) / not reported
- Metric/value: score (aggregate retrieval metric as reported in README) / 55.4 (`higher-is-better`)
- Model scope: Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
- Conditions: Reported in upstream README as a checkpoint summary; no separate protocol appendix or per-dataset breakdown located in the inspected README beyond the listed summary row.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- Locator: README.md (repository blob path: /blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md) — line/row in the README that lists "Snowflake arctic-m-v2.0 achieved a BEIR (15) score of 55.4."
- Caveat: Reported as a numeric summary row in the upstream README; the README does not include a separate per-dataset table or detailed protocol appendix in the inspected blob to verify per-dataset conditions.

### Retrieval / MIRACL

- Dataset/split: MIRACL (4) / not reported
- Metric/value: score (as reported in README) / 55.2 (`higher-is-better`)
- Model scope: Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
- Conditions: Reported in upstream README as a checkpoint summary; no separate protocol appendix or per-dataset breakdown located in the inspected README beyond the listed summary row.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- Locator: README.md (repository blob path: /blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md) — line/row in the README that lists "Snowflake arctic-m-v2.0 achieved a MIRACL (4) score of 55.2."
- Caveat: Reported as a numeric summary row in the upstream README; the README does not include a separate per-dataset table or detailed protocol appendix in the inspected blob to verify per-dataset conditions.

### Retrieval / CLEF

- Dataset/split: CLEF (Focused / Full) / not reported
- Metric/value: score (as reported in README) / 51.7 (Focused) ; 53.9 (Full) (`higher-is-better`)
- Model scope: Upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
- Conditions: Reported in upstream README as checkpoint summary rows for CLEF Focused and CLEF Full; no separate protocol appendix or per-dataset breakdown located in the inspected README beyond the listed summary rows.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- Locator: README.md (repository blob path: /blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md) — lines/rows in the README that list "Snowflake arctic-m-v2.0 achieved a CLEF (Focused) score of 51.7" and "CLEF (Full) score of 53.9."
- Caveat: Reported as numeric summary rows in the upstream README; the README does not include a separate per-dataset table or detailed protocol appendix in the inspected blob to verify per-dataset conditions.

## Comparisons

### leading open-source and proprietary models — `insufficient-evidence`

- Task: Multilingual retrieval (MTEB Retrieval / BEIR, CLEF, MIRACL families)
- Criteria: The README lists numeric rows for other named models and includes a high-level claim of outperforming leading open-source and proprietary models, but the inspected upstream README does not include a matched protocol appendix or reproducibility table that fully documents identical evaluation conditions and per-dataset protocols required for strict head-to-head verification.
- Rationale: Upstream README provides numeric summary rows for baselines (me5 base, bge-m3, gte, etc.) enabling a summary comparison, but lacks detailed protocol descriptions or separate evaluation tables to confirm exact matched-evaluation conditions; therefore a strict verified superiority judgment is unsupported by exact protocol matches in the inspected files.
- Comparison conditions: Not reported in README beyond numeric summary rows; no per-dataset protocol appendix located in the inspected README blob.
- Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0

## Limitations and safety

### Limitations

- Evidence gap: The checked upstream sources do not report special-token definitions, exact tokenizer implementation class beyond AutoTokenizer.from_pretrained usage in examples, or special-token id mappings for this exact checkpoint.
- Evidence gap: The checked upstream README and model card do not include a detailed protocol appendix or per-dataset evaluation tables that fully document evaluation conditions required for strict reproducibility of the reported benchmark numbers.
- Evidence gap: Exact immutable upstream artifact identifiers (e.g., safetensors file-size and SHA‑256 checksum) and an explicit mapping from upstream artifact to the Forge-served slug are not present in the inspected upstream files.
- Evidence gap: The checked upstream files do not provide explicit post-inference calibration procedures or production acceptance thresholds for retrieval decisions.

### Safety

- Forge policy: Do not use this embedding checkpoint as the sole basis for clinical, life-critical, or other high-stakes decisions without domain-specific validation and qualified human review.
- Evidence gap: The checked upstream sources do not report training-data provenance, proprietary-data usage, or detailed privacy/data-governance statements for this exact checkpoint.
- Use the checkpoint in ways consistent with its Apache 2.0 model-weights license as reported in the Hugging Face model card/README; no separate code-license statement was located in the inspected upstream files. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Snowflake/snowflake-arctic-embed-m-v2.0 — Hugging Face model card

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0
- Publisher: Hugging Face / Snowflake
- Type: `model-card`
- Primary because: Official Hugging Face model card page for the exact upstream checkpoint; contains checkpoint-level usage examples, pooling/normalization examples, and summary statements referenced throughout the dossier.
- Scope: Exact upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
- Supports: identity.upstreamName
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.outputs
- Supports: outputInterpretation.interpretation
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: researchSummary
- Supports: safety

### snowflake-arctic-embed-m-v2.0 README.md (repository blob)

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blob/0fcceba4650046e504a026be7fef01dc8666afb4/README.md
- Publisher: Hugging Face / Snowflake
- Type: `model-card`
- Primary because: Repository README blob for the exact upstream checkpoint; contains explicit numeric benchmark summary rows, parameter counts, embedding dimensionality, and usage/formatting guidance cited for benchmarks and identity claims.
- Scope: Exact upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0
- Supports: identity.parameterScale
- Supports: outputInterpretation.outputs
- Supports: benchmarks
- Supports: comparisons
- Supports: recommendedUseCases
- Supports: researchSummary

### Snowflake/snowflake-arctic-embed-m — Hugging Face repository page (usage snippets & tokenizer example)

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-m
- Publisher: Hugging Face / Snowflake
- Type: `model-card`
- Primary because: Upstream Hugging Face repository page containing example code snippets referenced by the model card/README (AutoTokenizer usage, tokenizer call parameters like padding/truncation/max_length).
- Scope: Related upstream repository pages for Snowflake arctic-embed models (examples referencing tokenizer usage and example prefixes)
- Supports: inputPreparation.preprocessings
- Supports: inputPreparation.validation
- Supports: inputPreparation.taskSpecificFormatting

### Configuration file excerpt in upstream repository (configuration_hf_alibaba_nlp_gte.py) — blame view

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0/blame/df87782f77b62df285ebf49a13cd16900cca23b3/configuration_hf_alibaba_nlp_gte.py
- Publisher: Hugging Face / Snowflake
- Type: `repository`
- Primary because: Upstream configuration file showing default model configuration parameters (vocab_size and other configuration defaults) accessible in the repository blob.
- Scope: Exact upstream checkpoint Snowflake/snowflake-arctic-embed-m-v2.0 (configuration file view)
- Supports: inputPreparation.validation
- Supports: identity.parameterScale
- Supports: researchSummary

## Evidence gaps

- Evidence gap: No immutable upstream artifact identifier (safetensors file-size and SHA-256 checksum) or explicit artifact-to-Forge-serving slug mapping was found in the inspected upstream Hugging Face pages and repository blobs.
- Evidence gap: Special-token definitions (token ids for CLS/SEP/etc.) for this exact checkpoint are not documented in the inspected upstream files.
- Evidence gap: The exact tokenizer implementation class beyond example use of AutoTokenizer.from_pretrained is not explicitly documented in the inspected upstream files.
- Evidence gap: No separate protocol appendix or per-dataset evaluation tables were located in the inspected README blob to fully document evaluation conditions for the reported benchmark summary numbers.
- Evidence gap: Training-data provenance, proprietary-data usage, and detailed privacy/data-governance statements for this exact checkpoint are not present in the inspected upstream README/model card/configuration files.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 14 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4] uses unapproved repository owner 'snowflake-labs' for this exact model scope: $.sources[4] uses unapproved repository owner 'snowflake-labs' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'teradata' for this exact model scope: $.sources[6] uses unapproved repository owner 'teradata' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'linerai' for this exact model scope: $.sources[7] uses unapproved repository owner 'linerai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nampham1106/snowflake-arctic-embed-m-v2.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Snowflake-Labs/arctic-embed/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Snowflake-Labs/arctic-embed/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Snowflake-Labs/arctic-embed/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nampham1106/snowflake-arctic-embed-m-v2.0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-m/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].value must contain a reported numeric result: $.benchmarks[3].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
