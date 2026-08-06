# Protein Structure model selection

- Category: `healthcare`
- Group: `protein-structure`
- Independent audit: `revised`
- Researched: `2026-07-23T20:27:42.027869+00:00`

Protein-structure workflow tasks relevant to healthcare R&D using one or both provided Forge NIMs: (a) standalone MSA generation and structural-template search from one or more amino-acid sequences; (b) single-sequence structure prediction without external MSA/templates; (c) structure prediction consuming externally-provided MSA and/or template files; (d) paired MSA generation for protein complexes (paired/complex MSA); (e) combined pipelines where MSA generation and structure-prediction are separate components executed serially. Out of scope: runtime/latency/GPU throughput as evidence of model quality, and any claims about checkpoints or variants not documented in the cited primary sources. The dossier does not assume support for fine-tuning or adapter updates unless explicitly stated in a cited primary source.

## Questions to answer before selecting

- Do I require a standalone MSA generation step (yes/no)?
- Do I require paired MSA support for protein complexes (yes/no)?
- Do I need the model to produce a 3D protein structure (PDB/mmCIF) from sequence input (yes/no)?
- Will I supply an external MSA and/or template files to the structure-prediction step (yes/no)?
- What is the maximum sequence length I must support (number of amino-acid residues)?
- Is a specific output alignment format required (a3m, fasta)?
- Is a specific MSA depth or maximum number of homologs required (numeric)?
- Do I require explicit documented commercial/clinical/regulatory permissions for deployment (yes/no)?
- Must the end-to-end pipeline guarantee compatibility between MSA outputs and the structure-prediction input formats (yes/no)?
- Do I require any head-to-head quality comparison to use the exact same evaluation dataset/split and identical preprocessing (yes/no)?

## Comparability rules

- Use the same target dataset and split (e.g., same CASP or CAMEO targets) for any head-to-head model-quality comparison; results from different benchmark suites (CASP vs CAMEO) are non-comparable without re-evaluation on a shared test set. (Supported by ColabFold paper and OpenFold2 evaluation reporting.)
- MSA source(s) and database identifiers must match exactly (examples present in MSA Search NIM: uniref30_2302, colabfold_envdb_202108, pdb70_220313); MSA origin and depth materially affect downstream structure prediction inputs. (Supported by MSA Search NIM configuration and release notes.)
- MSA depth and trimming parameters must match; the MSA Search NIM documents NIM_GLOBAL_MAX_MSA_DEPTH and api max_msa_sequences defaults and per-database behavior which must be matched across compared runs. (Supported by MSA Search NIM API reference and configure documentation.)
- Input sequence lengths must be within both candidates' supported ranges; OpenFold2 NIM versions and release notes specify supported sequence-length limits for particular releases, and the MSA Search NIM documents NIM_MSA_API_MAX_SEQUENCE_LENGTH defaults. If any target exceeds a model's documented supported length, the comparison is not comparable without model-specific evidence. (Supported by OpenFold2 release notes and MSA Search NIM configure.)
- Structure-evaluation metrics must be computed with identical implementations and parameters (e.g., TM-score with the same alignment method such as MM-align, lDDT computed on identical atom sets); where primary sources do not specify full metric-implementation parity, mark as non-comparable until parity is documented. (Supported by ColabFold reporting and OpenFold2 evaluation reporting.)
- Model inference configuration that affects quality must match between compared runs (examples: OpenFold2 selected_models and num_trials as reported in OpenFold2 performance documentation). (Supported by OpenFold2 performance reporting.)
- Preprocessing and file-format parity is required (MSA file formats a3m/.sto, templates mmCIF); absent documentation of exact preprocessing steps or API parameter defaults is an evidence gap. (Supported by MSA Search NIM API reference and OpenFold2 modelcard/release notes.)

## Conditional routing

### Prefer `colabfold-msa-search-nim` when User requires standalone MSA generation (MSA output file) or structural-template retrieval from a sequence (including a3m/fasta/mmCIF outputs).

