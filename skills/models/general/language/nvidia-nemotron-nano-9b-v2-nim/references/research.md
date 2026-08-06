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

- Research key: `build-nvidia-com-nvidia-nvidia-nemotron-nano-9b-v2-0a7b913edb`
- Independent audit: `revised`
- Researched: `2026-07-23T22:16:26.333091+00:00`

Nemotron Nano 9B v2 is an upstream NVIDIA checkpoint: a 9B-parameter hybrid Mamba‑Transformer (Nemotron‑Hybrid) model created by compressing a 12B base model using Minitron pruning and distillation. Primary NVIDIA sources (official build.nvidia model page, downloadable model-card PDF, NVIDIA Research technical report / arXiv preprint, NGC catalog, NIM API docs, and Megatron-Bridge docs) confirm the checkpoint identity, 9B parameter scale, hybrid Mamba‑2/transformer architecture, and maximum context length support up to 128k tokens. The technical report documents compression lineage (12B -> 9B via pruning/distillation), model internals (56 layers, hidden/FFN pruned sizes), and compression/throughput claims; the NIM API reference lists benchmark results reported in a 'Reasoning‑On' mode and states that evaluations used NeMo‑Skills. Several primary-sourced numeric benchmark entries are available via the NIM API reference; however, per-benchmark exact table/figure locators inside the technical-report PDF or model-card PDF are not enumerated in the collected findings for every dataset, and canonical tokenizer/vocabulary and complete prompt/evaluation-harness templates are not specified in the provided primary materials.

## Identity

- Upstream name: NVIDIA Nemotron Nano
- Checkpoint/version: Nemotron Nano 9B v2
- Immutable revision: not reported
- Parameter scale: 9B
- Architecture/head: Hybrid Mamba‑Transformer (Nemotron‑Hybrid / Mamba‑2 selective SSM + transformer layers)
- License: NVIDIA Open Model License (governs model weights)
- Evidence: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard, https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://arxiv.org/abs/2508.14444, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvidia-nemotron-nano-9b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2, https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/llm/nemotronh.html, https://docs.nvidia.com/vss/3.2.0/warehouse-docs/License-Information.html, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese, https://docs.nvidia.com/nemo/megatron-bridge/0.1.0/apidocs/bridge/bridge.recipes.nemotronh.nemotron_nano_9b_v2.html

## Selection

### Recommended

- **Unified reasoning and chat (general-purpose reasoning + instruction following)** — Official NVIDIA model page and downloadable model card describe Nemotron Nano 9B v2 as a unified model intended for reasoning and non-reasoning tasks and document a reasoning-trace-first response mode that can be enabled or controlled.
  Scope: Nemotron Nano 9B v2 (upstream checkpoint)
  Evidence: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard, https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf
- **High-throughput long-context inference (single-GPU long-context serving up to 128k tokens in bf16 on supported NVIDIA GPUs)** — The technical report and Megatron‑Bridge docs state the compressed 9B checkpoint supports inference up to 128k tokens and report throughput/efficiency gains versus a comparator (Qwen3‑8B) and configuration notes for running long contexts in bfloat16 on NVIDIA GPUs.
  Scope: Nemotron Nano 9B v2 (upstream checkpoint)
  Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/llm/nemotronh.html
- **Commercial deployment via NVIDIA NIM / NGC packaging (server/containerized deployments)** — The NGC catalog listing and NIM API reference document official NIM/container packaging and runtime APIs for the named checkpoint and list developer scenarios including agent and RAG-style deployment.
  Scope: Nemotron Nano 9B v2 (NVIDIA NIM container / upstream checkpoint)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvidia-nemotron-nano-9b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2

### Conditional


### Avoid

- **Clinical decision-making or regulated medical advice** — Evidence gap: primary sources do not document domain-specific safety validations, clinical approvals, or regulatory compliance for Nemotron Nano 9B v2; do not use for clinical decision-making without expert review and regulatory evidence.
  Scope: Nemotron Nano 9B v2
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- Input type is text strings (1D token sequences); the model consumes natural-language and code text inputs. Sources: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard, https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf

### Accepted formats

- Accepted format: text strings (1D token sequences); primary sources document maximum context support up to 128k tokens for the checkpoint and variants. Sources: https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese

### Preprocessing

- Evidence gap: canonical upstream tokenizer/vocabulary and step-by-step tokenization/preprocessing pipeline (tokenizer implementation, normalization rules) are not specified in the collected primary sources.

### Pre-submit validation

- Validate input sequence length against the documented maximum context length (128k tokens) and truncate or reject inputs exceeding this bound. Sources: https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### Task-specific formatting

