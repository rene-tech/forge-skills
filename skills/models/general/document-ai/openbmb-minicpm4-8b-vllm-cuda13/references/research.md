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

- Research key: `huggingface-co-openbmb-minicpm4-8b-116a2cb760`
- Independent audit: `revised`
- Researched: `2026-08-06T13:25:16.902719+00:00`

Checkpoint-scoped dossier for MiniCPM4-8B (8B parameters). Primary upstream artifacts (Hugging Face model card and repository, the MiniCPM paper on arXiv, checkpoint commit and tokenizer config, and the MiniCPM MCP demo README) document that MiniCPM4-8B is an efficient LLM designed for end-device use, supports long context (original_max_position_embeddings=32768 in the checkpoint config), uses bfloat16 dtype in the published config, and has a vocabulary size of 73,448 with rope_theta 10000. The arXiv family paper positions MiniCPM4 as ultra-efficient LLMs and lists evaluation comparisons at the family/checkpoint level. Psyche-R1 benchmark results for MiniCPM4-8B are reported in an arXiv HTML source. Several checkpoint-scoped implementation details (config.json fields, tokenizer.json) are present in the model repository/commit. Multiple important checkpoint-scoped items remain incompletely specified in upstream artifacts (per-dataset splits/protocols for reported scores in some demo READMEs, explicit post-inference calibration semantics, and exhaustive language-coverage documentation); these are listed under evidenceGaps. All claims below cite only the canonical upstream sources enumerated in sources.

## Identity

- Upstream name: MiniCPM4-8B
- Checkpoint/version: MiniCPM4-8B
- Immutable revision: bb2ae14cf59d4ca769c4e42ece54cc3b82a58ef7
- Parameter scale: 8B
- Architecture/head: Llama-style decoder with grouped-query attention (MiniCPM-specific grouped-query attention), LongRoPE, RMSNorm, and SwiGLU (as described in upstream artifacts and support notes)
- License: Apache-2.0
- Evidence: https://huggingface.co/openbmb/MiniCPM4-8B, https://arxiv.org/abs/2506.07900, https://github.com/openbmb/minicpm, https://github.com/OpenBMB/MiniCPM/blob/main/demo/minicpm4/MCP/README_en.md, https://huggingface.co/openbmb/MiniCPM4-8B/commit/bb2ae14cf59d4ca769c4e42ece54cc3b82a58ef7, https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/tokenizer.json, https://arxiv.org/html/2508.10848v3, https://github.com/huggingface/transformers/issues/47732, https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE

## Selection

### Recommended

- **Conversational AI and chat/instruction-following in English and Chinese** — The upstream Hugging Face model card and associated repository documentation describe chat and instruction-following uses for MiniCPM4-8B and present it as a text-only conversational model.
  Scope: MiniCPM4-8B
  Evidence: https://huggingface.co/openbmb/MiniCPM4-8B, https://github.com/openbmb/minicpm
