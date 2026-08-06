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

- Research key: `huggingface-co-alibaba-nlp-gte-modernbert-base-f26b0d9716`
- Independent audit: `revised`
- Researched: `2026-07-23T23:39:51.186797+00:00`

Checkpoint-scoped findings (exact checkpoint: Alibaba-NLP/gte-modernbert-base): Supported by the model repo/config/README and inference-provider view, this checkpoint is an encoder-only ModernBERT family embedding model (config.json model_type="modernbert", architecture "ModernBertModel") with hidden_size=768, num_hidden_layers=22, num_attention_heads=12, vocab_size=50368, and max_position_embeddings=8192. The model page and README report an embedding dimension of 768 and a parameter count of 149 million. The repository publishes tokenizer artifacts (tokenizer.json and tokenizer_config.json blob URLs) and a commit-linked safetensors artifact. The README and inference-provider view list numeric benchmark scores (MTEB 64.38; BEIR NDCG@10 55.33; LoCo NDCG@10 87.57; CoIR NDCG@10 79.31) and provide embedding extraction examples (README shows outputs.last_hidden_state[:, 0] / optional L2 normalization and an OpenAI-compatible embeddings JSON curl example). Important evidence gaps (items not explicitly declared in the checked primary files): the repository does not explicitly name a tokenizer implementation class (only tokenizer artifact files are present), the README lacks explicit benchmark protocol, dataset split identifiers, and reproduction/run scripts for reported numeric scores, and the repository does not authoritatively resolve the pooling policy conflict between the README CLS extraction example and config.json classifier_pooling="mean". Also, there is no explicit upstream mapping in the checked files from immutable upstream binary/revision to external serving-wrapper labelled variants (e.g., TEI or vllm pooling builds).

## Identity

- Upstream name: Alibaba-NLP/gte-modernbert-base
- Checkpoint/version: gte-modernbert-base
- Immutable revision: e7f32e3c00f91d699e8c43b53106206bcc72bb22
- Parameter scale: 149 million parameters
- Architecture/head: ModernBertModel (model_type='modernbert'; encoder-only)
- License: Apache-2.0
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/commits/e7f32e3c00f91d699e8c43b53106206bcc72bb22/model.safetensors

## Selection

### Recommended

- **Text embeddings for semantic search and document retrieval** — README usage examples, inference-provider display, and model metadata present embedding extraction examples and label the checkpoint as an embedding model; config.json supports embedding dimension and model architecture consistent with embedding outputs.
  Scope: gte-modernbert-base
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json
- **Long-document retrieval up to model max positions** — Config.json reports max_position_embeddings = 8192 and the README/inference-provider view reference 8192-length usage and long-context benchmark claims tied to the model series.
  Scope: gte-modernbert-base
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- **Reranking as part of the GTE family workflow (family-level)** — The model README and the canonical mGTE paper reference reranker variants within the GTE/mGTE family; repository and paper link the checkpoint to the family research describing reranking applications.
  Scope: gte-modernbert-base (family-level linkage to mGTE)
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://arxiv.org/pdf/2407.19669

### Conditional

- **Code search / code retrieval** — Repository README/inference-provider list CoIR/code retrieval benchmark scores for the checkpoint but do not provide tokenization details for code, dataset splits, or run scripts in the checked files; downstream validation of code-specific tokenization and retrieval ranking is required before production deployment.
  Scope: gte-modernbert-base
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- **Applying L2 normalization prior to similarity computation** — README shows an example of optional L2-normalize but does not mandate it; validate downstream retrieval ranking impact before production use.
  Scope: gte-modernbert-base (README example)
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

### Avoid

- **Autoregressive text generation (generation / decoding tasks)** — Upstream artifacts describe an encoder-only ModernBERT embedding model; no autoregressive decoder or generation head is described in the checked config/README files.
  Scope: gte-modernbert-base
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- **Treating this base checkpoint as a task‑tuned sibling without explicit evidence** — Model card and README distinguish embedding and rerank variants within the GTE series; the upstream checkpoint should not be assumed equivalent to task‑tuned siblings unless the repository documents that mapping.
  Scope: gte-modernbert-base and series
  Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

