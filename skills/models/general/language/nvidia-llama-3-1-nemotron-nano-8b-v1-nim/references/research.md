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

- Research key: `build-nvidia-com-nvidia-llama-3-1-nemotron-nano-8b-v1-979d519117`
- Independent audit: `revised`
- Researched: `2026-07-23T21:40:23.833745+00:00`

This dossier covers the exact NVIDIA checkpoint Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0). Primary NVIDIA-hosted artifacts (the vendor model card, the vendor Hugging Face repository for nvidia/Llama-3.1-Nemotron-Nano-8B-v1, the checkpoint config.json, the NVIDIA systemcard, NIM documentation, and the NGC container listing) state that this is an 8.0 billion-parameter dense decoder-only Transformer (LlamaForCausalLM) derived from Meta Llama-3.1-8B-Instruct, released 2025-03-18, post-trained for reasoning, human chat preferences, retrieval-augmented generation (RAG), tool calling, and code tasks. Vendor sources report a maximum position embeddings / context window supporting 131,072 positions (128K tokens) and state the model can be deployed locally (fit on a single RTX GPU) and is available as an NVIDIA NIM/container for GPU-accelerated inference. The primary NVIDIA sources inspected do not contain dataset-level numeric benchmark tables or matched-protocol head-to-head evaluation rows for this exact checkpoint; canonical per-dataset protocol details (dataset splits, prompt templates, temperature/seeds, and evaluation scripts) are not present in the inspected primary NVIDIA-hosted model card, systemcard, repository blobs, or NGC/NIM documentation and are recorded as evidence gaps below.

## Identity

- Upstream name: Llama-3.1-Nemotron-Nano-8B-v1 (NVIDIA)
- Checkpoint/version: Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0)
- Immutable revision: 1.0 (released 2025-03-18)
- Parameter scale: 8.0 billion
- Architecture/head: Dense decoder-only Transformer (LlamaForCausalLM)
- License: NVIDIA Open Model License; vendor documentation additionally references the Llama 3.1 Community License Agreement
- Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/config.json, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/systemcard, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/llama-nemotron.html

## Selection

### Recommended

- **General-purpose instruction-following and conversational assistant (chat) tasks** — Vendor model card and the NVIDIA-hosted Hugging Face repository describe the checkpoint as post-trained for reasoning and human chat preferences and list instruction-following/chat among intended applications.
  Scope: Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0)
  Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
- **Code generation and developer-assistant style tasks** — Vendor model card and the NVIDIA-hosted Hugging Face repository list code and coding languages among intended applications and report post-training for coding-related tasks.
  Scope: Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0)
  Evidence: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard
- **Retrieval-augmented generation (RAG) and tool-calling enabled workflows** — Vendor documentation states the checkpoint is post-trained for retrieval-augmented generation and tool calling.
  Scope: Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0)
  Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1

### Conditional

- **Multilingual assistant tasks (German, French, Italian, Portuguese, Hindi, Spanish, Thai)** — Vendor documentation lists additional supported languages but the inspected primary NVIDIA-hosted sources do not provide per-language benchmark protocols or per-language evaluation rows for this exact checkpoint; downstream per-language validation is required before production deployment.
  Scope: Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0)
  Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1

### Avoid

- **Life-critical clinical deployment without expert review** — Vendor safety metadata and NIM documentation state implementer responsibility for guardrails and do not provide clinical validation, PHI handling guidance, or clinical-grade performance claims for the checkpoint in the inspected primary sources.
  Scope: Llama-3.1-Nemotron-Nano-8B-v1 (model version 1.0)
  Evidence: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/llama-nemotron.html, https://docs.nvidia.com/nim/llama-3-1-nemotron-safety-guard-multilingual-8b-v1/latest/prompt-template.html

## Input preparation

### Semantic inputs

- Model consumes text inputs including assistant/instruction-style prompts, chat messages, and code. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
- Vendor documentation reports support for a large context length (131,072 position embeddings / 128K tokens) for this checkpoint. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/config.json, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard

### Accepted formats

- Accepted input modality: plain-text prompt payloads (instruction/chat style); the NGC container entry documents OpenAI-compatible API exposure for NVIDIA AI Enterprise deployment. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-v1, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard

### Preprocessing