- Why: The MSA Search NIM exposes API endpoints that return alignments in a3m/fasta and a structural-template search endpoint that returns mmCIF files; the NIM documents supported databases and API parameters for max_msa_sequences and global depth limits, making it the documented choice for standalone MSA/template generation.
- Alternative: openfold-openfold2-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/configure.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html, https://catalog.ngc.nvidia.com/orgs/nim/colabfold/containers/msa-search/-

### Prefer `colabfold-msa-search-nim` when User requires paired MSA generation for protein complexes (paired alignment across chains).

- Why: The MSA Search NIM release notes and API reference document a dedicated paired MSA search endpoint (/biology/colabfold/msa-search/paired/predict) and the search_type parameter supporting 'colabfold' and 'alphafold2' modes.
- Alternative: openfold-openfold2-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/msa-search/2.1.0/release-notes.html, https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html

### Prefer `openfold-openfold2-nim` when User requires 3D structure prediction (PDB/mmCIF output) from a single amino-acid sequence with no external MSA/templates provided.

- Why: OpenFold2 NIM documents structure prediction from sequence as a primary operation and reports evaluation metrics for structure accuracy; the OpenFold2 modelcard and overview present the NIM as a structure predictor that accepts optional MSAs/templates.
- Alternative: colabfold-msa-search-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html, https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/latest/performance.html

### Prefer `openfold-openfold2-nim` when User will supply an external MSA (a3m/sto) and/or template mmCIF files to the structure predictor and needs a model that consumes these inputs.

- Why: OpenFold2 NIM and its example requests/documentation accept optional MSA and template inputs (a3m/.sto and mmCIF templates in supported releases), making it the documented choice to consume externally-provided MSAs/templates.
- Alternative: colabfold-msa-search-nim
- Evidence: https://build.nvidia.com/openfold/openfold2/modelcard, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/release-notes.html

### Prefer `insufficient-evidence` when User plans a two-step pipeline (generate MSA/templates, then run structure prediction ingesting those MSAs/templates) and requests a single preferred Forge slug for both steps.

- Why: A two-step pipeline requires two distinct components (MSA generation and structure prediction). A single Forge slug cannot represent both roles; primary sources document each component separately but do not provide a single NIM that both generates MSAs and performs structure prediction in the candidate list.
- Alternative: colabfold-msa-search-nim
- Alternative: openfold-openfold2-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html, https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html, https://build.nvidia.com/openfold/openfold2/modelcard

### Prefer `openfold-openfold2-nim` when Target sequences exceed 1000 residues and the requirement is end-to-end structure prediction from a single model instance.

- Why: OpenFold2 NIM release notes for version 2.5.0 document support for sequence lengths up to 2048 residues on specified GPUs (A100, H100, B200) with TensorRT‑BioNeMo; this provides primary-source evidence that a recent OpenFold2 NIM release supports sequences >1000 when deployed under those documented conditions.
- Alternative: colabfold-msa-search-nim
- Evidence: https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2

### Prefer `colabfold-msa-search-nim` when User requires documented container availability and subscription/access details for deployment in industry pipelines.

- Why: The ColabFold MSA Search NIM container is listed on NGC and the MSA Search documentation/reference describe the service and APIs; the NGC listing documents container availability and access model.
- Alternative: openfold-openfold2-nim
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/colabfold/containers/msa-search/-, https://docs.api.nvidia.com/nim/reference/colabfold-msa-search, https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf

### Prefer `insufficient-evidence` when User requires explicit documented allowance for clinical (regulated) use in healthcare settings.

- Why: Primary sources do not contain a model-specific documented permission that explicitly allows clinical/regulatory use for either NIM; NVIDIA legal documents and modelcards require agreement to product-specific terms but do not contain a clear, model-specific clinical-use grant in the cited findings.
- Alternative: colabfold-msa-search-nim
- Alternative: openfold-openfold2-nim
- Evidence: https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf, https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/EULA.html, https://build.nvidia.com/openfold/openfold2/modelcard

