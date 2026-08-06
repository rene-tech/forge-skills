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

- Research key: `huggingface-co-openmoss-team-mova-360p-9ea737edd1`
- Independent audit: `revised`
- Researched: `2026-08-06T08:43:27.372087+00:00`

Primary canonical artifacts inspected (Hugging Face model card for OpenMOSS-Team/MOVA-360p, the OpenMOSS GitHub repository files README.md and LICENSE, and the arXiv technical report PDF) establish that MOVA is an Image-/Text-to-Video-Audio (IT2VA/T2VA) project whose stated goals include synchronized video-and-audio generation. The Hugging Face model card reports an MoE architecture with 32 billion total parameters and 18 billion active during inference and describes an asymmetric dual-tower fused by bidirectional cross-attention; the GitHub repository contains a project LICENSE (Apache-2.0) and a README, and the arXiv PDF documents phased training (Phase 1/2/3). The canonical artifacts inspected do not provide low-level runtime contracts (exact tokenizer files/token limits, precise preprocessing constants or scripts located at canonical file paths, explicit output container/codec/frame-rate/audio-sample-rate guarantees, or checkpoint-scoped numeric benchmark tables for MOVA-360p). Where findings conflict (for example, parameter-count reporting vs. README absence of a parameter table) both locators are cited below.

## Identity

