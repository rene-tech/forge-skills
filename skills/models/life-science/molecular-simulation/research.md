# Molecular Simulation model selection

- Category: `life-science`
- Group: `molecular-simulation`
- Independent audit: `revised`
- Researched: `2026-07-23T23:01:06.136692+00:00`

Select among the exact Forge candidates `gromacs-md-ngc-wrapper`, `lammps-kokkos-md-wrapper`, `microsoft-bioemu-v1-1`, and `openmm-md-8-5-1-wrapper` for two narrowly evidenced task families only: (1) molecular simulation runtimes documented by an official upstream container/repository source, and (2) protein conformational-ensemble generation documented by the official BioEmu repository and Microsoft Research publication source. Outside scope are unsupported claims about exact Forge wrapper versionKey identity, exact request schemas, exact file-format contracts, wrapper-level benchmarks, MLIP integration, or cross-engine scientific comparability when the provided primary findings do not specify them.

## Questions to answer before selecting

- Is the goal sequence-to-ensemble protein conformational sampling or classical molecular simulation from prepared inputs?
- Do you require the exact candidate to be evidenced by an official container tag/release page, or is repository-level evidence sufficient?
- Are your inputs prepared structure/topology/simulation files, or protein sequence with MSA?
- Do you need an engine specifically described for proteins and lipids, or a more general molecular-dynamics software package?
- Is Kokkos/CUDA acceleration specifically required and evidenced at the release/package-documentation level?
- Do you need documented repository files such as MODEL_CARD.md, LICENSE, SECURITY.md, or Azure AI Foundry documentation?
- Do you need outputs such as trajectories/energies versus ensembles of protein structures?
- Can you tolerate evidence gaps about exact Forge wrapper versionKey linkage, accepted JSON schema, and exact output file contract?
- Do you need benchmarked speed/accuracy claims from an original publication, and if so are upstream-checkpoint claims acceptable rather than Forge-runtime claims?
- Do licensing constraints rule out GPL-2.0 code or favor MIT-style terms, recognizing that exact Forge wrapper redistribution terms are not established in the findings?

## Comparability rules

- Classical MD engines may be compared only when the same scientific system definition, prepared inputs, and simulation settings are used; the provided findings do not supply a canonical shared protocol across GROMACS, LAMMPS, and OpenMM.
- Upstream publication claims for BioEmu are not directly comparable to container/repository evidence for GROMACS, LAMMPS, or OpenMM unless the task is narrowed to protein conformational-ensemble generation from sequence and the comparison protocol is explicitly matched.
- Do not compare Forge wrapper versions by exact versionKey, because the findings do not provide primary identity evidence linking the exact Forge versionKey strings to upstream unchanged artifacts for any of the four candidates.
- Do not compare performance or quality across candidates using third-party issues, discussions, blogs, or mirrors; only the retained top-level primary sources are admissible.
- Kokkos/package-setting documentation for LAMMPS establishes package controls, not end-to-end benchmark equivalence to GROMACS or OpenMM; identical potentials, neighbor settings, hardware, and input files would still need to match.
- OpenMM application-guide output/state documentation is comparable to other engines only at the level of generic simulation observables; the findings do not specify a shared benchmark dataset or protocol.

## Conditional routing

### Prefer `microsoft-bioemu-v1-1` when Protein conformational-ensemble generation is the primary task and upstream-checkpoint evidence from an official repository and original Microsoft Research publication is acceptable.

- Why: The official BioEmu repository is present, and the Microsoft Research publication states that BioEmu-1 can generate thousands of protein structures per hour on a single GPU, provides orders-of-magnitude greater computational efficiency than classical MD, predicts relative free energies with approximately 1 kcal/mol accuracy compared to millisecond-scale MD and experimental data, and captures functional motions such as cryptic pocket formation, local unfolding, and domain rearrangements. This is upstream-checkpoint evidence, not Forge-runtime benchmark evidence.
- Alternative: gromacs-md-ngc-wrapper
- Alternative: lammps-kokkos-md-wrapper
- Alternative: openmm-md-8-5-1-wrapper
- Evidence: https://github.com/microsoft/bioemu, https://microsoft.com/en-us/research/publication/scalable-emulation-of-protein-equilibrium-ensembles-with-generative-deep-learning