- Evidence gap: explicit canonical prompt templates, few-shot exemplars, chain-of-thought templates, and exact evaluation prompt formatting used for reported benchmarks are not specified in the collected primary sources.

## Output interpretation

### Outputs

- Output objects are natural-language text completions (text strings). Sources: https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf, https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard

### Interpretation

- Model generates a reasoning trace optionally followed by a final answer when configured; primary sources do not provide formal probabilistic-calibration semantics for output scores. Sources: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2

### Post-inference validation

- Evidence gap: no primary-source post-inference calibration protocol, score-normalization, or downstream-output validation heuristics are specified in the collected findings.

## Public benchmarks

### AIME25

- Dataset/split: AIME25 / not reported
- Metric/value: accuracy / 72.1% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

### MATH500

- Dataset/split: MATH500 / not reported
- Metric/value: accuracy / 97.8% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

### GPQA

- Dataset/split: GPQA / not reported
- Metric/value: accuracy / 64.0% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

### LCB

- Dataset/split: LCB / not reported
- Metric/value: accuracy / 71.1% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

### BFCL v3

- Dataset/split: BFCL v3 / not reported
- Metric/value: accuracy / 66.9% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

### IFEVAL-Prompt

- Dataset/split: IFEVAL-Prompt / not reported
- Metric/value: accuracy / 85.4% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

### IFEVAL-Instruction

- Dataset/split: IFEVAL-Instruction / not reported
- Metric/value: accuracy / 90.3% (`higher-is-better`)
- Model scope: Nemotron Nano 9B v2
- Conditions: Reported in NIM API reference as 'Reasoning-On' mode; evaluations performed using NeMo‑Skills per API docs.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Locator: NIM API reference — Benchmark results in Reasoning‑On mode (section)

## Comparisons

### allenai-olmo-2-0425-1b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No like-for-like benchmark protocol documented in the Nemotron primary sources for direct comparison with this alternative.
- Rationale: Nemotron primary sources list Nemotron results but do not present a direct, identical-protocol comparison against this alternative in the collected evidence.
- Comparison conditions: N/A — identical evaluation protocol not documented in collected primary Nemotron sources.
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf, https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard

### allenai-olmo-3-7b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No like-for-like benchmark protocol documented in the Nemotron primary sources for direct comparison with this alternative.
- Rationale: Nemotron primary sources do not provide a cross-model table matching this alternative under identical dataset/prompt/eval harness.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf

### bigcode-starcoder2-7b-nim — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No documented identical-protocol comparison in Nemotron primary sources.
- Rationale: Primary Nemotron sources list Nemotron benchmarks but do not include an explicit like-for-like comparison to StarCoder2 in the provided evidence.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvidia-nemotron-nano-9b-v2

### huggingfacetb-smollm3-3b-vllm-cuda13 — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No identical-protocol primary-source comparison documented for Nemotron Nano 9B v2 vs this alternative in the collected evidence.
- Rationale: Nemotron primary sources do not present a cross-model comparison under identical evaluation conditions with this Hugging Face-distributed alternative.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf

### meta-llama-3-1-70b-instruct-v1 — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No direct cross-model benchmark under identical protocol present in Nemotron primary sources.
- Rationale: Nemotron primary sources do not include a like-for-like table comparing Nemotron Nano 9B v2 to Llama-3-70B under the same dataset/prompts in the provided evidence.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### microsoft-phi-3-mini-4k-instruct-nim — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No direct protocol-matched comparison present in Nemotron primary sources.
- Rationale: No primary-source like-for-like comparative table against this alternative appears in the collected Nemotron evidence.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### microsoft-phi-4-mini-reasoning-vllm-cuda13 — `insufficient-evidence`

- Task: Reasoning/chain-of-thought
- Criteria: No identical-protocol primary-source comparison documented for reasoning/CoT between Nemotron and Phi-4 Mini in the provided evidence.
- Rationale: Nemotron technical report contains reasoning/CoT benchmarks for Nemotron but does not include an explicit, protocol-matched comparison to this alternative in the collected sources.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### mistralai-ministral-3-3b-instruct-2512 — `insufficient-evidence`

- Task: General language modeling
- Criteria: No documented identical-protocol comparison in provided Nemotron sources.
- Rationale: No primary-source like-for-like benchmark against this alternative is present in the Nemotron evidence set.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### mistralai-mistral-7b-instruct-v0-3-nim — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No direct comparable benchmark present in Nemotron primary sources.
- Rationale: No like-for-like comparison documented for this pair in the provided Nemotron primary materials.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### nvidia-llama-3-1-nemoguard-8b-content-safety-nim — `insufficient-evidence`

