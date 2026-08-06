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

- Research key: `build-nvidia-com-nvidia-llama-3-1-nemotron-nano-vl-8b-v1-8525423fc4`
- Independent audit: `revised`
- Researched: `2026-07-23T21:48:29.078753+00:00`

This dossier covers the Forge family build-nvidia-com-nvidia-llama-3-1-nemotron-nano-vl-8b-v1-8525423fc4 mapped to the NVIDIA NIM-served identifier nvidia/llama-3.1-nemotron-nano-vl-8b-v1 and the upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1. Primary NVIDIA sources (NIM API reference, Build model card, NGC container, and NVIDIA-authored Hugging Face repository and explainability docs) consistently describe the artifact as an 8B-parameter vision-language model that accepts image, video, and text inputs and emits natural-language text. The checkpoint is documented with a 16,000 token combined input+output limit and explicit truncation behavior in the upstream explainability document; the NIM API examples document OpenAI-compatible chat-style access and image-before-text request ordering and supported image file formats (JPG/JPEG/PNG). Benchmark numeric values for the requested datasets (AI2D, ChartQA, DocVQA, OCRBench, OCRBench‑V2 EN/CN, Video‑MME) are not attributable in the primary findings to the exact upstream Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint; available numeric benchmark tables in the arXiv paper correspond to Nemotron Nano V2 VL (a different 12B model) and therefore are not verifiable as Llama-3.1 upstream-checkpoint results. Quantized-variant benchmarks (FP4-QAD) are present for a separate FP4-QAD checkpoint and are explicitly variant-scoped. Immutable revision identifiers and container/image digests for the exact Forge-served artifact were not found in the inspected primary sources.

## Identity

- Upstream name: Llama-3.1-Nemotron-Nano-VL-8B-V1
- Checkpoint/version: Llama-3.1-Nemotron-Nano-VL-8B-V1
- Immutable revision: not reported
- Parameter scale: 8B
- Architecture/head: Vision-language model; vision encoder CRadioV2-H (listed in NVIDIA-authored FP4/QAD and mcore pages) and language encoder Llama-3.1-8B-Instruct (listed in NVIDIA-authored FP4/QAD and mcore pages); decoder-only LLM head for text output (as described in NVIDIA-authored model pages).
- License: Model weights and model-card/license metadata: NVIDIA Community Model License with additional Llama 3.1 Community Model License information for the upstream checkpoint; Container and serving packaging: governed by the NVIDIA Software License Agreement and Product‑Specific Terms for NVIDIA AI Products (NGC container listing) — preserve this model-weight versus container/code-license distinction.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-mcore

## Selection

### Recommended

- **Interactive visual question answering and multimodal chat over images** — Primary NVIDIA NIM API reference, Build model card, NGC container listing, and NVIDIA-authored Hugging Face model card describe the model as a vision-language model accepting image and text inputs and list interactive image Q&A and multimodal chat among supported use cases.
  Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim / upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1
- **Document and image summarization** — NVIDIA primary sources for the checkpoint list image summarization and document-image summarization among intended uses.
  Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim / upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1
- **OCR and document understanding from image inputs** — Primary NVIDIA sources explicitly list optical character recognition and document‑intelligence use cases for this VL checkpoint.
  Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim / upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1, https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1

### Conditional

- **Video query and summarization** — Primary sources state the model supports single-image and video inference but do not provide task-specific validated video latency, length, or resolution limits for the exact Forge-served runtime; downstream validation of video sampling, frame limits, and latency is required before production use.
  Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim serving scope (upstream-checkpoint evidence for video support)
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://docs.nvidia.com/nemo-framework/user-guide/25.11/vlms/llama_nemotron_vl.html
- **Edge deployment on Jetson Orin or laptops (quantized AWQ/TinyChat)** — Primary documentation describes AWQ 4-bit quantization and TinyChat/edge deployment for quantized or deployment-specific variants; validate accuracy, memory, and latency for the chosen quantized runtime because these are variant- and hardware-scoped claims and not documented as measured for the exact Forge-served base checkpoint.
  Scope: Deployment note for the VL family; applies to separate quantized/edge variants (variant-scoped evidence) rather than the exact Forge-served base model
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://docs.nvidia.com/nemo-framework/user-guide/25.11/vlms/llama_nemotron_vl.html
- **Use of FP4-QAD quantized variant for lower-cost inference** — Applies only to the separately published FP4-QAD checkpoint; validate quality and runtime behavior before adoption because provided benchmarks and runtime notes are variant-scoped and hardware-scoped (FP4 quantization, vLLM, simulated evaluation on specific GPUs).
  Scope: Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD (upstream quantized variant) not the exact Forge-served base model
  Evidence: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD

### Avoid

- **Clinical diagnostic or regulated medical use** — Primary sources inspected for this checkpoint do not report clinical validation, regulatory approval, or medical‑use evaluation for the exact Forge-served artifact.
  Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim / upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1
- **Any task requiring documented calibrated confidence scores or probability-calibrated outputs** — Primary sources describe text-string outputs but do not report calibrated confidence semantics or probability-calibration procedures for this checkpoint.
  Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim / upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md

## Input preparation

### Semantic inputs

- The model accepts Image, Video, and Text inputs (NIM API reference documents image, video, and text support). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1
- The NVIDIA-authored Hugging Face model card describes the checkpoint as a document-intelligence vision-language model that can query and summarize images. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1

### Accepted formats

- Image input format must be RGB (explicitly stated in the FP4-QAD README and FP4-QAD model pages). Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD
- Supported image file formats include JPG, JPEG, and PNG (NIM VLM API example page documents supported upload formats). Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/llama-nemotron-nano/api.html
- Text input format is a string. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true

### Preprocessing

- Provide images as RGB inputs (primary FP4-QAD README and model pages specify RGB requirement). Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD
- Evidence gap: The inspected primary sources do not specify official image resizing dimensions, per-channel normalization constants, explicit video frame-sampling procedure (frame rates, fps defaults) or tiling algorithm parameters for the exact Forge-served Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint.

### Pre-submit validation

- Validate that image inputs are RGB and text inputs are strings before submission (stated in NIM API reference and model-card pages). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true
- Validate prompts against the documented 16,000 combined input+output token limit for this VL checkpoint (upstream explainability document states total context length is 16,000 and truncation behavior). Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true

### Task-specific formatting

- NIM API examples show OpenAI-compatible chat-completions access for the VL model family and recommend placing an image before any text in the request body for better results; the API supports passing image URLs or base64-encoded images. Sources: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/llama-nemotron-nano/api.html, https://docs.nvidia.com/nim/vision-language-models/1.3.0/examples/llama-nemotron-nano/api.html
- Evidence gap: The inspected primary sources do not specify an official OCR/document-extraction structured prompt template or a canonical paired-input ordering schema beyond the image-before-text recommendation in the NIM example pages.

## Output interpretation

### Outputs

- Output type is generated natural-language text (string) emitted by the model as the textual response to image/text/video-conditioned queries. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1

### Interpretation

- Interpret outputs as generated natural-language responses from a vision-language model conditioned on supplied image/video/text inputs; primary sources do not document calibrated confidence or probability scores for outputs. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1
- The upstream explainability document states total context length is 16,000 tokens and that overlength input is truncated from the start; confirm truncation did not affect critical results when using long contexts. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md

### Post-inference validation

- Post-inference, verify that outputs are grounded in the provided image or video because the explainability document warns the model may generate inaccurate, omitted, irrelevant, redundant, biased, toxic, political, or misleading text. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md
- Post-inference, confirm that truncation did not remove essential context when long contexts are used because the upstream explainability document states overlength input is truncated from the start. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md

## Public benchmarks

### AI2D

