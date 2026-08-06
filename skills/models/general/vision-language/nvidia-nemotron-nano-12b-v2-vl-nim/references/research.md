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

- Research key: `build-nvidia-com-nvidia-nemotron-nano-12b-v2-vl-modelcard-d7fb808ed6`
- Independent audit: `revised`
- Researched: `2026-07-23T23:40:23.881344+00:00`

Checkpoint-scoped findings drawn from the provided primary artifacts: NVIDIA Nemotron Nano 12B V2 VL is described as a 12B-class (12.6B reported in distribution metadata) hybrid Mamba‑Transformer autoregressive language model (Nemotron‑Nano‑V2) paired with a RADIOv2.5 vision encoder and an MLP connector to enable multimodal (image/video+text) reasoning. Primary artifacts (NVIDIA technical report PDF and arXiv version, Build.NVIDIA modelcard, NGC container listing, and NVIDIA NIM docs) confirm dynamic tiling, uniform video-frame extraction, image/frame resizing to 512×512 in the described preprocessing, BF16/FP8/FP4 checkpoint packaging formats, training using Megatron in FP8 with supervised finetuning stages, and evaluations including benchmark tables reported in the arXiv/technical report (example reported scores: DocVQA 94.39, ChartQA 89.72). The inspected artifacts do not report an immutable upstream checkpoint identifier (commit SHA, file checksum, or immutable archive id) for the checkpoint. Several operational/runtime specifics (canonical exhaustive preprocessing implementation file, explicit prompt-template repository, per-checkpoint calibration artifacts, and an exhaustive dataset-level license manifest) are not present in the inspected artifacts and are reported below as evidence gaps. All statements and gaps cite the exact primary URLs inspected.

## Identity

- Upstream name: NVIDIA Nemotron Nano 12B V2 VL
- Checkpoint/version: Nemotron Nano 12B V2 VL
- Immutable revision: not reported
- Parameter scale: 12.6B
- Architecture/head: Nemotron‑Nano‑V2 hybrid Mamba‑Transformer LLM paired with RADIOv2.5 vision encoder and an MLP connector (hybrid multimodal Nemotron Nano V2 VL architecture)
- License: Model weights: NVIDIA Open Model License Agreement (as reported in model distribution metadata); NIM/container: NVIDIA Software License Agreement and Product‑Specific Terms for NVIDIA AI Products (container governance). Exact, separate license text/URLs per artifact: see evidenceUrls.
- Evidence: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-nano-12b-v2-vl, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16, https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl

## Selection

### Recommended

- **Multimodal document understanding (OCR-style extraction, document question answering, document summarization)** — Build.NVIDIA modelcard and NVIDIA technical report describe the model as intended for multimodal document intelligence and document-level reasoning; technical report and NIM docs document evaluation on OCR/DocVQA tasks and intended uses.
  Scope: Nemotron Nano 12B V2 VL (upstream checkpoint as described in the NVIDIA technical report and Build.NVIDIA modelcard)
  Evidence: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl
- **Visual Question Answering and image/frame-level multimodal reasoning (single-image and multi-image requests)** — Primary artifacts list VQA and multimodal reasoning as intended tasks and report benchmark results on DocVQA/ChartQA and other multimodal benchmarks.
  Scope: Nemotron Nano 12B V2 VL (upstream checkpoint as described in the NVIDIA technical report and arXiv/Build.NVIDIA artifacts)
  Evidence: https://arxiv.org/pdf/2511.03929, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard

### Conditional

- **Long-document and long-video reasoning in production (very large context lengths, streaming/video pipelines)** — Requires deployment validation of effective context length, runtime packaging, and serving-stack-specific enforcement (per-request limits, EVS/video pruning) because primary artifacts describe long-context design and EVS but do not provide canonical runtime enforcement details for a specific container tag or NIM mapping.
  Scope: Nemotron Nano 12B V2 VL (design/architecture claims from the NVIDIA technical report; serving/runtime behavior must be validated against the NIM/container release and deployment environment)
  Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl, https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html

