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

- Research key: `huggingface-co-qwen-qwen3-0-6b-259970c95b`
- Independent audit: `revised`
- Researched: `2026-08-06T09:10:34.975450+00:00`

Qwen3-0.6B (Qwen/Qwen3-0.6B) is a 0.6B-parameter dense causal LM checkpoint in the Qwen3 series licensed under Apache-2.0. Checkpoint-scoped repository files (config.json, tokenizer_config.json, generation_config.json) are available in the Hugging Face model repository and provide exact tokenizer and model-configuration values (layer count, head counts, hidden sizes, special-token mappings, model_max_length, generation defaults). The Qwen3 technical report (arXiv) describes the series (including the 0.6B scale) and reports series- and per-checkpoint benchmark claims, but the inspected primary artifacts contain ambiguous/conflicting values for effective served context length (tokenizer_config.json model_max_length = 131072 vs. config.json max_position_embeddings = 40960) and do not expose dataset-split-level evaluation protocol metadata needed to record apples-to-apples numeric benchmark rows for the exact checkpoint. Where repository files provide checkpoint-scoped configuration (e.g., generation_config.json sampling defaults), those values are reported below; where series-level statements exist without checkpoint-scoped confirmation, we record evidence gaps.

## Identity

- Upstream name: Qwen/Qwen3-0.6B
- Checkpoint/version: Qwen3-0.6B
- Immutable revision: not reported
- Parameter scale: 0.6 billion parameters
- Architecture/head: Model type: qwen3 (Qwen3ForCausalLM). Checkpoint-scoped config.json entries: num_hidden_layers = 28; num_attention_heads = 16; num_key_value_heads = 8; head_dim = 128; hidden_size = 1024; intermediate_size = 3072; hidden_act = "silu"; tie_word_embeddings = true; max_position_embeddings = 40960; rmsnorm_epsilon = 1e-06; rope_theta = 1000000; default torch dtype = bfloat16. These fields are taken from the Qwen3-0.6B config.json and repository files.
- License: Apache-2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/LICENSE, https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-0.6B

## Selection

### Recommended

- **Instruction following and multilingual chat (short to moderate turns)** — Qwen3-0.6B is listed on the official Hugging Face model page as part of the Qwen3 series described for instruction-following, reasoning, agent capabilities, and multilingual support; the Qwen3 technical report describes series-level instruction-following and multilingual capabilities that include the 0.6B scale.
  Scope: Qwen3-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388
- **Short-form logical reasoning, mathematics, and code synthesis for research and prototyping** — The Qwen3 technical report reports strong series-level performance on code generation, mathematics, and reasoning tasks and the Qwen3-0.6B model page describes reasoning and code-capable behavior for the checkpoint; repository-level configuration and generation defaults are available to support prototyping.
  Scope: Qwen3-0.6B
  Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-0.6B

### Conditional

- **Very long-context tasks (document-level summarization, long-document QA)** — Repository tokenizer_config.json, config.json, and the technical report contain conflicting/ambiguous values for supported context length (tokenizer_config.json.model_max_length = 131072 vs config.json.max_position_embeddings = 40960 vs series-level statements). Validate effective end-to-end context by testing the exact deployed checkpoint and serving wrapper before use in long-context production tasks.
  Scope: Qwen3-0.6B (checkpoint-scoped files conflict with series-level statements)
  Evidence: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json, https://arxiv.org/pdf/2505.09388
- **Relying on 'thinking' mode output formatting (<think>...</think>) or automatic internal-chain-of-thought-style markup** — The Qwen3 technical report describes thinking and non-thinking modes at series level. Tokenizer special tokens for <think> and </think> are present in the Qwen3-0.6B tokenizer_config.json, but no explicit checkpoint-scoped statement in the inspected Qwen3-0.6B repository confirms default enabling or runtime behavior for the 0.6B checkpoint. Validate thinking-mode behavior on the exact served artifact before operational reliance.
  Scope: Qwen3-0.6B (tokenizer contains think-tag tokens; default thinking-mode enabling not confirmed)
  Evidence: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://arxiv.org/pdf/2505.09388

