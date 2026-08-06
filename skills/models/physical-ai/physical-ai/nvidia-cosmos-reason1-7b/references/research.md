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

- Research key: `build-nvidia-com-nvidia-cosmos-reason1-7b-aa71847c2f`
- Independent audit: `revised`
- Researched: `2026-07-23T22:48:36.281097+00:00`

Cosmos-Reason1-7B is reported in the provided primary findings as a 7B-parameter multimodal reasoning vision-language checkpoint in the Cosmos-Reason1 family. The findings state the checkpoint is post‑trained from a Qwen2.5-VL-7B-Instruct architecture using supervised fine‑tuning and reinforcement learning for physical-common-sense and embodied-reasoning capabilities. Accepted modalities reported in the findings are text, image, and video; the model emits text outputs. The NVIDIA Open Model License PDF is the provided license artifact. The repository/commit blob (commit 0caf724f...) and the Hugging Face model-page are included among the primary artifacts in the findings. The NVIDIA research page reports Intuitive Physics (Physical Common Sense) checkpoint-scoped scores for the named 7B checkpoint; other embodied-reasoning and operational claims appearing in the draft were not supported by distinct, separate locators in the supplied findings and are listed as evidence gaps below.

## Identity

- Upstream name: Cosmos-Reason1
- Checkpoint/version: Cosmos-Reason1-7B
- Immutable revision: 0caf724f837efea5e25bf6d5818dcdeec0a36604
- Parameter scale: 7B
- Architecture/head: Qwen2.5-VL-7B-Instruct
- License: NVIDIA Open Model License
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604, https://github.com/nvidia-cosmos/cosmos-reason1, https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1, https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf, https://arxiv.org/abs/2503.15558

## Selection

### Recommended

- **Plan and reason about embodied actions in physical environments for robotic systems** — Research findings (Hugging Face model card and NVIDIA research page) describe Cosmos-Reason1-7B as designed for physical AI and embodied reasoning and list robot-planning/embodied reasoning as intended application classes.
  Scope: Cosmos-Reason1-7B
  Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- **Multimodal scene understanding to support robotics planning and non-clinical safety-relevant reasoning pipelines** — The Hugging Face model page and repository commit facts in the findings state the model accepts text, image, and video and is intended for physical-AI and embodied-reasoning tasks.
  Scope: Cosmos-Reason1-7B
  Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604

### Conditional

- **Limited/high-variance video-scene inference for downstream planning (use only after task-specific validation and human/expert review)** — Use only after task-specific validation and human or expert review on target distributions; the findings note post‑training with SFT and RL but do not provide exhaustive per-task calibration details.
  Scope: Cosmos-Reason1-7B
  Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://github.com/nvidia-cosmos/cosmos-reason1

### Avoid

- **High-stakes clinical or medical decision-making without explicit expert validation and authorization** — Evidence gap: the supplied primary findings do not include a primary-source statement authorizing clinical use or enumerating clinical-authorization/validation procedures for Cosmos-Reason1-7B; therefore the dossier cannot confirm safe/authorized clinical use from the provided artifacts.
  Scope: Cosmos-Reason1-7B
  Evidence: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf, https://huggingface.co/nvidia/Cosmos-Reason1-7B

## Input preparation

### Semantic inputs

- Accepted input modalities reported in the findings are text (string), image, and video. Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604
- Input types supported are text combined with image or video (model accepts multimodal inputs). Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604

### Accepted formats

- The findings report support for image and video inputs alongside text; the primary artifacts in the findings list image and video as accepted modalities but do not enumerate every file container/codec. Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B

### Preprocessing

- The findings state visual inputs are converted into visual tokens via a vision encoder and projector before combination with text tokens for processing. Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B
- Evidence gap: the supplied primary findings do not provide a machine-readable, line/line-range code locator enumerating the exact preprocessing code path or the precise tokenization steps for visual-to-visual-token conversion.

### Pre-submit validation

- Evidence gap: the supplied findings do not provide an exhaustive, machine-readable enumeration of tokenizer internals (token id map, complete max_length semantics) or per-benchmark prompt templates required for validation.