- A tokenizer configuration file (tokenizer.json) is provided in the NVIDIA-hosted checkpoint repository. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/tokenizer.json, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/029ff12ba0525730bb8b94dab56d5f14e34d67d9/tokenizer.json
- The inspected primary NVIDIA-hosted sources do not enumerate exact normalization rules, ordered tokenization steps, or step-by-step preprocessing beyond the presence of tokenizer configuration files for this checkpoint. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/tokenizer.json, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard

### Pre-submit validation

- Vendor documentation and systemcard state the checkpoint can be deployed locally and report GPU memory guidance (systemcard) but do not specify canonical input-validation behaviors (truncation rules, invalid-character handling) for this exact checkout in the inspected sources. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/systemcard, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard

### Task-specific formatting

- No canonical prompt templates, paired-input ordering conventions, or explicit task-formatting instructions for this exact checkpoint are published in the inspected NVIDIA-hosted model card or vendor model repository; example pipeline snippets exist in the repository README but a single canonical prompt template is not published in the inspected primary sources. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/README.md, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard

## Output interpretation

### Outputs

- Official outputs are natural-language text-generation responses for instruction-following, chat, and code tasks. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1

### Interpretation

- Interpret model outputs as generated text for instruction-following, chat, and code tasks; the inspected primary NVIDIA-hosted sources do not provide post-hoc calibration guidance or numeric confidence semantics for responses. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/llama-nemotron.html

### Post-inference validation

- Vendor NIM documentation and model safety notes recommend implementers apply guardrails and trustworthy-AI diligence; the inspected primary sources do not include automated post-inference calibration checks or recommended numeric thresholds. Sources: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/llama-nemotron.html, https://docs.nvidia.com/nim/llama-3-1-nemotron-safety-guard-multilingual-8b-v1/latest/prompt-template.html, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### meta-llama-3-1-8b-instruct — `insufficient-evidence`

- Task: instruction-following / reasoning
- Criteria: No primary-source, matched-protocol head-to-head benchmark for the exact NVIDIA Nemotron Nano 8B v1 checkpoint versus the upstream Llama-3.1-8B-Instruct was found in the inspected primary NVIDIA-hosted sources.
- Rationale: Vendor documentation states derivation from Llama-3.1-8B-Instruct, but no matched-protocol evaluation rows comparing this exact NVIDIA checkpoint to the upstream checkpoint are present in the inspected primary sources.
- Comparison conditions: not reported in inspected primary sources
- Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1

## Limitations and safety

### Limitations

- Vendor-reported training and post-training timeline: training/post-training reported between August 2024 and March 2025; pretraining data cutoff reported as 2023 (inherited from upstream). Sources: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
- Public, dataset-level benchmark protocol details (dataset splits, prompt templates, temperature/decoding/seed settings, evaluation scripts) for numeric scores attributed to this exact checkpoint were not found in the inspected NVIDIA-hosted model card, systemcard, repository blobs, or NGC/NIM documentation. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
- License and upstream-artifact linkage: vendor documentation references the NVIDIA Open Model License and the upstream Llama 3.1 Community License Agreement; an exact upstream-hosted LICENSE blob for the upstream model was not present among the inspected NVIDIA-hosted repository blobs in the findings and is therefore an evidence gap for canonical upstream license-text linkage. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard
- Operational/serving abstraction: NVIDIA provides an NIM container and NGC catalog entries for deployment; the NIM/container is an operational wrapper and runtime evidence (backends, throughput) is distinct from upstream model-weight quality claims. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-v1, https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/systemcard

### Safety

- Vendor safety metadata and NIM documentation state implementers are responsible for applying guardrails and trustworthy-AI diligence prior to deployment; inspected NVIDIA-hosted sources note outputs may contain undesirable content and recommend implementer-side mitigations. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/llama-nemotron.html, https://docs.nvidia.com/nim/llama-3-1-nemotron-safety-guard-multilingual-8b-v1/latest/prompt-template.html
- NVIDIA publishes Nemoguard content-safety model variants and NIM containers for safety-oriented deployments and documents prompt-template-driven safety-guard behavior; vendor guidance emphasizes developer responsibility to ensure safety and compliance. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemoguard-8b-content-safety

## Related upstream agent skills

### `related-model-workflow`

