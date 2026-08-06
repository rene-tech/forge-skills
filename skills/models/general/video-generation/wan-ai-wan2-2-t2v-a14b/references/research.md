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

- Research key: `github-com-wan-video-wan2-2-4460f5dc2a`
- Independent audit: `revised`
- Researched: `2026-07-23T23:15:28.960276+00:00`

Primary upstream evidence is the Wan2.2 GitHub repository and selected files: the repository root, README.md, LICENSE.txt, the animate preprocessing UserGuider.md, and the preprocess tree and example commit. The repository documents Wan2.2 as a major upgrade to Wan video models and provides animate preprocessing guidance (animation and replacement modes) and concrete preprocessing scripts and example invocations. The repository LICENSE.txt states the repository code license (Apache-2.0). The available primary files inspected do not provide checkpoint-scoped model-weight license text, explicit a14b-diffusers per-checkpoint config blobs or model_index.json entries, tokenizer files or tokenizer-length semantics for a14b-diffusers, or an explicit per-checkpoint benchmark table for a14b-diffusers in the inspected files. The dossier therefore records checkpoint-scoped evidence gaps where the primary repository files checked do not supply the requested per-checkpoint artifacts or numeric runtime/benchmark figures.

## Identity

- Upstream name: Wan2.2 (Wan-Video/Wan2.2 GitHub repository)
- Checkpoint/version: a14b-diffusers
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: Code: Apache-2.0 (per repository LICENSE.txt). Model-weights license: not reported
- Evidence: https://github.com/Wan-Video/Wan2.2, https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt

## Selection

### Recommended

- **Prepare inputs for Wan2.2 animate workflows using the repository's animate preprocessing scripts and guidance (animation and replacement modes).** — The repository provides an animate preprocessing user guide documenting generation modes, required files, parameters, and example invocations, and ships preprocessing scripts and an example tree showing flags and sample paths.
  Scope: Wan2.2 repository animate preprocessing artifacts (wan/modules/animate/preprocess) and example tree/commit.
  Evidence: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2

### Conditional

- **Run the repository-provided preprocessing pipeline with the example flags/paths shown in the repository example tree, using the repository's recommended models for detection/pose/masking as listed in the UserGuider.** — Follow the exact example invocation, directory layout, and required auxiliary model files named in the UserGuider and preprocess directory. Confirm any additional per-checkpoint runtime or memory requirements from authoritative per-checkpoint artifacts before high-resolution or large-batch inference.
  Scope: Wan2.2 repository preprocessing example invocation and required auxiliary models.
  Evidence: https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md

### Avoid

- **Assuming the repository code license (Apache-2.0) also licenses checkpoint model weights or using model weights without confirming an explicit model-weights license.** — Evidence gap: the research did not find an explicit model-weights license statement for a14b-diffusers in the inspected primary repository files; repository LICENSE.txt documents the code license but does not itself establish a separate model-weights license for a named checkpoint.
  Scope: Repository-level files (Wan2.2 root and LICENSE.txt) and inspected repository documentation.
  Evidence: https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt, https://github.com/Wan-Video/Wan2.2, https://github.com/Wan-Video/Wan2.2/blob/main/README.md
- **Deploying a14b-diffusers at scale or assuming specific single-GPU VRAM requirements without checkpoint-scoped verification.** — Evidence gap: the inspected primary repository files provide preprocessing examples and model metadata but do not include authoritative per-checkpoint numeric VRAM or runtime requirements for a14b-diffusers.
  Scope: Wan2.2 repository documentation and example trees.
  Evidence: https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2

## Input preparation

### Semantic inputs

- Text prompts or prompt files are used as inputs to Wan2.2 workflows and preprocessing modules expect reference and driving media files for animate workflows (video and character image). Sources: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2

### Accepted formats

- Repository preprocessing examples reference standard media files (e.g., driving video and character image) as inputs to animation preprocessing; exact container/codec/format constraints are not specified in the inspected files. Sources: https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2, https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md

### Preprocessing

