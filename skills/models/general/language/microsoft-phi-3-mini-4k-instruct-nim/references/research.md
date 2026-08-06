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

- Research key: `build-nvidia-com-microsoft-phi-3-mini-4k-instruct-2cea73bbb6`
- Independent audit: `revised`
- Researched: `2026-07-23T21:05:07.033680+00:00`

Upstream checkpoint identity: Phi-3-mini-4k-instruct (stated as the Phi-3 Mini, 3.8B parameters) with model_type "phi3" in the upstream config.json and tokenizer settings for a 4K (4096 token) context in tokenizer_config.json. The canonical Phi-3 technical report (arXiv) documents family-level design, SFT + DPO post-training alignment, mentions both 4K and 128K variants at the family level, and reports numeric summary benchmark values for the Phi-3 family/mini variant in the technical report text. The Hugging Face upstream repository contains config.json, tokenizer_config.json, LICENSE, and README entries that corroborate 3.8B parameter scale and 4K configuration keys. NVIDIA NGC catalog entries and an NVIDIA NeMo docs page document NGC/NIM packaging and note 4K and 128K variants and a packaged INT4 RTX artifact; however, the primary sources in this research did not provide exact, numbered table/figure locators for reported MMLU or MT-Bench numeric claims nor an explicit canonical locator proving that an NGC-packaged artifact is byte-for-byte identical to an upstream checkpoint; those are recorded as evidence gaps below.

## Identity

- Upstream name: Phi-3-mini-4k-instruct
- Checkpoint/version: Phi-3-mini-4k-instruct
- Immutable revision: not reported
- Parameter scale: 3.8B
- Architecture/head: phi3 (model_type set to "phi3") / dense decoder-only Transformer
- License: MIT (LICENSE file present in upstream repository; distinction between model-weights vs code license application not reported)
- Evidence: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/config.json, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/tokenizer_config.json, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/LICENSE, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, https://arxiv.org/pdf/2404.14219, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct

## Selection

### Recommended

- **Instruction-following and general-purpose chat (English)** — Upstream model card and README describe Phi-3-mini-4k-instruct as an instruction‑tuned member of the Phi-3 family and the README/NGC entries describe instruction following and chat-style capabilities; the technical report documents SFT + DPO post-training alignment at the family level.
  Scope: upstream Phi-3-mini-4k-instruct checkpoint
  Evidence: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/README.md, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct, https://arxiv.org/pdf/2404.14219
- **Latency-constrained deployments requiring a compact instruction-tuned model** — The upstream README and repository state the Phi-3 Mini (3.8B) is the smallest/tiniest Phi-3 member intended for quality/low-latency tradeoffs relative to larger family members; NGC packaging lists a compressed artifact targeted at RTX/Ada hardware for low-latency inference.
  Scope: upstream Phi-3-mini-4k-instruct checkpoint and NGC-packaged INT4 RTX artifact (packaging noted; identity mapping not proven)
  Evidence: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/README.md, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx

### Conditional

- **Long-context tasks requiring a 128K window (summarization, long‑document QA, RAG workflows)** — Use only when the explicit Phi-3 Mini 128K upstream variant is selected and the serving runtime/container explicitly supports the 128K configuration; treat the 128K variant as a distinct upstream checkpoint unless a packaging page explicitly documents that the NGC/NIM artifact maps to the same named upstream checkpoint.
  Scope: Phi-3-mini 128K upstream variant (distinct from 4K)
  Evidence: https://arxiv.org/pdf/2404.14219, https://huggingface.co/microsoft/Phi-3-mini-128k-instruct, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct

### Avoid

- **Clinical or regulated decision-making without explicit domain validation and expert review** — The technical report and Microsoft Research landing page describe post-training alignment, robustness testing, and family-level safety work (SFT + DPO and red-teaming) but do not provide checkpoint-specific clinical/regulatory validation or PHI/clinical handling procedures for Phi-3-mini-4k-instruct in the provided primary sources.
  Scope: upstream Phi-3-mini-4k-instruct checkpoint
  Evidence: https://arxiv.org/pdf/2404.14219, https://microsoft.com/en-us/research/publication/phi-3-technical-report-a-highly-capable-language-model-locally-on-your-phone

## Input preparation

### Semantic inputs

- Plain-text prompts (instruction-following/chat-style) in English; input format documented as Text in catalog entries and upstream model card. Sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx

### Accepted formats

- Text/plain prompts; model input and output formats are described as Text in NGC model metadata and the upstream model card describes instruction‑tuned text usage. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

### Preprocessing

- Tokenizer class and special tokens: tokenizer_class set to "LlamaTokenizer"; bos_token "<s>"; eos_token and pad_token set to "<|endoftext|>"; model_max_length set to 4096 (max_position_embeddings 4096 in config.json); vocab_size 32064 in config.json. Sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/tokenizer_config.json, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/config.json

### Pre-submit validation

- Validate that prompt/tokenized input length respects the 4K (4096) context limit for the 4K variant; confirm selection of the 128K variant when longer context is required. Sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/tokenizer_config.json, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/config.json

### Task-specific formatting


## Output interpretation

### Outputs

- Model outputs are plain natural‑language text generations (instruction‑following/chat responses); no structured JSON output contract is specified in the provided primary sources. Sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx

### Interpretation

- Treat generations as natural-language text and avoid overclaiming factual accuracy; primary sources describe alignment and safety processes at the family level but do not publish checkpoint-specific calibration semantics in the provided findings. Sources: https://arxiv.org/pdf/2404.14219, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

### Post-inference validation

- Post-inference validation should follow general RAI/harm-mitigation guidance described at the family level in the technical report; no checkpoint-specific device- or domain-calibration protocols are present in the provided primary sources. Sources: https://arxiv.org/pdf/2404.14219

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Model scale and architecture: upstream config.json documents model_type "phi3" with hidden_size 3072, num_hidden_layers 32, num_attention_heads 32, vocab_size 32064 and max_position_embeddings 4096; the NGC catalog also describes the model as a 3.8B-parameter dense decoder-only Transformer. Sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/config.json, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx
- Training data provenance: the technical report describes use of heavily filtered publicly available web data plus synthetic Phi-3 data at the family level but does not enumerate exact dataset names or granular provenance for the checkpoint in the provided primary sources. Sources: https://arxiv.org/pdf/2404.14219
- Benchmark protocol granularity: the technical report provides numeric summary values for family/mini-level results in the report text but the provided primary findings do not include exact numbered/labelled table or figure locators for MMLU or MT-Bench specific to the Phi-3-mini-4k-instruct checkpoint. Sources: https://arxiv.org/pdf/2404.14219
- Licensing scope: an MIT LICENSE file is present in the upstream Hugging Face repository; the provided primary sources do not report an explicit, separate model-weights vs code license distinction. Sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/LICENSE
- NGC packaging vs upstream identity: NGC/NGC container listings document an INT4 RTX packaged artifact and NIM container metadata, but the provided primary sources do not include an explicit, canonical locator proving byte-for-byte identity between the NGC-packaged artifact and a named upstream checkpoint. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct
- Runtime defaults and flags: the provided NGC/NIM container metadata does not include precise runtime flags, per-run batch-size defaults, or explicit CLI/default configuration guidance for the packaged checkpoint in the provided primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx

### Safety

- Phi-3 technical report documents post-training alignment steps (Supervised Fine-Tuning and Direct Preference Optimization) and describes red‑teaming and harm‑testing at the family level; apply human review and domain expert validation for sensitive/high-risk use cases. Sources: https://arxiv.org/pdf/2404.14219, https://microsoft.com/en-us/research/publication/phi-3-technical-report-a-highly-capable-language-model-locally-on-your-phone
- Evidence gap: The provided primary sources do not include checkpoint-specific PHI/data-protection procedures or clinical/regulatory compliance instructions for Phi-3-mini-4k-instruct; treat clinical/PHI handling as requiring independent expert review.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Phi-3 technical report (arXiv PDF)

- URL: https://arxiv.org/pdf/2404.14219
- Publisher: arXiv / Microsoft Research
- Type: `technical-report`
- Primary because: Canonical technical report providing family-level design, reported benchmarks, SFT+DPO description, long-context variant description, and training-data summary as used in the dossier.
- Scope: Phi-3 family (includes Phi-3-mini references)
- Supports: family-level SFT + DPO alignment and red-teaming descriptions
- Supports: mentions of 4K and 128K variants
- Supports: reported family/mini-level numeric summaries (MMLU 69%, MT-Bench 8.38) in report text (no numbered-table locators supplied in the provided findings)
- Supports: training-data summary (filtered public web data + synthetic Phi-3 data)

