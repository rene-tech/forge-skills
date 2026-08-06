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

- Research key: `github-com-hidream-ai-hidream-i1-e16c7971da`
- Independent audit: `revised`
- Researched: `2026-07-23T22:46:09.546749+00:00`

HiDream-I1 is a text-to-image generative foundation model family implemented as a sparse Diffusion Transformer (DiT) with a dynamic Mixture-of-Experts (MoE) stage. The family includes Full, Dev (distilled), and Fast (distilled) variants. Primary-source materials inspected (repository README and inference.py, Hugging Face model cards for Full/Dev/Fast, and the arXiv technical report HTML) report a family-level parameter scale of 17 billion parameters and document the DiT+MoE architecture and training disclosures. The HiDream-I1 repository exposes variant-specific inference defaults (Full: 50 steps, Dev: 28 steps, Fast: 16 steps) and enumerates supported output resolutions and runtime hyperparameters (scheduler, guidance_scale, num_inference_steps, shift). The repository LICENSE file declares an MIT license for repository artifacts. Several checkpoint-scoped, reproducibility, and provenance artifacts required for a strict checkpoint dossier were not found in the inspected primary sources: an immutable HiDream-I1-Fast checkpoint identifier (commit/tag/sha256 artifact) is not published at the inspected locations; per-checkpoint numeric breakdowns and reproducible benchmark protocols for GenEval/DPG/HPS per-checkpoint are not present in inspected locations; tokenizer implementation files and consolidated encoder-license provenance are not published in a single manifest; and reproducible latency/peak-VRAM benchmarks per variant are not published in the inspected primary sources. These missing items are recorded in evidenceGaps.

## Identity

- Upstream name: HiDream-I1
- Checkpoint/version: HiDream-I1-Fast
- Immutable revision: not reported
- Parameter scale: 17 billion parameters
- Architecture/head: Sparse Diffusion Transformer (DiT) with Mixture-of-Experts (MoE)
- License: MIT (repository LICENSE)
- Evidence: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md, https://github.com/HiDream-ai/HiDream-I1/blob/main/LICENSE, https://arxiv.org/html/2505.22705v1, https://huggingface.co/HiDream-ai/HiDream-I1-Fast, https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main/transformer/config.json, https://huggingface.co/HiDream-ai/HiDream-I1-Full, https://huggingface.co/HiDream-ai/HiDream-I1-Dev, https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main, https://github.com/HiDream-ai/HiDream-I1/commits/main

## Selection

### Recommended

- **Text-to-image generation (general-purpose image synthesis from text prompts).** — Primary repository and model-card materials present HiDream-I1 as a text-to-image generative foundation model family and expose an inference entrypoint and Fast variant intended for lower-step generation.
  Scope: HiDream-I1-Fast
  Evidence: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md, https://huggingface.co/HiDream-ai/HiDream-I1-Fast

### Conditional

- **High-fidelity, higher-step image generation where increased sampling steps and recommended runtime optimizations are acceptable.** — Select the Full variant and use the documented default num_inference_steps (Full: 50) and recommended runtime optimizations (as noted in repository README and model card). Verify downstream fidelity with task-specific validation; do not assume numerical benchmark parity across variants without per-checkpoint breakdowns.
  Scope: HiDream-I1-Full
  Evidence: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md, https://huggingface.co/HiDream-ai/HiDream-I1-Full
- **Lower-latency image generation (interactive previews) accepting quality trade-offs.** — Use HiDream-I1-Fast with its documented default of 16 inference steps; accept that per-variant latency/VRAM trade-offs are not published in the inspected primary sources and must be measured by the operator for target hardware.
  Scope: HiDream-I1-Fast
  Evidence: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Fast

### Avoid

- **Clinical diagnostic, medical decision-making, or other clinical-ready deployments.** — Primary sources (repository README, Hugging Face model card, and technical report) do not provide clinical validation, PHI-handling guidance, or statements clearing the model for clinical or diagnostic use.
  Scope: All HiDream-I1 checkpoints (Full, Dev, Fast)
  Evidence: https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md, https://huggingface.co/HiDream-ai/HiDream-I1-Full, https://arxiv.org/html/2505.22705v1

## Input preparation

### Semantic inputs

