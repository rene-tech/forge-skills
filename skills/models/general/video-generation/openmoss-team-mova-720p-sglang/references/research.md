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

- Research key: `huggingface-co-openmoss-team-mova-720p-4d8898cb1d`
- Independent audit: `revised`
- Researched: `2026-08-06T08:57:02.438845+00:00`

MOVA-720p (checkpoint MOVA-720p) is documented upstream as a foundation model for simultaneous video+audio synthesis supporting Text-to-Video-Audio (T2VA) and Image-to-Video-Audio (IT2VA) task modes. Canonical upstream artifacts (Hugging Face model card, README, GitHub repository, and the arXiv technical report) describe an asymmetric dual-tower architecture fused with bidirectional cross-attention and a Mixture-of-Experts design with a reported total of 32 billion parameters and ~18 billion active at inference. The Hugging Face commit metadata for the MOVA-720p checkpoint records checkpoint configuration fields (e.g., text_dim=4096, model dim and layer counts) and an immutable commit identifier. Upstream canonical sources do not provide several low-level operational details (explicit tokenizer name/files and tokenization protocol, exact input file-encoding MIME types, explicit prompt/JSON input schema, explicit dataset split filenames mapping to reported evaluation tables, or canonical container/codec/bitrate guidance). Where upstream artifacts disagree (the model card/README describe image-enabled IT2VA modes while a checkpoint commit metadata field indicates has_image_input=false) the dossier records that ambiguity and cites both artifacts.

## Identity

- Upstream name: MOVA
- Checkpoint/version: MOVA-720p
- Immutable revision: 169d1a94c53a197085b41deb788a4ff5166703c6
- Parameter scale: Mixture-of-Experts with 32 billion total parameters, 18 billion active during inference
- Architecture/head: Asymmetric dual-tower architecture fused via a bidirectional cross-attention mechanism; Mixture-of-Experts (MoE) design
- License: Apache License, Version 2.0
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6, https://github.com/OpenMOSS/MOVA, https://github.com/OpenMOSS/MOVA/blob/main/LICENSE, https://arxiv.org/abs/2602.08794

## Selection

### Recommended

- **Text-to-Video-Audio (T2VA) generation producing synchronized video and audio** — The Hugging Face model card and README describe MOVA as designed for T2VA and emphasize native bimodal generation (simultaneous video+audio synthesis) and synchronized outputs; the technical report frames MOVA as a foundation model for synchronized video-audio generation.
  Scope: MOVA-720p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://arxiv.org/abs/2602.08794
- **Image-to-Video-Audio (IT2VA) generation using a starting image plus text direction** — The model card and README list IT2VA as a supported task mode and document variant-specific examples and downloads; these upstream artifacts present IT2VA as an intended use for MOVA-720p.
  Scope: MOVA-720p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md
- **Lip-sync focused generation and evaluation (single- and multi-speaker scenarios)** — The README and the technical report present lip-sync evaluation as a primary benchmark axis for MOVA and describe evaluation protocols and metrics for lip-sync quality in the MOVA study.
  Scope: MOVA-720p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://arxiv.org/abs/2602.08794

### Conditional

- **Longer-duration or higher-resolution video generation beyond documented variant scope** — Evidence gap: Upstream canonical sources (Hugging Face model card, README, GitHub repo, arXiv technical report) do not specify a definitive maximum supported duration or an exact hard-coded maximum resolution for the MOVA-720p checkpoint. Users must validate longer durations or higher resolutions because the canonical artifacts do not state these bounds.
  Scope: MOVA-720p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794
- **LoRA-based fine-tuning of MOVA-720p for domain adaptation** — The README and model card document LoRA fine-tuning support; when applying LoRA adapters, downstream task performance (e.g., lip-sync metrics) must be validated using the provided evaluation code and benchmark because upstream artifacts do not enumerate exact fine-tuning protocols or expected metric changes.
  Scope: MOVA-720p (with LoRA)
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA

### Avoid

- **Assuming a different checkpoint or base-model variant is identical (e.g., substituting MOVA-360p or another variant for MOVA-720p without verification)** — Upstream documentation treats MOVA-360p and MOVA-720p as distinct variants with separate artifacts; checkpoint-scoped claims must be limited to the exact MOVA-720p checkpoint unless the other checkpoint's primary artifacts explicitly claim equivalence.
  Scope: MOVA-720p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md
