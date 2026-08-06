# Classification And Detection model selection

- Category: `general`
- Group: `classification-and-detection`
- Independent audit: `revised`
- Researched: `2026-07-23T19:48:36.464788+00:00`

This dossier covers three exact Forge NIM slugs: (A) hive-ai-generated-image-detection-nim — an image classification NIM artifact offered by Hive via NVIDIA Build/NIM that detects AI‑generated images and (per vendor documentation) provides a source‑identification capability; (B) hive-deepfake-image-detection-nim — a Hive face‑level deepfake detector served as a NIM container that locates faces and returns per‑face bounding boxes, a binary deepfake/not label and a per‑face confidence score; (C) nvidia-nemoguard-jailbreak-detect-nim — the NVIDIA NemoGuard JailbreakDetect NIM container (random forest classifier) that consumes text embeddings and returns a jailbreak classification and a scalar score/probability. Outside scope: any other checkpoints, reimplementations, mirrors, different NIM/container versions, or adapters not explicitly named in the three exact slugs above.

## Questions to answer before selecting

- What is the input modality for the use case (image vs text)? (Evidence: Build/NIM model cards for each slug specify modality.)
- If image: is per‑face detection and bounding boxes required, or only whole‑image AI‑generated detection? (Evidence gap: exact per‑face aggregation rules and recommended decision thresholds are not specified in primary NIM docs.)
- If image: are video inputs required and which container/runtime constraints apply (NIM container, TensorRT optimized profile needed)? (Supported GPUs and TensorRT/ONNX options are listed in the NIM support matrix.)
- What deployment target is required (real‑time edge with TensorRT optimized profile vs offline forensic analysis)? (Evidence: NIM support matrix documents TensorRT/ONNX support; Evidence gap: exact TensorRT profile IDs and runtime selection behaviours for each NIM container are not published in the available primary sources.)
- What adversary model is expected (known generators/deepfake engines vs unknown/new generative models)? (Evidence gap: primary sources do not provide controlled cross‑generator generalization evaluations.)
- What acceptable false‑positive / false‑negative tradeoff is mandated (consumer warning vs legal‑evidence pipeline)? (Evidence gap: primary sources do not publish recommended operating thresholds or explicit threshold selection procedures.)
- Is commercial use required and are NVIDIA NIM/container terms acceptable? (Evidence: Build/NIM model cards and NGC catalog entries state models/containers are offered for commercial use under NVIDIA licenses where specified.)
- Is per‑image explainability (bounding boxes, per‑face outputs) required? (Evidence: hive-deepfake-image-detection-nim documents per‑face bounding boxes and per‑face scores.)
- Must the model run inside an NVIDIA NIM container or can it be run in other runtimes? (Evidence: NIM support matrix documents TensorRT and ONNX runtime options; Evidence gap: exact runtime behavioural differences and manifest/profile bindings are not fully specified.)
- For LLM jailbreak detection: will the production embeddings match Snowflake Arctic Embed M Long or must a different embedding be used? (Evidence: NemoGuard NIM documentation and NGC catalog indicate the container includes/depends on Snowflake Arctic Embed M Long.)

## Comparability rules

- Only compare reported metrics when the exact same dataset name, split, and label definitions are used for all models being compared. (Evidence gap: primary sources do not publish canonical dataset names/splits for the Hive image detectors; NemoGuard paper references Jail-breakHub but NIM docs do not enumerate the exact evaluation splits.)
- For image detectors: require identical image preprocessing (explicit resolution, cropping, color normalization, and JPEG/codec quality) to compare metrics. Evidence gap: the primary NIM/modelcard sources do not publish canonical preprocessing parameters for comparison.
- For deepfake face detection: require the same face‑detection and face‑cropping pipeline and the same aggregation rule from per‑face outputs to image‑level decisions. Evidence gap: primary sources (NIM docs and Hive model card) describe per‑face outputs but do not provide a canonical face detector/cropping pipeline or aggregation rule.
- For NemoGuard comparisons: require the identical embedding model (Snowflake Arctic Embed M Long) and identical classifier artifact version. (Supported by NemoGuard NIM documentation and NGC catalog which indicate the container includes/depends on the Snowflake Arctic Embed M Long embedding and a random forest classifier.)
- Require identical NIM microservice/container version and model manifest/profile selection when runtime/profile affects the deployed binary. Evidence gap: primary sources list TensorRT/ONNX availability and supported GPUs but do not publish container profile IDs or a complete manifest-to-binary mapping necessary to guarantee binary equivalence across profiles.

