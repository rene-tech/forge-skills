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

- Research key: `docs-nvidia-com-nim-large-language-models-1-15-0-text-to-sql-model-html-86b0cae1d6`
- Independent audit: `revised`
- Researched: `2026-07-23T22:13:55.062563+00:00`

This dossier is checkpoint-scoped to the NGC/NIM packaged container nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container tag/version 1.15.1) as documented on NVIDIA NGC and NIM pages. Primary NVIDIA sources identify the package name, domain specialization (healthcare), intended developer/researcher audience, NGC access/governing terms, and supported hardware/precision profiles. NVIDIA NIM Text-to-SQL documentation and the NVIDIA Nemo Text-to-SQL recipe page specify the Text-to-SQL workflow semantics (DDL + question -> SQL), include system-prompt text used in the recipe, and describe desired SQL properties (executable, reference only provided schema). Primary sources do not publish an immutable checkpoint revision hash, detailed tokenizer configuration (merges/vocab/vocab size/special tokens/normalization), canonical prompt templates for the packaged checkpoint beyond the Nemo recipe system prompts, truncation rules/max token lengths, checkpoint-scoped Text2SQL correctness/accuracy numbers on canonical datasets, or checkpoint-scoped training-data provenance. These absences are recorded explicitly as evidence gaps with the exact NVIDIA pages checked.

## Identity

- Upstream name: nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0
- Checkpoint/version: 1.15.1
- Immutable revision: not reported
- Parameter scale: approximately 8 billion parameters (indicated by "8B" in the model name)
- Architecture/head: Llama 3.1 Nemotron Nano 8B reasoning model (Text-to-SQL head, healthcare domain)
- License: Governed by NVIDIA Software License Agreement; Product‑Specific Terms for NVIDIA AI Products; NVIDIA Open Model License; references Llama 3.1 Community License Agreement
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0/-/governing-terms, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://docs.nvidia.com/nim/large-language-models/latest/support-matrix.html

## Selection

### Recommended

- **Translate natural-language healthcare analytics questions plus database schema DDL into executable SQL queries (Text‑to‑SQL).** — NIM Text-to-SQL documentation describes the Text-to-SQL workflow semantics requiring table definitions (DDL) plus a natural-language question and specifies the model's role to generate executable SQL over the provided schema; the NGC container metadata for the packaged checkpoint names it as a healthcare Text-to-SQL reasoning model.
  Scope: nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container tag 1.15.1)
  Evidence: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0
- **Build developer or research tooling for clinical analytics where generated SQL is validated before execution (research, prototyping, and analyst-assist use cases).** — NGC container metadata describes the packaged checkpoint as enabling developers and researchers to build self-service analytics and research tools for clinical users; NIM Text-to-SQL documentation provides the workflow semantics to produce SQL from DDL + question which matches developer/research tool prototypes.
  Scope: nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container tag 1.15.1)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html

### Conditional

- **Deploy generated SQL within clinical decision support or operational systems that affect patient care.** — Require institution-specific validation, execution-harness testing, schema-aware execution checks, and expert (clinician/DBA) review before any production execution that could affect patient care. Primary NVIDIA sources do not state clinical validation, certification, or mandated deployment safeguards for this packaged checkpoint.
  Scope: nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container tag 1.15.1)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html

### Avoid

- **Use as a clinically validated diagnostic or decision‑making system without further validation.** — Primary NVIDIA sources describe the package as intended for developers and researchers and do not state that the checkpoint is clinically validated or certified for direct clinical decision‑making; no checkpoint-scoped regulatory certification or clinical validation statements are published on the checked NVIDIA pages.
  Scope: nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container tag 1.15.1)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0/-/governing-terms, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html

## Input preparation

### Semantic inputs

- Provide a natural-language question (text) and database table definitions expressed as Data Definition Language (DDL). Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html
- Packaged NGC container metadata identifies input modalities as text and schema (DDL) for the healthcare Text-to-SQL model. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

### Accepted formats

- NIM Text-to-SQL workflow requires providing table definitions using DDL together with a natural-language instruction/question to generate SQL. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html

### Preprocessing

