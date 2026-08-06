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

- Research key: `huggingface-co-ibm-granite-granite-4-1-8b-d40c6baf50`
- Independent audit: `revised`
- Researched: `2026-08-06T11:58:50.379452+00:00`

Granite-4.1-8B (ibm-granite/granite-4.1-8b) is reported in the inspected repository and blobs as an 8-billion-parameter decoder-only dense instruction/tuned text checkpoint released under Apache-2.0. The repository README and model-card describe supervised fine-tuning and reinforcement-learning alignment applied to the Granite-4.1 family and list supported languages. Repository artifacts inspected include config.json (architecture and max_position_embeddings = 131072) and generation_config.json (bos/eos/pad token ids). The README blob publishes an extensive benchmark table with per-task numeric scores for an "8B Dense" variant; the README does not publish complete evaluation protocol details (dataset splits, prompting/harness details, seeds) at the inspected locator. There are multiple upstream artifacts that report different long-context claims (config.json max_position_embeddings = 131072 vs. family-announcement blobs claiming larger staged extension): this ambiguity is present in the inspected sources. Tokenizer vocabulary and complete tokenization parameter artifacts were not found in the inspected primary blobs for the exact checkpoint metadata locations checked (evidence gaps documented). Default generation hyperparameters, explicit logits/probability output contract, and detailed input truncation/batching rules are not declared in the inspected artifacts and are recorded as evidence gaps.

## Identity

- Upstream name: ibm-granite/granite-4.1-8b
- Checkpoint/version: Granite-4.1-8B (ibm-granite/granite-4.1-8b); repository artifacts inspected include config.json and generation_config.json and referenced model signature/commit artifacts
- Immutable revision: commit 4b28eb0bc684385caa9fb62ecf7047170e3cc3a1 (README update) and additional commit SHAs present in repository history (see sources)
- Parameter scale: 8B
- Architecture/head: Decoder-only dense transformer (GQA / grouped-query attention, RoPE positional embeddings, SwiGLU MLP, RMSNorm, shared input/output embeddings) as stated in repository README and related blobs
- License: Apache-2.0
- Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md, https://huggingface.co/ibm-granite/granite-4.1-8b/commit/4b28eb0bc684385caa9fb62ecf7047170e3cc3a1, https://huggingface.co/ibm-granite/granite-4.1-8b/blame/main/config.json, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/main/generation_config.json

## Selection

### Recommended

- **Instruction-following chat and assistant workflows (text-only)** — Hugging Face model card and README describe the checkpoint as an instruction-following long-context text model finetuned to improve instruction following and chat capabilities.
  Scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
  Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- **Coding and program-synthesis completions (incl. FIM-style completions) as reported in README benchmarks** — The README benchmark table reports HumanEval and MBPP pass@1 scores for the 8B Dense variant and lists code-related capabilities.
  Scope: ibm-granite/granite-4.1-8b (8B Dense variant in README benchmark table)
  Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- **Tool-calling / function-calling integrations (user-provided function schema) — requires downstream integration** — Primary model-card and README describe improved tool-calling capabilities as a family feature; tool integrations require downstream function/schema wiring by the integrator.
  Scope: ibm-granite/granite-4.1-8b (checkpoint-level tool-calling capability described in model card/README; actual integration depends on user tooling)
  Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Conditional

- **Downstream finetuning to support additional languages or specialty domains** — Repository facts state the model family was finetuned from base with open-source permissive datasets plus internal synthetic data; extending language or domain support requires downstream finetuning by practitioners and is not documented as out-of-the-box for unsupported languages in the inspected checkpoint metadata.
  Scope: ibm-granite/granite-4.1-8b (requires user downstream finetuning)
  Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/commit/4b28eb0bc684385caa9fb62ecf7047170e3cc3a1

### Avoid

- **Assuming a specific unstated long-context behavior or context window beyond inspected config claims without verification** — Repository config.json sets max_position_embeddings = 131072; other non-repository announcements in the family commentary assert larger staged extension for the family. The inspected checkpoint blobs do not reconcile these differing claims at the exact checkpoint blob locator.
  Scope: ibm-granite/granite-4.1-8b (config.json / README blob)
  Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b/blame/main/config.json, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

## Input preparation

### Semantic inputs

- Text-based instruction/chat messages (instruction-following inputs and chat-style prompts as the intended input modality). Sources: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Accepted formats

- Repository distribution includes configuration and generation metadata files (config.json and generation_config.json) that represent the checkpoint artifacts inspected. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blame/main/config.json, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/main/generation_config.json
- Repository previews list tokenizer artifacts (tokenizer.json, tokenizer_config.json) among repository files for a related granite preview blob inspected in the findings; presence of tokenizer files was reported in repository previews. Sources: https://huggingface.co/ibm-granite/granite-switch-4.1-8b-preview

