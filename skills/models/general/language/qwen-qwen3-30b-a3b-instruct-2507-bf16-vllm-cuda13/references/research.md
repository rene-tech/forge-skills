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

- Research key: `huggingface-co-qwen-qwen3-30b-a3b-instruct-2507-ff761b3644`
- Independent audit: `revised`
- Researched: `2026-08-06T09:27:17.220546+00:00`

This dossier documents primary artifacts inspected for the Hugging Face checkpoint Qwen3-30B-A3B-Instruct-2507 and the canonical Qwen3 technical report (arXiv:2505.09388). Primary repository blobs located in the checkpoint repository include README.md, config.json, a config_1m.json (refs/PR), tokenizer_config.json, vocab.json, merges.txt, a LICENSE blob, and the repository commit history. The README and config_1m.json indicate MoE architecture and long-context support; config_1m.json lists model fields including num_experts=128 and num_experts_per_tok=8 and hidden_size/head_dim/intermediate_size values. tokenizer_config.json and vocab.json are present in the checkpoint repository and tokenizer_config.json records multiple special tokens and the model_max_length entry identified in repository blobs. The repository contains an explicit LICENSE file stating Apache License, Version 2.0. The model page lists benchmark scores, but the inspected checkpoint blobs and the technical report do not provide per-benchmark protocol artifacts (dataset splits, prompt templates, few/zero-shot settings, or scoring/aggregation) sufficient to protocol-verify model-page numeric benchmark rows for this exact checkpoint. Evidence gaps listed below identify missing or ambiguous checkpoint-scoped protocol artifacts and the exact repository locations that were examined.

## Identity

- Upstream name: Qwen3-30B-A3B-Instruct-2507
- Checkpoint/version: Qwen3-30B-A3B-Instruct-2507
- Immutable revision: 3ffd1f5 (commit 'Add 1M support (#12)')
- Parameter scale: 30.5 billion total parameters; 3.3 billion activated parameters; 29.9 billion non-embedding parameters (README.md)
- Architecture/head: Qwen3MoeForCausalLM (Mixture-of-experts MoE causal language model) as indicated by config_1m.json and README.md
- License: Apache License, Version 2.0 (LICENSE in repository)
- Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/110954009be4a882781a90356c7d2b8a9e3428dc/LICENSE, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/commits/main, https://arxiv.org/pdf/2505.09388

## Selection

### Recommended

- **General instruction following and conversational/dialog tasks** — The repository README demonstrates instruction/chat generation usage and the model page identifies this checkpoint as an Instruct variant.
  Scope: Qwen3-30B-A3B-Instruct-2507
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md
- **Long-context document-grounded workflows (conditional on following README/config_1m.json guidance)** — The repository contains a config_1m.json intended for length extrapolation and the README provides long-context workflow instructions; tokenizer_config.json and config_1m.json contain fields indicating extended-context support.
  Scope: Qwen3-30B-A3B-Instruct-2507 with README-driven config_1m.json workflow
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json
- **Coding assistance and code generation (research/deployment with downstream validation)** — The README and model card present this checkpoint as an Instruct variant with coding-related capability claims; use for code generation should include downstream validation and protocol-specific testing.
  Scope: Qwen3-30B-A3B-Instruct-2507
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md

### Conditional

- **Ultra-long context (hundreds of thousands to ~1,010,000 tokens) inference** — Must follow README-documented workflow: replace config.json with config_1m.json as provided in the repository and launch with the README vLLM flags; verify active configuration and target hardware memory before attempting extreme-length runs.
  Scope: Qwen3-30B-A3B-Instruct-2507 with README-driven config_1m.json workflow
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md
- **High-throughput batched serving** — Requires tuning of runtime batching/prefill flags per the README and validating throughput/memory trade-offs on target hardware; the repository does not provide standardized end-to-end latency/memory measurements for this checkpoint.
  Scope: Qwen3-30B-A3B-Instruct-2507
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md

### Avoid