- **Treating third-party wrappers, integrations, or community runtime tips as authoritative for upstream checkpoint internals or input/output contracts** — Third-party integration notes are not canonical upstream documentation; the canonical model card, README, repository, and technical report are the primary sources for checkpoint-scoped facts and should be used instead.
  Scope: MOVA-720p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA

## Input preparation

### Semantic inputs

- The model card and README state MOVA supports text and image inputs for its documented task modes (T2VA, IT2VA). Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md
- Ambiguity in upstream artifacts: the Hugging Face model card and README describe image-enabled IT2VA modes, while the MOVA-720p Hugging Face commit metadata records a checkpoint field "has_image_input": false. This is a conflict between checkpoint metadata and higher-level model-card/README statements. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md

### Accepted formats

- Upstream canonical artifacts (model card, README, repository, technical report) describe task modes and usage but do not enumerate exact image file encodings, MIME types, or explicit text input field encodings. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794

### Preprocessing

- Evidence gap: The canonical upstream artifacts do not provide tokenizer name/version, vocab/merges, or explicit text-normalization/tokenization protocol. The commit metadata records model config fields (e.g., text_dim=4096, model dim, num_layers) but not tokenizer files. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6, https://arxiv.org/abs/2602.08794
- Evidence gap: The canonical artifacts do not enumerate an ordered list of image/frame preprocessing transforms (explicit resize, mean/std normalization tensor values, or tokenization steps) required before inference. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794

### Pre-submit validation

- Evidence gap: Upstream sources do not publish an explicit input-validation checklist (bounds checking, exact allowed image dimensions, explicit truncation or padding rules) for MOVA-720p in the model card, README, repository, or technical report. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794

### Task-specific formatting

- The Hugging Face model card, README, and technical report describe supported task modes (T2VA, IT2VA, TI2VA) and high-level usage, but they do not provide a canonical prompt template, JSON HTTP input schema, or exact paired-input field ordering to serve as an API contract. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://arxiv.org/abs/2602.08794

## Output interpretation

### Outputs

- Upstream artifacts describe MOVA producing synchronized video frames and audio in a single inference pass; canonical outputs are therefore video (frame sequence) and audio (waveform) streams as evaluation targets. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794
- The checkpoint commit metadata includes model output-related configuration fields (e.g., out_dim), but the canonical sources do not provide an explicit runtime container/codec or bitrate guidance for produced outputs. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA

### Interpretation

- Evidence gap: The technical report and README reference synchronization metrics and evaluation protocols but the canonical artifacts do not define a standardized mapping from raw model outputs to consumer-level units (e.g., exact audio sampling/encoding, container codec) required for downstream measurement; users should treat reported evaluation metrics as computed under the paper's internal evaluation pipeline. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://arxiv.org/abs/2602.08794, https://github.com/OpenMOSS/MOVA

### Post-inference validation

- The README and repository release evaluation code and a MOVA Benchmark for Arena intended for reproducing reported metrics; users should run the provided evaluation code on MOVA-720p outputs to validate synchronization metrics. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794
- Evidence gap: Upstream artifacts do not specify canonical postprocessing container, codec, or bitrate requirements for video/audio output; the README and repo do not prescribe exact serving container parameters. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### Lightricks/LTX-2 (LTX-2 / LTX-2.3 family) — `insufficient-evidence`

- Task: Speech-content correctness (cpCER) and synchronization metrics
- Criteria: No primary-source, checkpoint-scoped numeric comparison evidence for LTX-2 versus MOVA-720p was found in the canonical MOVA artifacts available in the research findings; the canonical MOVA artifacts do not provide direct, fully-located competitor table rows that allow a protocol-equal comparison.
- Rationale: The canonical MOVA artifacts document MOVA design and evaluation but do not provide verifiable, checkpoint-scoped competitor rows for LTX-2 within the primary sources available in the research findings.
- Comparison conditions: Evidence gap: The MOVA paper and README (as available in the findings) do not include checkpoint-scoped competitor tables with exact dataset split locators that would permit strict protocol-matched comparison entries in this dossier.
- Evidence: https://arxiv.org/abs/2602.08794, https://huggingface.co/OpenMOSS-Team/MOVA-720p

### Ovi (unnamed baseline) — `insufficient-evidence`

