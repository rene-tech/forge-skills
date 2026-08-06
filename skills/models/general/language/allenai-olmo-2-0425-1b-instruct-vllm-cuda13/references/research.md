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

- Research key: `huggingface-co-allenai-olmo-2-0425-1b-instruct-4c1e79ec03`
- Independent audit: `revised`
- Researched: `2026-08-06T10:25:44.893613+00:00`

Authoritative Hugging Face repository artifacts for allenai/OLMo-2-0425-1B-Instruct were located and inspected (model card, config.json blame, generation_config.json, README, model.safetensors, commits/commit permalink). The config.json documents architecture-level fields (layers, hidden size, heads, context length, vocab size, pad/eos token ids). An immutable repository commit identifier (2b70dbeaeaa742ef496fa6e752483881f6a3de4b) is present in the repository commits and commit-permalink pages. The repository does not report an explicit numeric parameter count, does not publish per-checkpoint numeric benchmark values tied to this exact Instruct checkpoint, and does not explicitly document exported output tensors (logits/logprobs) or an explicit tokenizer-version/revision for the Instruct checkpoint beyond the repository token artifacts (merges.txt). Where primary upstream evidence was not present, precise evidence gaps are recorded in evidenceGaps.

## Identity

- Upstream name: allenai/OLMo-2-0425-1B-Instruct
- Checkpoint/version: allenai/OLMo-2-0425-1B-Instruct
- Immutable revision: 2b70dbeaeaa742ef496fa6e752483881f6a3de4b
- Parameter scale: not reported
- Architecture/head: Olmo2ForCausalLM (causal decoder transformer); config.json reports 16 hidden layers, hidden_size 2048, 16 attention heads, max_position_embeddings 4096, vocab_size 100352, eos_token_id 100257, pad_token_id 100277 (see config.json blame).
- License: not reported
- Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/commits/main, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/commit/2b70dbeaeaa742ef496fa6e752483881f6a3de4b

## Selection

### Recommended

- **Instruction-following chat and conversational Q&A** — The Instruct repository and README identify this artifact as an instruction‑tuned / post‑trained variant intended for instruction-following and chat scenarios; the README documents the post‑training recipe (SFT -> DPO -> RLVR) and provides chat-style usage guidance.
  Scope: allenai/OLMo-2-0425-1B-Instruct
  Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md
- **Research/experimentation for lightweight on-prem or local inference (1B-class model)** — The model card and README present the artifact as an open-weight, self-hostable instruct-tuned checkpoint with Transformers and vLLM integration examples suitable for local research or experimentation.
  Scope: allenai/OLMo-2-0425-1B-Instruct
  Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

### Conditional

- **vLLM- or Transformers-based serving (production) with downstream validation** — Repository README documents usage with Transformers and notes about vLLM installation; deployers must validate runtime-specific I/O semantics and end-to-end behavior since the upstream repository does not publish an explicit runtime contract for batching, truncation, or exported logits/logprobs.
  Scope: allenai/OLMo-2-0425-1B-Instruct (loaded via Transformers / vLLM)
  Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct
- **Quantized on-device inference (conditional)** — No upstream primary-source statement in the inspected repository files explicitly documents official upstream-distributed quantized artifacts for this exact Instruct checkpoint; any third-party quantized builds must be validated for fidelity by the deployer before use.
  Scope: allenai/OLMo-2-0425-1B-Instruct (quantized artifacts not documented upstream in inspected files)
  Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct

### Avoid

- **Clinical decision-making or production healthcare use without documented clinical validation** — The upstream model card and README do not publish explicit clinical/PHI handling guidance or clinical validation claims for this specific Instruct checkpoint; therefore clinical use without documented validation is unsupported by the inspected primary artifacts.
  Scope: allenai/OLMo-2-0425-1B-Instruct
  Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md
- **Safety‑critical or unmoderated deployment where harmful outputs are unacceptable** — The upstream repository does not document an in‑the‑loop filtering mechanism or exhaustive safety guarantees for this Instruct checkpoint in the inspected primary files.
  Scope: allenai/OLMo-2-0425-1B-Instruct
  Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

## Input preparation

### Semantic inputs

