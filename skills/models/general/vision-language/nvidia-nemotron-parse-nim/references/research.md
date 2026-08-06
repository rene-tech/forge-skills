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

- Research key: `build-nvidia-com-nvidia-nemotron-parse-7466ab787f`
- Independent audit: `revised`
- Researched: `2026-07-23T23:03:48.804542+00:00`

Using only NVIDIA primary-hosted pages inspected (build.nvidia model card, NGC container listings, NeMo Curator PDF pipeline and inference-stage docs, NIM example pages and RAG extraction docs), Nemotron Parse is documented as a tiny autoregressive Visual Language Model (VLM) for document transcription that produces reading-order text, spatially grounded bounding boxes, and semantic class labels from document inputs. Curator inference-stage docs show DEFAULT_MODEL_PATH 'nvidia/NVIDIA-Nemotron-Parse-v1.2' and list backend and inference defaults; NeMo Curator PDF pipeline docs list pipeline defaults and the interleaved Parquet output fields. NIM API example pages document one-image-per-request and lack of text-input support. RAG docs document PDF-focused extraction and dedicated GPU runtime constraints. Primary NVIDIA pages inspected do not publish an immutable container→upstream-checkpoint mapping beyond Curator's default model_path string, do not publish a consolidated numeric benchmark table tied to a specific container/release, and do not publish a canonical full request+response JSON schema with coordinate-origin conventions and numeric confidence-calibration guidance; these absences are reported in evidenceGaps.

## Identity

- Upstream name: nemotron-parse
- Checkpoint/version: nvidia/NVIDIA-Nemotron-Parse-v1.2
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Transformer-based tiny autoregressive Visual Language Model (VLM) with a visual feature extractor and autoregressive decoder (reading-order-preserving document transcription)
- License: NVIDIA Software License Agreement; Product-Specific Terms for NVIDIA AI Products; NVIDIA Nemotron Open Model License; NVIDIA Community Model License; CC-BY-4.0 (tokenizer)
- Evidence: https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://build.nvidia.com/nvidia/nemotron-parse

## Selection

### Recommended

- **Document transcription from PDFs and document images into structured text with spatial annotations (formatted/extracted text + bounding boxes + semantic class labels).** — NGC container listing and build.nvidia model card describe Nemotron Parse producing structured annotations (formatted text, bounding boxes, semantic classes) from document inputs; NeMo Curator PDF pipeline documents how Nemotron Parse integrates into PDF ingestion and emits interleaved Parquet outputs for downstream workflows.
  Scope: Nemotron Parse NIM/container (NGC container: nemotron-parse / nemotron-parse-v1.2) and NeMo Curator PDF pipeline integration.
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://build.nvidia.com/nvidia/nemotron-parse, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

### Conditional

- **Integration into document-processing pipelines that consume spatially grounded annotations (e.g., retrievers or curation pipelines) provided implementers validate exact runtime response fields and coordinate conventions per deployment.** — Confirm runtime response shapes, exact JSON/Parquet field names, coordinate-origin conventions, units, and score semantics in the deployed container/API because primary pages do not publish a canonical exhaustive response schema tied to the container release.
  Scope: Nemotron Parse NIM/container (NGC container listings) and NeMo Curator inference-stage integration.
  Evidence: https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf
- **Using Nemotron Parse outputs as training labels or high-assurance ground truth for downstream supervised training.** — Perform domain validation, calibration audits, and quality review because primary NVIDIA pages do not publish consolidated numeric benchmarks or prescriptive confidence-to-threshold calibration guidance tied to the container release.
  Scope: Nemotron Parse NIM/container (NGC/container listing and build.nvidia model card) and NeMo Curator pipeline outputs.
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://build.nvidia.com/nvidia/nemotron-parse, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

### Avoid

