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

- Research key: `build-nvidia-com-colabfold-msa-search-d8cbe43c2f`
- Independent audit: `revised`
- Researched: `2026-07-23T23:13:24.054436+00:00`

The Forge variant build-nvidia-com-colabfold-msa-search-d8cbe43c2f is an NVIDIA-served MSA Search NIM that implements a GPU-accelerated MMSeqs2-based MSA search pipeline in ColabFold-style (cascaded) and AlphaFold2-style (single-pass) search modes. NVIDIA primary documentation and catalog pages describe the NIM's endpoints, pipeline stages (Search, Expand, Align, Filter, result2msa), default pre-indexed databases (Uniref30_2302, colabfold_envdb_202108, PDB70_220313), environment controls (e.g., NIM_GLOBAL_MAX_MSA_DEPTH, NIM_DISABLE_GPU_SERVER), and throughput benchmarks (sequences/sec) by GPU type and sequence-length bins. The inspected NVIDIA sources list container/NGC packaging metadata and release notes but do not report an exact upstream checkpoint tag, repository commit hash, or model-weight identifier packaged in the NIM. NVIDIA primary sources report throughput benchmarks but do not publish checkpoint-scoped downstream structure-prediction accuracy benchmarks for this exact NIM variant. No explicit PHI/clinical-data handling policy or clinical-use endorsement for this exact NIM was found in the inspected NVIDIA primary pages.

## Identity

- Upstream name: ColabFold MSA Search (NVIDIA NIM serving a GPU-accelerated MMSeqs2/ColabFold-style MSA search pipeline)
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: GPU-accelerated MMSeqs2-based multiple-sequence-alignment (MSA) search pipeline (Search, Expand, Align, Filter, result2msa); not a deep-learning parameterized model
- License: MIT; NVIDIA Software License Agreement and Product‑Specific Terms for AI Products
- Evidence: https://docs.api.nvidia.com/nim/reference/colabfold-msa-search, https://build.nvidia.com/colabfold/msa-search/deploy, https://catalog.ngc.nvidia.com/orgs/nim/colabfold/containers/msa-search/-, https://github.com/sokrypton/ColabFold, https://mmseqs.com/latest/userguide.pdf

## Selection

### Recommended

- **Generate multiple-sequence alignments (MSAs) to feed downstream protein-structure prediction workflows (AlphaFold2/ColabFold/OpenFold-style pipelines).** — NVIDIA documents the MSA Search NIM as a GPU-accelerated provider of MSAs and structural-template search outputs intended to inform downstream structural-prediction models and describes supported search styles ('alphafold2' and 'colabfold') and output formats suitable for downstream predictors.
  Scope: MSA Search NIM (build-nvidia-com-colabfold-msa-search-d8cbe43c2f) served by NVIDIA NIM endpoints (monomer and paired endpoints as documented).
  Evidence: https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html, https://build.nvidia.com/colabfold/msa-search/deploy, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html

### Conditional

- **Large-batch or deep-MSA generation under GPU-Server mode where global MSA-depth limits and GPU-indexed databases are required.** — Requires enabling GPU Server (GPU Server is default in later releases) and configuring NIM_GLOBAL_MAX_MSA_DEPTH at container startup; databases must be pre-indexed/compatible with the running MMSeqs2 version and placed per NVIDIA configuration (database indices in GPU memory for GPU Server).
  Scope: MSA Search NIM (build-nvidia-com-colabfold-msa-search-d8cbe43c2f) running GPU Server mode with configured database indices and environment variables.
  Evidence: https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.3.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/configure.html

### Avoid

- **Clinical diagnostics or medical decision support (PHI/clinical data processing) where validated clinical workflows and explicit PHI-handling policies are required.** — Evidence gap: The inspected NVIDIA primary sources for this NIM do not publish explicit clinical-use endorsements, validated clinical workflows, or PHI-specific handling guidance for this exact Forge variant; checkpoint-scoped clinical validation is not provided in the inspected pages.
  Scope: MSA Search NIM (build-nvidia-com-colabfold-msa-search-d8cbe43c2f)
  Evidence: https://build.nvidia.com/colabfold/msa-search/deploy, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html

## Input preparation

### Semantic inputs

