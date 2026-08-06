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

- Research key: `huggingface-co-huggingfacetb-smollm3-3b-b2e5c24199`
- Independent audit: `revised`
- Researched: `2026-08-06T08:48:38.360872+00:00`

The official HuggingFaceTB SmolLM3-3B model page and README identify SmolLM3-3B as a 3B-parameter, decoder-only language model that supports long context and multilingual reasoning and which (per repository artifacts) uses GQA and NoPE with a 3:1 ratio. The repository contains an evaluation table (README) reporting numeric benchmark rows (e.g., HellaSwag 76.15, ARC-CF 65.61, Winogrande 58.88, MMLU-CF 44.13, GSM-Plus 83.4) as published in the README commit. Canonical architecture/configuration facts (e.g., num_hidden_layers = 36, num_attention_heads = 16, num_key_value_heads = 4, max_position_embeddings = 65536, rope_theta = 5000000.0, tie_word_embeddings = true) are documented in the repository base config.json blob. Primary upstream artifacts checked do not include canonical tokenizer artifacts (tokenizer_config.json, vocab files, merges.txt) in the HuggingFaceTB namespace; the README/config do not publish per-benchmark prompt templates, few-shot templates, or the checkpoint-specific provenance for any GSM8K/SFT variant. The dossier records explicit evidence gaps where the upstream artifacts are silent and preserves only benchmark rows and claims that are directly present in the verified primary README/config blobs.

## Identity

- Upstream name: HuggingFaceTB/SmolLM3-3B
- Checkpoint/version: SmolLM3-3B
- Immutable revision: f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5
- Parameter scale: 3B
- Architecture/head: Decoder-only transformer; uses GQA and NoPE with a 3:1 ratio; configuration fields (from repository base config) include num_hidden_layers = 36, num_attention_heads = 16, num_key_value_heads = 4, pretraining_tp = 2, rms_norm_eps = 1e-06, rope_theta = 5000000.0, max_position_embeddings = 65536, tie_word_embeddings = true.
- License: Apache-2.0
- Evidence: https://huggingface.co/HuggingFaceTB/SmolLM3-3B, https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md, https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/main/README.md, https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json, https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blame/refs%2Fpr%2F23/README.md

## Selection

### Recommended

- **Instruction following and general reasoning tasks** — The upstream HuggingFace model page and README present SmolLM3-3B as a multilingual, long-context reasoning model and include an evaluation table with reasoning/instruction-style benchmark results, supporting use for instruction-following and general reasoning tasks insofar as these align with a decoder-only LM.
  Scope: HuggingFaceTB/SmolLM3-3B (upstream model page and README commit)
  Evidence: https://huggingface.co/HuggingFaceTB/SmolLM3-3B, https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- **Long-context summarization and long-context chat (engineering required to reach extended context)** — The repository base config documents max_position_embeddings = 65536 and the model page/README present the model as supporting long context, indicating the checkpoint is published with a long native context configuration.
  Scope: HuggingFaceTB/SmolLM3-3B (upstream config.json and model page/README)
  Evidence: https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json, https://huggingface.co/HuggingFaceTB/SmolLM3-3B

### Conditional

- **High-accuracy math-benchmark evaluation (requires variant or recipe disclosure)** — Upstream README lists GSM-Plus as an aggregate/extended-mode result but the repository does not publish per-benchmark prompt templates, exact few-shot templates, or checkpoint-scoped GSM8K/SFT provenance in the checked HuggingFaceTB primary artifacts. Use of any GSM8K-specific or SFT-attributed numeric claim requires locating an explicit fine-tuned checkpoint, model-card entry, or commit not present in the checked primary artifacts.
  Scope: HuggingFaceTB/SmolLM3-3B (upstream README evaluation table) — conditional on locating a checkpoint-specific provenance for the numeric claim
  Evidence: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md

### Avoid

