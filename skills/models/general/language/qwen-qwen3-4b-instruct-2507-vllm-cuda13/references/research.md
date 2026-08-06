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

- Research key: `huggingface-co-qwen-qwen3-4b-instruct-2507-74d4771762`
- Independent audit: `revised`
- Researched: `2026-08-06T09:27:49.870332+00:00`

Checkpoint-scoped, source-verified summary using inspected Hugging Face repository files from the Qwen3-4B-Instruct-2507 repository: config.json (listed above) documents architecture and hyperparameters including model_type="qwen3", architecture class Qwen3ForCausalLM, num_hidden_layers=36, hidden_size=2560, num_attention_heads=32, num_key_value_heads=8, head_dim=128, rope_theta=5000000, torch_dtype="bfloat16", bos_token_id=151643, eos_token_id=151645, and max_position_embeddings=262144 (Source: config.json). The repository LICENSE file states Apache License, Version 2.0 (Source: LICENSE). The repository README.md lists numeric benchmark values for this checkpoint (Source: README.md) but does not report dataset splits, full evaluation protocols, or canonical prompt templates for those benchmarks (evidence gaps). The inspected checkpoint primary files do not provide tokenizer identity or tokenizer files in the official repository root (evidence gap). Canonical decoding/generation defaults are not published in the inspected checkpoint files (evidence gap).

## Identity

- Upstream name: Qwen3-4B-Instruct-2507
- Checkpoint/version: Qwen3-4B-Instruct-2507
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Qwen3ForCausalLM (model_type: qwen3); config.json reports hidden_act="silu", hidden_size=2560, intermediate_size=9728, max_position_embeddings=262144, max_window_layers=36, num_attention_heads=32, num_hidden_layers=36, num_key_value_heads=8, head_dim=128, rms_norm_eps=1e-06, rope_theta=5000000, torch_dtype="bfloat16", attention_bias=false, attention_dropout=0.0, tie_word_embeddings=true, rope_scaling=null, sliding_window=null, bos_token_id=151643, eos_token_id=151645
- License: Apache License, Version 2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE

## Selection

### Recommended

- **General instruction-following and general knowledge research/evaluation** — The checkpoint README.md lists instruction-style benchmark scores (e.g., MMLU‑Pro and MMLU‑Redux) for this exact checkpoint, indicating it has been evaluated on such tasks at the checkpoint level; downstream validation is required because the README does not publish prompt templates or dataset splits.
  Scope: Qwen3-4B-Instruct-2507 (checkpoint README.md)
  Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- **Coding-assistance and code-evaluation research** — The checkpoint README.md reports coding-oriented benchmark scores (e.g., LiveCodeBench v6, MultiPL‑E, LiveBench) for this checkpoint, indicating the model has been evaluated on coding tasks; use for production requires downstream test-suite validation and safety filtering.
  Scope: Qwen3-4B-Instruct-2507 (checkpoint README.md)
  Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- **Mathematical/problem-solving benchmark research** — The checkpoint README.md lists math/reasoning benchmark scores (e.g., AIME25, HMMT25, ZebraLogic) for this exact checkpoint, supporting use in research or assisted workflows after careful validation.
  Scope: Qwen3-4B-Instruct-2507 (checkpoint README.md)
  Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md

### Conditional

- **Long-context tasks exercising very large positional ranges** — config.json reports max_position_embeddings=262144 for this checkpoint; users should empirically validate end-to-end long-context behavior and memory/performance for their workload because the repository README.md does not provide an explicit recommended application-level output length or truncation/cropping policy.
  Scope: Qwen3-4B-Instruct-2507 (config.json)
  Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md

### Avoid

- **Clinical, medical-diagnostic, or other safety-critical decision-making without expert oversight** — Inspected checkpoint primary sources (model card, config.json, LICENSE) do not provide checkpoint-scoped clinical validation, certification, PHI-handling guidance, or creator-stated clinical-use instructions for Qwen3-4B-Instruct-2507.
  Scope: Qwen3-4B-Instruct-2507 (checkpoint files)
  Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE
- **Any safety-critical deployment that requires creator-provided operational/safety controls** — Inspected checkpoint primary sources do not include explicit creator-provided operational safety checklists or runtime mitigation guidance for this exact checkpoint.
  Scope: Qwen3-4B-Instruct-2507 (checkpoint files)
  Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE

## Input preparation

### Semantic inputs

- The inspected checkpoint primary sources do not explicitly enumerate canonical prompt-role tokens, role-convention markers (system/user/assistant), or a named prompt schema for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json
- Model architecture and repository imply causal-text input (Qwen3ForCausalLM) but the checkpoint primary files do not list accepted non-text semantic input types at the checkpoint level. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

### Accepted formats

- The primary checkpoint README.md and config.json do not state a canonical file or paired-input format for prompt submission (no named prompt schema found in inspected files). Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

### Preprocessing

- config.json reports model architecture hyperparameters and max_position_embeddings=262144 but does not specify tokenizer name, tokenizer vocabulary file path, special tokens list, or normalization/tokenization rules for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

### Pre-submit validation

- The inspected checkpoint files do not provide explicit input-validation rules, bounds, or truncation/cropping policy for inputs exceeding the model's positional limit; users must validate and enforce desired truncation behavior upstream. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md

### Task-specific formatting

- No canonical prompt templates, system/user/assistant role-tag examples, or instruction-formatting examples for this checkpoint were found in the checkpoint README.md or config.json. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

## Output interpretation

### Outputs

- The inspected checkpoint README.md and config.json do not publish canonical decoding/generation default parameters (e.g., temperature, top_p, top_k) for this checkpoint; no checkpoint-scoped generation defaults are found in the inspected primary files. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json
- config.json reports BOS/EOS token ids (bos_token_id=151643, eos_token_id=151645) but the repository does not publish a full runtime I/O contract (exact shapes/units for token-id arrays, logits tensor shapes, or normalized probability units) in the inspected files. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

### Interpretation

- The checkpoint README.md reports numeric benchmark scores but does not provide calibration guidance mapping raw outputs (logits/probabilities) to calibrated confidence scores; treat reported benchmark scores as evaluation metrics only and not as runtime confidence calibration. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- No explicit mapping from logits or token logits to user-level calibrated probabilities is provided in the inspected checkpoint files; users should not assume the model provides calibrated confidence without further calibration. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

### Post-inference validation

- Post-inference validation, calibration procedures, or recommended sanity checks are not documented at the checkpoint level in the inspected files; downstream users should run their own calibration and safety checks. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json

## Public benchmarks

### MMLU-Pro

- Dataset/split: MMLU‑Pro / not reported
- Metric/value: score / 69.6 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'MMLU‑Pro'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### MMLU-Redux

- Dataset/split: MMLU-Redux / not reported
- Metric/value: score / 84.2 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'MMLU-Redux'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### GPQA

- Dataset/split: GPQA / not reported
- Metric/value: score / 62.0 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'GPQA'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### SuperGPQA

- Dataset/split: SuperGPQA / not reported
- Metric/value: score / 42.8 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'SuperGPQA'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### AIME25

- Dataset/split: AIME25 / not reported
- Metric/value: score / 47.4 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'AIME25'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### HMMT25

- Dataset/split: HMMT25 / not reported
- Metric/value: score / 31.0 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'HMMT25'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### ZebraLogic

- Dataset/split: ZebraLogic / not reported
- Metric/value: score / 80.2 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'ZebraLogic'
- Caveat: Primary source (README.md) does not report dataset split or evaluation protocol details for this benchmark (evidence gap).

### LiveBench

- Dataset/split: LiveBench 20241125 / not reported
- Metric/value: score / 63.0 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'LiveBench 20241125'
- Caveat: Primary source (README.md) does not report exact dataset split or evaluation protocol (evidence gap).

### LiveCodeBench

- Dataset/split: LiveCodeBench v6 / not reported
- Metric/value: score / 35.1 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported (README lists date range but not full protocol)
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'LiveCodeBench v6 (25.02-25.05)'
- Caveat: Primary source (README.md) lists a date range but does not provide the full evaluation protocol or exact dataset split (evidence gap).

### MultiPL-E