- **Pure text-only processing workflows that accept only raw text (no image/PDF input).** — NIM API documentation states text input is not supported and examples show image/PDF-focused inputs; Nemotron Parse is documented as image/PDF-focused.
  Scope: Nemotron Parse NIM/container (NIM API examples and release notes).
  Evidence: https://docs.nvidia.com/nim/vision-language-models/1.5.0/examples/nemotron-parse/api.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/nemotron-parse/api.html, https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html
- **Assuming model confidences are calibrated for direct acceptance without application-specific validation.** — Primary sources do not provide prescriptive confidence calibration mappings or acceptance thresholds for Nemotron Parse outputs.
  Scope: Nemotron Parse NIM/container (model card and NGC/container listings).
  Evidence: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2

## Input preparation

### Semantic inputs

- Primary NVIDIA documentation references document pages delivered as PDFs and document images as the inputs Nemotron Parse consumes; Curator pipeline handles PDF rendering into per-page items before model inference. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

### Accepted formats

- NeMo Curator PDF pipeline and NVIDIA RAG docs document PDF as a supported/primary document input format; NIM API examples accept image data (image URL or Base64) for Nemotron Parse; an exhaustive MIME-type or file-extension list is not published on the inspected pages. Sources: https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/nemotron-parse/api.html, https://docs.nvidia.com/rag/latest/nemotron-parse-extraction.html

### Preprocessing

- NeMo Curator PDF pipeline documents defaults used for PDF rendering and inference orchestration: render DPI default 300, max_pages default 50, inference_batch_size default 4, pdfs_per_task default 10, max_num_seqs default 64, text_in_pic default False, enforce_eager default False, min_crop_px default 10; Curator inference-stage docs show DEFAULT_MODEL_PATH as 'nvidia/NVIDIA-Nemotron-Parse-v1.2' and list backend selection defaults. Sources: https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf, https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference
- Primary container and model-card pages do not publish exhaustive image preprocessing normalization constants (exact resize/crop policy, color-mean/std) for all ingress modes; such specifics are not present on the inspected primary pages. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

### Pre-submit validation

- Inspected primary sources do not enumerate detailed input-validation rules such as minimum readable text size, per-request byte limits, or exhaustive supported-image-extension lists; implementers should validate inputs and confirm container/API behavior in their deployment. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

### Task-specific formatting

- NIM example documentation shows control-token/tool-type usage (e.g., 'markdown_bbox', 'markdown_no_bbox', 'detection_only') and documents that only one tool type may be specified per request; NIM examples show images may be provided via a public URL or Base64-encoded string and follow image-payload patterns. Sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/examples/nemotron-parse/api.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/nemotron-parse/api.html, https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html
- NeMo Curator PDF pipeline example usage demonstrates manifest_path, pdf_dir, backend ('vllm'), pdfs_per_task 10, max_pages 50, and inference_batch_size 4 as a canonical ingestion example for Curator-driven runs. Sources: https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

## Output interpretation

### Outputs

- Nemotron Parse produces structured annotations including formatted/extracted text, bounding boxes, and semantic class labels (spatially grounded layout information) as documented on the NVIDIA model card and NGC container listing. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://build.nvidia.com/nvidia/nemotron-parse
- When used via the NeMo Curator PDF pipeline, outputs are emitted as interleaved Parquet rows containing fields such as sample_id, position, modality, text_content, binary_content, source_files, and url representing parsed page-level items. Sources: https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

### Interpretation

- Extracted text content, classes, and bounding boxes should be interpreted as model-extracted annotations intended for downstream document-understanding pipelines rather than guaranteed ground-truth; primary NVIDIA pages frame outputs as annotations for downstream usage. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2
- Primary sources do not provide prescriptive guidance for mapping model confidences to downstream acceptance thresholds or calibration procedures; integrators must design calibration and QA policies appropriate for their application. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2

### Post-inference validation