- **Long-context summarization and other long-context tasks (up to the checkpoint's original_max_position_embeddings)** — The MiniCPM4-8B checkpoint config sets original_max_position_embeddings to 32768, and the model card and demo materials describe long-context capabilities.
  Scope: MiniCPM4-8B (original_max_position_embeddings=32768 per checkpoint config)
  Evidence: https://huggingface.co/openbmb/MiniCPM4-8B/commit/bb2ae14cf59d4ca769c4e42ece54cc3b82a58ef7, https://huggingface.co/openbmb/MiniCPM4-8B
- **Edge- and resource-constrained deployments where efficiency is required** — The canonical MiniCPM4 family paper and the Hugging Face model card emphasize the family’s design and evaluation goals focused on ultra-efficient, end-device-capable LLMs.
  Scope: MiniCPM4-8B (family-design claims apply at checkpoint scale as described in the paper and model card)
  Evidence: https://arxiv.org/abs/2506.07900, https://huggingface.co/openbmb/MiniCPM4-8B

### Conditional

- **Domains requiring rigorous downstream validation or specialized domain knowledge (e.g., scientific, legal, or clinical workflows)** — Require explicit downstream validation, expert review of outputs, and task-specific evaluation because upstream sources do not document clinical validation or PHI handling guarantees for the checkpoint.
  Scope: MiniCPM4-8B
  Evidence: https://github.com/openbmb/minicpm, https://arxiv.org/abs/2506.07900
- **Tool-enabled agent usage via MCP (agent that calls external tools)** — Use only where MCP tool integration is validated for the deployment scenario; the MCP demo README reports that MiniCPM4-MCP is built on MiniCPM4-8B and supports tool calling, but deployment-dependent validation is required.
  Scope: MiniCPM4-8B (as used in MiniCPM4-MCP demo)
  Evidence: https://github.com/OpenBMB/MiniCPM/blob/main/demo/minicpm4/MCP/README_en.md, https://huggingface.co/openbmb/MiniCPM4-8B

### Avoid

- **High-stakes clinical, medical, legal, or PHI-sensitive decision making** — No explicit clinical validation, PHI-handling guarantees, or clinical-safety procedures are documented for the MiniCPM4-8B checkpoint in the canonical upstream sources.
  Scope: MiniCPM4-8B
  Evidence: https://github.com/openbmb/minicpm, https://arxiv.org/abs/2506.07900

## Input preparation

### Semantic inputs

- Textual inputs (chat/instruction prompts) in English and Chinese are the documented input modality for MiniCPM4-8B. Sources: https://huggingface.co/openbmb/MiniCPM4-8B, https://github.com/openbmb/minicpm

### Accepted formats

- Upstream artifacts document text-only usage for the MiniCPM4 family and checkpoint; no multimodal input formats are documented for the checkpoint in the cited sources. Sources: https://huggingface.co/openbmb/MiniCPM4-8B, https://github.com/openbmb/minicpm

### Preprocessing

- Checkpoint config indicates tokenizer/vocabulary details and model dtype: vocab_size=73448, torch_dtype=bfloat16, rope_theta=10000, original_max_position_embeddings=32768 (checkpoint config fields). Sources: https://huggingface.co/openbmb/MiniCPM4-8B/commit/bb2ae14cf59d4ca769c4e42ece54cc3b82a58ef7, https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/tokenizer.json
- The upstream tokenizer artifact and Transformers support notes indicate use of a Llama-style tokenizer implementation for MiniCPM4 checkpoints. Sources: https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/tokenizer.json, https://github.com/huggingface/transformers/issues/47732

### Pre-submit validation

- No explicit upstream input-validation rules beyond standard tokenization and token-length constraints are documented for the checkpoint in the cited sources. Sources: https://huggingface.co/openbmb/MiniCPM4-8B, https://huggingface.co/openbmb/MiniCPM4-8B/commit/bb2ae14cf59d4ca769c4e42ece54cc3b82a58ef7

### Task-specific formatting

- The upstream PR/README and demo materials include chat templates and tokenization artifacts referenced in the model repository; explicit canonical prompt-template tokens for the checkpoint (e.g., a definitive <|im_start|> / <|im_end|> template) are not fully enumerated as a single authoritative template in the cited sources. Sources: https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/README.md, https://github.com/OpenBMB/MiniCPM/blob/main/demo/minicpm4/MCP/README_en.md

## Output interpretation

### Outputs

- Primary upstream outputs are free-form text generations (string outputs) from the causal language model head. Sources: https://huggingface.co/openbmb/MiniCPM4-8B, https://arxiv.org/abs/2506.07900

### Interpretation

- Upstream sources do not document checkpoint-scoped post-inference calibration semantics or confidence-score interpretation; users should treat outputs as uncalibrated model-generated text unless they implement task-specific calibration. Sources: https://huggingface.co/openbmb/MiniCPM4-8B, https://arxiv.org/abs/2506.07900

### Post-inference validation

- Evidence gap: The upstream artifacts do not specify post-inference validation, calibration, or recommended confidence thresholds for MiniCPM4-8B; downstream validation is required.

## Public benchmarks

### Psyche-R1 benchmark overall and subtask scores (as reported)

- Dataset/split: Psyche-R1 / not reported
- Metric/value: overall average score / 60.46 (`higher-is-better`)
- Model scope: MiniCPM4-8B (as reported in Psyche-R1 results)
- Conditions: As reported in the Psyche-R1 results table in the cited arXiv HTML; the findings do not provide full protocol detail in the cited source fragment.
- Source: https://arxiv.org/html/2508.10848v3
- Locator: Psyche-R1 benchmark results table (arXiv HTML)
- Caveat: The cited arXiv HTML reports scores but the research findings do not provide detailed protocol/split descriptions or full experimental conditions for reproducibility.

### Psyche-R1 benchmark - generative metrics

- Dataset/split: Psyche-R1 / not reported
- Metric/value: R-1 / 65.62 (`higher-is-better`)
- Model scope: MiniCPM4-8B (as reported in Psyche-R1 results)
- Conditions: As reported in the Psyche-R1 results table in the cited arXiv HTML; protocol details not fully enumerated in the cited fragment.
- Source: https://arxiv.org/html/2508.10848v3
- Locator: Psyche-R1 benchmark results table (arXiv HTML)
- Caveat: Protocol details and dataset splits are not specified in the provided source fragment.

## Comparisons

### Qwen3-8B — `insufficient-evidence`

- Task: Psyche-R1-style benchmark comparison as referenced by the MiniCPM4 family paper
- Criteria: Upstream arXiv paper lists Qwen3-8B as a baseline for MiniCPM4-8B comparisons, but the research findings do not include primary checkpoint-scoped sources for the alternative with matching protocol details.
- Rationale: The MiniCPM4 paper references Qwen3-8B as a baseline, but the dossier’s primary-evidence set lacks direct, protocol-matched primary artifacts for the alternative; therefore a task- and protocol-specific comparison cannot be supported from the available findings.
- Comparison conditions: Insufficient primary-evidence for the alternative under identical protocol conditions in the available findings.
- Evidence: https://arxiv.org/abs/2506.07900

## Limitations and safety

### Limitations

- The upstream repository and model card emphasize that generated content must be evaluated by users and do not provide clinical validation; this frames limitations around risk, hallucination, and responsibility for outputs. Sources: https://github.com/openbmb/minicpm, https://huggingface.co/openbmb/MiniCPM4-8B

### Safety

- No explicit PHI-handling, clinical-safety guidelines, or certified clinical validation are documented for MiniCPM4-8B in the cited upstream sources; treat the checkpoint as a general-purpose model requiring downstream governance for sensitive data. Sources: https://github.com/openbmb/minicpm, https://arxiv.org/abs/2506.07900

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MiniCPM4-8B model card (OpenBMB)

- URL: https://huggingface.co/openbmb/MiniCPM4-8B
- Publisher: HuggingFace / OpenBMB
- Type: `model-card`
- Primary because: Canonical upstream Hugging Face model card for the MiniCPM4-8B checkpoint; contains intended uses and checkpoint-level metadata.
- Scope: openbmb/MiniCPM4-8B
- Supports: intended uses
- Supports: long-context claims
- Supports: checkpoint metadata references

### MiniCPM4: Ultra-Efficient LLMs on End Devices (arXiv)

- URL: https://arxiv.org/abs/2506.07900
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing the MiniCPM4 family, listed baselines and family-level evaluation and architecture claims.
- Scope: MiniCPM4 family / MiniCPM4-8B (family-level paper and checkpoint references)
- Supports: architecture overview
- Supports: family design goals (efficiency, end-device focus)
- Supports: baseline comparisons listing

### OpenBMB MiniCPM GitHub repository (root)

- URL: https://github.com/openbmb/minicpm
- Publisher: OpenBMB
- Type: `repository`
- Primary because: Official repository containing code, demo materials, and repository-level documentation and license for MiniCPM family.
- Scope: MiniCPM family / MiniCPM4-8B
- Supports: repository README and demonstrations
- Supports: deployment and demo guidance
- Supports: general implementation notes

### MiniCPM-MCP demo README (English)

- URL: https://github.com/OpenBMB/MiniCPM/blob/main/demo/minicpm4/MCP/README_en.md
- Publisher: OpenBMB
- Type: `repository`
- Primary because: Demo materials that document MiniCPM4-MCP built on MiniCPM4-8B and describe MCP tool-calling capabilities and demo-reported evaluation notes.
- Scope: MiniCPM4-8B (used in MCP demo)
- Supports: MCP demo description
- Supports: claims that MiniCPM4-MCP is built on MiniCPM4-8B
- Supports: demo-reported capabilities and tool integration

### MiniCPM4-8B checkpoint commit (model config)

- URL: https://huggingface.co/openbmb/MiniCPM4-8B/commit/bb2ae14cf59d4ca769c4e42ece54cc3b82a58ef7
- Publisher: HuggingFace / OpenBMB
- Type: `repository`
- Primary because: Checkpoint-specific commit exposing the model config.json fields (original_max_position_embeddings, vocab_size, torch_dtype, rope_theta) used to verify checkpoint-scoped implementation details.
- Scope: MiniCPM4-8B (checkpoint config)
- Supports: original_max_position_embeddings=32768
- Supports: vocab_size=73448
- Supports: torch_dtype=bfloat16
- Supports: rope_theta=10000

### MiniCPM4-8B tokenizer artifact (tokenizer.json)

- URL: https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/tokenizer.json
- Publisher: HuggingFace / OpenBMB
- Type: `repository`
- Primary because: Upstream tokenizer artifact for the checkpoint used to verify tokenizer format and Llama-style tokenizer usage.
- Scope: MiniCPM4-8B (tokenizer)
- Supports: tokenizer format
- Supports: tokenizer implementation hints

### Psyche-R1 benchmark results (arXiv HTML)

- URL: https://arxiv.org/html/2508.10848v3
- Publisher: arXiv
- Type: `paper`
- Primary because: ArXiv HTML page that reports Psyche-R1 benchmark scores for MiniCPM4-8B used by the dossier for checkpoint-scoped benchmark claims.
- Scope: MiniCPM4-8B (Psyche-R1 reported results)
- Supports: Psyche-R1 benchmark numeric scores

### HuggingFace Transformers issue discussing MiniCPM4 support and implementation notes

- URL: https://github.com/huggingface/transformers/issues/47732
- Publisher: HuggingFace / Transformers
- Type: `official-documentation`
- Primary because: Issue contains authoritative implementation notes about model attention layout, tokenizer usage, and supported checkpoint keys as reported by maintainers and integrators; used here only for implementation-layout corroboration present in the research findings.
- Scope: MiniCPM4 family / MiniCPM4-8B
- Supports: attention layout and implementation notes
- Supports: Llama-style tokenizer usage
- Supports: native Transformers support scope notes

### MiniCPM repository LICENSE (Apache-2.0)

- URL: https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE
- Publisher: OpenBMB
- Type: `repository`
- Primary because: Repository license file establishing the project/code license for MiniCPM artifacts.
- Scope: MiniCPM family / MiniCPM4-8B
- Supports: Apache-2.0 license for repository artifacts

### MiniCPM4-8B model card (OpenBMB) — cited revision/file

- URL: https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/README.md
- Publisher: HuggingFace / OpenBMB
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: openbmb/MiniCPM4-8B
- Supports: Exact audited claim citation

## Evidence gaps

- Exact dataset/split/protocol mappings for scores reported in some demo README materials (e.g., MCP README) are not enumerated in the cited upstream artifacts; the repo README lists scores but the research findings do not map those scores to explicit dataset splits.
- Post-inference calibration semantics, recommended confidence thresholds, or checkpoint-scoped calibrated scorers for MiniCPM4-8B are not documented in the cited upstream sources.
- Comprehensive, checkpoint-scoped documentation of language coverage beyond English and Chinese is not present in the cited upstream model card or repository artifacts.
- Detailed per-layer architectural hyperparameters (beyond the high-level architecture notes found in family paper and integration notes) for the exact 8B variant are not fully enumerated in the provided findings.
- Direct, protocol-matched primary-evidence comparisons between MiniCPM4-8B and specific Forge peer checkpoints (with matching dataset splits and evaluation protocol) are not present in the available findings; the family paper lists baseline names but the dossier lacks protocol-matched primary artifacts for many alternatives.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/openbmb/MiniCPM4-8B/blob/refs%2Fpr%2F4/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