## Input preparation

### Semantic inputs

- Plain text sequences (English/general text) intended for embedding or reranking. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference

### Accepted formats

- OpenAI-compatible embeddings JSON example using an `input` array of strings and `encoding_format` set to "float" is shown in the repository/inference-provider examples. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference

### Preprocessing

- README shows Python example using AutoTokenizer.from_pretrained and AutoModel.from_pretrained with example options referencing max_length=8192, padding=True, and truncation=True. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Config.json reports `max_position_embeddings = 8192`, indicating positional embedding support to 8192 tokens. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json
- Tokenization artifact files (tokenizer.json and tokenizer_config.json) are present in the repository blobs. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/7ca8b4ca700621b67618669f5378fe5f5820b8e4/tokenizer.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/e7f32e3c00f91d699e8c43b53106206bcc72bb22/tokenizer_config.json

### Pre-submit validation

- The repository files checked do not declare a tokenizer implementation class/name (only tokenizer artifact files are present); confirm tokenizer identity and vocabulary mapping before deploying. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/7ca8b4ca700621b67618669f5378fe5f5820b8e4/tokenizer.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/e7f32e3c00f91d699e8c43b53106206bcc72bb22/tokenizer_config.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json

### Task-specific formatting

- README example extracts embeddings via `outputs.last_hidden_state[:, 0]` (CLS token) and shows optional L2 normalization; inference-provider examples show OpenAI-compatible `v1/embeddings` JSON with `input` list. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference

## Output interpretation

### Outputs

- Model emits a single embedding vector per input text (README demonstrates shape (N, 768) for N inputs when using the example embeddings endpoint). Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

### Interpretation

- Embeddings are intended for nearest-neighbor similarity, retrieval, and reranking; README shows optional L2 normalization which affects downstream similarity computations. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference
- There is an upstream ambiguity between README-extracted CLS pooling and a config-listed classifier_pooling = "mean"; downstream systems must validate pooling semantics in the artifact they deploy. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json

### Post-inference validation

- Post-inference checks should confirm the embedding vector dimensionality (README/inference view assert 768) and pooling behavior (README shows CLS extraction while config.json indicates classifier_pooling='mean'), and whether the deployed artifact applies L2 normalization by default. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json
- No calibration, confidence, or probabilistic score semantics for embeddings are provided in the checked upstream sources; do not infer probabilistic meaning for embedding magnitudes from upstream artifacts. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base

## Public benchmarks

### Embedding evaluation (aggregate)

- Dataset/split: MTEB (English) / not reported
- Metric/value: MTEB score / 64.38 (`context-only`)
- Model scope: gte-modernbert-base
- Conditions: Value listed on README/inference-provider view but README does not provide explicit protocol, dataset split, or run script in the checked files.
- Source: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Locator: README benchmarks section
- Caveat: Protocol, dataset split, and evaluation commands not provided in the checked README file

### Information retrieval

- Dataset/split: BEIR / not reported
- Metric/value: NDCG@10 / 55.33 (`context-only`)
- Model scope: gte-modernbert-base
- Conditions: BEIR NDCG@10 value listed on README/inference-provider view without protocol, split, or run commands in the checked repository files.
- Source: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Locator: README benchmarks section
- Caveat: Protocol, dataset split, and evaluation commands not provided in the checked README file

### Long-document retrieval

- Dataset/split: LoCo / not reported
- Metric/value: NDCG@10 / 87.57 (`context-only`)
- Model scope: gte-modernbert-base
- Conditions: LoCo score reported on README/inference-provider view; README lacks protocol/split specification in the checked files.
- Source: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Locator: README benchmarks section
- Caveat: Protocol, dataset split, and evaluation commands not provided in the checked README file

### Code retrieval

- Dataset/split: CoIR / not reported
- Metric/value: NDCG@10 / 79.31 (`context-only`)
- Model scope: gte-modernbert-base
- Conditions: CoIR score reported on README/inference-provider view; README lacks protocol/split specification in the checked files.
- Source: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Locator: README benchmarks section
- Caveat: Protocol, dataset split, and evaluation commands not provided in the checked README file