- Required single-chain input parameter 'sequence' is a protein sequence string composed of the 20 standard amino-acid characters with support for unknown residue 'X'; documented length bounds are 1–4096 characters. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.3.0/release-notes.html
- Paired/complex inputs are supported via the paired endpoint which accepts multiple protein sequences (one per chain) in a single request and pairing strategies (e.g., 'greedy' and 'complete'). Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.1.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html
- Database selection is provided as a constrained list of configured database-name strings; the NIM exposes configured database names (e.g., 'uniref30_2302') via a metadata/config endpoint. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html

### Accepted formats

- Output alignment formats produced by the NIM include A3M and FASTA; default output_alignment_formats documented as 'a3m' in versioned API references. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html

### Preprocessing

- The NIM pipeline stages are documented as Search, Expand, Align, Filter, and result2msa (convert to A3M alignment); GPU-indexed databases are used for GPU Server operation. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/configure.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html

### Pre-submit validation

- Documented input-validation includes length bounds for 'sequence' (1–4096) and constrained database-name lists; incompatible or invalid inputs are rejected by the API as per API reference. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html
- When GPU Server is enabled, global MSA depth is governed by NIM_GLOBAL_MAX_MSA_DEPTH, which must be set at container startup and cannot be changed per request (environment-level control documented in release notes). Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/performance.html

### Task-specific formatting

- API parameter fields documented for predict endpoints include 'sequence' (single), 'sequences' (paired), 'databases', 'search_type' (e.g., 'alphafold2' or 'colabfold'), 'max_msa_sequences', 'output_alignment_formats', 'e_value', and 'iterations' with ranges/defaults documented in the versioned API reference. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html

## Output interpretation

### Outputs

- Primary NIM outputs are multiple-sequence-alignments in A3M (default) or FASTA format; response 'alignment' includes a 'format' field whose value is 'a3m' or 'fasta' as documented in API reference. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html
- The Structural Template Search endpoint returns structural template files in mmCIF format and includes fields 'structure' (mmCIF content) and 'format' ("mmcif"). Sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html

### Interpretation

- MSA quality and coverage materially influence downstream structure-prediction accuracy; NVIDIA documents that MSA outputs are intended to inform downstream predictors such as AlphaFold2/OpenFold. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/overview.html
- Per-residue confidence metrics (pLDDT/pTM) and predicted-aligned-error plots are outputs of downstream structure-prediction workflows that consume these MSAs, not outputs of the MSA Search NIM itself. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/overview.html

### Post-inference validation

- Post-inference validation of structure confidence (pLDDT/pTM/PAE) is performed by downstream structure-prediction workflows; the NIM documentation states its outputs feed those workflows but does not produce those downstream confidence metrics itself. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html

## Public benchmarks

### MSA search throughput (sequences per second) for AlphaFold2 search type (v2.0.0)

- Dataset/split: Default ColabFold databases: Uniref30_2302, colabfold_envdb_202108, PDB70_220313 / not reported
- Metric/value: sequences per second (seq/s) across defined sequence-length bins / AlphaFold2 search type on L40S: 1.83 seq/s for input lengths 0–200 aa (v2.0.0 performance table) (`higher-is-better`)
- Model scope: MSA Search NIM (build-nvidia-com-colabfold-msa-search-d8cbe43c2f) measured in v2.0.0 performance tables
- Conditions: Benchmarks conducted with GPU Server enabled (v2.0.0 documentation) and using the NIM's default ColabFold databases as documented for v2.0.0.
- Source: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/performance.html
- Locator: Performance tables for AlphaFold2 search type (L40S, 0–200 aa) in v2.0.0 performance page
- Caveat: Reported benchmarks measure throughput (seq/s) and do not measure downstream structure-prediction accuracy
- Caveat: Benchmarks depend on GPU type, sequence length bins, search type, and database configuration

### MSA search throughput (sequences per second) for AlphaFold2 search type (latest)