- Primary NVIDIA packaging and NIM pages checked do not specify tokenizer name, tokenizer configuration (merges/vocab), vocabulary size, special tokens, normalization/casing rules, or exact tokenization/truncation algorithm for the packaged checkpoint. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html
- NIM supported-models documentation lists supported hardware/precision profiles (e.g., BF16 TRT-LLM) but does not describe input normalization or tokenizer behavior for this packaged checkpoint. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html

### Pre-submit validation

- Primary NVIDIA documentation and container metadata do not publish explicit input-validation rules (for example: max schema size, DDL validation rules, automatic schema chunking, or truncation direction) for this packaged checkpoint. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

### Task-specific formatting

- NVIDIA Nemo Text-to-SQL recipe documents system prompts used in the Text-to-SQL workflow (for example: a system prompt string "You are an expert at generating clear and specific SQL tasks.") and describes SQL-context columns and expectations for generated SQL formatting and executability; the packaged NGC container and NIM Text-to-SQL docs describe the high-level DDL+question task but do not publish a single canonical prompt template and full default inference hyperparameter table for the packaged checkpoint. Sources: https://docs.nvidia.com/nemo/datadesigner/recipes/code-generation/text-to-sql, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

## Output interpretation

### Outputs

- Model outputs are executable SQL text and additional explanatory text (output modalities listed as SQL and text in the NGC container metadata and NIM documentation). Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html

### Interpretation

- NIM Text-to-SQL documentation and the NGC container page specify that generated SQL must be executable and reference only tables/columns in the provided context, but primary sources do not define SQL dialect constraints, canonical formatting rules, allowance of comments, or semantics for returned confidences or multiple candidate SQLs for the packaged checkpoint. Sources: https://docs.nvidia.com/nemo/datadesigner/recipes/code-generation/text-to-sql, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

### Post-inference validation

- Primary sources do not publish calibration scores, per-token logits, or a canonical execution-based correctness validation harness for this packaged checkpoint; NIM documentation documents deterministic inference settings (temperature=0) in the Text-to-SQL workflow but no checkpoint-scoped accuracy benchmarks are published on the checked pages. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0
- Downstream validation recommended by this dossier (execution-against-schema checks and human expert review) is necessary because primary NVIDIA sources do not prescribe a specific validation protocol for correctness prior to executing generated SQL in production. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### BioMistral-7B — `insufficient-evidence`

- Task: Text-to-SQL (healthcare context)
- Criteria: No primary-source, checkpoint-scoped Text2SQL accuracy or runtime results for the alternative were located in the NVIDIA pages checked; a canonical upstream model-card/paper for the alternative was not found among the NVIDIA primary sources inspected.
- Rationale: This dossier examined NVIDIA NIM and NGC pages for the packaged checkpoint and did not find primary-source task-matched evidence for BioMistral-7B on those NVIDIA pages. Without a canonical upstream primary source (model-card/paper) for the alternative checked here, a task- and protocol-matched comparison cannot be supported from the NVIDIA pages inspected.
- Comparison conditions: Comparison withheld due to absence of task-matched primary evidence for the alternative on the inspected NVIDIA pages.
- Evidence: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

### BioMedLM-2.7B — `insufficient-evidence`

- Task: Text-to-SQL (healthcare context)
- Criteria: No primary-source, checkpoint-scoped Text2SQL accuracy or runtime results for the alternative were located in the NVIDIA pages checked; a canonical upstream model-card/paper for the alternative was not found among the NVIDIA primary sources inspected.
- Rationale: This dossier examined NVIDIA NIM and NGC pages for the packaged checkpoint and did not find primary-source task-matched evidence for BioMedLM-2.7B on those NVIDIA pages. Without a canonical upstream primary source (model-card/paper) for the alternative checked here, a task- and protocol-matched comparison cannot be supported from the NVIDIA pages inspected.
- Comparison conditions: Comparison withheld due to absence of task-matched primary evidence for the alternative on the inspected NVIDIA pages.
- Evidence: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

## Limitations and safety

### Limitations