## Comparisons

### BAAI/bge-base-en-v1.5 — `insufficient-evidence`

- Task: Embedding for semantic search / retrieval
- Criteria: No primary-source, protocol-matched checkpoint-to-checkpoint comparison was found in the checked artifacts for gte-modernbert-base versus this alternative.
- Rationale: Checked upstream README/config/inference view do not contain direct head-to-head comparisons to the listed alternative checkpoint.
- Comparison conditions: No shared evaluation protocol or direct comparison table present in the repository README or config.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json

### BAAI/bge-large-en-v1.5 — `insufficient-evidence`

- Task: Embedding for semantic search / retrieval
- Criteria: No primary-source, protocol-matched comparison found in the checked upstream artifacts.
- Rationale: Checked upstream README/config/inference view do not contain direct head-to-head comparisons to the listed alternative checkpoint.
- Comparison conditions: No shared evaluation protocol or direct comparison table present in the repository README or config.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base

### ibm-granite/granite-embedding-small-english-r2 — `insufficient-evidence`

- Task: Embedding for semantic search / retrieval
- Criteria: No primary-source, protocol-matched comparison located in the checked artifacts.
- Rationale: No direct primary-source comparisons present in the gte-modernbert-base repository files.
- Comparison conditions: No shared evaluation protocol or direct comparison table present in the repository README or config.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

### intfloat/multilingual-e5-large-instruct — `insufficient-evidence`

- Task: Multilingual embedding / semantic search
- Criteria: No primary-source comparison located in the checked artifacts.
- Rationale: Checked gte-modernbert-base primary sources do not include direct comparisons to this alternative checkpoint.
- Comparison conditions: No shared evaluation protocol or direct comparison table present in the repository README or config.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

### sentence-transformers/all-MiniLM-L6-v2 — `insufficient-evidence`

- Task: Embedding for semantic search / retrieval
- Criteria: No primary-source comparison located in the checked artifacts.
- Rationale: No direct checkpoint-to-checkpoint comparisons found in the gte-modernbert-base README or config.
- Comparison conditions: No shared evaluation protocol or direct comparison table present in the repository README or config.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

### snowflake/snowflake-arctic-embed-l-v2.0 (and M) — `insufficient-evidence`

- Task: Embedding for semantic search / retrieval
- Criteria: No primary-source comparison located in the checked artifacts.
- Rationale: No direct checkpoint-to-checkpoint comparisons found in the gte-modernbert-base README or config.
- Comparison conditions: No shared evaluation protocol or direct comparison table present in the repository README or config.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

## Limitations and safety

### Limitations

- Tokenizer implementation class/name and explicit tokenization algorithm are not declared in the checked repository code/config; only tokenizer artifact files (tokenizer.json, tokenizer_config.json) are present. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/7ca8b4ca700621b67618669f5378fe5f5820b8e4/tokenizer.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/e7f32e3c00f91d699e8c43b53106206bcc72bb22/tokenizer_config.json, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json
- Benchmark protocol, dataset split, and exact reproduction commands for reported numeric scores (MTEB/BEIR/LoCo/CoIR) are not provided in the checked README or repository files. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference
- Pooling policy ambiguity: README extraction example uses CLS token (outputs.last_hidden_state[:, 0]) while config.json lists classifier_pooling = "mean"; the repository does not authoritatively resolve which pooling policy is canonical for embeddings. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json
- No explicit mapping in the checked repository files links specific serving-wrapper variants (TEI or vllm pooling-labelled builds) to an immutable upstream binary/revision with documented I/O-contract differences. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/commits/e7f32e3c00f91d699e8c43b53106206bcc72bb22/model.safetensors, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md

### Safety

