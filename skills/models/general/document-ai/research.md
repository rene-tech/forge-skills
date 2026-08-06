# Document Ai model selection

- Category: `general`
- Group: `document-ai`
- Independent audit: `revised`
- Researched: `2026-07-23T20:04:17.260859+00:00`

Evidence gap: The provided research findings contain no primary-source definitions for a canonical 'document-ai' task family. Intended scope (not verified in findings): selection among models for document-AI pipelines covering long-document understanding, document image QA (DocVQA-style), structured extraction (entity/table/key-value/JSON), and RAG/tooling workflows. The research did not locate authoritative primary-source definitions or a single canonical task specification in the findings; therefore every concrete task requirement (input modality details, exact output schema, context-window requirements, and evaluation protocol) must be sourced from primary documentation or recorded as an evidence gap.

## Questions to answer before selecting

- What input modality is expected (text, image, or multimodal document inputs) and what is the document format (PDFs, scanned images, OCR requirements)?
- What is the required context window (tokens/pages) to retain per document for the intended use-case?
- Is structured JSON output required (and if so what exact schema), or is free-form text acceptable?
- Are DocVQA-style visual question-answering capabilities required over document images, including table/figure reasoning?
- Is multi-language support required and which specific languages must be supported?
- Is retrieval-augmented generation (RAG) or external tool/function calling required?
- Are there licensing, on-premises deployment, or data-sensitivity constraints that would disqualify licenses like Apache-2.0, MIT, or other terms?
- What latency, throughput, and hardware constraints (GPU model, memory, runtime) apply to model selection?

## Comparability rules

- Evidence gap: The research findings do not include primary-source, protocol-level comparability rules. Recommended comparability rules (require primary-source validation before use): identical dataset+split, identical image preprocessing/OCR pipeline, identical prompt templates and temperature/decoding settings, identical evaluation metric definitions and normalization, and identical model variant (weights/checkpoint/precision) used for each reported result.
- Evidence gap: No primary-source specification for normalizing results across different context-window sizes was found in the findings; comparisons across context sizes must be treated as incomparable unless a primary source documents an explicit normalization or matched evaluation protocol.
- Evidence gap: The research did not locate primary-source guidance on whether results produced by a serving/runtime (NIM, CUDA runtime, or wrapper) correspond exactly to upstream-checkpoint results; any such comparison must be supported by documentation linking the runtime to the unchanged upstream checkpoint.

## Conditional routing

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: allenai-olmo-2-1124-7b-instruct-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: bytedance-seed-oss-36b-instruct-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: huggingfacetb-smollm3-3b-vllm
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: ibm-granite-granite-3-3-8b-instruct-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: ibm-granite-granite-4-1-8b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate or its serving runtime

- Why: Evidence gap: The research findings do not contain primary-source evidence linking the serving/runtime to an unchanged upstream checkpoint or documenting the candidate's claimed properties.
- Alternative: microsoft-phi-4-mini-instruct-nim
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: mistralai-devstral-small-2507-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: openbmb-minicpm4-8b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: openbmb-minicpm5-1b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: qwen-qwen3-0-6b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: qwen-qwen3-1-7b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: qwen-qwen3-14b-vllm
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: qwen-qwen3-14b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Specific claims about MoE, FP8, or coder-head behavior are required but no primary-source checkpoint-level evidence is available in the findings for this exact variant

- Why: Evidence gap: The research findings do not include the canonical primary-source documentation for the exact slug/variant or serving artifact; cannot verify MoE/FP8/coder-head claims from findings.
- Alternative: qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when Default selection when no primary-source, checkpoint-level evidence is available in the findings for the candidate

- Why: Evidence gap: The research findings do not contain primary-source evidence that would support preferring this candidate for the stated condition.
- Alternative: qwen-qwen3-8b-vllm-cuda13
- Evidence:

### Prefer `insufficient-evidence` when When a coder-focused, MoE, or FP8 quantized variant is cited but no canonical primary URL for the exact variant exists in the findings

