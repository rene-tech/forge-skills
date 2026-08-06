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

- Research key: `build-nvidia-com-nvidia-nemoretriever-parse-bf48b279ab`
- Independent audit: `revised`
- Researched: `2026-07-23T22:14:11.392530+00:00`

Canonical NVIDIA primary sources describe nemoretriever-parse as an NVIDIA-published vision-language document parsing artifact served via NVIDIA NIM/container runtimes. Verified NIM/container-level evidence (model card, product page, VLM examples, API examples, benchmarking, release notes, support matrix, NGC catalog, and RAG extraction docs) supports: (a) name and high-level purpose (document transcription and structured extraction from images, emitting reading-order text, bounding boxes, and semantic class labels); (b) architecture descriptors reported in VLM examples (transformer-based vision-encoder-decoder; C-RADIO visual extractor; mBART decoder) at the NIM/examples documentation; (c) API constraints and output modes (tools parameter, single-tool-per-request examples, output modes markdown_bbox, markdown_no_bbox, detection_only, and bounding-box coordinate fields); (d) NIM/container-level throughput and latency examples for fixed image sizes on the official benchmarking page. Primary NVIDIA sources do not publish an explicit numeric upstream checkpoint identifier matching Forge 'v1', do not publish a checkpoint-scoped parameter count, and do not publish tokenizer software/version/config tied explicitly to a named upstream checkpoint; these absent items are recorded as explicit evidence gaps with exact URLs/locators checked.

## Identity

- Upstream name: nemoretriever-parse
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Transformer-based vision-encoder-decoder; visual feature extraction by C-RADIO (Commercial Radio) and decoder reported as mBART (evidence scope: NIM/container and official VLM examples)
- License: Container and distribution governed by NVIDIA container/model licensing (NVIDIA Software License Agreement / NVIDIA Community Model License) for NIM/container artifacts; tokenizer usage reported under CC-BY-4.0 for related NGC catalog/container entries (evidence scope: NIM/container-level)
- Evidence: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://build.nvidia.com/nvidia/nemoretriever-parse, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html, https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html, https://docs.nvidia.com/nim/vision-language-models/1.5.0/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1, https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html, https://docs.nvidia.com/nim/vision-language-models/1.2.0/release-notes.html

## Selection

### Recommended

- **Document OCR and structured extraction from document images, producing reading-order text, per-element class labels, and bounding boxes** — Official NVIDIA model card and VLM examples describe nemoretriever-parse as a document-focused vision-language model that extracts formatted text with bounding boxes and semantic class labels from images (e.g., title, section, caption, index, footnote, lists, tables, bibliography, image).
  Scope: NIM/container-level evidence (nemoretriever-parse as published on Build.NVIDIA and VLM examples)
  Evidence: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html, https://build.nvidia.com/nvidia/nemoretriever-parse

### Conditional

- **Production deployment (only after license review, engineering validation, and operational testing)** — NVIDIA model card documents demonstration-only posture; require license review, engineering validation, and operational testing prior to production use. If a caller requires upstream-checkpoint provenance, additional validation is needed because no numeric upstream checkpoint identifier is published in the checked canonical NVIDIA sources.
  Scope: NIM/container-level (nemoretriever-parse as published by NVIDIA)
  Evidence: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://build.nvidia.com/nvidia/nemoretriever-parse

### Avoid

- **Tasks requiring guaranteed production-grade reliability, regulatory certification, or formal external validation without additional engineering controls** — The NVIDIA model card documents the artifact as intended for demonstration purposes and not recommended for production use (NIM/container-level statement).
  Scope: nemoretriever-parse (NIM/container identity as published by NVIDIA)
  Evidence: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard

## Input preparation

### Semantic inputs

- Primary input modality documented as document images (RGB) intended for document transcription and structured extraction (NIM/container-level evidence). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://build.nvidia.com/nvidia/nemoretriever-parse

### Accepted formats