- No model-specific safety guidance, PHI/clinical handling advice, or dual-use mitigation measures are described in the checked upstream model card or README. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base, https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Model repository indicates Apache-2.0 licensing for the checkpoint; adhere to Apache-2.0 obligations for model-weight and code use as indicated by the README/license declaration. Sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md, https://huggingface.co/Alibaba-NLP/gte-modernbert-base

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model page for gte-modernbert-base

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base
- Publisher: Alibaba-NLP / Hugging Face
- Type: `model-card`
- Primary because: Official model page providing top-level metadata, parameter count and model card information for the checkpoint.
- Scope: Alibaba-NLP/gte-modernbert-base (model page)
- Supports: The model page shows param size 149 M, dimension 768, and sequence length 8192 for gte-modernbert-base.
- Supports: The model page links to the repository README and model artifacts.

### README.md in the gte-modernbert-base repository

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md
- Publisher: Alibaba-NLP (Hugging Face repository README)
- Type: `repository`
- Primary because: Official README with usage examples, reported benchmarks, and metadata.
- Scope: Alibaba-NLP/gte-modernbert-base (README)
- Supports: The README lists gte-modernbert-base with dimension 768, sequence length 8192, and MTEB‑en score 64.38.
- Supports: The README lists BEIR score 55.33 for gte-modernbert-base.
- Supports: The README lists LoCo NDCG@10 score 87.57 for gte-modernbert-base.
- Supports: The README lists CoIR NDCG@10 score 79.31 for gte-modernbert-base.
- Supports: The README provides a curl command example that sends JSON with "model": "Alibaba-NLP/gte-modernbert-base" and "encoding_format": "float".
- Supports: The README shows Python code using AutoTokenizer.from_pretrained and AutoModel.from_pretrained with max_length=8192, padding=True, truncation=True.
- Supports: The README extracts embeddings via outputs.last_hidden_state[:, 0] and optionally normalizes them with F.normalize.
- Supports: The README states the gte-modernbert series replaces the pre‑training language model base from GTE‑MLM to ModernBert.

### Model config (config.json) for gte-modernbert-base

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json
- Publisher: Alibaba-NLP (Hugging Face repository files)
- Type: `repository`
- Primary because: Official config.json file containing architecture and hyperparameter fields for the checkpoint.
- Scope: Alibaba-NLP/gte-modernbert-base (config.json)
- Supports: The model type of gte-modernbert-base is "modernbert".
- Supports: The architecture listed is "ModernBertModel".
- Supports: The hidden size of gte-modernbert-base is 768.
- Supports: The number of hidden layers is 22.
- Supports: The number of attention heads is 12.
- Supports: The vocabulary size of gte-modernbert-base is 50368.
- Supports: The maximum position embeddings of gte-modernbert-base is 8192.
- Supports: The position embedding type is "absolute".
- Supports: The pad token id is 50283.
- Supports: The CLS/BOS token id is 50281.
- Supports: The SEP/EOS token id is 50282.
- Supports: The classifier_pooling method is "mean".
- Supports: Additional hyperparameters (initializer_range, intermediate_size, local_attention_window_size, rope theta values, etc.) are present in the config.

### Inference-provider view of the model page (hf-inference)

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference
- Publisher: Hugging Face (inference provider view)
- Type: `model-card`
- Primary because: The inference-provider display of the official model-hosted documentation included in the model page.
- Scope: Alibaba-NLP/gte-modernbert-base (inference-provider view)
- Supports: The model demonstrates reported benchmark values and metadata in the inference-provider display.
- Supports: The model supports OpenAI-compatible embeddings JSON input example with `input` array and `encoding_format` set to "float".
- Supports: The output embedding dimension is shown as 768 in the inference view.

### Commit-specific safetensors artifact for gte-modernbert-base (commit e7f32e3c...)

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/commits/e7f32e3c00f91d699e8c43b53106206bcc72bb22/model.safetensors
- Publisher: Alibaba-NLP (Hugging Face commits)
- Type: `repository`
- Primary because: Commit-specific artifact path showing the safetensors file associated with an identified repository commit.
- Scope: Alibaba-NLP/gte-modernbert-base (commit e7f32e3c... / model.safetensors)
- Supports: A safetensors variant was added (artifact referenced at the commit-specific path).