- Dataset/split: Default ColabFold databases: Uniref30_2302, colabfold_envdb_202108, PDB70_220313 / not reported
- Metric/value: sequences per second (seq/s) across defined sequence-length bins / AlphaFold2 search type on L40S: 1.94 seq/s for input lengths 0–200 aa (latest performance page) (`higher-is-better`)
- Model scope: MSA Search NIM (build-nvidia-com-colabfold-msa-search-d8cbe43c2f) measured in latest performance tables
- Conditions: Benchmarks conducted with GPU Server enabled (default) and environment variable NIM_GLOBAL_MAX_MSA_DEPTH set to 500 as documented on the latest performance page.
- Source: https://docs.nvidia.com/nim/bionemo/msa-search/latest/performance.html
- Locator: Latest performance tables for AlphaFold2 search type (L40S, 0–200 aa) on latest performance page
- Caveat: All benchmarks were conducted with the GPU Server enabled and NIM_GLOBAL_MAX_MSA_DEPTH set to 500 sequences (latest performance notes)
- Caveat: Paired MSA search performance is not directly comparable to monomer searches and tends to be slower for longer sequences due to per-chain searching overhead
- Caveat: Reported benchmarks measure throughput (seq/s) and do not measure downstream structure-prediction accuracy

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Protocol-matched comparisons between this MSA Search NIM and alternative structure-prediction workflows or other Forge candidates for MSA generation and downstream accuracy
- Criteria: Protocol-matched comparisons require identical input sequences, identical database versions, identical NIM/configuration, and explicit benchmark tables reporting the same metrics/splits; such like-for-like tables comparing this exact NIM to alternative Forge variants were not found in the inspected primary sources.
- Rationale: NVIDIA documentation and release notes describe NIM behavior and throughput but do not publish direct, protocol-matched comparison tables against alternative Forge variants or end-to-end downstream accuracy comparisons under identical conditions.
- Comparison conditions: No protocol-matched benchmark tables for identical inputs/databases/configurations across alternatives were identified in the inspected NVIDIA sources.
- Evidence: https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/performance.html

## Limitations and safety

### Limitations

- Evidence gap: The inspected NVIDIA primary sources do not report an exact upstream checkpoint tag, repository commit hash, or model-weight identifier packaged by NVIDIA for build-nvidia-com-colabfold-msa-search-d8cbe43c2f; exact checkpoint identity is not specified in the available NVIDIA pages. Sources: https://build.nvidia.com/colabfold/msa-search/deploy, https://catalog.ngc.nvidia.com/orgs/nim/colabfold/containers/msa-search/-, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html
- Benchmarks reported by NVIDIA for this NIM are throughput (sequences/sec) measures under specific runtime configurations and database sets; they are not measures of downstream structure-prediction accuracy and therefore do not substitute for checkpoint-scoped accuracy benchmarks. Sources: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/performance.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/performance.html, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/overview.html

### Safety

- Evidence gap: The inspected NVIDIA primary sources do not provide explicit PHI / clinical-data handling policies or explicit clinical-use restrictions for this Forge variant; users requiring PHI-safe operation must consult organizational policy and NVIDIA terms. Sources: https://build.nvidia.com/colabfold/msa-search/deploy, https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's MSA Search skill documents standard and paired searches, databases, A3M/FASTA artifacts, template behavior, validation, large local database requirements, and hosted/local path differences. Forge's exact route, storage design, image, and GPU matrix remain authoritative.
- [msa-search-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/msa-search-nim)

### `related-multi-model-pipeline`

The NVIDIA BioNeMo MSA-to-OpenFold3 meta-skill documents the A3M handoff between MSA Search and structure prediction. Treat its fixed examples as a workflow template; verify database choices, sequence/entity schema, MSA depth, exact Forge routes, and returned artifacts for the selected versions.
- [msa-structure-prediction-pipeline](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/meta-skills/msa-structure-prediction-pipeline)

## Primary sources

### MSA Search NIM API (v2.0.0) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/api-reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned API reference used to extract exact parameter names, ranges, defaults, endpoints, and response fields for the NIM.
- Scope: MSA Search NIM (v2.0.0) API reference
- Supports: Endpoint POST /biology/colabfold/msa-search/predict and paired endpoint paths
- Supports: Parameter bounds/defaults (sequence length 1–4096, output formats 'a3m'/'fasta')
- Supports: Response fields for structural template output and database metadata endpoints

