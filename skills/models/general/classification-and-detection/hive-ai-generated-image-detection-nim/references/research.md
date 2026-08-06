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

- Research key: `build-nvidia-com-hive-ai-generated-image-detection-36e2b7f1b1`
- Independent audit: `revised`
- Researched: `2026-07-23T20:02:40.323973+00:00`

The Forge-covered artifact is the Hive AI Generated Image Detection model (upstream ID hive/ai-generated-image-detection) packaged as an NVIDIA NIM container and exposed via a NIM inference endpoint. Primary creator documentation and NIM references state the model provides a binary AI-generated classification head (confidence score) and a source-attribution head that returns the likely generative engine or "none" when unidentified. The NIM reference reports the model architecture as a CNN based on EfficientNet-B4 and a model version v1.0. The NIM inference API documents runtime input encoding and upload rules (base64 data URI for images <200 KB; presigned S3 asset for larger images), accepted formats (jpg, jpeg, png), and a single-image-per-request constraint. Primary sources document training on millions of generated and human-created images and frequent updates to address new engines and adversarial techniques. Primary sources do not report parameter counts, an immutable checkpoint/revision identifier beyond v1.0, precise preprocessing transforms (pixel-dimension limits, resize/cropping, normalization mean/std, color-space conversions), numeric output tensor shapes or explicit calibrated score ranges or recommended thresholds; these missing items are recorded as evidence gaps.

## Identity

- Upstream name: hive/ai-generated-image-detection
- Checkpoint/version: v1.0
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: EfficientNet-B4 (CNN) — as stated in the NIM reference
- License: not reported
- Evidence: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html, https://build.nvidia.com/hive/ai-generated-image-detection

## Selection

### Recommended

- **Binary classification to detect whether an image is AI-generated or modified (surface likely AI-generated content for downstream workflows).** — Primary Hive documentation and the NIM catalog/reference describe a binary classification head that indicates whether an image is AI-generated accompanied by a confidence score.
  Scope: hive/ai-generated-image-detection (NIM-packaged model; upstream v1.0)
  Evidence: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection
- **Source attribution: return the likely generative engine that produced an image when identifiable (use as a signal for triage or investigative workflows).** — Creator documentation and NIM references describe a source-attribution head that returns the likely AI synthesis model or "none" if unidentified.
  Scope: hive/ai-generated-image-detection (NIM-packaged model; upstream v1.0)
  Evidence: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html

### Conditional

- **Integration into automated content-moderation stacks to surface likely AI-generated images for human review (automated gating only with local calibration).** — Primary sources do not provide calibrated score ranges or recommended decision thresholds; therefore automated actions must be gated by human review or validated local thresholds and continuous monitoring. Users must validate operating points in their environment.
  Scope: hive/ai-generated-image-detection (NIM-packaged model; upstream v1.0)
  Evidence: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://build.nvidia.com/hive/ai-generated-image-detection
- **Production deployment with operational monitoring to capture model updates and changes in coverage over time.** — NIM catalog and creator documentation state the model receives frequent updates; deployments should monitor updates and apply NIM model profiles and container updates as provided.
  Scope: NIM-packaged hive/ai-generated-image-detection (container runtime)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://docs.thehive.ai/docs/ai-image-and-video-detection

### Avoid

- **Any vision task outside AI-generated image detection or source attribution (for example: fine-grained species identification, OCR, general object detection).** — Primary sources describe the model specifically as an AI-generated image detector with a binary head and a source-attribution head; there is no primary-source evidence the checkpoint supports other vision tasks.
  Scope: hive/ai-generated-image-detection (NIM-packaged model; upstream v1.0)
  Evidence: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html
- **Deploying the model without reviewing or complying with Hive's terms-of-use and NIM/NGC access/governance requirements.** — Creator terms of use and NGC catalog documentation include usage restrictions and access requirements; users must review contractual/terms requirements prior to deployment.
  Scope: hive/ai-generated-image-detection (NIM-packaged model)
  Evidence: https://thehive.ai/terms-of-use, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://build.nvidia.com/hive/ai-generated-image-detection

## Input preparation

### Semantic inputs

- Image content: single 2D image representing the visual content to be classified for AI-generation origin. Sources: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer

### Accepted formats

- Accepted image formats for the inference endpoint are jpg, jpeg, and png. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection

### Preprocessing