- Primary sources do not publish recommended post-inference validation checks, QA thresholds, or filtering heuristics to improve extraction precision/recall for production workflows; implementers are advised to perform application-specific verification and QA. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: document-extraction / structured-layout extraction (protocol-matched comparison required)
- Criteria: No primary NVIDIA-side benchmark or primary-side head-to-head comparison for Nemotron Parse container/release was found on the inspected primary pages; protocol-matched comparisons and comparable primary evidence for alternatives are not published.
- Rationale: Primary NVIDIA model card, NGC container listing, Curator pipeline docs, NIM example pages, and RAG extraction docs do not provide task- and protocol-matched comparison tables or primary citations comparing Nemotron Parse to alternative containers or upstream checkpoints.
- Comparison conditions: A valid comparison requires both sides' primary documentation showing exact checkpoint/release, dataset/split, metric, and protocol; those elements are not published for Nemotron Parse on the inspected NVIDIA pages.
- Evidence: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf

## Limitations and safety

### Limitations

- Nemotron Parse is documented as a document-image/PDF transcription and structured layout extraction model and is not documented as a general-purpose pure-text transformer. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1
- Nemotron Parse integration and extraction features require GPU resources and RAG/Curator pages indicate dedicated GPU runtime requirements; some GPU SKUs are not supported per NVIDIA documentation. Sources: https://docs.nvidia.com/rag/2.4.0/nemotron-parse-extraction.html, https://docs.nvidia.com/rag/latest/nemotron-parse-extraction.html
- The inspected primary NVIDIA pages do not publish an explicit immutable mapping from every NIM/container release tag to an upstream immutable checkpoint identifier beyond Curator's default model_path string; implementers requiring immutable provenance must confirm mapping with NVIDIA or inspect container metadata. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference, https://build.nvidia.com/nvidia/nemotron-parse
- Primary pages do not publish exhaustive image preprocessing normalization constants (exact color-normalization values) or an exhaustive resize/crop policy across all ingress modes; these specifics are absent from the inspected documentation. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2
- Primary NVIDIA pages inspected do not publish consolidated numeric benchmark tables (dataset, split, metric, numeric value) tied to a specific NGC/container release; no such benchmark rows were found in the inspected primary pages. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2, https://docs.nvidia.com/nemotron/latest/usage-cookbook/Nemotron-Parse-v1.1/README.html

### Safety

- Evidence gap: Inspected primary NVIDIA pages (model card and NGC container listing) do not contain explicit prescriptive safety, privacy, or dual-use mitigation guidance or prescriptive data-handling rules. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2
- Evidence gap: Inspected primary NVIDIA RAG/Curator pages do not provide explicit guidance on handling sensitive personal data extracted from documents; implementers must apply their own data-handling, privacy, and legal reviews. Sources: https://build.nvidia.com/nvidia/nemotron-parse, https://docs.nvidia.com/rag/latest/nemotron-parse-extraction.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Nemotron Parse model card — build.nvidia.com

- URL: https://build.nvidia.com/nvidia/nemotron-parse
- Publisher: NVIDIA Corporation
- Type: `model-card`
- Primary because: Official NVIDIA model card used to verify capability statements, intended uses, and to check for benchmarks, input/output descriptions, and safety statements.
- Scope: Nemotron Parse model card (build.nvidia.com)
- Supports: capability statements: formatted text, bounding boxes, semantic classes
- Supports: intended uses: retriever/curator solutions and LLM/VLM training-data support
- Supports: document-format mentions and deployment information

### Nemotron Parse NGC container — v1.2

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2
- Publisher: NVIDIA Corporation (NGC catalog)
- Type: `official-documentation`
- Primary because: NGC container listing for Nemotron Parse v1.2 used to verify container-level capability statements, licensing names, release metadata, and documented container readiness.
- Scope: Nemotron Parse NGC container v1.2
- Supports: Nemotron Parse v1.2 produces structured annotations from images
- Supports: container-level capability and release metadata
- Supports: container licensing names referenced