- The repository includes preprocessing scripts and documents an animation preprocessing invocation with flags such as --ckpt_path, --video_path, --refer_path, --save_path, --resolution_area, --retarget_flag, and --use_flux; these scripts and example invocations form the authoritative preprocessing instructions present in the upstream repository. Sources: https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2
- Preprocessing requires specific auxiliary models (pose detector, optional mask extraction and image editing models) and an expected directory structure for required models including names such as det/yolov10m.onnx, pose2d/vitpose_h_wholebody.onnx, sam2/sam2_hiera_large.pt, and FLUX.1-Kontext-dev as listed in the UserGuider. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess

### Pre-submit validation

- The preprocessing guidance requires presence of specific files and a directory structure matching the example invocation flags; missing or misnamed files and incorrect directory layout will break the preprocessing scripts. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md

### Task-specific formatting

- UserGuider.md documents two generation modes: 'animation' and 'replacement' and provides mode-specific preprocessing parameter guidance (retargeting recommendation for animation; mask/file outputs for replacement). Use the repository examples to construct required input directories and filenames. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess

## Output interpretation

### Outputs

- Preprocessing produces processed media files in the specified save_path (for example, files named src_face.mp4 and src_pose.mp4 for animation mode; src_bg.mp4 and src_mask.mp4 additionally for replacement mode); the repository does not provide an explicit per-checkpoint standardized output video shape or duration for a14b-diffusers in the inspected files. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2

### Interpretation

- Evidence gap: the inspected primary repository files do not define a mapping from internal model scores to human-interpretable perceptual-quality metrics or provide post-inference calibrated quality scores for generated videos; the repository provides preprocessing and generation-mode guidance but not post-inference perceptual-quality mappings for a14b-diffusers. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md

### Post-inference validation

- Evidence gap: the repository files inspected do not include post-inference perceptual-quality mapping, output calibration protocols, or standardized validation scripts for generated videos tied to a14b-diffusers. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Exact numeric VRAM and memory/runtime suitability comparisons between a14b-diffusers and other Wan2.2 variants
- Criteria: No authoritative per-checkpoint numeric VRAM or benchmark table for a14b-diffusers was found in the inspected primary repository files; repository-level documentation and preprocess examples exist but do not provide comparable numeric rows for the checkpoint.
- Rationale: The upstream repository files inspected include project README and preprocessing documentation but do not present per-checkpoint numeric VRAM claims or benchmark table rows for a14b-diffusers in the checked files.
- Comparison conditions: Repository-level documentation only; no verified per-checkpoint artifacts (model_index.json, per-checkpoint config blobs) for a14b-diffusers were identified in the inspected files.
- Evidence: https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md

## Limitations and safety

### Limitations

- Repository-level limitation: the upstream GitHub repository documents preprocessing workflows, project identity, and contains an Apache-2.0 LICENSE for repository code, but does not supply explicit checkpoint-scoped model-weight license text within the cited repository files (model-weights license not reported). Sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt
- Evidence gap: the inspected primary repository files do not provide an authoritative single‑GPU VRAM requirement (GB) or per-checkpoint runtime guidance for the a14b-diffusers checkpoint; numeric runtime/resource claims for a14b-diffusers were not found in the checked files. Sources: https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2

### Safety

- Evidence gap: the inspected primary repository files (README, LICENSE, UserGuider.md, preprocessing scripts) do not include explicit safety, privacy, or human-subject handling guidance tied specifically to the a14b-diffusers checkpoint. Sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Wan2.2 GitHub repository (root)

- URL: https://github.com/Wan-Video/Wan2.2
- Publisher: github.com
- Type: `repository`
- Primary because: Official upstream repository for Wan2.2; contains README and repository artifacts referenced by this dossier.
- Scope: wan-ai-wan2-2
- Supports: Project identity and repository-level artifacts

### Wan2.2 repository README.md (main)

- URL: https://github.com/Wan-Video/Wan2.2/blob/main/README.md
- Publisher: github.com
- Type: `official-documentation`
- Primary because: Main project README documenting project identity and listing innovations cited in the dossier.
- Scope: wan-ai-wan2-2
- Supports: Project announcement and high-level Wan2.2 claims

### Wan2.2 repository LICENSE.txt

- URL: https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt
- Publisher: github.com
- Type: `official-documentation`
- Primary because: Repository license file; authoritative for repository code license (Apache-2.0).
- Scope: wan-ai-wan2-2
- Supports: Repository code license (Apache-2.0)