- Model card/product pages list PDF and PPT document extraction capability (NIM/container-level claim). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard
- Nemoretriever Parse extraction documentation states only PDF is supported by the service (NIM/container-level claim), creating a conflict with the model card's PPT listing. Sources: https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html

### Preprocessing

- NIM/container benchmarking examples use fixed document image sizes (e.g., 1648×2048 px) in throughput/latency examples (container/NIM-level operational examples). Sources: https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html

### Pre-submit validation

- Release notes document that only one image per request is supported and that text input is not supported at the retriever/parse API level; these are runtime/NIM/container constraints. Sources: https://docs.nvidia.com/nim/vision-language-models/1.2.0/release-notes.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html

### Task-specific formatting

- API examples list output modes (markdown_bbox, markdown_no_bbox, detection_only) and show request structure examples that select a single extraction tool via the 'tools' parameter (examples-level API documentation). Sources: https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html

## Output interpretation

### Outputs

- Emits reading-order text and structured encodings including text content, bounding-box coordinates, and semantic class attributes for document elements (NIM/container-level outputs documented on the model card and examples). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html

### Interpretation

- Document-element semantic classes explicitly documented include title, section, caption, index, footnote, lists, tables, bibliography, and image (model card). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard

### Post-inference validation

- Post-inference validation guidance: verify returned outputs include the documented class labels and bounding-box fields (e.g., xmin, ymin, xmax, ymax) before downstream consumption (API examples and model card imply these checks). Sources: https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html, https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard

## Public benchmarks

### NIM/container throughput (document-image extraction)

- Dataset/split: NIM/container benchmarking (operational throughput for fixed image sizes) / not reported
- Metric/value: requests_per_second (throughput) / 5.07 requests/second for image size 1648×2048 px under a specific ISL/OSL configuration (container/NIM-level benchmarking example) (`higher-is-better`)
- Model scope: container / NIM (operational throughput example)
- Conditions: Image size 1648×2048 px; reported under a specific ISL/OSL configuration on the official NIM benchmarking page (container/NIM-level operational example).
- Source: https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html
- Locator: Throughput/Latency examples for fixed image sizes (benchmarking examples for 1648×2048 px) on the VLM NIM benchmarking page
- Caveat: This is a container / NIM-level operational throughput example documented by NVIDIA, not a checkpoint-scoped dataset/split/metric benchmark.
- Caveat: The reported values are tied to the NIM/container benchmarking operational configuration (ISL/OSL) reported on the benchmarking page; no explicit upstream checkpoint identifier or checkpoint-scoped benchmark row is published in the checked sources.

### NIM/container latency (document-image extraction)

- Dataset/split: NIM/container benchmarking (operational latency for fixed image sizes) / not reported
- Metric/value: average_request_latency_ms / 828 ms average request latency for image size 1648×2048 px under a specific ISL/OSL configuration (container/NIM-level benchmarking example) (`lower-is-better`)
- Model scope: container / NIM (operational latency example)
- Conditions: Image size 1648×2048 px; reported under a specific ISL/OSL configuration on the official NIM benchmarking page (container/NIM-level operational example).
- Source: https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html
- Locator: Throughput/Latency examples for fixed image sizes (benchmarking examples for 1648×2048 px) on the VLM NIM benchmarking page
- Caveat: This is a container / NIM-level operational latency example documented by NVIDIA, not a checkpoint-scoped dataset/split/metric benchmark.
- Caveat: The reported values are tied to the NIM/container benchmarking operational configuration (ISL/OSL) reported on the benchmarking page; no explicit upstream checkpoint identifier or checkpoint-scoped benchmark row is published in the checked sources.

### NIM/container alternative operational example (other configuration)