## Benchmark taxonomy

### MSA generation and structural-template retrieval (standalone MSA/service accuracy)

- Datasets: uniref30_2302, colabfold_envdb_202108, pdb70_220313, uniref90, mgnify, smallbfd
- Metrics: MSA depth and sequence-identity statistics as reported by the MSA Search NIM, Throughput (sequences/sec) on specified GPU hardware for cascaded vs iterative search under documented NIM_GLOBAL_MAX_MSA_DEPTH settings
- Compare only when: Match per-database identifiers and the same per-database sequence limits and trimming policies (MSA Search NIM documents NIM_MSA_API_DEFAULT_STRUCTURAL_TEMPLATE_DBS, NIM_MSA_EXPANDABLE_DBS, and NIM_GLOBAL_MAX_MSA_DEPTH). (Supported by MSA Search NIM configure and release notes.)
- Compare only when: Use identical API parameters (max_msa_sequences, e_value, max_accept, alt_ali) and the same GPU Server / NIM_GLOBAL_MAX_MSA_DEPTH configuration when measuring throughput or MSA depth. (Supported by MSA Search NIM API reference and performance reporting.)
- Compare only when: Compare only output formats that downstream tools accept (a3m, fasta, mmCIF) and ensure identical post-processing prior to downstream use. (Supported by MSA Search NIM API reference and release notes.)

### Sequence-only structure prediction (structure from single sequence without external MSA/templates)

- Datasets: CASP14 free-modeling targets (as cited in ColabFold reporting), OpenFold2-reported evaluation sets (e.g., CAMEO split reported by OpenFold2)
- Metrics: TM-score (global fold similarity) as reported by ColabFold benchmarks, mean lDDT-Cα / lDDT (local per-residue accuracy) as reported by OpenFold2
- Compare only when: Evaluate on the same sequence test set (e.g., identical CASP or CAMEO targets) and use identical preprocessing (sequence length constraints, handling of ambiguous residues). (Supported by ColabFold paper and OpenFold2 evaluation reporting.)
- Compare only when: Ensure TM-score and lDDT are computed with the same tool/parameters; where full metric-implementation details are missing in primary sources, record an evidence gap. (Supported by ColabFold reporting and OpenFold2 reporting.)

### Template-assisted structure prediction (use of PDB templates during inference)

- Datasets: PDB70_220313, Benchmark targets where templates are available (select identically for both models)
- Metrics: TM-score, RMSD on backbone atoms, per-residue confidence scores (pLDDT or lDDT) with identical atom sets and alignment procedures, Count and quality of templates returned/used (number of templates returned by template search endpoints)
- Compare only when: Use identical template database snapshots (e.g., pdb70_220313) and the same template-selection thresholds and file formats (mmCIF). (Supported by MSA Search NIM configure and OpenFold2 release notes/modelcard.)
- Compare only when: Match template preprocessing and ingestion parameters; if template-processing behavior differs across releases (e.g., HHR removal / mmCIF usage), mark as non-comparable unless re-evaluated with identical processing. (Supported by OpenFold2 release notes and MSA Search NIM documentation.)

### Combined pipeline evaluation (MSA generation by one component followed by structure prediction by another)

- Datasets: Any of the above test sets provided the MSA source, MSA depth, template database snapshot, and preprocessing are identical between runs
- Metrics: TM-score, lDDT, RMSD (structural metrics) and MSA metrics (depth, mean sequence identity) where relevant
- Compare only when: MSA generator must produce formats accepted by the structure predictor (a3m/.sto for MSAs, mmCIF for templates). (Supported by MSA Search NIM API reference and OpenFold2 modelcard/release notes.)
- Compare only when: Match MSA depth limits and trimming policies (NIM_GLOBAL_MAX_MSA_DEPTH and max_msa_sequences) between steps. (Supported by MSA Search NIM configure and api-reference.)
- Compare only when: Match OpenFold2 configuration parameters that affect accuracy (selected_models and num_trials) if used; where OpenFold2 release notes or example requests do not fully document a knob for the exact NIM release, record an evidence gap. (Supported by OpenFold2 performance and example-requests documentation.)

