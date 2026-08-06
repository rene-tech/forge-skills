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

- Research key: `huggingface-co-qwen-qwen3-30b-a3b-instruct-2507-fp8-6399ab64f2`
- Independent audit: `revised`
- Researched: `2026-08-06T09:37:41.673151+00:00`

The only primary-source evidence inspected is the Hugging Face model card at https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8. That page presents the checkpoint name (appearing in the benchmark table as Qwen3-30B-A3B-Instruct-2507) and a benchmark table containing many per-checkpoint numeric scores (examples: MultiPL-E, IFEval, Arena-Hard v2, Creative Writing v3, WritingBench, BFCL-v3, TAU variants, MMLU variants, GPQA, SuperGPQA, and others). The inspected primary source provides explicit numeric benchmark values as shown in the Benchmarks table but does not provide checkpoint-scoped metadata (the research did not find checkpoint-scoped immutable revision identifiers, parameter-count strings, architecture descriptions, tokenizer artifact file paths, or explicit weights-license text in the inspected source).

## Identity

- Upstream name: Qwen3-30B-A3B-Instruct-2507-FP8
- Checkpoint/version: Qwen3-30B-A3B-Instruct-2507-FP8
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

## Selection

### Recommended

- **Benchmark evaluation and empirical performance measurement on the tasks listed on the FP8 model card (e.g., MultiPL-E, IFEval, Arena-Hard v2, Creative Writing v3, WritingBench, BFCL-v3, TAU variants, MMLU variants, GPQA, SuperGPQA, AIME25, HMMT25, ZebraLogic, LiveBench, LiveCodeBench, MultiIF, MMLU-ProX, INCLUDE, PolyMATH).** — The Hugging Face model card for the FP8 checkpoint explicitly lists per-checkpoint numeric scores for these benchmarks in its Benchmarks table.
  Scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- **Use in text-generation / instruction-following workflows to produce textual outputs for downstream evaluation.** — The checkpoint is presented on the model card under a name that includes the token 'Instruct' and the Benchmarks table contains many text-task benchmark results, indicating checkpoint-scoped use for textual generation/evaluation.
  Scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card)
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Conditional

- **Protocol-matched benchmark reproduction or head-to-head comparisons that require dataset splits and aggregation protocols.** — Only appropriate if the deployer obtains and documents full protocol metadata (dataset split, aggregation method, and evaluation harness) because the model card lists numeric scores without associated dataset-split or aggregation metadata; reproductions must supply the missing protocol details.
  Scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Avoid

- **Assuming checkpoint-scoped parameter counts, architecture details, immutable weights revision identifiers, or an explicit weights license for this FP8 artifact.** — The inspected Hugging Face model card presents the checkpoint name and benchmark table values but does not report checkpoint-scoped parameter-count strings, architecture text, an immutable revision identifier, or an explicit weights-license declaration.
  Scope: Qwen3-30B-A3B-Instruct-2507-FP8
  Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

## Input preparation

### Semantic inputs

- Textual inputs for instruction-following and text-generation evaluation (inferred from the checkpoint name and the set of text-centered benchmarks listed on the model card). Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Accepted formats

- Evidence gap: The inspected Hugging Face FP8 model card does not provide explicit checkpoint-scoped accepted file formats or tokenizer artifact file paths (tokenizer.json, tokenizer_config.json, SentencePiece, merges/vocab files). Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Preprocessing

- Evidence gap: The inspected FP8 model card does not publish checkpoint-scoped tokenizer artifacts or explicit tokenization/truncation rules; the model card lists benchmark results but does not include per-checkpoint preprocessing artifact paths. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Pre-submit validation

- Evidence gap: The FP8 model card does not provide checkpoint-scoped input-validation rules (bounds, required fields, or explicit invalid/ambiguous-case handling) for submissions to the model. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Task-specific formatting

- Evidence gap: The FP8 model card does not publish canonical prompt templates, paired-input order, or checkpoint-scoped instruction-format examples; task-specific prompt formatting must be validated by the deployer. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

## Output interpretation

### Outputs

- Primary emissions are textual generations evaluated by the benchmarks listed in the model card. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Interpretation