## Conditional routing

### Prefer `hive-ai-generated-image-detection-nim` when Use case: detect whether a general (non‑face‑specific) image is AI‑generated; requirement: whole‑image label and optional source identification; operational constraint: run in NVIDIA NIM microservice with TensorRT optimized profile for supported GPUs.

- Why: Primary NIM/Build sources describe Hive's AI‑Generated Image Detection model as an image classification model for detecting AI‑generated content and reference a source‑identification capability in the Hive/NIM documentation and model card. NIM support matrix documents TensorRT/ONNX runtime options for the model on supported GPUs.
- Alternative: hive-deepfake-image-detection-nim
- Alternative: nvidia-nemoguard-jailbreak-detect-nim
- Evidence: https://build.nvidia.com/hive/ai-generated-image-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html

### Prefer `hive-deepfake-image-detection-nim` when Use case: per‑face deepfake detection on images or video; requirement: per‑face bounding boxes and per‑face confidence for forensic review or human‑in‑the‑loop triage; deployment: NIM container or NGC catalog artifact.

- Why: Primary NIM reference and Hive model/container catalog state the Deepfake Image Detection model locates faces and outputs per‑face bounding boxes, binary deepfake/not labels and per‑face confidence scores; NGC catalog entry documents the container distribution.
- Alternative: hive-ai-generated-image-detection-nim
- Alternative: nvidia-nemoguard-jailbreak-detect-nim
- Evidence: https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/deepfake-image-detection, https://build.nvidia.com/hive/deepfake-image-detection

### Prefer `nvidia-nemoguard-jailbreak-detect-nim` when Use case: classify text prompts/inputs to detect jailbreak or prompt‑injection attempts against LLMs; required outputs: boolean 'jailbreak' flag and an interpretable scalar score; allowed license: commercial; runtime: NIM microservice or NIM container acceptable.

- Why: NemoGuard NIM model card and NIM documentation describe the NemoGuard JailbreakDetect container as a random forest classifier consuming text embeddings and returning classification and probability, and NGC lists the container including the Snowflake Arctic Embed M Long embedding model. The NIM docs reference the related arXiv paper that details the evaluated methodology.
- Alternative: hive-ai-generated-image-detection-nim
- Alternative: hive-deepfake-image-detection-nim
- Evidence: https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard, https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect

### Prefer `hive-ai-generated-image-detection-nim` when Use case: real‑time edge deployment requiring TensorRT optimized runtime on supported GPUs for whole‑image detection throughput.

- Why: NIM support matrix lists the Hive AI‑Generated Image Detection model and Deepfake Image Detection model as supported with TensorRT-optimized FP32 engines on A100/H100/L40/A10G GPUs; for whole‑image detection where a TensorRT-optimized path is required, the Hive AI model entry and NIM support documentation are the primary sources of runtime support information.
- Alternative: hive-deepfake-image-detection-nim
- Alternative: nvidia-nemoguard-jailbreak-detect-nim
- Evidence: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection

### Prefer `insufficient-evidence` when Use case: determine which artifact generalizes better to previously unseen/new generative models or novel deepfake engines (adversary: previously unseen generators); requirement: generalization to unseen generator families.

