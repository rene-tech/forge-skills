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

- Research key: `huggingface-co-openbmb-minicpm5-1b-e330c92570`
- Independent audit: `revised`
- Researched: `2026-08-06T13:19:29.874467+00:00`

Verified primary artifacts for openbmb/MiniCPM5-1B (Hugging Face model blobs and the OpenBMB GitHub README) show a LlamaForCausalLM-style decoder model configuration with 24 layers, 16 attention heads, grouped key/value heads = 2, hidden_size 1536, intermediate_size 4608, head_dim 128, SiLU activation, rope_theta = 5,000,000, max_position_embeddings = 131,072, vocab_size = 130,560, use_cache = true, and torch_dtype = bfloat16. The model-hosted generation_config.json declares do_sample = true, temperature = 0.9, top_p = 0.95 and transformers_version = 5.6.2. The OpenBMB README (repository root) reports an aggregate average benchmark score (42.57) across multiple evaluation categories but does not provide per-dataset splits or a reproducible evaluation protocol. Several low-level items required for operational certainty are not present in the inspected primary files and are recorded as evidence gaps (exact parameter count in upstream blobs, license text for model weights vs code, tokenizer identity and exact special-token id numbers, per-dataset benchmark protocol and splits, and explicit safety/clinical/PHI-handling guidance).

## Identity

- Upstream name: openbmb/MiniCPM5-1B
- Checkpoint/version: MiniCPM5-1B
- Immutable revision: not reported
- Parameter scale: evidence gap: exact total parameter count not reported in the reviewed primary artifacts
- Architecture/head: architectures = ["LlamaForCausalLM"]; model_type = "llama"; num_hidden_layers = 24; num_attention_heads = 16; num_key_value_heads = 2; head_dim = 128; hidden_size = 1536; intermediate_size = 4608; hidden_act = "silu"; rope_theta = 5000000; max_position_embeddings = 131072; use_cache = true; torch_dtype = bfloat16; vocab_size = 130560
- License: evidence gap: exact model-weight or repository LICENSE text/type not present in the reviewed primary blobs
- Evidence: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/main/config.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base, https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json, https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/special_tokens_map.json, https://github.com/OpenBMB/MiniCPM/blob/main/README.md, https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/64c2e3ae79542983b70ff9e03f24685569878be0/.ms_upload_cache

## Selection

### Recommended

- **Local / on-device assistant and resource-constrained deployments using the upstream MiniCPM5-1B checkpoint** — The Hugging Face model page lists supported local deployment backends (Transformers BF16/FP16, llama.cpp (GGUF), Ollama, LM Studio, MLX/4-bit), and the project README and model hosting emphasize local / on-device deployment and supported runtime backends.
  Scope: MiniCPM5-1B (upstream checkpoint; model-hosted metadata and README)
  Evidence: https://huggingface.co/openbmb/MiniCPM5-1B-Base, https://github.com/OpenBMB/MiniCPM/blob/main/README.md
- **Applications requiring very long context windows (research or evaluation of long-context performance), after runtime validation** — The model config and model card state a native maximum position embeddings / context length of 131,072 tokens; using such long contexts requires validating the chosen runtime and memory behavior.
  Scope: MiniCPM5-1B (upstream config: max_position_embeddings = 131072)
  Evidence: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base
- **Reasoning, multi-step math, and coding tasks using the model's documented generation defaults (when validated for the target runtime)** — The model-hosted generation_config.json sets do_sample true with temperature 0.9 and top_p 0.95; the project documents a Think/No-Think mode concept on the model card and README (switching generation mode is a documented feature of the upstream artifacts).
  Scope: MiniCPM5-1B (upstream generation_config.json and README describing Think/No-Think usage)
  Evidence: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json, https://github.com/OpenBMB/MiniCPM/blob/main/README.md, https://huggingface.co/openbmb/MiniCPM5-1B-Base

### Conditional

- **Using extended context lengths (tens of thousands of tokens) in production workflows** — Explicitly validate memory, truncation behavior, and correctness on the chosen runtime. Primary artifacts show native support up to 131,072 tokens but do not document runtime defaults or per-runtime configuration; therefore runtime-level testing and configuration are required.
  Scope: MiniCPM5-1B (upstream config max_position_embeddings = 131072). Condition applies to downstream runtime configuration.
  Evidence: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base

### Avoid