- Dataset/split: AI2D test / test
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (`higher-is-better`)
- Model scope: Not attributable to Llama-3.1-Nemotron-Nano-VL-8B-V1 in the inspected primary sources; the arXiv benchmark table reports AI2D scores for Nemotron Nano V2 VL (12B) only.
- Conditions: ArXiv table rows correspond to Nemotron Nano V2 VL (12B) and report multiple processing modes (tiling/native/tiling-size matching); the inspected primary sources do not provide a matching table row for the Llama-3.1 8B checkpoint.
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows)
- Caveat: Benchmark values in the arXiv table are for Nemotron Nano V2 VL (12B), not the Llama-3.1‑Nemotron‑Nano‑VL‑8B checkpoint; therefore AI2D numeric claims cannot be attributed to the 8B checkpoint from inspected primary sources.

### Chart question answering

- Dataset/split: ChartQA test / test
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (`higher-is-better`)
- Model scope: ArXiv benchmark table provides ChartQA numbers for Nemotron Nano V2 VL (12B) only; no matching ChartQA numeric row was found for the Llama-3.1 8B checkpoint in inspected primary sources.
- Conditions: ArXiv reports multiple processing modes for Nemotron Nano V2 VL; inspected primary sources do not provide checkpoint-scoped ChartQA numbers for Llama-3.1 8B.
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows)
- Caveat: Not attributable to the Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint in the inspected primary sources.

### Document visual question answering

- Dataset/split: DocVQA validation / validation
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (`higher-is-better`)
- Model scope: ArXiv benchmark table reports DocVQA validation numbers for Nemotron Nano V2 VL (12B); no DocVQA validation numeric row for Llama-3.1 8B was located in the inspected primary sources.
- Conditions: ArXiv rows correspond to Nemotron Nano V2 VL and multiple processing modes; inspected primary sources do not attribute a DocVQA validation score to the Llama-3.1 8B checkpoint.
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows)
- Caveat: Not attributable to the Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint in the inspected primary sources.

### OCR/document understanding

- Dataset/split: OCRBench test / test
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (see caveats) (`higher-is-better`)
- Model scope: ArXiv table reports OCRBench numbers for Nemotron Nano V2 VL (12B); FP4-QAD quantized variant publishes an OCRBench numeric value for the FP4-QAD checkpoint (variant-scoped evidence).
- Conditions: FP4-QAD OCRBench numeric evidence pertains to the separate FP4‑QAD quantized checkpoint and simulated/variant evaluation; arXiv numbers are for Nemotron Nano V2 VL (12B).
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows); see FP4‑QAD README for variant-scoped OCRBench numeric evidence
- Caveat: ArXiv OCRBench numbers are for Nemotron Nano V2 VL (12B) and cannot be attributed to Llama-3.1 8B based on inspected sources; FP4‑QAD README reports OCRBench=836 for the FP4‑QAD quantized variant (variant-scoped evidence).

### OCR/document understanding

- Dataset/split: OCRBench-V2 (EN) test / test
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (`higher-is-better`)
- Model scope: ArXiv reports OCRBench‑V2 (English) numbers for Nemotron Nano V2 VL (12B) only; inspected primary sources do not provide a matching numeric row for Llama-3.1 8B.
- Conditions: ArXiv benchmark table corresponds to Nemotron Nano V2 VL; no Llama-3.1 8B row found in inspected sources.
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows)
- Caveat: Not attributable to the Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint in inspected primary sources.

### OCR/document understanding

- Dataset/split: OCRBench-V2 (CN) test / test
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (`higher-is-better`)
- Model scope: ArXiv reports OCRBench‑V2 (Chinese) numbers for Nemotron Nano V2 VL (12B) only; no Llama-3.1 8B numeric row was located in inspected primary sources.
- Conditions: ArXiv benchmark table corresponds to Nemotron Nano V2 VL; no Llama-3.1 8B row found in inspected sources.
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows)
- Caveat: Not attributable to the Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint in inspected primary sources.

### Video understanding