### Task-specific formatting

- Evidence gap: while the findings state chain-of-thought reasoning capability is used, the provided primary artifacts do not include an explicit, cited README/code blob showing specific prompt tag templates (e.g., exact <think>/<answer> tag lines) with exact file/line locators. Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B

## Output interpretation

### Outputs

- Text (natural-language) responses are the reported output modality for the checkpoint. Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604

### Interpretation

- Model outputs are described in the findings as natural-language reasoning steps or final-text answers rather than direct numeric scores; numeric evaluation values are reported separately in benchmark artifacts. Sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1

### Post-inference validation

- Post-inference validation should align generated text outputs with intended physical-AI task objectives; the findings provide benchmark scores that can be used as empirical references but do not include per-instance calibration artifacts in the supplied primary sources. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1, https://arxiv.org/abs/2503.15558

## Public benchmarks

### Physical Common Sense — Arrow of Time

- Dataset/split: Physical Common Sense / not reported
- Metric/value: Arrow of Time / 56.0 (`higher-is-better`)
- Model scope: Cosmos-Reason1-7B
- Conditions: Reported on the NVIDIA research page for Cosmos-Reason1 (checkpoint-scoped result reported in the supplied primary findings).
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- Locator: NVIDIA research lab page — reported Intuitive Physics (Physical Common Sense) results (no numbered table/figure locator provided in the supplied findings).
- Caveat: The supplied findings do not provide a numbered table/figure locator for this numeric entry; value is reported on the NVIDIA research page as provided in the findings.

### Physical Common Sense — Spatial Puzzle

- Dataset/split: Physical Common Sense / not reported
- Metric/value: Spatial Puzzle / 85.4 (`higher-is-better`)
- Model scope: Cosmos-Reason1-7B
- Conditions: Reported on the NVIDIA research page for Cosmos-Reason1 (checkpoint-scoped result reported in the supplied primary findings).
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- Locator: NVIDIA research lab page — reported Intuitive Physics (Physical Common Sense) results (no numbered table/figure locator provided in the supplied findings).
- Caveat: The supplied findings do not provide a numbered table/figure locator for this numeric entry; value is reported on the NVIDIA research page as provided in the findings.

### Physical Common Sense — Object Permanence

- Dataset/split: Physical Common Sense / not reported
- Metric/value: Object Permanence / 82.0 (`higher-is-better`)
- Model scope: Cosmos-Reason1-7B
- Conditions: Reported on the NVIDIA research page for Cosmos-Reason1 (checkpoint-scoped result reported in the supplied primary findings).
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- Locator: NVIDIA research lab page — reported Intuitive Physics (Physical Common Sense) results (no numbered table/figure locator provided in the supplied findings).
- Caveat: The supplied findings do not provide a numbered table/figure locator for this numeric entry; value is reported on the NVIDIA research page as provided in the findings.

### Physical Common Sense — Average (Arrow of Time, Spatial Puzzle, Object Permanence)

- Dataset/split: Physical Common Sense / not reported
- Metric/value: Average / 74.5 (`higher-is-better`)
- Model scope: Cosmos-Reason1-7B
- Conditions: Reported aggregate average on the NVIDIA research page for the named checkpoint in the supplied findings.
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- Locator: NVIDIA research lab page — reported Intuitive Physics (Physical Common Sense) aggregate (no numbered table/figure locator provided in the supplied findings).
- Caveat: The supplied findings do not provide a numbered table/figure locator for this numeric aggregate; value is reported on the NVIDIA research page as provided in the findings.

### Physical Common Sense — Physical AI RL variant (Arrow of Time, Spatial Puzzle, Object Permanence aggregate)

- Dataset/split: Physical Common Sense (Physical AI RL variant) / not reported
- Metric/value: Per-subtask scores and average (RL variant) / 64.5 / 94.0 / 86.0 (average 81.5) (`higher-is-better`)
- Model scope: Physical AI RL variant of the model (as reported in the supplied findings)
- Conditions: Reported as the Physical AI RL variant results on the NVIDIA research page in the supplied findings; this is a variant result rather than the base checkpoint performance.
- Source: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- Locator: NVIDIA research lab page — reported Physical AI RL variant results (no numbered table/figure locator provided in the supplied findings).
- Caveat: This entry reports an RL-variant's numbers as presented in the findings; it is a distinct reported variant and the supplied findings do not provide a numbered table/figure locator.

