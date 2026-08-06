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

- Research key: `huggingface-co-qwen-qwen3-embedding-0-6b-03b6bda49f`
- Independent audit: `revised`
- Researched: `2026-08-06T09:27:17.203072+00:00`

Primary upstream artifacts (Hugging Face model card, repository README snapshots, config.json, and the Qwen3 Embedding arXiv papers) identify Qwen/Qwen3-Embedding-0.6B as a 0.6B-parameter embedding model in the Qwen3 series with a 1024-dimensional embedding vector and model configuration indicating max_position_embeddings=32768. The model card and README snapshots report MTEB-style aggregate and per-subtask numbers, but multiple README snapshots show different numeric aggregates (see benchmarks) and the primary sources do not publish end-to-end experimental protocol details (dataset splits, batch sizes, tokenization commands) alongside the reported aggregates. The upstream repository and config.json supply architecture and max-position settings; an immutable checkpoint hash or revision identifier for the specific named checkpoint was not reported in the checked primary sources.

## Identity

- Upstream name: Qwen/Qwen3-Embedding-0.6B
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 0.6 billion parameters
- Architecture/head: Qwen3ForCausalLM; num_hidden_layers: 28; hidden_size: 1024; embedding dimension: 1024; model_type: "qwen3"; num_attention_heads: 16; num_key_value_heads: 8; head_dim: 128; intermediate_size: 3072; max_position_embeddings: 32768; torch_dtype: bfloat16; tie_word_embeddings: true
- License: Apache-2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md, https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/abs/2506.05176, https://arxiv.org/abs/2505.09388

## Selection

### Recommended

- **Text embedding for semantic search and retrieval (monolingual and multilingual).** — Hugging Face model card and the repository README snapshots present the model as an embedding/ranking model and report MTEB-style aggregate scores indicating retrieval/embedding performance.
  Scope: Qwen/Qwen3-Embedding-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md
- **Code retrieval and code-aware multilingual retrieval (use embedding vectors for code/document similarity).** — The model card and repository describe the series' support for programming-language text and list code retrieval among intended tasks.
  Scope: Qwen/Qwen3-Embedding-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://github.com/QwenLM/Qwen3-Embedding
- **Using embeddings as features for clustering and classification downstream tasks.** — Repository README snapshots include reported subtask scores for classification and clustering, and the model card lists clustering/classification among intended uses.
  Scope: Qwen/Qwen3-Embedding-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B

### Conditional

- **Instruction-conditioned embeddings (using explicit instruction prefixes to influence embedding behavior).** — Validate effectiveness per downstream task; README shows instruction-prefixed examples but does not provide the per-task experimental protocol or acceptance thresholds—perform task-specific validation before production use.
  Scope: Qwen/Qwen3-Embedding-0.6B (instruction-aware embedding mode)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md, https://github.com/QwenLM/Qwen3-Embedding
- **Integration via Sentence-Transformers library (instantiate as a SentenceTransformer).** — Repository README/blame indicate Sentence-Transformers usage and required library versions; confirm integration behavior and tokenizer settings in your environment and validate downstream metrics because the README provides integration notes rather than full validation protocols.
  Scope: Qwen/Qwen3-Embedding-0.6B when used through Sentence-Transformers
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blame/main/README.md, https://github.com/QwenLM/Qwen3-Embedding

### Avoid

- **Treating provider-hosted runtime limits or provider-managed server settings as the canonical model input contract.** — Upstream model configuration (config.json) states max_position_embeddings=32768; the model card and repository are the authoritative upstream contract for model architecture and limits. Provider-hosted runtime limits or server wrappers are operational/serving constraints and are not documented as the model's immutable contract in the primary upstream artifacts.
  Scope: Qwen/Qwen3-Embedding-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json
- **Claiming cross-model superiority or protocol-matched superiority based solely on reported aggregate scores in the README/model card.** — Primary README snapshots and the model card report aggregate scores but do not include complete per-experiment protocol details required for protocol-matched comparisons (dataset splits, batch size, exact tokenization steps).
  Scope: Qwen/Qwen3-Embedding-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