### Avoid

- **Relying on a published immutable upstream checkpoint identifier (commit SHA, file checksum, or immutable archive id) for reproducible provenance** — Evidence gap: No immutable upstream checkpoint revision identifier (commit SHA, file checksum, or immutable archive id) was reported in the inspected primary artifacts.
  Scope: Nemotron Nano 12B V2 VL (upstream checkpoint as described in the NVIDIA technical report and Build.NVIDIA modelcard)
  Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard

## Input preparation

### Semantic inputs

- Model accepts multimodal inputs: image(s), video (frames), and text prompts that are interleaved with image/frame embeddings for multimodal reasoning. Sources: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl
- For video inputs the model uses uniform frame extraction; for images the model uses a dynamic tiling strategy driven by aspect ratio (dynamic tiling). Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf

### Accepted formats

- Accepted image formats: Not explicitly enumerated in the NVIDIA technical report or Build.NVIDIA modelcard PDFs. Distribution metadata lists PNG and JPG as supported image formats (distribution metadata source). Sources: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard
- Accepted video formats: distribution metadata lists MP4 and other container formats as supported (distribution metadata source). The technical report describes video inputs conceptually but does not enumerate an exact accepted-formats list. Sources: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf

### Preprocessing

- Image tiles and video frames are resized to 512×512 pixels prior to encoding by the RADIO vision encoder; image and text embeddings are interleaved and fed to the Nemotron LLM. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf
- The model uses dynamic tiling (tile count varies by aspect ratio) and uniform frame extraction for videos; tiles/frames are processed by RADIOv2.5 and passed through an MLP connector to the LLM. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929
- Evidence gap: A single canonical exhaustive preprocessing pipeline implementation file (ordered normalization, tokenization, exact pad/resize rules, explicit tile-layout enumeration such as an authoritative 12‑tile parameter specification and multi-image packing ordering) was not found in the inspected primary artifacts. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://arxiv.org/pdf/2511.03929

### Pre-submit validation

- Callers must validate that inputs conform to their chosen deployment's runtime constraints; primary artifacts describe design intent (multi-image and long-context inputs) but do not provide deployment-enforced per-request limits in a canonical runtime contract. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf
- Evidence gap: Exact per-request enforcement semantics (e.g., official container/NIM guaranteed max-images-per-request, strict per-container release-note lines) are not specified in the technical report or modelcard; distribution metadata and NIM docs contain operational references but do not provide a single canonical enforcement contract in the inspected artifacts. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-nano-12b-v2-vl, https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard

### Task-specific formatting

- Evidence gap: No canonical published prompt-template repository or exhaustive system-prompt flag list was located in the inspected primary artifacts; the modelcard and technical report describe interleaving of image/text embeddings but do not present a definitive set of deployment prompt templates or system flags. Sources: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929

## Output interpretation

### Outputs

- Primary artifacts describe the model producing natural-language textual outputs (autoregressive token sequences) as responses for VQA, extraction, summarization, and multimodal chat; outputs are standard text strings/token sequences produced by the Nemotron LLM after interleaving image/text embeddings. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16

### Interpretation

- Treat model-generated textual extraction/transcription as LLM outputs requiring downstream verification for high-stakes tasks; primary artifacts describe intended uses and note standard LLM output behaviors but do not provide per-output calibrated confidence numbers. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16

### Post-inference validation

- Evidence gap: No per-output standardized calibration curves or published per-checkpoint calibrated confidence scores for extraction/transcription tasks were present in the inspected primary artifacts. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929

## Public benchmarks

### Document Visual Question Answering (DocVQA)