### Preprocessing

- The inspected model-card and README describe the checkpoint as instruction-tuned but do not publish explicit tokenization parameters or a complete tokenization/vocabulary listing at the exact checkpoint README locator. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Pre-submit validation

- The inspected artifacts do not declare explicit input-validation rules (bounds beyond the config.json max_position_embeddings value, structured JSON constraints, or required message schemas) at the README/config blobs inspected. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blame/main/config.json, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Task-specific formatting

- The checkpoint is presented as an instruction-tuned text model suitable for chat-style prompts and instruction-following formats as described in the model card and README; the README lists chat/instruction usage but does not provide a single mandatory upstream prompt template at the inspected locator. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

## Output interpretation

### Outputs

- Primary repository/README describe the checkpoint as producing text/chat completions (natural language generation outputs) for instruction-following and chat tasks. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- The inspected repository blobs do not declare an explicit upstream output contract exposing logits or per-token probability arrays at the README/config blob locations inspected. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Interpretation

- Generated text should be interpreted as uncalibrated model text outputs; the inspected artifacts do not provide a documented calibrated confidence or numeric scoring output contract. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Post-inference validation

- Evidence gap: repository README and config blobs do not publish recommended post-inference validation, calibration datasets, or thresholding guidance at the inspected locators. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

## Public benchmarks

### Mathematics (chain-of-thought evaluation)

- Dataset/split: DeepMind Math / not reported
- Metric/value: CoT score / 80.07 (0-shot) reported for 8B Dense variant at inspected README blob (`higher-is-better`)
- Model scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
- Conditions: Evaluation protocol details (prompting, split, seeds) not reported at inspected README blob
- Source: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Locator: README.md (benchmarks section)
- Caveat: Inspected README table lists numeric value but omits protocol specifics (split/prompting/seeds) at the locator

### Code generation / program synthesis

- Dataset/split: HumanEval / not reported
- Metric/value: pass@1 / 85.37 (8B Dense variant) reported in README table (`higher-is-better`)
- Model scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
- Conditions: Prompting/protocol not reported at inspected README blob; README shows multiple variant numbers without disambiguating protocol differences at the locator
- Source: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Locator: README.md (benchmarks section)
- Caveat: README lists multiple variant scores; variant-protocol mapping not provided at locator

### Code generation / program synthesis

- Dataset/split: MBPP / not reported
- Metric/value: pass@1 / 87.30 (8B Dense variant) reported in README table (`higher-is-better`)
- Model scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
- Conditions: Evaluation protocol details not reported at inspected README blob
- Source: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Locator: README.md (benchmarks section)
- Caveat: README lists numeric value but omits split/prompting/seeds at locator

### Safety evaluation

- Dataset/split: SALAD-Bench / not reported
- Metric/value: safety score / 95.80 (8B Dense variant) reported in README table (`higher-is-better`)
- Model scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
- Conditions: Evaluation protocol details not reported at inspected README blob
- Source: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Locator: README.md (benchmarks section)
- Caveat: README reports multiple variant safety scores; protocol details not given at locator

### Tool-calling tasks

- Dataset/split: BFCL v3 / not reported
- Metric/value: BFCL v3 score / 68.27 (8B Dense variant) reported in README table (`higher-is-better`)
- Model scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
- Conditions: Tool-calling evaluation harness / attached adapter/head details not specified at README locator
- Source: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Locator: README.md (benchmarks section)
- Caveat: README does not explicitly state whether BFCL v3 evaluation used a downstream service/adapter; the locator lacks those protocol details

### Multitask / aggregated eval

- Dataset/split: Eval+ Avg (MULTIPLE / assorted suites) / not reported
- Metric/value: Eval+ Avg pass@1 / 80.21 (8B Dense variant) reported in README table (`higher-is-better`)
- Model scope: ibm-granite/granite-4.1-8b (8B Dense variant as reported in README)
- Conditions: Aggregate composition and split details not reported at README locator
- Source: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Locator: README.md (benchmarks section)
- Caveat: README reports aggregate numbers but omits composition/split/protocol details at locator

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Task-specific performance comparisons to other candidate models (per-task head-to-head)
- Criteria: No primary-source task-by-task head-to-head comparisons found in the inspected repository/README blobs for the exact checkpoint; README presents absolute numbers but not direct controlled comparisons with protocol parity to specific alternatives.
- Rationale: The README provides per-task scores for the 8B Dense variant but does not provide head-to-head, protocol-matched comparisons to named alternative checkpoints at the inspected locators.
- Comparison conditions: Inspected README blob and commit history were checked; no protocol-matched direct comparisons to alternative named upstream checkpoints were found at those locators.
- Evidence: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

## Limitations and safety

### Limitations

