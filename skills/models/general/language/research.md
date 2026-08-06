# Language model selection

- Category: `general`
- Group: `language`
- Independent audit: `revised`
- Researched: `2026-07-23T21:36:29.582329+00:00`

Group-level remit: define and compare exact Forge-served general-language checkpoints (instruction-following, code-generation, safety evaluations) only when primary-source canonical evidence for the exact named checkpoint/packaging exists. The available research findings include a single primary source (NVIDIA NIM reference for z-ai / glm4.7). The provided findings do not contain primary-source evidence for any of the Forge candidate slugs listed in the expected scope; therefore this dossier documents taxonomy and routing intent but cannot verify or ascribe checkpoint-scoped claims (architecture, packaging, benchmarks, datasets, licenses, or instruction-tuning regimes) for those slugs. Any claim about a listed Forge candidate that is not directly supported by the single provided source is an evidence gap and is recorded in evidenceGaps.

## Questions to answer before selecting

- Do you require built-in Nemoguard-style safety or topic-control safety (Yes/No)?
- Is Apache-2.0 or MIT licensing a requirement (specify preference)?
- Is explicit code-generation capability (The Stack v2 provenance) required (Yes/No)?
- Is long-context support required (e.g., >64k tokens) (Yes/No)?
- Do you require NVIDIA NIM packaging or other specific serving formats (Yes/No)?
- Is multilingual capability outside English required (Yes/No)?
- Is a specific parameter scale (e.g., 7B, 70B) required (specify)?

## Comparability rules

- Results are comparable only when the primary-source evaluation protocol for each model matches exactly on: dataset name and version, prompt templates, input shapes/context window, decoding settings (sampling/temperature/top-k/top-p/beam size), and any post-processing or scoring conventions.
- If primary sources report differing evaluation protocols (even for the same dataset name), treat cross-model numeric comparisons as an evidence gap.
- Benchmarks that depend on downstream heads, attached classifiers, or special serving wrappers are not comparable to callable Forge slugs unless the primary source documents the callable slug producing that result.

## Conditional routing

### Prefer `insufficient-evidence` when Default routing for general use-cases across all provided Forge slugs

- Why: Evidence gap: The provided research findings contain only a single NVIDIA NIM reference for an unrelated model (z-ai / glm4.7). No primary-source evidence for any of the listed Forge candidate slugs exists in the available findings; therefore there is insufficient primary evidence to deterministically prefer any single Forge slug for general routing.
- Alternative: allenai-olmo-2-0425-1b-instruct-vllm-cuda13
- Alternative: allenai-olmo-3-7b-instruct-vllm-cuda13
- Alternative: bigcode-starcoder2-7b-nim
- Alternative: huggingfacetb-smollm3-3b-vllm-cuda13
- Alternative: meta-llama-3-1-8b-instruct-nim
- Alternative: meta-llama-3-2-1b-instruct-nim
- Alternative: meta-llama-3-2-3b-instruct-nim
- Alternative: meta-llama-3.1-70b-instruct-v1
- Alternative: microsoft-phi-3-mini-4k-instruct-nim
- Alternative: microsoft-phi-4-mini-reasoning-vllm-cuda13
- Alternative: mistralai-ministral-3-3b-instruct-2512-vllm-cuda13
- Alternative: mistralai-mistral-7b-instruct-v0-3-nim
- Alternative: nvidia-llama-3-1-nemoguard-8b-content-safety-nim
- Alternative: nvidia-llama-3-1-nemoguard-8b-topic-control-nim
- Alternative: nvidia-llama-3-1-nemotron-nano-8b-v1-nim
- Alternative: nvidia-nemotron-nano-9b-v2-nim
- Alternative: openai-gpt-oss-20b-vllm
- Alternative: qwen-2-5-7b-instruct-nim
- Alternative: qwen-qwen2-5-7b-instruct-vllm-cuda13
- Alternative: qwen-qwen2-5-coder-7b-instruct-vllm-cuda13
- Alternative: qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13
- Alternative: qwen-qwen3-4b-instruct-2507-vllm
- Alternative: qwen-qwen3-4b-instruct-2507-vllm-cuda13
- Evidence: https://docs.api.nvidia.com/nim/reference/z-ai-glm4-7

## Benchmark taxonomy

### general-instruction-following

- Datasets: Dolma, Tülu-3
- Metrics: instruction-following quality
- Compare only when: Dataset version must match exactly; prompt wording, prompt templates, and post-processing must be identical; decoding settings and input context window must match primary-source protocol.

### code-generation

- Datasets: The Stack v2
- Metrics: code-generation quality
- Compare only when: Code prompt templates, dataset split, code tokenization and decoding settings (temperature, top-k/top-p, beam) must match exactly as documented in the primary source for the exact checkpoint.

### safety-evaluation