### Avoid

- **Automated clinical, medical, or other high-assurance safety‑critical decision-making** — Evidence gap: primary Qwen3-0.6B artifacts inspected do not provide checkpoint-scoped operational safety certifications, clinical-use approvals, or explicit vendor prohibitions/guardrails for safety-critical deployments. Avoid deploying Qwen3-0.6B in clinical or similarly safety-critical automated decision contexts without vendor guidance, regulatory validation, and expert review.
  Scope: Qwen3-0.6B
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- Primary accepted modality is text; the model repository and model page document the checkpoint as a text-generation causal LM intended for text/instruction/dialogue inputs. Sources: https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388

### Accepted formats

- Checkpoint repository exposes tokenizer and generation configuration files for textual inputs; accepted upstream formats for the checkpoint are tokenized text and the standard text-generation inputs expected by Qwen3ForCausalLM implementations. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/generation_config.json

### Preprocessing

- Tokenizer class documented for the checkpoint: Qwen2Tokenizer is specified in tokenizer_config.json. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json
- Tokenizer configuration: clean_up_tokenization_spaces = false; split_special_tokens = false; unk_token = null; pad_token = "<|endoftext|>"; eos token is "<|im_end|>"; model_max_length = 131072 (tokenizer_config.json). Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json
- Model configuration (config.json) provides model-level position embedding and other model hyperparameters that may affect preprocessing/positioning semantics (e.g., max_position_embeddings = 40960); reconcile tokenizer and model config before assuming an end-to-end context length. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json

### Pre-submit validation

- Validate effective end-to-end token limits and truncation behavior for the exact served artifact: tokenizer_config.json lists model_max_length = 131072 while config.json lists max_position_embeddings = 40960; these checkpoint-scoped files conflict and require empirical validation of the deployed model/wrapper. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json
- Validate which special tokens are present and how they are used by the served checkpoint (message boundaries, think-tags, tool-response markers) by testing the exact deployment against tokenizer mappings. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B

### Task-specific formatting

- Repository tokenizer provides special tokens that can denote message boundaries and structured tags (examples: <|im_start|>, <|im_end|>, <|endoftext|>, <think>, </think>, </tool_response>); the repository does not include a checkpoint-scoped instruction-prompt template in the inspected files. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B

## Output interpretation

### Outputs

- Primary documented output modality is text generation (string outputs) from a causal LM checkpoint; repository and model page indicate the checkpoint emits textual responses. Sources: https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388
- Tokenizer-configured special tokens indicate the checkpoint may emit structured tags (e.g., <think>...</think>, </tool_response>, <|im_end|>) and these token-to-string mappings are present in tokenizer_config.json. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json

### Interpretation

- Do not assume calibrated numeric semantics for low-level outputs (logits, calibrated probabilities) from the checkpoint unless the deployed runtime explicitly exposes and documents them; the inspected primary artifacts do not define calibration semantics. Sources: https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388

### Post-inference validation

