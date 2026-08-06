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

- Research key: `huggingface-co-deepseek-ai-deepseek-r1-distill-qwen-14b-2691341a52`
- Independent audit: `revised`
- Researched: `2026-08-06T11:16:27.273102+00:00`

DeepSeek-R1-Distill-Qwen-14B (checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, revision c79f47acaf303faabb7133b4b7b76f24231f2c8d) is an upstream distilled variant derived from the Qwen2.5-14B family and documented as a dense causal LM. Primary upstream artifacts (Hugging Face model page, config.json, tokenizer_config.json, LICENSE, repository commit, and the DeepSeek-R1 GitHub repository) establish checkpoint identity, architecture identifier (Qwen2ForCausalLM), a context-window configuration in config.json (max_position_embeddings = 131072), tokenizer configuration (tokenizer_config.json), and an MIT license on the checkpoint repository. The Qwen2.5-14B base lineage and its Apache-2.0 license are documented on the Qwen base model page. Primary-source benchmark table entries on the Hugging Face model page report numeric evaluation rows for this exact checkpoint (AIME 2024, MATH-500, GPQA-Diamond, LiveCodeBench, Codeforces rating) and a reported 14B parameter class for the distilled checkpoint. Primary sources do not document formal checkpoint-specific safety policies, calibrated confidence-score semantics, or a formal input schema beyond tokenizer configuration; tokenizer_config.json and config.json contain potentially inconsistent context- and tokenizer-limits (model config max_position_embeddings = 131072 vs tokenizer_config model_max_length = 16384 and the model-card text referencing 128k tokens), introducing an ambiguity that requires downstream validation of the effective serving context window. No primary-source evidence was found that Forge pins this exact commit as a runtime guarantee; revision evidence is limited to the repository commit page. All claims in this dossier are explicitly scoped to the exact upstream checkpoint or labeled as an evidence gap where upstream primary sources do not supply checkpoint-specific information.

## Identity

- Upstream name: DeepSeek-R1-Distill-Qwen-14B
- Checkpoint/version: deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Immutable revision: c79f47acaf303faabb7133b4b7b76f24231f2c8d
- Parameter scale: 14 billion dense parameters (reported for DeepSeek-R1-Distill-Qwen-14B in primary-source benchmark table on the Hugging Face model page).
- Architecture/head: Dense causal language model; config.json identifies architecture as "Qwen2ForCausalLM" and model type "qwen2" for this checkpoint.
- License: Model repository LICENSE file (DeepSeek-R1-Distill-Qwen-14B) states the MIT License; the Qwen2.5-14B base model lineage is documented as Apache‑2.0 in the Qwen2.5 base model page.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/LICENSE, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d, https://github.com/deepseek-ai/deepseek-r1, https://huggingface.co/Qwen/Qwen2.5-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json

## Selection

### Recommended

- **Text-only conversational generation and reasoning-oriented chat** — Primary Hugging Face model page documents the checkpoint as a distilled model derived from Qwen2.5-14B and highlights reasoning-oriented capabilities and chain-of-thought/self-verification behaviors for the DeepSeek-R1 family that motivate use in text-generation/chat reasoning settings.
  Scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

### Conditional

- **Long-context text generation workloads** — Use only after downstream validation of the effective context limit in the actual serving stack because primary sources show an ambiguity: config.json sets max_position_embeddings = 131072, tokenizer_config.json sets model_max_length = 16384, and the model page text references 128k tokens; confirm effective usable token window in the deployed runtime.
  Scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B; not a Forge runtime guarantee
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

### Avoid

- **Applications requiring documented checkpoint-specific safety policies, bias-mitigation guidance, or content-filtering guarantees** — Primary sources for this exact checkpoint do not provide explicit safety warnings, bias mitigation statements, or content-filtering guidelines.
  Scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- **Workflows that require formally specified confidence scores or a documented calibrated output contract** — Primary documentation for this exact checkpoint lacks a formal output contract or confidence-score specification; outputs are documented only as generated text/token continuations.
  Scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
  Evidence: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

## Input preparation

### Semantic inputs

- The documented real-world input modality for this checkpoint is text. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

### Accepted formats

- Official upstream repository artifacts for the checkpoint include model files such as config.json and tokenizer_config.json hosted in the Hugging Face model repository. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json
- The checkpoint is intended to consume tokenized text as governed by its tokenizer configuration (tokenizer_config.json). Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json

### Preprocessing

- Tokenizer configuration (tokenizer_config.json) specifies token-level behaviors (bos/eos tokens, model_max_length) that define required tokenization settings for inputs; config.json documents model dtype and other model-level config but does not specify additional normalization routines. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json
- The model config identifies dtype as bfloat16 and other architecture hyperparameters; no upstream checkpoint-specific text-normalization pipeline or additional preprocessing steps are documented in the primary artifacts inspected. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json

### Pre-submit validation

- Evidence gap: The primary sources do not provide a formal input-validation schema, bounds, or prohibited-input categories for this exact checkpoint. Inspected files: config.json, tokenizer_config.json, and the Hugging Face model page. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