- Why: Evidence gap: The findings do not include a primary-source locator for the exact Qwen3-Coder-30B-A3B-Instruct variant named in the draft; decision evidence cannot be validated from the findings.
- Alternative: qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm
- Evidence:

## Benchmark taxonomy

### Document-VQA on document images (DocVQA)

- Datasets: DocVQA
- Metrics: Evidence gap: The research findings do not contain primary-source metric names or values for DocVQA for any candidate; no verified metric table/figure/section was present in findings.
- Compare only when: Evidence gap: The research findings do not contain a primary-source, reproduced evaluation protocol (dataset split, image preprocessing/OCR, prompt templates, answer normalization) required to compare DocVQA results across candidates.

### Long-context document summarization

- Datasets: Evidence gap: No canonical long-document summarization dataset/split was identified in the findings for these candidates
- Metrics: Evidence gap: The research findings do not include verified primary-source summarization metrics (e.g., ROUGE/BLEU/QA-based measures) tied to exact checkpoints/variants.
- Compare only when: Evidence gap: The research findings do not include primary-source protocol details for long-context summarization (context-window matching, prompt templates, truncation/paging, pooling/normalization) necessary for valid cross-model comparisons.

## Primary sources

- [Exact official starting source declared by Forge](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/ibm-granite/granite-4.1-8b) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/microsoft/phi-4-mini-instruct/deploy) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/mistralai/Devstral-Small-2507) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/openbmb/MiniCPM4-8B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/openbmb/MiniCPM5-1B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-0.6B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-1.7B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-14B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-8B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The research findings did not include any primary-source URLs or documents for any of the candidate slugs; no model-card, vendor page, official checkpoint repository, or canonical paper was present in the findings.
- Evidence gap: No primary-source model-card or vendor documentation was found in the findings for Qwen3-Coder-30B-A3B-Instruct (the draft cited two external URLs that are not present in the research findings).
- Evidence gap: There is no primary-source, checkpoint-level documentation in the findings for MoE/FP8/coder-head claims for the Qwen variants; cannot verify parameter counts, MoE topology, or FP8/quantized serving claims from the findings.
- Evidence gap: The findings do not contain verified numeric benchmarks, tables, figures, or metric values for DocVQA or long-context summarization tied to exact checkpoints/variants; head-to-head comparisons are not supported by the findings.
- Evidence gap: The research findings contain no documentation of exact context-window claims (e.g., 32K, 128K, 131K, 512K) tied to exact checkpoint variants; context-window verification is not possible from the findings.
- Evidence gap: The research findings do not include exact license texts or license identifiers for the listed candidates; license verification per checkpoint/variant is not possible from the findings.
- Evidence gap: The research findings contain no primary-source descriptions of input preprocessing, prompt templates, output shape (JSON schema), pooling/normalization, or evaluation code for any benchmark; these must be requested from model authors or located in canonical sources.
- Evidence gap: No primary-source evidence in the findings ties any serving/runtime (NIM, OpenRouter, CUDA runtime) to an unchanged upstream checkpoint; serving-vs-upstream provenance cannot be established from the findings.
- Evidence gap: No head-to-head evaluation across the candidate set on an identical document-AI task (DocVQA, long-context summarization, or structured extraction) was present in the findings.
- Evidence gap: For every candidate slug listed in the expected scope, the research findings did not provide the canonical model-card URL, repository URL, or vendor documentation required to populate the top-level sources list.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://featherless.ai/models/Qwen/Qwen3-Coder-30B-A3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/HuggingFaceTB/SmolLM3-3B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/ibm-granite/granite-3.3-8b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/ibm-granite/granite-4.1-8b: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/microsoft/phi-4-mini-instruct/deploy: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/mistralai/Devstral-Small-2507: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/openbmb/MiniCPM4-8B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/openbmb/MiniCPM5-1B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-0.6B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-1.7B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-14B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-8B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