- Sanity-check generated outputs and special-token emission on the exact served artifact; confirm tokenizer mappings and whether thinking-mode tags or other structured markers are emitted by the deployed checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B
- When output correctness or safety is material to the application, require downstream validation, human review, or calibration experiments on the exact deployed checkpoint and wrapper prior to production use. Sources: https://arxiv.org/pdf/2505.09388

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Training-data provenance and per-datum documentation are not provided in the checkpoint-scoped repository files; the technical report reports a pretraining corpus scale (~36 trillion tokens) at series level but does not provide full per-datum provenance for the checkpoint. Sources: https://arxiv.org/pdf/2505.09388
- Conflicting checkpoint-scoped values for practical maximum context length: tokenizer_config.json.model_max_length = 131072 vs config.json.max_position_embeddings = 40960; series-level text in the technical report references supported large contexts. This conflict is a limitation for long-context use until the effective served limit is validated for the exact deployment. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json, https://arxiv.org/pdf/2505.09388
- Checkpoint-scoped repository files do not include explicit operational safety prohibitions or clinical-use approvals for Qwen3-0.6B; absence of such statements is a limitation for safety-critical deployments. Sources: https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388
- Tokenizer configuration sets unk_token = null and split_special_tokens = false; downstream systems must validate handling of unknown tokens and special tokens in the deployed runtime. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json
- The technical report and model page report series- and per-checkpoint benchmark numbers, but the inspected primary artifacts do not provide dataset split and per-benchmark protocol metadata required to record unambiguous numeric benchmark rows for the exact checkpoint (see EvidenceGaps). Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-0.6B

### Safety

- Evidence gap: Primary Qwen3-0.6B artifacts inspected do not provide checkpoint-scoped operational safety guidance, clinical-use prohibitions, or certifications. Users must not assume the checkpoint is suitable for clinical or other regulated safety-critical uses without vendor guidance and regulatory validation.
- The Qwen3-0.6B checkpoint is licensed under Apache License Version 2.0 as provided in the repository LICENSE file; license terms should be reviewed for downstream compliance obligations. Sources: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/LICENSE

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-0.6B — Hugging Face model page

- URL: https://huggingface.co/Qwen/Qwen3-0.6B
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face repository and model card for the Qwen3-0.6B checkpoint; includes config.json, tokenizer_config.json, generation_config.json, LICENSE, and other checkpoint-scoped files.
- Scope: Qwen3-0.6B model card and repository (primary checkpoint files)
- Supports: identity.checkpoint
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: outputInterpretation.outputs
- Supports: researchSummary

### Qwen3-0.6B config.json (Hugging Face repo file)

- URL: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository config.json documents model architecture hyperparameters (layers, heads, hidden sizes, head_dim, max_position_embeddings, activation, dtype) for the Qwen3-0.6B checkpoint.
- Scope: Qwen3-0.6B config.json (checkpoint-scoped model configuration)
- Supports: identity.architecture
- Supports: inputPreparation.validation
- Supports: limitations

### Qwen3-0.6B tokenizer_config.json (Hugging Face repo file)

- URL: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository tokenizer_config.json documents tokenizer class, special tokens, model_max_length, split_special_tokens, unk_token, and special-token-to-ID mappings for the Qwen3-0.6B checkpoint.
- Scope: Qwen3-0.6B tokenizer_config.json (checkpoint-scoped tokenizer configuration)
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.outputs

### Qwen3-0.6B generation_config.json (Hugging Face repo file)

- URL: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/generation_config.json
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository generation_config.json documents default generation parameters (do_sample, temperature, top_k, top_p, bos/eos/pad token ids) for the Qwen3-0.6B checkpoint.
- Scope: Qwen3-0.6B generation_config.json (checkpoint-scoped generation defaults)
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: recommendedUseCases

### Qwen3-0.6B LICENSE (Hugging Face repo file)

- URL: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/LICENSE
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository LICENSE file for the Qwen3-0.6B checkpoint explicitly declares Apache License Version 2.0 for the checkpoint artifacts.
- Scope: Qwen3-0.6B LICENSE (checkpoint weight license)
- Supports: identity.license
- Supports: safety

### Qwen3-0.6B repository tree

- URL: https://huggingface.co/Qwen/Qwen3-0.6B/tree/main
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository tree listing shows checkpoint files (config, tokenizer, vocab, model weights) and weight file size for the Qwen3-0.6B checkpoint.
- Scope: Qwen3-0.6B repository tree (checkpoint files listing and weights)
- Supports: identity.parameterScale
- Supports: inputPreparation.preprocessing
- Supports: researchSummary

### Qwen3 Technical Report (arXiv PDF)

