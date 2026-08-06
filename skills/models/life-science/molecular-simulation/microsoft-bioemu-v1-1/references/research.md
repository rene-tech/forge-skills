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

- Research key: `github-com-microsoft-bioemu-1ade956592`
- Independent audit: `revised`
- Researched: `2026-07-23T23:29:48.566606+00:00`

Canonical repository files and the publisher article together establish that BioEmu is a Microsoft Research protein-monomer conformational-ensemble sampler built on the Distributional Graphormer (DiG) architecture; the repository README documents a named checkpoint selector ("--model_name=\"bioemu-v1.1\"") and backbone-frame ensemble outputs and documents HPacker-based side-chain reconstruction and optional MD-relaxation tooling. The Nature Methods publisher page confirms DiG as the architecture and reports sampling throughput (e.g., "10,000 independent protein structures within minutes to hours on a single GPU") and 30–50 denoising steps. Primary-source gaps remain for an immutable release tag or commit SHA that concretely binds the label bioemu-v1.1 to a release asset, an explicit model-weights license distinct from the repository code license, an authoritative numeric MAE benchmark locator (paper table/figure/section) for reported free-energy MAE values, and exact callable preprocessing/tokenization function locators in the repository.

## Identity

- Upstream name: BioEmu
- Checkpoint/version: bioemu-v1.1
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: DiG
- License: MIT (repository code license). Evidence gap: model-weights license not specified
- Evidence: https://github.com/microsoft/bioemu/blob/main/README.md, https://github.com/microsoft/bioemu, https://nature.com/articles/s41592-025-02874-1

## Selection

### Recommended

- **Protein monomer conformational-ensemble sampling (backbone-frame ensembles)** — Repository README documents that BioEmu accepts a protein sequence and produces backbone-frame conformational ensembles for monomers; Nature Methods article describes BioEmu as a biomolecular emulator that samples approximate equilibrium distributions for protein conformations.
  Scope: bioemu-v1.1 upstream checkpoint (named checkpoint selector documented in README)
  Evidence: https://github.com/microsoft/bioemu/blob/main/README.md, https://nature.com/articles/s41592-025-02874-1

### Conditional

- **Downstream physics-based simulation seeding and MD augmentation (requires downstream side-chain reconstruction and optional MD-relaxation)** — Requires invoking repository side-chain reconstruction tooling (HPacker) and optional MD-relaxation commands as described in README; downstream calibration or MD-equilibration may be required to produce side-chain-resolved or fully energy-minimized structures for workflows that demand those outputs.
  Scope: bioemu-v1.1 upstream checkpoint used together with repository HPacker and optional MD-relaxation commands
  Evidence: https://github.com/microsoft/bioemu/blob/main/README.md, https://github.com/microsoft/bioemu/blob/main/src/bioemu/config/steering/physical_steering.yaml

### Avoid

- **Clinical deployment or real-world therapeutic prediction** — Evidence gap: the canonical upstream sources do not provide any authorization, regulatory clearance, or explicit upstream statement authorizing clinical use of bioemu-v1.1; do not deploy clinically without further expert review and regulatory authorization.
  Scope: bioemu-v1.1 upstream checkpoint
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- Protein sequence of a single-chain (monomer) protein is the accepted primary input modality. Sources: https://github.com/microsoft/bioemu/blob/main/README.md, https://nature.com/articles/s41592-025-02874-1

### Accepted formats

- Accepted input: a protein sequence for a monomer; repository CLI examples show sequence-based monomer ensemble generation. Sources: https://github.com/microsoft/bioemu/blob/main/README.md

### Preprocessing

- Evidence gap: canonical repository files (README, source tree) do not expose an exact preprocessing/tokenization/featurization function name, module path, or in-repo callable that normalizes a protein_sequence input; no exact file+function locator was found in the supplied canonical sources.

### Pre-submit validation

- Evidence gap: canonical upstream sources do not provide a located callable input-validation function (sequence-length bounds, alphabet checks, steric-clash filters) with an exact file/function/line locator; no canonical in-repo validation locator was found.

### Task-specific formatting

- The repository README documents CLI usage that selects a checkpoint by name; example: --model_name="bioemu-v1.1". Sources: https://github.com/microsoft/bioemu/blob/main/README.md

## Output interpretation

### Outputs

- BioEmu produces backbone-frame protein-structure ensembles (backbone-only representations) for monomer sequences; side-chain reconstruction is provided as a downstream optional step via HPacker. Sources: https://github.com/microsoft/bioemu/blob/main/README.md