- **Clinical decision-making or other safety-critical healthcare use** — Evidence gap: the upstream repository, README, and canonical config artifacts do not document clinical validation, medical licensing, or expert-reviewed clinical benchmarks for SmolLM3-3B; no primary-source clinical validation evidence is present in the checked HuggingFaceTB artifacts.
  Scope: HuggingFaceTB/SmolLM3-3B (upstream checkpoint)
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- Text (natural language) inputs up to the model's maximum context length as published. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B, https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json

### Accepted formats

- Plain-text natural language intended for causal/decoder LM consumption (tokenization required before conversion to token IDs). Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B, https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json

### Preprocessing

- Respect max_position_embeddings = 65536; inputs longer than this must be truncated or windowed by downstream engineering. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json
- Evidence gap: the canonical tokenizer artifacts (tokenizer_config.json, tokenizer.json, vocab files, merges.txt) are not present in the checked HuggingFaceTB repository blobs; therefore the tokenizer vocabulary size and exact normalization/tokenization pipeline cannot be verified from the upstream primary artifacts. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Inputs must be tokenized and converted to token IDs prior to model submission; repository config lists some token id defaults (e.g., pad_token_id) but the full tokenizer mapping is not present in the checked primary artifacts. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json, https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md

### Pre-submit validation

- Validate tokenized input length does not exceed max_position_embeddings = 65536 before submission. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json
- Evidence gap: the upstream repository does not publish a canonical tokenizer vocabulary size or a tokenizer normalization/tokenization pipeline in the HuggingFaceTB/SmolLM3-3B primary repository artifacts; therefore downstream systems must treat tokenizer properties as unverified until a canonical tokenizer artifact is published in the upstream namespace. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md

### Task-specific formatting

- Evidence gap: the upstream README and repository do not provide canonical prompt templates, few-shot example files, or prompt-format artifacts for the reported benchmark evaluations; the README lists numeric results but does not publish template files in the checked primary artifacts. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md

## Output interpretation

### Outputs

- Generated natural-language continuations produced by a decoder-only language model (text generation outputs). Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B, https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/main/README.md

### Interpretation

- Model outputs are natural-language continuations; the upstream README provides evaluation metrics but does not provide calibrated probability-to-confidence mappings for downstream decision-making. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md, https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- Evidence gap: no primary-source documentation was found in the checked HuggingFaceTB artifacts for exact output score semantics (per-token logit scaling, calibrated confidences) or recommended thresholding for downstream decisions. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md

### Post-inference validation

- Evidence gap: the primary repository/config does not prescribe specific downstream post-inference validation routines; no canonical post-inference checks are documented in the checked upstream artifacts. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B

## Public benchmarks

### Commonsense reasoning / completion

- Dataset/split: HellaSwag / not reported
- Metric/value: accuracy / 76.15 (`higher-is-better`)
- Model scope: HuggingFaceTB/SmolLM3-3B (upstream README evaluation table)
- Conditions: As reported in the upstream README evaluation table; the README commit does not publish per-benchmark prompt templates, seeds, or full experimental protocol files in the checked primary artifacts.
- Source: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Locator: README.md (commit f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5) -> evaluation table row labeled 'HellaSwag'
- Caveat: The README provides the numeric score but does not include full experimental protocol specifics in the checked primary artifacts; treat cross-model comparisons cautiously.

### Grade-school / multiple-choice science reasoning

- Dataset/split: ARC-CF / not reported
- Metric/value: accuracy (average) / 65.61 (`higher-is-better`)
- Model scope: HuggingFaceTB/SmolLM3-3B (upstream README evaluation table)
- Conditions: Reported in upstream README evaluation table; protocol details (prompting, few-shot counts, seeds) are not provided in the checked primary artifacts.
- Source: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Locator: README.md (commit f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5) -> evaluation table row labeled 'ARC-CF'
- Caveat: Protocol details (prompting, few-shot setting, chain-of-thought, exact split) are not specified in the checked primary artifacts; direct comparisons require matched protocols.

