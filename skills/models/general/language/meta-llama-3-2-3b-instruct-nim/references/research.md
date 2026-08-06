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

- Research key: `build-nvidia-com-meta-llama-3-2-3b-instruct-67d2640330`
- Independent audit: `revised`
- Researched: `2026-07-23T22:20:31.413956+00:00`

Primary-source evidence shows an upstream Meta Llama 3.2 instruction‑tuned 3B checkpoint (meta-llama/Llama-3.2-3B-Instruct) and an NVIDIA-packaged AWQ INT4 -> ONNX artifact published on NGC for the 3B Instruct variant. Upstream documentation and README (Hugging Face) describe intended uses such as multilingual instruction-following and assistant-like chat; NVIDIA NGC and build.nvidia.com pages describe the NGC artifact as quantized to AWQ INT4 via AutoAWQ and converted to ONNX for RTX GPUs. Primary sources inspected do not publish an immutable upstream checkpoint revision/hash that maps the exact Forge build key to a specific upstream revision, do not publish a Forge-build-scoped packaged tokenizer filename/path for the NVIDIA AWQ INT4 ONNX artifact, and do not publish protocol-matched numeric benchmarks for the NVIDIA-packaged AWQ INT4 ONNX artifact that would allow direct numeric parity comparisons with upstream checkpoint benchmarks.

## Identity

- Upstream name: meta-llama/Llama-3.2-3B-Instruct
- Checkpoint/version: meta-llama/Llama-3.2-3B-Instruct
- Immutable revision: not reported
- Parameter scale: 3B
- Architecture/head: auto-regressive transformer; instruction-tuned (instruction‑tuned generative 3B variant)
- License: Llama 3.2 Community License
- Evidence: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md, https://ai.meta.com/static-resource/sept-responsible-use-guide, https://build.nvidia.com/meta/llama-3.2-3b-instruct

## Selection

### Recommended

- **Multilingual instruction-following dialogue and assistant-like chat** — Upstream Hugging Face README documents instruction-tuned intended uses including assistant-like chat, multilingual instruction-following, summarization and related NLG tasks; NVIDIA NGC and build.nvidia.com model pages describe the packaged 3B Instruct variant as optimized for multilingual dialogue and assistant-like tasks.
  Scope: meta-llama/Llama-3.2-3B-Instruct (upstream-checkpoint evidence) and meta-llama-3.2-3b-onnx-int4-rtx (NVIDIA-packaged AWQ INT4 ONNX artifact)
  Evidence: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://build.nvidia.com/meta/llama-3.2-3b-instruct

### Conditional

- **Constrained/quantized edge deployment using NVIDIA AWQ INT4 ONNX artifact** — Requires explicit application- and hardware-specific quality/regression validation on the target RTX hardware; treat upstream checkpoint numeric benchmarks as upstream-checkpoint evidence and re-run application-specific evaluation for the NVIDIA AWQ INT4 ONNX artifact prior to production.
  Scope: meta-llama-3.2-3b-onnx-int4-rtx (NVIDIA-packaged AWQ INT4 ONNX artifact)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx
- **Retrieval-augmented pipelines (knowledge retrieval + summarization)** — Validate retrieval, prompt-handling, and safety on the target serving stack; re-run evaluation for the quantized NVIDIA artifact before deployment and treat upstream numeric benchmarks as upstream-checkpoint evidence.
  Scope: meta-llama/Llama-3.2-3B-Instruct (upstream-checkpoint evidence) and meta-llama-3.2-3b-onnx-int4-rtx (NVIDIA-packaged artifact)
  Evidence: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx

### Avoid

- **Embedding generation or non-text modalities without explicit packaging/support** — Neither the upstream model-card nor the NVIDIA-packaged artifact document embeddings or non-text modality support for the inspected 3B Instruct variant; supported types are documented as text (and code as strings where noted).
  Scope: meta-llama-3.2-3b-instruct (NVIDIA-packaged artifact and upstream model-card evidence)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- **Deployments that violate the Llama 3.2 Community License or Acceptable Use Policy** — Upstream license and use-policy require compliance and contain restrictions; deployments violating those terms are disallowed by upstream governance.
  Scope: meta-llama/Llama-3.2-3B-Instruct (upstream license/use-policy)
  Evidence: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md

## Input preparation