- Runtime input encoding: images <200 KB must be provided as a base64-encoded data URI (data:image/{format};base64,{base64encodedimage}); images >200 KB must be uploaded to a presigned S3 bucket via NVCF Asset APIs and referenced as data:image/png;asset_id,{asset_id}. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer
- Only a single image is supported per inference request; batching is not supported by the documented inference endpoint. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer
- Model manifest and profile location: NIM model profiles are stored inside the container at /opt/nim/etc/default/model_manifest.yaml (profile contents not exposed in the inspected documentation). Sources: https://docs.nvidia.com/nim/multimodal-safety/latest/models.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection
- Evidence gap: Primary sources do not specify pixel-dimension limits, explicit resize/cropping rules, normalization mean/std, color-space conversions, or any numeric preprocessing parameters for this checkpoint in the inspected documents. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection

### Pre-submit validation

- Validate that the input is a single 2D image in an accepted format (jpg/jpeg/png) and that images larger than 200 KB are uploaded as assets and referenced by asset_id URIs; invalid requests produce HTTP 422 as documented. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer
- Evidence gap: Primary sources do not provide per-input semantic bounds for ambiguous cases, nor do they provide a canonical list of unsupported image types or per-pixel limits in the inspected references. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html

### Task-specific formatting

- No task-specific prompt templates, paired-input order, or control fields are documented for the image-classification inference endpoint in the inspected primary evidence. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer, https://docs.thehive.ai/docs/ai-image-and-video-detection

## Output interpretation

### Outputs

- Binary classification head: returns a confidence indicator that the image is AI-generated or modified (described as a confidence score in creator and NIM references). Exact tensor shapes, numeric score datatype, and explicit calibrated numeric bounds are not reported in the inspected primary sources. Sources: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection
- Source-attribution head: returns the likely generative engine (generator identifier) when identifiable or "none" if it cannot identify a source. Primary sources describe the field semantically but do not expose a formal token list, shape, or confidence-vector schema. Sources: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html
- Inference endpoint behavior: on success returns HTTP 200 with classification results; invalid requests return HTTP 422 Validation Error (documented response semantics). Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer

### Interpretation

- Do not assume calibrated numeric score ranges or fixed thresholds: primary sources describe confidence scores but do not provide numeric calibration guidance or recommended operating points in the inspected documents. Sources: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection

### Post-inference validation

- Post-inference validation: users should validate local performance and set decision thresholds appropriate to their risk tolerance because the primary sources do not document calibrated thresholds or gating guidance for automated actions. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### hive-deepfake-image-detection-nim — `insufficient-evidence`

- Task: AI-generated / manipulated image detection (detection/classification of synthetic images)
- Criteria: No primary-source checkpoint-scoped numeric benchmarks, dataset names/splits, metrics, or evaluation protocols for direct comparison were found in the inspected documentation for the exact hive/ai-generated-image-detection checkpoint versus hive/deepfake-image-detection.
- Rationale: The NIM support matrix and NGC catalog list both Hive models, but the inspected sources do not publish numeric, checkpoint-scoped evaluation results or comparable protocol details for these specific checkpoints.
- Comparison conditions: Checked NIM support matrix and NGC catalog entries for both models; no numeric benchmark tables/figures/sections for either checkpoint were found in these primary sources.
- Evidence: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://build.nvidia.com/hive/ai-generated-image-detection

### nvidia-nemoguard-jailbreak-detect-nim — `insufficient-evidence`

- Task: AI-generated / manipulated image detection (detection/classification of synthetic images)
- Criteria: No primary-source checkpoint-scoped performance metrics or direct protocol comparisons between hive/ai-generated-image-detection and the cited alternative were available in the inspected NIM documentation and NGC catalog.
- Rationale: Inspected NIM documentation and NGC catalog do not contain checkpoint-scoped benchmark numbers or protocol details for a direct comparison; therefore insufficient primary evidence exists to prefer one candidate over the other for this task.
- Comparison conditions: Checked NIM docs and NGC catalog for benchmark or protocol links; no comparable numeric evaluation data found.
- Evidence: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection

## Limitations and safety

### Limitations

