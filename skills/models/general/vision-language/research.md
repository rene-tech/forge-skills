# Vision Language model selection

- Category: `general`
- Group: `vision-language`
- Independent audit: `revised`
- Researched: `2026-07-23T19:53:45.668157+00:00`

This group covers callable vision-language systems in the supplied Forge scope that accept text with image inputs, plus document/image parsing services that return text-oriented structured extraction. It includes multimodal chat, image question answering, document understanding, OCR-style extraction, and screenshot-conditioned or document-conditioned generation when those behaviors are explicitly supported by the cited primary sources for the exact checkpoint or NVIDIA-served model. It excludes unsupported family-level claims, unsupported latency or GPU-quality claims, and direct benchmark comparisons when the findings do not verify matched dataset, split, prompt, preprocessing, and evaluation conditions for the exact Forge candidates.

## Questions to answer before selecting

- Is the task general multimodal chat/VQA over images, or document parsing/OCR-style extraction with bounding boxes and semantic classes?
- Do you need a parse-oriented service that explicitly returns formatted text with bounding boxes/class attributes, rather than free-form text generation?
- Is the use case specifically screenshot/computer-use style interaction with screenshot plus text context?
- Do you require commercial-ready or production-intended positioning, or is a demonstration-purpose service acceptable?
- Is a 128K-class context/input+output limit required by the use case?
- Do you need support for video inputs, or only text-plus-image inputs?
- Are you choosing based on verified official benchmark numbers for an exact checkpoint, or only on supported task descriptions and I/O contract?
- Can you compare only when both candidates have primary-source evidence for the same benchmark and protocol, or must the result be treated as insufficient evidence?

## Comparability rules

- Compare benchmark values only when the exact checkpoint or exact NVIDIA-served variant is identified in primary evidence for both sides.
- Require the same dataset name and split, metric definition, prompt/evaluation protocol, and preprocessing/input conditions before treating numeric results as comparable.
- Do not compare NVIDIA serving-runtime documentation with upstream checkpoint quality benchmarks as if they were the same evidence type; keep runtime/API evidence separate from model-quality evidence.
- If one source provides only capability descriptions or model-card aggregates without matched protocol details for the other candidate, route with insufficient-evidence rather than implying a ranking.
- For document-parse services, do not compare their extraction outputs numerically against free-form VLM chat checkpoints unless the same dataset, output format expectations, and scoring protocol are explicitly documented for both.

## Conditional routing

### Prefer `nvidia-nemotron-parse-nim` when If the task is document parsing or OCR-style extraction and you need formatted text with bounding boxes and semantic classes from images.

- Why: The exact NVIDIA Nemotron Parse source in scope is described as a document-parsing model card endpoint, and the closely related NVIDIA parse evidence used in the findings for parse-style services explicitly describes extraction of formatted text with bounding boxes and class attributes for document handling. However, the findings do not provide a verified head-to-head protocol against the other parse candidate, so this preference is based on task fit rather than comparative benchmark evidence.
- Alternative: nvidia-nemoretriever-parse-nim
- Evidence: https://build.nvidia.com/nvidia/nemotron-parse, https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard

### Prefer `insufficient-evidence` when If the task is document parsing or OCR-style extraction but production intent matters and you want to avoid a model explicitly marked for demonstration purposes only.

- Why: The findings explicitly say nemoretriever-parse is for demonstration purposes only and not intended for production usage, but the findings do not provide equally specific production-intent evidence for the exact nvidia-nemotron-parse-nim source URL in scope. That prevents a primary-evidence winner between the two exact Forge parse services under a strict comparison rule.
- Alternative: nvidia-nemoretriever-parse-nim
- Alternative: nvidia-nemotron-parse-nim
- Evidence: https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard, https://build.nvidia.com/nvidia/nemotron-parse

### Prefer `microsoft-fara-7b-vllm-cuda13` when If you specifically need a screenshot-conditioned computer-use style model with screenshot plus text context and action/thought prediction framing.