- Task: Speech-content correctness (cpCER) and synchronization metrics
- Criteria: No primary-source, checkpoint-scoped numeric comparison evidence for Ovi versus MOVA-720p was found in the canonical MOVA artifacts available in the research findings.
- Rationale: The research findings do not contain verifiable competitor benchmark rows or exact locators that report Ovi numeric values under an identical protocol alongside MOVA-720p.
- Comparison conditions: Evidence gap: Missing explicit competitor table locators or cited dataset split mapping in the canonical sources.
- Evidence: https://arxiv.org/abs/2602.08794, https://huggingface.co/OpenMOSS-Team/MOVA-720p

### genmo-mochi-1-preview — `insufficient-evidence`

- Task: general video-generation quality and synchronized audio capability
- Criteria: No primary-source comparable benchmark evidence for genmo/mochi was located within the canonical MOVA artifacts available in the research findings.
- Rationale: The research findings do not include checkpoint-scoped primary-source benchmark comparisons between MOVA-720p and Genmo/Mochi.
- Comparison conditions: Evidence gap: lack of protocol-matched primary benchmark rows in canonical sources.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://arxiv.org/abs/2602.08794

### hunyuanvideo-community-hunyuanvideo-1-5 — `insufficient-evidence`

- Task: general video-generation quality and synchronized audio capability
- Criteria: No protocol-matched primary benchmark evidence for HunyuanVideo 1.5 versus MOVA-720p was found in the canonical MOVA artifacts provided in the research findings.
- Rationale: Canonical MOVA artifacts do not include primary-source rows for HunyuanVideo to enable direct comparison.
- Comparison conditions: Evidence gap: Missing or non-comparable primary benchmarks.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://arxiv.org/abs/2602.08794

## Limitations and safety

### Limitations

- Evidence gap: The canonical upstream artifacts (model card, README, repository, technical report) do not provide tokenizer name/version, vocab/merges, or an exact text-normalization/tokenization protocol, limiting exact reproducibility of text preprocessing. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794
- Evidence gap: The canonical artifacts do not enumerate exact dataset split filenames or the precise mapping from MOVA Benchmark for Arena samples to the paper's reported table rows; therefore direct reproduction of table-by-table reported metrics is constrained without additional upstream mapping artifacts. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://arxiv.org/abs/2602.08794, https://github.com/OpenMOSS/MOVA
- Evidence gap: The canonical sources do not provide explicit postprocessing/container/codec/bitrate guidance for produced video/audio outputs; integrations may document practical defaults but those integration artifacts are not canonical upstream sources. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA
- The repository and model card present MOVA-720p as a high-capacity model (MoE, large model dimensions recorded in the checkpoint metadata) and thus computationally non-trivial to run; exact runtime resource guidance (e.g., VRAM footprints under specific configs) is not specified in canonical upstream artifacts. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6, https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA
- The project is released under Apache License 2.0 as declared in the repository LICENSE file; users must comply with that license for model and code use. Sources: https://github.com/OpenMOSS/MOVA/blob/main/LICENSE, https://huggingface.co/OpenMOSS-Team/MOVA-720p

### Safety

- Evidence gap: No upstream guidance found on PHI handling, clinical-use prohibitions, or specialized data-retention/consent procedures in the canonical sources checked (model card, README, repository, technical report, LICENSE). Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794, https://github.com/OpenMOSS/MOVA/blob/main/LICENSE
- Users should treat MOVA outputs as automatically generated multimedia content and apply appropriate content-policy, copyright, and privacy reviews before publication or deployment; canonical upstream artifacts do not provide deployment-specific safety rules, so operational safety review and legal review are required prior to sensitive uses. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### OpenMOSS-Team/MOVA-720p (Hugging Face model card)

- URL: https://huggingface.co/OpenMOSS-Team/MOVA-720p
- Publisher: OpenMOSS-Team (Hugging Face model card)
- Type: `model-card`
- Primary because: Official Hugging Face model page for the MOVA-720p checkpoint; contains the model summary, variant statements, and links to README and repo.
- Scope: MOVA-720p
- Supports: intended design and supported tasks (T2VA, IT2VA)
- Supports: high-level model summary and variant listing

### OpenMOSS/MOVA README (Hugging Face-hosted README for MOVA-720p)

- URL: https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md
- Publisher: OpenMOSS-Team (README hosted on Hugging Face model page)
- Type: `official-documentation`
- Primary because: Model README linked from the official model page documenting installation, benchmark references, LoRA support, and high-level evaluation notes.
- Scope: MOVA-720p (README content and benchmark references)
- Supports: variant descriptions, mentions of LoRA support, references to MOVA Benchmark for Arena

### MOVA model commit with file and config metadata (Hugging Face commit)