### Nemotron Parse NGC container (generic/version=1 listing)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1
- Publisher: NVIDIA Corporation (NGC catalog)
- Type: `official-documentation`
- Primary because: NGC container catalog entry used to verify general container-level capability descriptions and licensing references.
- Scope: Nemotron Parse generic NGC container listing (version=1)
- Supports: container-level capability description for document text extraction with bounding boxes and semantic classes
- Supports: release metadata and licensing name references

### NeMo Curator — Nemotron-Parse PDF pipeline (load-data docs)

- URL: https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf
- Publisher: NVIDIA Corporation (NeMo Curator docs)
- Type: `official-documentation`
- Primary because: NeMo Curator documentation describing the Nemotron-Parse PDF pipeline and pipeline-level defaults and output schema used for preprocessing and Curator integration.
- Scope: NeMo Curator Nemotron-Parse PDF pipeline
- Supports: PDF pipeline defaults: dpi=300, max_pages=50, inference_batch_size=4, pdfs_per_task=10
- Supports: interleaved Parquet output fields (sample_id, position, modality, text_content, binary_content, source_files, url)
- Supports: pipeline-level parameters including model_path and backend selection

### NeMo Curator — Nemotron Parse inference stage docs

- URL: https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference
- Publisher: NVIDIA Corporation (NeMo Curator docs)
- Type: `official-documentation`
- Primary because: Curator inference-stage documentation that documents inference-stage parameters and DEFAULT_MODEL_PATH used by the Curator Nemotron-Parse inference stage.
- Scope: NeMo Curator Nemotron-Parse inference stage
- Supports: DEFAULT_MODEL_PATH set to 'nvidia/NVIDIA-Nemotron-Parse-v1.2'
- Supports: inference-stage parameters: model_path, backend (vllm/hf), inference_batch_size default=4, max_num_seqs default=64, text_in_pic default False

### NIM Nemotron-Parse API examples — NIM (1.5.0 overview + api)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.5.0/examples/nemotron-parse/api.html
- Publisher: NVIDIA Corporation
- Type: `official-documentation`
- Primary because: NIM API documentation and examples describing Nemotron Parse API invocation patterns, tool types, and input constraints.
- Scope: NIM Nemotron-Parse API examples (1.5.0)
- Supports: definitions of tool types (markdown_bbox, markdown_no_bbox, detection_only), input methods (image URL/Base64), bounding-box coordinate conventions (0.0–1.0 with top-left origin), and that text input is not supported

### NIM Nemotron-Parse API examples — NIM (1.7.0 examples)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/nemotron-parse/api.html
- Publisher: NVIDIA Corporation
- Type: `official-documentation`
- Primary because: NIM 1.7.0 example page documenting API-level behavior for Nemotron-Parse, input constraints, and recommended prompt/control-token usage.
- Scope: NIM Nemotron-Parse API examples (1.7.0)
- Supports: API requires launching the NIM container before making requests and shows image-based request examples

### NIM release notes (Nemotron Parse) — 1.5.0 release notes

- URL: https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html
- Publisher: NVIDIA Corporation
- Type: `official-documentation`
- Primary because: NIM release notes enumerating Nemotron Parse API limitations and behavior.
- Scope: NIM Nemotron Parse release notes (1.5.0)
- Supports: limitations: only one image per request, no text input, no system messages, no output streaming, no video input

### RAG Nemotron Parse extraction docs (latest)

- URL: https://docs.nvidia.com/rag/latest/nemotron-parse-extraction.html
- Publisher: NVIDIA Corporation (RAG docs)
- Type: `official-documentation`
- Primary because: Latest RAG extraction documentation mirroring runtime and configuration statements for Nemotron Parse.
- Scope: RAG Nemotron Parse extraction (latest)
- Supports: requires dedicated GPU resources; PDF-focused extraction; configuration environment variables for enabling Nemotron Parse in ingestion

### RAG Nemotron Parse extraction docs (2.4.0)