- Dataset/split: DocVQA / not reported
- Metric/value: accuracy (as reported in benchmark table) / 94.39 (`higher-is-better`)
- Model scope: Nemotron Nano V2 VL (benchmark row reported for Nemotron Nano V2 VL in arXiv/technical report)
- Conditions: Reported in the benchmark table in the arXiv/technical report; primary artifacts do not provide a separate per-checkpoint evaluation script path in the inspected artifacts.
- Source: https://arxiv.org/pdf/2511.03929
- Locator: Benchmark table in arXiv:2511.03929 (benchmark table comparing Nemotron Nano V2 VL to other models)
- Caveat: Primary artifacts report benchmark table entries but do not provide an explicit file path to per-checkpoint evaluation logs or an immutable checkpoint identifier linking the exact evaluated artifact to a published immutable archive.

### Chart question answering (ChartQA)

- Dataset/split: ChartQA / not reported
- Metric/value: accuracy (as reported in benchmark table) / 89.72 (`higher-is-better`)
- Model scope: Nemotron Nano V2 VL (benchmark row reported for Nemotron Nano V2 VL in arXiv/technical report)
- Conditions: Reported in the benchmark table in the arXiv/technical report; primary artifacts do not provide a separate per-checkpoint evaluation script path in the inspected artifacts.
- Source: https://arxiv.org/pdf/2511.03929
- Locator: Benchmark table in arXiv:2511.03929 (benchmark table comparing Nemotron Nano V2 VL to other models)
- Caveat: Primary artifacts provide benchmark table rows but do not include per-checkpoint raw result logs or dataset-split specification in an attachable evaluation artifact in the inspected files.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Head-to-head numeric comparison on identical protocol (multimodal document extraction / VQA)
- Criteria: No aligned per-checkpoint numeric tables (checkpoint, dataset/split, metric, value) with precise evaluation protocol and per-checkpoint identifiers were present in the inspected artifacts to enable a protocol-matched numeric comparison.
- Rationale: ArXiv/technical report include benchmark tables showing Nemotron Nano V2 VL scores; however the inspected artifacts do not provide per-checkpoint evaluation logs or immutable checkpoint identifiers that would enable direct protocol-aligned comparisons to other Forge candidates.
- Comparison conditions: Benchmarks are reported in the technical report/arXiv but the inspected artifacts lack per-checkpoint evaluation artifacts or explicit dataset-split file references to guarantee strict protocol matching.
- Evidence: https://arxiv.org/pdf/2511.03929, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf

## Limitations and safety

### Limitations

- Evidence gap: Immutable upstream checkpoint revision identifier (commit SHA, file checksum, or immutable archive id) for Nemotron Nano 12B V2 VL is not reported in the inspected primary artifacts. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard
- Evidence gap: Canonical exhaustive training-data provenance manifest (dataset-level sources and licenses) is not present in the inspected primary artifacts; training/data sections describe datasets at a high level but do not enumerate a dataset-by-dataset license manifest in the provided files. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929
- Evidence gap: No single canonical preprocessing implementation file specifying exact pad/resize rules, tile-layout enumeration (e.g., authoritative 12-tile parameterization), and multi-image packing ordering was found in the inspected primary artifacts. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://arxiv.org/pdf/2511.03929
- Evidence gap: Per-output calibration artifacts (confidence calibration curves or standardized per-checkpoint calibration stats for extraction/transcription) are not published in the inspected primary artifacts. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929
- Evidence gap: Exact runtime/container enforcement guarantees (per-container release-note lines that guarantee production EVS/video-support or strict per-request image-count enforcement for a specific container tag) were not present in the inspected primary artifacts; distribution metadata and NIM docs reference formats and tags but do not provide a single canonical enforcement contract in the inspected artifacts. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-nano-12b-v2-vl, https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard

### Safety

- Primary artifacts include a safety.md in distribution metadata describing dataset scanning for illegal content, a guard-model approach, and recommendations to apply additional rails for instruction-tuned models; callers should apply human review for high-stakes extraction tasks. Sources: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-FP8/blob/main/safety.md, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf
- Evidence gap: No separate NVIDIA-hosted repository safety.md or an explicit, detailed guard-model pipeline document hosted on research.nvidia.com or build.nvidia.com was located in the inspected primary artifacts (distribution metadata contains a safety.md but a separate NVIDIA-hosted operational safety pipeline text was not found). Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-FP8/blob/main/safety.md