- Natural-language text prompts are the supported semantic input modality for generation. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md
- Model variants reference external text encoders as constituent encoder dependencies for prompt processing (variant model cards reference encoder names). Sources: https://huggingface.co/HiDream-ai/HiDream-I1-Fast, https://huggingface.co/HiDream-ai/HiDream-I1-Dev, https://huggingface.co/HiDream-ai/HiDream-I1-Full

### Accepted formats

- Supported generation output resolutions are enumerated in inference.py (repository inference configuration lists supported target resolutions). Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py

### Preprocessing

- Inference configuration exposes scheduler, guidance_scale, num_inference_steps, and shift parameters per variant; these runtime hyperparameters control sampling behavior. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py
- Fast-variant model-card references constituent encoder choices (encoder model names listed on the Fast model card). Sources: https://huggingface.co/HiDream-ai/HiDream-I1-Fast

### Pre-submit validation

- No explicit input-validation rules (e.g., character limits, tokenizer truncation lengths, or exact batching semantics) are documented in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Fast, https://huggingface.co/HiDream-ai/HiDream-I1-Full

### Task-specific formatting

- Repository provides CLI invocation examples and variant selection via a model_type flag in inference.py; no formal prompt template or paired-input format is published in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md, https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py

## Output interpretation

### Outputs

- Model outputs are generated images at the supported resolutions enumerated in inference.py (e.g., 1024×1024 among supported targets). Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Full

### Interpretation

- Primary sources do not document any numeric per-sample probability, confidence score, or calibrated likelihood outputs accompanying generated images; treat outputs as synthetic images without model-provided confidence values. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Full

### Post-inference validation

- No formal post-inference calibration, quality, or sanity-check procedures are published in the inspected primary sources; users must apply application-specific checks or human evaluation. Sources: https://huggingface.co/HiDream-ai/HiDream-I1-Full, https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md

## Public benchmarks

### HPS v2.1 alignment (family-level claim)

- Dataset/split: HPS v2.1 / not reported
- Metric/value: HPS v2.1 averaged score / 33.82 (`context-only`)
- Model scope: HiDream-I1 (family-level claim reported in repository/README)
- Conditions: README presents an averaged HPS v2.1 score but does not publish a per-checkpoint numeric breakdown, dataset splits, or a reproducible evaluation protocol at the inspected locations.
- Source: https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md
- Locator: README.md (HPS v2.1 averaged score claim)
- Caveat: Primary repository README reports an averaged family-level HPS v2.1 score but does not include per-checkpoint tables, dataset split identifiers, or evaluation scripts at the inspected locations; therefore the per-checkpoint attribution and reproducibility protocol are not verifiable from inspected sources.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Exact immutable checkpoint identifier for HiDream-I1-Fast (commit hash, model artifact sha256, or immutable release tag) is not published in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main, https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main/transformer/config.json
- Full reproducible evaluation protocols and dataset/split identifiers for reported GenEval and DPG scores are not provided in the inspected primary sources. Sources: https://huggingface.co/HiDream-ai/HiDream-I1-Full, https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md
- Tokenizer implementation details (exact tokenizer class/file, token truncation length, prompt-to-tensor serialization) are not published in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Fast
- API/CLI response schema or explicit output serialization format (HTTP/JSON schema, tensor shapes beyond resolution) are not documented in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Full
- Per-variant reproducible latency and peak VRAM measurements (e.g., ms/sample at 1024×1024 and hardware specification) are not provided in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1, https://huggingface.co/HiDream-ai/HiDream-I1-Fast
- Consolidated encoder-license provenance for encoders automatically downloaded by inference.py (exact license texts, location, or required access steps for each encoder) is not published as a single manifest in the inspected primary sources. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Fast, https://huggingface.co/HiDream-ai/HiDream-I1-Dev
- Evidence gap: Parameter-scale reporting ambiguity: primary inspected sources report 17B parameters but conflicting secondary reporting exists outside the inspected primary sources; primary sources inspected do not include an authoritative per-checkpoint artifact manifest to disambiguate conflicting external reports.

### Safety

- The model is not documented or validated for clinical or diagnostic use; primary sources do not provide PHI-handling guidance, clinical validation, or clearance for medical deployments. Sources: https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md, https://huggingface.co/HiDream-ai/HiDream-I1-Full, https://arxiv.org/html/2505.22705v1

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### HiDream-I1 repository (root)