### Winograd-schema style commonsense

- Dataset/split: Winogrande / not reported
- Metric/value: accuracy / 58.88 (`higher-is-better`)
- Model scope: HuggingFaceTB/SmolLM3-3B (upstream README evaluation table)
- Conditions: As reported in README evaluation table; protocol details are not fully enumerated in the checked primary artifacts.
- Source: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Locator: README.md (commit f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5) -> evaluation table row labeled 'Winogrande'
- Caveat: Direct comparability requires matched evaluation protocol which the README does not provide in the checked primary artifacts.

### Multitask language understanding (closed-book exam)

- Dataset/split: MMLU-CF / not reported
- Metric/value: accuracy (average) / 44.13 (`higher-is-better`)
- Model scope: HuggingFaceTB/SmolLM3-3B (upstream README evaluation table)
- Conditions: Reported in README evaluation table; README lacks full protocol details in the checked primary artifacts.
- Source: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Locator: README.md (commit f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5) -> evaluation table row labeled 'MMLU-CF'
- Caveat: The README reports the numeric value but does not provide complete protocol details necessary for exact reproducibility in the checked primary artifacts.

### High-school math / aggregate (extended-thinking mode)

- Dataset/split: GSM-Plus / not reported
- Metric/value: accuracy (aggregate / extended-thinking mode) / 83.4 (`higher-is-better`)
- Model scope: HuggingFaceTB/SmolLM3-3B (upstream README evaluation table; extended-thinking mode)
- Conditions: Reported in README as an extended-thinking-mode GSM-Plus result; the README does not publish per-component prompt templates or full protocol details in the checked primary artifacts.
- Source: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Locator: README.md (commit f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5) -> evaluation table row labeled 'GSM-Plus'
- Caveat: GSM-Plus is presented as an aggregate/extended-mode metric in the README and the README does not include per-subcomponent protocol specifics in the provided primary artifacts.

## Comparisons

### Qwen3-4B — `insufficient-evidence`

- Task: General reasoning / knowledge benchmarks as reported in the SmolLM3 README
- Criteria: Protocol-matched, checkpoint-scoped head-to-head comparison requires identical prompting, shot counts, dataset splits, and seeds; SmolLM3 upstream artifacts do not publish the prompting templates, seeds, or per-benchmark protocol files required to match another model's protocol.
- Rationale: The upstream SmolLM3 README provides numeric results but omits detailed prompting templates and per-benchmark protocol specifics in the checked primary artifacts; without those details a protocol-matched comparison to Qwen3-4B or any other model cannot be verified from the SmolLM3 primary artifacts alone.
- Comparison conditions: SmolLM3 primary artifacts lack prompting templates, seeds, and per-benchmark protocol files required to match another model's protocol.
- Evidence: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md, https://huggingface.co/HuggingFaceTB/SmolLM3-3B

## Limitations and safety

### Limitations

- Evidence gap: The upstream repository/config artifacts do not include canonical tokenizer artifacts (tokenizer_config.json, tokenizer.json, vocab files, merges.txt) in the checked HuggingFaceTB namespace; tokenizer vocabulary size and normalization pipeline cannot be verified from the upstream primary artifacts. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Protocol-limited comparability: The README reports numeric benchmark values but does not include full experimental protocol details (prompt templates, few-shot examples, seeds, or exact split definitions) necessary for exact, reproducible cross-model comparisons in the checked primary artifacts. Sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md

### Safety

- Evidence gap: The upstream primary sources do not provide model-specific privacy, clinical, biosecurity, or regulated-domain safety validations; apply conservative human-review and domain-expert validation for high-risk use.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### HuggingFace model page: HuggingFaceTB/SmolLM3-3B

