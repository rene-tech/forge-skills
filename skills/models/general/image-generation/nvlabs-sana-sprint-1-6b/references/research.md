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

- Research key: `github-com-nvlabs-sana-c4c236c402`
- Independent audit: `revised`
- Researched: `2026-07-23T23:31:58.508605+00:00`

Primary NVlabs repository files (README and asset/docs), the NVlabs-hosted project documentation (nvlabs.github.io Sana docs), and NVlabs repository release notes together document a Sana‑Sprint 1.6B checkpoint intended for 1024×1024 text-to-image generation and show Diffusers conversion/packaging examples recommending bf16. NVlabs repository performance tables report operating-point numeric summaries (examples: a 2-step operating row with FID=6.50 in asset/docs/sana_sprint.md and a repository root reported FID=5.92 at 1024×1024), but the inspected NVlabs primary materials do not supply canonical checkpoint-scoped evaluation metadata such as explicit dataset split identifiers, RNG seeds, or a single-line canonical scheduler/default-parameter table; therefore numeric values should be treated as summary operating points reported by NVlabs rather than protocol-matched reproducible benchmark rows in the absence of further upstream protocol detail. NVlabs model_zoo documents a ControlNet entry marked "Coming soon" and the repository LICENSE file states Apache-2.0 for repository code; issue discussion flags a license discrepancy noted on an external hub page (see sources) that NVlabs materials do not resolve.

## Identity

- Upstream name: Efficient-Large-Model/Sana_Sprint_1.6B_1024px_diffusers
- Checkpoint/version: Efficient-Large-Model/Sana_Sprint_1.6B_1024px/checkpoints/Sana_Sprint_1.6B_1024px.pth
- Immutable revision: not reported
- Parameter scale: 1.6B
- Architecture/head: SANA‑Sprint text-to-image diffusion family; repository conversion examples and docs reference Diffusers pipeline packaging for SanaSprint pipeline artifacts (SanaSprintPipeline / SanaSprintImg2ImgPipeline); checkpoint conversion examples reference config files under configs/sana_sprint_config.
- License: Apache-2.0 (repository LICENSE)
- Evidence: https://github.com/NVlabs/Sana, https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md, https://nvlabs.github.io/Sana/docs/model_zoo, https://github.com/NVlabs/Sana/releases, https://github.com/NVlabs/Sana/blob/main/LICENSE, https://github.com/NVlabs/Sana/blob/main/docs/ComfyUI/SANA-Sprint.json, https://github.com/NVlabs/Sana/issues/332

## Selection

### Recommended

- **High-throughput text-to-image generation at 1024×1024 using the NVlabs-provided 1.6B Sana‑Sprint checkpoint packaged for Diffusers.** — NVlabs model_zoo and asset/docs present a Sana‑Sprint 1.6B 1024px checkpoint and NVlabs conversion/examples show conversion to a Diffusers pipeline with dtype bf16 and usage examples for 1024×1024 variants; repository performance tables report throughput/latency operating points for 1024×1024 Sana variants.
  Scope: Sana_Sprint_1.6B_1024px (NVlabs conversion examples and model_zoo entries)
  Evidence: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md, https://nvlabs.github.io/Sana/docs/model_zoo
- **Image-to-image (img2img) workflows using the SanaSprint img2img Diffusers packaging as provided in NVlabs conversion examples and docs.** — NVlabs repository includes a ComfyUI/packaging JSON and model_zoo/conversion examples referencing img2img-capable variants and Diffusers packaging; repository and docs show example configs and precision variants used for image-conditioning workflows.
  Scope: Sana_Sprint_1.6B_1024px with img2img support (as shown in NVlabs ComfyUI JSON and model_zoo conversion examples)
  Evidence: https://github.com/NVlabs/Sana/blob/main/docs/ComfyUI/SANA-Sprint.json, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md

### Conditional

- **Low-latency interactive or near-real-time text-to-image generation when reproducing NVlabs-reported low-step operating points and runtime environment.** — Only applicable when callers reproduce the exact runtime/hardware and inference step-count operating point cited by NVlabs performance tables (for example the 2-step operating row reported in asset/docs/sana_sprint.md) and follow NVlabs conversion/load examples (recommended dtype bf16). Without reproducing those hardware/runtime and dtype conditions, the upstream latency/throughput claims are not reproducible from the checkpoint alone.
  Scope: Sana_Sprint_1.6B_1024px (use conditioned on reproducing NVlabs hardware/protocol and dtype)
  Evidence: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md, https://github.com/NVlabs/Sana/releases
