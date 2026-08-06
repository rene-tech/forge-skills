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

- Research key: `huggingface-co-nvidia-cosmos-ea-cosmos3-nano-d55efb7b36`
- Independent audit: `revised`
- Researched: `2026-08-06T13:22:39.185253+00:00`

Using only the supplied research findings (Hugging Face Cosmos3-Nano model page and asset blobs, and the NVIDIA NIM model card present in the findings), I verified Nano identity (nvidia/Cosmos3-Nano), MoT architecture claim, tokenizer.json artifact presence, generation defaults (generation_config.json), and SAFETY.md statements. The supplied findings do not include immutable model-weight filenames/hashes, tokenizer merges/vocab/class-version metadata beyond tokenizer.json, per-checkpoint numeric benchmark cells for Nano, explicit tensor-shape/runtime resolution/aspect-ratio contracts, or reproducible evaluation scripts for Nano-specific numeric results. Where the supplied findings are silent, I record explicit evidence gaps and cite the exact URLs inspected.

## Identity

- Upstream name: nvidia/Cosmos3-Nano
- Checkpoint/version: Cosmos3-Nano
- Immutable revision: not reported
- Parameter scale: Nano: 16 B total parameters (dense 8 B transformer)
- Architecture/head: Mixture-of-Transformers (MoT) — Transformer family with separate reasoning and generation towers per the model card and transformer config
- License: Model materials / checkpoints: OpenMDW-1.1 (as stated in the Hugging Face model card facts in the provided findings)
- Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/transformer/config.json

## Selection

### Recommended

- **Physical‑AI world modeling and multimodal generation for research and synthetic-data creation (text->image, text->video, image->video)** — The Hugging Face Cosmos3-Nano model card and the NIM model card describe Cosmos3-Nano as an omnimodal world model intended for Physical AI applications and synthetic-data generation; the model page lists supported modalities and intended application domains.
  Scope: nvidia/Cosmos3-Nano
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://build.nvidia.com/nvidia/cosmos3-nano/modelcard
- **Research and experimentation with policy/action SFT variants (policy-tuned Nano research variants)** — The Hugging Face model card facts reference policy variants (e.g., Cosmos3-Nano-Policy-DROID) and the model assets include example prompts and tokenizer/config artifacts that support research workflows for action/policy modeling.
  Scope: nvidia/Cosmos3-Nano (and policy-tuned Nano variants referenced on Hugging Face)
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md

### Conditional

- **Production deployment in safety‑critical physical systems after extensive domain validation and guardrails** — Requires domain-specific validation, human‑in‑the‑loop safeguards, and additional testing because SAFETY.md explicitly disclaims certification for life‑critical use and the supplied findings do not publish calibrated per-sample confidence outputs or turnkey certification artifacts.
  Scope: nvidia/Cosmos3-Nano
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md, https://huggingface.co/nvidia/Cosmos3-Nano
- **Edge or real-time deployment only after verifying an explicitly edge-targeted variant or performing runtime adaptation** — The supplied findings describe Nano as a named variant in the family but do not publish an explicit edge-targeted runtime artifact or configuration for Nano in the inspected URLs; verify edge-targeted artifacts before claiming identical behavior for edge deployments.
  Scope: Cosmos3 family / Cosmos3-Nano (family-level evidence only in supplied findings)
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano

### Avoid

- **Turnkey clinical or medical decision‑making without independent clinical validation** — The SAFETY.md states the model is not safety‑certified for life‑critical use and requires system‑level validation and safeguards; no clinical validation artifacts or approvals are present in the supplied findings.
  Scope: nvidia/Cosmos3-Nano
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md
- **Assuming per‑sample calibrated confidence outputs are provided by the checkpoint for automated safety decisions** — The supplied findings (model card and blobs) do not document calibrated per-sample confidence outputs or a calibration protocol for generated modalities.
  Scope: nvidia/Cosmos3-Nano
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/generation_config.json
- **High‑resolution, long‑horizon video generation assumed to be physically accurate without downstream verification** — The Hugging Face model facts in the supplied findings state outputs should not be treated as physically accurate simulation or safety‑certified decision making and advise additional validation for robotics/control applications.
  Scope: nvidia/Cosmos3-Nano
  Evidence: https://huggingface.co/nvidia/Cosmos3-Nano

## Input preparation

### Semantic inputs