- Model coverage and updates: the model was trained on millions of AI-generated and human-created images and receives frequent updates to address new generative engines and adversarial techniques; coverage therefore evolves over time (implication: operational drift and coverage gaps are possible). Sources: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection
- Optimization scope: primary sources state the model is optimized for media generated by popular engines (examples listed by the creator); the scope beyond listed engines and per-engine performance are not documented in the inspected references. Sources: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html
- Packaging/runtime constraints: the model is delivered as an NVIDIA NIM container running on a CUDA-accelerated runtime; operational characteristics and optimizations are tied to the NIM container and model profiles (implementation details separate from upstream checkpoint behavior). Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html
- Evidence gap: Primary sources inspected do not report per-input preprocessing parameters (pixel-dimension caps, resize/resampling/cropping rules, normalization mean/std, or explicit color-space conversions) for this exact checkpoint. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection
- Evidence gap: Primary sources inspected do not report parameter counts, an immutable checkpoint revision identifier beyond v1.0, or layer-level architecture details beyond the stated EfficientNet-B4 family description. Sources: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.thehive.ai/docs/ai-image-and-video-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection

### Safety

- Use governance and contractual restrictions: users must comply with creator terms and NIM/NGC access/governance; Hive's Terms of Use prohibit using the AI Service for identifying any person or for facial recognition without explicit written authorization. Sources: https://thehive.ai/terms-of-use, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://build.nvidia.com/hive/ai-generated-image-detection
- Security maintenance: the model receives frequent updates to address new engines and adversarial techniques; deployments should include update-monitoring and security maintenance practices. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://docs.thehive.ai/docs/ai-image-and-video-detection

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hive — AI Image and Video Detection (creator documentation)

- URL: https://docs.thehive.ai/docs/ai-image-and-video-detection
- Publisher: Hive
- Type: `official-documentation`
- Primary because: Canonical creator documentation describing the Hive AI-generated-image-detection model, training data description, output heads, and intended uses.
- Scope: Upstream Hive ai-generated-image-detection model (creator documentation)
- Supports: Model determines whether an input image or video is entirely AI-generated
- Supports: Model trained on millions of artificially generated images and human-created images from across the web
- Supports: Model returns a binary classification indicating whether the image is AI-generated accompanied by a confidence score
- Supports: Model returns the likely AI synthesis model that created the image (source attribution head)
- Supports: Model can be used to flag and remove AI-generated content on platforms

### NVIDIA NIM reference: hive-ai-generated-image-detection (model reference)

- URL: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection
- Publisher: NVIDIA (NIM API reference)
- Type: `official-documentation`
- Primary because: NVIDIA NIM reference page documenting the packaged Hive model, version, architecture statement, accepted inputs, and high-level output descriptions.
- Scope: NIM-packaged hive/ai-generated-image-detection (reference-level upstream metadata)
- Supports: Model returns a binary classification and a source-attribution head
- Supports: Model architecture described as a CNN based on EfficientNet-B4
- Supports: Accepted input image formats include PNG, JPEG, JPG
- Supports: Model version reported as v1.0
- Supports: Model uses a TensorRT engine for inference and was tested on NVIDIA L40 hardware (runtime evidence listed on the reference)

### NVIDIA NIM inference API: hive-ai-generated-image-detection infer

- URL: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection-infer
- Publisher: NVIDIA (NIM API reference)
- Type: `official-documentation`
- Primary because: Official NIM inference endpoint documentation describing runtime input encoding, size/upload rules, accepted formats, single-image request constraint, and HTTP response behaviors.
- Scope: NIM inference endpoint for hive/ai-generated-image-detection
- Supports: Inference requests must provide each image as a base64-encoded data URI if the image is smaller than 200 KB
- Supports: Images larger than 200 KB must be uploaded to a presigned S3 bucket and referenced via an asset_id URI
- Supports: Only a single image input is supported per inference request
- Supports: Accepted image formats for the inference endpoint are jpg, png, and jpeg
- Supports: Successful inference returns HTTP 200; invalid requests return HTTP 422 Validation Error

### NVIDIA NIM Multimodal Safety — models page

- URL: https://docs.nvidia.com/nim/multimodal-safety/latest/models.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: NIM multimodal-safety official documentation describing supported models, model profiles, and the two-head architecture for Hive's model as packaged in NIM.
- Scope: NIM-packaged multimodal-safety models including hive/ai-generated-image-detection
- Supports: Model has two heads: a binary classification head and a source-attribution head
- Supports: NIM model profiles are stored at /opt/nim/etc/default/model_manifest.yaml inside the container
- Supports: The model manifest defines a profile for Hive AI Generated Image Detection with the two-head architecture