NVIDIA's Nemotron customization skill is first-party guidance for curating, training, evaluating, converting, and optimizing Nemotron-family checkpoints in the Nemotron repository. It is not an inference payload or Nebius deployment contract; verify the exact listed checkpoint and use the Forge/Serverless instructions for serving.
- [nemotron-customize](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-customize)

## Primary sources

### NVIDIA modelcard - llama-3_1-nemotron-nano-8b-v1 modelcard

- URL: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party vendor model card containing checkpoint identity, intended uses, context-window, training timeline, and license metadata for the named checkpoint.
- Scope: Llama-3.1-Nemotron-Nano-8B-v1 (version 1.0)
- Supports: model name and version
- Supports: derivation from Meta Llama-3.1-8B-Instruct
- Supports: post-training intents (reasoning, chat, code, RAG, tool calling)
- Supports: context window 131072 position embeddings (128K tokens)
- Supports: training/post-training timeline (Aug 2024 - Mar 2025)
- Supports: pretraining data cutoff (2023, inherited from upstream)
- Supports: release date (2025-03-18)
- Supports: statement that the model fits on a single RTX GPU
- Supports: license metadata reference

### Hugging Face model page - NVIDIA Llama-3.1-Nemotron-Nano-8B-v1

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
- Publisher: NVIDIA (Hugging Face repository)
- Type: `model-card`
- Primary because: First-party repository page published by NVIDIA hosting the checkpoint artifacts, README examples, and safety/license metadata.
- Scope: Llama-3.1-Nemotron-Nano-8B-v1 (version 1.0)
- Supports: repository hosting for checkpoint artifacts
- Supports: intended uses and safety metadata
- Supports: release date and version
- Supports: notes about post-training intents (reasoning, chat, RAG, tool calling)

### tokenizer.json (checkpoint repository, main)

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/tokenizer.json
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: First-party tokenizer configuration file provided in the checkpoint repository.
- Scope: tokenizer for Llama-3.1-Nemotron-Nano-8B-v1
- Supports: presence of tokenizer.json for the checkpoint

### tokenizer.json (checkpoint repository, specific blob)

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/029ff12ba0525730bb8b94dab56d5f14e34d67d9/tokenizer.json
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Specific tokenizer.json blob referenced in the inspected findings confirming tokenizer configuration availability.
- Scope: tokenizer blob for Llama-3.1-Nemotron-Nano-8B-v1
- Supports: tokenizer configuration file presence

### config.json (checkpoint repository)

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/config.json
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Configuration file hosted in the NVIDIA checkpoint repository specifying architecture, hidden size, attention heads, and maximum position embeddings.
- Scope: configuration for Llama-3.1-Nemotron-Nano-8B-v1
- Supports: architecture type (llama / LlamaForCausalLM)
- Supports: network hyperparameters (hidden size, heads, layers)
- Supports: maximum position embeddings (131072 -> 128K token support)
- Supports: torch dtype (bfloat16)

### NVIDIA model systemcard for llama-3.1-nemotron-nano-8b-v1

- URL: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/systemcard
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party systemcard providing hardware guidance, precision/memory recommendations, and deployment notes for the named checkpoint/NIM.
- Scope: Llama-3.1-Nemotron-Nano-8B-v1 (system/deployment guidance)
- Supports: GPU memory guidance for bf16 and fp8 precisions
- Supports: support for LoRA customization and fine-tuning
- Supports: support for TensorRT-LLM local engine building
- Supports: deployment and hardware guidance

### NVIDIA NeMo microservices documentation - Llama Nemotron customizer

- URL: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/llama-nemotron.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Vendor documentation describing model parameters (8B reported) and microservice/customizer integration notes.
- Scope: Llama-3.1-Nemotron-Nano-8B-v1 (microservices/customizer)
- Supports: reported parameter count (8 billion)
- Supports: integration/customizer documentation
- Supports: LoRA and full SFT training/deployment notes

### NGC Catalog: NIM container entry for llama-3.1-nemotron-nano-8b-v1

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-v1
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: First-party NGC catalog entry describing the NIM/container availability and OpenAI-compatible API exposure for NVIDIA AI Enterprise deployment.
- Scope: NIM/container for Llama-3.1-Nemotron-Nano-8B-v1
- Supports: availability as an NVIDIA NIM container
- Supports: OpenAI-compatible API exposure via NVIDIA AI Enterprise
- Supports: operational/deployment notes

