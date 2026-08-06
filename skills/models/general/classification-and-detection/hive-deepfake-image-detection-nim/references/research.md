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

- Research key: `build-nvidia-com-hive-deepfake-image-detection-8b102328c6`
- Independent audit: `revised`
- Researched: `2026-07-23T21:48:21.341518+00:00`

Primary NVIDIA NIM API reference and the NIM support matrix describe the NIM-served Hive Deepfake Image Detection model as an image-based detector that identifies whether an image is a deepfake. The NIM API reference states the model locates faces in an image and, for each detected face, outputs a bounding box, a classification, and an accompanying confidence score; it also states the model is ready for commercial and non-commercial use. The NIM support matrix documents supported GPUs and precision/engine support (explicitly listing support via optimized TensorRT engine on A100, H100, L40, and A10G with FP32 and ONNX support for GPUs with sufficient memory) and notes the Docker environment must support NVIDIA GPUs and the NVIDIA Container Toolkit. The inspected primary sources do not report an immutable upstream checkpoint identifier, parameter count, numeric preprocessing parameters (resize/normalization/cropping), accepted-image-file-encoding numeric limits, model-weights license text, or numeric evaluation benchmark rows tied to this exact served checkpoint; these absences are recorded as evidence gaps in this dossier.

## Identity

- Upstream name: Hive Deepfake Image Detection model
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

## Selection

### Recommended

- **Per-face deepfake detection in images (binary classification per detected face)** — The NIM API reference describes the model as identifying whether an image is a deepfake and states that the model locates faces and outputs, for each detected face, a bounding box, a classification, and an accompanying confidence score.
  Scope: hive/deepfake-image-detection (NIM-served Hive Deepfake Image Detection model)
  Evidence: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- **Deploying the NIM-distributed Hive Deepfake Image Detection model on NVIDIA GPUs (validate integration and performance on target hardware)** — The NIM support matrix documents GPU and engine support (TensorRT on specific GPUs and ONNX for GPUs with sufficient memory) and requires a Docker environment that supports NVIDIA GPUs and the NVIDIA Container Toolkit; implementers must validate throughput/latency on their hardware.
  Scope: hive/deepfake-image-detection (NIM packaging/runtime constraints)
  Evidence: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

### Conditional

- **Deploying on target hardware where throughput/latency must be validated before production** — Validate integration, engine selection (TensorRT vs ONNX), and performance on the target GPU and Docker/NVIDIA Container Toolkit environment; NIM support matrix documents GPU/engine options but does not publish per-checkpoint runtime measurement protocols in the inspected pages.
  Scope: hive/deepfake-image-detection (NIM-served container/runtime)
  Evidence: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html, https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

### Avoid

- **Using the Hive Deepfake Image Detection model for non-image modalities (e.g., text, audio, or embeddings)** — The NIM API reference describes the model specifically as identifying whether an image is a deepfake, and the documented behavior is face detection and per-face classification in images; the inspected sources do not document non-image modality support.
  Scope: hive/deepfake-image-detection (NIM-served Hive Deepfake Image Detection model)
  Evidence: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

## Input preparation

### Semantic inputs

- The model consumes images and locates faces; for each detected face it produces a per-face classification, a bounding box, and an accompanying confidence score. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

### Accepted formats

- Evidence gap: The inspected primary sources do not specify accepted input image file-encoding lists or constraints in a machine-readable manifest on the checked pages. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

### Preprocessing

- Evidence gap: The inspected primary sources do not publish numeric preprocessing pipeline parameters (resize dimensions, normalization parameters, color-space conversion, cropping/truncation behavior, or batching defaults) for the served checkpoint. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

### Pre-submit validation

- Evidence gap: The inspected primary sources do not specify input-validation bounds such as maximum file size, pixel-dimension limits, or required color depth for inputs to the served checkpoint. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

### Task-specific formatting

- Evidence gap: The inspected primary sources do not provide task prompt templates, paired-input orders, or control-field formatting instructions for the deepfake image detection checkpoint. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

## Output interpretation

### Outputs

- For each detected face the model outputs a bounding box (location), a classification label, and an accompanying confidence score. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

### Interpretation

- Evidence gap: The inspected primary sources do not publish calibration details or recommended operational thresholds for the reported confidence scores; the presence of a confidence score is documented but not its numeric scale or calibration guidance. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

### Post-inference validation

- Evidence gap: The inspected primary sources do not prescribe post-inference validation rules, sanity checks, or thresholding guidance tied to the served checkpoint; implementers must define application-specific validation. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Evidence gap: Immutable upstream checkpoint identifier or file checksum for the Hive deepfake checkpoint is not reported on the inspected primary pages. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- Evidence gap: Parameter count for the Hive deepfake checkpoint is not reported in the inspected primary pages. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- Evidence gap: Exact numeric preprocessing pipeline parameters (resize dimensions, normalization parameters, color-space conversion, cropping/truncation behavior, batching defaults) are not documented in the inspected primary sources. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- Evidence gap: Exact accepted image file-encoding constraints beyond the documented behavior are not specified in the inspected primary pages. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- Evidence gap: Numeric benchmark rows tied to this exact served checkpoint (dataset/split/metric/value and evaluation conditions) are not present in the inspected primary pages; no numeric evaluation tables/figures/sections were found on the checked pages. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- Evidence gap: Exact model-weights license text or third-party model license terms for the served checkpoint are not included in the inspected primary pages. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html
- Evidence gap: Runtime/precision-tested artifacts (explicit TensorRT/FP32 test runs with hardware/protocol/measurement details tied to an immutable checkpoint) are not reported on the inspected pages. Sources: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html, https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

