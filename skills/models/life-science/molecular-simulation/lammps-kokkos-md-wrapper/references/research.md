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

- Research key: `github-com-lammps-lammps-releases-tag-stable-22jul2025-update4-637524d4d1`
- Independent audit: `revised`
- Researched: `2026-07-23T23:35:38.032751+00:00`

The verified primary sources establish that `stable_22Jul2025_update4` is an official LAMMPS release tag, listed as update 4 for the 22 Jul 2025 stable release, released on 16 Apr 2026 with commit `611ca3b`. Upstream sources describe LAMMPS as classical molecular dynamics software distributed under GPLv2, and document KOKKOS execution modes plus some runtime defaults and caveats. The checked evidence supports use of this upstream release for classical MD workflows driven by LAMMPS input scripts, data/restart files, and documented output/logging formats. However, the verified findings do not provide checkpoint-specific numeric benchmarks for `stable_22Jul2025_update4`, do not report an immutable Forge-wrapper license beyond upstream GPLv2, and do not document a canonical upstream JSON job-submission schema for LAMMPS.

## Identity

- Upstream name: LAMMPS
- Checkpoint/version: stable_22Jul2025_update4
- Immutable revision: 611ca3b
- Parameter scale: not reported
- Architecture/head: Classical molecular dynamics software; built using CMake (preferred) or a legacy makefile system, with optional KOKKOS execution modes Serial, OpenMP, CUDA, and HIP.
- License: Upstream code/source distribution: GNU General Public License version 2 (GPLv2). Forge wrapper/runtime license terms beyond upstream GPLv2 were not reported in the verified primary sources.
- Evidence: https://github.com/lammps/lammps/releases, https://github.com/lammps/lammps/tree/stable_22Jul2025_update4, https://github.com/lammps/lammps, https://docs.lammps.org/Build.html, https://docs.lammps.org/Speed_kokkos.html, https://lammps.org/download

## Selection

### Recommended

- **Classical molecular dynamics simulations using the official LAMMPS stable release and its documented input-script workflow** — Primary sources identify LAMMPS as classical molecular dynamics software and document the structure of a typical input script with initialization, system definition, simulation settings, and run steps.
  Scope: LAMMPS upstream release `stable_22Jul2025_update4`
  Evidence: https://github.com/lammps/lammps/tree/stable_22Jul2025_update4, https://docs.lammps.org/Commands_structure.html
- **KOKKOS-accelerated MD runs using documented KOKKOS execution modes** — Primary KOKKOS documentation states that Kokkos provides Serial, OpenMP, CUDA, and HIP execution modes per MPI task.
  Scope: LAMMPS upstream release `stable_22Jul2025_update4` with the KOKKOS package/runtime path documented in LAMMPS KOKKOS documentation
  Evidence: https://docs.lammps.org/Speed_kokkos.html

### Conditional

- **Running KOKKOS on hardware/software stacks where GPU-aware MPI availability is uncertain** — Validate MPI and GPU-awareness behavior on the target environment before production use. The verified findings state that when GPU-aware MPI is not available, the default `gpu/aware` option in the KOKKOS package is off.
  Scope: LAMMPS KOKKOS package behavior as documented for the upstream release/manual set covering `stable_22Jul2025_update4`
  Evidence: https://docs.lammps.org/package.html
- **Using KOKKOS defaults for neighbor-list and Newton settings on CPUs vs GPUs** — Confirm that the package defaults match the intended scientific and performance behavior for the target run, because verified findings report different defaults for CPUs and GPUs.
  Scope: LAMMPS KOKKOS package behavior as documented for the upstream release/manual set covering `stable_22Jul2025_update4`
  Evidence: https://docs.lammps.org/package.html

### Avoid

