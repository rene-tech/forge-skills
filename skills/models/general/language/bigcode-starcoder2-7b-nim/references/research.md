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

- Research key: `build-nvidia-com-bigcode-starcoder2-7b-b4e247a817`
- Independent audit: `revised`
- Researched: `2026-07-23T22:46:26.318370+00:00`

Primary-source findings support that NVIDIA serves a StarCoder2-7B-related offering and that official upstream creator-controlled material describes StarCoder2-7B as a 7 billion parameter code model trained on The Stack v2-related data, intended for code completion, synthesis, and infilling. However, the provided findings do not prove immutable unchanged-upstream provenance from the Forge page to a specific upstream revision, so upstream checkpoint evidence and NVIDIA serving evidence must remain separate. The strongest verified quantitative evidence is the upstream paper Table 9 greedy-decoding pass@1 results for HumanEval, HumanEval+, MBPP, and MBPP+. Prompt templates, exact Forge/NIM request contract details, tokenizer/config specifics, and post-inference validation procedures remain evidence gaps in the provided findings.

## Identity

- Upstream name: StarCoder2-7B
- Checkpoint/version: StarCoder2-7B
- Immutable revision: not reported
- Parameter scale: 7 billion parameters
- Architecture/head: The research findings say StarCoder2-7B uses Grouped Query Attention. The research findings do not specify a fuller checkpoint-scoped architecture description for the NVIDIA serving page.
- License: NVIDIA NIM container evidence says the underlying model license is the BigCode Model License Agreement. Scope metadata expects bigcode-openrail-m, but the provided primary findings do not include the canonical license text or a source explicitly equating that exact NVIDIA-served scope to BigCode OpenRAIL-M; code license not reported.
- Evidence: https://build.nvidia.com/bigcode/starcoder2-7b, https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.2, https://huggingface.co/bigcode/starcoder2-7b

## Selection

### Recommended

- **Code completion** — Primary NVIDIA container findings state StarCoder2-7B is designed for code completion tasks.
  Scope: NVIDIA StarCoder2-7B container / serving scope
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b, https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.2
- **Code synthesis** — Primary NVIDIA container findings state StarCoder2-7B is designed for code synthesis tasks.
  Scope: NVIDIA StarCoder2-7B container / serving scope
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b, https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.2
- **Code infilling** — Primary NVIDIA container findings state StarCoder2-7B is designed for infilling tasks.
  Scope: NVIDIA StarCoder2-7B container / serving scope
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b, https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.2
- **Upstream code-generation benchmark evaluation on HumanEval and MBPP-style tasks** — The canonical paper findings explicitly report StarCoder2-7B greedy-decoding pass@1 results in Table 9 for HumanEval, HumanEval+, MBPP, and MBPP+.
  Scope: StarCoder2-7B upstream checkpoint
  Evidence: https://arxiv.org/html/2402.19173, https://arxiv.org/pdf/2402.19173

### Conditional

- **Natural-language-to-code generation from instructions** — Conditionally appropriate only after downstream validation for the target instruction format, because creator-controlled upstream findings say the model is not an instruction-following model and that commands such as "Write a function that computes the square root." do not work well.
  Scope: StarCoder2-7B upstream checkpoint
  Evidence: https://huggingface.co/bigcode/starcoder2-7b

### Avoid

- **Assuming strong general instruction-following behavior without task-specific validation** — The official upstream model-card findings say StarCoder2-7B is not an instruction-following model and that commands like "Write a function that computes the square root." do not work well.
  Scope: StarCoder2-7B upstream checkpoint
  Evidence: https://huggingface.co/bigcode/starcoder2-7b

## Input preparation

### Semantic inputs

- StarCoder2-7B accepts natural language and code prompts as input to generate source code. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b
- Upstream evaluation evidence covers natural-language prompts and code-problem inputs from HumanEval and MBPP-family benchmarks. Sources: https://arxiv.org/html/2402.19173, https://arxiv.org/html/2402.19173v1