## Input preparation

### Semantic inputs

- Text (natural languages) including multilingual inputs and programming-language text (code) are accepted as semantic inputs. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://github.com/QwenLM/Qwen3-Embedding

### Accepted formats

- The Hugging Face inference-style examples in the README show an HTTP POST/JSON style payload with an "inputs" array of strings for batch embedding requests. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md
- The repository documentation indicates the model can be used via Sentence-Transformers (instantiate as a SentenceTransformer) and that certain library version constraints apply; follow the repository README for exact code examples. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blame/main/README.md, https://github.com/QwenLM/Qwen3-Embedding

### Preprocessing

- Respect the model's maximum position embeddings as given in config.json (max_position_embeddings: 32768). Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json
- README recommends enabling flash_attention_2 in model_kwargs for acceleration/memory saving. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

### Pre-submit validation

- Validate that input token count does not exceed the model's max_position_embeddings (32768 as reported in config.json). Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
- If using the Sentence-Transformers integration, confirm requirements and tokenizer configuration (the repository README/blame indicates usage/examples); perform local checks that tokenizer padding_side and library versions behave as expected. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blame/main/README.md, https://github.com/QwenLM/Qwen3-Embedding

### Task-specific formatting

- Example inputs in the README include instruction-prefixed examples (e.g., instruction text such as an "Instruct:" prefix) to illustrate instruction-conditioned embedding behavior; follow README examples when reproducing instruction-aware flows. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md
- The model's inference examples and model card indicate per-input output objects include an "embedding" field containing the embedding vector. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

## Output interpretation

### Outputs

- Each output object includes an "embedding" field; the canonical embedding dimensionality for the 0.6B model is 1024. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json, https://arxiv.org/abs/2506.05176
- The README documents dtype-related behavior in usage examples (e.g., interactions with float16) but does not provide a full API response JSON example with exact numeric array typing and schema in the primary sources. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

### Interpretation

- Treat the embedding vector as a 1024-dimensional feature vector for downstream similarity, clustering, classification, or retrieval; primary sources provide dimensionality but do not specify a canonical distance metric or normalization procedure. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json, https://arxiv.org/abs/2506.05176
- Primary sources do not specify canonical similarity metric semantics (cosine vs dot-product) or an explicit embedding-score calibration procedure. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

### Post-inference validation

- Post-inference sanity checks: confirm returned embedding length equals 1024 and that dtype matches requested dtype in your usage context; verify instruction-conditioned changes via task-specific evaluation because upstream sources do not provide numeric acceptance thresholds. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

## Public benchmarks

### Embedding evaluation (MTEB - English mean task score)

- Dataset/split: MTEB (English) / not reported
- Metric/value: mean task score / 66.33 (`higher-is-better`)
- Model scope: Qwen/Qwen3-Embedding-0.6B
- Conditions: Primary README snapshot reports the aggregate score but does not include per-experiment protocol details (dataset splits, batch size, tokenization commands). See caveats.
- Source: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md
- Locator: README snapshot (main) showing 'Mean(Task) 66.33'
- Caveat: Different README snapshot (specific commit) reports a different 'Mean(Task)' value; primary sources contain multiple README snapshots with differing aggregates. The README snapshots do not publish full experimental protocol details needed for protocol-matched comparisons.

### Embedding evaluation (MTEB - Multilingual mean task score)

- Dataset/split: MTEB (Multilingual) / not reported
- Metric/value: mean task score / 64.33 (`higher-is-better`)
- Model scope: Qwen/Qwen3-Embedding-0.6B
- Conditions: The specific README commit snapshot lists a 'Mean(Task)' value of 64.33; primary sources show differing snapshot aggregates between commits. No per-experiment protocol details are provided alongside numeric aggregates.
- Source: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md
- Locator: README snapshot (commit 66e95e3...) listing 'Mean(Task) 64.33'
- Caveat: Primary sources contain multiple README snapshots with different aggregate values; the README snapshots do not include the experiment protocol required for direct comparability.

### MTEB subtasks (classification, clustering, pair-classification, reranking, retrieval, STS, etc.)