- **Selecting this dossier as a checkpoint with verified checkpoint-specific throughput or accuracy benchmark numbers** — The verified primary sources checked for this audit do not provide checkpoint-specific numeric benchmark tables for `stable_22Jul2025_update4`; therefore benchmark-backed selection for this exact release is not supported by the available primary evidence.
  Scope: LAMMPS upstream release `stable_22Jul2025_update4` and Forge wrapper `lammps-kokkos-md-wrapper`
  Evidence: https://github.com/lammps/lammps/releases, https://lammps.org/download, https://docs.lammps.org/Speed_kokkos.html
- **Assuming an upstream JSON job-submission API or canonical JSON simulation-request schema** — The verified findings document script structure, data-file format, and output/logging behavior, but do not report any canonical upstream JSON submission schema.
  Scope: LAMMPS upstream release `stable_22Jul2025_update4`
  Evidence: https://docs.lammps.org/Commands_structure.html, https://docs.lammps.org/99/data_format.html, https://docs.lammps.org/Run_output.html

## Input preparation

### Semantic inputs

- A typical LAMMPS input script has four parts: Initialization, System definition, Simulation settings, and Run a simulation. Sources: https://docs.lammps.org/Commands_structure.html
- System definition can be performed by reading a data file, reading a restart file, or creating a lattice, region, box, and atoms. Sources: https://docs.lammps.org/Commands_structure.html

### Accepted formats

- LAMMPS accepts input scripts composed of commands for initialization, system definition, simulation settings, and running a simulation. Sources: https://docs.lammps.org/Commands_structure.html
- LAMMPS data files use a documented data-file format where entry keywords must be left-justified and capitalized, blank lines separate entries, and indentation is otherwise unimportant. Sources: https://docs.lammps.org/99/data_format.html
- LAMMPS produces screen and logfile output during a run, including thermodynamic state and related run statistics. Sources: https://docs.lammps.org/Run_output.html

### Preprocessing

- Prepare input scripts according to the documented command structure: initialization commands, system definition, simulation settings, and run commands. Sources: https://docs.lammps.org/Commands_structure.html
- Prepare data files so that entry keywords are left-justified and capitalized, with blank lines separating entries. Sources: https://docs.lammps.org/99/data_format.html

### Pre-submit validation

- Validate that data-file entry keywords are left-justified and capitalized and that blank-line-separated entries are used, because these are documented format requirements. Sources: https://docs.lammps.org/99/data_format.html
- If the optional final `nx, ny, nz` values are present in the `Atoms` entry, they are read only if the `true` flag command is specified. Sources: https://docs.lammps.org/99/data_format.html
- For KOKKOS runs, validate whether GPU-aware MPI is available, because when it is not available the default `gpu/aware` option is off. Sources: https://docs.lammps.org/package.html

### Task-specific formatting

- Initialization commands documented for typical input scripts include `units`, `dimension`, `newton`, `processors`, `boundary`, `atom_style`, and `atom_modify`. Sources: https://docs.lammps.org/Commands_structure.html
- System definition may be formatted by reading a data file, reading a restart file, or creating a lattice, region, box, and atoms. Sources: https://docs.lammps.org/Commands_structure.html

## Output interpretation

### Outputs

- During a run LAMMPS prints screen and logfile output including memory per processor, thermodynamic state, number of owned atoms, ghost atoms, and pairwise neighbor counts. Sources: https://docs.lammps.org/Run_output.html

### Interpretation

- Interpret screen/logfile output as run diagnostics and thermodynamic/run-state reporting, since the documented outputs include memory per processor, thermodynamic state, owned atoms, ghost atoms, and pairwise neighbor counts. Sources: https://docs.lammps.org/Run_output.html

### Post-inference validation

- Post-run validation should confirm that the printed run statistics and thermodynamic/logfile outputs are present and internally consistent for the intended simulation, because these are the documented runtime outputs available from primary sources. Sources: https://docs.lammps.org/Run_output.html
- For KOKKOS runs, validate that observed behavior is consistent with the selected execution mode and package defaults, because the documented defaults differ across CPU and GPU settings. Sources: https://docs.lammps.org/package.html, https://docs.lammps.org/Speed_kokkos.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### gromacs-md-ngc-wrapper — `insufficient-evidence`

