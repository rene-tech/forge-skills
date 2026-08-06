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

- Research key: `huggingface-co-qwen-qwen3-8b-3527d355ea`
- Independent audit: `revised`
- Researched: `2026-08-06T09:27:49.860320+00:00`

Primary upstream sources (Qwen3 technical report and the official Hugging Face Qwen3-8B model page and repository) document that Qwen3-8B is an 8 billion parameter dense Transformer in the Qwen3 family with Grouped Query Attention (GQA), SwiGLU activations, RoPE position embeddings, RMSNorm (pre-norm), the introduction of QK-Norm, and removal of QKV-bias. The technical report provides per-checkpoint architectural hyperparameters (36 layers; 32 query heads / 8 key/value heads; untied embeddings; 128K context) and states a BBPE tokenizer with vocabulary size 151,669. The Hugging Face model page includes a LICENSE file declaring Apache-2.0 for weights and code. The primary sources do not provide per-checkpoint numeric benchmark table rows for the specific datasets named in the draft (see evidence gaps), do not publish an explicit checkpoint revision tag, and do not expose tokenizer implementation files or prompt/evaluation templates for reproducing reported evaluations; those are listed as evidence gaps below.

## Identity

- Upstream name: Qwen3-8B
- Checkpoint/version: Qwen3-8B
- Immutable revision: not reported
- Parameter scale: 8000000000
- Architecture/head: Dense Transformer (Qwen3 dense): Grouped Query Attention (GQA); SwiGLU activation; Rotary Positional Embeddings (RoPE); RMSNorm with pre-normalization; QK‑Norm; removal of QKV‑bias. Per-checkpoint hyperparameters reported for Qwen3-8B: 36 transformer layers; 32 query heads and 8 key/value heads per layer; untied input/output embeddings; context length 128K tokens.
- License: Apache License, Version 2.0 (model weights and code) -- see Hugging Face LICENSE file for exact text
- Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1, https://huggingface.co/Qwen/Qwen3-8B, https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE, https://github.com/qwenLM/qwen3

## Selection

### Recommended

- **Long-context tasks (e.g., long-context summarization, long-context document reading and QA)** — Qwen3-8B is reported with a context length of 128K tokens in the Qwen3 technical report.
  Scope: Qwen3-8B
  Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1
- **General reasoning and academic-benchmark evaluation candidate (instruction-following / chat / reasoning tasks)** — The Qwen3 technical report states architectural and training innovations across the series and describes benchmark evaluation of Qwen3 models; Qwen3-8B is a reported dense checkpoint in that evaluation scope.
  Scope: Qwen3-8B
  Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Conditional

- **Thinking-mode (multi-step reasoning) evaluation or instruction-following in production** — Primary sources document the existence of 'thinking mode' vs 'non-thinking mode' conceptually but do not provide the exact prompt templates, instruction/chat formatting, or decoding/prompting hyperparameters required to reproduce reported evaluations; downstream validation and reproduction of prompts/evaluation protocols are required before production use.
  Scope: Qwen3-8B (concept described in Qwen3 technical report at family/series level and referenced for checkpoints)
  Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Avoid

- **Explicit safety-critical clinical deployment (diagnosis, triage, treatment planning, or other regulated clinical decision-making)** — Evidence gap: the checked primary sources (Qwen3 technical report PDF/HTML and the Hugging Face Qwen3-8B model card) do not document clinical validation, regulatory approval, or clinical-grade evaluation or provide expert-review workflows specific to Qwen3-8B.
  Scope: Qwen3-8B
  Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1, https://huggingface.co/Qwen/Qwen3-8B

## Input preparation

### Semantic inputs

- Plain-text textual inputs tokenized using the Qwen3 BBPE tokenizer (the model expects token sequences produced by the Qwen3 tokenizer). Sources: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Accepted formats

- Text (plain text → token sequences via Qwen3 BBPE tokenizer). Sources: https://arxiv.org/pdf/2505.09388

### Preprocessing

- Tokenizer: byte-level Byte-Pair Encoding (BBPE); vocabulary size reported as 151,669 tokens in the technical report. Sources: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Pre-submit validation

- Evidence gap: primary sources do not provide explicit input-validation rules (bounds checking, exact input truncation/cropping, batching behavior) for Qwen3-8B; these must be established by downstream reproduction and runtime documentation. Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### Task-specific formatting