- **Clinical or safety-critical medical diagnosis without domain validation** — No checkpoint-scoped documentation of clinical validation, PHI handling procedures, or regulatory-clearance guidance was located in the inspected checkpoint repository blobs or the family technical report.
  Scope: Qwen3-30B-A3B-Instruct-2507
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://arxiv.org/pdf/2505.09388
- **Assuming the model emits calibrated numeric confidence/probability scores in plain text by default** — The inspected primary artifacts do not document checkpoint-scoped emission of calibrated numeric confidence/probability fields or calibration guarantees.
  Scope: Qwen3-30B-A3B-Instruct-2507
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://arxiv.org/pdf/2505.09388

## Input preparation

### Semantic inputs

- Plain-text instruction prompts and chat-style multi-turn messages (text and code mixtures) are the intended input modalities for this Instruct checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md

### Accepted formats

- README examples use chat-format messages and plain text prompts; generation example code uses from_pretrained/generation call patterns. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507

### Preprocessing

- tokenizer_config.json is present and records tokenizer-level semantics and special tokens; the repository also contains vocab.json and merges.txt tokenizer artifacts. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/vocab.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/fcc1528445189b27dbe3139c2cf9a1139203a4ff/merges.txt
- Repository config.json contains runtime fields relevant to tokenization and runtime behavior (examples observed: num_key_value_heads, output_router_logits, torch_dtype, use_cache, vocab_size). Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/config.json
- README documents launch/runtime flags and a workflow to replace config.json with config_1m.json to enable length extrapolation and sparse attention settings. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json

### Pre-submit validation

- Validate which repository configuration is active (default config.json vs. README-recommended config_1m.json) before submitting long-context inputs; mismatches between tokenizer_config.json model_max_length and the active configuration can affect runtime behavior. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json
- A tokenizer vocabulary artifact (vocab.json) and merges.txt are present in the repository; use these files to verify token-to-string mappings and special-token semantics for input preparation. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/vocab.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/fcc1528445189b27dbe3139c2cf9a1139203a4ff/merges.txt

### Task-specific formatting

- The README demonstrates a chat-template tokenization helper and example generation code; adopt the chat template shown in the README for multi-turn chat inputs. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md
- Evidence gap: The inspected checkpoint blobs do not include a single canonical, standalone prompt-template file enumerating all control tokens and exact canonical usage; verify prompt templates and tokenizer special-token semantics using the listed tokenizer artifacts when precise prompt control is required. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md

## Output interpretation

### Outputs

- Primary model output is generated text (string) produced by the causal language model as shown in README generation examples (max_new_tokens usage). Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507

### Interpretation

- Treat generated text as uncalibrated model output unless downstream calibration or explicit probability-emission mechanisms are implemented; checkpoint-scoped artifacts do not document emission of calibrated numeric confidence/probabilities. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://arxiv.org/pdf/2505.09388
- When using the README chat/tool templates, interpret tool-response blocks according to the repository examples and perform JSON/schema validation on structured outputs post hoc. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md

### Post-inference validation

- Perform downstream validation and expert review for factual, safety-sensitive, or high-stakes outputs; the inspected primary artifacts do not provide checkpoint-scoped calibration or clinical validation. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://arxiv.org/pdf/2505.09388
- For long outputs or JSON-structured responses, validate against an expected schema and enforce output-length bounds where consumers expect a maximum; README examples show long-generation settings that may produce very large outputs. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: benchmark protocol verification
- Criteria: Valid task- and protocol-matched comparisons require exact per-benchmark protocol artifacts (dataset version/split, prompt templates, few-shot/zero-shot setting, and scoring/aggregation) for both the subject checkpoint and the alternative.
- Rationale: The Hugging Face model page lists benchmark scores for this checkpoint but the inspected primary artifacts (checkpoint blobs and the technical report) do not include the per-dataset protocol details required to verify or to match those numeric rows against alternatives.
- Comparison conditions: Require checkpoint-scoped protocol artifacts for each numeric benchmark row (dataset/split, prompt templates, shot settings, and aggregation method) before performing a valid comparison.
- Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://arxiv.org/pdf/2505.09388

## Limitations and safety

### Limitations