- **Clinical decision-making, PHI-sensitive automated processing, or other regulated clinical deployments** — No primary-source documentation in the reviewed model-hosted blobs or repository README provides clinical validation, PHI handling guidance, regulatory compliance statements, or operational clinical safeguards for MiniCPM5-1B.
  Scope: MiniCPM5-1B (upstream checkpoint and repository materials)
  Evidence: https://github.com/OpenBMB/MiniCPM/blob/main/README.md, https://huggingface.co/openbmb/MiniCPM5-1B-Base

## Input preparation

### Semantic inputs

- Primary accepted input modality: text (prompts / chat messages) as a causal LM checkpoint. Sources: https://huggingface.co/openbmb/MiniCPM5-1B-Base, https://github.com/OpenBMB/MiniCPM/blob/main/README.md
- The upstream config declares a large native context capacity (max_position_embeddings = 131072); callers should treat context-length usage as subject to runtime validation. Sources: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json

### Accepted formats

- The model-hosted materials list supported deployment backends and runtime formats including Transformers (BF16/FP16 inference), llama.cpp (GGUF local inference), Ollama (GGUF local runtime), LM Studio (GGUF Mac desktop), and MLX (4-bit on Apple Silicon). Sources: https://huggingface.co/openbmb/MiniCPM5-1B-Base

### Preprocessing

- The upstream config lists vocab_size = 130560; tokenization artifacts (tokenizer name/version) are not specified in the reviewed primary blobs. Sources: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base
- Special token textual contents (e.g., bos '<s>', eos '</s>', pad '</s>', unk '<unk>') are defined in the special_tokens_map.json blobs; explicit numeric token ids for these special tokens are not present in the reviewed primary blobs and therefore are an evidence gap. Sources: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/special_tokens_map.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/special_tokens_map.json
- Generation defaults (do_sample true, temperature 0.9, top_p 0.95) are declared in the model-hosted generation_config.json and inform sampling behavior unless overridden at runtime. Sources: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json

### Pre-submit validation

- Before deploying long-context workloads, validate truncation/memory/latency on the chosen runtime because native max_position_embeddings is 131,072 but runtime behavior is implementation-dependent. Sources: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json, https://huggingface.co/openbmb/MiniCPM5-1B-Base
- Evidence gap: explicit tokenizer identity (repository/name/version) and numeric special-token ids are not present in the reviewed primary blobs; callers must obtain or confirm tokenizer artifacts before production deployment.

### Task-specific formatting

- The upstream README and model-hosted materials document a Think/No-Think generation mode concept (enable_thinking flag referenced) but do not provide a full, canonical prompt template in the reviewed blobs; therefore exact template tokens and wrapped-message markers are an evidence gap in the checked primary files. Sources: https://github.com/OpenBMB/MiniCPM/blob/main/README.md, https://huggingface.co/openbmb/MiniCPM5-1B-Base

## Output interpretation

### Outputs

- Primary output type is generated text tokens from a causal LM; the generation_config.json declares sampling defaults (do_sample true, temperature 0.9, top_p 0.95). Sources: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json
- The model config sets use_cache = true, indicating attention/key-value caching is enabled during generation in the upstream checkpoint configuration. Sources: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json

### Interpretation

- Generated token sequences should be interpreted as causal LM outputs; sampling hyperparameters in the generation_config.json influence randomness and behavior. Sources: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json
- Evidence gap: the reviewed primary artifacts do not include an explicit upstream output contract for logits, probabilities, or embeddings (shapes, units, or API fields).

### Post-inference validation

- Validate generation behavior when changing sampling settings (temperature, top_p) against known-answer tasks before deploying to production; generation defaults are declared in generation_config.json but runtime implementations may differ. Sources: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json

## Public benchmarks

### Aggregate evaluation across reasoning, knowledge, code, instruction-following, math, logic, and agentic benchmarks (aggregate score reported by repository)

- Dataset/split: aggregate evaluation suites (per-repository grouping reported in README; per-dataset names/splits not enumerated) / not reported
- Metric/value: aggregate average score (repository-reported aggregation) / 42.57 (`higher-is-better`)
- Model scope: MiniCPM5-1B (repository claim in README)
- Conditions: Repository-level aggregate claim; per-dataset protocol, splits, and evaluation harness are not provided in the referenced primary artifact
- Source: https://github.com/OpenBMB/MiniCPM/blob/main/README.md
- Locator: README.md (root) — repository-level evaluation summary paragraph reporting an aggregate average score of 42.57
- Caveat: The README does not list per-dataset numeric breakdowns, dataset splits, metric definitions, or the exact evaluation harness; direct reproducibility is not possible from this artifact alone.

## Comparisons

