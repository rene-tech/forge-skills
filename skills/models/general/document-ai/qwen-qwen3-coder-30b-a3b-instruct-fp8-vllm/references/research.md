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

- Research key: `huggingface-co-qwen-qwen3-coder-30b-a3b-instruct-fp8-5b84e368da`
- Independent audit: `revised`
- Researched: `2026-08-06T09:41:51.440445+00:00`

Checkpoint-scoped summary using only the inspected primary artifacts: I inspected the Hugging Face checkpoint landing page, the repository tree, the checkpoint README (refs/pr/5), the config.json at the cited blame path (refs/pr/6), tokenizer.json, vocab.json, the referenced commit object (fd8eeb80...), the LICENSE blob (refs/pr/5), and the Qwen3 technical report (arXiv PDF). Checkpoint-scoped verifications: (1) README and model page consistently label this named checkpoint as a 'Coder' variant intended for code-focused generation and explicitly indicate non-thinking-mode operation for this checkpoint; (2) the README recommends reducing context to 32,768 tokens to mitigate OOM while checkpoint commit/config artifacts indicate a much larger native context length (checkpoint commit indicates 262,144 tokens); (3) config.json (blame/refs%2Fpr%2F6/config.json) and the commit metadata provide checkpoint-scoped quantization metadata references (quantization_config, quant_method, weight_block_size) and experts/activation counts identifiers (128 experts / 8 activated experts reported in commit metadata); (4) tokenizer.json and vocab.json artifacts are present in the repository tree but do not unambiguously publish a single reconciled vocabulary-size statement or an enumerated canonical list of special tokens in the checked tokenizer metadata; (5) the repository does not publish an immutable quantized-weight file digest or immutable checkpoint model-file hash in the checked artifacts; (6) no checkpoint-scoped numeric benchmark rows (HumanEval, CodeXGLUE, pass@k, or comparable code-generation metrics) or reproducible evaluation protocol tying numeric scores to this exact named FP8 instruct checkpoint were found in the checked README, config, commit, or arXiv tables/figures. Family-level evidence (from the Qwen3 technical report) documents MoE architecture options and family-level parameter-scale claims; these family-level items are kept separate from checkpoint-scoped claims in this dossier.

## Identity

- Upstream name: Qwen3-Coder-30B-A3B-Instruct-FP8
- Checkpoint/version: Qwen3-Coder-30B-A3B-Instruct-FP8
- Immutable revision: fd8eeb80a6b8ab24e15a3349f03004e64c36e479
- Parameter scale: Family-level: Qwen3 family includes a 30B A3B MoE variant (family-level parameter claims in the Qwen3 technical report). No checkpoint-scoped total-parameter value was found in the checked checkpoint artifacts.
- Architecture/head: Family-level: Mixture-of-Experts (MoE) autoregressive Transformer documented for the Qwen3 family in the Qwen3 technical report. Checkpoint-scoped MoE evidence (experts/activation counts and architecture pointers) appear in checkpoint commit/config artifacts but no single authoritative checkpoint-scoped architecture manifest beyond the checked config/commit files was found.
- License: Apache-2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blame/refs%2Fpr%2F6/config.json, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479, https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/LICENSE

## Selection

### Recommended

- **Code generation and coding-focused text generation (Coder variant)** — Checkpoint README and the model landing page present this named checkpoint as a 'Coder' variant focused on code-generation and agentic coding workflows.
  Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
  Evidence: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md
- **Long-context code comprehension and multi-file / repository-scale prompts (subject to hardware validation and README guidance)** — Checkpoint config/commit artifacts expose a very large native context length and the repository README provides generation and long-context guidance; use for extreme long-context tasks is possible but requires hardware profiling and validation against the README recommendation.
  Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
  Evidence: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md

### Conditional

- **Chain-of-thought / 'thinking-mode' reasoning tasks (only when using an explicitly thinking-mode checkpoint/variant)** — The Qwen3 family-level technical report documents a family-level thinking/non-thinking framework; the checkpoint README and commit metadata for this named FP8 instruct checkpoint explicitly document non-thinking-mode operation. Do not assume thinking-mode behavior for this named checkpoint unless an explicit checkpoint-level artifact states otherwise.
  Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
  Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479