- URL: https://docs.nvidia.com/rag/2.4.0/nemotron-parse-extraction.html
- Publisher: NVIDIA Corporation (RAG docs)
- Type: `official-documentation`
- Primary because: RAG extraction documentation describing Nemotron Parse runtime requirements and PDF extraction behavior for a pinned RAG version.
- Scope: RAG Nemotron Parse extraction (2.4.0)
- Supports: requires dedicated GPU resources; compatibility notes regarding GPU SKUs

### Nemotron-Parse-v1.1 README (Nemotron docs)

- URL: https://docs.nvidia.com/nemotron/latest/usage-cookbook/Nemotron-Parse-v1.1/README.html
- Publisher: NVIDIA Corporation (Nemotron docs)
- Type: `official-documentation`
- Primary because: Nemotron project README describing model capabilities and claimed benchmark-level performance statements for Nemotron-Parse v1.1.
- Scope: Nemotron-Parse-v1.1 usage cookbook
- Supports: describes Nemotron-Parse as converting messy documents into structured JSON/LaTeX/Markdown, provides claims about precise normalized bounding boxes and benchmark performance mentions (e.g., PubTables-1M) tied to that README

### Nemotron-Parse nightly/usage-cookbook README

- URL: https://docs.nvidia.com/nemotron/nightly/usage-cookbook/Nemotron-Parse-v1.1/README.html
- Publisher: NVIDIA Corporation (Nemotron docs)
- Type: `official-documentation`
- Primary because: Nightly documentation for Nemotron-Parse usage and notebook examples.
- Scope: Nemotron-Parse-v1.1 nightly usage cookbook
- Supports: usage notebook, conversion examples, and publication/update timestamps as shown in the README

### NVIngest microservice helm chart (NVIngest) — Nemotron Parse image references

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/helm-charts/nv-ingest
- Publisher: NVIDIA Corporation (NGC catalog)
- Type: `official-documentation`
- Primary because: NVIngest microservice configuration listing Nemotron Parse image repository and default tag used in NVIngest helm chart examples.
- Scope: NVIngest microservice configuration referencing Nemotron Parse image
- Supports: NVIngest configuration references the Nemotron Parse image repository 'nvcr.io/nim/nvidia/nemotron-parse' and a default tag value in the helm chart

### NIM API reference (vision-language-models) — API endpoints

- URL: https://docs.nvidia.com/nim/vision-language-models/1.1.0/api-reference.html
- Publisher: NVIDIA Corporation
- Type: `official-documentation`
- Primary because: NIM API reference listing endpoints such as /v1/models and health/readiness endpoints relevant for runtime validation.
- Scope: NIM API reference (1.1.0)
- Supports: lists endpoints useful for runtime validation (health/readiness/metrics)

## Evidence gaps

- No primary-source explicit mapping (NIM/container release tag → immutable upstream checkpoint revision) located on inspected primary NVIDIA pages beyond Curator's DEFAULT_MODEL_PATH string; checked https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2 (NGC container listing), https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference (Curator inference-stage docs), and https://build.nvidia.com/nvidia/nemotron-parse (model card).
- No primary-source consolidated numeric benchmark table (dataset, split, metric, numeric value) tied to the NIM/container release located on inspected primary pages; checked https://build.nvidia.com/nvidia/nemotron-parse (model card), https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2 (NGC container), and https://docs.nvidia.com/nemotron/latest/usage-cookbook/Nemotron-Parse-v1.1/README.html (Nemotron README) for benchmark tables/figures/sections.
- No primary-source canonical example full request+response JSON schema (exact field names, nesting, coordinate-origin conventions, and confidence semantics) located on inspected NVIDIA primary pages; checked https://docs.nvidia.com/nim/vision-language-models/1.5.0/examples/nemotron-parse/api.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/nemotron-parse/api.html, and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2 (NGC).
- No primary-source explicit bounding-box coordinate-origin convention and units documented beyond NIM API examples' normalized 0.0–1.0 coordinates with top-left origin; checked https://docs.nvidia.com/nim/vision-language-models/1.5.0/examples/nemotron-parse/api.html and https://docs.nvidia.com/nemo/curator/nemo-curator/nemo_curator/stages/interleaved/pdf/nemotron_parse/inference for coordinate conventions.
- No primary-source canonical documentation of exact confidence/score numeric ranges and calibration guidance for Nemotron Parse on inspected NVIDIA pages; checked https://build.nvidia.com/nvidia/nemotron-parse and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2.
- No primary-source prescriptive image preprocessing normalization constants or exhaustive resize/crop policy located on the inspected pages; checked https://docs.nvidia.com/nemo/curator/curate-text/load-data/nemotron-parse-pdf and https://build.nvidia.com/nvidia/nemotron-parse.
- No primary-source consolidated full software/component license texts for every packaged component located on the model-card or container pages; checked https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse-v1.2 and https://build.nvidia.com/nvidia/nemotron-parse and recommend inspecting the container artifact metadata or contacting NVIDIA for full license texts.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 142 deterministic draft defect(s) were supplied to the audit.