- Task: Safety-focused content filtering / generation
- Criteria: No direct protocol-matched comparison documented in Nemotron primary sources.
- Rationale: The collected Nemotron evidence does not include a like-for-like evaluation versus this safety-focused NVIDIA product.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### nvidia-llama-3-1-nemoguard-8b-topic-control-nim — `insufficient-evidence`

- Task: Topic control / safety-focused generation
- Criteria: No identical-protocol comparison in Nemotron primary materials.
- Rationale: No direct comparative benchmark is present in the Nemotron primary sources for this pairing.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### nvidia-llama-3-1-nemotron-nano-8b-v1-nim — `insufficient-evidence`

- Task: General language modeling / instruction following
- Criteria: No identical-protocol benchmark between the 8B variant and 9B v2 is documented in the provided Nemotron evidence.
- Rationale: Nemotron primary sources include benchmark tables for 9B v2 but do not provide a like-for-like 8B vs 9B v2 comparison in the collected evidence.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

### nvidia-nemotron-nano-12b-v2-vl-nim — `insufficient-evidence`

- Task: Higher-capacity Nemotron variant comparison
- Criteria: No documented identical-protocol comparison in Nemotron primary sources between the 12B and the 9B v2 checkpoint in the collected evidence.
- Rationale: While the technical report documents teacher/teacher-student lineage (12B -> 9B) and compression lineage, the provided evidence does not present a like-for-like benchmark table comparing 12B‑v2 and 9B‑v2 under identical protocols.
- Comparison conditions: N/A
- Evidence: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf

## Limitations and safety

### Limitations

- The model has a documented maximum context length of 128k tokens which implies substantial memory and compute requirements for long-context workloads. Sources: https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf, https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese
- Evidence gap: canonical tokenizer/vocabulary and end-to-end tokenization/preprocessing implementation are not specified in the collected primary sources.
- The checkpoint is reported as a compressed 9B model derived from a 12B teacher via pruning and distillation (Minitron); technical-report facts document the compression strategy and some layer/channel pruning details. Sources: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf, https://arxiv.org/abs/2508.14444
- Evidence gap: exact per-benchmark table/figure/section locators inside the technical-report PDF or model-card PDF for some reported numeric results are not enumerated in the collected findings; locating the precise table/figure would be required to disambiguate some reported numeric variants.
- Evidence gap: canonical prompt templates, few-shot exemplars, chain-of-thought prompting templates, and exact evaluation-harness code for reported benchmarks (where applicable) are not provided in the collected primary evidence.

### Safety

- Evidence gap: the collected primary sources do not document domain-specific safety testing, clinical validation, or regulatory approvals for Nemotron Nano 9B v2.
- Evidence gap: primary sources do not specify detailed training-data provenance or data-handling controls beyond high-level corpus descriptions in the collected findings; treat as an evidence gap for sensitive-data deployments.

## Related upstream agent skills

### `related-model-workflow`

NVIDIA's Nemotron customization skill is first-party guidance for curating, training, evaluating, converting, and optimizing Nemotron-family checkpoints in the Nemotron repository. It is not an inference payload or Nebius deployment contract; verify the exact listed checkpoint and use the Forge/Serverless instructions for serving.
- [nemotron-customize](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-customize)

## Primary sources

### NVIDIA Nemotron Nano 9B v2 model card (build.nvidia.com model page)

- URL: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card page describing the Nemotron Nano 9B v2 checkpoint, intended uses, and reasoning-trace behavior.
- Scope: Nemotron Nano 9B v2
- Supports: upstream checkpoint identity
- Supports: intended uses (reasoning and chat)
- Supports: reasoning-trace response mode
- Supports: supported languages

### NVIDIA Nemotron Nano 9B v2 model card (downloadable PDF)

- URL: https://developer.nvidia.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official downloadable model-card PDF containing architecture summary, context length, input/output types, and release/data-cutoff notes.
- Scope: Nemotron Nano 9B v2
- Supports: maximum context length
- Supports: input/output semantics
- Supports: architecture summary
- Supports: release and data-cutoff notes

### NVIDIA Nemotron Nano 2 technical report (research.nvidia.com PDF)

- URL: https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf
- Publisher: NVIDIA Research
- Type: `technical-report`
- Primary because: Official technical report detailing architecture, compression/lineage, pruning/distillation strategy, layer/channel counts, and throughput/efficiency claims.
- Scope: Nemotron Nano 9B v2
- Supports: architecture and compression details
- Supports: pruning/distillation lineage (12B -> 9B)
- Supports: layer counts and pruned dimensions
- Supports: throughput and long-context inference claims