- Why: Primary NIM and NGC catalog entries document training data summaries (e.g., 'millions of images from dozens of major deepfake generators' for the deepfake model) and model capabilities, but do not provide head‑to‑head controlled cross‑generator generalization evaluations or held‑out generator family tests in the available primary sources. Therefore primary evidence is insufficient to prefer any single slug for unseen/new generator generalization.
- Alternative: hive-ai-generated-image-detection-nim
- Alternative: hive-deepfake-image-detection-nim
- Alternative: nvidia-nemoguard-jailbreak-detect-nim
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/deepfake-image-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection

### Prefer `insufficient-evidence` when Use case: requirement that the model artifact and runtime licensing explicitly permit commercial use and operation inside a NIM container.

- Why: Primary NIM model cards and NGC catalog entries indicate these containers/models are offered for commercial use under NVIDIA licensing terms and that NemoGuard uses the NVIDIA Open Model License at the build modelcard; however, exact runtime licensing permissibility and product‑specific terms must be checked at deployment time against the current NGC/NIM licensing artifacts. The available primary sources indicate commercial‑use intent but do not substitute for a deployment license check.
- Alternative: hive-ai-generated-image-detection-nim
- Alternative: hive-deepfake-image-detection-nim
- Alternative: nvidia-nemoguard-jailbreak-detect-nim
- Evidence: https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection

## Benchmark taxonomy

### AI-generated image detection (binary) and source identification (multi-class where supported) — hive-ai-generated-image-detection-nim

- Datasets: Evidence gap: primary sources do not list canonical dataset names or held‑out splits for hive-ai-generated-image-detection-nim
- Metrics: Binary detection metrics: AUROC, Average Precision (AP), accuracy, false positive rate (FPR) and false negative rate (FNR) at reported operating points (operating point thresholds must be reported to interpret FPR/FNR)., Source‑identification (multi‑class) metrics where the source‑id head is enabled: per‑class accuracy, macro and micro F1, confusion matrix over named generator classes., Calibration metrics: Brier score or expected calibration error for confidence scores when reported.
- Compare only when: Exact match of dataset name and split is required to compare numeric results. Evidence gap: dataset/split names are not provided in the primary sources.
- Compare only when: Identical image preprocessing: resolution, cropping, color space and compression/JPEG quality must be matched. Evidence gap: these exact preprocessing parameters are not specified in the primary sources.
- Compare only when: Same model head configuration (binary-only vs binary+source-identification head) and identical NIM container version/profile must be used for comparison. Evidence gap: primary sources do not publish explicit manifest/profile→binary mapping.

### Face-level deepfake detection (per‑face bounding box, per‑face binary classification) — hive-deepfake-image-detection-nim

- Datasets: Evidence gap: primary sources do not list canonical dataset names or held‑out splits for hive-deepfake-image-detection-nim
- Metrics: Per‑face metrics: per‑face accuracy, per‑face AUROC, per‑face AP., Image‑level aggregation metrics (after applying a specified aggregation rule): image‑level accuracy, TPR@fixed FPR, FNR under that aggregation., Per‑identity and per‑manipulation breakdowns: per‑generator and per‑manipulation‑type performance where available.
- Compare only when: Use the same face detector and face cropping pipeline prior to running the model. Evidence gap: primary sources do not specify a canonical face detector or cropping parameters.
- Compare only when: Use the same aggregation rule from per‑face outputs to image‑level decisions (e.g., max face score). Evidence gap: aggregation rule is not documented in primary NIM/modelcard sources.
- Compare only when: Report identical preprocessing (image/video formats and codec/JPEG quality) and the same NIM container/artifact version and model manifest/profile.

### Jailbreak / prompt‑injection detection for text prompts — nvidia-nemoguard-jailbreak-detect-nim