- Evidence gap: primary sources do not publish exact official prompt templates, system/user message conventions, or instruction-formatting rules for Qwen3-8B evaluative runs; the technical report references 'thinking mode' vs 'non-thinking mode' conceptually but provides no reproduction-ready templates. Sources: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

## Output interpretation

### Outputs

- Evidence gap: primary sources do not specify the exact runtime output object schema for Qwen3-8B (whether official packaging exposes raw logits, token ids, or probability units). Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### Interpretation

- Evidence gap: primary sources contain no explicit calibration, confidence-interpretation guidance, or recommended scoring/post-processing procedures for Qwen3-8B outputs. Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### Post-inference validation

- Evidence gap: no post-inference quality checks, calibration scripts, or deterministic-output procedures are provided in the checked primary sources for Qwen3-8B. Sources: https://arxiv.org/pdf/2505.09388, https://github.com/qwenLM/qwen3

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### allenai/OLMo-2-1124-7B-Instruct — `insufficient-evidence`

- Task: Instruction following / chat
- Criteria: No protocol-matched primary-source comparative results for the alternative were found in the checked primary sources; Qwen3 primary sources do not contain protocol-matched tables comparing Qwen3-8B to this alternative.
- Rationale: The checked Qwen3 technical report and Hugging Face model card document Qwen3 series architecture and per-checkpoint hyperparameters but do not provide protocol-matched primary evidence comparing Qwen3-8B to the named alternative. The alternative's primary evidence was not provided in the checked sources.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### ByteDance-Seed/Seed-OSS-36B-Instruct — `insufficient-evidence`

- Task: Instruction following / chat
- Criteria: No primary-source comparative results for the alternative were located in the checked primary sources.
- Rationale: Checked Qwen3 primary sources lack protocol-matched comparative tables for this alternative; alternative primary-source evidence not provided.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### deepseek-ai/DeepSeek-R1-0528-Qwen3-8B — `insufficient-evidence`

- Task: Model identity / packaging comparison
- Criteria: No primary-source evidence for the alternative packaging was found in the checked canonical sources.
- Rationale: The Qwen3 technical report and Hugging Face model card provide upstream checkpoint identity; no canonical primary-source documentation for this alternative packaging was identified in the checked sources.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### deepseek-ai/DeepSeek-R1-Distill-Qwen-14B — `insufficient-evidence`

- Task: Cross-scale quality comparison
- Criteria: No primary-source checkpoint-matched comparative results for the alternative were found in checked sources.
- Rationale: Qwen3 technical report lists per-checkpoint hyperparameters but does not provide protocol-matched comparative benchmark tables for this third-party alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### HuggingFaceTB/SmolLM3-3B — `insufficient-evidence`

- Task: General document-ai tasks
- Criteria: No primary-source comparative results for the alternative were found in checked Qwen3 primary sources.
- Rationale: The Qwen3 technical report and HF model card do not include protocol-matched comparative data for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### ibm-granite/granite-3.3-8b-instruct — `insufficient-evidence`

- Task: Instruction following / chat
- Criteria: No primary-source comparative results for the alternative were located in the checked Qwen3 primary sources.
- Rationale: Qwen3 primary documentation does not provide protocol-matched comparative tables for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### ibm-granite/granite-4.1-8b — `insufficient-evidence`

- Task: General document-ai tasks
- Criteria: No primary-source comparative results for the alternative were located in the checked Qwen3 primary sources.
- Rationale: Qwen3 primary documentation does not include protocol-matched comparative tables for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### Microsoft Phi-4 Mini Instruct (provider page) — `insufficient-evidence`

- Task: Instruction following / chat
- Criteria: No primary-source comparative results for the alternative were present in the checked Qwen3 primary sources.
- Rationale: No protocol-matched comparative evidence available in checked Qwen3 sources; alternative primary-source evidence not supplied.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### mistralai/Devstral-Small-2507 — `insufficient-evidence`

- Task: General document-ai tasks
- Criteria: No primary-source comparative results for the alternative were present in checked Qwen3 sources.
- Rationale: Qwen3 primary documentation lacks protocol-matched comparative data for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### openbmb/MiniCPM4-8B — `insufficient-evidence`