- Large GPU memory requirements for extreme-long contexts: the README documents a config replacement and vLLM workflow to enable very long contexts and provides troubleshooting/launch guidance; this implies substantial GPU memory requirements when used for extreme-length inference. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md
- Conflicting or varying reported maximum context-length indicators across inspected artifacts: tokenizer_config.json, README, and config_1m.json contain differing context-length related fields (tokenizer_config.json entries, config_1m.json max_position_embeddings and dual_chunk_attention_config, README long-context claims), creating ambiguity about an authoritative single maximum context length for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md
- Evidence gap: Per-dataset splits, exact prompt templates, few-shot/zero-shot settings, and aggregation protocols for benchmark numbers reported on the model page were not located in the inspected checkpoint repository blobs or the technical report; numeric benchmark rows cannot be protocol-verified from the available artifacts. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://arxiv.org/pdf/2505.09388

### Safety

- Evidence gap: The inspected checkpoint blobs do not provide checkpoint-scoped PHI handling procedures, clinical validation, or regulatory-clearance documentation for Qwen3-30B-A3B-Instruct-2507; treat medical or sensitive-data use as research-only unless additional validation and governance is obtained. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://arxiv.org/pdf/2505.09388
- The repository contains a LICENSE file that states the work is licensed under the Apache License, Version 2.0 (see LICENSE blob). Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/110954009be4a882781a90356c7d2b8a9e3428dc/LICENSE, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/commits/main
- Primary artifacts (README and technical report) document family-level safety evaluation categories, but the inspected README and technical report do not provide full checkpoint-scoped safety-policy artifacts or vulnerability/attack results; perform independent safety evaluation for deployment in sensitive contexts. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://arxiv.org/pdf/2505.09388

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: Qwen3-30B-A3B-Instruct-2507

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507
- Publisher: not reported
- Type: `model-card`
- Primary because: Official Hugging Face model repository page for the exact checkpoint; contains the model card, reported benchmark listings, and links to repository blobs.
- Scope: Qwen3-30B-A3B-Instruct-2507 (model card and repository index)
- Supports: Checkpoint identifier and distribution
- Supports: Links to repository blobs (README, config, tokenizer_config, vocab)
- Supports: Reported benchmark listings on the model page

### Hugging Face model blob: config.json (Qwen3-30B-A3B-Instruct-2507)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/config.json
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository configuration blob available in the checkpoint repository; contains runtime/configuration fields.
- Scope: Qwen3-30B-A3B-Instruct-2507 (config.json blob)
- Supports: Repository configuration/runtime fields (num_key_value_heads, output_router_logits, torch_dtype, use_cache, vocab_size)

### Hugging Face model blob: tokenizer_config.json (Qwen3-30B-A3B-Instruct-2507)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository tokenizer configuration blob for the exact checkpoint; records tokenizer_class, special tokens, and other tokenizer-level fields.
- Scope: Qwen3-30B-A3B-Instruct-2507 (tokenizer_config.json blob)
- Supports: Tokenizer-class and tokenizer-level fields including listed special tokens and tokenizer semantics

### Hugging Face model blob: vocab.json (Qwen3-30B-A3B-Instruct-2507)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/vocab.json
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository tokenizer vocabulary artifact present in the checkpoint repository.
- Scope: Qwen3-30B-A3B-Instruct-2507 (vocab.json)
- Supports: Tokenizer vocabulary (token-to-string mapping) asset for the checkpoint repository

### Hugging Face model blob: merges.txt (Qwen3-30B-A3B-Instruct-2507)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/fcc1528445189b27dbe3139c2cf9a1139203a4ff/merges.txt
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository tokenizer merges artifact present in the checkpoint repository.
- Scope: Qwen3-30B-A3B-Instruct-2507 (merges.txt)
- Supports: Byte-pair merges tokenizer artifact

### Hugging Face model blob: config_1m.json (Qwen3-30B-A3B-Instruct-2507, refs/PR/26)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository blob intended for length-extrapolation configuration; contains explicit architecture and MoE numeric fields for this checkpoint's config_1m.json.
- Scope: Qwen3-30B-A3B-Instruct-2507 (config_1m.json blob)
- Supports: Architecture designation (Qwen3MoeForCausalLM / model_type qwen3_moe)
- Supports: Numeric configuration fields including num_experts, num_experts_per_tok, num_hidden_layers, num_attention_heads, hidden_size, intermediate_size, head_dim, max_position_embeddings, dual_chunk_attention_config, and vocab_size