- Datasets: Jail-breakHub (as reported in arXiv:2412.01547) and other benchmark suites referenced in the arXiv paper. (Evidence gap: NIM model card and NIM docs reference the paper but do not enumerate exact train/val/test split names used by the paper for the NemoGuard NIM container evaluation.)
- Metrics: Binary classification metrics: accuracy, AUROC, Average Precision (AP), TPR at fixed FPR; operating point selection and thresholding must be reported to interpret TPR/FPR., Calibration and thresholding metrics: explicit selected threshold on the reported score range and false positive rate at that threshold., Score distribution analyses (histograms) for benign vs attack prompts to justify threshold selection as reported.
- Compare only when: Same embedding model must be used (Snowflake Arctic Embed M Long) when reproducing or comparing results that depend on embeddings. (Supported by NemoGuard NIM docs and NGC catalog which indicate the container uses Snowflake Arctic Embed M Long.)
- Compare only when: Use identical prompt templates, tokenization and context window when constructing benign vs attack examples. Evidence gap: the NIM documentation and model card reference the paper but do not publish the exact prompt templates or tokenization settings used in the paper's evaluation.
- Compare only when: Use the exact same NIM container version and classifier artifact for any reported comparisons. Evidence gap: container manifest/version mapping to classifier artifact details is not published in the available primary sources.

### Cross‑model comparability notes (image detectors vs image detectors and cross‑modal comparisons)

- Datasets: Evidence gap: no single canonical cross‑task dataset linking AI‑generated detection and deepfake per‑face labels is published in the provided primary sources
- Metrics: When comparing different image detectors, ensure identical metrics, identical preprocessing and identical label schemas (recommended metrics: AUROC, AP, TPR@FPR, per‑class accuracy for source‑ID tasks, calibration metrics).
- Compare only when: Same dataset with explicit, non‑overlapping label schema and clearly defined decision mapping for hybrid/perturbed images is required. Evidence gap: primary sources do not provide such a cross‑task dataset or label mapping.

## Primary sources