- Accepted input modalities described in the supplied findings include text, image, video, and action trajectories (multimodal heterogeneous inputs for world modeling). Sources: https://huggingface.co/nvidia/Cosmos3-Nano
- Modalities are combined via structured JSON input files within framework examples referenced on the model page (e.g., modality routing via numeric fields such as num_frames to select image vs video). Sources: https://huggingface.co/nvidia/Cosmos3-Nano

### Accepted formats

- The NIM model card (as present in the supplied findings) states the generator API returns MP4 videos encoded as base64 for generator outputs and accepts text prompts and optional image conditioning. Sources: https://build.nvidia.com/nvidia/cosmos3-nano/modelcard
- The supplied Hugging Face model page and repository blobs provide examples and JSON-style modality routing but do not enumerate a single exhaustive byte-level container specification beyond example usage. Sources: https://huggingface.co/nvidia/Cosmos3-Nano, https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/transformer/config.json

### Preprocessing

- Generation defaults relevant to inference (do_sample, top_k, top_p, temperature, repetition_penalty, bos/eos/pad token IDs) are recorded in generation_config.json in the supplied findings and can serve as default sampling parameters. Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/generation_config.json
- A tokenizer.json artifact is published for Cosmos3-Nano on Hugging Face (tokenizer.json blob present in the supplied findings). Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/tokenizer.json
- The supplied findings do not publish separate merges/vocab files or an explicit tokenizer class name/version beyond tokenizer.json (evidence gap for full tokenizer configuration). Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/tokenizer.json, https://huggingface.co/nvidia/Cosmos3-Nano

### Pre-submit validation

- The SAFETY.md describes dataset filtering, automated and manual review pipelines, and application-level safeguards, but the supplied findings do not present a centralized, explicit input-validation ruleset (forbidden tokens, PHI filters, exact filter lists) for runtime input acceptance — evidence gap. Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md, https://huggingface.co/nvidia/Cosmos3-Nano

### Task-specific formatting

- The supplied Hugging Face model page contains example prompts (e.g., a task planning example) and references JSON-style modality routing; no single canonical cross-modal prompt template is published in the supplied findings. Sources: https://huggingface.co/nvidia/Cosmos3-Nano

## Output interpretation

### Outputs