## Primary sources

- [NVIDIA NIM MSA Search configure](https://docs.nvidia.com/nim/bionemo/msa-search/latest/configure.html) — NVIDIA; supports NIM_MSA_API_MAX_STRUCTURES default and max_structures parameter, NIM_MSA_API_SEQ_PATTERN sequence validation regex, NIM_MSA_API_MAX_SEQUENCE_LENGTH default 4096, NIM_MSA_API_DEFAULT_STRUCTURAL_TEMPLATE_DBS default pdb70_220313, NIM_MSA_COLABFOLD_DEFAULT_PROFILE_DB default uniref30_2302, NIM_MSA_EXPANDABLE_DBS default list
- [NVIDIA NIM MSA Search API reference](https://docs.nvidia.com/nim/bionemo/msa-search/latest/api-reference.html) — NVIDIA; supports API parameter definitions (max_msa_sequences, e_value, max_accept, alt_ali), Endpoints including /biology/colabfold/msa-search/structure-templates/predict and paired/predict, Default behavior tied to NIM_GLOBAL_MAX_MSA_DEPTH
- [NVIDIA NIM MSA Search overview](https://docs.nvidia.com/nim/bionemo/msa-search/latest/overview.html) — NVIDIA; supports General description that MSA Search NIM generates MSAs and finds structural templates, Description of ColabFold and AlphaFold2 search styles and documented databases
- [NVIDIA NIM MSA Search release notes (2.2.0)](https://docs.nvidia.com/nim/bionemo/msa-search/2.2.0/release-notes.html) — NVIDIA; supports Release-2.2.0 changes: unified max_msa_sequences validation with NIM_GLOBAL_MAX_MSA_DEPTH, Release-2.2.0 added Structural Template Search endpoint returning mmCIF and combined MSA output, Database name case-insensitivity and other documented behavior
- [NVIDIA NIM MSA Search release notes (2.1.0)](https://docs.nvidia.com/nim/bionemo/msa-search/2.1.0/release-notes.html) — NVIDIA; supports Release-2.1.0 introduced a dedicated Paired MSA Search endpoint, alphafold2 search type remains supported with appropriate databases
- [NVIDIA NIM MSA Search release notes (2.0.0)](https://docs.nvidia.com/nim/bionemo/msa-search/2.0.0/release-notes.html) — NVIDIA; supports Release-2.0.0 enabled GPU Server by default, MMSeqs2 v18 upgrade, and default database list (Uniref30_2302, colabfold_envdb_202108, PDB70_220313), AlphaFold2 databases (uniref90, small_bfd, mgnify) not included for GPU Server operation, External custom databases can be mounted via MODEL_PATH
- [NVIDIA NGC catalog entry: ColabFold MSA Search container](https://catalog.ngc.nvidia.com/orgs/nim/colabfold/containers/msa-search/-) — NVIDIA NGC; supports NGC container availability and subscription requirement for the MSA Search NIM, Container versioning information and GPU-accelerated MMSeqs2 support
- [NVIDIA NIM ColabFold reference](https://docs.api.nvidia.com/nim/reference/colabfold-msa-search) — NVIDIA; supports Statement that ColabFold MSA Search uses GPU-accelerated MMSeqs2 for fast database search and template discovery
- [ColabFold peer-reviewed paper (Nature Methods, PubMed record)](https://www.nature.com/articles/s41592-022-01488-1) — Nature Methods / PubMed; supports ColabFold benchmarks (CASP reporting) and methodological description referenced by MSA Search NIM documentation
- [ColabFold preprint (biorxiv)](https://www.biorxiv.org/content/10.1101/2021.08.15.456425v2.full-text) — bioRxiv; supports Preprint reporting mean TM-score for ColabFold configurations and specific experimental notes cited by ColabFold literature
- [NVIDIA OpenFold2 NIM overview](https://docs.nvidia.com/nim/bionemo/openfold2/latest/overview.html) — NVIDIA; supports OpenFold2 described as a PyTorch reimplementation of AlphaFold2 and that OpenFold2 NIM predicts 3D structures from sequence with optional MSA/templates
- [NVIDIA OpenFold2 build page](https://build.nvidia.com/openfold/openfold2) — NVIDIA; supports OpenFold2 NIM build/model page and metadata referenced in findings
- [OpenFold2 modelcard (NVIDIA build)](https://build.nvidia.com/openfold/openfold2/modelcard) — NVIDIA / OpenFold upstream; supports OpenFold2 modelcard statements about input types (sequence, MSA, templates) and licensing indications in the modelcard
- [OpenFold2 performance page (NVIDIA NIM)](https://docs.nvidia.com/nim/bionemo/openfold2/latest/performance.html) — NVIDIA; supports OpenFold2 benchmark timings and reported accuracy metrics (examples on H100/A100/other GPUs) and reported CADS/LDDT values in performance reporting
- [OpenFold preprint (bioRxiv) - architecture and evaluation](https://biorxiv.org/content/10.1101/2022.11.20.517210v3.full.pdf) — bioRxiv (OpenFold authors); supports OpenFold/OpenFold2 upstream evaluation reporting (mean lDDT-Cα on CAMEO) and architecture/training descriptions
- [OpenFold2 release notes (2.5.0)](https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/release-notes.html) — NVIDIA; supports Release-2.5.0 support for sequence lengths up to 2048 on specified GPUs, support for user-provided mmCIF templates, and GPU support changes
- [NVIDIA NGC container listing: OpenFold2](https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold2) — NVIDIA NGC; supports OpenFold2 NIM container metadata and compressed size for reported container versions
- [OpenFold2 EULA (NIM release-specific EULA)](https://docs.nvidia.com/nim/bionemo/openfold2/2.5.0/EULA.html) — NVIDIA; supports Statement that usage of the OpenFold2 NIM requires agreement to NVIDIA AI product terms for the NIM
- [NVIDIA API Trial Terms of Service (legal)](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf) — NVIDIA; supports Governance and legal terms referenced for NIM usage and need for vendor/legal review for commercial/regulated deployment
- [NVIDIA NIM EULA / product-specific terms reference](https://docs.nvidia.com/nim/speech/latest/resources/eula.html) — NVIDIA; supports Reference to NVIDIA Software License Agreement and product-specific terms governing NIM containers
- [Exact official starting source declared by Forge](https://build.nvidia.com/colabfold/msa-search) — build.nvidia.com; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No primary-source, head-to-head evaluation comparing the exact NIM-packaged ColabFold MSA Search NIM plus OpenFold2 NIM pipeline versus OpenFold2 NIM using identical datasets/splits/parameters was found in the provided findings.
- Evidence gap: Metric-implementation parity details (exact TM-score/MM-align command-line versions and parameters, and exact lDDT atom set/residue inclusion) are not fully specified in the provided primary sources for direct comparisons between ColabFold and OpenFold2.
- Evidence gap: OpenFold2 primary sources do not fully document all inference-config knobs (for the exact NIM release) used for published benchmarks (for example exact number of recycles used in a specific reported benchmark run is not present in the findings).
- Evidence gap: While OpenFold2 v2.5.0 release notes document support for longer sequences on specific GPUs, there is no primary-source evidence in the findings that guarantees all OpenFold2 NIM deployments (all versions) support sequences >1000; verify the exact NIM release before relying on >1000-residue end-to-end predictions.
- Evidence gap: Primary-source, model-specific explicit permission for clinical/regulatory use of either NIM is not present in the findings; obtain vendor/legal confirmation before deploying in regulated clinical settings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/msa-search/latest/configure.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/colabfold/msa-search: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