- **Production deployments using extreme long-context (>32,768 tokens)** — The README recommends reducing context to 32,768 tokens to avoid OOM; the checkpoint commit/config indicate a native context length far larger (checkpoint commit indicates 262,144). When operating beyond the README-recommended bound, perform hardware-specific profiling and validation prior to production use.
  Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
  Evidence: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479

### Avoid

- **Using this exact FP8 instruct checkpoint for tasks that require thinking-mode behavior** — Checkpoint README and commit metadata explicitly indicate this named FP8 instruct checkpoint operates in non-thinking mode; the Qwen3 family-level paper documents thinking-mode capability at the family level but the checkpoint does not advertise that behavior.
  Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
  Evidence: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479

## Input preparation

### Semantic inputs

- The checkpoint consumes text inputs including code and natural language; the README and model landing page present this named checkpoint as a code-focused 'Coder' variant. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md

### Accepted formats

- The model repository provides instructions for using the checkpoint with Transformers, vLLM, and SGLang inference frameworks (framework compatibility stated in repository materials). Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/tree/main
- Checkpoint tokenizer artifacts (tokenizer.json and vocab.json) are present in the repository tree. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/tokenizer.json, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/vocab.json, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/tree/main

### Preprocessing

- Config.json (checkpoint blame path) contains quantization-related fields (for example quantization_config, quant_method, weight_block_size) and tokenizer/position fields which should be respected by model-loading and preprocessing pipelines. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blame/refs%2Fpr%2F6/config.json
- Checkpoint commit metadata indicates experts and activation counts (e.g., experts and activated experts) which are relevant to loading and runtime configuration for MoE models. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479

### Pre-submit validation

- Validate inputs and deployment configurations against the README guidance: if out-of-memory (OOM) occurs, the README recommends reducing context length to 32,768 tokens. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md
- Tokenization files (tokenizer.json, vocab.json) are present and should be verified for consistency prior to inference. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/tokenizer.json, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/vocab.json
- Evidence gap: The checkpoint tokenizer artifacts checked do not unambiguously publish a single reconciled vocabulary-size statement or an enumerated special-tokens list (for example the presence or exact spelling of a '<think>' special token is not documented in the checked tokenizer artifacts). Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/tokenizer.json, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/vocab.json

### Task-specific formatting

- No canonical checkpoint-scoped prompt templates, instruction-format examples, or reproducible code-evaluation configs were found in the checkpoint README or repository tree; integrators must develop and validate task-specific prompt formats. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/tree/main

## Output interpretation

### Outputs

- The checkpoint emits autoregressive text tokens (natural language and code) as its primary output; no alternative structured heads or numeric-score outputs are documented in the checked checkpoint artifacts. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8

### Interpretation

- No checkpoint-scoped primary documentation was found that defines explicit calibration or probability-to-confidence mappings (logits/softmax-to-confidence) for this FP8 checkpoint; sampling defaults are described but no mapping from logits to calibrated confidence is published in the checked artifacts. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://arxiv.org/pdf/2505.09388

### Post-inference validation

- No official post-inference calibration pipelines, canonical unit-test harnesses, or reproducible evaluation configurations for generated code were found in the checkpoint README or the Qwen3 technical report; downstream validation procedures must be developed by integrators. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://arxiv.org/pdf/2505.09388

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: head-to-head comparisons for this exact checkpoint
- Criteria: No primary-source checkpoint-scoped comparative protocol or table tying this exact named FP8 checkpoint to other models under matching dataset and evaluation protocols was found in the checked artifacts.
- Rationale: Neither the checkpoint README, the checkpoint commit/config artifacts, nor the Qwen3 technical report provided a reproducible, checkpoint-scoped head-to-head comparison table or protocol for this exact FP8 variant.
- Comparison conditions: Checked README sections, checkpoint config/commit, and arXiv technical report for checkpoint-scoped numeric benchmark rows or reproducible protocols; none were found that name this exact checkpoint and dataset/split/protocol.
- Evidence: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blame/refs%2Fpr%2F6/config.json, https://arxiv.org/pdf/2505.09388

## Limitations and safety

### Limitations