- Task: GPU-accelerated classical MD production runs
- Criteria: No protocol-matched primary benchmark evidence for the alternative was included in the verified findings, and no checkpoint-specific numeric benchmark table for LAMMPS `stable_22Jul2025_update4` was verified.
- Rationale: The verified primary findings for this audit establish identity, licensing, inputs, outputs, and KOKKOS behavior for LAMMPS, but do not establish comparable benchmark numbers for this exact release or for the named alternative under a matched protocol.
- Comparison conditions: Comparison is not supportable from the verified findings because the checked LAMMPS primary sources did not provide checkpoint-specific numeric benchmarks for `stable_22Jul2025_update4`, and no primary evidence for the alternative was supplied in the verified findings set.
- Evidence: https://github.com/lammps/lammps/releases, https://lammps.org/download, https://docs.lammps.org/Speed_kokkos.html

### openmm-md-8-5-1-wrapper — `insufficient-evidence`

- Task: Biomolecular or general MD simulation selection
- Criteria: No protocol-matched primary benchmark evidence for the alternative was included in the verified findings, and no checkpoint-specific numeric benchmark table for LAMMPS `stable_22Jul2025_update4` was verified.
- Rationale: The verified findings support only scoped LAMMPS identity and documentation claims, not comparative performance or accuracy claims against the named alternative.
- Comparison conditions: No comparable primary-source evidence for the alternative was present in the verified findings set; LAMMPS-side benchmark evidence for the exact checkpoint was also not verified.
- Evidence: https://github.com/lammps/lammps/releases, https://lammps.org/download

### microsoft-bioemu-v1-1 — `insufficient-evidence`

- Task: Simulation workflow selection
- Criteria: No primary-source evidence for the alternative was included in the verified findings, and the LAMMPS findings do not provide a matched comparative protocol.
- Rationale: A task-specific comparison cannot be grounded in the verified findings because only LAMMPS primary documentation and release metadata were verified here.
- Comparison conditions: The verified findings set lacks alternative-side primary evidence and lacks checkpoint-specific LAMMPS benchmark numbers for matched comparison.
- Evidence: https://github.com/lammps/lammps/releases, https://lammps.org/download

## Limitations and safety

### Limitations

- The verified findings do not report checkpoint-specific numeric benchmark values for `stable_22Jul2025_update4`, so benchmark-based claims for this exact release cannot be established from the checked primary sources. Sources: https://github.com/lammps/lammps/releases, https://lammps.org/download, https://docs.lammps.org/Speed_kokkos.html
- Compatibility notes for KOKKOS were last updated for LAMMPS version 11 February 2026 and Kokkos library version 5.0.2, so the documentation verified here is package/manual-level evidence rather than a per-checkpoint benchmark or per-wrapper validation artifact. Sources: https://docs.lammps.org/Speed_kokkos.html
- Forge-wrapper runtime or container license terms beyond upstream GPLv2 were not reported in the verified primary sources used for this audit. Sources: https://github.com/lammps/lammps/tree/stable_22Jul2025_update4, https://github.com/lammps/lammps, https://lammps.org/download

### Safety

- Use expert review and downstream validation for scientific runs whose correctness depends on KOKKOS execution-mode defaults, because documented defaults differ across CPU and GPU settings and GPU-aware MPI availability changes behavior. Sources: https://docs.lammps.org/package.html, https://docs.lammps.org/Speed_kokkos.html
- Do not assume the Forge wrapper provides upstream-verified handling rules for sensitive or clinical data, because the verified primary sources describe molecular dynamics software and runtime behavior but do not report PHI or clinical-workflow guarantees. Sources: https://github.com/lammps/lammps/tree/stable_22Jul2025_update4, https://docs.lammps.org/Commands_structure.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### LAMMPS releases