- Why: Fara-7B is explicitly described as a multimodal decoder-only model that takes screenshot image plus text context as input, with user goal, current screenshot(s), and history of previous outputs, and it directly predicts thoughts and actions with grounded arguments.
- Alternative: qwen-qwen2-5-vl-7b-instruct-vllm
- Alternative: qwen-qwen3-vl-4b-instruct-vllm-cuda13
- Evidence: https://huggingface.co/microsoft/Fara-7B

### Prefer `microsoft-fara-7b-vllm-cuda13` when If a verified 128K-class context limit is essential for text-plus-image use and video is not required.

- Why: The findings explicitly state that Fara-7B supports a context length of 128,000 tokens. The Mistral Small NVIDIA API page in the findings confirms API usage but does not provide a verified context-length fact there, so the exact in-scope NIM variant cannot be preferred over Fara on this criterion from the supplied evidence alone.
- Alternative: mistralai-mistral-small-3-2-24b-instruct-2506-nim
- Alternative: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim
- Evidence: https://huggingface.co/microsoft/Fara-7B, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html

### Prefer `nvidia-nemotron-nano-12b-v2-vl-nim` when If you need verified support for video inputs in the exact cited source evidence.

- Why: The exact NVIDIA Nemotron Nano 12B V2 VL model card in the findings states supported input types are Image, Video, and Text, and also specifies supported video formats. The other exact Forge candidates in the supplied findings are either image-text only or lack equally explicit video-input evidence.
- Alternative: qwen-qwen2-5-vl-7b-instruct-vllm
- Alternative: qwen-qwen3-vl-4b-instruct-vllm-cuda13
- Evidence: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard

### Prefer `nvidia-nemotron-nano-12b-v2-vl-nim` when If you need a commercial-ready NVIDIA model for document-image summarization or VQA with explicit multi-image document handling.

- Why: The findings state Nemotron Nano 12B V2 VL is ready for commercial use, can process up to four images of documents at 1k x 2k each with a long text prompt, and is intended for summarization and VQA.
- Alternative: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim
- Alternative: mistralai-mistral-small-3-2-24b-instruct-2506-nim
- Evidence: https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard, https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1/modelcard, https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html

### Prefer `nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim` when If you need a general image-plus-text NVIDIA VLM explicitly positioned for OCR, image summarization, and interactive Q&A on images, but do not need video input evidence.

- Why: The NVIDIA model card findings for Llama Nemotron Nano VL explicitly list use cases including image summarization, text-image analysis, OCR, and interactive Q&A on images, with Image and Text as supported inputs.
- Alternative: nvidia-nemotron-nano-12b-v2-vl-nim
- Alternative: mistralai-mistral-small-3-2-24b-instruct-2506-nim
- Evidence: https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1/modelcard

### Prefer `nvidia-nemotron-nano-12b-v2-vl-nim` when If you need the strongest verified benchmark evidence among the exact candidates for chart reasoning and document VQA from the supplied findings.

- Why: The upstream NVIDIA Hugging Face source in the findings reports exact scores for Nemotron-Nano-12B-v2-VL on ChartQA (89.72) and DocVQA (94.39). The supplied findings do not provide matched ChartQA or DocVQA numbers for the other exact Forge candidates under comparable conditions.
- Alternative: qwen-qwen2-5-vl-7b-instruct-vllm
- Alternative: qwen-qwen3-vl-4b-instruct-vllm-cuda13
- Evidence: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16

### Prefer `qwen-qwen2-5-vl-7b-instruct-vllm` when If you need exact verified official benchmark numbers for the Qwen checkpoint in scope rather than only capability descriptions.

- Why: The findings for the exact Qwen2.5-VL-7B-Instruct model page include named benchmark results such as MVBench 69.6, PerceptionTest test 70.5, Video-MME 65.1/71.6, MMBench-Video 1.79, and several agent benchmark scores. The supplied findings for Qwen3-VL-4B-Instruct provide usage instructions but no numeric benchmark facts.
- Alternative: qwen-qwen3-vl-4b-instruct-vllm-cuda13
- Evidence: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct

### Prefer `insufficient-evidence` when If the only verified evidence for the exact candidate is API usage/serving documentation and you need a quality-based ranking against other models.

- Why: For the exact Mistral Small 3.2 24B Instruct 2506 NIM source in scope, the supplied findings confirm API querying examples and a link to a model card, but they do not provide verified benchmark values or exact quality claims for head-to-head routing versus the other exact Forge candidates.
- Alternative: mistralai-mistral-small-3-2-24b-instruct-2506-nim
- Evidence: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html

## Benchmark taxonomy

### Document visual question answering and document-image summarization

- Datasets: DocVQA, ChartQA
- Metrics: accuracy or task-specific score exactly as defined by the cited model card or benchmark table, report split and aggregation exactly as published, higher is better
- Compare only when: same exact checkpoint or exact served variant
- Compare only when: same dataset and split
- Compare only when: same prompt/evaluation protocol
- Compare only when: same image/document preprocessing and resolution conditions
- Compare only when: same output constraints if applicable

### Video-language understanding

- Datasets: MVBench, PerceptionTest test, Video-MME, MMBench-Video
- Metrics: benchmark score exactly as reported by the official source, report whether subtitles are used when the source distinguishes settings, higher is better
- Compare only when: only compare if both exact candidates publish the same benchmark with the same setting
- Compare only when: match subtitle condition for Video-MME
- Compare only when: match split and protocol as reported in primary evidence

### Agentic screenshot or UI-oriented evaluation

- Datasets: ScreenSpot, ScreenSpot Pro, AITZ_EM, Android Control High_EM, Android Control Low_EM, AndroidWorld_SR, MobileMiniWob++_SR
- Metrics: benchmark score exactly as reported by the official source, higher is better
- Compare only when: same benchmark version and setting
- Compare only when: same action space and evaluation protocol
- Compare only when: do not compare to non-agentic VLMs unless the exact same benchmark is reported for both

### Document parsing and OCR-style structured extraction

- Datasets: The research findings did not identify a verified primary-source benchmark dataset for the exact parse services in scope.
- Metrics: The research findings did not verify a retained canonical metric for the exact parse services in scope.
- Compare only when: treat as non-comparable until a primary source for both exact services specifies dataset, split, output schema, and metric
- Compare only when: match whether bounding boxes and semantic classes are required
- Compare only when: match document type such as PDF, PPT, or image input

## Primary sources