- Dataset/split: MultiPL‑E / not reported
- Metric/value: score / 76.8 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'MultiPL‑E'
- Caveat: Primary source (README.md) does not report dataset split or exact evaluation protocol (evidence gap).

### Aider-Polyglot

- Dataset/split: Aider‑Polyglot / not reported
- Metric/value: score / 12.9 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'Aider‑Polyglot'
- Caveat: Primary source (README.md) does not report dataset split or exact evaluation protocol (evidence gap).

### IFEval

- Dataset/split: IFEval / not reported
- Metric/value: score / 83.4 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507
- Conditions: not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'IFEval'
- Caveat: Primary source (README.md) does not report dataset split or exact evaluation protocol (evidence gap).

### Arena-Hard v2

- Dataset/split: Arena‑Hard v2 / not reported
- Metric/value: win rate / score / 43.4 (`higher-is-better`)
- Model scope: Qwen3-4B-Instruct-2507 (win rate evaluated by GPT-4.1 as reported in README.md)
- Conditions: evaluated win rate reported as GPT-4.1 adjudicated metric in README.md; full protocol not reported
- Source: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Locator: README.md — Benchmarks section, row 'Arena-Hard v2' (win rate evaluated by GPT-4.1)
- Caveat: Primary source (README.md) states the win rate was evaluated by GPT-4.1 but does not provide the exact evaluation protocol, prompts, or dataset split (evidence gap).
- Caveat: This benchmark depends on a GPT-4.1 adjudication process reported in the README and the README does not publish the adjudication prompts or protocol (evidence gap).

## Comparisons

### allenai-olmo-2-0425-1b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: Various (benchmarks reported for Qwen3-4B-Instruct-2507)
- Criteria: No peer primary-source, task-matched checkpoint-scoped benchmark evidence for the comparator was inspected alongside Qwen3-4B-Instruct-2507; protocols and splits cannot be confirmed for direct comparison.
- Rationale: Inspected research findings include only checkpoint-scoped primary files for Qwen3-4B-Instruct-2507 and do not include canonical primary-source checkpoint-scoped benchmarks for this alternative.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### allenai-olmo-3-7b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: Various (benchmarks reported for Qwen3-4B-Instruct-2507)
- Criteria: Peer checkpoint primary-source benchmark data not inspected; cannot ensure matching dataset/split/protocol.
- Rationale: Inspected findings do not include canonical primary-source task-matched benchmarks for the alternative.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### bigcode-starcoder2-7b-nim — `insufficient-evidence`

- Task: Coding-related benchmarks
- Criteria: No peer primary-source checkpoint-scoped benchmarks inspected for this comparator in the provided findings.
- Rationale: Cannot perform task-matched numeric comparison without peer-side canonical primary evidence.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### huggingfacetb-smollm3-3b-vllm-cuda13 — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer primary-source benchmark evidence not included in inspected findings.
- Rationale: Inspected dataset contains only Qwen checkpoint primary files; peer canonical results required for comparison were not inspected.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### meta-llama-3-1-8b-instruct-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer checkpoint-scoped primary benchmarks not present in inspected findings.
- Rationale: No peer canonical checkpoint results available in provided evidence to match tasks and protocol.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### meta-llama-3-2-1b-instruct-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer-side canonical benchmark evidence absent from inspected findings.
- Rationale: Inspected findings include only Qwen checkpoint primary files; peer canonical evidence not available for task-matched comparison.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### meta-llama-3-2-3b-instruct-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: No peer checkpoint-scoped canonical benchmarks inspected for comparison.
- Rationale: Peer canonical primary-source results required for direct comparison were not present in the inspected research findings.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### meta-llama-3.1-70b-instruct-v1 — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer canonical benchmark evidence not inspected.
- Rationale: Inspected evidence set contains only Qwen checkpoint primary files; peer results missing for direct task-matched comparison.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### microsoft-phi-3-mini-4k-instruct-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer checkpoint-scoped canonical benchmarks not present in inspected findings.
- Rationale: No peer canonical sources were inspected for this comparator in the provided evidence.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### microsoft-phi-4-mini-reasoning-vllm-cuda13 — `insufficient-evidence`