- Documented output modalities in the supplied findings include text, image, video, audio (sound), and action sequences (policy outputs). Sources: https://huggingface.co/nvidia/Cosmos3-Nano
- The supplied NIM model card states the preview/generator API returns MP4 videos encoded as base64 strings (output encoding documented in the provided NIM model card URL). Sources: https://build.nvidia.com/nvidia/cosmos3-nano/modelcard
- The supplied findings do not publish explicit output tensor shapes, channel ordering, or standardized per-output numeric confidence fields for the Nano checkpoint (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Nano, https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/transformer/config.json

### Interpretation

- Treat generated multimodal outputs as synthetic world-model outputs requiring downstream domain validation and physical/temporal sanity checks; the model page cautions about treating outputs as physically accurate or safety‑certified. Sources: https://huggingface.co/nvidia/Cosmos3-Nano
- Runtime preview guardrails and SynthID watermarking are described on the NIM model card in the supplied findings as runtime-serving protections rather than model-weight artifacts. Sources: https://build.nvidia.com/nvidia/cosmos3-nano/modelcard

### Post-inference validation

- Post-inference validation should include physical-law checks, semantic-alignment checks, geometric-consistency checks, and visual-integrity checks; the supplied findings describe verification concepts at a high level but do not provide a turnkey validation suite (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Nano, https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md
- For policy/action outputs, repository-level examples referenced on the model page indicate simulator-in-the-loop verification and trajectory continuity checks are recommended, but a centralized, explicit simulator-validation spec is not published in the supplied findings (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Nano

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### nvidia/Cosmos3-Super — `tradeoff`

- Task: Multimodal world modeling and generation (family-level tier tradeoff)
- Criteria: Family-level tier descriptions (Nano vs Super) and deployment targets inferred from the model page facts; no protocol-matched numeric benchmark cells for Nano vs Super are available in the supplied findings.
- Rationale: The supplied Hugging Face facts list family variants (Nano and Super) indicating different tiers; the supplied findings do not include protocol-matched numeric benchmark values for Nano vs Super to make numeric comparisons.
- Comparison conditions: Family-level description only; no per-checkpoint numeric tables located in the supplied findings to support head-to-head numeric comparison.
- Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://build.nvidia.com/nvidia/cosmos3-nano/modelcard

### insufficient-evidence — `insufficient-evidence`

- Task: Direct protocol-matched benchmark comparisons between Cosmos3-Nano and other candidate checkpoints
- Criteria: Protocol-matched numeric comparisons require both sides to publish numeric values on the same dataset/split/metric/protocol; supplied findings do not provide such comparable numeric results for Nano versus alternatives.
- Rationale: The supplied findings do not publish per-checkpoint numeric benchmark cells or reproducible evaluation scripts for Nano; therefore direct numeric comparisons are unsupported.
- Comparison conditions: No Nano-scoped numeric benchmark cells or reproducible evaluation artifacts present in the supplied URLs.
- Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://build.nvidia.com/nvidia/cosmos3-nano/modelcard

## Limitations and safety

### Limitations

- Generation instability and failure modes (temporal inconsistency, unstable camera motion, imprecise physical interactions, action-state drift) are noted as limitations for use in long-horizon or high-resolution scenarios in the supplied findings. Sources: https://huggingface.co/nvidia/Cosmos3-Nano
- Evidence gap: exact per-checkpoint numeric benchmark values, dataset splits, seeds, and reproducible evaluation scripts for Cosmos3-Nano are not published in the supplied findings. Sources: https://huggingface.co/nvidia/Cosmos3-Nano, https://build.nvidia.com/nvidia/cosmos3-nano/modelcard
- Evidence gap: tokenizer configuration details beyond tokenizer.json (merges/vocab separate files, explicit tokenizer class/version) are not present in the supplied findings. Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/tokenizer.json, https://huggingface.co/nvidia/Cosmos3-Nano
- Evidence gap: exact immutable model-weight filenames or artifact hashes for Cosmos3-Nano are not published in the supplied findings. Sources: https://huggingface.co/nvidia/Cosmos3-Nano
- Evidence gap: a single, unambiguous mapping between model-weights license and any distinct code license for all deployment artifacts is not present in the supplied findings. Sources: https://huggingface.co/nvidia/Cosmos3-Nano

### Safety

- The SAFETY.md for the Nano model variant states the model is not safety‑certified for life‑critical use and must not be used as the sole basis for life‑critical decisions; human review and safeguards are required. Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md
- The SAFETY.md documents training-data acquisition safeguards including CSAM hash-matching, NCII classifier-based moderation, automated and manual filtering pipelines, and human review; full provenance manifests for training data are not published in the supplied findings (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md
- The NIM model card in the supplied findings documents runtime preview guardrails and output watermarking (SynthID) applied by the hosted endpoint; these are runtime-serving protections rather than intrinsic model-weight properties in the supplied findings. Sources: https://build.nvidia.com/nvidia/cosmos3-nano/modelcard

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: nvidia/Cosmos3-Nano

- URL: https://huggingface.co/nvidia/Cosmos3-Nano
- Publisher: Hugging Face (model card by NVIDIA)
- Type: `model-card`
- Primary because: Canonical Hugging Face model hosting and README entries for the upstream Cosmos3-Nano checkpoint are included in the supplied findings and underpin identity, modalities, and high-level limitations.
- Scope: nvidia/Cosmos3-Nano
- Supports: upstreamName
- Supports: checkpoint
- Supports: intended uses
- Supports: input/output modalities
- Supports: generation limitations
- Supports: tokenizer artifact presence (tokenizer.json)

### Hugging Face generation_config.json for Cosmos3-Nano

- URL: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/generation_config.json
- Publisher: Hugging Face (model assets by NVIDIA)
- Type: `model-card`
- Primary because: Provides canonical sampling and generation defaults recorded for the Cosmos3-Nano model in the supplied findings.
- Scope: nvidia/Cosmos3-Nano
- Supports: sampling defaults (do_sample, top_k, top_p, temperature, repetition_penalty)
- Supports: token id defaults (bos/eos/pad ids)

### Hugging Face SAFETY.md for Cosmos3-Nano

- URL: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/SAFETY.md
- Publisher: Hugging Face (model assets by NVIDIA)
- Type: `model-card`
- Primary because: Contains canonical safety statements, data‑acquisition safeguards, and usage disclaimers included in the supplied findings.
- Scope: nvidia/Cosmos3-Nano (policy and safety guidance)
- Supports: safety statements
- Supports: training data safeguards
- Supports: disclaimer about non-certified use in life-critical systems

### Hugging Face tokenizer blob for Cosmos3-Nano (tokenizer.json)

- URL: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/tokenizer.json
- Publisher: Hugging Face (model assets by NVIDIA)
- Type: `model-card`
- Primary because: Direct tokenizer artifact hosted alongside the Cosmos3-Nano model as present in the supplied findings.
- Scope: nvidia/Cosmos3-Nano (tokenizer artifact)
- Supports: tokenizer artifact presence

### Hugging Face transformer config for Cosmos3-Nano (transformer/config.json)

- URL: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/transformer/config.json
- Publisher: Hugging Face (model assets by NVIDIA)
- Type: `model-card`
- Primary because: Transformer configuration blob present in the supplied findings describing model instance targets and pretrained_weights references.
- Scope: nvidia/Cosmos3-Nano (transformer config)
- Supports: architecture details referenced in the config
- Supports: pretrained_weights/backbone_path references

### NIM/NVIDIA model card: cosmos3-nano (modelcard)

- URL: https://build.nvidia.com/nvidia/cosmos3-nano/modelcard
- Publisher: build.nvidia.com (NVIDIA NIM model card as included in the supplied findings)
- Type: `official-documentation`
- Primary because: NIM model card in the supplied findings documents API output encoding (MP4 base64) and notes on runtime preview guardrails.
- Scope: nvidia/cosmos3-nano (NIM preview/runtime statements)
- Supports: API output encoding (MP4 base64)
- Supports: runtime preview guardrails and watermarking statements

### Exact official starting source declared by Forge

- URL: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-cosmos3-omni
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Per-checkpoint numeric benchmark values for Cosmos3-Nano (per-dataset, per-split, per-metric cells) are not present in the supplied findings. Checked: https://huggingface.co/nvidia/Cosmos3-Nano (model card and asset blobs) and https://build.nvidia.com/nvidia/cosmos3-nano/modelcard — no Nano-scoped numeric benchmark table cells or reproducible evaluation scripts were present in these URLs in the supplied findings.
- Evidence gap: Exact immutable model-weight filenames and artifact hashes for nvidia/Cosmos3-Nano are not published in the supplied findings. Checked: https://huggingface.co/nvidia/Cosmos3-Nano and associated asset blobs listed in the supplied findings (tokenizer.json, generation_config.json, transformer/config.json) — no immutable weight filename or cryptographic hash was found.
- Evidence gap: Tokenizer configuration details beyond tokenizer.json (separate merges/vocab files, explicit tokenizer class name/version) are not published in the supplied findings. Checked: https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/tokenizer.json and https://huggingface.co/nvidia/Cosmos3-Nano (model page) — no merges/vocab/class-version metadata found in the supplied findings.
- Evidence gap: Explicit input/output tensor shapes, channel ordering, and formal runtime resolution/aspect-ratio contracts for the Nano checkpoint are not present in the supplied findings. Checked: https://huggingface.co/nvidia/Cosmos3-Nano and https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/transformer/config.json — no explicit tensor-shape or resolution/aspect-ratio contract documented in the supplied findings.
- Evidence gap: Calibrated per-sample confidence outputs and a documented calibration protocol for generated modalities are not present in the supplied findings. Checked: https://huggingface.co/nvidia/Cosmos3-Nano and https://huggingface.co/nvidia/Cosmos3-Nano/blob/main/generation_config.json — no calibration semantics or per-sample confidence fields documented in the supplied findings.
- Evidence gap: Reproducibility artifacts for reported benchmarks (evaluation scripts, exact dataset splits, seeds, run commands) for Cosmos3-Nano are not present in the supplied findings. Checked: https://huggingface.co/nvidia/Cosmos3-Nano and https://build.nvidia.com/nvidia/cosmos3-nano/modelcard — no reproducible evaluation scripts or exact split/seed disclosures found in the supplied findings.
- Evidence gap: A canonical primary URL for https://github.com/nvidia-cosmos/cosmos-transfer2.5 is not present in the supplied research findings, therefore any draft claims depending on that URL cannot be verified from the supplied findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 14 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses forbidden secondary URL https: $.sources[3] uses forbidden secondary URL https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'vllm-project' for this exact model scope: $.sources[10] uses unapproved repository owner 'vllm-project' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses forbidden secondary URL https: $.sources[14] uses forbidden secondary URL https://wavespeed.ai/blog/posts/what-is-nvidia-cosmos3-nano Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].value must contain a reported numeric result: $.benchmarks[0].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].value must contain a reported numeric result: $.benchmarks[1].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