### Wan2.2 UserGuider.md (animate preprocessing)

- URL: https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md
- Publisher: github.com
- Type: `official-documentation`
- Primary because: Primary repository documentation for animate preprocessing and generation modes; documents required files, parameters, and modes used by preprocessing.
- Scope: wan-ai-wan2-2
- Supports: Animate preprocessing requirements, generation modes ('animation' and 'replacement'), parameter names, and example file outputs

### Wan2.2 preprocess directory (tree listing)

- URL: https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess
- Publisher: github.com
- Type: `repository`
- Primary because: Contains preprocessing scripts (preprocess_data.py and related utilities) and demonstrates concrete preprocessing code shipped in the repository.
- Scope: wan-ai-wan2-2
- Supports: Preprocessing scripts and example invocation flags

### Wan2.2 repository example tree/commit (animation preprocessing example invocation)

- URL: https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2
- Publisher: github.com
- Type: `repository`
- Primary because: Repository tree snapshot showing an example animation preprocessing command and flags used in repository examples.
- Scope: wan-ai-wan2-2
- Supports: Concrete example invocation for preprocessing (flags and sample paths)

## Evidence gaps

- Per-checkpoint artifacts for a14b-diffusers (model_index.json, per-checkpoint config blobs such as config.json, unet/config, scheduler config): checked primary locations: https://github.com/Wan-Video/Wan2.2, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2 — the research did not find explicit per-checkpoint config blobs for a14b-diffusers in these inspected repository locations.
- Model-weights license for a14b-diffusers: checked primary location https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt and repository files listed in sources; the research did not find a separate explicit model-weights license statement for a14b-diffusers in the inspected repository files.
- Tokenizer files and tokenizer maximum input length or prompt/sequence-length semantics for a14b-diffusers: checked primary locations https://github.com/Wan-Video/Wan2.2, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2 — the research did not find tokenizer artifacts or documented tokenizer-length constraints for a14b-diffusers in these inspected files.
- Declared parameter counts specifically for the a14b-diffusers checkpoint: checked primary locations https://github.com/Wan-Video/Wan2.2 and https://github.com/Wan-Video/Wan2.2/blob/main/README.md — the research findings supply parameter numbers for other Wan2.2 variants but do not report a parameter-count statement explicitly tied to the a14b-diffusers checkpoint in the inspected repository files.
- Exact single-GPU VRAM requirement (GB) or per-checkpoint runtime/memory guidance for a14b-diffusers: checked primary locations https://github.com/Wan-Video/Wan2.2/blob/main/README.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess, https://github.com/Wan-Video/Wan2.2/tree/29d4a35d32273d5309a3a95250bd4e118d8789b2 — no authoritative per-checkpoint VRAM numeric figure for a14b-diffusers was found in these inspected files.
- Sampling defaults (default number of sampling steps, default sampler), seed/reproducibility conventions, and post-inference validation scripts for a14b-diffusers: checked primary locations https://github.com/Wan-Video/Wan2.2, https://github.com/Wan-Video/Wan2.2/blob/main/wan/modules/animate/preprocess/UserGuider.md, https://github.com/Wan-Video/Wan2.2/tree/main/wan/modules/animate/preprocess — no sampling-defaults, seed conventions, or post-inference perceptual-quality mapping scripts tied to the a14b-diffusers checkpoint were found in these inspected files.
- Wan-Bench or benchmark table/figure entries referencing a14b-diffusers: checked primary locations https://github.com/Wan-Video/Wan2.2/blob/main/README.md and the repository trees listed in sources; the research did not find an exact benchmark table/figure/row for a14b-diffusers in the inspected repository files.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 16 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://github.com/Wan-Video/Wan2.2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses forbidden secondary URL https: $.sources[14] uses forbidden secondary URL https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers/discussions/11 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary URL https: $.sources[15] uses forbidden secondary URL https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers/discussions/4 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md#license-agreement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md#license-agreement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/AbstractFramework/wan2.2-ti2v-5b-diffusers-8bit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md#license-agreement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers/discussions/4 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://willitrunai.com/video-models/wan-video-2-2-ti2v-5b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md#license-agreement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md#license-agreement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2/blob/main/README.md#license-agreement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