### qwen-qwen3-8b — `insufficient-evidence`

- Task: aggregate evaluation suites (reasoning, knowledge, code, instruction-following, math, logic, agentic)
- Criteria: No reproducible, checkpoint-to-checkpoint per-dataset numeric breakdown or evaluation protocol present in the inspected primary artifacts to support a direct comparison.
- Rationale: The repository README reports an aggregate score but does not provide the per-dataset results, splits, or exact evaluation harness necessary to reproduce or validate a head-to-head comparison with Qwen3-8B.
- Comparison conditions: Reproducible comparison would require (1) the exact checkpoint tag used, (2) per-dataset scores and splits, (3) evaluation harness code or seed/configuration, and (4) the alternative model's matching evaluation outputs.
- Evidence: https://github.com/OpenBMB/MiniCPM/blob/main/README.md

### allenai-olmo-2-1124-7b-instruct — `insufficient-evidence`

- Task: general/document-ai tasks
- Criteria: No primary-source checkpoint-to-checkpoint comparison or shared benchmark protocol is present in the reviewed artifacts.
- Rationale: The inspected upstream blobs do not include per-dataset comparisons or a protocol usable to compare to this alternative.
- Comparison conditions: Reproducible comparison would require per-dataset metrics, checkpoint identifiers, and evaluation-harness details for both models.
- Evidence: https://github.com/OpenBMB/MiniCPM/blob/main/README.md

## Limitations and safety

### Limitations

- Evidence gap: exact model-weight license text/type and distinctions between model weights vs repository/code licensing are not present in the reviewed primary blobs.
- Evidence gap: exact total parameter count and non-embedding parameter breakdown are not present in the reviewed primary blobs.
- Per-dataset benchmark breakdowns, dataset splits, and the full evaluation protocol are not provided in the repository README; the aggregate score alone prevents reproducible benchmarking. Sources: https://github.com/OpenBMB/MiniCPM/blob/main/README.md
- Evidence gap: tokenizer repository/name/version and numeric special-token ids are not present in the reviewed primary blobs; callers must obtain or confirm tokenizer artifacts before production deployment.

### Safety

- Evidence gap: the reviewed upstream model-hosted blobs and repository README do not provide explicit clinical, PHI-handling, or domain-specific safety and misuse mitigation guidance for MiniCPM5-1B.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MiniCPM5-1B-Base config.json (Hugging Face blob, exact commit/blob path)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/config.json
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: First-party model configuration blob listing architectures, layer counts, attention-head counts, dtype, max_position_embeddings, vocab_size, and other upstream model identity fields.
- Scope: MiniCPM5-1B-Base config.json (specific blob)
- Supports: architectures = ["LlamaForCausalLM"]
- Supports: hidden_size = 1536
- Supports: intermediate_size = 4608
- Supports: num_hidden_layers = 24
- Supports: num_attention_heads = 16
- Supports: num_key_value_heads = 2
- Supports: head_dim = 128
- Supports: max_position_embeddings = 131072
- Supports: torch_dtype = bfloat16
- Supports: use_cache = true
- Supports: vocab_size = 130560
- Supports: hidden_act = "silu"

### MiniCPM5-1B-Base config.json (Hugging Face blob, main path reporting rope_theta and tie_word_embeddings)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/main/config.json
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: First-party model configuration blob (main path) containing rope_theta and tie_word_embeddings entries.
- Scope: MiniCPM5-1B-Base config.json (main path)
- Supports: rope_theta = 5000000
- Supports: tie_word_embeddings = false

### MiniCPM5-1B generation_config.json (Hugging Face blob)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/generation_config.json
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: First-party generation configuration file declaring sampling defaults and transformers_version.
- Scope: MiniCPM5-1B generation_config.json (main blob)
- Supports: do_sample = true
- Supports: temperature = 0.9
- Supports: top_p = 0.95
- Supports: transformers_version = "5.6.2"

### MiniCPM5-1B-Base generation_config.json (Hugging Face blame view)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blame/main/generation_config.json
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: Blame view of the model-hosted generation_config confirming transformers_version metadata for the Base hosted repo.
- Scope: MiniCPM5-1B-Base generation_config.json (blame view)
- Supports: transformers_version = "5.6.2"

### MiniCPM5-1B special_tokens_map.json (Hugging Face blob)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B/blob/main/special_tokens_map.json
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: First-party special_tokens_map file declaring textual special-token contents for the hosted checkpoint.
- Scope: MiniCPM5-1B special_tokens_map.json (main blob)
- Supports: bos token content = "<s>"
- Supports: eos token content = "</s>"
- Supports: pad token content = "</s>"
- Supports: unk token content = "<unk>"