### Prefer `gromacs-md-ngc-wrapper` when A containerized molecular-dynamics engine with an official catalog tag evidenced in the provided findings is required for proteins and lipids.

- Why: The NVIDIA NGC GROMACS source lists container image tags including `hpc/gromacs:2023.2` and describes GROMACS as a popular molecular dynamics application used to simulate proteins and lipids.
- Alternative: lammps-kokkos-md-wrapper
- Alternative: openmm-md-8-5-1-wrapper
- Alternative: microsoft-bioemu-v1-1
- Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs

### Prefer `lammps-kokkos-md-wrapper` when The user specifically needs a GPL-2.0-licensed upstream molecular-dynamics codebase with an official stable release page in the findings.

- Why: The official LAMMPS repository findings state that LAMMPS is a public development project of the LAMMPS molecular dynamics software package and is distributed under the GPL-2.0 license, and the official release URL supplied by Forge is the stable_22Jul2025_update4 release page. The package documentation also evidences KOKKOS package controls via the `-k on` command-line switch.
- Alternative: gromacs-md-ngc-wrapper
- Alternative: openmm-md-8-5-1-wrapper
- Alternative: microsoft-bioemu-v1-1
- Evidence: https://github.com/lammps/lammps/releases/tag/stable_22Jul2025_update4, https://github.com/lammps/lammps, https://docs.lammps.org/package.html

### Prefer `openmm-md-8-5-1-wrapper` when The user needs official upstream documentation that simulation state outputs can include positions, velocities, forces, energy, parameters, parameterDerivatives, and integratorParameters.

- Why: The OpenMM repository is the official source declared by Forge, and the official OpenMM user guide documents that `Context.getState()` can return positions, velocities, forces, energy, parameters, parameterDerivatives, and integratorParameters, with a documented `periodic` argument behavior.
- Alternative: gromacs-md-ngc-wrapper
- Alternative: lammps-kokkos-md-wrapper
- Alternative: microsoft-bioemu-v1-1
- Evidence: https://github.com/openmm/openmm, https://docs.openmm.org/latest/userguide/application/04_advanced_sim_examples.html

### Prefer `insufficient-evidence` when The selection depends on exact Forge wrapper versionKey identity, exact accepted request schema, exact output file contract, or directly comparable benchmark results across the four candidates.

- Why: The retained primary findings do not establish exact Forge wrapper versionKey linkage for any candidate, do not provide a canonical shared cross-engine benchmark protocol, and do not document exact accepted Forge input/output schemas at wrapper level.
- Alternative: gromacs-md-ngc-wrapper
- Alternative: lammps-kokkos-md-wrapper
- Alternative: microsoft-bioemu-v1-1
- Alternative: openmm-md-8-5-1-wrapper
- Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://github.com/lammps/lammps/releases/tag/stable_22Jul2025_update4, https://github.com/microsoft/bioemu, https://github.com/openmm/openmm

## Benchmark taxonomy

### Protein conformational-ensemble generation (sequence/MSA to protein structure ensemble)

- Datasets: Evidence gap: No canonical dataset names or splits are specified in the provided primary findings for the exact BioEmu v1.1 Forge candidate.
- Metrics: Structures generated per hour on a single GPU; higher is better, Relative free-energy error in kcal/mol versus millisecond-scale MD and experimental data; lower is better, Evidence gap: The provided findings do not specify the exact benchmark protocol, dataset split, or aggregation details for these BioEmu publication metrics
- Compare only when: Treat Microsoft Research publication results as upstream-checkpoint evidence for BioEmu, not Forge-runtime evidence.
- Compare only when: Use the same protein targets, sequence/MSA preparation, and evaluation procedure before comparing ensemble-generation results.
- Compare only when: Do not compare these publication metrics directly against classical MD engines unless the protocol explicitly measures the same task and conditions.