- Dataset/split: NIM/container benchmarking (operational throughput/latency additional example) / not reported
- Metric/value: requests_per_second; average_request_latency_ms / 3.75 requests/second and 1872 ms average request latency for image size 1648×2048 px under another reported configuration (container/NIM-level benchmarking example) (`context-only`)
- Model scope: container / NIM (operational example)
- Conditions: Image size 1648×2048 px; reported as an alternative configuration on the official NIM benchmarking page.
- Source: https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html
- Locator: Alternative throughput/latency examples for fixed image sizes on the VLM NIM benchmarking page
- Caveat: Container/NIM-level operational example; not a checkpoint-scoped evaluation on a dataset/split/metric protocol.
- Caveat: Different reported configuration produces different throughput/latency; values are tied to the specific NIM/container benchmarking configuration.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: No task-protocol-matched comparison available for a named nemoretriever-parse checkpoint
- Criteria: No checkpoint-scoped dataset/split/metric/value rows tied to a named nemoretriever-parse checkpoint were found; only container/NIM-level operational benchmarking examples are available.
- Rationale: Canonical NVIDIA sources provide NIM/container-level throughput and latency examples but do not provide checkpoint-scoped benchmark rows for a named nemoretriever-parse checkpoint; therefore protocol-matched comparisons cannot be supported from the checked primary NVIDIA sources.
- Comparison conditions: Checked model card, NIM container pages, VLM benchmarking pages, API examples, and release notes; no checkpoint-scoped evaluation rows matching a named nemoretriever-parse checkpoint were found in those locations.
- Evidence: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html

## Limitations and safety

### Limitations

- The official NVIDIA model card documents nemoretriever-parse as intended for demonstration purposes and not recommended for production use (NIM/container-level statement). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard
- Evidence gap: No canonical NVIDIA primary source in the checked set publishes a numeric upstream checkpoint identifier matching Forge 'v1'; checked locations include the model card, product pages, examples/overview, API examples, benchmarking page, release notes, support matrices, related NGC container entries, and extraction docs. Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://build.nvidia.com/nvidia/nemoretriever-parse, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html, https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html, https://docs.nvidia.com/nim/vision-language-models/1.5.0/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1, https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html, https://docs.nvidia.com/nim/vision-language-models/1.2.0/release-notes.html
- Evidence gap: Exact parameter count (parameterScale) and tokenizer software/version/config for a named nemoretriever-parse checkpoint are not reported in the inspected canonical NVIDIA sources. Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1
- Evidence gap: Canonical NVIDIA sources checked do not provide checkpoint-scoped calibration/confidence semantics or numeric correctness scores (precision/recall/F1) for a named nemoretriever-parse checkpoint. Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html
- Evidence gap: Ambiguity in accepted document container formats between model card/product page (PDF and PPT listed) and extraction documentation (PDF only). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html

### Safety

- The published NVIDIA model card and related NGC catalog entries document NVIDIA container/model licensing and governance; container-level artifacts are governed by NVIDIA licensing (NVIDIA Software License Agreement and NVIDIA Community Model License) and related NGC catalog entries indicate tokenizer usage under CC-BY-4.0 for the related container listing (NIM/container-level licensing statements). Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1
- Evidence gap: Canonical NVIDIA sources checked do not provide explicit PII-redaction, privacy, or clinical/biosecurity mitigations specific to nemoretriever-parse at checkpoint scope; practitioners should perform data-governance review and add downstream redaction/PII controls as required. Sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Nemoretriever-parse modelcard

- URL: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card describing nemoretriever-parse capabilities, inputs, outputs, and demonstration posture.
- Scope: nemoretriever-parse (model card / NIM/container)
- Supports: model name and description (document transcription, structured extraction)
- Supports: document-format support claims (PDF and PPT listed on model card)
- Supports: document-element classification capabilities and bounding-box outputs
- Supports: demonstration-only deployment posture and licensing/governance notes
- Supports: emitted outputs (reading-order text and structured encodings)

### Nemoretriever-parse (product/home) page

- URL: https://build.nvidia.com/nvidia/nemoretriever-parse
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA product/home page listed by Forge as the starting upstream URL and providing product-level governance and access notes.
- Scope: nemoretriever-parse (product/home)
- Supports: product listing and governance/access notes
- Supports: reference identity for Forge mapping
- Supports: primary input modality and high-level purpose statements