### MSA Search performance page (v2.0.0) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/performance.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned performance page providing throughput benchmarks across GPUs and sequence-length bins for documented NIM versions.
- Scope: MSA Search NIM performance (v2.0.0)
- Supports: Throughput benchmarks (seq/s) by GPU and sequence-length bins for AlphaFold2 and ColabFold search types in v2.0.0
- Supports: Benchmark conditions: GPU Server enabled and default ColabFold databases (v2.0.0)

### MSA Search API (latest) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Latest API reference documenting endpoints including paired/monomer/structure-template predict endpoints and database metadata endpoints.
- Scope: MSA Search NIM (latest) API reference
- Supports: Paired MSA search endpoint path /biology/colabfold/msa-search/paired/predict (POST)
- Supports: Structural template search endpoint and mmCIF output fields
- Supports: Database configuration/metadata endpoints

### MSA Search release notes (2.1.0) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.1.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned NIM release notes introducing the paired MSA endpoint and describing pairing strategies.
- Scope: MSA Search NIM release 2.1.0
- Supports: Paired MSA Search endpoint and pairing strategies
- Supports: Paired endpoint input behavior

### MSA Search release notes (2.2.0) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned release notes documenting the Structural Template Search endpoint and default pre-indexed databases.
- Scope: MSA Search NIM release 2.2.0
- Supports: Structural Template Search endpoint and mmCIF outputs
- Supports: Default pre-indexed databases: Uniref30_2302, colabfold_envdb_202108, PDB70_220313
- Supports: Notes on merged alignment output behavior

### MSA Search release notes (2.3.0) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.3.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned release notes documenting input-character support, MMSeqs2 upgrade, GPU Server defaults, and environment controls.
- Scope: MSA Search NIM release 2.3.0
- Supports: Support for unknown residue 'X' in query sequences
- Supports: MMSeqs2 upgrade to version 18 (as documented in release notes)
- Supports: GPU Server enabled by default and NIM_DISABLE_GPU_SERVER control

### MSA Search release notes (latest) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Latest release notes documenting paired behavior, endpoint paths, and default database lists.
- Scope: MSA Search NIM release (latest)
- Supports: Paired MSA endpoint path and pairing strategies
- Supports: Default pre-indexed databases mapping and names

### MSA Search overview (latest) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical overview describing search styles, use of MSA outputs for downstream prediction, and use of GPU-accelerated MMSeqs2.
- Scope: MSA Search NIM (latest) overview
- Supports: Search styles: 'alphafold2' (single-pass) and 'colabfold' (cascaded)
- Supports: MSA outputs used for downstream structure prediction (AlphaFold2/OpenFold)
- Supports: Use of GPU-accelerated MMSeqs2

### MSA Search performance page (latest) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/latest/performance.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Latest performance page documenting throughput benchmarks and environment settings used in benchmarks.
- Scope: MSA Search NIM performance (latest)
- Supports: Latest throughput benchmarks (seq/s) across GPUs and sequence-length bins
- Supports: Benchmark conditions: GPU Server enabled and NIM_GLOBAL_MAX_MSA_DEPTH=500

### MSA Search NIM configuration and GPU Server documentation (latest) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/latest/configure.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Configuration page documenting pipeline stages, GPU Server behavior, and environment variables controlling MSA-depth and databases.
- Scope: MSA Search NIM configuration (latest)
- Supports: Pipeline stages (Search, Expand, Align, Filter, result2msa)
- Supports: NIM_GLOBAL_MAX_MSA_DEPTH and GPU Server requirements
- Supports: Database indexing requirements for GPU Server

### Build NVIDIA ColabFold MSA Search (deploy page) - NVIDIA Build

- URL: https://build.nvidia.com/colabfold/msa-search/deploy
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Forge Build/Deploy page for the ColabFold MSA Search NIM describing provisioning, Docker image, and run notes for the served variant.
- Scope: MSA Search NIM / Forge model deploy metadata
- Supports: NIM deployment image (nvcr.io/nim/colabfold/msa-search:latest) and run flags
- Supports: Provisioning and free-tier prototype note
- Supports: High-level MSA Search purpose and default database names

### NGC catalog entry for MSA Search container - NVIDIA NGC