- Dataset/split: MTEB subtasks / not reported
- Metric/value: mean task/subtask scores (per-subtask numeric values) / Classification 66.83; Clustering 52.33; Pair Classification 80.83; Rerank 61.41; Retrieval 64.64; STS 76.17 (as reported in README commit snapshot) (`higher-is-better`)
- Model scope: Qwen/Qwen3-Embedding-0.6B
- Conditions: Per-subtask numbers are reported in the specific README snapshot; the README does not include protocol metadata (dataset splits, tokenization steps, batch size) alongside these numbers.
- Source: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md
- Locator: README snapshot (commit 66e95e3...) benchmark table containing per-subtask numeric values
- Caveat: Benchmarks are taken from a README snapshot commit. A different README snapshot has different numeric aggregates; primary sources do not provide the per-experiment protocol required for reproducibility and protocol-matched comparison.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- License: model and repository indicate Apache-2.0 licensing; comply with Apache-2.0 terms. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://github.com/QwenLM/Qwen3-Embedding
- Primary sources do not disclose detailed training-data composition, dataset provenance, or data-use carve-outs necessary for thorough bias or privacy risk assessment. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/abs/2506.05176
- Primary sources (model card and README snapshots) report benchmark aggregates but omit full experimental protocol details required for reproducible, protocol-matched comparisons (dataset splits, batch sizes, tokenization/preprocessing commands). Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
- Primary sources include multiple README snapshots with differing aggregate numbers, producing ambiguity about which reported aggregate corresponds to the named checkpoint at a specific immutable revision. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md

### Safety

- Primary upstream artifacts (model card, README snapshots, and arXiv paper) do not present model-specific safety mitigations, clinical-use disclaimers, or dual-use handling instructions; no model-specific safety policy text was found in the checked upstream sources. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md, https://arxiv.org/abs/2506.05176

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-Embedding-0.6B — Hugging Face model card

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card for Qwen3-Embedding-0.6B containing model description and links to README and config.
- Scope: Qwen/Qwen3-Embedding-0.6B (model card)
- Supports: model family membership and intended tasks
- Supports: links to README and config.json
- Supports: evaluation/summary claims as presented on the model page

### Qwen3-Embedding README (main)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/README.md
- Publisher: Qwen / Hugging Face (model repository)
- Type: `repository`
- Primary because: Primary repository README snapshot (main) providing usage examples, integration notes, and reported aggregate benchmark numbers.
- Scope: Qwen/Qwen3-Embedding-0.6B (README main)
- Supports: inference input example format ('inputs' array)
- Supports: instruction-aware examples
- Supports: reported aggregate benchmark numbers (Mean(Task) 66.33 in snapshot)

### Qwen3-Embedding README (commit 66e95e3... snapshot)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/66e95e324bebb9453d3b5be447c898dca1ba0eb0/README.md
- Publisher: Qwen / Hugging Face (model repository)
- Type: `repository`
- Primary because: Specific README snapshot commit containing a benchmark table with per-subtask numeric values for the 0.6B variant.
- Scope: Qwen/Qwen3-Embedding-0.6B (README snapshot commit 66e95e3...)
- Supports: benchmark table with per-subtask numeric values (Classification 66.83; Clustering 52.33; Pair Classification 80.83; Rerank 61.41; Retrieval 64.64; STS 76.17)
- Supports: series and variant claims

### Qwen3-Embedding config.json

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/main/config.json
- Publisher: Qwen / Hugging Face (model repository)
- Type: `repository`
- Primary because: Canonical model configuration file specifying architecture parameters (num_hidden_layers, hidden_size, max_position_embeddings, etc.).
- Scope: Qwen/Qwen3-Embedding-0.6B (config.json)
- Supports: architecture details (Qwen3ForCausalLM, hidden_size 1024, 28 layers)
- Supports: max_position_embeddings 32768
- Supports: model_type 'qwen3', num_attention_heads, head_dim, intermediate_size, torch_dtype

### Qwen3-Embedding repository (GitHub)

