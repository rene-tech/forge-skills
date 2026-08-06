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

- Research key: `huggingface-co-snowflake-snowflake-arctic-embed-l-v2-0-d8e9bdd569`
- Independent audit: `revised`
- Researched: `2026-08-06T10:03:12.379690+00:00`

This dossier covers the exact Hugging Face checkpoint snowflake-arctic-embed-l-v2.0. Primary owner materials inspected (Hugging Face model card and the checkpoint's config.json and README) present the checkpoint as a multilingual text embedding model that produces 1024-dimensional dense vectors and is released under Apache-2.0. Owner-reported aggregate retrieval metrics appear on the model card/README (BEIR, MIRACL, CLEF, MTEB aggregate numbers) but per-dataset splits, exact pooling/normalization rules, and full evaluation scripts are not present in the inspected primary artifacts. The checkpoint's config.json documents an XLM‑RoBERTa architecture with hidden_size=1024, 24 layers, 16 attention heads, and max_position_embeddings=8194; Snowflake provider documentation (Cortex Search and Cortex embed/AI_EMBED docs) documents service bindings and model variants (including an -8k variant) and includes recommendations for chunking/truncation. Where primary-source facts conflict (for example, differing published parameter counts and differing statements about the canonical max context), this dossier records the conflict and lists evidence gaps rather than resolving them without primary-source basis.

## Identity

- Upstream name: snowflake-arctic-embed-l-v2.0
- Checkpoint/version: snowflake-arctic-embed-l-v2.0
- Immutable revision: not reported
- Parameter scale: 568 million total parameters (303 million non-embedding) reported on the Hugging Face model card; a README blob in the same repository lists 335 million — these sources conflict and no immutable upstream revision/hash tying metrics to a single revision was found in the inspected primary artifacts.
- Architecture/head: XLMRobertaModel (config.json for this checkpoint reports model_type "xlm-roberta", hidden_size=1024, intermediate_size=4096, num_hidden_layers=24, num_attention_heads=16, max_position_embeddings=8194, tokenizer bos/eos/pad token ids present).
- License: Apache-2.0
- Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json

## Selection

### Recommended

- **Multilingual semantic search and retrieval** — Hugging Face model card and Snowflake Cortex Search documentation present this checkpoint as a multilingual text embedding model with 1024 output dimensions and report retrieval-oriented evaluation aggregates.
  Scope: snowflake-arctic-embed-l-v2.0
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview
- **Enterprise retrieval / RAG pipelines, clustering and indexing of text** — Owner model card and Snowflake AI_EMBED/Cortex embed runtime docs describe the model and how Snowflake exposes embeddings for SQL and REST consumption; the 1024-dim embedding shape is suitable for vector-store indexing and similarity search.
  Scope: snowflake-arctic-embed-l-v2.0 (upstream checkpoint served via Snowflake Cortex/AI_EMBED runtime)
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/sql-reference/functions/ai_embed, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api

### Conditional

- **Using this checkpoint for image embeddings** — Snowflake AI_EMBED documentation shows image embedding support via a different named image multimodal model (voyage-multimodal-3); owner primary sources do not document snowflake-arctic-embed-l-v2.0 accepting image inputs. Confirm runtime/model mapping before assuming image support.
  Scope: snowflake-arctic-embed-l-v2.0
  Evidence: https://docs.snowflake.com/en/sql-reference/functions/ai_embed
- **Using extended-context variants (e.g., 8k) of this checkpoint without runtime confirmation** — Snowflake provider documentation references a -8k variant and the checkpoint's config.json shows a large max_position_embeddings value, but the Hugging Face primary artifacts and Snowflake docs present differing signals about canonical context support for this specific checkpoint. Verify the exact variant served (e.g., snowflake-arctic-embed-l-v2.0 vs snowflake-arctic-embed-l-v2.0-8k) with the provider/runtime before assuming 8k context.
  Scope: variant-specific (snowflake-arctic-embed-l-v2.0 versus snowflake-arctic-embed-l-v2.0-8k)
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview

### Avoid

- **Using this checkpoint as a generative language model (text completion / LM logits source)** — Upstream owner-provided materials document this checkpoint as a text embedding model that emits dense vectors (1024-dim). There is no primary-source evidence in the inspected owner materials that the checkpoint exposes LM logits or a decoding/generation head appropriate for text generation.
  Scope: snowflake-arctic-embed-l-v2.0
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- **Assuming clinical or regulated suitability without formal validation** — Primary owner materials inspected do not label this checkpoint as clinically validated or certified; such deployments require domain expert review and formal validation beyond the documented owner materials.
  Scope: snowflake-arctic-embed-l-v2.0
  Evidence: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/sql-reference/functions/ai_embed

## Input preparation

### Semantic inputs

- Primary semantic input type documented by upstream owner is text strings intended for embedding. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/sql-reference/functions/ai_embed
- Evidence gap: owner primary sources inspected do not document audio input semantics for this checkpoint; no upstream primary-source tokenizer/preprocessor spec for non-text modalities was found in the inspected artifacts.

### Accepted formats

- Provider/runtime contract: Snowflake Cortex embed REST API accepts JSON requests containing a text array and a model identifier (POST /api/v2/cortex/inference:embed); this documents the provider runtime binding and call signature. Sources: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/cortex-embed/cortex-embed-introduction, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api
- Provider/runtime contract: Snowflake AI_EMBED SQL function accepts a model identifier and text input and returns a VECTOR type; this documents how Snowflake exposes the checkpoint in SQL. Sources: https://docs.snowflake.com/en/sql-reference/functions/ai_embed

### Preprocessing

- The upstream config.json identifies XLM‑RoBERTa model type and reports tokenizer token id slots (bos/eos/pad) and structural model hyperparameters (hidden_size, layers, heads); explicit canonical tokenizer artifact files (tokenizer.json, vocab files) were not found among the inspected owner primary artifacts. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json, https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- Evidence gap: canonical tokenizer implementation files (tokenizer.json, vocab files, tokenizer-specific normalization or pre-tokenization rules) for this exact checkpoint were not present in the inspected primary sources.

### Pre-submit validation

- Inputs should be validated to respect the model's maximum context length; primary artifacts present conflicting signals about maximum context (see limitations) so validate against the chosen serving/runtime and the upstream config before use. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview
- Provider/runtime validation: Cortex embed API documents request body constraints (text array up to 1280 strings, each up to 4096 characters) and required headers; these are provider runtime constraints that do not redefine upstream tokenization. Sources: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api

### Task-specific formatting

- Provider/runtime example: Snowflake Cortex embed endpoint is invoked via POST /api/v2/cortex/inference:embed with a JSON body that includes the text array and model name; this documents the runtime call signature but does not change the upstream checkpoint's model-card contract. Sources: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/cortex-embed/cortex-embed-introduction, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api
- Provider/runtime formatting: Snowflake AI_EMBED documents SQL usage as AI_EMBED(model_name, input) returning VECTOR; this is a Snowflake SQL wrapper around a supported model. Sources: https://docs.snowflake.com/en/sql-reference/functions/ai_embed

## Output interpretation

### Outputs

- The upstream checkpoint produces a dense embedding vector of dimensionality 1024 as reported by the Hugging Face model card and README metrics table; the owner materials present the vector as the model output for retrieval tasks. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blob/6022d0ed2f4198f019f6f8e762c4cd363c18f19d/README.md
- Provider/runtime representation: Snowflake AI_EMBED exposes the result as a VECTOR type in Snowflake SQL and the Cortex embed API returns the embedding in the response body; these are runtime consumption formats for the upstream embedding vector. Sources: https://docs.snowflake.com/en/sql-reference/functions/ai_embed, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api

### Interpretation

- Vectors are dense embeddings intended for similarity computations (e.g., cosine, inner product); primary owner sources describe retrieval usage but do not publish a mandatory normalization convention for the upstream checkpoint — normalization behavior may depend on the serving runtime. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/sql-reference/functions/ai_embed

### Post-inference validation

- Post-inference checks should verify embedding dimensionality (1024) and confirm whether the serving runtime performed normalization; when in doubt, re-normalize before cosine similarity computations. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api
- Evidence gap: the inspected primary artifacts do not specify the tensors' dtype (e.g., float32) for the published embeddings for this exact checkpoint; verify dtype at runtime.

## Public benchmarks

### Retrieval

- Dataset/split: BEIR (15-dataset aggregate) / not reported
- Metric/value: NDCG@10 / 55.6 (`higher-is-better`)
- Model scope: snowflake-arctic-embed-l-v2.0
- Conditions: Primary source reports an aggregate BEIR NDCG@10 score on the model card without publishing per-dataset splits or full evaluation protocol in the inspected primary artifacts.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- Locator: model card metrics summary / top-level metrics section
- Caveat: Primary-source report is an aggregate; per-dataset splits and exact evaluation protocol (pooling, tokenization, metrics variants) are not provided in the cited source.

### Retrieval

- Dataset/split: MIRACL (4-dataset aggregate) / not reported
- Metric/value: NDCG@10 / 55.8 (`higher-is-better`)
- Model scope: snowflake-arctic-embed-l-v2.0
- Conditions: Primary source reports an aggregate MIRACL NDCG@10 score on the model card without publishing per-dataset splits or full protocol details.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- Locator: model card metrics summary / top-level metrics section
- Caveat: Aggregate number provided by owner; per-dataset breakdown and exact evaluation details are not present in the cited primary source.

### Retrieval

- Dataset/split: CLEF (focused and full aggregates reported separately) / not reported
- Metric/value: NDCG@10 / 52.9 / 54.3 (focused / full aggregates) (`higher-is-better`)
- Model scope: snowflake-arctic-embed-l-v2.0
- Conditions: Primary source reports CLEF aggregate scores without per-dataset tables or the exact evaluation protocol.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- Locator: model card metrics summary / top-level metrics section
- Caveat: CLEF values are reported as aggregates; reproducing or comparing requires per-dataset metric tables and exact protocol which are not present in the cited primary source.

### Retrieval (MTEB aggregate reported)

- Dataset/split: MTEB (aggregate / retrieval) / not reported
- Metric/value: NDCG@10 / 55.98 (`higher-is-better`)
- Model scope: snowflake-arctic-embed-l-v2.0 (README metrics table)
- Conditions: MTEB Retrieval Score reported in README blob; per-dataset breakdown and evaluation protocol are not present in the inspected README artifact.
- Source: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blob/6022d0ed2f4198f019f6f8e762c4cd363c18f19d/README.md
- Locator: README metrics table
- Caveat: Aggregate number provided by owner; per-dataset breakdown and exact evaluation protocol are not present in the cited primary source.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Maximum context length inconsistency: the checkpoint's config.json reports max_position_embeddings = 8194 while Snowflake Cortex Search documentation documents the base snowflake-arctic-embed-l-v2.0 having a 512-token context window and a separate -8k variant for an 8192-token context window; these primary sources conflict about which context window applies to this exact checkpoint. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview
- Benchmark reporting is aggregate in the inspected owner materials: Hugging Face model card and README report aggregate BEIR/MIRACL/CLEF/MTEB numbers but do not include per-dataset splits, exact pooling/prompting/pooling-aggregation protocol, or evaluation scripts in those primary artifacts. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blob/6022d0ed2f4198f019f6f8e762c4cd363c18f19d/README.md
- Tokenization artifacts and tokenizer implementation: the model config.json documents model_type and token id slots but canonical tokenizer files and explicit tokenization rules for this exact checkpoint were not present in the inspected primary sources, creating an evidence gap for exact tokenization behavior. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json, https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- Training-data provenance and counts: owner README and (owner) engineering materials discuss training regimen and Matryoshka Representation Learning but full dataset manifests, licensing provenance per-split, and exact training data counts sufficient for compliance auditing were not published in the inspected primary artifacts. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blob/6022d0ed2f4198f019f6f8e762c4cd363c18f19d/README.md

### Safety

- The owner-provided materials inspected do not label the checkpoint as clinically validated or certified; treat clinical/regulated deployments as requiring domain expert validation and formal compliance beyond what is stated upstream. Sources: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0, https://docs.snowflake.com/en/sql-reference/functions/ai_embed
- Forge policy: Perform a data-provenance and privacy review before embedding or indexing sensitive personal data (including PHI); upstream primary sources do not provide clinical/PHI handling guidance for this checkpoint and the researcher/operator must apply organizational data-protection policies.
- When using provider runtimes (Snowflake Cortex/AI_EMBED) that expose normalization/truncation parameters, explicitly record and verify runtime parameters (e.g., normalization, truncation direction) used in evaluation and production because metric behavior depends on these runtime options. Sources: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api, https://docs.snowflake.com/en/sql-reference/functions/ai_embed

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Snowflake / snowflake-arctic-embed-l-v2.0 — Hugging Face

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
- Publisher: Snowflake (Hugging Face model card)
- Type: `model-card`
- Primary because: Official Hugging Face model card published by Snowflake for this checkpoint; contains owner-provided model description, aggregate metrics, and parameter-count claims.
- Scope: snowflake-arctic-embed-l-v2.0 (Hugging Face model card)
- Supports: The model name is snowflake-arctic-embed-l-v2.0.
- Supports: Embedding dimensionality 1024 is reported.
- Supports: Aggregate BEIR/MIRACL/CLEF NDCG@10 scores are reported.
- Supports: Parameter counts (568M total, 303M non-embedding) are reported on the model card.
- Supports: Model is released under Apache-2.0.

### Hugging Face model config.json (blame URL) for snowflake-arctic-embed-l-v2.0

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blame/9fd85e702ce5326f8b5340aabd05792e4e72af83/config.json
- Publisher: Hugging Face model repository (config.json)
- Type: `repository`
- Primary because: Directly exposes the checkpoint's configuration details for the exact checkpoint (model_type, hidden_size, num_hidden_layers, num_attention_heads, max_position_embeddings, tokenizer token id slots).
- Scope: config.json for snowflake-arctic-embed-l-v2.0
- Supports: model_type is "xlm-roberta" (XLMRobertaModel).
- Supports: hidden_size = 1024.
- Supports: intermediate_size = 4096.
- Supports: num_hidden_layers = 24.
- Supports: num_attention_heads = 16.
- Supports: max_position_embeddings = 8194.
- Supports: tokenizer token id slots (bos_token_id, eos_token_id, pad_token_id) are present.

### snowflake-arctic-embed-l-v2.0 README (repository blob)

- URL: https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/blob/6022d0ed2f4198f019f6f8e762c4cd363c18f19d/README.md
- Publisher: Snowflake (repository README)
- Type: `repository`
- Primary because: Repository README containing a metrics table and parameter-count assertions; provides an alternate parameter-count figure and MTEB retrieval score for the checkpoint as published in the repository.
- Scope: README blob for snowflake-arctic-embed-l-v2.0
- Supports: Reports an MTEB Retrieval Score (NDCG@10) of 55.98 in the README metrics table.
- Supports: Lists an alternate parameter count (335 million) in the README.

### Snowflake AI_EMBED SQL reference

- URL: https://docs.snowflake.com/en/sql-reference/functions/ai_embed
- Publisher: Snowflake documentation
- Type: `official-documentation`
- Primary because: Official Snowflake SQL reference documenting the AI_EMBED function and listing supported models including this checkpoint; documents SQL calling convention and VECTOR return type.
- Scope: snowflake-arctic-embed-l-v2.0 (AI_EMBED SQL exposure)
- Supports: AI_EMBED lists snowflake-arctic-embed-l-v2.0 as a supported text embedding model.
- Supports: AI_EMBED returns a VECTOR type containing the embedding.
- Supports: Example usage: SELECT AI_EMBED('snowflake-arctic-embed-l-v2.0', 'hello world');

### Snowflake Cortex REST API — embed API (developer guide)

- URL: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/cortex-embed/cortex-embed-introduction
- Publisher: Snowflake documentation (developer guide)
- Type: `official-documentation`
- Primary because: Official Snowflake developer-guide documentation describing the Cortex embed REST API endpoint and request path for embeddings; authoritative provider runtime binding for REST calls.
- Scope: Cortex embed REST API (provider/runtime documentation)
- Supports: Documents the POST /api/v2/cortex/inference:embed endpoint for embedding text.

### Snowflake Cortex REST API — embed API (user guide)

- URL: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api/embed-api
- Publisher: Snowflake documentation
- Type: `official-documentation`
- Primary because: Official Snowflake user-guide documentation describing Cortex REST embed API usage, request/response shape, and runtime constraints.
- Scope: snowflake-arctic-embed-l-v2.0 (served via Snowflake Cortex embed API)
- Supports: The EMBED endpoint model argument specifies the model to create embeddings.
- Supports: The request JSON accepts a "text" array (up to 1280 strings, each up to 4096 characters) and a "model" field.
- Supports: Authentication and role requirements for using the Cortex REST API are documented.

### Snowflake Cortex Search overview (Cortex Search docs referencing model variants)

- URL: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview
- Publisher: Snowflake documentation
- Type: `official-documentation`
- Primary because: Official Snowflake documentation describing Cortex Search behavior and noting supported model variants and recommended chunking/truncation behavior.
- Scope: snowflake-arctic-embed-l-v2.0 (Cortex Search documentation)
- Supports: States snowflake-arctic-embed-l-v2.0 has 1024 output dimensions and multilingual support and references a -8k variant with an 8192-token context window.
- Supports: Recommends splitting text into chunks (≈512 tokens) for indexing and notes truncation behavior when input exceeds context window.

## Evidence gaps

- Canonical tokenizer implementation files (tokenizer.json, vocab files, tokenizer-specific normalization or pre-tokenization rules) for this exact checkpoint were not present in the inspected primary sources.
- Per-dataset splits, exact metric definitions, pooling/prompting/aggregation protocol, and evaluation scripts required to reproduce the reported BEIR/MIRACL/CLEF/MTEB aggregate numbers are not present in the inspected primary artifacts.
- Conflicting parameter-count reports for this checkpoint: Hugging Face model card reports 568M total parameters (303M non-embedding) while a README blob in the same repository lists 335M. No immutable upstream revision hash was found in the inspected primary artifacts to reconcile these counts.
- Conflicting context-window evidence: the checkpoint config.json reports max_position_embeddings = 8194 while Snowflake Cortex Search docs state the base l-v2.0 model has a 512-token context and a distinct -8k variant provides 8192-token support. The inspected primary artifacts do not reconcile which exact context window applies to this named checkpoint.
- Exact tensor dtype for published embeddings (e.g., float32) is not specified in the inspected primary artifacts for this exact checkpoint; dtype should be validated at runtime.
- Model-card and README aggregate benchmark numbers lack per-dataset tables and reproducible evaluation scripts in the inspected primary artifacts; head-to-head, protocol-matched comparisons against peers cannot be constructed from the available primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 11 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'snowflake-labs' for this exact model scope: $.sources[8] uses unapproved repository owner 'snowflake-labs' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary host benchmarklist.com: $.sources[9] uses forbidden secondary host benchmarklist.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary host ai.azure.com: $.sources[11] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[1] without evidence must be labeled as a Forge policy or evidence gap: $.safety[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.identity.parameterScale_evidenceUrls: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.inputPreparation_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