- URL: https://catalog.ngc.nvidia.com/orgs/nim/colabfold/containers/msa-search/-
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: NGC catalog entry listing container version metadata and packaging for the MSA Search NIM container.
- Scope: MSA Search NIM container (NGC)
- Supports: Container packaging information and listed container version metadata (v2.5.0 noted in findings)

### ColabFold repository (Sokrypton) - upstream project

- URL: https://github.com/sokrypton/ColabFold
- Publisher: Sokrypton (GitHub)
- Type: `repository`
- Primary because: Canonical upstream ColabFold project repository referenced by NVIDIA documentation as the ColabFold-style pipeline implementation used by the NIM.
- Scope: ColabFold upstream project
- Supports: Upstream ColabFold project repository and instructions for MMseqs2 usage and GPU database setup referenced by NVIDIA

### MMseqs2 user guide (MMseqs official site)

- URL: https://mmseqs.com/latest/userguide.pdf
- Publisher: MMseqs (soedinglab)
- Type: `official-documentation`
- Primary because: Official MMSeqs2 user guide describing MMSeqs2 behavior, licensing, and GPU database setup used by ColabFold-style pipelines.
- Scope: MMSeqs2 user guide
- Supports: MMseqs2 implementation and database/indexing guidance used by the NIM
- Supports: License statement for MMseqs2 (MIT as documented on mmseqs.com user guide)

### MMseqs2 Nature Biotechnology paper (2017)

- URL: https://nature.com/articles/nbt.3988
- Publisher: Nature Biotechnology
- Type: `paper`
- Primary because: Canonical publication describing MMseqs2 and cited as the core algorithmic basis for the NIM's search pipeline.
- Scope: MMseqs2 algorithm publication
- Supports: Foundational description of MMseqs2 sensitive sequence searching used by GPU-accelerated implementations

### MSA Search NIM API (2.3.0) - NVIDIA

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.3.0/api-reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned API reference used for MMSeqs2 version endpoint details and compatibility notes.
- Scope: MSA Search NIM API (2.3.0)
- Supports: MMSeqs2 version endpoint (/biology/colabfold/msa-search/mmseqs2/version) returning mmseqs2_version string
- Supports: Compatibility note that custom database indices must match running MMSeqs2 version

### MSA Search framework release notes and BioNeMo framework context - NVIDIA

- URL: https://docs.api.nvidia.com/nim/reference/colabfold-msa-search
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: API-level documentation listing release history, container images, and framework-level licensing/terms for the NIM.
- Scope: MSA Search NIM (framework-level reference)
- Supports: Listed NIM release history and container image names
- Supports: Statements that training/evaluation are not applicable (not a deep-learning model)
- Supports: License and trial terms notes for the NIM

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/overview.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: colabfold-msa-search
- Supports: Exact independently audited claim citation

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/colabfold/msa-search
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: colabfold-msa-search
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: Exact upstream checkpoint tag, repository commit hash, or model-weight identifier packaged by NVIDIA for build-nvidia-com-colabfold-msa-search-d8cbe43c2f is not reported in the inspected primary sources (checked: deployment page, NGC catalog, API reference, and release notes).
- Evidence gap: No primary-source, checkpoint-scoped benchmark tables/figures were found that evaluate build-nvidia-com-colabfold-msa-search-d8cbe43c2f for downstream structure-prediction accuracy; NVIDIA reports throughput benchmarks but not checkpoint-scoped accuracy metrics for this NIM.
- Evidence gap: No explicit PHI / clinical-data handling policy or clinical-use restriction statement for this exact NIM was found in the inspected NVIDIA primary pages.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 27 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://colab.fold/mmseqs.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/sokrypton/ColabFold/wiki/Running-ColabFold-in-Docker Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://hub.docker.com/r/ddhmed/colabfold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/advanced-modeling-and-applications-of-predicted-protein-structures/customising-alphafold-structure-predictions/outputs-from-colabfold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ebi.ac.uk/training/online/courses/alphafold/advanced-modeling-and-applications-of-predicted-protein-structures/customising-alphafold-structure-predictions/outputs-from-colabfold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/openfold/openfold2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.conditionalUseCasesNotes: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.avoidUseCasesNotes: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/overview.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/colabfold/msa-search: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