### Accepted formats

- The NVIDIA container findings describe text-like inputs as natural language and code prompts. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b
- Evidence gap: the provided findings do not specify the exact Forge/NIM API request schema, MIME types, tokenizer payload shape, or official accepted file formats.

### Preprocessing

- Evidence gap: the provided findings do not specify required preprocessing, normalization, tokenization steps, or truncation rules for the Forge/NIM service.
- Upstream benchmark findings say the evaluated models use greedy decoding and report mean pass@1 for benchmark problems. Sources: https://arxiv.org/pdf/2402.19173, https://arxiv.org/html/2402.19173v1

### Pre-submit validation

- Evidence gap: the provided findings do not report official input length bounds, invalid-input handling, or pre-submission validation rules for the Forge/NIM service.
- For MBPP+ comparability, note that EvalPlus uses 399 out of the original 427 MBPP problems after sanitization by the original authors. Sources: https://arxiv.org/html/2402.19173v1

### Task-specific formatting

- Evidence gap: the provided findings do not provide an official prompt template or task-formatting contract for NVIDIA Forge/NIM requests.
- Upstream benchmark formatting conditions are only partially evidenced: HumanEval retains all 164 original problems, and EvalPlus uses 399 sanitized MBPP problems. Sources: https://arxiv.org/html/2402.19173v1

## Output interpretation

### Outputs

- The NVIDIA container findings say StarCoder2-7B outputs generated source code. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b
- Upstream benchmark outputs reported in the paper are mean pass@1 results for benchmark problem sets under greedy decoding. Sources: https://arxiv.org/pdf/2402.19173, https://arxiv.org/html/2402.19173v1

### Interpretation

- Interpret the model output as generated source code rather than a guaranteed correct or instruction-faithful answer. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b, https://huggingface.co/bigcode/starcoder2-7b
- Interpret pass@1 benchmark values as mean pass@1 under the paper's greedy-decoding benchmark protocol; they are upstream-checkpoint results, not verified Forge runtime results. Sources: https://arxiv.org/html/2402.19173, https://arxiv.org/pdf/2402.19173

### Post-inference validation

- Evidence gap: the provided findings do not specify official post-inference validation or output-sanitization procedures for NVIDIA Forge/NIM.
- Benchmark-score reproduction requires matching the paper protocol, including greedy decoding and the stated dataset variants such as sanitized MBPP+ via EvalPlus. Sources: https://arxiv.org/pdf/2402.19173, https://arxiv.org/html/2402.19173v1

## Public benchmarks

### Code generation

- Dataset/split: HumanEval / test
- Metric/value: pass@1 / 35.4 (`higher-is-better`)
- Model scope: StarCoder2-7B upstream checkpoint
- Conditions: Greedy decoding as reported for the StarCoder2-7B row.
- Source: https://arxiv.org/html/2402.19173
- Locator: Table 9
- Caveat: Upstream-checkpoint result; not a Forge runtime benchmark.

### Code generation

- Dataset/split: HumanEval+ / test
- Metric/value: pass@1 / 29.9 (`higher-is-better`)
- Model scope: StarCoder2-7B upstream checkpoint
- Conditions: Greedy decoding as reported for the StarCoder2-7B row.
- Source: https://arxiv.org/html/2402.19173
- Locator: Table 9
- Caveat: Upstream-checkpoint result; not a Forge runtime benchmark.

### Code generation

- Dataset/split: MBPP / test
- Metric/value: pass@1 / 54.4 (`higher-is-better`)
- Model scope: StarCoder2-7B upstream checkpoint
- Conditions: Greedy decoding as reported for the StarCoder2-7B row.
- Source: https://arxiv.org/html/2402.19173
- Locator: Table 9
- Caveat: Upstream-checkpoint result; not a Forge runtime benchmark.

### Code generation