- Evidence gap: The FP8 model card does not provide checkpoint-scoped logits/probability semantics, calibration guarantees, or recommended output-interpretation thresholds. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Post-inference validation

- Evidence gap: The FP8 model card does not provide recommended post-inference validation checks, calibration tests, or task-specific sanity-check protocols for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

## Public benchmarks

### MultiPL-E

- Dataset/split: MultiPL-E / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 82.2, 82.7, 77.7, 79.3, 74.6, 83.8 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### Aider-Polyglot

- Dataset/split: Aider-Polyglot / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 55.1, 45.3, 44.0, 59.6, 24.4, 35.6 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### IFEval

- Dataset/split: IFEval / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 82.3, 83.9, 84.3, 83.2, 83.7, 84.7 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### Arena-Hard v2

- Dataset/split: Arena-Hard v2 / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 45.6, 61.9, 58.3, 52.0, 24.8, 69.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### Creative Writing v3

- Dataset/split: Creative Writing v3 / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 81.6, 84.9, 84.6, 80.4, 68.1, 86.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### WritingBench

- Dataset/split: WritingBench / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 74.5, 75.5, 80.5, 77.0, 72.2, 85.5 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### BFCL-v3

- Dataset/split: BFCL-v3 / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 64.7, 66.5, 66.1, 68.0, 58.6, 65.1 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### TAU1-Retail

- Dataset/split: TAU1-Retail / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 49.6, 60.3#, 65.2, 65.2, 38.3, 59.1 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### TAU1-Airline

- Dataset/split: TAU1-Airline / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 32.0, 42.8#, 48.0, 32.0, 18.0, 40.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### TAU2-Retail

- Dataset/split: TAU2-Retail / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 71.1, 66.7#, 64.3, 64.9, 31.6, 57.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### TAU2-Airline

- Dataset/split: TAU2-Airline / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 36.0, 42.0#, 42.5, 36.0, 18.0, 38.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### TAU2-Telecom

- Dataset/split: TAU2-Telecom / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 34.0, 29.8#, 16.9, 24.6, 18.4, 12.3 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### MMLU-Pro

- Dataset/split: MMLU-Pro / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 81.2, 79.8, 81.1, 75.2, 69.1, 78.4 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### MMLU-Redux

- Dataset/split: MMLU-Redux / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 90.4, 91.3, 90.6, 89.2, 84.1, 89.3 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### GPQA

- Dataset/split: GPQA / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 68.4, 66.9, 78.3, 62.9, 54.8, 70.4 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### SuperGPQA

- Dataset/split: SuperGPQA / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 57.3, 51.0, 54.6, 48.2, 42.2, 53.4 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### AIME25

- Dataset/split: AIME25 / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 46.6, 26.7, 61.6, 24.7, 21.6, 61.3 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### HMMT25

- Dataset/split: HMMT25 / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 27.5, 7.9, 45.8, 10.0, 12.0, 43.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### ZebraLogic

- Dataset/split: ZebraLogic / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 83.4, 52.6, 57.9, 37.7, 33.2, 90.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### LiveBench 20241125

- Dataset/split: LiveBench 20241125 / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 66.9, 63.7, 69.1, 62.5, 59.4, 69.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### LiveCodeBench v6 (25.02-25.05)

- Dataset/split: LiveCodeBench v6 (25.02-25.05) / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 45.2, 35.8, 40.1, 32.9, 29.0, 43.2 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### MultiIF

- Dataset/split: MultiIF / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 66.5, 70.4, 69.4, 70.2, 70.8, 67.9 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### MMLU-ProX

- Dataset/split: MMLU-ProX / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 75.8, 76.2, 78.3, 73.2, 65.1, 72.0 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### INCLUDE

- Dataset/split: INCLUDE / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 80.1, 82.1, 83.8, 75.6, 67.8, 71.9 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

### PolyMATH