## Related upstream agent skills

### `related-model-workflow`

NVIDIA's Nemotron customization skill is first-party guidance for curating, training, evaluating, converting, and optimizing Nemotron-family checkpoints in the Nemotron repository. It is not an inference payload or Nebius deployment contract; verify the exact listed checkpoint and use the Forge/Serverless instructions for serving.
- [nemotron-customize](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-customize)

## Primary sources

### Build.NVIDIA.com modelcard: Nemotron Nano 12B V2 VL

- URL: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: Forge-declared official modelcard and serving-page for the NIM variant; used to verify serving/usage intent and high-level input/output claims.
- Scope: nvidia-nemotron-nano-12b-v2-vl (serving/modelcard)
- Supports: intended uses (document intelligence, VQA, summarization)
- Supports: high-level input modalities and long-text+image support
- Supports: serving/Forge starting source identity

### NVIDIA Nemotron Nano-V2-VL Technical Report (PDF)

- URL: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf
- Publisher: NVIDIA Research
- Type: `technical-report`
- Primary because: Authoritative technical report describing architecture (Nemotron‑Nano‑V2 Mamba‑Transformer, RADIOv2.5), preprocessing (512×512 tiles/frames, dynamic tiling), training recipe (Megatron, FP8, SFT stages), and reported evaluations.
- Scope: Nemotron Nano V2 VL (upstream technical report describing model design, training, and evaluation)
- Supports: architecture description (Mamba‑Transformer LLM, RADIOv2.5, MLP connector)
- Supports: image/video preprocessing (512×512 resize, dynamic tiling, uniform frame extraction)
- Supports: training recipe notes (Megatron, FP8, SFT stages)
- Supports: benchmarking claims and reported evaluation summaries
- Supports: checkpoint packaging formats mention (BF16, FP8, FP4) as reported in the document

### ArXiv PDF: Nemotron Nano V2 VL (arXiv:2511.03929)

- URL: https://arxiv.org/pdf/2511.03929
- Publisher: arXiv
- Type: `paper`
- Primary because: Preprint version of the technical report containing an explicit benchmark table and corroborating architecture/training claims.
- Scope: Nemotron Nano V2 VL (arXiv/preprint of the technical report)
- Supports: architecture claims (RADIOv2.5, Nemotron‑Nano‑V2)
- Supports: training recipe notes (Megatron, FP8, SFT)
- Supports: benchmark table entries (DocVQA, ChartQA scores cited)

### NVIDIA NIM reference: Nemotron Nano 12B V2 VL

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl
- Publisher: docs.api.nvidia.com (NVIDIA NIM docs)
- Type: `official-documentation`
- Primary because: NIM reference and API documentation describing the NIM serving variant, intended uses, and runtime-level notes for the served model.
- Scope: nvidia-nemotron-nano-12b-v2-vl (NIM serving/runtime reference)
- Supports: serving/runtime metadata and API-level descriptions
- Supports: intended use cases and per-request input descriptions (as documented in the NIM reference)

### NGC Container Catalog: Nemotron Nano 12B v2 VL

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-nano-12b-v2-vl
- Publisher: NGC (NVIDIA)
- Type: `official-documentation`
- Primary because: NGC container listing providing container governance, NIM container naming/tags, and listed available checkpoint precisions.
- Scope: nvidia-nemotron-nano-12b-v2-vl (NGC container/distribution metadata)
- Supports: container governance and license references
- Supports: checkpoint packaging formats (BF16, FP8, FP4) as listed in distribution metadata
- Supports: container tag identifiers

### Hugging Face model distribution metadata: NVIDIA-Nemotron-Nano-12B-v2-VL-BF16

