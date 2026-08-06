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

- Research key: `huggingface-co-biomedica-bmc-clip-cf-936c5098c5`
- Independent audit: `revised`
- Researched: `2026-08-06T09:10:34.948386+00:00`

Primary-source inspection established an immutable Hugging Face repository snapshot at full commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6. The inspected commit tree lists a .gitattributes file and a README.md at that commit, and the commits page records the same full commit hash; the repository contributor for the initial commit is recorded as Alejandro98. The inspected primary artifacts (the repository snapshot and commits pages) contain those file entries and commit metadata but do not, within the inspected locators, report model-weights licensing, numeric benchmarks, low-level inference I/O constants, tokenizer/vocabulary files, embedding dimensionalities, or runtime performance measurements.

## Identity

- Upstream name: not reported
- Checkpoint/version: commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Immutable revision: 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/b2f0fd28a6e2f7a394cc9fd3ab938780e4d39576/.gitattributes

## Selection

### Recommended

- **Repository snapshot inspection and audit (verify files and commit state)** — The immutable Hugging Face commit tree and commits page document the repository snapshot and files at commit 68e06746...; these artifacts support auditing the repository state at that exact commit.
  Scope: Hugging Face repository snapshot at commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
  Evidence: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Conditional

- **Any downstream use that requires model weights or inference I/O contracts** — Requires locating explicit model-weights files, weights-specific license, tokenizer/vocabulary files, and inference I/O constants in primary artifacts; these were not present in the inspected commit-tree locators and commits pages.
  Scope: Hugging Face repository snapshot at commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
  Evidence: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Avoid

- **Assuming the inspected repository snapshot provides model weights, tokenizer vocabularies, or low-level inference contracts suitable for direct deployment** — The inspected immutable commit-tree and commits pages list only a .gitattributes and README.md at the checked commit and do not contain model-weights files, tokenizer/vocabulary files, or inference-time constants in the checked locators.
  Scope: Hugging Face repository snapshot at commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
  Evidence: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/b2f0fd28a6e2f7a394cc9fd3ab938780e4d39576/.gitattributes

## Input preparation

### Semantic inputs

- Evidence gap: The research did not find repository-declared semantic input types (image/text pairs or other) in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Accepted formats

- The inspected commit tree at commit 68e06746... contains a README.md and a .gitattributes file at the checked commit snapshot. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Evidence gap: The research did not find explicit accepted file-format declarations (image file types, text encodings, or serialized artifact formats) in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Preprocessing

- Evidence gap: The research did not find any inference-time preprocessing parameters (resize/crop rules, pixel normalization constants, color-space handling) in the inspected commit-tree locators or commits pages. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Pre-submit validation

- Evidence gap: The research did not find runnable input-validation checks or bounds (image size limits, allowed MIME types, text-length bounds) in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Task-specific formatting

- Evidence gap: The research did not find explicit task-specific prompt templates, paired-input ordering, or zero-shot/classification text templates in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

## Output interpretation

### Outputs

- Evidence gap: The research did not find repository-declared output contracts (embedding dimensionalities, tensor shapes/dtypes, or structured JSON response schemas) in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Interpretation

- Evidence gap: The research did not find guidance in the inspected commit-tree locators on interpreting similarity scores, calibrated probabilities, or recommended numeric thresholds for downstream decision-making. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Post-inference validation

- Evidence gap: The research did not find post-inference calibration guidance, sanity checks, or recommended validation routines in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: not reported
- Criteria: No protocol-matching per-checkpoint numeric benchmarks or cross-evaluation scripts were found in the inspected commit-tree locators that would enable a reproducible head-to-head comparison.
- Rationale: The inspected immutable repository snapshot and commits pages do not contain evaluation tables or scripts tied to the inspected commit; therefore protocol-matching comparison data are not available at these primary locators.
- Comparison conditions: Checked repository tree at commit 68e06746... and commits page for that commit; no per-commit evaluation artifacts were found in those locators.
- Evidence: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

## Limitations and safety

### Limitations

- The inspected immutable repository snapshot documents only a small set of files at the checked commit (README.md and .gitattributes) and commit metadata; repository contents required for full model use (weights, tokenizer/vocab files, evaluation artifacts, runtime metrics) were not found in the inspected locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Evidence gap: The research did not find a distinct model-weights license file or a weights-vs-code license statement in the inspected commit-tree locators. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

### Safety

- Evidence gap: The inspected commit-tree locators and commits pages do not document PHI-handling policies, privacy controls, or biosecurity/dual-use mitigation measures. Sources: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6, https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face immutable tree/commit for BIOMEDICA/BMC_CLIP_CF (commit 68e06746...)

- URL: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Immutable repository tree URL documenting the snapshot contents and exact commit identifier; used to verify files present at the named commit.
- Scope: Repository tree listing at commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Supports: Presence of a README.md file at the checked commit snapshot.
- Supports: Presence of a .gitattributes file at the checked commit snapshot.
- Supports: Verification of the full commit hash for the inspected snapshot.

### Hugging Face commits page for commit 68e06746...

- URL: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Commits page confirming the commit hash and contributor metadata for the initial commit used to identify the repository snapshot.
- Scope: Commits metadata for commit 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6
- Supports: Recording of the full commit hash 68e06746b071b7c8ee1b03e2049d62f0ae6b8be6.
- Supports: Contributor metadata showing the initial commit contributor as Alejandro98.

### Hugging Face commits page for .gitattributes file history (example commit listing)

- URL: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/b2f0fd28a6e2f7a394cc9fd3ab938780e4d39576/.gitattributes
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Commits-history locator showing a .gitattributes entry and confirming the repository has commit-history traces related to .gitattributes; used to cross-check file presence and commit verification.
- Scope: Commits history entry for .gitattributes in the BIOMEDICA/BMC_CLIP_CF repository
- Supports: Evidence that the repository includes a .gitattributes file in its history.
- Supports: Verification note that the repository initial commit short hash is 68e0674 and is marked as verified in the commits history view.

### Exact official starting source declared by Forge

- URL: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: biomedica-bmc-clip
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The inspected immutable repository tree at https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6 and the commits page https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6 do not contain model-weights files, tokenizer/vocabulary files, evaluation result tables, inference-time preprocessing constants, or runtime performance measurements; these artifacts were not found at the exact checked locators.
- Evidence gap: The research did not find an explicit model-weights license file or a separate weights-vs-code license statement at https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6.
- Evidence gap: The research did not find repository-declared semantic input/output contracts (embedding dimensionalities, tensor shapes/dtypes, or structured response schemas) in the inspected commit-tree locators at https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6.
- Evidence gap: The research did not find per-commit numeric benchmark rows, evaluation CSVs, or benchmark tables tied to commit 68e06746... when checking https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6 and https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6.
- Evidence gap: The inspected commit-tree locators do not document PHI-handling policies, privacy controls, or biosecurity/dual-use mitigation measures at the checked locators: https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/tree/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6 and https://huggingface.co/BIOMEDICA/BMC_CLIP_CF/commits/68e06746b071b7c8ee1b03e2049d62f0ae6b8be6.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 12 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2] uses unapproved repository owner 'minwoosun' for this exact model scope: $.sources[2] uses unapproved repository owner 'minwoosun' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses unapproved repository owner 'ale9806' for this exact model scope: $.sources[3] uses unapproved repository owner 'ale9806' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses unapproved repository owner 'bmclab' for this exact model scope: $.sources[4] uses unapproved repository owner 'bmclab' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/BIOMEDICA/BMC_CLIP_CF: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