- Dataset/split: Video-MME test / test
- Metric/value: score / not verifiable for Llama-3.1-Nemotron-Nano-VL-8B-V1 in inspected primary sources (`higher-is-better`)
- Model scope: ArXiv reports a Video‑MME score for Nemotron Nano V2 VL (12B); no matching Video‑MME numeric row for Llama-3.1 8B was located in the inspected primary sources.
- Conditions: ArXiv benchmark table corresponds to Nemotron Nano V2 VL; inspected primary sources do not attribute Video-MME numeric values to the Llama-3.1 8B checkpoint.
- Source: https://arxiv.org/html/2511.03929v1
- Locator: arXiv benchmark table (Nemotron Nano V2 VL rows)
- Caveat: Not attributable to the Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint in inspected primary sources.

### OCR/document understanding (quantized variant)

- Dataset/split: OCRBench test / test
- Metric/value: score / 836 (`higher-is-better`)
- Model scope: Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD (FP4 quantized variant) — variant-scoped upstream-checkpoint evidence
- Conditions: Reported for the FP4‑QAD quantized checkpoint; evaluation performed with FP4 simulated quantization on an H100 GPU and inference engine vLLM as documented in the FP4‑QAD pages (variant- and hardware-scoped).
- Source: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD
- Locator: FP4‑QAD README and evaluation notes
- Caveat: This numeric value is for the separately published FP4‑QAD quantized variant and is variant-scoped; it cannot be attributed to the exact Forge-served base checkpoint without additional primary evidence.

## Comparisons

### nvidia-llama-3-1-nemotron-nano-8b-v1-nim — `prefer-this`

- Task: Context-length and modality fit
- Criteria: Choose the VL model when image or video understanding is required; the text-only sibling documents a larger context length in its model card but does not provide visual-input modalities in the cited source.
- Rationale: NIM API reference and the VL model card document multimodal image/video/text acceptance for the VL checkpoint; the text-only Hugging Face model card documents a 128K context length but lacks VL input modalities in the inspected primary sources.
- Comparison conditions: Comparison is protocol- and capability-scoped: modality support (VL vs text-only) and reported context-length differences; not a benchmark head-to-head.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1

### nvidia-llama-3-1-nemotron-nano-vl-8b-v1-fp4-qad — `tradeoff`

- Task: Base precision versus quantized variant selection
- Criteria: FP4‑QAD quantized variant may reduce inference cost but is a separately published quantized checkpoint with variant-scoped evaluation and hardware-scoped testing conditions.
- Rationale: The FP4‑QAD README reports near-matching or variant-scoped benchmark values for several tasks under FP4 simulated quantization and documents deployment/runtime engine and hardware; these are not runtime-matched to the exact Forge-served base checkpoint and so represent a precision-versus-cost tradeoff.
- Comparison conditions: The FP4‑QAD evidence is for a separate quantized checkpoint evaluated under simulated FP4 quantization on specific GPUs with vLLM; not protocol-matched to the base 8B upstream checkpoint serving mode.
- Evidence: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD

## Limitations and safety

### Limitations

- Evidence gap: The research findings did not report an immutable upstream or container revision identifier (commit ID, checksum, or image digest) for the exact Forge-served artifact.
- Primary sources report distinct license scopes for model weights versus container/service packaging; a single undifferentiated license label would be misleading. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-vl-8b-v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true
- Evidence gap: Detailed official preprocessing rules such as image resizing dimensions, per-channel normalization constants, tiling algorithm parameters, and explicit video frame-sampling procedures for the exact Forge-served Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint were not specified in the inspected primary sources.
- The upstream explainability document documents a 16,000 token total context limit and states overlength input is truncated from the start, constraining long-context uses for this VL checkpoint. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md
- Benchmark numeric evidence available in the inspected primary sources is either for a different model (Nemotron Nano V2 VL 12B in the arXiv paper) or for separately published quantized variants (FP4‑QAD); therefore verified runtime-serving benchmarks for the exact Forge-served endpoint are not present in the inspected primary sources. Sources: https://arxiv.org/html/2511.03929v1, https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD

### Safety

- The upstream explainability document states the model may produce biased, toxic, incorrect, political, misleading, irrelevant, redundant, or omitted text and recommends human review for consequential outputs. Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md
- The explainability document warns the vLLM host should not be exposed to untrusted network connections (network-exposure warning). Sources: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md
- Forge policy: Do not use this checkpoint for sensitive personal, clinical, or regulated decisions without domain-specific review and deployment controls, because the inspected primary sources do not provide such validation.