- URL: https://github.com/HiDream-ai/HiDream-I1
- Publisher: HiDream-ai (GitHub)
- Type: `official-documentation`
- Primary because: Official repository root (canonical starting source) for the project, linking code, README, and artifacts referenced throughout the dossier.
- Scope: HiDream-I1 family (Full/Dev/Fast)
- Supports: overall family identity and starting canonical source for repository artifacts

### HiDream-I1 README (repository)

- URL: https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md
- Publisher: HiDream-ai (GitHub)
- Type: `repository`
- Primary because: Repository README presenting family-level parameter claim, HPS v2.1 averaged score, example usage, and runtime recommendations; used to support family-level identity and benchmark claim.
- Scope: HiDream-I1 README (family-level claims, HPS v2.1 averaged score, runtime recommendations)
- Supports: model family identity
- Supports: 17B parameter claim (family-level)
- Supports: HPS v2.1 averaged score claim
- Supports: runtime recommendations (CUDA/Flash Attention)

### HiDream-I1 inference configuration (inference.py)

- URL: https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py
- Publisher: HiDream-ai (GitHub)
- Type: `repository`
- Primary because: Official inference script exposing variant-specific defaults, hyperparameters (scheduler, guidance_scale, num_inference_steps, shift), and enumerated supported output resolutions.
- Scope: HiDream-I1 inference configuration (inference.py)
- Supports: variant inference-step counts and schedulers
- Supports: supported resolutions
- Supports: variant-specific guidance_scale and shift parameters
- Supports: CLI invocation examples

### HiDream-I1 LICENSE file (MIT)

- URL: https://github.com/HiDream-ai/HiDream-I1/blob/main/LICENSE
- Publisher: HiDream-ai (GitHub)
- Type: `repository`
- Primary because: LICENSE file in the official repository declaring the MIT license for repository artifacts.
- Scope: Repository license file (MIT)
- Supports: MIT license statement for repository artifacts

### HiDream-I1 repository commits (commits view)

- URL: https://github.com/HiDream-ai/HiDream-I1/commits/main
- Publisher: HiDream-ai (GitHub)
- Type: `repository`
- Primary because: Repository commit history used to inspect changes to README and code and to check for published releases or tags.
- Scope: Repository commits history
- Supports: commit SHAs for README and code updates
- Supports: evidence of repository maintenance and updates

### HiDream-I1 technical report (arXiv HTML)

- URL: https://arxiv.org/html/2505.22705v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical technical report describing the architecture (Sparse DiT with MoE), training methods, and family-level disclosures used to support architecture and training claims.
- Scope: HiDream-I1 technical report (arXiv HTML)
- Supports: Sparse DiT architecture with MoE
- Supports: training methods and family-level parameter claim as reported in the technical report

### HiDream-I1-Full model card (Hugging Face)