### arXiv preprint for Nemotron Nano technical report (arXiv:2508.14444)

- URL: https://arxiv.org/abs/2508.14444
- Publisher: arXiv / NVIDIA authors
- Type: `technical-report`
- Primary because: Canonical preprint identifier for the technical report describing Nemotron Nano 2.
- Scope: Nemotron Nano 9B v2
- Supports: technical-report canonical preprint reference
- Supports: architecture description

### NGC catalog: NVIDIA Nemotron Nano 9B v2 NIM container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvidia-nemotron-nano-9b-v2
- Publisher: NVIDIA
- Type: `repository`
- Primary because: Official NGC/NIM container listing documenting deployment/packaging details for the named checkpoint.
- Scope: Nemotron Nano 9B v2
- Supports: deployment/runtime packaging
- Supports: distribution channels
- Supports: NGC/NIM packaging identity

### NVIDIA NIM API reference for Nemotron Nano 9B v2

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-nvidia-nemotron-nano-9b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM API/docs listing that includes benchmark results (Reasoning‑On mode) and runtime/deployment notes.
- Scope: Nemotron Nano 9B v2 (NIM/runtime)
- Supports: runtime API and deployment notes
- Supports: benchmark results reported in Reasoning‑On mode
- Supports: note that evaluations were performed using NeMo‑Skills

### NemotronH documentation (Megatron-Bridge)

- URL: https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/llm/nemotronh.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official documentation describing Nemotron-H architecture family and configuration/runtime hints referenced by the checkpoint.
- Scope: NemotronH / Nemotron Nano 9B v2
- Supports: architecture family description
- Supports: model configuration and long-context runtime hints
- Supports: Megatron-Bridge recipe/configuration guidance

### License information (NVIDIA Open Model License reference)

- URL: https://docs.nvidia.com/vss/3.2.0/warehouse-docs/License-Information.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Authoritative NVIDIA documentation listing license that governs the model weights.
- Scope: NVIDIA Nemotron Nano 9B v2 (weights)
- Supports: model-weights license identification (NVIDIA Open Model License)

### Hugging Face listing for Japanese variant (context length note)

- URL: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese
- Publisher: NVIDIA (Hugging Face listing)
- Type: `repository`
- Primary because: Provider-hosted variant listing that documents variant-specific context-length support (128k tokens) as hosted by NVIDIA on Hugging Face.
- Scope: Nemotron Nano 9B v2 (Japanese variant)
- Supports: context length (128k tokens) for the listed Japanese variant

### Megatron-Bridge recipe API for Nemotron Nano 9B v2 (apidocs)

- URL: https://docs.nvidia.com/nemo/megatron-bridge/0.1.0/apidocs/bridge/bridge.recipes.nemotronh.nemotron_nano_9b_v2.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Bridge recipe API docs for configuring Nemotron‑Nano‑9B‑v2 training/parallelism and runtime options.
- Scope: Nemotron Nano 9B v2
- Supports: bridge recipe and configuration parameters
- Supports: parallelism and sequence/context configuration guidance

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-nemotron-nano-9b-v2
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: canonical tokenizer/vocabulary and exact tokenization/preprocessing pipeline (implementation, normalization, byte-encoding) for Nemotron Nano 9B v2 are not specified in the collected primary sources and must be located in authoritative upstream code or tokenizer documentation.
- Evidence gap: explicit per-benchmark table/figure/section/page locators inside the technical-report PDF or model-card PDF for many previously-circulated numeric claims (e.g., MMLU-style variants) are not enumerated in the collected findings; exact table/figure locators are required to verify checkpoint-scoped numeric entries reported elsewhere.
- Evidence gap: canonical prompt templates, few-shot exemplars, chain-of-thought prompting templates, and exact evaluation-harness code (including sampling/temperature, pass@k calculation harness, and any code-execution evaluation procedures) used for reported benchmarks are not present in the collected primary sources and are required to reproduce or verify numeric claims requiring specific harnesses.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 50 deterministic draft defect(s) were supplied to the audit.

- `medium` $.identity: $.identity: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity: $.identity: unexpected property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.identity: $.identity: unexpected property think_sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0]: $.limitations[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1]: $.limitations[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2]: $.limitations[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3]: $.limitations[3]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4]: $.limitations[4]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[5]: $.limitations[5]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0]: $.safety[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[1]: $.safety[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.nVIDIA.com/downloads/assets/ace/model_card/nemotron-nano-9b-v2.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arXiv.org/abs/2508.14444 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[6].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/nvidia-nemotron-nano-9b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