- Plain text instruction-following / chat-style inputs (natural language prompts). Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

### Accepted formats

- Repository provides examples and artifacts for use with Transformers and vLLM; model is presented as a causal language model expecting tokenized text inputs. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

### Preprocessing

- Tokenizer special token ids and vocabulary size are declared in repository config/generation_config: eos_token_id = 100257, pad_token_id = 100277, vocab_size = 100352; these values are defined in config.json and generation_config.json. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/generation_config.json
- A merges.txt tokenization artifact is present in the repository (merges.txt), indicating BPE-style tokenizer artifacts are included in the model repository. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/merges.txt

### Pre-submit validation

- Maximum context length is documented in config.json as 4096 tokens (max_position_embeddings); repository does not publish a per-call truncation/padding policy. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct

### Task-specific formatting

- README and model card provide chat-style guidance and reference special role tokens for user/assistant in prompt templates (chat usage guidance present in README). Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct

## Output interpretation

### Outputs

- The upstream artifact is an autoregressive causal language model that produces text when invoked (usage examples show loading with AutoModelForCausalLM and generating text). Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct

### Interpretation

- The inspected upstream artifacts do not provide calibrated confidence semantics for generated text; consumers should treat outputs as uncalibrated and apply downstream validation for critical tasks. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

### Post-inference validation

- The repository documents the SFT -> DPO -> RLVR post-training recipe at a model level but does not publish a canonical downstream validation checklist for outputs; practitioners must validate domain-specific correctness. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: instruction-following / general-purpose benchmarks
- Criteria: No matched-protocol, checkpoint-scoped numeric comparisons for allenai/OLMo-2-0425-1B-Instruct versus alternative checkpoints were found in the inspected primary artifacts.
- Rationale: Inspected primary upstream pages (model card, README, config.json) do not provide numeric, dataset/split/metric values for the 1B Instruct checkpoint that could be directly compared to other checkpoints under a shared protocol.
- Comparison conditions: Checked https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct and https://huggingface.co/allenai/OLMo-2-0425-1B for matched-protocol numeric comparisons; none found.
- Evidence: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B

## Limitations and safety

### Limitations

- Evidence gap: upstream primary sources do not report an explicit numeric parameter count for the allenai/OLMo-2-0425-1B-Instruct checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json
- Evidence gap: no per-checkpoint numeric benchmarks (dataset/split/metric/value/protocol) for the Instruct checkpoint were published in the inspected primary sources. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B
- Evidence gap: the upstream repository does not explicitly document exported output tensors (logits, per-token logprobs) or calibrated probability semantics for the Instruct checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md
- Evidence gap: the upstream repository does not publish an explicit tokenizer package version or immutable tokenizer revision for the Instruct checkpoint beyond token artifact files (merges.txt); tokenizer 'version' metadata is not reported in inspected files. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/merges.txt, https://huggingface.co/allenai/OLMo-2-0425-1B-SFT/blob/0d85a3d037876ce6ac7d4311d994400fc66ac27f/vocab.json

### Safety

- Evidence gap: the upstream model card and README do not contain explicit clinical/PHI guidance or an explicit in‑the‑loop response-filtering mechanism for this Instruct checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct, https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### allenai/OLMo-2-0425-1B-Instruct — Hugging Face model card

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct
- Publisher: Hugging Face / Allen Institute for AI (model repository)
- Type: `model-card`
- Primary because: Official Hugging Face model repository and model card for the Instruct checkpoint; contains README, files, and links to repository artifacts for this exact checkpoint.
- Scope: allenai/OLMo-2-0425-1B-Instruct
- Supports: Model card and README-level descriptions of the Instruct checkpoint, post-training recipe (SFT -> DPO -> RLVR) mentions, and usage guidance

### allenai/OLMo-2-0425-1B — Hugging Face model card (base)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B
- Publisher: Hugging Face / Allen Institute for AI (model repository)
- Type: `model-card`
- Primary because: Official Hugging Face model repository for the base OLMo-2-0425-1B checkpoint; used for family-level context and linked repository artifacts.
- Scope: allenai/OLMo-2-0425-1B
- Supports: Base-model family-level descriptions and any benchmark/table content present in the base model card