- URL: https://huggingface.co/HiDream-ai/HiDream-I1-Full
- Publisher: HiDream-ai (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face Full model card page used to verify Full-variant model-card claims, usage notes, and benchmark/reporting statements at the model-card level.
- Scope: HiDream-I1-Full model card
- Supports: Full variant model-card benchmark/reporting statements and usage notes
- Supports: Gradio demo and usage examples referenced on the model card

### HiDream-I1-Dev model card (Hugging Face)

- URL: https://huggingface.co/HiDream-ai/HiDream-I1-Dev
- Publisher: HiDream-ai (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face Dev model card used to verify Dev-variant model-card claims and encoders/VAE provenance remarks.
- Scope: HiDream-I1-Dev model card
- Supports: Dev variant encoder mentions and VAE provenance remarks

### HiDream-I1-Fast model card (Hugging Face)

- URL: https://huggingface.co/HiDream-ai/HiDream-I1-Fast
- Publisher: HiDream-ai (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face Fast model page used to verify Fast-variant model-card claims, encoder references, and usage notes; used for checkpoint-scoped input-preparation claims.
- Scope: HiDream-I1-Fast model card
- Supports: Fast variant encoder mentions
- Supports: variant-specific notes about encoders and VAE provenance
- Supports: usage instructions and inference invocation notes

### HiDream-I1-Fast transformer config (commits view / config.json)

- URL: https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main/transformer/config.json
- Publisher: HiDream-ai (Hugging Face)
- Type: `model-card`
- Primary because: Fast checkpoint transformer configuration file and its commit history used to extract config fields and inspect for commit SHAs referenced in the dossier.
- Scope: HiDream-I1-Fast transformer config (commit/blame view)
- Supports: Fast checkpoint config fields and commit-level inspection

### HiDream-I1-Fast commits (commit history)

- URL: https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main
- Publisher: HiDream-ai (Hugging Face)
- Type: `model-card`
- Primary because: Commit history for the Fast variant demonstrating updates to checkpoint configuration and allowing inspection for potential immutable identifiers; inspected to check for published immutable artifact identifiers.
- Scope: HiDream-I1-Fast commits history (Hugging Face)
- Supports: commit-level updates to Fast checkpoint files
- Supports: evidence that no immutable checkpoint artifact identifier was found at the inspected commit history

## Evidence gaps

- Evidence gap: Exact immutable checkpoint identifier for HiDream-I1-Fast (commit hash, model artifact SHA256, or release/tag) not found in inspected sources: inspected https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py, https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main, and https://huggingface.co/HiDream-ai/HiDream-I1-Fast/commits/main/transformer/config.json and found no published immutable artifact identifier for HiDream-I1-Fast.
- Evidence gap: GenEval numeric values and reproducible protocol (overall score and per-category dataset splits and evaluation scripts) are not present in the inspected primary sources: inspected https://huggingface.co/HiDream-ai/HiDream-I1-Full and https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md and found no GenEval tables or evaluation scripts in those locations.
- Evidence gap: DPG numeric value and reproducible protocol not found in the inspected primary sources: inspected https://huggingface.co/HiDream-ai/HiDream-I1-Full and https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md and found no DPG numeric table or evaluation script in those locations.
- Evidence gap: Exact numeric HPS v2.1 per-checkpoint breakdown and reproducible protocol: although an averaged HPS v2.1 score (33.82) is reported in the repository README, no per-checkpoint numeric table or evaluation script was found in inspected primary sources: inspected https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md and https://huggingface.co/HiDream-ai/HiDream-I1-Full and found no reproducible protocol or per-checkpoint HPS table.
- Evidence gap: Tokenization implementation details (exact tokenizer class/file path, token truncation length, tokenization parameters, prompt-to-tensor serialization) are not published in the inspected primary sources: inspected https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py and https://huggingface.co/HiDream-ai/HiDream-I1-Fast and found encoder names referenced but no tokenizer implementation files or parameter declarations.
- Evidence gap: API/CLI response schema and explicit output serialization format (HTTP/JSON schema, exact tensor shapes beyond reported resolutions) are not published in the inspected primary sources: inspected https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py and https://huggingface.co/HiDream-ai/HiDream-I1-Full and found no response-schema documentation.
- Evidence gap: Per-variant reproducible latency and peak VRAM measurements (e.g., ms/sample at 1024×1024 on specified hardware) are not published in the inspected primary sources: inspected https://github.com/HiDream-ai/HiDream-I1 and https://huggingface.co/HiDream-ai/HiDream-I1-Fast and found no official latency/VRAM benchmark tables.
- Evidence gap: Consolidated encoder-license provenance for all encoders automatically downloaded by inference.py is not published as a single manifest in the inspected primary sources: inspected https://github.com/HiDream-ai/HiDream-I1/blob/main/inference.py and https://huggingface.co/HiDream-ai/HiDream-I1-Fast and https://huggingface.co/HiDream-ai/HiDream-I1-Dev and found references to encoders but no consolidated license texts or manifest.
- Evidence gap: Direct, primary-source task- and protocol-matched benchmark comparisons between HiDream-I1 checkpoints and candidate external peers are not present in the inspected primary sources: inspected https://github.com/HiDream-ai/HiDream-I1/blob/main/README.md and https://huggingface.co/HiDream-ai/HiDream-I1-Full and found no identical-protocol comparison tables linking HiDream-I1 checkpoints to external peers.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 26 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24].primary must be true: $.sources[24].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25].primary must be true: $.sources[25].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[26].primary must be true: $.sources[26].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[27].primary must be true: $.sources[27].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[28].primary must be true: $.sources[28].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[29].primary must be true: $.sources[29].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[30].primary must be true: $.sources[30].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[31].primary must be true: $.sources[31].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/vladmandic/sdnext/wiki/HiDream Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/vladmandic/sdnext/wiki/HiDream Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].value must contain a reported numeric result: $.benchmarks[3].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.conditionalUseCases_note: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCases_note_evidenceUrls: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCases_metadata: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCases_placeholder: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCases_unused: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCases_unused2: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