- Primary repository config.json sets max_position_embeddings = 131072, while family-level announcements in other blobs state staged long-context extension for the family; the inspected checkpoint README/config blobs do not reconcile this difference. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blame/main/config.json, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Evidence gap: tokenizer vocabulary and tokenization parameter artifacts are not published at the inspected checkpoint README/config blob locators (tokenizer.json/tokenizer_config.json presence was reported in a related preview listing but a definitive published tokenizer vocabulary and tokenization parameters for the exact checkpoint locator were not found). Sources: https://huggingface.co/ibm-granite/granite-switch-4.1-8b-preview, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Evidence gap: default generation hyperparameters (recommended temperature, top-k, top-p) and explicit logits/probability output contract are not declared in the inspected generation_config.json or README blobs at the checked locators. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/main/generation_config.json, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- The README benchmark table reports multiple variant scores (e.g., several numeric variants per task) but does not explain variant differences or provide the full evaluation protocol at the inspected locator. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

### Safety

- SALAD-Bench safety score for the 8B Dense variant reported in the README is 95.80 (README table entry). Sources: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Evidence gap: the inspected repository/README blobs do not publish detailed operational safety, privacy, PHI-handling, or deployment-level governance procedures at the checked locators. Sources: https://huggingface.co/ibm-granite/granite-4.1-8b, https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: ibm-granite/granite-4.1-8b

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b
- Publisher: Hugging Face (model card provided by Granite Team at IBM)
- Type: `model-card`
- Primary because: Official Hugging Face model card for the exact ibm-granite/granite-4.1-8b checkpoint used to assert identity and intended uses.
- Scope: Granite-4.1-8B (ibm-granite/granite-4.1-8b)
- Supports: Identity fields (model name, 8B parameter scale, instruction-tuned intent)
- Supports: Intended uses (instruction following, chat, tool-calling claims)
- Supports: Pointers to repository README and benchmark summaries

### Hugging Face repository README (benchmarks): granite-4.1-8b README.md blob

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/8ef2991f6d22335c8584a890dbf02290e549f80a/README.md
- Publisher: Hugging Face (model repository blob)
- Type: `repository`
- Primary because: Repository README contains the benchmark tables and variant score listings for the 8B Dense variant and is the canonical locator for numeric benchmark claims.
- Scope: Granite-4.1-8B (benchmarks and variant scores for 8B Dense)
- Supports: Benchmark numbers (HumanEval, MBPP, DeepMind Math, SALAD-Bench, BFCL v3, Eval+ Avg, and others) for 8B Dense variant
- Supports: Architecture description and intended capabilities

### Hugging Face commit (README update) for granite-4.1-8b

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/commit/4b28eb0bc684385caa9fb62ecf7047170e3cc3a1
- Publisher: Hugging Face (model repository commit)
- Type: `repository`
- Primary because: Repository commit that updates README metadata for the checkpoint; used to verify revision history and presence of README benchmark content.
- Scope: Granite-4.1-8B (release/README metadata)
- Supports: Revision/commit-level evidence for README updates and release metadata

### Hugging Face blob: generation_config.json for granite-4.1-8b

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/blob/main/generation_config.json
- Publisher: Hugging Face (repository blob)
- Type: `repository`
- Primary because: Repository generation configuration blob inspected for token id and generation metadata.
- Scope: Granite-4.1-8B (generation configuration blob)
- Supports: Declaration of bos_token_id, eos_token_id, pad_token_id, and reported transformers version in generation_config.json

### Hugging Face blob (blame view) for config.json: granite-4.1-8b

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/blame/main/config.json
- Publisher: Hugging Face (repository blob/blame view)
- Type: `repository`
- Primary because: Repository config.json inspected for architecture hyperparameters and max_position_embeddings for the exact checkpoint.
- Scope: Granite-4.1-8B (config.json content)
- Supports: Model configuration values (hidden_size, intermediate_size, max_position_embeddings = 131072, num_attention_heads, num_hidden_layers, vocab_size, rope_theta, torch_dtype, transformers_version, rms_norm_eps, hidden_act)

### Hugging Face commits index (refs/pr/4) for granite-4.1-8b

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/commits/refs%2Fpr%2F4
- Publisher: Hugging Face (repository commits view)
- Type: `repository`
- Primary because: Repository commits history showing multiple release/maintenance commits for the checkpoint family.
- Scope: Granite-4.1-8B (commit history)
- Supports: Presence of multiple commit SHAs in repository history for the model family

### Hugging Face commits blob (model.sig paths) for granite-4.1-8b (refs/pr/6 and main)

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/commits/refs%2Fpr%2F6/model.sig
- Publisher: Hugging Face (repository commit blob)
- Type: `repository`
- Primary because: Commit-level artifacts (model.sig) and commit SHAs verified in repository history for the family.
- Scope: Granite-4.1-8B (commit signatures/history)
- Supports: Verification of several repository commit SHAs referenced in commit history