- Task: Reasoning/benchmarks
- Criteria: Peer canonical benchmark evidence missing from inspected findings.
- Rationale: Cannot ensure comparable protocol without peer checkpoint primary-source results.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### mistralai-ministral-3-3b-instruct-2512-vllm-cuda13 — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer primary-source checkpoint results not inspected.
- Rationale: Inspected evidence set does not include canonical peer checkpoint benchmarks for task-matched comparison.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### mistralai-mistral-7b-instruct-v0-3-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer canonical checkpoint benchmarks not present in inspected findings.
- Rationale: No peer canonical results were available in inspected evidence for direct comparison.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### nvidia-llama-3-1-nemoguard-8b-content-safety-nim — `insufficient-evidence`

- Task: Content-safety specific evaluations
- Criteria: Peer checkpoint-scoped canonical results for content-safety tasks were not inspected.
- Rationale: Inspected findings do not include peer canonical benchmarks required for comparison.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### nvidia-llama-3-1-nemoguard-8b-topic-control-nim — `insufficient-evidence`

- Task: Topic-control / safety evaluations
- Criteria: Peer canonical checkpoint benchmarks not inspected.
- Rationale: No peer canonical task-matched checkpoint results available in inspected evidence.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### nvidia-llama-3-1-nemotron-nano-8b-v1-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer canonical checkpoint benchmarks not inspected.
- Rationale: Inspected evidence set contains only Qwen checkpoint primary files; peer-side primary evidence missing.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### nvidia-nemotron-nano-9b-v2-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer canonical checkpoint benchmarks not inspected for comparison.
- Rationale: Peer canonical evidence required for task-matched comparisons was not part of inspected findings.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### openai-gpt-oss-20b-vllm — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer checkpoint-scoped primary benchmarks were not inspected.
- Rationale: Inspected evidence includes only Qwen checkpoint primary files; peer canonical results missing for direct numeric comparisons.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### qwen-2-5-7b-instruct-nim — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer checkpoint canonical benchmarks not inspected.
- Rationale: No peer canonical checkpoint results available in inspected findings for direct comparison.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### qwen-qwen2-5-7b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: General/Instruction benchmarks
- Criteria: Peer canonical checkpoint-scoped benchmarks not inspected.
- Rationale: Peer canonical primary evidence required for direct comparison not present in inspected findings.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### qwen-qwen2-5-coder-7b-instruct-vllm-cuda13 — `insufficient-evidence`

- Task: Coding benchmarks
- Criteria: Peer checkpoint and task-matched benchmarks not inspected.
- Rationale: Inspected findings do not include canonical peer checkpoint benchmarks for this alternative.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

### qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13 — `insufficient-evidence`

- Task: Large-scale Qwen family comparisons
- Criteria: Although model-family discussion exists in other contexts, peer checkpoint-specific canonical benchmarks are not part of the inspected findings for direct comparison.
- Rationale: Inspected evidence set contains only the Qwen3-4B-Instruct-2507 checkpoint primary files; peer checkpoint canonical results missing.
- Comparison conditions: peer-side primary-source evidence not present in inspected findings
- Evidence: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md

## Limitations and safety

### Limitations

- License: The checkpoint repository LICENSE file states the model is distributed under Apache License, Version 2.0. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE
- Checkpoint-scoped parameter count (exact number of model parameters for Qwen3-4B-Instruct-2507) is not reported in the inspected primary files (config.json, README.md, model card). Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Architecture and max position embedding limits are reported in config.json, but the repository does not provide runtime memory/latency profiles or recommended deployment hardware for this checkpoint (evidence gap). Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json
- Repository README.md reports many benchmark scores but does not publish dataset splits, full evaluation protocol details, or the prompt templates used for those benchmarks (evidence gap). Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md

### Safety

- License restriction: the checkpoint repository LICENSE file is Apache License, Version 2.0; follow the Apache-2.0 terms for redistribution and use. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE
- Evidence gap: No checkpoint-scoped privacy, PHI-handling, clinical-use, or deployment operational checklist was found in the inspected checkpoint primary files; this is an operational safety evidence gap requiring expert review before use in sensitive domains. Sources: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-4B-Instruct-2507 — Hugging Face model card