### VLM retriever examples: overview (1.2.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official VLM NIM examples describing retriever/parse behavior and architecture notes.
- Scope: VLM NIM examples / nemoretriever-parse (examples-level)
- Supports: description as a tiny autoregressive visual language model for document transcription
- Supports: visual feature extraction by C-RADIO
- Supports: decoder reported as mBART
- Supports: output-in-reading-order statement
- Supports: reported output modes overview

### VLM retriever API examples (1.2.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official retriever API examples demonstrating request parameters, output modes, and example request constraints.
- Scope: retriever API examples / nemoretriever-parse (API-level)
- Supports: single-tool-per-request example constraint ('tools' parameter)
- Supports: statement that text input is not supported in the retriever API examples
- Supports: output modes: markdown_bbox, markdown_no_bbox, detection_only
- Supports: example request structure and example request snippets

### VLM NIM benchmarking (latest)

- URL: https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM benchmarking documentation providing container/NIM-level throughput and latency examples for fixed image sizes.
- Scope: NIM/container benchmarking (container-level operational examples)
- Supports: container/NIM-level throughput and latency examples for image sizes such as 1648×2048 px
- Supports: examples of alternative configurations producing different throughput/latency

### VLM NIM release notes (1.7.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes documenting runtime constraints and behavioral notes for VLM NIMs including input and runtime restrictions.
- Scope: VLM NIM release notes (1.7.0)
- Supports: single-image-per-request constraint
- Supports: text input not supported
- Supports: system messages not supported
- Supports: video input not supported

### VLM NIM support matrix (1.5.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.5.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Support matrix documenting resource and precision guidance for VLM NIMs used to corroborate operational requirements.
- Scope: VLM NIM support matrix (1.5.0)
- Supports: GPU and software support guidance for running VLM NIMs
- Supports: resource and precision guidance referenced by NIM documentation

### NGC catalog: Nemotron-Parse container (related parser/container)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1
- Publisher: NVIDIA
- Type: `repository`
- Primary because: NGC catalog entry for a related parser container used in NVIDIA documentation to corroborate container-level outputs and licensing.
- Scope: Related NGC container (nemotron-parse) used for provenance
- Supports: container-level packaging and licensing notes (NVIDIA Software License Agreement / Community Model License)
- Supports: example statement that the container emits bounding boxes and semantic classes
- Supports: tokenizer licensing reported as CC-BY-4.0 in this related container entry

### NeMo/RAG extraction: Nemoretriever Parse extraction docs (2.3.0)

- URL: https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Extraction and deployment guidance for Nemoretriever Parse service used by NVIDIA-hosted endpoints and documented deployment configuration and supported input formats.
- Scope: Nemoretriever Parse extraction / deployment guidance (service-level)
- Supports: deployment and GPU-resource requirements for Nemoretriever Parse service
- Supports: statement that Nemoretriever Parse only supports PDF format documents (service-level extraction doc)
- Supports: deployment/environment configuration keys and deployment guidance

### VLM NIM release notes (1.2.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.2.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes (1.2.0) documenting initial behavioral notes for VLM NIMs including nemoretriever-parse initial release and runtime constraints.
- Scope: VLM NIM release notes (1.2.0)
- Supports: initial release notes for nemoretriever-parse
- Supports: statement that only one image per request is supported and that text input is not allowed

### Nemotron-Parse modelcard (related NVIDIA model card)

- URL: https://build.nvidia.com/nvidia/nemotron-parse/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card for a related Nemotron-Parse artifact used to corroborate example API bounding-box field names and licensing statements in NVIDIA's documentation set.
- Scope: Nemotron-Parse model card (related artifact)
- Supports: example statement that the model is ready for commercial use (related artifact)
- Supports: tokenizer licensing statements and container licensing references