### Classical molecular dynamics simulation for biomolecular systems

- Datasets: Evidence gap: No canonical shared coordinate/topology benchmark dataset names are specified in the retained primary findings.
- Metrics: Evidence gap: No verified cross-candidate numeric benchmark values are documented in the retained primary findings for the exact Forge candidates, Simulation observables such as positions, velocities, forces, and energy may be relevant, but the findings do not define a shared benchmark metric set
- Compare only when: Match prepared system definition, force field or potential, integrator, timestep, boundary conditions, and output sampling before comparing engines.
- Compare only when: Container tag/release identity must be explicit if comparing specific packaged artifacts.
- Compare only when: Do not use repository popularity, issue discussions, or unsupported third-party scripts as scientific performance evidence.

### LAMMPS package-configuration-dependent molecular simulation

- Datasets: Evidence gap: No canonical dataset names are specified in the retained primary findings for Kokkos-specific evaluation.
- Metrics: Evidence gap: No verified numeric benchmark metrics are provided in the retained primary findings for `lammps-kokkos-md-wrapper`, Configuration controls documented include binsize, neigh or neigh/thread behavior, gpu/aware setting, and `-k on` package activation, but these are setup parameters rather than benchmark metrics
- Compare only when: Compare only runs with matched package settings such as KOKKOS activation and neighbor-list options.
- Compare only when: Hardware/software stack and MPI/GPU-awareness settings must match because the package documentation indicates GPU-specific defaults.
- Compare only when: Do not infer quality or speed advantages without matched benchmark inputs and reported numeric outcomes.

### Simulation-state extraction and reporting

- Datasets: Evidence gap: No canonical benchmark dataset names are specified in the retained primary findings for OpenMM state extraction.
- Metrics: Availability of positions, velocities, forces, energy, parameters, parameterDerivatives, and integratorParameters from the simulation state, Evidence gap: No cross-candidate numeric scoring protocol is specified for state-extraction functionality
- Compare only when: Compare only if each candidate exposes analogous outputs under matched simulation conditions.
- Compare only when: Document whether periodic wrapping behavior is matched when comparing positions because OpenMM documents a `periodic` argument affecting returned positions.

## Primary sources