- **ControlNet-conditioned generation (only if/when NVlabs publishes a 1.6B ControlNet artifact upstream).** — Applicable only when NVlabs publishes a ControlNet artifact at the documented model_zoo path; current NVlabs model_zoo entry marks a ControlNet artifact as "Coming soon" indicating no published 1.6B ControlNet artifact at the inspected path.
  Scope: Sana_Sprint_1.6B_1024px and ControlNet variants (only if/when NVlabs publishes upstream ControlNet artifacts)
  Evidence: https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md, https://nvlabs.github.io/Sana/docs/model_zoo

### Avoid

- **Treating NVlabs-reported numeric benchmarks (FID/CLIP/GenEval) as protocol-matched equivalents to other models without verifying dataset split identifiers, RNG/seed, and full preprocessing/evaluation protocol.** — NVlabs repository performance tables include numeric operating-point summaries (for example a 2-step row with FID=6.50 in asset/docs/sana_sprint.md and a repository-root reported FID=5.92 for 1024×1024), but the inspected NVlabs primary materials do not publish canonical checkpoint-scoped dataset split identifiers or RNG/seed policy required for matched-protocol numeric comparison. Treat numeric rows as upstream-reported summaries unless full protocol metadata is published upstream.
  Scope: Sana_Sprint_1.6B_1024px (checkpoint-scoped numeric claims)
  Evidence: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana
- **Clinical or PHI-bearing production deployment assuming upstream clinical validation or PHI-handling guidance.** — Inspected NVlabs repository and docs do not publish checkpoint-scoped clinical validation, PHI handling procedures, or domain-specific safety approvals for this checkpoint; do not assume the checkpoint is validated for clinical use without separate domain-specific evaluation and approvals.
  Scope: Sana_Sprint_1.6B_1024px
  Evidence: https://github.com/NVlabs/Sana, https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md

## Input preparation

### Semantic inputs

- Primary input modality is text prompts (single or batched strings) tokenized and consumed by the pipeline as shown in NVlabs conversion and usage examples. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md
- Image-conditioning (img2img) inputs are supported as shown by NVlabs ComfyUI packaging examples and model_zoo usage references. Sources: https://github.com/NVlabs/Sana/blob/main/docs/ComfyUI/SANA-Sprint.json, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md

### Accepted formats

- NVlabs provides Diffusers conversion and loading examples referencing an original .pth checkpoint and showing from-pretrained / conversion patterns that target Diffusers pipeline artifacts. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md
- NVlabs conversion examples reference an orig_ckpt_path string (a .pth checkpoint locator) and show conversion invocation patterns recommending dtype bf16 for converted artifacts. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md

### Preprocessing

- NVlabs example config files and conversion examples reference specific config YAML files for the 1.6B 1024px variant (for example configs/sana_sprint_config/1024ms/SanaSprint_1600M_1024px_allqknorm_bf16_scm_ladd.yaml) to be used during conversion and pipeline instantiation. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md
- NVlabs model_zoo and conversion examples document recommended precision usage (bf16) for the 1.6B 1024px Sana‑Sprint variants and show how variant/dtype arguments should be set when loading Diffusers-packaged checkpoints. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md, https://nvlabs.github.io/Sana/docs/model_zoo

### Pre-submit validation

- Evidence gap: The inspected primary NVlabs files do not publish a canonical checkpoint-scoped numeric max_sequence_length for the text encoder.
- Evidence gap: The inspected primary NVlabs files do not publish a single-line canonical default parameter table (scheduler class + default step count + default guidance_scale/CFG + RNG seed/seed-policy) for the packaged SanaSprintPipeline; examples show num_inference_steps usage but no canonical unified default table.

### Task-specific formatting

- NVlabs provides canonical conversion and loading examples that reference an --orig_ckpt_path string and a dtype argument for conversion to Diffusers artifacts; example config filenames and example num_inference_steps values appear in usage examples. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md

## Output interpretation

### Outputs

- Evidence gap: NVlabs primary materials inspected do not publish an explicit per-output shape/serialization contract beyond showing examples and referring to pipeline usage; implementers should follow Diffusers pipeline API conventions when consuming generated images.

### Interpretation

- NVlabs numerical evaluation summaries reported in repository tables and docs are upstream-reported operating-point summaries; because NVlabs materials inspected do not publish explicit dataset split names or RNG/seed policy for the reported rows, treat numeric values as summary operating points rather than protocol-matched, directly comparable benchmark values. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana
- Latency and throughput tradeoffs reported upstream refer to different inference step counts in repository summaries; verify the reported step-count in the cited NVlabs table/row before comparing across sources. Sources: https://github.com/NVlabs/Sana, https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md

### Post-inference validation

- Evidence gap: No upstream-documented per-sample confidence, per-image calibration scores, or attached NSFW/safety scores for generated outputs were located in the inspected NVlabs primary files and docs.

## Public benchmarks

### image-generation (text-to-image)