### NIM reference documentation for nvidia-llama-3_1-nemotron-nano-8b-v1

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-8b-v1
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Programmatic NIM reference documenting the named NIM/microservice and release metadata.
- Scope: NIM API reference for Llama-3.1-Nemotron-Nano-8B-v1
- Supports: release date and model identity
- Supports: post-training process description (supervised fine-tuning and reinforcement stages) reported by vendor

### NIM safety-guard prompt template documentation (Nemotron safety-guard multilingual 8B v1)

- URL: https://docs.nvidia.com/nim/llama-3-1-nemotron-safety-guard-multilingual-8b-v1/latest/prompt-template.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Vendor documentation describing safety-guard prompt-template-driven behavior for a Nemotron safety-guard NIM variant referenced in the dossier.
- Scope: Nemotron safety-guard NIM (multilingual 8B v1)
- Supports: safety-guard behavior
- Supports: existence of structured prompt templates for the safety-guard NIM

### NVIDIA modelcard - llama-3_1-nemoguard-8b-content-safety modelcard

- URL: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Vendor-hosted modelcard for the Nemoguard content-safety variant used as supporting safety evidence.
- Scope: Nemoguard content-safety model
- Supports: safety model descriptions and developer guidance

### NGC Catalog entry for Nemoguard content-safety container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemoguard-8b-content-safety
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: First-party NGC catalog entry documenting availability of the Nemoguard content-safety container.
- Scope: Nemoguard content-safety NIM/container
- Supports: safety model deployment guidance and container availability

### NVIDIA root landing for the exact Forge starting source (Build entry)

- URL: https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-8b-v1
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-llama-3-1-nemotron-nano-8b-v1
- Supports: Forge-to-upstream exact-version identity and starting source

### Hugging Face model page - NVIDIA Llama-3.1-Nemotron-Nano-8B-v1 — cited revision/file

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/README.md
- Publisher: NVIDIA (Hugging Face repository)
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: Llama-3.1-Nemotron-Nano-8B-v1 (version 1.0)
- Supports: Exact audited claim citation

## Evidence gaps

- No primary-source numeric benchmark table/row for this exact checkpoint was found at the vendor model card. Checked URL and locator: https://build.nvidia.com/nvidia/llama-3_1-nemotron-nano-8b-v1/modelcard (inspected modelcard content; no dataset-level benchmark tables/rows for this exact checkpoint were present).
- No primary-source numeric benchmark table/row for this exact checkpoint was found at the vendor Hugging Face repository README or repository blobs. Checked URL and locator: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1 (inspected README and repository files; no dataset-level benchmark tables/rows for this exact checkpoint were present).
- Evidence gap: canonical upstream-hosted LICENSE blob for the upstream Llama 3.1 Community License Agreement was not present among the inspected NVIDIA-hosted repository blobs in the findings and therefore the exact upstream LICENSE artifact locator is not provided by the inspected primary NVIDIA-hosted sources.
- Evidence gap: exact, vendor-published normalization rules and ordered tokenization/token-preprocessing algorithm steps (beyond the presence of tokenizer.json) for this checkpoint are not enumerated in the inspected NVIDIA-hosted primary sources (checked tokenizer.json blobs and repository files at https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/tokenizer.json).
- Evidence gap: canonical, single published prompt template or paired-input ordering convention for production use of this exact checkpoint was not found in the inspected NVIDIA-hosted model card or repository (checked modelcard and README at the two NVIDIA-hosted locations above).
- Evidence gap: exact output JSON shapes/field names and numeric confidence/probability output formats for standard NIM checkpoint responses are not specified in the inspected NVIDIA-hosted NIM reference or modelcard (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-8b-v1 and the modelcard).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 26 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://developer.nvidia.com/blog/build-enterprise-ai-agents-with-advanced-open-nvidia-llama-nemotron-reasoning-models Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20].primary must be true: $.sources[20].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[22].primary must be true: $.sources[22].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24].primary must be true: $.sources[24].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25].primary must be true: $.sources[25].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[26].primary must be true: $.sources[26].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[27].primary must be true: $.sources[27].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[28].primary must be true: $.sources[28].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[29].primary must be true: $.sources[29].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1/blob/main/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