- [NVIDIA NGC GROMACS container catalog](https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs) — NVIDIA NGC; supports Official starting source for `gromacs-md-ngc-wrapper`, Container tags include `hpc/gromacs:2023.2`, GROMACS is described as a popular molecular dynamics application used to simulate proteins and lipids, Evidence relevant to upstream/container identity, not exact Forge wrapper versionKey identity
- [LAMMPS stable_22Jul2025_update4 release](https://github.com/lammps/lammps/releases/tag/stable_22Jul2025_update4) — LAMMPS GitHub repository; supports Official starting source for `lammps-kokkos-md-wrapper`, Evidence of an official stable release locator for the scoped candidate
- [LAMMPS GitHub repository](https://github.com/lammps/lammps) — LAMMPS GitHub repository; supports LAMMPS is a public development project of the LAMMPS molecular dynamics software package, LAMMPS is distributed under the GPL-2.0 license, Repository-level evidence used for task scoping and licensing
- [LAMMPS package documentation](https://docs.lammps.org/package.html) — LAMMPS documentation; supports KOKKOS package defaults can be set via the `-k on` command-line switch, Neighbor-list and GPU-aware package configuration facts relevant to Kokkos-scoped setup comparability
- [Microsoft BioEmu GitHub repository](https://github.com/microsoft/bioemu) — Microsoft GitHub repository; supports Official starting source for `microsoft-bioemu-v1-1`, Repository contains files including MODEL_CARD.md, LICENSE, README.md, SECURITY.md, and AZURE_AI_FOUNDRY.md, Repository-level evidence for BioEmu identity and documentation surface
- [Scalable emulation of protein equilibrium ensembles with generative deep learning](https://microsoft.com/en-us/research/publication/scalable-emulation-of-protein-equilibrium-ensembles-with-generative-deep-learning) — Microsoft Research; supports BioEmu-1 can generate thousands of protein structures per hour on a single GPU, BioEmu provides orders of magnitude greater computational efficiency compared to classical molecular dynamics simulations, BioEmu runs up to 100,000 times faster than traditional simulations, BioEmu predicts relative free energies with approximately 1 kcal/mol accuracy compared to millisecond-scale MD and experimental data, BioEmu captures functional motions such as cryptic pocket formation, local unfolding, and domain rearrangements, Original upstream publication evidence for ensemble-generation task claims
- [OpenMM GitHub repository](https://github.com/openmm/openmm) — OpenMM GitHub repository; supports Official starting source for `openmm-md-8-5-1-wrapper`, Repository-level evidence for OpenMM identity
- [OpenMM User Guide: Advanced Simulation Examples](https://docs.openmm.org/latest/userguide/application/04_advanced_sim_examples.html) — OpenMM documentation; supports `Context.getState()` can return positions, velocities, forces, energy, parameters, parameterDerivatives, and integratorParameters, The `periodic` argument determines whether positions are wrapped to the periodic box, Official output/state-shape evidence for OpenMM

## Evidence gaps

- Evidence gap: The retained primary findings do not verify exact Forge wrapper versionKey linkage for `gromacs-md-ngc-wrapper` (`ngc-2023-2-wrapper-20260602`) beyond the upstream/container source URL and catalog tag evidence.
- Evidence gap: The retained primary findings do not verify exact Forge wrapper versionKey linkage for `lammps-kokkos-md-wrapper` (`lammps-22jul2025u4-sm80-20260616`) beyond the upstream stable release page and repository/package documentation.
- Evidence gap: The retained primary findings do not verify exact Forge wrapper versionKey linkage for `microsoft-bioemu-v1-1` (`bioemu-v1-1-bioemu-1-3-1-wrapper`) or prove that Forge serves an unchanged upstream checkpoint for that exact wrapper string.
- Evidence gap: The retained primary findings do not verify exact Forge wrapper versionKey linkage for `openmm-md-8-5-1-wrapper` (`8-5-1-cuda12-wrapper-profiler-optimized-20260604`) beyond the upstream repository source URL.
- Evidence gap: Exact accepted Forge input schemas, field names, file requirements, and validation rules are not specified in the retained primary findings for any of the four candidates.
- Evidence gap: Exact Forge output contracts, file formats, and schema guarantees are not specified in the retained primary findings for any of the four candidates.
- Evidence gap: Cross-candidate benchmark datasets, splits, and matched protocols for direct scientific comparison are not documented in the retained primary findings.
- Evidence gap: No retained primary finding provides verified numeric benchmark rows for `gromacs-md-ngc-wrapper`, `lammps-kokkos-md-wrapper`, or `openmm-md-8-5-1-wrapper` under matched conditions.
- Evidence gap: The retained primary findings do not establish wrapper-level MLIP integration details for the exact Forge candidates.
- Evidence gap: Licensing and redistribution terms for the exact Forge wrappers or containers, distinct from upstream repository code licenses, are not fully specified in the retained primary findings.
- Evidence gap: For BioEmu, the retained primary findings provide upstream publication claims but do not specify the exact dataset names, splits, or benchmark tables needed to reconstruct checkpoint-specific benchmark rows for the exact Forge candidate.
- Evidence gap: Comparison-specific evidence is insufficient to rank all four candidates on a single shared molecular-simulation benchmark because the retained primary findings cover different task types and documentation depths across candidates.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: unexpected property benchmarkEvidenceMapping Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses forbidden secondary URL https: $.sources[7] uses forbidden secondary URL https://developer.nvidia.com/blog/enabling-scalable-ai-driven-molecular-dynamics-simulations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://cass.community/impacts/2026-01-lammps.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