- URL: https://github.com/lammps/lammps/releases
- Publisher: LAMMPS GitHub
- Type: `repository`
- Primary because: Official upstream GitHub releases page for verifying the exact stable release update, tag name, release date, commit hash, and signed-release metadata.
- Scope: LAMMPS upstream release history including `stable_22Jul2025_update4`
- Supports: identity.checkpoint
- Supports: identity.revision
- Supports: researchSummary release identity
- Supports: avoid-use benchmark absence check
- Supports: limitations benchmark absence check
- Supports: comparisons insufficient-evidence scoping

### LAMMPS repository tree for stable_22Jul2025_update4

- URL: https://github.com/lammps/lammps/tree/stable_22Jul2025_update4
- Publisher: LAMMPS GitHub
- Type: `repository`
- Primary because: Official upstream repository tree for the exact tag, used to verify the exact checkpoint tree identity and the upstream GPLv2 license statement.
- Scope: LAMMPS exact checkpoint `stable_22Jul2025_update4`
- Supports: identity.upstreamName
- Supports: identity.license
- Supports: recommended classical MD use
- Supports: safety non-clinical boundary
- Supports: limitations license/wrapper-term boundary

### LAMMPS upstream repository

- URL: https://github.com/lammps/lammps
- Publisher: LAMMPS GitHub
- Type: `repository`
- Primary because: Official upstream repository used to corroborate GPLv2 licensing at the repository level.
- Scope: LAMMPS upstream repository metadata
- Supports: identity.license
- Supports: limitations license/wrapper-term boundary

### LAMMPS Build documentation

- URL: https://docs.lammps.org/Build.html
- Publisher: LAMMPS documentation
- Type: `official-documentation`
- Primary because: Official build documentation used to verify build-system architecture claims.
- Scope: LAMMPS build system documentation applicable to the verified release/manual set
- Supports: identity.architecture

### LAMMPS KOKKOS speed documentation

- URL: https://docs.lammps.org/Speed_kokkos.html
- Publisher: LAMMPS documentation
- Type: `official-documentation`
- Primary because: Official KOKKOS documentation used to verify KOKKOS execution modes and package-level compatibility-note scope.
- Scope: LAMMPS KOKKOS documentation applicable to the verified release/manual set
- Supports: identity.architecture
- Supports: recommended KOKKOS use
- Supports: conditional KOKKOS hardware use
- Supports: output post-validation for KOKKOS
- Supports: limitations package/manual-level evidence scope
- Supports: benchmarks evidence gap locator

### LAMMPS download page

- URL: https://lammps.org/download
- Publisher: LAMMPS project
- Type: `official-documentation`
- Primary because: Official project download page used to verify that the stable 22 Jul 2025 release was last updated on 16 Apr 2026 and is licensed under GPLv2.
- Scope: Official LAMMPS release/distribution metadata for the stable 22 Jul 2025 release
- Supports: identity.license
- Supports: researchSummary release update metadata
- Supports: avoid-use benchmark absence check
- Supports: limitations benchmark absence check
- Supports: comparisons insufficient-evidence scoping

### LAMMPS commands structure documentation

- URL: https://docs.lammps.org/Commands_structure.html
- Publisher: LAMMPS documentation
- Type: `official-documentation`
- Primary because: Official command-structure documentation used to verify semantic inputs, input-script structure, and task formatting.
- Scope: LAMMPS input-script structure documentation
- Supports: recommended classical MD use
- Supports: input semantics
- Supports: accepted input format
- Supports: preprocessing structure
- Supports: task-specific formatting
- Supports: avoid-use JSON submission schema boundary
- Supports: safety non-clinical boundary

### LAMMPS data format documentation