- URL: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16
- Publisher: Hugging Face (distribution metadata mirror)
- Type: `official-documentation`
- Primary because: Distribution metadata listing parameter count, supported input formats, reported benchmark scores, and other distribution-level fields used in the dossier; included because the research findings provided these distribution facts.
- Scope: NVIDIA Nemotron Nano 12B V2 VL (distribution/packaged BF16 artifact metadata)
- Supports: parameter count (12.6B as reported in distribution metadata)
- Supports: supported input formats (PNG, JPG) and video formats (MP4, MKV, FLV, 3GP) as reported in distribution metadata
- Supports: reported benchmark scores in distribution metadata summary
- Supports: reported checkpoint precision availability (BF16, FP8, FP4) in distribution metadata

### NIM Vision-Language Models Release Notes (1.5.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Release notes identifying the NIM release version 1.5.0 that references Nemotron Nano 12B v2 VL.
- Scope: NIM release 1.5.0 (serving/runtime release metadata)
- Supports: serving/runtime version hint (nim-1-5-0) reference
- Supports: identification of the NIM release that packages the model

### NeMo Megatron Bridge documentation: Nemotron Nano V2 VL

- URL: https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/vlm/nemotron-nano-v2-vl.html
- Publisher: docs.nvidia.com (NVIDIA NeMo)
- Type: `official-documentation`
- Primary because: NeMo Megatron Bridge docs describing support for fine-tuning and conversion workflows for Nemotron Nano V2 VL.
- Scope: Nemotron Nano V2 VL (conversion/finetuning tooling)
- Supports: finetuning and LoRA application notes
- Supports: conversion guidance for downstream evaluation

### Cited official first-party source

- URL: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-FP8/blob/main/safety.md
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-nemotron-nano-12b-v2-vl
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: Immutable upstream checkpoint revision identifier (commit SHA, file checksum, or immutable archive id) for Nemotron Nano 12B V2 VL is not reported in the inspected primary artifacts. Paths inspected: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf (technical report), https://arxiv.org/pdf/2511.03929 (arXiv preprint), https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard (modelcard), https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-nano-12b-v2-vl (NGC container listing).
- Evidence gap: Canonical exhaustive preprocessing pipeline implementation file (single-file ordered specification of exact pad/resize rules, explicit tile-layout enumeration with authoritative 12‑tile parameterization, multi-image packing ordering, and deployment-conditional rules) was not present in the inspected primary artifacts. Paths inspected: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16.
- Evidence gap: Per-checkpoint numeric benchmark raw logs and explicit dataset-split mapping (checkpoint × dataset split × metric × raw value with evaluation script or hash) are not present in the inspected primary artifacts; the arXiv/technical report provide benchmark table rows but do not include attachable per-checkpoint evaluation artifacts or immutable identifiers. Paths inspected: https://arxiv.org/pdf/2511.03929, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16.
- Evidence gap: Canonical exhaustive training-data provenance manifest (dataset-level sources with license URLs per dataset) was not included in the inspected primary artifacts. Paths inspected: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929.
- Evidence gap: Per-output calibration artifacts (calibration curves or standardized per-checkpoint calibration stats for extraction/transcription) are not published in the inspected primary artifacts. Paths inspected: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://arxiv.org/pdf/2511.03929.
- Evidence gap: A separate NVIDIA-hosted operational safety pipeline document (safety.md or guard-model pipeline) hosted on research.nvidia.com or build.nvidia.com was not found in the inspected primary artifacts; distribution metadata contains a safety.md but a distinct NVIDIA-hosted operational safety artifact was not located. Paths inspected: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-V2-VL-report.pdf, https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-FP8/blob/main/safety.md.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 16 deterministic draft defect(s) were supplied to the audit.

- `medium` $.comparisons[5]: $.comparisons[5]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[6]: $.comparisons[6]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Fara-7B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemotron-parse Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-FP8/blob/main/safety.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