### Microsoft Research: Phi-3 technical report landing page

- URL: https://microsoft.com/en-us/research/publication/phi-3-technical-report-a-highly-capable-language-model-locally-on-your-phone
- Publisher: Microsoft Research
- Type: `official-documentation`
- Primary because: Official publisher landing page for the Phi-3 technical report referenced in the dossier.
- Scope: Phi-3 family
- Supports: publication/landing page for the Phi-3 technical report
- Supports: family-level descriptions of training and post-training alignment

### Hugging Face model card: microsoft/Phi-3-mini-4k-instruct (repo landing page)

- URL: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct
- Publisher: Hugging Face (model repository hosted by Microsoft)
- Type: `model-card`
- Primary because: Upstream model card and repository landing page used to confirm checkpoint name, README statements, and repository hosting of canonical files.
- Scope: Phi-3-mini-4k-instruct
- Supports: upstream checkpoint landing page and README
- Supports: statement of 4K and 128K variants at family level
- Supports: instruction-tuned / model card metadata and usage notes

### config.json (microsoft/Phi-3-mini-4k-instruct - upstream repository)

- URL: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/config.json
- Publisher: Hugging Face (repository file maintained by Microsoft)
- Type: `repository`
- Primary because: Contains exact model configuration keys used to verify architecture class and model configuration fields.
- Scope: Phi-3-mini-4k-instruct
- Supports: model_type: phi3
- Supports: hidden_size: 3072
- Supports: num_hidden_layers: 32
- Supports: num_attention_heads: 32
- Supports: vocab_size: 32064
- Supports: max_position_embeddings: 4096
- Supports: torch_dtype: bfloat16
- Supports: attention_dropout: 0.0

### tokenizer_config.json (microsoft/Phi-3-mini-4k-instruct - upstream repository)

- URL: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/tokenizer_config.json
- Publisher: Hugging Face (repository file maintained by Microsoft)
- Type: `repository`
- Primary because: Contains tokenizer configuration keys (tokenizer class, special tokens, model_max_length) used to verify input-prep semantics for the 4K variant.
- Scope: Phi-3-mini-4k-instruct
- Supports: tokenizer_class: LlamaTokenizer
- Supports: bos_token: <s>
- Supports: eos_token: <|endoftext|>
- Supports: pad_token: <|endoftext|>
- Supports: model_max_length: 4096
- Supports: padding_side: left

### LICENSE (Phi-3-mini-4k-instruct upstream repository)

- URL: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/LICENSE
- Publisher: Hugging Face (repository file maintained by Microsoft)
- Type: `model-card`
- Primary because: Upstream repository LICENSE file used to confirm MIT licensing statements present in the repository.
- Scope: Phi-3-mini-4k-instruct repository
- Supports: MIT license file in upstream repository

### README.md (microsoft/Phi-3-mini-4k-instruct upstream repository)

- URL: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/README.md
- Publisher: Hugging Face (repository file maintained by Microsoft)
- Type: `repository`
- Primary because: Repository README used to support positioning statements about the Mini variant and reported capabilities referenced in the dossier.
- Scope: Phi-3-mini-4k-instruct
- Supports: statement that the Phi-3 Mini 4K model has 3.8B parameters
- Supports: summary statements about benchmark performance at the family/mini level

### NGC model page: phi-3-mini-4k-instruct-int4-rtx

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx
- Publisher: NVIDIA NGC (catalog)
- Type: `official-documentation`
- Primary because: NGC catalog entry documenting an INT4 RTX packaged artifact and model metadata (parameter count, architecture descriptor, input/output types, supported hardware).
- Scope: NGC-packaged phi-3-mini-4k-instruct-int4-rtx artifact
- Supports: model described as 3.8B parameters
- Supports: dense decoder-only Transformer architecture description
- Supports: input format: Text, output format: Text
- Supports: packaged INT4 RTX artifact metadata

### NGC container listing: nim teams / microsoft / phi-3-mini-4k-instruct

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct
- Publisher: NVIDIA NGC (container registry)
- Type: `official-documentation`
- Primary because: NIM container listing used to support NIM packaging metadata claims and notes about 4K/128K variants at the family level.
- Scope: NGC NIM container for Phi-3-mini-4k-instruct
- Supports: mentions Phi-3 family and Mini variants with 4K and 128K context lengths
- Supports: container packaging metadata (tags, size) and enterprise support notes