### Task-specific formatting

- Evidence gap: The primary sources used here do not provide a checkpoint-specific prompt template or chat message formatting contract for DeepSeek-R1-Distill-Qwen-14B; inspected locations: Hugging Face model page and repository tokenizer/config files. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json

## Output interpretation

### Outputs

- The checkpoint is documented as a causal language model producing generated text/token continuations (not a structured confidence-scored classifier); treat outputs as free-text continuations. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

### Interpretation

- Outputs should be interpreted as generated text from a dense causal LM; primary sources do not define a calibrated confidence score or formal score semantics for this checkpoint. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

### Post-inference validation

- Evidence gap: No official post-inference validation, calibration, or acceptance-check procedure is documented for this exact checkpoint in the inspected primary sources (model page, config.json, tokenizer_config.json). Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json

## Public benchmarks

### General reasoning / competition-style benchmarks

- Dataset/split: AIME 2024 / not reported
- Metric/value: pass@1 / 69.7 (`higher-is-better`)
- Model scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B (benchmark table entry on the Hugging Face model page)
- Conditions: Protocol details (dataset split, evaluation seed, prompt/template) not reported in the inspected table entry.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Locator: Benchmark table on the Hugging Face model page for DeepSeek-R1-Distill-Qwen-14B
- Caveat: Primary source lists the numeric result but does not provide protocol-level details in the inspected table entry.

### Mathematics/problem solving

- Dataset/split: MATH-500 / not reported
- Metric/value: pass@1 / 93.9 (`higher-is-better`)
- Model scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B (benchmark table entry on the Hugging Face model page)
- Conditions: Protocol details not reported in the inspected table entry.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Locator: Benchmark table on the Hugging Face model page for DeepSeek-R1-Distill-Qwen-14B
- Caveat: Primary source lists the numeric result but does not include evaluation protocol details in the inspected table entry.

### Reading comprehension / question answering

- Dataset/split: GPQA-Diamond / not reported
- Metric/value: pass@1 / 59.1 (`higher-is-better`)
- Model scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Conditions: Protocol details not reported in the inspected table entry.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Locator: Benchmark table on the Hugging Face model page for DeepSeek-R1-Distill-Qwen-14B
- Caveat: Primary source provides the numeric value but omitted detailed protocol information in the inspected table entry.

### Code generation / programming tasks

- Dataset/split: LiveCodeBench / not reported
- Metric/value: pass@1 / 53.1 (`higher-is-better`)
- Model scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Conditions: Protocol details not reported in the inspected table entry.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Locator: Benchmark table on the Hugging Face model page for DeepSeek-R1-Distill-Qwen-14B
- Caveat: Primary source lists the numeric result but does not include the evaluation protocol in the inspected table entry.

### Competitive programming rating

- Dataset/split: Codeforces / not reported
- Metric/value: rating / 1481 (`higher-is-better`)
- Model scope: Upstream checkpoint deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Conditions: Rating reported in benchmark table; protocol details not reported in the inspected table entry.
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Locator: Benchmark table on the Hugging Face model page for DeepSeek-R1-Distill-Qwen-14B
- Caveat: Primary source provides a numeric rating but does not document the exact benchmarking protocol in the inspected table entry.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The primary sources do not provide explicit safety warnings, bias mitigation statements, or content-filtering guidelines for this exact checkpoint. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- The primary sources do not provide detailed input-validation rules for this exact checkpoint (no formal prohibited-input categories or bounds were documented in inspected upstream files). Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json
- The primary documentation does not describe a formal output shape or confidence-score specification for this exact checkpoint. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Context-length evidence is ambiguous between primary artifacts: the model page references 128k tokens, config.json sets max_position_embeddings = 131072, and tokenizer_config.json sets model_max_length = 16384; these inconsistent locators require downstream validation of effective usable context in deployment. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json
- Revision/serving-scope limitation: the commit URL documents a repository revision but primary evidence does not show that Forge or any serving runtime pins this exact commit as a runtime guarantee. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d

### Safety

- Evidence gap: No explicit safety warnings, bias mitigation statements, or content-filtering guidelines are provided in the inspected primary sources for this exact checkpoint. Sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Forge policy: Do not use this checkpoint for safety-critical or regulated decisions without domain-specific human review and downstream validation, because the primary sources do not document checkpoint-specific safety controls or calibrated confidence behavior.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### DeepSeek-R1-Distill-Qwen-14B model page

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
- Publisher: deepseek-ai
- Type: `model-card`
- Primary because: Official Hugging Face repository page for the exact upstream checkpoint containing the model card, attached benchmark table entries, and links to repository files.
- Scope: DeepSeek-R1-Distill-Qwen-14B upstream checkpoint
- Supports: identity.upstreamName
- Supports: identity.checkpoint
- Supports: identity.parameterScale
- Supports: recommendedUseCases
- Supports: benchmarks
- Supports: limitations
- Supports: safety
- Supports: inputPreparation.semanticInputs