- URL: https://arxiv.org/pdf/2505.09388
- Publisher: arXiv (Qwen authors)
- Type: `paper`
- Primary because: Canonical technical report on arXiv describing the Qwen3 series, reporting series- and some per-checkpoint results and describing series-level features (thinking mode, dataset scale, languages).
- Scope: Qwen3 technical report (arXiv preprint) covering the Qwen3 series including the 0.6B checkpoint
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: limitations

### Qwen3-0.6B commits (Hugging Face repo)

- URL: https://huggingface.co/Qwen/Qwen3-0.6B/commits/main
- Publisher: Qwen / Hugging Face
- Type: `repository`
- Primary because: Repository commits page documents staged updates to README and tokenizer/config files for the Qwen3-0.6B checkpoint and supports provenance checks of checkpoint-scoped files.
- Scope: Qwen3-0.6B repository commit history
- Supports: identity.revision
- Supports: inputPreparation.preprocessing

## Evidence gaps

- Exact dataset split-level metadata and full per-benchmark evaluation protocol (prompt templates, zero-shot vs. few-shot vs. finetuned conditions) for numeric benchmark values reported for Qwen3-0.6B: checked the Qwen3 technical report (https://arxiv.org/pdf/2505.09388) and the Qwen3-0.6B Hugging Face model page (https://huggingface.co/Qwen/Qwen3-0.6B) and did not find split-level protocol details required to record apples-to-apples numeric benchmark rows for the checkpoint.
- Effective end-to-end served maximum context length for the exact Qwen3-0.6B checkpoint and a given serving wrapper: repository tokenizer_config.json declares model_max_length = 131072 (https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json) while config.json declares max_position_embeddings = 40960 (https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json); the technical report contains series-level context statements (https://arxiv.org/pdf/2505.09388). No single checkpoint-scoped primary artifact unambiguously declares the effective end-to-end served max tokens for Qwen3-0.6B.
- Checkpoint-scoped sampling and serving recommendations (temperature, top_k, top_p, min_p, deterministic-seed guidance) for Qwen3-0.6B beyond the repository generation_config.json defaults: generation_config.json documents do_sample=true, temperature=0.6, top_k=20, top_p=0.95 for the checkpoint (https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/generation_config.json). No additional checkpoint-scoped sampling guidance or deterministic-seed policy is present in the inspected primary artifacts.
- Explicit checkpoint-scoped prompt templates or instruction-format schemas used to tune Qwen3-0.6B: checked Qwen3-0.6B repository files and the technical report (https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388) and did not find explicit per-checkpoint prompt templates or instruction-format artifacts for the 0.6B checkpoint.
- Truncation/padding/batching semantics and API-level token truncation behavior for Qwen3-0.6B when served under specific wrappers: repository files supply tokenizer and model configuration (https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/config.json) but do not specify a per-checkpoint serving contract for truncation/padding/batching; validate on the exact deployment.
- Direct, primary-source, checkpoint-scoped apples-to-apples comparisons between Qwen3-0.6B and external Forge peer checkpoints: the inspected Qwen3-0.6B primary artifacts (https://huggingface.co/Qwen/Qwen3-0.6B and https://arxiv.org/pdf/2505.09388) do not contain per-peer, per-checkpoint matched-protocol comparison tables to support firm comparative numeric claims for the listed peers.
- Explicit checkpoint-scoped statement prohibiting or authorizing clinical/medical/safety-critical use for Qwen3-0.6B: checked the Qwen3-0.6B repository and the technical report (https://huggingface.co/Qwen/Qwen3-0.6B, https://arxiv.org/pdf/2505.09388) and found no explicit clinical-use prohibitions or approvals for this checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 5 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[9] uses forbidden secondary host ai.azure.com: $.sources[9] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary host ollama.com: $.sources[10] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://huggingface.co/papers/2505.09388 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0] without evidence must be labeled as a Forge policy or evidence gap: $.safety[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretation_validation: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