- Dataset/split: not reported / not reported
- Metric/value: FID / 6.50 (`lower-is-better`)
- Model scope: Sana_Sprint_1.6B_1024px (NVlabs performance table entry)
- Conditions: 2 inference steps at 1024×1024 as listed in the NVlabs asset/docs performance table row; RNG/seed and exact dataset split identifier not specified in the inspected table row.
- Source: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md
- Locator: asset/docs/sana_sprint.md performance table (row: Sana‑Sprint‑1.6B, 2 inference steps) — no numbered table/figure identifier provided in source
- Caveat: The source does not specify dataset split identifiers or RNG/seed policy for the reported row; treat as an upstream summary operating point.

### image-generation (text-to-image)

- Dataset/split: not reported / not reported
- Metric/value: FID / 5.92 (`lower-is-better`)
- Model scope: Sana_Sprint_1.6B_1024px (repository-root reported performance entry)
- Conditions: Repository-root performance summary for Sana‑1.6B at 1024×1024 includes throughput and latency numbers alongside FID; RNG/seed and dataset split identifiers are not provided in the inspected repository root materials.
- Source: https://github.com/NVlabs/Sana
- Locator: GitHub repository root performance table / summary (row: Sana‑1.6B, 1024×1024) — no numbered table/figure identifier provided in source
- Caveat: The repository summary does not include explicit dataset split identifiers or RNG/seed policy; values differ from other reported operating points in repository materials.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: image-generation (text-to-image)
- Criteria: Protocol parity (explicit dataset split, RNG seed, preprocessing, and exact step-count conditions) required for matched numeric comparisons is not available in the inspected NVlabs primary materials for the Sana 1.6B checkpoint.
- Rationale: NVlabs repository and docs report multiple numeric operating points but do not publish canonical checkpoint-scoped protocol metadata required to ensure comparability; therefore direct numeric comparisons to alternatives cannot be verified from the inspected upstream sources.
- Comparison conditions: Checked NVlabs repository root, asset/docs/sana_sprint.md, and nvlabs.github.io model_zoo; missing checkpoint-scoped protocol elements prevent a verified numeric comparison.
- Evidence: https://github.com/NVlabs/Sana, https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://nvlabs.github.io/Sana/docs/model_zoo

## Limitations and safety

### Limitations

- Upstream numeric metrics (FID, CLIP, GenEval, throughput, latency) are reported by NVlabs in repository tables and docs, but inspected NVlabs materials do not consistently publish dataset split identifiers, RNG/seed policy, or the complete evaluation protocol necessary for matched-protocol reproducibility; this limits external reproduction and prevents protocol-matched numeric comparisons. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana, https://nvlabs.github.io/Sana/docs/model_zoo
- ControlNet variant availability for the 1.6B checkpoint is not published at the NVlabs model_zoo path inspected; model_zoo marks a ControlNet entry as "Coming soon", indicating no published 1.6B ControlNet artifact at that location. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md, https://nvlabs.github.io/Sana/docs/model_zoo
- There is a license statement discrepancy reported between NVlabs repository LICENSE (Apache-2.0) and an external hub presentation discussed in repository issue threads; NVlabs materials do not resolve the contradiction in the inspected sources. Sources: https://github.com/NVlabs/Sana/blob/main/LICENSE, https://github.com/NVlabs/Sana/issues/332
- Reproducing the pipeline and matching reported performance may require following NVlabs conversion and runtime examples (conversion scripts, recommended dtype bf16, example configs); NVlabs does not publish a single-line canonical default parameter table for scheduler/default guidance/seed policy in the inspected sources. Sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md, https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md

### Safety

- The NVlabs/Sana repository LICENSE file states the repository code license as Apache License, Version 2.0; this governs the repository code as published upstream. Sources: https://github.com/NVlabs/Sana/blob/main/LICENSE
- Evidence gap: No upstream-attached per-sample safety scoring (for example NSFW or per-output confidence scores) or per-sample calibration metadata for generated images was found in the inspected NVlabs primary files and docs.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVlabs Sana repository (root) — canonical project URL

- URL: https://github.com/NVlabs/Sana
- Publisher: NVlabs / Sana repository
- Type: `repository`
- Primary because: Repository root provides project-level summaries, performance rows, and links used as first-party primary evidence.
- Scope: SANA project (repository root)
- Supports: Project-level claims, repository performance summary rows (Sana‑1.6B 1024×1024 metrics), release notes pointers, and links to asset/docs

### NVlabs Sana usage and performance examples (asset/docs/sana_sprint.md)