### MiniCPM5-1B-Base special_tokens_map.json (Hugging Face blob)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/f731357bacfa8ba90f0b64b9cc5485ac5dbdf95b/special_tokens_map.json
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: First-party special_tokens_map file for the Base repo confirming textual special-token contents.
- Scope: MiniCPM5-1B-Base special_tokens_map.json (specific blob)
- Supports: bos token content = "<s>"
- Supports: eos token content = "</s>"
- Supports: pad token content = "</s>"
- Supports: unk token content = "<unk>"

### MiniCPM5-1B-Base model page (Hugging Face model card)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B-Base
- Publisher: OpenBMB (Hugging Face model hosting)
- Type: `model-card`
- Primary because: Official hosted model card for the Base checkpoint listing supported backends, intended use, long-context support, and general model descriptions.
- Scope: MiniCPM5-1B-Base model card
- Supports: description of LlamaForCausalLM architecture and intended local-assistant/use-case guidance
- Supports: statement that the model provides native long-context support and Think/No-Think chat modes
- Supports: list of supported deployment backends (Transformers, vLLM, llama.cpp, Ollama, LM Studio, MLX)

### OpenBMB MiniCPM repository README (GitHub root README.md)

- URL: https://github.com/OpenBMB/MiniCPM/blob/main/README.md
- Publisher: OpenBMB (GitHub repository)
- Type: `repository`
- Primary because: First-party project repository README containing project description and a repository-level evaluation summary claim (aggregate average score).
- Scope: Repository README (root)
- Supports: repository-level aggregate evaluation claim reporting an average score of 42.57 across multiple benchmark categories
- Supports: mention of a built-in chat template and an enable_thinking flag as a repository feature

### .ms_upload_cache (Hugging Face model repo metadata blob)

- URL: https://huggingface.co/openbmb/MiniCPM5-1B-Base/blob/64c2e3ae79542983b70ff9e03f24685569878be0/.ms_upload_cache
- Publisher: OpenBMB (Hugging Face model repo)
- Type: `model-card`
- Primary because: First-party hosted repo upload cache showing exact uploaded file sizes for model weights and key metadata files.
- Scope: MiniCPM5-1B-Base upload cache blob
- Supports: model-00000-of-00001.safetensors file size and sizes for config/generation_config/special_tokens_map blobs

### Exact official starting source declared by Forge

- URL: https://huggingface.co/openbmb/MiniCPM5-1B
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: openbmb-minicpm5-1b
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Exact total parameter count for the upstream MiniCPM5-1B checkpoint is not present in the reviewed primary blobs; a model-weight manifest or explicit parameter-count statement in the upstream artifacts is required to verify this.
- Exact model-weight license text/type and an explicit statement distinguishing model-weight licensing from repository/code licensing are not present in the reviewed primary blobs; the upstream LICENSE file or an explicit model-weight license blob is required.
- Tokenizer identity (repository/name/version) and numeric special-token ID mappings are not present in the reviewed primary blobs; the tokenizer artifact or explicit mapping file is required to verify tokenizer identity and token ids.
- Per-dataset benchmark breakdowns, dataset splits, metric definitions, and the full evaluation harness/protocol for the README-reported aggregate score are not present in the reviewed primary artifacts; these are required to reproduce or validate reported benchmark numbers.
- Explicit upstream output contract (logits/probabilities/embedding shapes and API field names) is not present in the reviewed primary artifacts; runtime or API documentation from the model owner is required to verify these details.
- Primary deployment skill files (skills/* SKILL.md) and other repository subpaths were not present in the supplied research-findings blobs; any claims that would rely on those files should be re-verified against those exact repo paths if needed.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 16 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0] uses forbidden secondary host ollama.com: $.sources[0] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'abiray' for this exact model scope: $.sources[12] uses unapproved repository owner 'abiray' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary URL https: $.sources[13] uses forbidden secondary URL https://huggingface.co/openbmb/MiniCPM5-1B/discussions/4 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/OpenBMB/MiniCPM/blob/main/docs/deployment/transformers.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/OpenBMB/MiniCPM/blob/main/docs/deployment/transformers.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/OpenBMB/MiniCPM/blob/main/docs/deployment/transformers.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/OpenBMB/MiniCPM/blob/main/docs/deployment/transformers.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/OpenBMB/MiniCPM/blob/main/docs/deployment/transformers.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/openbmb/MiniCPM5-1B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