- URL: https://docs.lammps.org/99/data_format.html
- Publisher: LAMMPS documentation
- Type: `official-documentation`
- Primary because: Official data-format documentation used to verify data-file formatting and validation requirements.
- Scope: LAMMPS data-file input format documentation
- Supports: acceptedFormats data file
- Supports: preprocessing data file
- Supports: input validation rules
- Supports: avoid-use JSON submission schema boundary

### LAMMPS run output documentation

- URL: https://docs.lammps.org/Run_output.html
- Publisher: LAMMPS documentation
- Type: `official-documentation`
- Primary because: Official runtime-output documentation used to verify output objects and their interpretation.
- Scope: LAMMPS runtime output/logging documentation
- Supports: accepted output/logfile format
- Supports: outputs
- Supports: interpretation
- Supports: post-output validation
- Supports: avoid-use JSON submission schema boundary

### LAMMPS package documentation

- URL: https://docs.lammps.org/package.html
- Publisher: LAMMPS documentation
- Type: `official-documentation`
- Primary because: Official package documentation used to verify documented KOKKOS defaults and GPU-aware MPI behavior.
- Scope: LAMMPS package/KOKKOS behavior documentation
- Supports: conditional KOKKOS use
- Supports: input validation for KOKKOS
- Supports: post-output validation for KOKKOS
- Supports: limitations/default-behavior caveats
- Supports: safety expert-validation rule

### Exact official starting source declared by Forge

- URL: https://github.com/lammps/lammps/releases/tag/stable_22Jul2025_update4
- Publisher: github.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: lammps-md
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Benchmarks gap: Checked primary sources `https://github.com/lammps/lammps/releases` (release entry for `stable_22Jul2025_update4`), `https://lammps.org/download` (stable release listing for 22 Jul 2025, updated 16 Apr 2026), and `https://docs.lammps.org/Speed_kokkos.html` (KOKKOS documentation heading and compatibility-note content). No checkpoint-specific numeric benchmark table, figure, or metric value for `stable_22Jul2025_update4` was reported in the verified findings.
- Comparisons gap: The verified findings set contains no primary-source benchmark or evaluation materials for `gromacs-md-ngc-wrapper`, `openmm-md-8-5-1-wrapper`, or `microsoft-bioemu-v1-1`, so only `insufficient-evidence` comparisons are supportable.
- Forge/runtime license gap: The verified primary sources establish upstream GPLv2 licensing for LAMMPS, but do not report separate authoritative license terms for the Forge wrapper `lammps-kokkos-md-wrapper` or any NVIDIA container/runtime terms within the verified findings.
- JSON submission-schema gap: Checked `https://docs.lammps.org/Commands_structure.html`, `https://docs.lammps.org/99/data_format.html`, and `https://docs.lammps.org/Run_output.html`; the verified findings describe script structure, data-file format, and runtime/log outputs, but do not report a canonical upstream JSON job-submission schema.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 19 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://github.com/lammps/lammps/releases/tag/stable_22Jul2025_update4 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary host sourceforge.net: $.sources[10] uses forbidden secondary host sourceforge.net Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://doc.lammps.org/stable/Manual.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://doc.lammps.org/stable/Manual.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/lammps/patch23Oct2017/layers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://doc.lammps.org/stable/Manual.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://matsci.org/t/generating-images-flags-from-dump-file-for-rerun/66225 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ccportal.ims.ac.jp/en/node/3870 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://matsci.org/t/generating-images-flags-from-dump-file-for-rerun/66225 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://matsci.org/t/lammps-users-cannot-get-a-better-performance-on-gpus-compared-to-cpus/37832 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://gensoft.pasteur.fr/docs/lammps/2020.03.03/Speed_kokkos.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://matsci.org/t/generating-images-flags-from-dump-file-for-rerun/66225 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://matsci.org/t/generating-images-flags-from-dump-file-for-rerun/66225 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://github.com/lammps/lammps/releases/tag/stable_22Jul2025_update4: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