### Semantic inputs

- Textual inputs (natural language and code) supplied as strings. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nvigisdk/models/llama-3.2-3b

### Accepted formats

- Accepted input format: string (text and code as strings) as documented for NVIDIA-packaged artifacts and SDK pages. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nvigisdk/models/llama-3.2-3b

### Preprocessing

- Evidence gap: No authoritative primary-source locator was found in the inspected canonical sources that publishes a tokenizer artifact filename/path or packaged tokenizer shipped with the NVIDIA AWQ INT4 ONNX artifact. Sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx

### Pre-submit validation

- Upstream and packaging documentation recommend safety testing and application-specific validation prior to production deployment. Sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx

### Task-specific formatting

- Evidence gap: No authoritative Forge-build-scoped prompt-formatting templates or exact prompt protocol for the NVIDIA-packaged artifact were found in the inspected primary sources. Sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://build.nvidia.com/meta/llama-3.2-3b-instruct

## Output interpretation

### Outputs

- Outputs are textual strings (natural language; code strings also documented as supported). Sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx

### Interpretation

- Numeric confidence/calibration semantics are not comprehensively specified in the inspected primary sources for the NVIDIA-packaged AWQ INT4 ONNX artifact; treat numeric outputs as uncalibrated unless downstream calibration is performed. Sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

### Post-inference validation

- Post-inference safety checks and application-specific validation are recommended by upstream Meta materials and NVIDIA packaging notes prior to production use. Sources: https://ai.meta.com/static-resource/sept-responsible-use-guide, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx

## Public benchmarks

### MMLU (multitask knowledge / closed-book QA)

- Dataset/split: MMLU (macro-average) / not reported
- Metric/value: accuracy (macro-average) / 63.4% (`higher-is-better`)
- Model scope: 3B upstream checkpoint (as reported on NVIDIA NIM reference)
- Conditions: Reported on NVIDIA NIM reference for Llama-3.2-3B-Instruct; protocol details beyond dataset name and reported metric not enumerated in the inspected locator.
- Source: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-3b-instruct
- Locator: NIM reference page (benchmark listings)
- Caveat: Result is reported on the NIM reference for the upstream 3B checkpoint; the NVIDIA-packaged AWQ INT4 ONNX artifact on NGC does not have protocol-matched numeric benchmark data published in the inspected sources.

### Instruction-following accuracy (IFEval)

- Dataset/split: IFEval (instruction-following) / not reported
- Metric/value: accuracy / 77.4% (`higher-is-better`)
- Model scope: 3B upstream checkpoint (as reported on NVIDIA NIM reference)
- Conditions: Reported on NVIDIA NIM reference for Llama-3.2-3B-Instruct.
- Source: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-3b-instruct
- Locator: NIM reference page (benchmark listings)
- Caveat: Upstream-checkpoint evidence; does not demonstrate performance for the NVIDIA AWQ INT4 ONNX artifact without protocol-matched evaluation.

### AGIEval (English average)

- Dataset/split: AGIEval / not reported
- Metric/value: accuracy / 39.2% (`higher-is-better`)
- Model scope: 3B upstream checkpoint (as reported on NVIDIA NIM reference / upstream README where enumerated)
- Conditions: Reported on upstream README and/or NIM reference; inspected primary locator lists the value but does not provide a precision or packaging label tied to a quantized NGC artifact.
- Source: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-3b-instruct
- Locator: NIM reference page (benchmark listings) and upstream README where enumerated
- Caveat: Upstream-checkpoint evidence; no matching protocol reported for NVIDIA AWQ INT4 ONNX artifact in inspected sources.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: multitask knowledge/closed-book QA (MMLU)
- Criteria: Protocol-matched comparison requires identical dataset, split, prompt protocol, and precision/packaging across both sides; inspected sources do not publish a protocol-matched benchmark for the NVIDIA AWQ INT4 ONNX artifact to compare against upstream numeric results.
- Rationale: Upstream numeric benchmarks for the 3B checkpoint are present on the NVIDIA NIM reference and upstream README, but the NGC catalog entry for the AWQ INT4 ONNX artifact does not include matching-protocol numeric evaluations in the inspected primary sources.
- Comparison conditions: Upstream numbers listed on NIM reference/README are checkpoint-level; NGC artifact is quantized AWQ INT4 -> ONNX. No same-precision, same-protocol results for the NGC artifact were found.
- Evidence: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-3b-instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