### Interpretation

- Ensembles are intended to represent sampled conformational distributions for protein monomers and may be analyzed relative to simulation or experimental data. Sources: https://github.com/microsoft/bioemu/blob/main/README.md, https://nature.com/articles/s41592-025-02874-1

### Post-inference validation

- Evidence gap: no canonical numbered paper table/figure/section/appendix/page or model-card heading in the located primary sources ties a specific numeric energy-calibration MAE claim to the exact bioemu-v1.1 checkpoint and exposed backbone-only output head; numeric MAE claims appear in non-canonical artifacts in the supplied findings and therefore cannot be deterministically grounded to an upstream-checkpoint locator.

## Public benchmarks

### Sampling throughput (independent structures per time on single GPU)

- Dataset/split: not applicable / not reported
- Metric/value: independent structures sampled (count) per wall-clock time / BioEmu can sample 10,000 independent protein structures within minutes to hours on a single GPU (publisher statement). (`context-only`)
- Model scope: BioEmu as described in the Nature Methods paper (publisher-described model and experiments)
- Conditions: Reported in publisher article; also notes 30–50 denoising steps per sample. The publisher page states the throughput as an empirical statement but does not present a paper table/figure locator in the supplied findings.
- Source: https://nature.com/articles/s41592-025-02874-1
- Locator: Nature Methods article (publisher page statement; article text describing throughput and denoising steps)
- Caveat: The publisher page gives an empirical throughput statement but no paper table/figure/section/appendix/table row was located in the supplied canonical sources that enumerates hardware, batch size, or exact benchmark protocol details for a checkpoint-named run.
- Caveat: It is not established in the canonical sources whether this throughput measurement corresponds to a backbone-only output or requires additional downstream processing.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Protocol-matched checkpoint-to-checkpoint numeric comparison with classical MD engines (GROMACS/LAMMPS/OpenMM)
- Criteria: No canonical primary-source, protocol-matched, checkpoint-to-checkpoint numeric comparison table/figure/section was found in the located repository or publisher article.
- Rationale: The located primary sources (repo and publisher page) do not present a table or figure directly comparing BioEmu checkpoint results to classical MD engine runs under matched protocols; therefore direct numeric comparisons are unsupported.
- Comparison conditions: No comparable protocol and numeric table/figure found at canonical locators for both sides.
- Evidence: https://github.com/microsoft/bioemu/blob/main/README.md, https://nature.com/articles/s41592-025-02874-1

## Limitations and safety

### Limitations

- Evidence gap: no canonical upstream locator provides an explicit model-weights license distinct from the repository code license; the repository contains a LICENSE file for code but a weights-specific license statement is not present in the located primary sources.
- The canonical repository README documents that side-chain reconstruction relies on HPacker and that optional MD-relaxation tooling is provided; HPacker installation has conda-related requirements documented in the repository README. Sources: https://github.com/microsoft/bioemu/blob/main/README.md
- Ambiguity in denoiser/physical-steering parameter names: the physical_steering.yaml file located in the repository contains explicit steering parameters and umbrella potentials (eps_t, max_t, N, noise, umbrella potentials), while a repository-tree-level description in the located primary sources also lists key steering parameters including num_particles and ess_threshold. The two canonical locators create an ambiguity about the exact presence/location of parameters named num_particles and ess_threshold. Sources: https://github.com/microsoft/bioemu/blob/main/src/bioemu/config/steering/physical_steering.yaml, https://github.com/microsoft/bioemu/tree/main
- Evidence gap: exact callable preprocessing/tokenization function names, module paths, and in-repo example invocation locators for protein_sequence inputs were not found in the located canonical sources.

### Safety

- Evidence gap: the located canonical upstream sources do not provide any explicit authorization for clinical use or regulatory clearance for bioemu-v1.1; no clinical authorization statement is present in the repository or publisher article.
- Repository code is distributed under an MIT License per the repository's LICENSE and README file, but no weights-specific license text was located. Sources: https://github.com/microsoft/bioemu/blob/main/README.md, https://github.com/microsoft/bioemu

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### BioEmu repository (root)

- URL: https://github.com/microsoft/bioemu
- Publisher: Microsoft Research
- Type: `repository`
- Primary because: Canonical repository root used to locate repository-level metadata, LICENSE, MODEL_CARD.md, and to navigate to README and config files.
- Scope: BioEmu upstream repository
- Supports: Repository-level metadata and navigation to primary files (README, config files, LICENSE)
- Supports: General installation/runtime notes (packaging/attribution)