### config.json (blame view) for OLMo-2-0425-1B-Instruct

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Repository configuration file that defines architecture parameters, token ids, vocabulary size, and max position embeddings for the Instruct checkpoint.
- Scope: allenai/OLMo-2-0425-1B-Instruct (config)
- Supports: Architecture fields: 16 layers, hidden_size 2048, 16 attention heads, max_position_embeddings 4096, vocab_size 100352, eos_token_id 100257, pad_token_id 100277

### generation_config.json for OLMo-2-0425-1B-Instruct

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/generation_config.json
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Repository generation configuration file for the Instruct checkpoint; documents generation-related token ids and transformers_version.
- Scope: allenai/OLMo-2-0425-1B-Instruct (generation_config)
- Supports: eos_token_id and pad_token_id settings for generation and transformers_version reference

### commits listing for OLMo-2-0425-1B-Instruct (main)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/commits/main
- Publisher: Hugging Face repository (model artifact metadata)
- Type: `repository`
- Primary because: Repository commits page showing commit history for the Instruct checkpoint repository; provides an immutable commit identifier referenced by the repository.
- Scope: allenai/OLMo-2-0425-1B-Instruct (repo history)
- Supports: Listing of the initial commit hash (2b70dbe) and commit history for the repository

### Commit permalink for initial commit (2b70dbe...)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/commit/2b70dbeaeaa742ef496fa6e752483881f6a3de4b
- Publisher: Hugging Face repository (model artifact metadata)
- Type: `repository`
- Primary because: Immutable commit permalink in the official repository; provides a concrete immutable revision identifier for the repository state.
- Scope: allenai/OLMo-2-0425-1B-Instruct (commit 2b70dbeaeaa742ef496fa6e752483881f6a3de4b)
- Supports: Immutable commit identifier and the files added in that commit (Git LFS filter definitions)

### model.safetensors (Instruct) blob in repository

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/model.safetensors
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Direct model weight artifact file referenced in the official Instruct repository (model.safetensors).
- Scope: allenai/OLMo-2-0425-1B-Instruct (weights file listing)
- Supports: Presence of a model.safetensors file in the official Instruct repository

### README.md (Instruct) in repository

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Repository README providing usage examples, post-training recipe statements, and integration guidance for the Instruct checkpoint.
- Scope: allenai/OLMo-2-0425-1B-Instruct (README)
- Supports: Usage examples (AutoModelForCausalLM.from_pretrained), post-training SFT/DPO/RLVR statements, and vLLM/Transformers integration notes

### model.safetensors index for base checkpoint (stage shards)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B/blame/main/model.safetensors.index.json
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Repository index for base-model safetensors shards documenting sharded weight filenames for the base checkpoint.
- Scope: allenai/OLMo-2-0425-1B (weights index)
- Supports: Indicates base checkpoint safetensors are sharded across model-00001-of-00002.safetensors and model-00002-of-00002.safetensors

### stage1 safetensors blob (base) with SHA-256 reported in repository blame

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B/blame/stage1-step1907359-tokens4001B/model-00001-of-00002.safetensors
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Repository safetensors shard file for the base checkpoint with reported file size and SHA‑256 hash in the repository blame view.
- Scope: allenai/OLMo-2-0425-1B (weights shard)
- Supports: File size and SHA‑256 hash recorded for a base-model safetensors shard

### allenai/OLMo-2-0425-1B tree view (repository)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B/tree/main
- Publisher: Hugging Face repository (model artifact file listing)
- Type: `repository`
- Primary because: Repository file tree for the base checkpoint used to verify presence of base-model artifacts referenced from the Instruct repository.
- Scope: allenai/OLMo-2-0425-1B (repository tree)
- Supports: Repository file listing for base checkpoint artifacts

### allenai/OLMo-2-0425-1B-SFT/vocab.json (SFT repository artifact)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-SFT/blob/0d85a3d037876ce6ac7d4311d994400fc66ac27f/vocab.json
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Vocabulary file present in the SFT repository associated with the OLMo family; used to verify tokenizer artifacts associated with family post-training.
- Scope: allenai/OLMo-2-0425-1B-SFT (vocab artifact)
- Supports: Presence of a vocab.json file in the SFT repository (tokenizer artifact)