### VLM Nemotron-Parse API examples (1.5.0 examples)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.5.0/examples/nemotron-parse/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: API documentation for Nemotron-Parse examples documenting bounding-box coordinate fields and normalized ranges used in NVIDIA examples.
- Scope: Nemotron-Parse API examples (1.5.0)
- Supports: bounding-box coordinate outputs (xmin, ymin, xmax, ymax) and normalized coordinate range (0.0 to 1.0)
- Supports: mode descriptions: markdown_bbox, markdown_no_bbox, detection_only (corroborating examples)

## Evidence gaps

- Evidence gap: No canonical NVIDIA primary source in the checked set publishes an explicit numeric upstream checkpoint identifier matching Forge 'v1'. Checked locators: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard (model card), https://build.nvidia.com/nvidia/nemoretriever-parse (product/home), https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html (examples/overview), https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html (examples/API), https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html (benchmarking page), https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html (release notes), https://docs.nvidia.com/nim/vision-language-models/1.5.0/support-matrix.html (support matrix), https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1 (related NGC container), https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html (extraction doc), https://docs.nvidia.com/nim/vision-language-models/1.2.0/release-notes.html (release notes 1.2.0).
- Evidence gap: Exact parameter count (parameterScale) for nemoretriever-parse is not reported in the inspected canonical NVIDIA sources. Checked locators: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/overview.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1.
- Evidence gap: Exact tokenizer software version and full tokenizer-configuration details for a named nemoretriever-parse checkpoint are not reported in the inspected canonical NVIDIA sources. Checked locators: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nemotron-parse?version=1 (related NGC container tokenizer licensing statement), https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard.
- Evidence gap: Canonical NVIDIA sources checked do not provide checkpoint-scoped calibration/confidence semantics or numeric correctness scores (precision/recall/F1) for a named nemoretriever-parse checkpoint. Checked locators: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/nim/vision-language-models/latest/benchmarking.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/release-notes.html.
- Evidence gap: Ambiguity in accepted document container formats: model card/product pages document PDF and PPT support, while the NeMo/RAG extraction doc states the Nemoretriever Parse service only supports PDF; checked locators: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 100 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: unexpected property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: unexpected property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: unexpected property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: unexpected property think_sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[2]: $.outputInterpretation.validation[2]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[3]: $.outputInterpretation.validation[3]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[4]: $.outputInterpretation.validation[4]: expected object, got list Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: missing required property statement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: unexpected property alternative Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: unexpected property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: unexpected property criteria Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: unexpected property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: unexpected property task Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5]: $.outputInterpretation.validation[5]: unexpected property verdict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: missing required property statement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: unexpected property alternative Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: unexpected property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: unexpected property criteria Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: unexpected property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: unexpected property task Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6]: $.outputInterpretation.validation[6]: unexpected property verdict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: missing required property statement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: unexpected property alternative Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: unexpected property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: unexpected property criteria Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: unexpected property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: unexpected property task Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7]: $.outputInterpretation.validation[7]: unexpected property verdict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: missing required property statement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: unexpected property alternative Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: unexpected property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: unexpected property criteria Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: unexpected property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: unexpected property task Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8]: $.outputInterpretation.validation[8]: unexpected property verdict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: missing required property statement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: unexpected property alternative Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: unexpected property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: unexpected property criteria Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: unexpected property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: unexpected property task Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9]: $.outputInterpretation.validation[9]: unexpected property verdict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: missing required property statement Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: unexpected property alternative Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: unexpected property comparisonConditions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: unexpected property criteria Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: unexpected property rationale Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: unexpected property task Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10]: $.outputInterpretation.validation[10]: unexpected property verdict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemoretriever-parse/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/nvidia-nemoretriever-parse Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/2.0.8-variant/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/nemotron-parse?version=1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemoretriever-parse/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemoretriever-parse/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemoretriever-parse/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemoretriever-parse/- Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/2.0.8-variant/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.2.0/examples/retriever/api.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/2.0.8-variant/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/rag/2.3.0/nemoretriever-parse-extraction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/2.0.8-variant/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/vision-language-models/1.5.0/benchmarking.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[5] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[5] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[6] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[6] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[7] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[7] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[8] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[8] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[9] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[9] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[10] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[10] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.limitations_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