- URL: https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6
- Publisher: OpenMOSS-Team (Hugging Face commit log)
- Type: `repository`
- Primary because: Immutable commit entry for MOVA-720p checkpoint recording configuration fields, file size, and a version object SHA256; used as the checkpoint revision evidence.
- Scope: MOVA-720p checkpoint config and file metadata
- Supports: checkpoint revision SHA, model config fields (text_dim, dim, num_layers, num_heads, patch_size, required VAE embedding), checkpoint file sizes and hashes

### MOVA repository (OpenMOSS / GitHub)

- URL: https://github.com/OpenMOSS/MOVA
- Publisher: OpenMOSS (GitHub repository)
- Type: `repository`
- Primary because: Canonical project repository containing training/inference code, pointers to model downloads, and project-level documents.
- Scope: MOVA project (installation, code, evaluation scripts)
- Supports: installation and inference code pointers, project-level documentation

### MOVA LICENSE (Apache-2.0) in repository

- URL: https://github.com/OpenMOSS/MOVA/blob/main/LICENSE
- Publisher: OpenMOSS (GitHub repository license file)
- Type: `repository`
- Primary because: Repository LICENSE file explicitly declaring Apache License, Version 2.0 for project artifacts.
- Scope: MOVA project license
- Supports: Apache-2.0 license statement for MOVA

### MOVA technical report: "MOVA: Towards Scalable and Synchronized Video-Audio Generation" (arXiv)

- URL: https://arxiv.org/abs/2602.08794
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical technical report describing architecture and evaluation for the MOVA project.
- Scope: MOVA family; architecture and evaluation descriptions
- Supports: architecture description, evaluation framing, and high-level discussion of synchronization metrics and benchmark methodology

### Hugging Face model commit recording ancillary metadata (alternative commit in findings)

- URL: https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/4765a74b7a60fa13a23c787af1fc953a56057987
- Publisher: OpenMOSS-Team (Hugging Face commit log)
- Type: `repository`
- Primary because: Additional recorded commit metadata for the MOVA project referenced in the research findings (records license field and other high-level metadata).
- Scope: MOVA project metadata
- Supports: repository-level metadata and claims about native bimodal generation and artifacts

## Evidence gaps

- Evidence gap: No explicit tokenizer name/version, vocab/merges, or tokenization protocol found in the canonical sources checked (model card, README, repository, arXiv): https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794.
- Evidence gap: No canonical JSON/HTTP input schema (field names, types, required/optional flags) was found in the canonical sources checked (model card, README, repository, arXiv): https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794.
- Evidence gap: The canonical sources do not provide exact numeric benchmark table/figure locators (table/figure numbers, appendix tables, or page numbers) for per-checkpoint metric values (DeSync, IB-Score, LSE-C/LSE-D, cpCER) within the artifacts available in the research findings; therefore these numeric claims cannot be independently verified from the provided canonical artifacts: checked https://arxiv.org/abs/2602.08794, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA.
- Evidence gap: The canonical sources do not supply a precise mapping of MOVA Benchmark for Arena sample indices/split filenames to the paper's reported tables/metrics; checked https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://arxiv.org/abs/2602.08794, https://github.com/OpenMOSS/MOVA.
- Evidence gap: No canonical guidance on container formats, codecs, or audio/video bitrate parameters was found in the model card, README, repository, or technical report (checked https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794).
- Evidence gap: Ambiguity between high-level artifacts and checkpoint metadata on whether the checkpoint accepts image input: model card and README describe IT2VA support, but commit metadata records "has_image_input": false (checked https://huggingface.co/OpenMOSS-Team/MOVA-720p/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-720p/commit/169d1a94c53a197085b41deb788a4ff5166703c6).
- Evidence gap: No upstream, checkpoint-scoped competitor benchmark rows or exact table locators for alternatives (LTX-2, Ovi, Genmo/Mochi, HunyuanVideo 1.5, LTX-Video, SkyReels V2, Stable Video Diffusion XT, Wan2.2, CogVideoX-2b) were found in the canonical MOVA artifacts provided in the research findings; therefore cross-model checkpoint-scoped comparisons cannot be produced from these canonical sources alone (checked https://arxiv.org/abs/2602.08794, https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 21 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'richservo' for this exact model scope: $.sources[6] uses unapproved repository owner 'richservo' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/genmoai/mochi Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Lightricks/LTX-Video Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.37.1/en/api/pipelines/skyreels_v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Wan-Video/Wan2.2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/zai-org/CogVideoX-2b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