### allenai/OLMo-2-0425-1B-RLVR1/merges.txt (RLVR1 tokenizer artifact)

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-RLVR1/blob/main/merges.txt
- Publisher: Hugging Face repository (model artifact file)
- Type: `repository`
- Primary because: Tokenizer merges artifact present in the RLVR1 repository associated with the OLMo family; used for tokenizer-file verification across family repositories.
- Scope: allenai/OLMo-2-0425-1B-RLVR1 (merges artifact)
- Supports: Presence of merges.txt tokenizer artifact in a family-associated repository

### allenai/OLMo-2-0425-1B-Instruct — Hugging Face model card — cited revision/file

- URL: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/merges.txt
- Publisher: Hugging Face / Allen Institute for AI (model repository)
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: allenai/OLMo-2-0425-1B-Instruct
- Supports: Exact audited claim citation

## Evidence gaps

- Evidence gap: exact reported parameter count for allenai/OLMo-2-0425-1B-Instruct — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct and https://huggingface.co/allenai/OLMo-2-0425-1B and did not find an explicit numeric parameter-count statement for the Instruct checkpoint in those primary files.
- Evidence gap: per-checkpoint numeric benchmark results (dataset + split + metric + numeric value + protocol) for allenai/OLMo-2-0425-1B-Instruct — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct and https://huggingface.co/allenai/OLMo-2-0425-1B; no per-checkpoint numeric tables/figures tying dataset/split/metric/numeric-value to this exact Instruct checkpoint were found.
- Evidence gap: explicit upstream statement enumerating exported output tensors/shapes/semantics (logits, per-token logprobs, calibrated probabilities) for allenai/OLMo-2-0425-1B-Instruct — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json and https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/README.md but no explicit output-contract documentation was found.
- Evidence gap: canonical tokenizer package version or immutable tokenizer revision for the Instruct checkpoint — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/merges.txt and https://huggingface.co/allenai/OLMo-2-0425-1B-SFT/blob/0d85a3d037876ce6ac7d4311d994400fc66ac27f/vocab.json and no tokenizer package version or tokenizer-revision metadata was published in those primary files.
- Evidence gap: upstream statement documenting official upstream-distributed quantized artifacts (GGUF, LiteRT-LM, or other quantized formats) for the exact allenai/OLMo-2-0425-1B-Instruct checkpoint — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct (model card and README) and no official upstream quantized-distribution statement was found.
- Evidence gap: explicit upstream confirmation that the Forge-serving variant allenai-olmo-2-0425-1b-instruct-vllm-cuda13 serves an unchanged upstream checkpoint (immutable proof tying that packaged variant to the exact upstream artifact) — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct (model card and README) and the repository commit pages; no explicit mapping statement to that Forge-serving packaging was found in inspected primary artifacts.
- Evidence gap: runtime truncation/padding/batching API-level contract (behavior when inputs exceed context window, explicit pad/truncate policy per API call, batching semantics) — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blame/main/config.json and README but no explicit runtime-level policy was published upstream.
- Evidence gap: numeric hardware latency / memory / throughput measurements for the exact 1B Instruct checkpoint under any specific serving packaging — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct and related repository files and no upstream performance benchmarks for this exact checkpoint+serving configuration were found.
- Evidence gap: matched-protocol checkpoint-to-checkpoint numeric comparisons involving allenai/OLMo-2-0425-1B-Instruct and named external alternatives — inspected https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct and https://huggingface.co/allenai/OLMo-2-0425-1B and found no matched-protocol numeric comparison rows for the 1B Instruct checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 16 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://allenai.org/blog/olmo2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] describes itself as secondary evidence: $.sources[6] describes itself as secondary evidence Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'unsloth' for this exact model scope: $.sources[8] uses unapproved repository owner 'unsloth' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'vllm-project' for this exact model scope: $.sources[9] uses unapproved repository owner 'vllm-project' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'collections' for this exact model scope: $.sources[11] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary host ollama.com: $.sources[15] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct/blob/main/merges.txt: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