- Primary sources describe the model as a reasoning model post‑trained for the healthcare domain but do not state that this checkpoint is clinically validated or certified for clinical decision-making. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html
- The NGC container governing terms and NGC container metadata indicate the package is provided under NVIDIA licensing/governing terms and requires NGC subscription access; primary sources do not provide checkpoint-scoped training-data provenance or an immutable revision hash for the packaged checkpoint. Sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0/-/governing-terms, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0
- NIM supported-models documentation lists GPU and precision requirements and BF16 TRT‑LLM buildable profile support but the checked NVIDIA pages do not publish checkpoint-scoped Text2SQL correctness/accuracy benchmarks on canonical datasets. Sources: https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html
- Primary sources do not specify tokenizer configuration, canonical prompt templates for the packaged checkpoint, truncation policy, SQL dialect targeting, multi-candidate output formats, or exposed confidence semantics for the packaged checkpoint. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html

### Safety

- Primary NVIDIA sources (NGC container page and NIM Text-to-SQL documentation) do not include explicit statements about PHI handling procedures or mandated clinical regulatory certifications for this packaged checkpoint; users must follow institutional policies and applicable law when handling PHI. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html
- Access to the container requires NGC subscription and the container is governed by NVIDIA licensing/governing-terms; users should ensure compliance with the listed licenses and NGC access requirements. Sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0/-/governing-terms, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0

## Related upstream agent skills

### `related-model-workflow`

NVIDIA's Nemotron customization skill is first-party guidance for curating, training, evaluating, converting, and optimizing Nemotron-family checkpoints in the Nemotron repository. It is not an inference payload or Nebius deployment contract; verify the exact listed checkpoint and use the Forge/Serverless instructions for serving.
- [nemotron-customize](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-customize)

## Primary sources

### NGC container page: Llama-3.1-Nemotron-Nano-8B-Healthcare-Text2sql-v1.0 (teams view)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0
- Publisher: NVIDIA NGC (NIM)
- Type: `official-documentation`
- Primary because: First-party NVIDIA NGC container page naming the packaged checkpoint, describing intended use, model identity, and listing the container version tag.
- Scope: nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container/packaged checkpoint)
- Supports: Model identifier and packaged checkpoint name
- Supports: Container intended audience (developers/researchers)
- Supports: Container version tag 1.15.1 (container metadata)
- Supports: Statements about packaging, readiness for developer/research use

### NGC container governing terms for Llama-3.1-Nemotron-Nano-8B-Healthcare-Text2sql-v1.0

- URL: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0/-/governing-terms
- Publisher: NVIDIA NGC (NIM)
- Type: `official-documentation`
- Primary because: Governing terms page linked from the NGC container providing licensing and NGC access/subscription requirements for the container.
- Scope: Governing terms for nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 container
- Supports: NGC subscription/access requirement
- Supports: Licensing/governing-terms statements referenced by the container

### NIM Text-to-SQL model documentation (NIM 1.15.0)

- URL: https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM documentation describing Text-to-SQL task semantics, instruction to provide DDL + question, deterministic setting mention, and out-of-scope behavior.
- Scope: NIM Text-to-SQL documentation used to interpret the packaged checkpoint's task semantics
- Supports: Text-to-SQL workflow semantics (DDL + question -> SQL)
- Supports: Instruction to provide table definitions using DDL
- Supports: Deterministic inference setting mention and out-of-scope behavior

### NIM supported models page (1.15.0)

- URL: https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official supported-models listing that maps catalog identifiers to container tags and lists supported hardware/precision profiles for NIM 1.15.0.
- Scope: Supported-models listing for NIM 1.15.0 including the Llama-3.1-Nemotron-Nano-8B-Healthcare-Text2sql-v1.0 entry
- Supports: Catalog identifier nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 mapped to container tag 1.15.1
- Supports: Supported GPU families and BF16 TRT-LLM buildable profile
- Supports: Hardware/precision requirements

### NIM support matrix (latest)

- URL: https://docs.nvidia.com/nim/large-language-models/latest/support-matrix.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM support matrix listing certified NIMs, used to verify presence of the packaged checkpoint in NVIDIA's support matrix.
- Scope: Support matrix entries for certified NIMs including the packaged checkpoint
- Supports: Presence of the catalog identifier nvidia/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 in NVIDIA's support matrix