- [NVIDIA Build — Hive AI-Generated Image Detection](https://build.nvidia.com/hive/ai-generated-image-detection) — NVIDIA Build / Hive; supports Hive's ai-generated-image-detection model is a robust image classification model for detecting and managing AI-generated content.
- [NIM Reference — Hive AI-Generated Image Detection](https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection) — NVIDIA NIM (reference documentation); supports Documentation describing the Hive AI-Generated Image Detection model served via NIM (model reference entry).
- [NIM Multimodal Safety — Support Matrix (models & runtimes)](https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html) — NVIDIA NIM (product documentation); supports Lists NIM model IDs including hive/ai-generated-image-detection and hive/deepfake-image-detection., States TensorRT-optimized FP32 support on GPUs A100, H100, L40, A10G for the listed multimodal safety models and that ONNX/FP32 is available on GPUs with >=4GB memory.
- [NVIDIA Build — Hive Deepfake Image Detection](https://build.nvidia.com/hive/deepfake-image-detection) — NVIDIA Build / Hive; supports Hive deepfake-image-detection model description indicating the model detects faces and identifies deepfake images.
- [NIM Reference — Hive Deepfake Image Detection](https://docs.api.nvidia.com/nim/reference/hive-deepfake-image-detection) — NVIDIA NIM (reference documentation); supports States the Deepfake Image Detection model locates faces and for each detected face outputs a bounding box, a (binary) classification, and a confidence score., States supported input formats (PNG, JPEG/JPG) and that the model is offered via NIM as a third‑party model.
- [NGC Catalog — Hive Deepfake Image Detection container](https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/deepfake-image-detection) — NVIDIA NGC (container catalog); supports Catalog entry for Hive Deepfake Image Detection container (NGC) and statements that the model was trained on millions of images from dozens of major deepfake generators and is distributed as a prebuilt NIM container.
- [Hive — AI Image and Video Detection (product docs)](https://docs.thehive.ai/docs/ai-image-and-video-detection) — Hive (official product documentation); supports Product documentation describing Hive's AI Image and Video Detection APIs, formats supported, and per-face scoring description for deepfake detection.
- [NVIDIA Build — NemoGuard JailbreakDetect model card](https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect/modelcard) — NVIDIA Build (model card); supports NemoGuard JailbreakDetect model card describing the model as a random forest classifier for jailbreak detection, ready for commercial use, referencing the paper 'Improved Large Language Model Jailbreak Detection via Pretrained Embeddings', and stating input is a text embedding and outputs classification and probability.
- [NIM Documentation — NemoGuard JailbreakDetect](https://docs.nvidia.com/nim/nemoguard-jailbreakdetect/latest/index.html) — NVIDIA NIM (product documentation); supports NemoGuard JailbreakDetect microservice documentation stating the microservice classifies jailbreak attempts and that the microservice uses a random forest (Ardennes) trained on Snowflake Arctic Embed M Long embeddings; references the related paper.
- [NGC Catalog — NemoGuard JailbreakDetect container](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemoguard-jailbreak-detect) — NVIDIA NGC (container catalog); supports NGC catalog entry for NemoGuard JailbreakDetect container, stating the container includes a random forest classifier and the Snowflake Arctic Embed M Long embedding model and is distributed as a NIM container.
- [Paper (arXiv) — Improved Large Language Model Jailbreak Detection via Pretrained Embeddings](https://arxiv.org/pdf/2412.01547) — arXiv (preprint); supports Paper describing the approach pairing pretrained embeddings with classifiers for jailbreak detection and reporting evaluation results on the authors' benchmark (references to Jail-breakHub dataset and performance claims appear in the paper).

## Evidence gaps

- Evidence gap: Primary sources do not list canonical public dataset names, versions, or held‑out splits for hive-ai-generated-image-detection-nim; dataset pages and split definitions are required to reproduce or compare numeric benchmarks.
- Evidence gap: Primary sources do not list canonical public dataset names, versions, or held‑out splits for hive-deepfake-image-detection-nim; dataset pages and split definitions are required to reproduce or compare numeric benchmarks.
- Evidence gap: Primary NIM/modelcard sources do not publish exact image preprocessing parameters (canonical resolution, crop window, color normalization, JPEG/codec quality) for hive-ai-generated-image-detection-nim or hive-deepfake-image-detection-nim; these are required for identical comparisons.
- Evidence gap: Primary NIM/modelcard sources do not publish the canonical face detector, face‑crop parameters, or per‑face→image aggregation rule for hive-deepfake-image-detection-nim; these are required to reproduce image‑level metrics.
- Evidence gap: Primary NIM/modelcard and NGC sources do not provide explicit container manifest/profile IDs or a complete manifest→binary mapping showing how TensorRT/ONNX profile selection maps to a specific deployed binary for the Hive NIM containers; this information is required to guarantee binary equivalence across runtime profiles.
- Evidence gap: Primary sources do not provide controlled head‑to‑head cross‑generator generalization evaluations or held‑out generator family tests for the Hive image detectors that would allow preferring one slug for generalization to previously unseen generator families.
- Evidence gap: For nvidia-nemoguard-jailbreak-detect-nim, the NIM documentation and model card reference the arXiv paper but do not publish the exact prompt templates, tokenization settings, or the exact train/val/test split identifiers used in the paper's evaluation; reproducing the paper's numeric results for the NIM container requires those artifacts.
- Evidence gap: Primary sources do not publish recommended operating thresholds, threshold selection procedures, or calibration guidance (explicit thresholds for score→binary mapping) for any of the three NIM artifacts; such procedures are required for operational deployment with fixed FPR/FNR constraints.
- Evidence gap: Primary sources do not publish fine‑tuning regimes (retrain head vs full fine‑tune), hyperparameters, random seeds, or recommended evaluation batching rules for the packaged NIM artifacts; these are necessary to reproduce vendor reported results or to fine‑tune the artifact.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