- Dataset/split: MBPP+ / test
- Metric/value: pass@1 / 45.6 (`higher-is-better`)
- Model scope: StarCoder2-7B upstream checkpoint
- Conditions: Greedy decoding as reported for the StarCoder2-7B row.
- Source: https://arxiv.org/html/2402.19173
- Locator: Table 9
- Caveat: Upstream-checkpoint result; not a Forge runtime benchmark.
- Caveat: MBPP+ comparability depends on the EvalPlus sanitized set, which the paper HTML notes uses 399 of the original 427 MBPP problems.

## Comparisons

### DeepSeekCoder-6.7B — `prefer-alternative`

- Task: HumanEval+ and MBPP+ within the paper's medium-sized-model comparison context
- Criteria: Reported benchmark performance on HumanEval+ and MBPP+ in the paper context summarized by the primary PDF findings.
- Rationale: The primary PDF findings state that DeepSeekCoder-6.7B outperforms StarCoder2-7B by 32.4% on HumanEval+ and 24.1% on MBPP+.
- Comparison conditions: Scoped only to the paper's reported evaluation context; the provided findings do not fully specify protocol parity beyond greedy decoding and benchmark context.
- Evidence: https://arxiv.org/pdf/2402.19173

### StarCoderBase-3B — `insufficient-evidence`

- Task: Code benchmarks referenced by the StarCoder2 paper findings
- Criteria: The primary findings only state a comparison for StarCoder2-3B versus StarCoderBase-3B, not for the exact StarCoder2-7B checkpoint against a matched 7B StarCoderBase alternative.
- Rationale: The available primary findings do not provide a direct checkpoint-matched comparison between StarCoder2-7B and a 7B StarCoderBase model.
- Comparison conditions: Evidence mismatch in parameter scale and exact checkpoint scope prevents a valid direct comparison.
- Evidence: https://arxiv.org/pdf/2402.19173

## Limitations and safety

### Limitations

- StarCoder2-7B is not an instruction-following model; commands like "Write a function that computes the square root." do not work well. Sources: https://huggingface.co/bigcode/starcoder2-7b
- The provided findings do not prove that the Forge/NIM serving page corresponds to an unchanged upstream checkpoint revision, so upstream benchmark evidence should not be treated as a Forge runtime benchmark. Sources: https://build.nvidia.com/bigcode/starcoder2-7b, https://arxiv.org/html/2402.19173
- Benchmark comparability for MBPP+ is limited because EvalPlus uses 399 out of the original 427 MBPP problems after sanitization by the original authors. Sources: https://arxiv.org/html/2402.19173v1
- Evidence gap: the provided findings do not specify tokenizer configuration, vocabulary details, special tokens, or official preprocessing rules for this Forge-served scope.
- Evidence gap: the provided findings do not report an immutable upstream revision, checkpoint hash, or exact container-to-checkpoint provenance mapping for the Forge variant.

### Safety

- Evidence gap: the provided findings do not include the canonical BigCode OpenRAIL-M license text or explicit model-use restriction clauses for this scope, so downstream users should verify the governing license terms before deployment.
- Forge policy: do not treat generated source code as verified correct, safe, or policy-compliant without downstream review and testing.
- Forge policy: when using proprietary or sensitive code prompts, apply organizational data-handling review because the provided findings do not specify privacy, retention, or confidential-data guarantees for the Forge/NIM service.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Use BigCode StarCoder2 7B

- URL: https://build.nvidia.com/bigcode/starcoder2-7b
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA model page for the exact Forge source scope named in the brief.
- Scope: Forge model page for bigcode-starcoder2-7b-nim
- Supports: Forge serving scope identity
- Supports: Evidence boundary that the page is the official starting source for this dossier

### StarCoder2-7B NIM container version 2.0.2

- URL: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC/NIM container listing for the named StarCoder2-7B service packaging.
- Scope: NVIDIA StarCoder2-7B container version 2.0.2
- Supports: NVIDIA packaging scope
- Supports: Parameter scale
- Supports: Task descriptions
- Supports: Underlying model license wording