- Task: Multimodal / document tasks
- Criteria: No primary-source comparative results for the alternative were present in the checked Qwen3 primary sources.
- Rationale: Qwen3 primary documentation does not include protocol-matched comparative tables for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### openbmb/MiniCPM5-1B — `insufficient-evidence`

- Task: Multimodal / small-model tradeoff
- Criteria: No primary-source comparative results for the alternative were present in the checked Qwen3 primary sources.
- Rationale: Qwen3 primary documentation does not include protocol-matched comparative tables for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### Qwen/Qwen3-0.6B — `insufficient-evidence`

- Task: Cross-scale comparison
- Criteria: Qwen3 technical report lists per-checkpoint architectural hyperparameters but does not provide protocol-matched per-checkpoint benchmark tables for direct numeric cross-scale comparisons in the checked documentation.
- Rationale: Per-checkpoint hyperparameters are reported in Table 1 of the technical report, but checkpoint-matched numeric benchmark rows for cross-scale comparisons are not present for the named datasets in the checked primary sources.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Qwen/Qwen3-1.7B — `insufficient-evidence`

- Task: Cross-scale comparison
- Criteria: Per-checkpoint hyperparameters present, but no protocol-matched numeric benchmark tables for cross-scale comparisons were found in the checked primary sources.
- Rationale: Checked technical report provides hyperparameters but not per-checkpoint benchmark numeric rows for direct comparison.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Qwen/Qwen3-14B — `insufficient-evidence`

- Task: Cross-scale comparison
- Criteria: Per-checkpoint hyperparameters present, but no protocol-matched numeric benchmark tables for cross-scale comparisons were found in the checked primary sources.
- Rationale: Checked technical report provides hyperparameters but not per-checkpoint benchmark numeric rows for direct comparison.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1

### Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 — `insufficient-evidence`

- Task: Cross-scale/instruction-tuned comparison
- Criteria: No protocol-matched comparative tables for this alternative were located in the checked Qwen3 primary sources.
- Rationale: Qwen3 primary documentation does not include the requested per-checkpoint numeric comparison rows for this alternative in the checked sources.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

### Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 — `insufficient-evidence`

- Task: Coding / instruction-tuned comparison
- Criteria: No protocol-matched comparative tables for this alternative were located in the checked Qwen3 primary sources.
- Rationale: Checked Qwen3 documentation lacks per-checkpoint numeric benchmark rows for this alternative.
- Comparison conditions: not reported
- Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

## Limitations and safety

### Limitations

- Per-checkpoint architectural hyperparameters for Qwen3-8B are reported (36 layers; 32 query heads / 8 key/value heads; untied embeddings; 128K context) in the Qwen3 technical report, which supports architecture-level assertions. Sources: https://arxiv.org/pdf/2505.09388, https://arxiv.org/html/2505.09388v1
- The Qwen3 technical report and Hugging Face model card do not publish reproduction-ready tokenizer implementation files (tokenizer.json, merges/SPM binaries, special-token mapping files) for Qwen3-8B in the checked canonical locations; only BBPE semantics and vocabulary-size are stated. Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B
- Evidence gap: the checked primary sources do not include explicit prompt templates, decoding hyperparameters, or the exact evaluation harness scripts required to reproduce the numeric benchmark entries implied in external drafts. Sources: https://arxiv.org/pdf/2505.09388, https://github.com/qwenLM/qwen3
- License for model weights and code is declared in the Hugging Face repository LICENSE file as Apache License, Version 2.0 (see HF LICENSE URL). Sources: https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE, https://huggingface.co/Qwen/Qwen3-8B

### Safety

- Evidence gap: primary sources (Qwen3 technical report PDF/HTML and the Hugging Face model card) do not document model-specific safety mitigations, automated content filters, PHI handling guidance, or deployment-specific data-retention/privacy procedures for Qwen3-8B. Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B
- Evidence gap: no clinical-use disclaimers, regulatory-approval statements, or expert-review workflows for safety-critical uses of Qwen3-8B were located in the checked primary sources. Sources: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-8B

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3 technical report (PDF)