## Related upstream agent skills

### `related-model-workflow`

NVIDIA's Nemotron customization skill is first-party guidance for curating, training, evaluating, converting, and optimizing Nemotron-family checkpoints in the Nemotron repository. It is not an inference payload or Nebius deployment contract; verify the exact listed checkpoint and use the Forge/Serverless instructions for serving.
- [nemotron-customize](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-customize)

## Primary sources

### NVIDIA NIM API reference: nvidia-llama-3_1-nemotron-nano-vl-8b-v1

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-nano-vl-8b-v1
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM API reference for the exact served model scope, supporting identity, modalities, token limit mention in NIM docs and API usage examples.
- Scope: nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim serving scope
- Supports: identity
- Supports: inputPreparation
- Supports: taskSpecificFormatting
- Supports: recommendedUseCases
- Supports: avoidUseCases

### Build NVIDIA model card: llama-3.1-nemotron-nano-vl-8b-v1

- URL: https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official Build NVIDIA model card for the exact model family, supporting intended-use phrasing and checkpoint description.
- Scope: Llama-3.1-Nemotron-Nano-VL-8B-V1
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: identity

### NGC container listing: llama-3.1-nemotron-nano-vl-8b-v1

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-vl-8b-v1
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: NGC container listing for the exact VL NIM container, supporting packaging/license scope and intended use descriptions.
- Scope: NIM container for Llama-3.1-Nemotron-Nano-VL-8B-V1
- Supports: identity
- Supports: license
- Supports: recommendedUseCases

### Hugging Face model card: Llama-3.1-Nemotron-Nano-VL-8B-V1

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1
- Publisher: NVIDIA on Hugging Face
- Type: `model-card`
- Primary because: NVIDIA-authored upstream checkpoint page for the VL model, supporting identity, modalities, and intended uses.
- Scope: Upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1
- Supports: identity
- Supports: recommendedUseCases
- Supports: inputPreparation
- Supports: outputInterpretation

### Hugging Face explainability/safety: Llama-3.1-Nemotron-Nano-VL-8B-V1 explainability.md

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/explainability.md
- Publisher: NVIDIA on Hugging Face
- Type: `repository`
- Primary because: Upstream checkpoint explainability and safety document for the exact checkpoint, supporting token-limit behavior and safety caveats.
- Scope: Upstream checkpoint Llama-3.1-Nemotron-Nano-VL-8B-V1 explainability/safety
- Supports: inputPreparation.validation
- Supports: outputInterpretation
- Supports: limitations
- Supports: safety

### Hugging Face FP4-QAD README (download) for Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD/resolve/main/README.md?download=true
- Publisher: NVIDIA on Hugging Face
- Type: `repository`
- Primary because: Upstream checkpoint README for the FP4‑QAD quantized variant demonstrating variant-scoped licensing, inputs, RGB requirement, token limit, and variant benchmark notes.
- Scope: Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD (quantized variant)
- Supports: conditionalUseCases
- Supports: comparisons
- Supports: inputPreparation
- Supports: benchmarks
- Supports: license

### Hugging Face FP4-QAD model page: Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD
- Publisher: NVIDIA on Hugging Face
- Type: `repository`
- Primary because: FP4‑QAD quantized variant page with evaluation benchmarks and model metadata.
- Scope: Llama-3.1-Nemotron-Nano-VL-8B-V1-FP4-QAD
- Supports: benchmarks
- Supports: inputPreparation
- Supports: comparisons

### ArXiv HTML: Nemotron Nano V2 VL (benchmark table)

- URL: https://arxiv.org/html/2511.03929v1
- Publisher: NVIDIA Research authors / arXiv
- Type: `paper`
- Primary because: Canonical authored benchmark table source in the inspected primary findings; however, reported numeric rows in this paper correspond to Nemotron Nano V2 VL (12B) rather than the Llama-3.1 8B checkpoint.
- Scope: Nemotron Nano V2 VL (12B) benchmark table
- Supports: benchmarks
- Supports: researchSummary
- Supports: limitations