### Hugging Face model blob: README.md (Qwen3-30B-A3B-Instruct-2507)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository README containing usage examples, long-context workflow notes, and reported checkpoint-scoped descriptive statistics and capability claims.
- Scope: Qwen3-30B-A3B-Instruct-2507 (README.md blob)
- Supports: Usage examples and chat-template suggestions
- Supports: Reported parameter counts and activation counts
- Supports: Description of instruction-following and long-context capabilities
- Supports: Instruction to replace config.json with config_1m.json for length extrapolation

### Hugging Face model blob: LICENSE (Qwen3-30B-A3B-Instruct-2507)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/110954009be4a882781a90356c7d2b8a9e3428dc/LICENSE
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository-distributed LICENSE file for this checkpoint specifying copyright and license terms.
- Scope: Qwen3-30B-A3B-Instruct-2507 (LICENSE blob)
- Supports: License text indicating Apache License, Version 2.0 and copyright attribution

### Hugging Face repository commits: Qwen3-30B-A3B-Instruct-2507 (commit history)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/commits/main
- Publisher: not reported
- Type: `model-card`
- Primary because: Repository commit history showing commit hashes that modify checkpoint blobs (used to identify revision metadata).
- Scope: Qwen3-30B-A3B-Instruct-2507 (commits/main)
- Supports: Commit hashes and history including 'Add 1M support (#12)' (hash 3ffd1f5) and LICENSE creation commits

### Qwen3 technical report (arXiv PDF)

- URL: https://arxiv.org/pdf/2505.09388
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical technical report for the Qwen3 family describing family-level architecture, MoE variants, and family-level evaluation context.
- Scope: Qwen3 family and MoE variants (family-level technical report)
- Supports: Family-level description of Qwen3 series and listing of MoE variants including Qwen3-30B-A3B
- Supports: Family-level safety/evaluation categories

### Qwen3 project repository (reference)

- URL: https://github.com/qwenLM/qwen3
- Publisher: not reported
- Type: `repository`
- Primary because: Authoritative project repository referenced by the technical report and useful to cross-check family-level claims.
- Scope: Qwen3 family repository (reference)
- Supports: Project-level pointers and citations to the Qwen3 technical report and family-level implementation artifacts

## Evidence gaps

- Evidence gap: No per-benchmark protocol artifacts (dataset version/split, exact prompt templates, few-shot/zero-shot settings, and scoring/aggregation) were found in the inspected checkpoint repository blobs or the Qwen3 technical report for the numeric benchmark rows listed on the model page; inspected locations: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md, https://arxiv.org/pdf/2505.09388.
- Evidence gap: While tokenizer artifacts (vocab.json and merges.txt) are present, there is no single canonical checkpoint-scoped prompt-template file enumerating all control tokens and exact canonical prompt usage; inspected locations: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/vocab.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md.
- Evidence gap: The README and config_1m.json provide extended-context indicators, but there is not a single authoritative checkpoint-scoped statement that reconciles tokenizer_config.json model_max_length, config_1m.json max_position_embeddings, and README long-context claims into one canonical maximum context-length value for runtime use; inspected locations: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blob/refs%2Fpr%2F26/config_1m.json, https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507/blame/97291689aa1d570fa5dfe204ddb77274a648fd77/README.md.
- Evidence gap: Checkpoint-scoped formal clinical validation, PHI-handling procedures, or regulatory-clearance documentation for Qwen3-30B-A3B-Instruct-2507 were not found in the inspected checkpoint repository blobs or the technical report; inspected locations: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507 and https://arxiv.org/pdf/2505.09388.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 29 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2] uses unapproved repository owner 'inferless' for this exact model scope: $.sources[2] uses unapproved repository owner 'inferless' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'nvfp4' for this exact model scope: $.sources[5] uses unapproved repository owner 'nvfp4' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'byteshape' for this exact model scope: $.sources[6] uses unapproved repository owner 'byteshape' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[9].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[10].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[11].value must contain a reported numeric result: $.benchmarks[11].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretation_additional: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