### StarCoder2-7B NIM container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/bigcode/containers/starcoder2-7b
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA container page describing the served model inputs, outputs, and intended tasks.
- Scope: NVIDIA StarCoder2-7B container / team listing
- Supports: Semantic inputs
- Supports: Output modality
- Supports: Recommended use cases
- Supports: Task scope

### StarCoder2-7B model card

- URL: https://huggingface.co/bigcode/starcoder2-7b
- Publisher: BigCode
- Type: `model-card`
- Primary because: Creator-controlled upstream model-card page for the exact StarCoder2-7B checkpoint.
- Scope: StarCoder2-7B upstream checkpoint
- Supports: Upstream identity
- Supports: Parameter scale
- Supports: Architecture detail that it uses Grouped Query Attention
- Supports: Instruction-following limitation

### StarCoder 2 and The Stack v2

- URL: https://arxiv.org/html/2402.19173
- Publisher: BigCode
- Type: `paper`
- Primary because: Canonical primary paper URL required by the brief and used for direct benchmark verification.
- Scope: StarCoder2 paper, including Table 9 benchmark results
- Supports: Verified Table 9 benchmark values for StarCoder2-7B
- Supports: Upstream benchmark scope and caveats

### StarCoder 2 and The Stack v2

- URL: https://arxiv.org/pdf/2402.19173
- Publisher: BigCode
- Type: `paper`
- Primary because: Canonical paper PDF among the provided primary findings, supporting benchmark protocol and comparison statements.
- Scope: StarCoder2 paper PDF
- Supports: Greedy decoding and mean pass@1 benchmark protocol
- Supports: Comparison statement for DeepSeekCoder-6.7B versus StarCoder2-7B

### StarCoder 2 and The Stack v2

- URL: https://arxiv.org/html/2402.19173v1
- Publisher: BigCode
- Type: `paper`
- Primary because: Primary paper HTML version in the provided findings with dataset-sanitization details used for benchmark caveats.
- Scope: StarCoder2 paper HTML v1
- Supports: HumanEval and MBPP+/EvalPlus dataset-scope details
- Supports: Benchmark validation caveats

## Evidence gaps

- The provided findings do not prove an immutable unchanged-upstream provenance link from the Forge page to a specific upstream StarCoder2-7B revision.
- The provided findings do not specify the exact Forge/NIM request schema, prompt template, tokenizer payload contract, or accepted MIME/file formats.
- The provided findings do not provide tokenizer files, vocab size, special-token list, or max input validation rules for this serving scope.
- The provided findings do not state a code license distinct from the model license.
- The provided findings do not specify official post-inference validation procedures for generated code outputs.
- The provided findings do not provide enough matched-protocol primary evidence for a broad comparison set beyond the scoped DeepSeekCoder-6.7B comparison.
- The provided findings do not establish that Table 9 benchmark values are measurements of the Forge runtime rather than the upstream checkpoint.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 40 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property avoidUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property conditionalUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property inputPreparation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property recommendedUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/bigcode/starcoder2-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.4/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.3/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2402.19173 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/bigcode/starcoder2-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/bigcode/starcoder2-7b/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/bigcode/starcoder2-7b/discussions/4/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://licenses.ai/ai-pubs-open-railm-vz1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://scancode-licensedb.aboutcode.org/bigcode-open-rail-m-v1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/1.15.3/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/bigcode-project/starcoder2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.nvidia.com/blog/unlock-your-llm-coding-potential-with-starcoder2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.4/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.3/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2402.19173 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/bigcode/starcoder2-7b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/bigcode/starcoder2-7b/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/bigcode/starcoder2-7b/discussions/4/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://licenses.ai/ai-pubs-open-railm-vz1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://scancode-licensedb.aboutcode.org/bigcode-open-rail-m-v1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/1.15.3/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/bigcode/containers/starcoder2-7b/2.0.6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/bigcode-project/starcoder2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.nvidia.com/blog/unlock-your-llm-coding-potential-with-starcoder2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