## Limitations and safety

### Limitations

- Evidence gap: Exact immutable upstream checkpoint revision or hash mapping the Forge build key build-nvidia-com-meta-llama-3-2-3b-instruct-67d2640330 to a specific upstream revision is not present in the inspected primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- Upstream numeric benchmarks reported on the NIM reference and upstream README are scoped to upstream checkpoints and must be treated as upstream-checkpoint evidence when cited for a packaged/quantized NVIDIA artifact. Sources: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-3b-instruct, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- Evidence gap: No authoritative primary-source locator for a tokenizer artifact filename/path or an authoritative Forge-build-scoped tokenizer provenance statement for the NVIDIA-packaged AWQ INT4 ONNX artifact was present in the inspected primary sources. Sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx
- Evidence gap: No NVIDIA-packaged AWQ INT4 ONNX/TensorRT runtime latency, throughput, or context-length performance numbers for the exact Forge build key were published in the inspected primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://build.nvidia.com/meta/llama-3.2-3b-instruct

### Safety

- Evidence gap: Forge-specific safety implementation details for the exact NVIDIA-packaged build (build-nvidia-com-meta-llama-3-2-3b-instruct-67d2640330) are not described in the inspected primary sources; downstream validation and implementation-specific safety controls are recommended prior to deployment. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- Upstream license governance: Model use is governed by the Llama 3.2 Community License; distributed copies must include required attribution and comply with the Acceptable Use Policy referenced by upstream. Sources: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md
- Responsible-use recommendation: Meta's Responsible Use Guide advises prompt engineering, input-level mitigation, and deployment risk assessment; apply jurisdictional and internal legal/risk review for deployments. Sources: https://ai.meta.com/static-resource/sept-responsible-use-guide

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/meta/llama-3.2-3b-instruct
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: Forge-declared official starting source for the covered serving variant; prototype access examples and model descriptions.
- Scope: meta-llama-3-2-3b-instruct
- Supports: Forge-to-upstream exact-version identity
- Supports: prototype access examples

### NVIDIA build modelcard (modelcard)

- URL: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: NVIDIA-hosted modelcard describing the Meta Llama 3.2 3B Instruct family and intended uses.
- Scope: meta-llama-3-2-3b-instruct
- Supports: instruction-tuned model description
- Supports: intended uses and optimization notes

### NGC catalog: meta-llama-3.2-3b-onnx-int4-rtx

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA catalog entry documenting the AWQ INT4 -> ONNX packaged artifact and packaging notes.
- Scope: meta-llama-3.2-3b-onnx-int4-rtx (NVIDIA-packaged AWQ INT4 ONNX artifact)
- Supports: artifact packaging (AWQ INT4 -> ONNX via AutoAWQ / Onnxruntime-GenAI)
- Supports: supported input/output types (text and code strings)
- Supports: artifact readiness statements

### NGC TensorRT Model Optimizer page for the NGC artifact

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/meta-llama3.2-3b-instruct-onnx-int4-rtx-tensorrt-model-optimizer
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA TensorRT Model Optimizer documentation describing the model as an auto-regressive language model using an optimized transformer architecture.
- Scope: meta-llama-3.2-3b-onnx-int4-rtx (TensorRT optimization context)
- Supports: architecture description
- Supports: runtime optimization notes

### NGC file browser for meta-llama-3.2-3b-onnx-int4-rtx v1.0

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/-/models/meta-llama-3.2-3b-onnx-int4-rtx/1.0/file-browser
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NGC file browser listing packaged artifact files and included license/notice texts.
- Scope: meta-llama-3.2-3b-onnx-int4-rtx v1.0
- Supports: packaged file listings (license, readme, notices, third_party_licenses)

### NGC IGI SDK model page (supported input/output types and languages)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nvigisdk/models/llama-3.2-3b
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NGC SDK model page listing supported input type, input format, official supported languages, and output format for an NVIDIA-served variant.
- Scope: Llama 3.2 3B (NGC IGI SDK listing)
- Supports: supported input type: Text (string)
- Supports: officially supported languages
- Supports: supported output format: Text (string)

### Hugging Face model card: Llama-3.2-3B-Instruct