### NVIDIA Nemo Text-to-SQL recipe (system prompts and SQL expectations)

- URL: https://docs.nvidia.com/nemo/datadesigner/recipes/code-generation/text-to-sql
- Publisher: NVIDIA NEMO (NIM documentation)
- Type: `official-documentation`
- Primary because: Official NVIDIA Nemo recipe page documenting system prompts (e.g., "You are an expert at generating clear and specific SQL tasks.") and explicit SQL generation expectations used by NIM Text-to-SQL workflows.
- Scope: Nemo Text-to-SQL recipe used by NIM to define system prompts and expected SQL output properties
- Supports: System prompt text and sql_prompt/sql_context column definitions
- Supports: Requirements that generated SQL be executable and reference only provided schema
- Supports: Readability and relevance scoring rubric described in the recipe documentation

## Evidence gaps

- Evidence gap: Checkpoint immutable revision hash — inspected https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 and https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0/-/governing-terms (container metadata and governing-terms pages) and found no published immutable checkpoint revision identifier.
- Evidence gap: Exact tokenizer name and tokenizer configuration (merges/vocab, vocabulary size, special tokens, normalization/casing rules) — inspected https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0, https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html, and https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html and found no tokenizer configuration for the packaged checkpoint.
- Evidence gap: Canonical prompt templates, system prompts beyond the Nemo recipe, and default inference hyperparameters (max_output_tokens, temperature defaults, top_k/top_p, stop tokens) for the packaged checkpoint — inspected https://docs.nvidia.com/nemo/datadesigner/recipes/code-generation/text-to-sql and https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html and found the Nemo recipe system prompt but no single canonical prompt template or full inference-hyperparameter table published for the packaged NGC checkpoint.
- Evidence gap: Truncation/cropping rules and max token lengths for inputs and outputs (truncation direction, schema truncation policy, automatic chunking) — inspected https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 and found no published truncation or automatic chunking policy for the packaged checkpoint.
- Evidence gap: Exact numeric runtime latency/throughput values and units for the packaged checkpoint — inspected https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 and found hardware/precision requirements but no checkpoint-scoped numeric latency or throughput rows.
- Evidence gap: Checkpoint-scoped Text2SQL correctness/accuracy benchmarks on canonical public datasets (dataset name/version/split, metric, numeric value) — inspected https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html (no benchmark tables/figures/sections reporting checkpoint-scoped Text2SQL accuracy), https://docs.nvidia.com/nim/large-language-models/1.15.0/supported-models.html (no benchmark tables), and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 (container metadata page; no benchmark tables).
- Evidence gap: SQL dialect targeting, canonical SQL formatting rules, allowance of comments in outputs, multi-candidate SQL outputs, and returned confidence scores — inspected https://docs.nvidia.com/nemo/datadesigner/recipes/code-generation/text-to-sql and https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html and found descriptions of desired SQL properties but no checkpoint-scoped statements about dialect targeting or exposed confidence semantics for the packaged checkpoint.
- Evidence gap: Checkpoint-scoped training-data descriptions and domain provenance (datasets, curation, or filtering) — inspected https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 and https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html and found no checkpoint-scoped training-data provenance published.
- Evidence gap: NIM wrapper preprocessing specifics (whether NIM performs tokenization with a named tokenizer, DDL parsing/conversion, schema normalization, or passes DDL/prompt unchanged to the upstream checkpoint) — inspected https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 and found no NIM wrapper preprocessing implementation details for this packaged checkpoint.
- Evidence gap: Direct primary-source, checkpoint-scoped model-card/paper or supported-models listing for Forge peer alternatives (e.g., BioMistral-7B, BioMedLM-2.7B) on the inspected NVIDIA pages — checked https://docs.nvidia.com/nim/large-language-models/1.15.0/text-to-sql-model.html and https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemotron-nano-8b-healthcare-text2sql-v1.0 and found no canonical upstream primary-source entries for those alternatives on the NVIDIA pages inspected.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