- URL: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md
- Publisher: NVlabs / Sana repository
- Type: `repository`
- Primary because: Repository usage examples and an explicit performance table row providing checkpoint-scoped numeric entries and conversion examples.
- Scope: Sana_Sprint_1.6B_1024px (usage examples and performance table)
- Supports: Conversion invocation examples (orig_ckpt_path string, example config path, dtype bf16) and a performance table row reporting a 2-step operating point with FID=6.50

### NVlabs Sana model_zoo (asset/docs/model_zoo.md)

- URL: https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md
- Publisher: NVlabs / Sana repository
- Type: `repository`
- Primary because: Official repository model_zoo listing providing checkpoint identifiers, precision notes, and ControlNet status entries.
- Scope: Sana_Sprint and family-level model_zoo entries
- Supports: Lists Sana‑Sprint‑1.6B 1024px with Diffusers path and precision bf16, and marks ControlNet artifact as Coming soon

### NVlabs Sana project docs — model_zoo (documentation site)

- URL: https://nvlabs.github.io/Sana/docs/model_zoo
- Publisher: NVlabs
- Type: `official-documentation`
- Primary because: NVlabs-hosted documentation summarizing model_zoo entries and precision guidance.
- Scope: Sana model_zoo documentation site
- Supports: Lists Sana‑Sprint‑1.6B 1024px entries and precision recommendations; supports model_zoo/ControlNet status references

### NVlabs Sana releases (GitHub releases page)

- URL: https://github.com/NVlabs/Sana/releases
- Publisher: NVlabs / Sana repository
- Type: `repository`
- Primary because: Official project releases page documenting release history and conversion/diffusers support additions.
- Scope: SANA project (release history)
- Supports: Release notes mentioning diffusers conversion script updates and added guidance features

### NVlabs Sana repository LICENSE

- URL: https://github.com/NVlabs/Sana/blob/main/LICENSE
- Publisher: NVlabs / Sana repository
- Type: `official-documentation`
- Primary because: Repository-hosted LICENSE file asserting the repository code license.
- Scope: SANA project (repository license)
- Supports: States the repository code license as Apache License, Version 2.0

### NVlabs Sana ComfyUI packaging JSON for SANA‑Sprint

- URL: https://github.com/NVlabs/Sana/blob/main/docs/ComfyUI/SANA-Sprint.json
- Publisher: NVlabs / Sana repository
- Type: `repository`
- Primary because: Repository-hosted ComfyUI packaging example used to verify packaging/config references for img2img and model identifiers.
- Scope: SanaSprint ComfyUI packaging (example JSON)
- Supports: ComfyUI JSON shows model identifier and precision tags used in packaging examples

### NVlabs repository issue discussing hub license presentation

- URL: https://github.com/NVlabs/Sana/issues/332
- Publisher: NVlabs / Sana repository
- Type: `repository`
- Primary because: Repository issue thread records and documents a license discrepancy discussion referencing external hub presentation.
- Scope: Repository issue thread (license discrepancy)
- Supports: Discussion noting a discrepancy between repository LICENSE (Apache-2.0) and an external hub license presentation for the checkpoint

## Evidence gaps

- Evidence gap: Checkpoint-scoped published dataset split names, random seeds, and the full end-to-end evaluation protocol (preprocessing pipeline, exact split identifiers, RNG/seed policy) for NVlabs-reported numeric metrics are not specified in the inspected NVlabs primary materials (checked sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md ; https://github.com/NVlabs/Sana ; https://nvlabs.github.io/Sana/docs/model_zoo).
- Evidence gap: Canonical cryptographic hashes or published safetensor filenames for Diffusers-converted artifacts and a canonical orig_ckpt_path integrity checksum are not provided in the inspected NVlabs primary sources (checked sources: https://github.com/NVlabs/Sana/blob/main/asset/docs/sana_sprint.md ; https://github.com/NVlabs/Sana/blob/main/asset/docs/model_zoo.md).
- Evidence gap: The inspected NVlabs primary files do not publish a single-line canonical default parameter table (canonical scheduler class + default step count + default guidance_scale/CFG + RNG seed/seed-policy) for the Diffusers-packaged SanaSprintPipeline; implementers must follow examples and set parameters explicitly.
- Evidence gap: Exact numeric max_sequence_length for the checkpoint's text encoder is not published in the inspected NVlabs primary files.
- Evidence gap: Published ControlNet checkpoint artifacts for Sana‑Sprint 1.6B are not present at the NVlabs model_zoo path inspected; the model_zoo entry marks the ControlNet artifact as "Coming soon".
- Evidence gap: Per-sample safety/NSFW scores or per-output confidence/calibration metadata for generated images are not provided in the inspected NVlabs primary files.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 7 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://github.com/NVlabs/Sana Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0].primary must be true: $.sources[0].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary host medium.com: $.sources[4] uses forbidden secondary host medium.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarksEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.limitationsEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