### Safety

- Operators must ensure their Docker/NIM environment supports NVIDIA GPUs and the NVIDIA Container Toolkit; this requirement is documented in the NIM support matrix. Sources: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html
- Evidence gap: The inspected primary documentation does not provide specialized regulated-data, clinical, or PHI handling guidance for this model; implementers should apply organizational data-protection controls. Sources: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NIM API Reference: hive-deepfake-image-detection

- URL: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA NIM API reference page listing the Hive Deepfake Image Detection model's documented per-face outputs and basic model purpose.
- Scope: hive/deepfake-image-detection (NIM API reference)
- Supports: Hive's Deepfake Image Detection model identifies whether an image is a deepfake.
- Supports: The model locates faces in an image.
- Supports: For each detected face, the model outputs a bounding box for its location, a classification, and an accompanying confidence score.
- Supports: The model is an image classification model that classifies whether an image is a deepfake.
- Supports: The model is ready for commercial and non-commercial use.

### NIM support matrix

- URL: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA NIM support matrix documenting supported GPUs, engine/precision support, and Docker/runtime environment requirements for NIM-distributed multimodal detectors including the Deepfake Image Detection model.
- Scope: NIM support matrix (multimodal detectors)
- Supports: The model ID for Deepfake Image Detection is hive/deepfake-image-detection and the publisher is Hive.
- Supports: NVIDIA supports the Deepfake Image Detection model on A100 GPUs with 40 or 80 GB memory using FP32 precision via the optimized TensorRT engine.
- Supports: NVIDIA supports the Deepfake Image Detection model on H100 GPUs with 80 GB memory using FP32 precision via the optimized TensorRT engine.
- Supports: NVIDIA supports the Deepfake Image Detection model on L40 GPUs with 48 GB memory using FP32 precision via the optimized TensorRT engine.
- Supports: NVIDIA supports the Deepfake Image Detection model on A10G GPUs with 24 GB memory using FP32 precision via the optimized TensorRT engine.
- Supports: NVIDIA supports the Deepfake Image Detection model on any NVIDIA GPU with sufficient memory (at least 4 GB) using FP32 precision via ONNX.
- Supports: The Docker environment must support NVIDIA GPUs and the NVIDIA Container Toolkit for running the model.

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/hive/deepfake-image-detection
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: hive-deepfake-image-detection
- Supports: Forge-to-upstream exact-version identity

### Deepfake Detection

- URL: https://docs.thehive.ai/reference/deepfake-detection-1
- Publisher: Hive
- Type: `official-documentation`
- Primary because: A human reviewer opened this primary source and verified the structured benchmark rows and exact locator recorded in research/manual-review-hints.json.
- Scope: hive-deepfake-image-detection
- Supports: Manually verified primary-source provenance and scope guidance

## Evidence gaps

- Evidence gap: Immutable upstream checkpoint identifier or file checksum for the Hive deepfake checkpoint is not reported on the inspected primary page: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Model Overview; Model Architecture; Input; Output; Model Version(s); Training Dataset; Inference).
- Evidence gap: Parameter count for the Hive deepfake checkpoint is not reported in the inspected primary page: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Model Overview; Model Architecture; Model Version(s)).
- Evidence gap: Exact preprocessing pipeline numeric parameters (resize dimensions, normalization parameters, color-space conversion, cropping/truncation behavior, batching defaults) are not documented in the inspected primary pages: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Input; Inference) and https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html (checked support/packaging rows).
- Evidence gap: Exact accepted image file-encoding constraints (e.g., required color depth, maximum file size, or byte-encoding constraints) are not specified in the inspected primary pages: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings: Input) and https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html.
- Evidence gap: Confidence-threshold calibration guidance or recommended score thresholds for operational binary decisions is not provided in the inspected primary documentation: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings: Output; Inference).
- Evidence gap: Exact upstream-checkpoint origin (canonical upstream repository/model-card/paper or checksum) when packaged by NVIDIA NIM is not documented on the inspected pages: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Model Version(s); Training Dataset).
- Evidence gap: Numeric benchmark rows tied to this exact served checkpoint (dataset/split/metric/value and evaluation conditions) are not present on the inspected primary pages: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Model Overview; Model Architecture; Model Version(s); Training Dataset; Inference) and https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html (checked relevant model entries).
- Evidence gap: Exact model-weights license text or the third-party model license terms are not included in the inspected primary pages: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Model Version(s); License) and https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html.
- Evidence gap: Runtime/precision-tested artifacts (explicit TensorRT/FP32 test runs with hardware/protocol/measurement details tied to an immutable checkpoint) are not reported on the inspected pages: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html (checked engine/precision rows) and https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked Inference).
- Evidence gap: No numeric benchmark or direct numeric comparison results were found for the exact hive/deepfake-image-detection checkpoint in the inspected primary page: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection (checked headings/sections: Model Overview; Model Architecture; Input; Output; Model Version(s); Training Dataset; Inference).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/hive/deepfake-image-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/hive/deepfake-image-detection: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.thehive.ai/reference/deepfake-detection-1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