### tokenizer.json blob in gte-modernbert-base repository

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/7ca8b4ca700621b67618669f5378fe5f5820b8e4/tokenizer.json
- Publisher: Alibaba-NLP (Hugging Face repository blobs)
- Type: `repository`
- Primary because: Tokenizer artifact file present in the official repository.
- Scope: Alibaba-NLP/gte-modernbert-base (tokenizer.json)
- Supports: The repository includes a tokenizer.json file for gte-modernbert-base.

### tokenizer_config.json blob in gte-modernbert-base repository (commit e7f32e3c...)

- URL: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/e7f32e3c00f91d699e8c43b53106206bcc72bb22/tokenizer_config.json
- Publisher: Alibaba-NLP (Hugging Face repository blobs)
- Type: `repository`
- Primary because: Tokenizer configuration artifact file present in the official repository at the cited commit.
- Scope: Alibaba-NLP/gte-modernbert-base (tokenizer_config.json)
- Supports: The tokenizer_config.json defines added tokens such as "||IP_ADDRESS||" (id 0) and "<|padding|>" (id 1).
- Supports: The tokenizer_config.json lists special tokens like "<|endoftext|>" (id 50279) and "[UNK]" (id 50280).

### mGTE canonical paper (arXiv PDF)

- URL: https://arxiv.org/pdf/2407.19669
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint linked by the model repository and model card describing the mGTE family research.
- Scope: mGTE family (paper)
- Supports: The paper introduces a text encoder pre-trained by MLM with an 8,192 token context and describes architecture choices (RoPE, GELU, LayerNorm) relevant to the mGTE family.

### mGTE conference paper PDF (ACL Anthology)

- URL: https://aclanthology.org/2025.emnlp-main.316.pdf
- Publisher: ACL Anthology
- Type: `paper`
- Primary because: Published conference paper PDF containing evaluation details for mGTE family models referenced by the repository.
- Scope: mGTE paper (conference proceedings)
- Supports: The mGTE paper provides benchmark rows and training/evaluation details relevant to the mGTE family and documents the family-level research.

## Evidence gaps

- Evidence gap: Tokenizer implementation class/name and explicit tokenization algorithm (e.g., WordPiece/BPE/Unigram) are not declared in the checked repository files; checked files: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/7ca8b4ca700621b67618669f5378fe5f5820b8e4/tokenizer.json , https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/e7f32e3c00f91d699e8c43b53106206bcc72bb22/tokenizer_config.json — these blobs exist but do not state an implementation class name.
- Evidence gap: README and inference-provider view list numeric benchmark scores but do not include explicit evaluation protocol, dataset split identifiers, or run scripts necessary to reproduce reported MTEB/BEIR/LoCo/CoIR values in the checked README or repository files (checked: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md , https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference).
- Evidence gap: Pooling policy authoritative statement is absent: README extraction example uses CLS (`outputs.last_hidden_state[:, 0]`) while config.json lists classifier_pooling = "mean"; the repository does not provide an authoritative internal statement resolving which pooling is canonical (checked: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md , https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/config.json).
- Evidence gap: No explicit mapping in the checked repository files links specific serving-wrapper variants (TEI or vllm pooling-labelled builds) to an immutable upstream binary/revision with documented I/O-contract differences; checked commit artifact and README do not provide that mapping (checked: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/commits/e7f32e3c00f91d699e8c43b53106206bcc72bb22/model.safetensors , https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md).
- Evidence gap: The checked repository files do not publish explicit dataset splits or run commands for the reported benchmark rows; the README/inference view reports values but lacks reproducibility details (checked: https://huggingface.co/Alibaba-NLP/gte-modernbert-base/blob/main/README.md , https://huggingface.co/Alibaba-NLP/gte-modernbert-base?inference_provider=hf-inference).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'miyako' for this exact model scope: $.sources[5] uses unapproved repository owner 'miyako' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'unsloth' for this exact model scope: $.sources[7] uses unapproved repository owner 'unsloth' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