- Dataset/split: PolyMATH / not reported
- Metric/value: benchmark score (per-model reported values on model card) / 32.2, 25.5, 41.9, 27.0, 23.3, 43.1 (`higher-is-better`)
- Model scope: Qwen3-30B-A3B-Instruct-2507-FP8 (Hugging Face model card — Benchmarks table)
- Conditions: Scores listed on the FP8 model card without accompanying dataset-split or aggregation protocol metadata.
- Source: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Locator: Hugging Face model card — Benchmarks table
- Caveat: Model-card benchmark listing lacks explicit dataset-split, aggregation, and full protocol details required for strict cross-model comparability.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: General instruction-following / text-evaluation tasks
- Criteria: No protocol-matched peer-side primary-source benchmark artifacts were available in the single inspected primary source (the FP8 model card) to support head-to-head comparisons; dataset-split and aggregation metadata required for protocol-matched comparisons are not present on the inspected model card.
- Rationale: The inspected primary source provides per-checkpoint numeric benchmark values but does not supply the protocol metadata necessary to match comparisons to peer results.
- Comparison conditions: Direct comparisons require protocol-matched dataset splits, aggregation, and evaluation harnesses which are not provided in the inspected source.
- Evidence: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

## Limitations and safety

### Limitations

- The only inspected primary source is the Hugging Face FP8 model card which lists per-checkpoint benchmark numbers but does not report checkpoint-scoped architecture, parameter counts, tokenizer artifact file paths, immutable weights revision identifiers, or an explicit weights-license declaration; therefore key identity and deployment metadata are not available from the inspected source. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Evidence gap: The inspected model card includes numeric benchmark listings but lacks dataset-split, aggregation method, and full protocol metadata required for strict cross-model comparability for every benchmark row in the table. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

### Safety

- Evidence gap: The inspected FP8 model card does not provide checkpoint-scoped privacy, PHI handling, data-retention, or regulatory deployment guidance; deployers must apply organizational and legal data-handling requirements and perform risk assessments. Sources: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-30B-A3B-Instruct-2507-FP8 model card (Hugging Face)

- URL: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
- Publisher: Qwen / Hugging Face model hub
- Type: `model-card`
- Primary because: Official Hugging Face model card page for the exact named FP8 checkpoint; contains the checkpoint name and the Benchmarks table with the numeric values extracted in this audit.
- Scope: Qwen3-30B-A3B-Instruct-2507-FP8 (FP8 variant)
- Supports: Checkpoint identity as Qwen3-30B-A3B-Instruct-2507-FP8 (model-card naming)
- Supports: Per-checkpoint benchmark numeric listings (Benchmarks table) for the FP8 artifact
- Supports: No checkpoint-scoped publication of tokenizer artifact file paths, parameter-count strings, architecture text, immutable weights revision identifiers, or explicit weights-license text was found on the inspected page.

## Evidence gaps

- Evidence gap: Checkpoint-scoped tokenizer and vocabulary artifact file paths (e.g., tokenizer.json, tokenizer_config.json, SentencePiece files, merges/vocab.txt) were not found on the inspected Hugging Face model card — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (Benchmarks table and model card content).
- Evidence gap: Checkpoint-scoped immutable weights revision identifier (weights file SHA, revision string, or tagged release) was not reported on the inspected Hugging Face model card — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (model card and Files listing).
- Evidence gap: Checkpoint-scoped parameter count and architecture details were not reported on the inspected Hugging Face model card — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (model card content and Benchmarks table).
- Evidence gap: Explicit checkpoint-scoped weights-license declaration was not present on the inspected Hugging Face model card — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (model card content).
- Evidence gap: The Benchmarks table on the inspected model card lists numeric values but does not include full protocol metadata (dataset split, aggregation method) required for protocol-matched comparability — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (Benchmarks table).
- Evidence gap: The inspected FP8 model card does not publish checkpoint-scoped logits/probability semantics, calibration guarantees, or recommended output-interpretation thresholds — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (model card content).
- Evidence gap: The inspected FP8 model card does not provide checkpoint-scoped input-validation rules (bounds, required fields, or explicit invalid/ambiguous-case handling) — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (model card content).
- Evidence gap: The inspected FP8 model card does not publish canonical prompt templates or task-specific instruction-format examples for this checkpoint — checked: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (model card content).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2] uses forbidden secondary host ai.azure.com: $.sources[2] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