- URL: https://github.com/QwenLM/Qwen3-Embedding
- Publisher: QwenLM (GitHub)
- Type: `repository`
- Primary because: Official project repository describing the Qwen3 Embedding series, installation/integration notes, and usage examples.
- Scope: Qwen3-Embedding project repository
- Supports: series variants listing (0.6B, 4B, 8B)
- Supports: integration notes and Sentence-Transformers usage examples
- Supports: recommendations such as enabling flash_attention_2 and tokenizer padding_side notes (as documented)

### Qwen3 Embedding — arXiv abstract (2506.05176)

- URL: https://arxiv.org/abs/2506.05176
- Publisher: arXiv / Qwen authors
- Type: `paper`
- Primary because: Canonical preprint abstract page for the Qwen3 Embedding paper describing architecture and series claims.
- Scope: Qwen3 Embedding paper (abstract)
- Supports: paper identifier and publication metadata
- Supports: architecture and series claims as presented in the paper

### Qwen3 Embedding — arXiv technical report (2505.09388)

- URL: https://arxiv.org/abs/2505.09388
- Publisher: arXiv / Qwen authors
- Type: `paper`
- Primary because: Canonical arXiv technical report referenced in the repository and paper set.
- Scope: Qwen3 Embedding technical report
- Supports: technical background and supporting claims referenced by the project

### Qwen3-Embedding README (blame/main snapshot)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blame/main/README.md
- Publisher: Qwen / Hugging Face (model repository)
- Type: `repository`
- Primary because: Blame view of README used to verify repository-present integration notes and version requirements (Sentence-Transformers, transformers).
- Scope: Qwen/Qwen3-Embedding-0.6B (README blame view)
- Supports: statements about required transformers and sentence-transformers versions and SentenceTransformer usage examples

## Evidence gaps

- Evidence gap: immutable checkpoint identifier or immutable revision hash for the named checkpoint 'huggingface-co-qwen-qwen3-embedding-0-6b-03b6bda49f' is not reported in the checked primary sources (checked: Hugging Face model card, config.json, README snapshots, GitHub repository, and arXiv papers).
- Evidence gap: per-benchmark experimental protocol metadata (exact dataset split, batch size, tokenization/preprocessing commands, evaluation script versions) accompanying the reported aggregate and per-subtask numbers is not published in the checked primary sources (checked: README snapshots, Hugging Face model card, and arXiv paper).
- Evidence gap: primary sources do not specify a canonical similarity metric or normalization/calibration procedure for interpreting embedding similarity scores (cosine vs dot-product semantics and normalization guidance absent in checked sources: model card, README snapshots, arXiv).
- Evidence gap: the README and model card do not include a full concrete API response JSON schema example with explicit numeric dtype/shape fields for a hosted inference endpoint; checked: README snapshots and model card.
- Evidence gap: training-data composition, dataset provenance, and data-use constraints are not disclosed in the checked primary sources (checked: model card, GitHub repository, and arXiv paper).
- Evidence gap: no primary-source, same-protocol head-to-head comparisons versus other Forge candidates were found in the checked upstream artifacts (checked: README snapshots, model card, GitHub repo, and arXiv papers).
- Evidence gap: the explicit sentence-transformers model-page query-parameter URL (e.g., the Hugging Face page variant with '?library=sentence-transformers') was not present among the checked primary sources; checked sources: Hugging Face model card and README blame/main.
- Evidence gap: tokenizer artifact presence and the canonical tokenizer file path/contents (e.g., tokenizer.json or tokenizer config keys) were not unambiguously located in the checked primary sources; checked: config.json, README snapshots, and GitHub repository.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 15 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://qwenlm.github.io/blog/qwen3-embedding Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary URL https: $.sources[13] uses forbidden secondary URL https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/discussions/6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses forbidden secondary URL https: $.sources[14] uses forbidden secondary URL https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/discussions/1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary host ollama.com: $.sources[15] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B?library=sentence-transformers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B?library=sentence-transformers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B?library=sentence-transformers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].value must contain a reported numeric result: $.benchmarks[2].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.conditionalUseCases_evidenceGaps_note: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