### DeepSeek-R1-Distill-Qwen-14B config.json

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json
- Publisher: deepseek-ai
- Type: `repository`
- Primary because: Official configuration file for the exact checkpoint providing architecture identifier and max_position_embeddings.
- Scope: DeepSeek-R1-Distill-Qwen-14B upstream checkpoint (config)
- Supports: identity.architecture
- Supports: inputPreparation.preprocessing
- Supports: limitations

### DeepSeek-R1-Distill-Qwen-14B tokenizer_config.json

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json
- Publisher: deepseek-ai
- Type: `repository`
- Primary because: Official tokenizer configuration for the exact checkpoint specifying bos/eos tokens, model_max_length, and tokenizer class.
- Scope: DeepSeek-R1-Distill-Qwen-14B upstream checkpoint (tokenizer)
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.taskSpecificFormatting

### DeepSeek-R1-Distill-Qwen-14B LICENSE

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/LICENSE
- Publisher: deepseek-ai
- Type: `repository`
- Primary because: Official LICENSE file inside the exact checkpoint repository declaring the MIT License and copyright holder.
- Scope: DeepSeek-R1-Distill-Qwen-14B upstream checkpoint (license)
- Supports: identity.license
- Supports: limitations

### DeepSeek-R1 repository (GitHub)

- URL: https://github.com/deepseek-ai/deepseek-r1
- Publisher: deepseek-ai
- Type: `repository`
- Primary because: Official project repository documenting DeepSeek-R1 series licensing and project-level statements relevant to the checkpoint family.
- Scope: DeepSeek-R1 family and repository-level materials
- Supports: identity.license
- Supports: identity.upstreamName
- Supports: limitations

### DeepSeek-R1-Distill-Qwen-14B commit c79f47acaf303faabb7133b4b7b76f24231f2c8d

- URL: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d
- Publisher: deepseek-ai
- Type: `repository`
- Primary because: Official commit page for the exact checkpoint repository showing the documented revision and change (adds LICENSE and notes).
- Scope: DeepSeek-R1-Distill-Qwen-14B upstream checkpoint (revision metadata)
- Supports: identity.revision
- Supports: limitations

### Qwen2.5-14B base model page

- URL: https://huggingface.co/Qwen/Qwen2.5-14B
- Publisher: Qwen
- Type: `model-card`
- Primary because: Canonical model-card page for the Qwen2.5-14B base model documenting lineage and license for the base family.
- Scope: Qwen2.5-14B base-model lineage
- Supports: identity.license
- Supports: identity.architecture

## Evidence gaps

- Comparison-specific evidence gap: No protocol-matched primary evidence comparing this exact checkpoint (deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) against specific alternatives was found in inspected primary sources. Inspected sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json, https://github.com/deepseek-ai/deepseek-r1
- Input-format evidence gap: The primary sources do not provide a formal prompt/message schema beyond tokenizer_config.json and example usages on the model page. Inspected locations: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json
- Preprocessing evidence gap: No detailed normalization or tokenization procedure beyond tokenizer_config.json was documented in the inspected upstream artifacts. Inspected locations: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/tokenizer_config.json, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json
- Output-contract evidence gap: The primary documentation lacks a formal output shape/confidence contract beyond causal text generation. Inspected locations: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/config.json
- Post-output-validation evidence gap: No official calibration or acceptance-check procedure was documented for this checkpoint in the inspected primary sources (model page, config.json, tokenizer_config.json).
- Runtime-scope evidence gap: The supplied primary findings document upstream checkpoint identity but do not document Forge-specific behavior, pinning, or runtime guarantees for the vllm-0.21.0-cuda13 Forge candidate; inspected locations: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 57 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/deepseek-ai/deepseek-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/LICENSE Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://recipes.vllm.ai/deepseek-ai/DeepSeek-R1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nicoboss/DeepSeek-R1-Distill-Qwen-14B-Uncensored Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/second-state/DeepSeek-R1-Distill-Qwen-14B-GGUF Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BlueMoonlight/DeepSeek-R1-Distill-Qwen-14B-mlx-4Bit/commit/318add4c5611abf77cc29e570c2a2c973280001e Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B-bnb-4bit Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://second-state/DeepSeek-R1-Distill-Qwen-14B-GGUF Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-14B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/deepseek-ai/deepseek-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://nicoboss/DeepSeek-R1-Distill-Qwen-14B-Uncensored Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/deepseek-ai/deepseek-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://inference.readthedocs.io/en/v1.4.1/models/builtin/llm/deepseek-r1-distill-qwen.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/open-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/commit/c79f47acaf303faabb7133b4b7b76f24231f2c8d Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/deepseek-ai/deepseek-r1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/blob/main/LICENSE Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://recipes.vllm.ai/deepseek-ai/DeepSeek-R1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nicoboss/DeepSeek-R1-Distill-Qwen-14B-Uncensored Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nicoboss/DeepSeek-R1-Distill-Qwen-14B-Uncensored Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.identity.evidenceUrlsDeprecated: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