### BioEmu README.md

- URL: https://github.com/microsoft/bioemu/blob/main/README.md
- Publisher: Microsoft Research
- Type: `repository`
- Primary because: Repository README provides CLI examples (--model_name selector), documents backbone outputs, HPacker-based side-chain reconstruction, optional MD-relaxation commands, and installation hints.
- Scope: BioEmu repository README
- Supports: Checkpoint selector example (--model_name="bioemu-v1.1")
- Supports: Backbone-frame output descriptions and HPacker side-chain reconstruction invocation
- Supports: Optional MD-relaxation command examples

### physical_steering.yaml (steering/denoiser configuration)

- URL: https://github.com/microsoft/bioemu/blob/main/src/bioemu/config/steering/physical_steering.yaml
- Publisher: Microsoft Research
- Type: `repository`
- Primary because: This repository file documents denoiser/physical-steering configuration parameters and umbrella potentials intended to be passed as denoiser_config.
- Scope: BioEmu steering configuration file
- Supports: Definition of denoiser_config parameters (eps_t, max_t, N, noise, umbrella potentials)
- Supports: File-level evidence that steering config is provided in the repository

### BioEmu releases (GitHub releases page)

- URL: https://github.com/microsoft/bioemu/releases
- Publisher: Microsoft Research
- Type: `repository`
- Primary because: Canonical releases page used to inspect available release tags and release metadata.
- Scope: BioEmu upstream releases
- Supports: Repository release metadata (listed release tags and associated metadata)

### BioEmu repository tree (main branch)

- URL: https://github.com/microsoft/bioemu/tree/main
- Publisher: Microsoft Research
- Type: `repository`
- Primary because: Repository tree provides context for file locations and higher-level documentation statements regarding steering parameters and packaging.
- Scope: BioEmu repository tree
- Supports: Tree-level statements about presence and organization of config files and steering parameters

### Nature Methods publisher page for BioEmu (canonical paper/publisher page)

- URL: https://nature.com/articles/s41592-025-02874-1
- Publisher: Nature Methods / Springer Nature
- Type: `paper`
- Primary because: Publisher article is the canonical primary publication describing BioEmu, the DiG architecture use, the sampling design and empirical throughput statements.
- Scope: BioEmu canonical paper (publisher page)
- Supports: Description of BioEmu as a biomolecular emulator
- Supports: Identification of Distributional Graphormer (DiG) architecture
- Supports: Empirical statements on sampling throughput (10,000 independent structures within minutes to hours on a single GPU) and denoising steps (30–50)

### PubMed entry for BioEmu paper

- URL: https://pubmed.ncbi.nlm.nih.gov/41068462
- Publisher: PubMed / NCBI
- Type: `paper`
- Primary because: PubMed record is a canonical bibliographic locator for the publisher article and supports identification of the primary publication.
- Scope: BioEmu canonical paper (bibliographic record)
- Supports: Bibliographic metadata for the BioEmu Nature Methods publication

## Evidence gaps

- Evidence gap: No canonical upstream release tag or commit SHA was found that immutably binds the label "bioemu-v1.1" to a release asset in the located repository releases page or repository files; the README documents a --model_name selector but does not map that string to an immutable release asset at a located primary-source path.
- Evidence gap: No canonical paper table/figure/section/appendix/page/README path was located in the primary sources that deterministically reports numeric MAE results tied to the bioemu-v1.1 checkpoint (the numeric MAE values reported in non-canonical artifacts cannot be used as upstream-checkpoint evidence).
- Evidence gap: The located canonical repository sources include a code LICENSE (MIT) but do not provide a separate model-weights license statement; a weights-specific license locator is missing.
- Evidence gap: Exact callable preprocessing/tokenization/featurization function names and file paths for protein_sequence inputs are not present in the located canonical sources; no file+function locator was found.
- Evidence gap: Exact callable input-validation code (sequence-length bounds, allowed alphabet checks, steric-clash filters) with file/function/line locators is not present in the located canonical sources.
- Evidence gap: For numeric MAE benchmarks, the canonical sources do not provide the full set of required protocol details (exact checkpoint name used in the experiment, dataset split, metric aggregation, hardware, batch size, and whether benchmarks are backbone-only or require downstream calibration); these elements are missing from canonical locators.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].caveats: $.benchmarks[0].caveats: expected array, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[1]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