### Hugging Face model card: microsoft/Phi-3-mini-128k-instruct (upstream repository)

- URL: https://huggingface.co/microsoft/Phi-3-mini-128k-instruct
- Publisher: Hugging Face (model repository hosted by Microsoft)
- Type: `model-card`
- Primary because: Upstream model card for the 128K variant used to corroborate existence of a distinct 128K upstream checkpoint and its benchmark summaries in the provided findings.
- Scope: Phi-3-mini-128k-instruct
- Supports: Phi-3 Mini 128K variant exists (3.8B parameters) and supports 128K context length
- Supports: benchmark summaries for long-context tasks as listed on the 128K model page

### NeMo user guide: Phi-3 support entry

- URL: https://docs.nvidia.com/nemo-framework/user-guide/25.02/llms/phi3.html
- Publisher: NVIDIA (NeMo documentation)
- Type: `official-documentation`
- Primary because: NVIDIA NeMo documentation referring to Phi-3 Mini model support and used to corroborate model-architecture/scale statements in the dossier.
- Scope: Phi-3 family / Phi-3-mini
- Supports: statement that the Phi-3-Mini-4K model has 3.8B parameters

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/microsoft/phi-3-mini-4k-instruct
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: microsoft-phi-3-mini-4k-instruct
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Benchmarks: The arXiv technical report and upstream README present numeric summary values attributed to the Phi-3 family/mini variant (reported MMLU 69% and MT-Bench 8.38 in the provided findings), but the primary sources in the provided research findings do not include exact numbered/named table, figure, section, appendix, or page locators that verify those numeric values specifically for the Phi-3-mini-4k-instruct checkpoint. Checked source: https://arxiv.org/pdf/2404.14219.
- Benchmark-protocol dependency: The provided primary findings do not state whether any reported numeric benchmark values were obtained on downstream heads, quantized artifacts (e.g., INT4), or specific NGC packaged runtimes; therefore the numeric summaries cannot be confirmed as applying to the callable Forge-served artifact without an explicit locator. Checked sources: https://arxiv.org/pdf/2404.14219, https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx.
- Task-specific prompt templates / formatting: No canonical prompt templates, paired-input order examples, or official task-formatting templates for Phi-3-mini-4k-instruct were found in the provided primary sources (upstream model card, config/tokenizer files, README, or technical report). Checked sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct, https://arxiv.org/pdf/2404.14219.
- 128K variant identity mapping: While the technical report and Hugging Face pages describe both 4K and 128K variants, the provided primary findings do not include an explicit locator proving that any NGC/NIM packaged artifact maps exactly to the named upstream Phi-3-mini-128k-instruct checkpoint; treat the 128K variant as a distinct upstream checkpoint unless explicit packaging mapping is provided. Checked sources: https://arxiv.org/pdf/2404.14219, https://huggingface.co/microsoft/Phi-3-mini-128k-instruct, https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct.
- Runtime flags and defaults: The provided NGC/NIM container metadata does not include exact runtime flags, default batch-size guidance, or per-run defaults for the packaged checkpoint in the provided primary sources. Checked sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/microsoft/containers/phi-3-mini-4k-instruct.
- Comparisons/head-to-head: The provided primary findings do not include direct head-to-head benchmark tables/figures comparing the exact Phi-3-mini-4k-instruct checkpoint to other Forge candidates under identical protocols; therefore no direct comparisons are supported by the provided primary sources. Checked sources: https://arxiv.org/pdf/2404.14219, https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 34 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[0] uses forbidden secondary host ai.azure.com: $.sources[0] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/bigcode/starcoder2-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.1-8b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-1b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.2-3b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/meta/llama-3.1-70b-instruct-v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://mistralai/ministral-3-3B-Instruct-2512 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/mistralai/mistral-7b-instruct-v0.3-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3-1-nemoguard-8b-content-safety-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3-1-nemoguard-8b-topic-control-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3-1-nemotron-nano-8b-v1-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/nemotron-nano-9b-v2-nim Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/openai/gpt-oss-20b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/qwen/qwen-2.5-7b-instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/models/phi-3-mini-4k-instruct-int4-rtx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.inputPreparation_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://build.nvidia.com/microsoft/phi-3-mini-4k-instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