- URL: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Canonical upstream model-card/landing page reporting checkpoint descriptions, intended uses, and loading guidance for the upstream checkpoint.
- Scope: meta-llama/Llama-3.2-3B-Instruct (upstream-checkpoint)
- Supports: intended uses (instruction-following, assistant-like chat)
- Supports: loading guidance and example pipeline (torch_dtype hints)
- Supports: release and checkpoint download instructions

### Hugging Face README for Llama-3.2-3B-Instruct (README.md)

- URL: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md
- Publisher: Hugging Face (upstream model repository)
- Type: `repository`
- Primary because: Upstream README enumerates intended uses and additional details referenced by the model-card.
- Scope: meta-llama/Llama-3.2-3B-Instruct (upstream README)
- Supports: intended uses and benchmark listings (where enumerated)
- Supports: release date and usage notes

### NVIDIA NIM reference: meta-llama-3_2-3b-instruct

- URL: https://docs.api.nvidia.com/nim/reference/meta-llama-3_2-3b-instruct
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NIM reference page providing numeric benchmark listings and other model evaluation metrics for Llama-3.2-3B-Instruct as reported by NVIDIA documentation.
- Scope: meta-llama/Llama-3.2-3B-Instruct (benchmark/evaluation listings)
- Supports: numeric benchmark values (MMLU, IFEval, GSM8K, etc.) as reported on the NIM reference

### Llama 3.2 Community License (LICENSE file)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE
- Publisher: Meta
- Type: `repository`
- Primary because: Canonical upstream license text used to verify license terms and governance for Llama 3.2 materials.
- Scope: Llama 3.2 Community License (llama3_2/LICENSE)
- Supports: license text and commercial governance clauses

### Llama 3.2 Acceptable Use Policy (USE_POLICY.md)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md
- Publisher: Meta
- Type: `repository`
- Primary because: Canonical upstream acceptable-use policy used for safety and deployment guidance.
- Scope: Llama 3.2 Acceptable Use Policy
- Supports: use-policy restrictions and scope

### Meta Responsible Use Guide (Llama 3.2)

- URL: https://ai.meta.com/static-resource/sept-responsible-use-guide
- Publisher: Meta
- Type: `official-documentation`
- Primary because: Official responsible-use guidance published by Meta that outlines deployment, safety, and risk assessment recommendations.
- Scope: Responsible Use Guide for Llama 3.2
- Supports: responsible-use recommendations and deployment risk assessment guidance

## Evidence gaps

- Evidence gap: Exact immutable upstream checkpoint revision or hash mapping the Forge build key build-nvidia-com-meta-llama-3-2-3b-instruct-67d2640330 to an upstream revision is not present in the inspected primary sources.
- Evidence gap: No authoritative primary-source locator for a tokenizer artifact filename/path or packaged tokenizer shipped with the NVIDIA AWQ INT4 ONNX artifact was present in the inspected primary sources.
- Evidence gap: No protocol-matched numeric benchmarks for the NVIDIA AWQ INT4 ONNX packaged artifact were published in the inspected primary sources; thus direct numeric comparisons with upstream checkpoint benchmarks are unsupported by the inspected evidence.
- Evidence gap: No NVIDIA-packaged AWQ INT4 ONNX/TensorRT runtime latency, throughput, or exact context-length performance numbers for the exact Forge build key were published in the inspected primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 57 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA: $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/large-language-models/1.10.0/models.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/benchmarking/llm/latest/performance.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/unsloth/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/meta-llama/llama3/blob/main/llama/tokenizer.py Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/discussions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.meta.com/static-resource/sept-responsible-use-guide Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/unsloth/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://community.sambanova.ai/t/context-length-for-the-meta-llama-3-1-405b-instruct-is-too-small/184 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/large-language-models/1.10.0/models.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/meta-llama/llama3/blob/main/llama/tokenizer.py Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://paddlenlp.readthedocs.io/en/latest/_static/website/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/discussions Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/meta-llama-3.2-3b-onnx-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/bigcode/starcoder2-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/unsloth/Llama-3.2-3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://community.sambanova.ai/t/context-length-for-the-meta-llama-3-1-405b-instruct-is-too-small/184 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/benchmarking/llm/latest/performance.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/large-language-models/1.10.0/models.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/large-language-models/1.10.0/models.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