- Checkpoint README and family-level technical report differ in scope: the README and commit metadata for this exact FP8 instruct checkpoint document non-thinking-mode operation while the Qwen3 technical report documents a family-level thinking/non-thinking framework. Do not assume thinking-mode behavior for this exact checkpoint without an explicit checkpoint-scoped statement. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479
- Evidence gap: No checkpoint-scoped immutable model-file digest or immutable checkpoint hash for the FP8 quantized weights was identified in the examined primary repository artifacts (no published immutable weight-file checksum was found in the checked files/paths). Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/tree/main
- Config/commit vs README operational guidance conflict: checkpoint commit/config indicate a native context length (checkpoint commit indicates 262,144 tokens) while the README recommends reducing context to 32,768 tokens to avoid OOM; this primary-source inconsistency requires integrator validation. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479, https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md
- Evidence gap: No checkpoint-scoped reproducible evaluation protocol (prompt templates, seeds, dataset splits, and evaluation scripts) linking numeric HumanEval or comparable code-benchmark scores to this exact named FP8 checkpoint was found in the checked primary artifacts. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://arxiv.org/pdf/2505.09388

### Safety

- The checkpoint repository includes an Apache License, Version 2.0 license blob. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/LICENSE
- Evidence gap: No checkpoint-scoped primary documentation for clinical/PHI-specific or domain-restricted data-handling procedures was found in the checked README, config, or technical report; integrators should apply conservative data-handling and domain-expert review when using the checkpoint on sensitive or regulated data. Sources: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md, https://arxiv.org/pdf/2505.09388

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-Coder-30B-A3B-Instruct-FP8 — model page

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8
- Publisher: Qwen / Hugging Face (model repository)
- Type: `model-card`
- Primary because: Official Hugging Face model landing page for the checkpoint; authoritative repository landing page and model card used for checkpoint-scoped statements.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs

### Qwen3-Coder-30B-A3B-Instruct-FP8 — README (checkpoint model card / README.md, refs/pr/5)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md
- Publisher: Qwen / Hugging Face (model repository)
- Type: `model-card`
- Primary because: Checkpoint README.md containing operational guidance, sampling defaults, non-thinking-mode statement, and long-context guidance; used as primary checkpoint-scoped evidence.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: avoidUseCases
- Supports: conditionalUseCases
- Supports: inputPreparation.validation
- Supports: taskSpecificFormatting
- Supports: outputInterpretation.validation
- Supports: limitations

### Qwen3-Coder-30B-A3B-Instruct-FP8 — config.json (checkpoint repository, blame/refs/pr/6)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blame/refs%2Fpr%2F6/config.json
- Publisher: Qwen / Hugging Face (checkpoint repository)
- Type: `repository`
- Primary because: Checkpoint config.json listing checkpoint-scoped quantization fields, tokenizer/position fields, and architecture-relevant entries used as primary checkpoint-scoped evidence.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: identity.architecture
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.preprocessin
- Supports: limitations

### Qwen3-Coder-30B-A3B-Instruct-FP8 — tokenizer.json (tokenizer artifact)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/tokenizer.json
- Publisher: Qwen / Hugging Face (checkpoint repository)
- Type: `repository`
- Primary because: Checkpoint tokenizer artifact present in the repository tree; used to verify presence of tokenizer artifact files and attempted to verify special tokens and vocabulary.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.validation
- Supports: evidenceGaps

### Qwen3-Coder-30B-A3B-Instruct-FP8 — vocab.json (tokenizer vocab artifact)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/vocab.json
- Publisher: Qwen / Hugging Face (checkpoint repository)
- Type: `repository`
- Primary because: Checkpoint tokenizer vocab artifact present in the repository tree; used to corroborate tokenizer artifact availability and to attempt to determine vocabulary size / special tokens.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.validation
- Supports: evidenceGaps

### Qwen3-Coder-30B-A3B-Instruct-FP8 — repository tree (main)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/tree/main
- Publisher: Qwen / Hugging Face (checkpoint repository)
- Type: `repository`
- Primary because: Repository tree used to verify presence of repository files and file organization (tokenizer artifacts, README, LICENSE, config); used to check for published weight-file artifacts or digests.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: inputPreparation.acceptedFormats
- Supports: evidenceGaps
- Supports: limitations

### Qwen3-Coder-30B-A3B-Instruct-FP8 — checkpoint commit (fd8eeb80...)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/commit/fd8eeb80a6b8ab24e15a3349f03004e64c36e479
- Publisher: Qwen / Hugging Face (checkpoint repository)
- Type: `repository`
- Primary because: Repository commit object referenced for README/config/commit-scoped metadata (experts count, activated experts, native context length), used as a checkpoint-scoped locator.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: identity.revision
- Supports: inputPreparation.preprocessing
- Supports: limitations