## Comparisons

### nvidia-cosmos-embed1 — `insufficient-evidence`

- Task: Physical AI Reasoning / multimodal tasks
- Criteria: No primary-source, checkpoint-scoped, identical-protocol side-by-side numeric comparison for Cosmos-Reason1-7B vs the alternative was found in the supplied findings.
- Rationale: The supplied findings provide primary evidence for Cosmos-Reason1-7B (model card, repo commit, NVIDIA research page, arXiv), but do not provide an aligned primary-source benchmark for the alternative under identical protocol for direct numeric comparison.
- Comparison conditions: Insufficient aligned protocol evidence in the supplied findings for a direct comparison.
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1, https://arxiv.org/abs/2503.15558

### nvidia-cosmos-policy-aloha-predict2-b300-optimized — `insufficient-evidence`

- Task: Physical AI reasoning tasks
- Criteria: No primary-source, checkpoint-scoped, identical-protocol side-by-side numeric comparison present in the supplied findings.
- Rationale: The supplied findings do not include a primary-source aligned evaluation comparing Cosmos-Reason1-7B to this policy variant under identical protocols.
- Comparison conditions: Insufficient aligned protocol evidence in the supplied findings for a direct comparison.
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1

### nvidia-cosmos-reason2-8b — `insufficient-evidence`

- Task: Reasoning tasks (multimodal)
- Criteria: No primary-source, checkpoint-scoped identical-protocol comparisons for Cosmos-Reason1-7B vs Cosmos-Reason2-8B are present in the supplied findings.
- Rationale: The supplied findings include Cosmos-Reason1-7B primary artifacts but do not include an aligned, checkpoint-scoped evaluation artifact for Reason2-8B to enable a fair, identical-protocol comparison within the supplied findings.
- Comparison conditions: Insufficient aligned protocol evidence in the supplied findings for a direct comparison.
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason1-7B, https://arxiv.org/abs/2503.15558

## Limitations and safety

### Limitations

- Model distribution and use are governed by the NVIDIA Open Model License; consult the license PDF for legal terms that govern permitted uses and redistribution. Sources: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
- Evidence gap: the supplied primary findings do not enumerate exhaustive tokenizer internals (token id assignments, complete max_length semantics) required to reproduce tokenizer behavior deterministically.
- Evidence gap: the supplied primary findings do not provide machine-readable per-benchmark prompt templates or per-instance calibration artifacts needed to precisely reproduce benchmark runs.

### Safety

- Model weights and associated artifacts in the supplied findings are distributed under the NVIDIA Open Model License (June 2024); license terms govern permitted uses and redistribution. Sources: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
- Evidence gap: the supplied primary findings do not include an exhaustive primary-source statement enumerating data-privacy, clinical, or biosecurity mitigation steps beyond the license and model-card-level guidance.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card — Cosmos-Reason1-7B

- URL: https://huggingface.co/nvidia/Cosmos-Reason1-7B
- Publisher: NVIDIA / Hugging Face
- Type: `model-card`
- Primary because: Canonical Hugging Face model page for the named checkpoint as provided in the research findings.
- Scope: Cosmos-Reason1-7B
- Supports: checkpoint identity
- Supports: modalities (text,image,video)
- Supports: high-level capabilities statement
- Supports: visual-to-token conversion (high-level)

### Hugging Face commit blob — Cosmos-Reason1-7B (commit 0caf724f...)

- URL: https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604
- Publisher: NVIDIA / Hugging Face (repository blob)
- Type: `repository`
- Primary because: Commit blob cited in the findings representing the named checkpoint build and parameter/component breakdowns.
- Scope: Cosmos-Reason1-7B (specific commit)
- Supports: release commit/revision
- Supports: input types supported (text+image/video)
- Supports: component parameter counts
- Supports: architecture string attribution