- URL: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507
- Publisher: Qwen / Hugging Face (model card page)
- Type: `model-card`
- Primary because: Official Hugging Face model card page for the Qwen3-4B-Instruct-2507 checkpoint; used as the top-level checkpoint locator and repository root.
- Scope: Qwen3-4B-Instruct-2507 (checkpoint page)
- Supports: Repository presence and model card metadata for Qwen3-4B-Instruct-2507

### README.md for Qwen3-4B-Instruct-2507 (repository)

- URL: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/README.md
- Publisher: Qwen / Hugging Face (repository README)
- Type: `repository`
- Primary because: Repository README.md listing checkpoint-scoped numeric benchmark scores and win-rate statements used to support benchmark claims.
- Scope: Qwen3-4B-Instruct-2507 (checkpoint README)
- Supports: Checkpoint-scoped benchmark numeric values (MMLU‑Pro, MMLU‑Redux, GPQA, SuperGPQA, AIME25, HMMT25, ZebraLogic, LiveBench 20241125, LiveCodeBench v6, MultiPL‑E, Aider‑Polyglot, IFEval, Arena‑Hard v2)
- Supports: Win-rate statements (e.g., Arena-Hard v2 evaluated by GPT-4.1) as reported for the checkpoint

### config.json for Qwen3-4B-Instruct-2507

- URL: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json
- Publisher: Qwen / Hugging Face (repository config file)
- Type: `repository`
- Primary because: Repository configuration file declaring model_type, architecture class, layer counts, hidden sizes, rope_theta, torch_dtype, and max_position_embeddings for the checkpoint.
- Scope: Qwen3-4B-Instruct-2507 (checkpoint config)
- Supports: model_type: qwen3
- Supports: architecture: Qwen3ForCausalLM
- Supports: num_hidden_layers=36
- Supports: hidden_size=2560
- Supports: num_attention_heads=32
- Supports: num_key_value_heads=8
- Supports: head_dim=128
- Supports: rope_theta=5000000
- Supports: torch_dtype=bfloat16
- Supports: max_position_embeddings=262144
- Supports: bos_token_id and eos_token_id entries (token ids present in config)

### LICENSE file for Qwen3-4B-Instruct-2507

- URL: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE
- Publisher: Qwen / Hugging Face (repository LICENSE)
- Type: `repository`
- Primary because: Repository LICENSE file used to verify licensing terms for the checkpoint.
- Scope: Qwen3-4B-Instruct-2507 (checkpoint LICENSE file)
- Supports: Model is licensed under the Apache License, Version 2.0

## Evidence gaps

- Evidence gap: Tokenizer identity and tokenization details (tokenizer class/name, vocab file path, special tokens list, normalization rules) are not reported in the inspected checkpoint repository root files (config.json, README.md, model card).
- Evidence gap: Checkpoint-specific exact parameter count for Qwen3-4B-Instruct-2507 is not reported in the inspected primary files (config.json, README.md, model card).
- Evidence gap: Canonical decoding/generation default parameters (temperature, top_p, top_k, min_p) are not published in the inspected checkpoint primary files; no checkpoint-scoped recommended generation defaults found in README.md or config.json.
- Evidence gap: Exact dataset splits, full evaluation protocol, and prompt templates used for each reported benchmark score are not provided in the checkpoint README.md; README.md lists numeric values but does not publish the dataset split, exact evaluation protocol, or prompt templates.
- Evidence gap: Prompt-role conventions and canonical prompt templates (system/user/assistant role tokens or structured instruction-format examples) are not present in the inspected checkpoint files.
- Evidence gap: Runtime I/O contract (exact shapes/units for token-id arrays, logits/probability tensor shapes, and explicit truncation/cropping policies) is not documented in the inspected checkpoint files.
- Evidence gap: Checkpoint-scoped safety, privacy (PHI), clinical-use guidance, and deployment operational checklists are not provided in the inspected checkpoint primary files.
- Evidence gap: Family-level technical report or upstream preprint/arXiv entry for the Qwen3 family was not present in the inspected research findings; family-level pretraining scale and series-level claims cannot be verified from the inspected checkpoint primary files.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[9].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[10].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[11].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[11].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[12].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[12].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