### NIM VLM API example page 1.3.1: llama-nemotron-nano API example

- URL: https://docs.nvidia.com/nim/vision-language-models/1.3.1/examples/llama-nemotron-nano/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM API example showing request format, image-before-text ordering recommendation, supported image formats, and OpenAI-compatible chat-style access.
- Scope: nvidia/llama-3.1-nemotron-nano-vl-8b-v1 NIM example
- Supports: inputPreparation.acceptedFormats
- Supports: taskSpecificFormatting

### NIM VLM API example page 1.3.0: llama-nemotron-nano API example

- URL: https://docs.nvidia.com/nim/vision-language-models/1.3.0/examples/llama-nemotron-nano/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Additional NIM example page referenced in the inspected findings documenting API usage and example requests for the VL family.
- Scope: nvidia/llama-3.1-nemotron-nano-vl-8b-v1 NIM example
- Supports: taskSpecificFormatting
- Supports: inputPreparation

### NeMo framework VLM documentation: llama_nemotron_vl

- URL: https://docs.nvidia.com/nemo-framework/user-guide/25.11/vlms/llama_nemotron_vl.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NeMo documentation describing training and deployment notes for the Nemotron Nano VL family, supporting deployment and training-stage notes.
- Scope: NeMo Nemotron Nano VL family documentation
- Supports: conditionalUseCases
- Supports: inputPreparation
- Supports: researchSummary

### Hugging Face mcore/metadata page for Llama-3.1-Nemotron-Nano-VL-8B-V1-mcore

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1-mcore
- Publisher: NVIDIA on Hugging Face
- Type: `repository`
- Primary because: Repository metadata listing vision-encoder and language-encoder names and other checkpoint metadata referenced in the inspected findings.
- Scope: Upstream checkpoint metadata for Llama-3.1-Nemotron-Nano-VL-8B-V1
- Supports: identity.architecture
- Supports: recommendedUseCases

### Hugging Face model card: Llama-3.1-Nemotron-Nano-8B-v1 (text-only sibling)

- URL: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1
- Publisher: NVIDIA on Hugging Face
- Type: `model-card`
- Primary because: Upstream checkpoint page for the text-only sibling model used in scoped comparison (context-length claim present in inspected findings).
- Scope: Llama-3.1-Nemotron-Nano-8B-v1 (text-only sibling)
- Supports: comparisons
- Supports: identity

## Evidence gaps

- Evidence gap: Immutable revision identifiers (commit ID, checksum, container/image digest) for the exact Forge-served artifact were not found in the inspected primary sources.
- Evidence gap: Official detailed preprocessing parameters (image resizing dimensions, per-channel normalization constants, tiling algorithm parameters, frame-sampling/fps defaults) for the exact Forge-served Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint were not specified in the inspected primary sources.
- Evidence gap: An official checkpoint-specific OCR/document-extraction structured prompt template or canonical paired-input ordering beyond the NIM image-before-text recommendation was not found in the inspected primary sources.
- Evidence gap: Verified numeric benchmark rows for AI2D, ChartQA, DocVQA, OCRBench, OCRBench‑V2 (EN/CN), and Video‑MME attributable to the exact Llama-3.1-Nemotron-Nano-VL-8B-V1 checkpoint were not found in the inspected primary sources; arXiv benchmark tables correspond to Nemotron Nano V2 VL (12B) and FP4‑QAD numbers correspond to a separate quantized variant.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://developer.nvidia.com/blog/new-nvidia-llama-nemotron-nano-vision-language-model-tops-ocr-benchmark-for-accuracy Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary URL https: $.sources[9] uses forbidden secondary URL https://developer.nvidia.com/blog/turn-complex-documents-into-usable-data-with-vlm-nvidia-nemotron-parse-1-1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemotron-parse Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].value must contain a reported numeric result: $.benchmarks[0].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