### NVIDIA-cosmos GitHub repository — cosmos-reason1

- URL: https://github.com/nvidia-cosmos/cosmos-reason1
- Publisher: NVIDIA Cosmos (GitHub)
- Type: `repository`
- Primary because: Upstream repository for Cosmos-Reason1 family cited in the findings for training/post-training utilities and docs.
- Scope: Cosmos-Reason1 family
- Supports: post-training framework (SFT/RL) claims (family-level)
- Supports: repository-level documentation

### NVIDIA research lab page — Cosmos-Reason1 (research page)

- URL: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1
- Publisher: NVIDIA Research
- Type: `official-documentation`
- Primary because: NVIDIA research page included in the findings that reports checkpoint-scoped Intuitive Physics (Physical Common Sense) numeric results for the 7B checkpoint.
- Scope: Cosmos-Reason1 family; includes Cosmos-Reason1-7B
- Supports: Intuitive Physics (Physical Common Sense) numeric benchmark values for Cosmos-Reason1-7B
- Supports: reported RL-variant numeric values

### NVIDIA Open Model License (June 2024) — license PDF

- URL: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official license PDF included in the supplied findings governing model distribution/rights.
- Scope: License governing Cosmos-Reason1-7B distribution
- Supports: license terms and rights statements

### arXiv preprint — Cosmos-Reason1 (abs page)

- URL: https://arxiv.org/abs/2503.15558
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv entry for the Cosmos-Reason1 paper included in the supplied findings.
- Scope: Cosmos-Reason1 family
- Supports: paper-level family descriptions
- Supports: paper canonical reference

### arXiv preprint (context-aware listing)

- URL: https://arxiv.org/abs/2503.15558?context=cs.CV
- Publisher: arXiv
- Type: `paper`
- Primary because: arXiv listing with subject/context information cited in the supplied findings.
- Scope: Cosmos-Reason1 family
- Supports: paper metadata and categorization

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/cosmos-reason1-7b
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-cosmos-reason1
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Exact numbered table/figure/appendix locators in an official paper PDF or repository file for every reported numeric embodied-reasoning benchmark (BridgeData V2, RoboVQA, Agibot, HoloAssist, AV, RoboFail, embodied-suite averages) are not present in the supplied research findings; those numeric entries could not be independently verified from the provided primary artifacts.
- Evidence gap: Exact file/line locators or machine-readable code blobs enumerating the visual preprocessing pipeline (the precise visual-encoder-to-visual-token projector code path and parameters) are not present in the supplied findings.
- Evidence gap: Exact tokenizer internals (complete token id assignments and explicit max_length numeric semantics) are not enumerated in the supplied primary findings.
- Evidence gap: Per-benchmark, machine-readable prompt templates and exact prompt files used to compute the published benchmark numbers are not provided in the supplied primary findings.
- Evidence gap: The supplied findings do not include a primary-source explicit statement authorizing clinical or medical diagnostic use for the checkpoint; absence of such authorization cannot be interpreted as approval.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 52 deterministic draft defect(s) were supplied to the audit.

- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].sourceType: $.sources[10].sourceType: 'blog' is not in ['paper', 'model-card', 'repository', 'official-documentation', 'technical-report'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason1-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary URL https: $.sources[10] uses forbidden secondary URL https://huggingface.co/blog/PranjaliJoshi/cosmos-reason-world-foundation-model Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/nVIDIA-cosmos/cosmos-reason1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B/blob/3210bec0495fdc7a8d3dbb8d58da5711eab4b423/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B/blob/25940bb29e7e055777451d93d9ffa3757b8de69a/tokenizer_config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy/blob/main/ALOHA.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/NVlabs/cosmos-policy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B/blob/3210bec0495fdc7a8d3dbb8d58da5711eab4b423/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B/blob/0caf724f837efea5e25bf6d5818dcdeec0a36604 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Reason1-7B/blob/3210bec0495fdc7a8d3dbb8d58da5711eab4b423/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[9].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[10].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.sources[4]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/cosmos-reason1-7b: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