### NVIDIA NIM for Multimodal Safety — support matrix

- URL: https://docs.nvidia.com/nim/multimodal-safety/latest/support-matrix.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Official NIM support matrix listing model IDs and supported hardware/engine notes for NIM-packaged models.
- Scope: Support matrix entries for NIM multimodal-safety models including hive/ai-generated-image-detection
- Supports: Lists model named "AI Generated Image Detection" with model ID "hive/ai-generated-image-detection" published by Hive
- Supports: Lists hive/deepfake-image-detection as a separate model published by Hive
- Supports: Indicates NVIDIA provides optimized TensorRT engine support on specific GPU models for the Hive model

### NVIDIA NGC catalog: Hive AI Generated Image Detection (NIM container)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection
- Publisher: NVIDIA NGC / NIM
- Type: `repository`
- Primary because: NGC catalog entry documenting the NIM container packaging of Hive's AI Generated Image Detection model, runtime packaging, update behavior, and access model.
- Scope: NIM-packaged hive/ai-generated-image-detection container (NGC catalog)
- Supports: NIM container analyzes images and returns a confidence score indicating how likely the image is AI-generated or modified
- Supports: NIM model was trained on millions of images from dozens of major AI image generators and receives frequent updates
- Supports: NIM container runs on a CUDA-accelerated runtime optimized for NVIDIA GPUs
- Supports: Access to the NGC catalog entry requires a subscription

### Build.NVIDIA — Hive AI Generated Image Detection (landing)

- URL: https://build.nvidia.com/hive/ai-generated-image-detection
- Publisher: NVIDIA Build
- Type: `model-card`
- Primary because: Build.NVIDIA landing/model-card presenting the Hive offering as packaged for Forge/Build and describing model purpose at a high level.
- Scope: Build.NVIDIA presentation and model card for hive/ai-generated-image-detection
- Supports: Model described as a robust image classification model for detecting and managing AI-generated content
- Supports: High-level product description and links to deployment guidance

### Hive — Terms of Use

- URL: https://thehive.ai/terms-of-use
- Publisher: Hive
- Type: `official-documentation`
- Primary because: Creator's terms of use describing allowed uses, restrictions (noting prohibitions on facial recognition/identification), and license-like usage restrictions for their AI services.
- Scope: Hive legal terms applicable to use of Hive AI services including detection APIs
- Supports: States AI Service does not provide definitive identifications of any person
- Supports: Prohibits using the AI Service for identifying any person or for facial recognition without explicit written authorization
- Supports: Grants a revocable, limited, non-exclusive, non-sublicensable, non-transferable right to use the services for internal business purposes

## Evidence gaps

- Benchmark gap: No primary-source numeric benchmark results (dataset name/version/split, metric, numeric value, evaluation protocol) for the exact hive/ai-generated-image-detection checkpoint were found in the inspected primary sources. Checked locators: https://docs.thehive.ai/docs/ai-image-and-video-detection (model documentation page), https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection (NIM model reference page), https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection (NGC container catalog entry), https://build.nvidia.com/hive/ai-generated-image-detection (Build.NVIDIA model card).
- Preprocessing gap: Primary sources do not publish explicit preprocessing parameters (pixel-dimension limits, resize/cropping rules, normalization mean/std, or color-space conversions). Checked locators: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.nvidia.com/nim/multimodal-safety/latest/models.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection.
- Checkpoint metadata gap: Primary sources do not publish parameter counts, an immutable checkpoint revision beyond v1.0, or full layer-level architecture details. Checked locators: https://docs.api.nvidia.com/nim/reference/hive-ai-generated-image-detection, https://docs.thehive.ai/docs/ai-image-and-video-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection.
- Runtime profile contents gap: The NIM model manifest location is documented (/opt/nim/etc/default/model_manifest.yaml) but the manifest/profile contents for this model were not published in the inspected documentation. Checked locators: https://docs.nvidia.com/nim/multimodal-safety/latest/models.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection.
- Licensing gap: Primary sources inspected do not provide an explicit model-weight versus code-license statement (exact license identifiers for model weights and container code are not reported). Checked locators: https://docs.thehive.ai/docs/ai-image-and-video-detection, https://catalog.ngc.nvidia.com/orgs/nim/teams/hive/containers/ai-generated-image-detection, https://thehive.ai/terms-of-use.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA: $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