- Datasets: N/A (safety features)
- Metrics: safety alignment
- Compare only when: Safety evaluation methods and threat models must be stated in primary sources or comparisons are an evidence gap.

## Primary sources

- [NVIDIA NIM reference: z-ai / glm4.7](https://docs.api.nvidia.com/nim/reference/z-ai-glm4-7) — NVIDIA (docs.api.nvidia.com); supports The model "z-ai / glm4.7" has a release date on Build.NVIDIA.com of January 2026., The model "z-ai / glm4.7" has a release date on Hugging Face of December 22, 2025., The model architecture type is Transformer., The network architecture is GLM (General Language Model)., The total number of parameters is 358 billion., The base model versions are GLM-4.5 and GLM-4.6., The model accepts text input., The input format is a string., The input parameters are one-dimensional (1D)., The model supports multi-turn conversations, tool calling, and system prompts., The input context length is 131,072 tokens., The model outputs text., The output format is a string., The output parameters are one-dimensional (1D)., The model supports streaming, structured output, and reasoning traces., The output context length is 131,072 tokens.
- [Exact official starting source declared by Forge](https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/allenai/Olmo-3-7B-Instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/bigcode/starcoder2-7b) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/meta/llama-3.1-8b-instruct) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/meta/llama-3.2-1b-instruct) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/meta/llama-3.2-3b-instruct) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/microsoft/phi-3-mini-4k-instruct) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/microsoft/Phi-4-mini-reasoning) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/mistralai/mistral-7b-instruct-v0.3) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-content-safety) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-topic-control) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-8b-v1) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/openai/gpt-oss-20b) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://build.nvidia.com/qwen/qwen-2.5-7b-instruct) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: The provided research findings include only one primary source (https://docs.api.nvidia.com/nim/reference/z-ai-glm4-7) for the model z-ai / glm4.7. No primary-source evidence for any of the listed Forge candidate slugs is present in the findings; therefore architecture/scale, training-data sources, instruction-finetuning regimes, licensing, input/output modalities, safety features, packaging (NIM/vLLM/NGC/Hub), or published results for those slugs cannot be verified.
- Evidence gap: For each named Forge candidate slug in the expected scope, the research findings do not supply the canonical model-card, Hugging Face page, NVIDIA NIM/NGC entry, original repository, or paper needed to verify exact-checkpoint claims (parameter counts, task head, precision, NIM/service version, or runtime).
- Evidence gap: No primary-source benchmark tables/figures/sections were supplied in the research findings for any listed candidate. Therefore no numeric benchmarks (Dolma, Tülu-3, The Stack v2, or other datasets) can be verified for any candidate checkpoint.
- Evidence gap: For Dolma and Tülu-3 datasets, the findings do not show any candidate checkpoint reporting results on these datasets; dataset-specific verification for each candidate is missing.
- Evidence gap: For The Stack v2, the findings do not include evidence that any listed candidate checkpoint was trained on or evaluated on The Stack v2; code-generation provenance and comparability cannot be established.
- Evidence gap: Input preprocessing, prompt templates, decoding settings, and evaluation recipe details for each listed candidate are not present in the provided findings; comparabilityRules therefore cannot be operationalized for cross-model numerical comparison.
- Evidence gap: Licensing statements (model-weight license vs code license) for the listed Forge candidates are not present in the findings and thus cannot be verified.
- Evidence gap: Packaging provenance (whether a Forge-served slug is an upstream checkpoint, an NVIDIA-packaged NIM, or modified) for each candidate is not present in the findings; upstream vs serving-runtime separation cannot be documented.
- Evidence gap: Safety-feature claims (Nemoguard, content-safety, topic-control) for the listed NVIDIA-named slugs cannot be verified from the single provided source; no per-slug safety documentation found in the findings.
- Evidence gap: No primary-source evidence in the provided findings documents instruction-finetuning regimes (DPO, RLHF, RLVR) for any of the listed candidate slugs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 7 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarkTaxonomy[0]: $.benchmarkTaxonomy[0]: unexpected property datasetsNote Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[1]: $.benchmarkTaxonomy[1]: unexpected property datasetsNote Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarkTaxonomy[2]: $.benchmarkTaxonomy[2]: unexpected property datasetsNote Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-content-safety/latest/index.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/allenai/Olmo-3-7B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/bigcode/starcoder2-7b: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/HuggingFaceTB/SmolLM3-3B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/meta/llama-3.1-8b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/meta/llama-3.2-1b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/meta/llama-3.2-3b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/microsoft/phi-3-mini-4k-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/microsoft/Phi-4-mini-reasoning: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/mistralai/mistral-7b-instruct-v0.3: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-content-safety: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-topic-control: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-8b-v1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/openai/gpt-oss-20b: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/qwen/qwen-2.5-7b-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen2.5-7B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