- URL: https://arxiv.org/pdf/2505.09388
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv preprint PDF of the Qwen3 technical report containing architecture descriptions and per-checkpoint hyperparameters; used as the principal primary-source evidence for architectural and tokenizer claims.
- Scope: Qwen3 series technical report (includes Qwen3-8B per-checkpoint hyperparameters and family-level architecture descriptions)
- Supports: Qwen3 series family architecture (GQA, SwiGLU, RoPE, RMSNorm pre-norm, QK-Norm, removal of QKV-bias)
- Supports: Per-checkpoint hyperparameters for Qwen3-8B (36 layers; 32 query heads / 8 key/value heads; untied embeddings; context length 128K)
- Supports: Tokenizer semantics: BBPE and vocabulary size (151,669)

### Qwen3 technical report (HTML)

- URL: https://arxiv.org/html/2505.09388v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical arXiv HTML view of the Qwen3 technical report used as an alternative primary-format locator for tables/sections referenced in the dossier.
- Scope: Qwen3 series technical report (includes Qwen3-8B per-checkpoint hyperparameters and family-level architecture descriptions)
- Supports: Same architecture and per-checkpoint hyperparameter claims as the arXiv PDF

### Hugging Face model card: Qwen3-8B

- URL: https://huggingface.co/Qwen/Qwen3-8B
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: Official Hugging Face model card page for the upstream Qwen3-8B checkpoint; used to verify model-card metadata and the presence of a LICENSE file in the model repository.
- Scope: qwen-qwen3-8b (Hugging Face model card for Qwen3-8B)
- Supports: Official model-card landing page for Qwen3-8B
- Supports: Source location for LICENSE file (weights/code license declaration)

### Hugging Face LICENSE file for Qwen3-8B

- URL: https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: Exact LICENSE file published in the official Hugging Face Qwen3-8B repository declaring Apache License, Version 2.0 for the model weights and code.
- Scope: qwen-qwen3-8b (license for the Hugging Face Qwen3-8B repo)
- Supports: Apache License 2.0 declaration for model weights and code

### Qwen3 repository (official developer repository)

- URL: https://github.com/qwenLM/qwen3
- Publisher: qwenLM (GitHub)
- Type: `repository`
- Primary because: Official developer GitHub repository for the Qwen3 series used as the canonical developer release/announcement location referenced in the findings.
- Scope: Qwen3 series (repository-level resources and release manifest)
- Supports: Developer repository and recorded release date for the Qwen3 series

## Evidence gaps

- Evidence gap: explicit numeric benchmark table locators and reported numeric values for MMLU, MMLU-Redux, MMLU-Pro, SuperGPQA, BBH, GSM8K, MATH, EvalPlus, and MultiPL-E for the Qwen3-8B checkpoint were not found in the checked primary sources (checked https://arxiv.org/pdf/2505.09388 and https://huggingface.co/Qwen/Qwen3-8B).
- Evidence gap: explicit checkpoint revision tag or commit hash for Qwen3-8B is not present in the checked technical report (https://arxiv.org/pdf/2505.09388) or the Hugging Face model card (https://huggingface.co/Qwen/Qwen3-8B).
- Evidence gap: tokenizer implementation files (tokenizer.json, merges/SPM binaries, special-token mapping files) for Qwen3-8B are not published in the checked canonical locations (https://huggingface.co/Qwen/Qwen3-8B and https://github.com/qwenLM/qwen3); only BBPE semantics and vocabulary size are reported in the technical report (https://arxiv.org/pdf/2505.09388).
- Evidence gap: exact prompt templates, system/user message conventions, and decoding/prompting hyperparameters used in reported evaluations for Qwen3-8B are not provided in the checked primary sources (https://arxiv.org/pdf/2505.09388; https://huggingface.co/Qwen/Qwen3-8B).
- Evidence gap: explicit input truncation/cropping, batching behavior, and runtime decoding settings used for reported evaluations are not present in the checked primary sources (https://arxiv.org/pdf/2505.09388; https://github.com/qwenLM/qwen3).
- Evidence gap: the checked primary sources do not specify output object schema (raw logits vs. softmaxed probabilities vs. token-id streams) nor post-inference calibration guidance for Qwen3-8B (checked https://arxiv.org/pdf/2505.09388 and https://huggingface.co/Qwen/Qwen3-8B).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 19 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
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
- `medium` $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[7].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[8].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[8].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[1]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[2]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[3]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[4]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[5]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[6]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[7]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[8]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[9]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