- Upstream name: OpenMOSS-Team/MOVA-360p
- Checkpoint/version: MOVA-360p
- Immutable revision: not reported
- Parameter scale: Total parameters: 32 billion; active during inference: 18 billion (as reported on the Hugging Face model card)
- Architecture/head: Asymmetric dual-tower fused via bidirectional cross-attention; Mixture-of-Experts (MoE) diffusion backbone (as reported on the Hugging Face model card)
- License: Apache-2.0 (repository LICENSE at https://github.com/OpenMOSS/MOVA/blob/main/LICENSE; Hugging Face model card cites Apache-2.0)
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/LICENSE, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

## Selection

### Recommended

- **Synchronized video-plus-audio generation from text and/or image prompts (IT2VA/T2VA)** — Hugging Face model card describes MOVA as a framework for Image‑Text and Text‑to‑Video‑Audio tasks and the arXiv technical report title and abstract define MOVA's aim toward scalable and synchronized video-audio generation.
  Scope: OpenMOSS-Team/MOVA-360p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794

### Conditional

- **LoRA fine-tuning or adapter-based downstream fine-tuning of MOVA-360p** — Hugging Face model card and GitHub repository list/support LoRA fine-tuning at a high level; however, the inspected repository README.md did not contain explicit, copy-paste LoRA command-lines or per-checkpoint resource tables tied specifically to MOVA-360p. Before production fine-tuning, obtain the exact fine-tuning scripts/commands and measured resource tables from the repository paths or release artifacts that provide them.
  Scope: OpenMOSS-Team/MOVA-360p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md

### Avoid

- **Adopting undocumented hardware or per-step performance recommendations as authoritative (for example: 'do not train 8s 360p on single RTX 4090')** — Evidence gap: the inspected canonical artifacts (model-card, repository README, and arXiv PDF) do not contain checkpoint-scoped hardware recommendation statements or per-step performance tables tied specifically to MOVA-360p.
  Scope: OpenMOSS-Team/MOVA-360p
  Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

## Input preparation

### Semantic inputs

- MOVA accepts text prompts and optional first-frame images as inputs for synchronized video+audio generation (IT2VA/T2VA). Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794

### Accepted formats

- Model weights and checkpoint artifact for MOVA-360p are published as a Hugging Face model-card artifact and can be downloaded (model-card points to repository usage). Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md
- Evidence gap: the canonical primary artifacts inspected do not enumerate accepted input image file formats (e.g., PNG, JPEG) or an exact programmatic multimodal input payload schema for MOVA-360p. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### Preprocessing

- Evidence gap: the inspected canonical artifacts do not provide exact low-level preprocessing steps (resize algorithm, pixel scaling, color-space conversions, or normalization constants) for MOVA-360p inputs. Sources: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794

### Pre-submit validation

- Evidence gap: tokenizer identity/version, vocabulary source, special tokens, token limits, and truncation behavior for text prompts are not documented in the inspected model-card, README.md, or arXiv PDF for MOVA-360p. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### Task-specific formatting

- Evidence gap: a canonical prompt template, multimodal API field names, or exact paired-input ordering for MOVA-360p is not specified in the inspected primary artifacts. Sources: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p

## Output interpretation

### Outputs

- Primary published outputs are synchronized video frames plus aligned audio (a single jointly generated audiovisual sequence). Sources: https://arxiv.org/pdf/2602.08794, https://huggingface.co/OpenMOSS-Team/MOVA-360p

### Interpretation

- No numeric internal confidence or likelihood outputs are documented in the inspected canonical artifacts for MOVA-360p; outputs should be treated as generated media without documented probability scores. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md

### Post-inference validation

- Evidence gap: the canonical artifacts inspected provide no standardized post-output acceptance thresholds or automated perceptual-metric validators tied to MOVA-360p. Sources: https://arxiv.org/pdf/2602.08794, https://github.com/OpenMOSS/MOVA/blob/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### genmo-mochi-1-preview — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No same-protocol, checkpoint-matched side-by-side numeric comparison rows were found in the MOVA primary artifacts inspected.
- Rationale: Checked MOVA canonical artifacts (model-card, repository README, arXiv PDF) and found no numeric, checkpoint-scoped comparison rows for this alternative.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA; no MOVA checkpoint-scoped comparison table was present.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### hunyuanvideo-community-hunyuanvideo-1-5 — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No checkpoint-scoped same-protocol comparisons found in the inspected MOVA primary artifacts.
- Rationale: No side-by-side numeric comparison rows for this alternative were located in the MOVA model-card, README, or arXiv PDF.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### lightricks-ltx-2 — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No checkpoint-scoped same-protocol comparisons present in MOVA primary artifacts.
- Rationale: Inspected MOVA model-card, repo README, and arXiv PDF; no matching comparison rows were found.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### lightricks-ltx-video — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No same-protocol comparisons present in MOVA primary artifacts.
- Rationale: No MOVA checkpoint-scoped side-by-side numeric comparison rows for this alternative were found in the inspected MOVA primary artifacts.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### openmoss-team-mova-720p — `insufficient-evidence`

- Task: video-generation (higher-resolution sibling)
- Criteria: Although MOVA publishes multiple checkpoint variants, no same-protocol numeric checkpoint-matched comparison table between MOVA-360p and MOVA-720p was found in the inspected primary artifacts.
- Rationale: Inspected MOVA model-card, repository README, and arXiv PDF; no direct numeric comparison rows for MOVA-360p vs. MOVA-720p were located at those locators.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### skywork-skyreels-v2 — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No MOVA-side, checkpoint-scoped comparisons located in inspected artifacts.
- Rationale: No checkpoint-scoped numeric comparison rows for this alternative were present in the MOVA model-card, README, or arXiv PDF.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### stabilityai-stable-video-diffusion-img2vid-xt — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No same-protocol, checkpoint-matched comparisons found in inspected MOVA artifacts.
- Rationale: Inspected MOVA primary artifacts and found no numeric, checkpoint-scoped comparison rows for this candidate.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### wan-ai-wan2-2 — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No MOVA checkpoint-scoped comparisons present in inspected primary artifacts.
- Rationale: No side-by-side numeric comparison rows for this alternative were located in the MOVA model-card, README, or arXiv PDF.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### wan-ai-wan2-2-ti2v — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No MOVA-side checkpoint-matched comparisons were found in the inspected artifacts.
- Rationale: Inspected MOVA model-card, repository README, and arXiv PDF; no numeric comparison rows for this alternative were present.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

### zai-org-cogvideox-2b — `insufficient-evidence`

- Task: video-generation (general)
- Criteria: No checkpoint-scoped comparisons for this candidate were present in the MOVA primary artifacts inspected.
- Rationale: No same-protocol, checkpoint-matched numeric rows were found in the MOVA model-card, README, or arXiv PDF.
- Comparison conditions: Inspected locators: Hugging Face model card, repository README.md, arXiv PDF for MOVA.
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

## Limitations and safety

### Limitations

- Parameter-count reporting: the Hugging Face model card reports '32 billion total parameters' and '18 billion active during inference' for MOVA (model-card locator), while the repository README.md does not include a checkpoint-scoped parameter table (README.md locator). This is an ambiguity between the model-card parameter statements and absence of a parameter table in the README. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md
- Architecture-level limitation: architecture and topology are described at a high level on the Hugging Face model card (asymmetric dual-tower, bidirectional cross-attention, MoE diffusion backbone), but the canonical artifacts inspected do not include low-level per-layer implementation documentation or a checkpoint-scoped immutable revision identifier for MOVA-360p. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md
- Evidence gap: no checkpoint-scoped numeric benchmark rows (dataset/split/metric/value) for MOVA-360p were found in the inspected canonical artifacts. Sources: https://arxiv.org/pdf/2602.08794, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p
- Evidence gap: low-level preprocessing/tokenizer definitions and authoritative output containerization (codec/frame-rate/audio sample-rate) are not specified in the inspected canonical artifacts. Sources: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794

### Safety

- Evidence gap: the inspected canonical primary artifacts (Hugging Face model card, repository README.md, and arXiv PDF) do not contain an explicit deployment safety checklist, PHI/data-handling policy, or domain-specific clinical/biological safety guidance for MOVA-360p. Sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### OpenMOSS-Team/MOVA-360p (Hugging Face model card)

- URL: https://huggingface.co/OpenMOSS-Team/MOVA-360p
- Publisher: OpenMOSS-Team (Hugging Face model card)
- Type: `model-card`
- Primary because: Official Hugging Face model-card for the named MOVA-360p checkpoint; contains architecture and parameter-count statements cited in the findings.
- Scope: OpenMOSS-Team/MOVA-360p (model-card)
- Supports: Existence and naming of the MOVA-360p checkpoint
- Supports: Architecture summary (asymmetric dual-tower, bidirectional cross-attention, MoE diffusion backbone)
- Supports: Parameter-scale statements (32 billion total parameters; 18 billion active during inference)
- Supports: High-level task scope (IT2VA/T2VA, synchronized video+audio generation)

### OpenMOSS/MOVA (GitHub repository root)

- URL: https://github.com/OpenMOSS/MOVA
- Publisher: OpenMOSS Team (GitHub repository)
- Type: `repository`
- Primary because: Official project repository containing README.md and references to usage and download instructions; repository-level LICENSE file documents code license.
- Scope: Project repository and release artifacts (MOVA project)
- Supports: Repository README presence and project-level usage references
- Supports: Links and pointers used by the model-card
- Supports: Hosting of repository files inspected (README.md, LICENSE)

### README.md (repository file)

- URL: https://github.com/OpenMOSS/MOVA/blob/main/README.md
- Publisher: OpenMOSS Team (GitHub repository)
- Type: `repository`
- Primary because: Repository README.md was inspected for usage, download, and training/fine-tuning instructions and for checkpoint-scoped documentation; it is cited where absent or ambiguous information was noted.
- Scope: Repository README (file)
- Supports: Repository-level usage instructions and examples (where present)
- Supports: Absence of an explicit checkpoint-scoped parameter table or per-checkpoint numeric benchmark rows (used to form evidence gaps)

### LICENSE (repository file)

- URL: https://github.com/OpenMOSS/MOVA/blob/main/LICENSE
- Publisher: OpenMOSS Team (GitHub repository)
- Type: `repository`
- Primary because: Repository LICENSE file contains the Apache License Version 2.0 text; used to support the code license statement.
- Scope: Repository LICENSE file
- Supports: Code license: Apache License, Version 2.0

### MOVA: Towards Scalable and Synchronized Video-Audio Generation (arXiv preprint PDF)

- URL: https://arxiv.org/pdf/2602.08794
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical technical report describing MOVA, its task scope, and phased training; inspected PDF used to verify training-phase claims and absence of checkpoint-scoped numeric benchmark tables for MOVA-360p.
- Scope: MOVA technical report (paper PDF)
- Supports: Project technical report and task scope (synchronized video-and-audio generation)
- Supports: Phased training description (Phase 1/2/3) and other paper-level commentary

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric benchmark rows (dataset name + split + metric + numeric value) for OpenMOSS-Team/MOVA-360p were found at these inspected locators: https://arxiv.org/pdf/2602.08794 (arXiv PDF), https://github.com/OpenMOSS/MOVA/blob/main/README.md (repo README), https://huggingface.co/OpenMOSS-Team/MOVA-360p (model-card).
- Evidence gap: Tokenizer identity/version, vocabulary source, special tokens, token limits, and truncation behavior for MOVA-360p are not documented at: https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://arxiv.org/pdf/2602.08794.
- Evidence gap: Exact low-level input preprocessing pipeline (resize algorithm, pixel scaling, color-space conversion, normalization constants) for MOVA-360p is not specified at: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794.
- Evidence gap: Canonical prompt template, multimodal API field names, and paired-input ordering for MOVA-360p are not specified at: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p.
- Evidence gap: No explicit output container/codec, frame-rate, spatial-resolution guarantees, or audio sample-rate/format for MOVA-360p were found at: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794.
- Evidence gap: No checkpoint-scoped LoRA fine-tuning command examples, measured per-step time, or VRAM/host-RAM numeric tables tied specifically to MOVA-360p were found at: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794.
- Evidence gap: No deployment safety checklist, PHI/data-handling policy, or domain-specific clinical/biological safety guidance for MOVA-360p was found at: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p, https://arxiv.org/pdf/2602.08794.
- Evidence gap: No immutable checkpoint revision identifier (git tag or commit hash) for the MOVA-360p checkpoint was reported at: https://github.com/OpenMOSS/MOVA/blob/main/README.md, https://huggingface.co/OpenMOSS-Team/MOVA-360p.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 5 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1] uses forbidden secondary URL https: $.sources[1] uses forbidden secondary URL https://huggingface.co/papers/2602.08794 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://studio.aifilms.ai/blog/mova-open-source-video-generation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.comparisonsSummary: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