- `medium` $.recommendedUseCases[0]: $.recommendedUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0]: $.recommendedUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1]: $.recommendedUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1]: $.recommendedUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[0]: $.conditionalUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[0]: $.conditionalUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[1]: $.conditionalUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.conditionalUseCases[1]: $.conditionalUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[0]: $.avoidUseCases[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[1]: $.avoidUseCases[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases[1]: $.avoidUseCases[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1]: $.inputPreparation.acceptedFormats[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1]: $.inputPreparation.preprocessing[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[2]: $.inputPreparation.preprocessing[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1]: $.inputPreparation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[1]: $.inputPreparation.taskSpecificFormatting[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1]: $.outputInterpretation.outputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[2]: $.outputInterpretation.outputs[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1]: $.outputInterpretation.interpretation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property sourceLocator Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property sourceUrl Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].direction: $.benchmarks[0].direction: 'insufficient-evidence' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[0]: $.comparisons[0]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[1]: $.comparisons[1]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[2]: $.comparisons[2]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[2]: $.comparisons[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[2]: $.comparisons[2]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[3]: $.comparisons[3]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[3]: $.comparisons[3]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[3]: $.comparisons[3]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[4]: $.comparisons[4]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[4]: $.comparisons[4]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[4]: $.comparisons[4]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[5]: $.comparisons[5]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[5]: $.comparisons[5]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[5]: $.comparisons[5]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[6]: $.comparisons[6]: missing required property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[6]: $.comparisons[6]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons[6]: $.comparisons[6]: missing required property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0]: $.limitations[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1]: $.limitations[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2]: $.limitations[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3]: $.limitations[3]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4]: $.limitations[4]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0]: $.safety[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[1]: $.safety[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0]: $.sources[0]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1]: $.sources[1]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2]: $.sources[2]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3]: $.sources[3]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4]: $.sources[4]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8]: $.sources[8]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property publisher Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property sourceType Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10]: $.sources[10]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/nemotron-parse Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1] uses forbidden secondary host ai.azure.com: $.sources[1] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://developer.nvidia.com/blog/turn-complex-documents-into-usable-data-with-vlm-nvidia-nemotron-parse-1-1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://emergentmind.com/topics/nemotron-parse-1-1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://aws.amazon.com/marketplace/pp/prodview-ny2ngku2i4ge6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/rag/latest/nemotron-parse-extraction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/nemotron-parse/api.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].split must say 'not reported' or name the split: $.benchmarks[0].split must say 'not reported' or name the split Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must not be empty: $.benchmarks[0].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].value must contain a reported numeric result: $.benchmarks[0].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[0].evidenceUrls must not be empty: $.recommendedUseCases[0].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases[1].evidenceUrls must not be empty: $.recommendedUseCases[1].evidenceUrls must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[2] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[2] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0] without evidence must be labeled as a Forge policy or evidence gap: $.safety[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[1] without evidence must be labeled as a Forge policy or evidence gap: $.safety[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