### Qwen3 Technical Report (arXiv PDF)

- URL: https://arxiv.org/pdf/2505.09388
- Publisher: Qwen authors / arXiv (technical report)
- Type: `paper`
- Primary because: Canonical Qwen3 technical report on arXiv; used for family-level architecture descriptions, family-level parameter counts, and family-level thinking/non-thinking framework; family-level evidence is kept separate from checkpoint-scoped evidence.
- Scope: Qwen3 family / Qwen3-30B-A3B
- Supports: identity.parameterScale
- Supports: identity.architecture
- Supports: researchSummary
- Supports: limitations

### Qwen3-Coder-30B-A3B-Instruct-FP8 — LICENSE (refs/pr/5)

- URL: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/LICENSE
- Publisher: Qwen / Hugging Face (checkpoint repository)
- Type: `official-documentation`
- Primary because: Checkpoint LICENSE blob verifying Apache-2.0 license for the model artifacts in the repository.
- Scope: Qwen3-Coder-30B-A3B-Instruct-FP8
- Supports: identity.license
- Supports: safety

## Evidence gaps

- Evidence gap: No checkpoint-scoped immutable model-file digest or immutable checkpoint revision/hash for the FP8 quantized weights was identified in the examined primary repository artifacts; checked: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 and https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/tree/main (no published immutable weight-file checksum found).
- Evidence gap: No checkpoint-scoped, reproducible benchmark protocol (prompt templates, seeds, dataset splits, and evaluation scripts) linking numeric HumanEval or comparable code-benchmark scores to this exact named FP8 checkpoint was found in the checked primary artifacts; checked: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md and https://arxiv.org/pdf/2505.09388 (arXiv contains family-level benchmark tables only).
- Evidence gap: The exact tokenizer vocabulary size for this checkpoint could not be unambiguously determined from the checked repository artifacts; checked: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/tokenizer.json and https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/vocab.json (no single reconciled vocabulary-size statement found).
- Evidence gap: Presence or exact spelling of special tokens such as "<think>" in the checkpoint tokenizer was not verifiable from the checkpoint-scoped tokenizer artifacts inspected; checked: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/tokenizer.json and https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/main/vocab.json (no tokenizer_config.json enumerating special tokens was found in the checked artifacts).
- Evidence gap: No canonical checkpoint-scoped prompt templates or instruction-format examples for this exact FP8 instruct checkpoint were found in the model README or the Qwen3 technical report; checked: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md and https://arxiv.org/pdf/2505.09388.
- Evidence gap: No checkpoint-scoped post-inference calibration pipelines, canonical unit-test harnesses, or reproducible evaluation configurations for generated code were found in the checked primary artifacts; checked: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8/blob/refs%2Fpr%2F5/README.md and https://arxiv.org/pdf/2505.09388.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 17 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[2].direction: $.benchmarks[2].direction: 'higher-is-better for throughput; lower-is-better for latency' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses unapproved repository owner 'furiosa-ai' for this exact model scope: $.sources[3] uses unapproved repository owner 'furiosa-ai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'xinjiahui' for this exact model scope: $.sources[6] uses unapproved repository owner 'xinjiahui' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://leadergpu.com/catalog/628-qwen3-coder-a-broken-paradigm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://blog.laozhang.ai/en/posts/qwen3-30b-a3b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://kinigadner.at/qwen3-coder-30b-a3b-instruct-fp8-pc-with-npu-full-method Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://willitrunai.com/models/qwen-3-coder-30b-a3b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://featherless.ai/models/Qwen/Qwen3-Coder-30B-A3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://leadergpu.com/catalog/628-qwen3-coder-a-broken-paradigm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://leadergpu.com/catalog/628-qwen3-coder-a-broken-paradigm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://featherless.ai/models/Qwen/Qwen3-Coder-30B-A3B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://kinigadner.at/qwen3-coder-30b-a3b-instruct-fp8-pc-with-npu-full-method Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://kinigadner.at/qwen3-coder-30b-a3b-instruct-fp8-pc-with-npu-full-method Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://willitrunai.com/models/qwen-3-coder-30b-a3b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