### Hugging Face commits blob (model.sig) main branch for granite-4.1-8b

- URL: https://huggingface.co/ibm-granite/granite-4.1-8b/commits/main/model.sig
- Publisher: Hugging Face (repository commit blob)
- Type: `repository`
- Primary because: Main-branch commit signature artifact used to corroborate repository revision evidence.
- Scope: Granite-4.1-8B (main commit signature)
- Supports: Commit signature artifacts on main branch

### Hugging Face preview listing: granite-switch-4.1-8b-preview (repository preview facts)

- URL: https://huggingface.co/ibm-granite/granite-switch-4.1-8b-preview
- Publisher: Hugging Face (repository preview listing)
- Type: `repository`
- Primary because: Repository preview listing referenced in findings that enumerates some repository files (config/tokenizer artifacts) and reports context length and file lists used to inform tokenizer/file presence claims.
- Scope: Granite-4.1 family preview (tokenizer/config listing and reported context length)
- Supports: Reported repository files (model.safetensors, config.json, tokenizer.json, tokenizer_config.json, adapter_index.json, io_configs/, io.yaml, chat_template.jinja, BUILD.md) and reported context length of 131,072 tokens in preview listing

### HFViewer listing for granite-4.1-8b-base (model architecture summary)

- URL: https://hfviewer.com/ibm-granite/granite-4.1-8b-base
- Publisher: HFViewer (model artifact viewer)
- Type: `repository`
- Primary because: Model artifact viewer summarizing base-model architectural parameters (layer counts, hidden size, vocab size, context window) used in the research findings.
- Scope: Granite-4.1-8B-base (architecture and context limit summary)
- Supports: Base-model architecture numbers (40 layers, hidden size 4096, vocab size 100,352) and reported context window up to 131,072 tokens in the viewer

### LinkedIn post referencing Granite 4.1 release

- URL: https://linkedin.com/pulse/ibm-has-released-granite-41-its-next-generation-small-kwxye
- Publisher: LinkedIn (third-party post)
- Type: `technical-report`
- Primary because: Included in research findings as an inspected item reporting family composition and context window claims.
- Scope: Granite-4.1 family (third-party report)
- Supports: Reported family sizes and reported context window claims as recorded in the findings

### DataNorth news item reporting Granite 4.1 claims

- URL: https://datanorth.ai/news/ibm-releases-granite-4-1
- Publisher: DataNorth (news/third-party)
- Type: `technical-report`
- Primary because: Research findings included this third-party news item reporting family-level training scale and context claims.
- Scope: Granite-4.1 family (third-party report)
- Supports: Reported family-level claims (training tokens, context window) as presented in the findings

### Daily.dev article referencing Granite 4.1 family capabilities

- URL: https://daily.dev/posts/ibm-granite-4-1-how-the-8b-model-beats-a-32b-moe-6dkxujokc
- Publisher: Daily.dev (third-party article)
- Type: `technical-report`
- Primary because: Research findings included this article summarizing family training scale, capability claims, and staged-extension statements used by the researcher to document family-level claims.
- Scope: Granite-4.1 family (third-party article)
- Supports: Family-level claims about training tokens, staged long-context extension, and performance summaries as captured in the findings

## Evidence gaps

- Evidence gap: Tokenizer vocabulary and tokenization parameters not published in the inspected repository README or config blobs for the exact checkpoint locator; repository preview listings reference tokenizer files but a definitive published tokenizer vocabulary and parameters for the exact checkpoint locator were not found (checked: README blob, preview listing, config.json).
- Evidence gap: Detailed benchmark protocol (dataset splits, prompt templates, sampling seeds, harness) for README-reported scores is not present at the inspected README blob locator; README reports numeric results but omits per-benchmark protocol details.
- Evidence gap: Default generation hyperparameters (recommended temperature, top-k, top-p) are not declared in the inspected generation_config.json or README blobs at the checked locators.
- Evidence gap: Explicit upstream output contract exposing logits/per-token probability arrays or token-id output shape is not published at the inspected README/config/generation blobs.
- Evidence gap: Detailed operational safety, privacy, PHI-handling, and deployment governance procedures are not published in the inspected repository README/config blobs.
- Evidence gap: Ambiguity in long-context claims — repository config.json shows max_position_embeddings = 131072 while other family-level commentary in the inspected findings references staged long-context extension; inspected checkpoint blobs do not reconcile or document the staged-extension procedure at the checkpoint locator.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[4] uses unapproved repository owner 'blog' for this exact model scope: $.sources[4] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://huggingface.co/blog/ibm-granite/granite-4-1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] describes itself as secondary evidence: $.sources[5] describes itself as secondary evidence Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary host ollama.com: $.sources[6] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary host ai.azure.com: $.sources[11] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.sources[10]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