- URL: https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model page and model card for SmolLM3-3B; authoritative for high-level model description and links to repository artifacts.
- Scope: HuggingFaceTB/SmolLM3-3B (upstream model repository and model card)
- Supports: high-level model description (3B parameter decoder-only LM, long context, multilingual claims)
- Supports: presentation of evaluation table on the model page (as surfaced from README)

### SmolLM3 README (main branch)

- URL: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/main/README.md
- Publisher: Hugging Face (repository README)
- Type: `repository`
- Primary because: Repository README (main) contains model description and links; used to corroborate model-level claims and presence of an evaluation table on the model page.
- Scope: HuggingFaceTB/SmolLM3-3B README (main)
- Supports: presence of README.md in the repository
- Supports: high-level descriptive claims about the model

### SmolLM3 README (specific commit blob f17cc5c8...)

- URL: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/f17cc5c813d8ec93e04aeb1859ce968cf0bd53f5/README.md
- Publisher: Hugging Face (repository blob)
- Type: `repository`
- Primary because: Commit-specific README blob that contains the evaluation table rows and commit metadata cited for benchmark verification.
- Scope: HuggingFaceTB/SmolLM3-3B README (commit f17cc5c8...)
- Supports: evaluation table numeric results (HellaSwag 76.15, ARC-CF 65.61, Winogrande 58.88, MMLU-CF 44.13, GSM-Plus 83.4) as present in this commit's README
- Supports: assertion that canonical tokenizer artifacts were not located in the checked repository blobs (as noted by the research findings)

### SmolLM3 base config.json (repository blob)

- URL: https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base/blob/main/config.json
- Publisher: Hugging Face (repository blob)
- Type: `repository`
- Primary because: Canonical base model config.json blob documenting architecture hyperparameters and configuration fields.
- Scope: HuggingFaceTB/SmolLM3-3B-Base config.json (blob /main)
- Supports: max_position_embeddings = 65536
- Supports: pad_token_id = 128004
- Supports: num_attention_heads = 16
- Supports: num_hidden_layers = 36
- Supports: num_key_value_heads = 4
- Supports: pretraining_tp = 2
- Supports: rms_norm_eps = 1e-06
- Supports: rope_theta = 5000000.0
- Supports: tie_word_embeddings = true

### SmolLM3 README (blame view for PR refs/PR/23)

- URL: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blame/refs%2Fpr%2F23/README.md
- Publisher: Hugging Face (repository blame view)
- Type: `repository`
- Primary because: Repository blame view used to corroborate language-support claims and other README content present in a PR context.
- Scope: HuggingFaceTB/SmolLM3-3B README (blame/refs/PR/23)
- Supports: language support claims (listing of supported languages as present in the README/PR view)

## Evidence gaps

- Evidence gap: No canonical tokenizer vocabulary file(s) (tokenizer_config.json, tokenizer.json, vocab files, merges.txt) were found in the HuggingFaceTB/SmolLM3-3B primary repository blobs checked; tokenizer vocabulary size and normalization/tokenization pipeline cannot be verified from upstream primary artifacts.
- Evidence gap: No checkpoint-specific GSM8K or GSM-Plus SFT/fine-tuned checkpoint metadata, model-card entry, or commit provenance was found in the HuggingFaceTB primary namespace; therefore any GSM8K/SFT-attributed numeric claim for a SmolLM3-3B fine-tuned variant could not be verified from the checked upstream artifacts.
- Evidence gap: The upstream README and repository blobs do not publish canonical prompt templates, few-shot example files, seed values, or per-benchmark protocol artifacts necessary to exactly reproduce the evaluation-table numeric results; protocol details required for strict protocol-matched comparisons are absent in the checked primary artifacts.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 30 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property avoidUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property conditionalUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property inputPreparation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B/blob/main/config.json Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/blog/smollm3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/HuggingFaceTB/SmolLM3-3B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs is empty without a section-specific evidence gap: $.inputPreparation.semanticInputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