- [microsoft/Fara-7B](https://huggingface.co/microsoft/Fara-7B) — Hugging Face / Microsoft Research; supports Exact source URL for microsoft-fara-7b-vllm-cuda13, Fara-7B identity and 7B size, screenshot-plus-text input framing, computer-use style thoughts/actions description, 128,000-token context claim
- [Mistral Small 3.2 24B Instruct 2506 API example](https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/mistral-small-3-2/api.html) — NVIDIA; supports Exact source URL for mistralai-mistral-small-3-2-24b-instruct-2506-nim, NIM API usage evidence, OpenAI Chat Completion request example, serving documentation rather than retained quality benchmarks in the supplied findings
- [Llama 3.1 Nemotron Nano VL 8B V1](https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1) — NVIDIA; supports Exact source URL for nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim
- [Llama 3.1 Nemotron Nano VL 8B V1 model card](https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1/modelcard) — NVIDIA; supports document-intelligence VLM positioning, supported Image and Text inputs, English text input statement, use cases including OCR, summarization, and image Q&A, architecture names
- [NeMo Retriever Parse](https://build.nvidia.com/nvidia/nemoretriever-parse) — NVIDIA; supports Exact source URL for nvidia-nemoretriever-parse-nim
- [NeMo Retriever Parse model card](https://build.nvidia.com/nvidia/nemoretriever-parse/modelcard) — NVIDIA; supports general-purpose document text extraction description, formatted text with bounding boxes and semantic class output, demonstration-only/not intended for production statement, PDF and PPT extraction statement, RGB image input and text output description
- [Nemotron Nano 12B V2 VL model card](https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl/modelcard) — NVIDIA; supports Exact source URL for nvidia-nemotron-nano-12b-v2-vl-nim, commercial-ready statement, up to four document images at 1k x 2k, supported Image Video Text inputs, supported media formats, 128K input-plus-output token limit, reasoning OFF by default and no video reasoning support
- [Nemotron Parse](https://build.nvidia.com/nvidia/nemotron-parse) — NVIDIA; supports Exact source URL for nvidia-nemotron-parse-nim, exact in-scope source identity for the parse service
- [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) — Hugging Face / Qwen; supports Exact source URL for qwen-qwen2-5-vl-7b-instruct-vllm, official numeric benchmark facts for the exact checkpoint, usage/tooling notes from the official model page
- [Qwen/Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct) — Hugging Face / Qwen; supports Exact source URL for qwen-qwen3-vl-4b-instruct-vllm-cuda13, official usage-instructions evidence for the exact checkpoint
- [NVIDIA-Nemotron-Nano-12B-v2-VL-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16) — Hugging Face / NVIDIA; supports upstream-checkpoint benchmark numbers for Nemotron Nano 12B V2 VL, ChartQA and DocVQA scores, vision benchmark average and modality/task use cases

## Evidence gaps

- Evidence gap: The supplied findings do not provide a verified primary-source benchmark table for the exact Mistral Small 3.2 24B Instruct 2506 NIM candidate, so quality-based routing against the other exact candidates is unsupported.
- Evidence gap: The supplied findings do not provide matched head-to-head benchmark protocols across Fara-7B, Qwen2.5-VL-7B-Instruct, Qwen3-VL-4B-Instruct, Llama 3.1 Nemotron Nano VL 8B V1, and the Mistral Small 3.2 NIM candidate; direct ranking across these models is therefore protocol-incomplete.
- Evidence gap: The supplied findings include exact benchmark numbers for Qwen2.5-VL-7B-Instruct and NVIDIA Nemotron Nano 12B V2 VL, but they do not verify shared evaluation settings tightly enough to claim a fair cross-model winner on those tasks.
- Evidence gap: For qwen-qwen3-vl-4b-instruct-vllm-cuda13, the supplied findings confirm official usage instructions but do not provide retained exact benchmark numbers, context limit, or dataset-specific quality claims for the exact checkpoint.
- Evidence gap: For nvidia-nemotron-parse-nim, the supplied findings include only the exact source identity URL and no retained model-card facts or benchmark protocol for the exact source beyond its existence in scope.
- Evidence gap: The supplied findings do not identify a verified canonical benchmark dataset, split, and metric for exact comparison between nvidia-nemoretriever-parse-nim and nvidia-nemotron-parse-nim.
- Evidence gap: The supplied findings do not verify exact preprocessing, prompt template, output schema validation, or scoring procedure needed to compare parse-style services numerically against free-form VLM chat models.
- Evidence gap: The supplied findings mention NVIDIA Nemotron Nano 12B V2 VL benchmark scores through the upstream Hugging Face source, but those are upstream-checkpoint quality facts and should not be treated as NVIDIA NIM runtime-performance evidence.
- Evidence gap: The supplied findings do not provide exact benchmark numbers for microsoft-fara-7b-vllm-cuda13, nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim, or the exact Mistral NIM candidate under the same public benchmark protocol as Nemotron Nano 12B V2 VL or Qwen2.5-VL-7B-Instruct.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property datasetsVersions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property primaryCitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property datasetsVersions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property primaryCitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property datasetsVersions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property primaryCitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: unexpected property datasetsVersions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[3]: $.benchmarkTaxonomy[3]: unexpected property primaryCitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://featherless.ai/models/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl-bf16.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
