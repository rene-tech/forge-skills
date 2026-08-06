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

- Research key: `catalog-ngc-nvidia-com-orgs-hpc-containers-gromacs-305a6b721f`
- Independent audit: `revised`
- Researched: `2026-07-24T00:06:00.113148+00:00`

Primary NVIDIA NGC evidence verifies the scoped runtime as hpc/gromacs:2023.2, an NVIDIA NGC HPC container for GROMACS molecular-dynamics use, with container metadata, example invocation, multi-arch status, no multinode support, and GPU-oriented example mdrun flags. Upstream GROMACS primary documentation supports checkpoint-scoped facts about canonical MD inputs, outputs, and file formats for GROMACS 2023.2. The checked primary sources do not report an authoritative mapping from the Forge wrapper string ngc-2023.2-wrapper-20260602 to a manifest digest, commit, or other immutable upstream artifact, and no primary-source numeric benchmark tied to the NVIDIA hpc/gromacs:2023.2 container tag was found.

## Identity

- Upstream name: GROMACS
- Checkpoint/version: 2023.2 (NGC container tag)
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Molecular dynamics application packaged as the NVIDIA NGC container image hpc/gromacs:2023.2; upstream GROMACS documentation cited here establishes command-line MD workflow components such as gmx grompp and gmx mdrun.
- License: Upstream GROMACS: GNU Lesser General Public License (LGPL) version 2.1 or any later version. NVIDIA container/runtime terms: not reported in the checked primary NVIDIA hpc/gromacs sources used here.
- Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://manual.gromacs.org/2023.2/reference-manual/preface.html, https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html

## Selection

### Recommended

- **Running bounded nonclinical molecular-dynamics simulations with the NVIDIA NGC hpc/gromacs:2023.2 container** — The NGC container listing identifies hpc/gromacs:2023.2 and provides an example batch run command invoking gmx mdrun with explicit runtime flags for GPU-accelerated execution.
  Scope: NVIDIA NGC hpc/gromacs:2023.2 container tag
  Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- **Simulating biochemical molecules such as proteins, lipids, and nucleic acids with GROMACS workflows served through the container** — The NGC container listing describes GROMACS as a molecular dynamics application used to simulate proteins and lipids and as designed for biochemical molecules like proteins, lipids, and nucleic acids; upstream GROMACS documentation provides the canonical gmx grompp to gmx mdrun workflow.
  Scope: NVIDIA NGC hpc/gromacs:2023.2 container tag with upstream GROMACS 2023.2 workflow evidence
  Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html

### Conditional

- **Using the Forge wrapper string for provenance-sensitive audit trails or release-to-artifact traceability** — Only if a primary source later provides an explicit mapping from ngc-2023.2-wrapper-20260602 to a specific container manifest, release artifact, or upstream revision; the checked primary sources do not provide that mapping.
  Scope: Forge wrapper string ngc-2023.2-wrapper-20260602 relative to NVIDIA NGC hpc/gromacs:2023.2
  Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/gromacs/2023.2/layers

### Avoid

- **Clinical decision-making or regulated clinical use** — The checked primary NVIDIA NGC source presents GROMACS as a research molecular-dynamics application for simulating biochemical molecules and does not document clinical authorization, regulatory clearance, or clinical-use approval.
  Scope: NVIDIA NGC hpc/gromacs:2023.2 container tag
  Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- **Assuming multinode execution is supported by this container tag** — The NGC container listing states that the container does not support multinode execution.
  Scope: NVIDIA NGC hpc/gromacs:2023.2 container tag
  Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs

## Input preparation

### Semantic inputs

- A molecular system to be simulated, including biochemical molecules such as proteins, lipids, and nucleic acids, is within the documented problem scope. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- The only input file required by gmx mdrun to start a run is a .tpr run input file in upstream GROMACS workflow documentation. Sources: https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html

### Accepted formats

- Upstream GROMACS documentation states that the run input file is .tpr and that trajectory files can be written in .trr, .tng, or .xtc format. Sources: https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html
- Upstream GROMACS topology and structure documentation covers .top topology files and .gro coordinate files. Sources: https://manual.gromacs.org/documentation/2023.2/reference-manual/topologies/topology-file-formats.html

### Preprocessing

- Upstream GROMACS documentation states that the .tpr run input file is generated by gmx grompp from a structure file (.gro), topology file (.top), mdp parameter file, and optionally an index file (.ndx). Sources: https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html
- The NGC example batch run command sets the working directory via -build_base_dir=/usr/local/gromacs -build_default=avx2_256 before invoking gmx mdrun. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs

### Pre-submit validation

- Before mdrun, upstream workflow documentation requires creation of a valid .tpr file via gmx grompp from the documented upstream inputs; the research did not find additional container-tag-specific input bounds or schema validation rules. Sources: https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html

### Task-specific formatting

- The NGC example batch run command uses hpc/gromacs:2023.2 and invokes gmx mdrun with flags including -ntmpi 8, -ntomp 15, -nb gpu, -pme gpu, -npme 1, -update gpu, -bonded gpu, -nsteps 100000, -resetstep 90000, -noconfout, -dlb no, -nstlist 300, -pin on, -v, and -gpu_id 0123. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- For upstream multi-simulation formatting, gmx mdrun -multidir requires one subdirectory per simulation, each containing the necessary input files such as topol.tpr, and directory order matters when simulation order matters. Sources: https://manual.gromacs.org/2023.2/user-guide/mdrun-features.html

## Output interpretation

### Outputs

- Upstream GROMACS documentation says typical outputs of gmx mdrun are a trajectory file (.trr), a log file (.log), and optionally a checkpoint file (.cpt). Sources: https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html
- The NGC example batch run command writes a GROMACS log and energy-related outputs through the invoked gmx mdrun workflow; the checked primary findings specifically report example output paths only for command invocation context, not a full wrapper output schema. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs

### Interpretation

- For rerun mode, upstream GROMACS documentation states that only positions are read from the trajectory, velocities are ignored, and the output includes potential energy, volume, density, dH/dl terms, and restraint information; it does not report kinetic energy, total energy, conserved energy, temperature, virial, or pressure in rerun output. Sources: https://manual.gromacs.org/2023.2/user-guide/mdrun-features.html

### Post-inference validation

- When gmx mdrun receives a TERM or INT signal, upstream documentation states it stops at the next neighbor-search step or second global communication step, writes usual output, and creates a checkpoint file; users can use that documented behavior as a post-run integrity check for interrupted runs. Sources: https://manual.gromacs.org/2023.2/user-guide/mdrun-features.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### NVIDIA NGC nvidia/gromacs container listing — `tradeoff`

- Task: Selecting between the scoped hpc/gromacs:2023.2 runtime and another NVIDIA GROMACS container listing for documented hardware/runtime requirements
- Criteria: The scoped hpc container source provides exact tag identity, image metadata, no-multinode status, and example mdrun invocation, while the alternate NVIDIA listing provides hardware/runtime prerequisites such as supported GPU architectures, AVX requirement on x86_64, Singularity or nvidia-docker runtime, and CUDA driver requirement.
- Rationale: Both are primary NVIDIA sources but they support different operational questions. Use the scoped hpc listing for exact tag-level identity and example command details; use the alternate NVIDIA listing only for the documented hardware/runtime requirement facts it reports. The findings do not establish that the alternate listing is the same scoped artifact as hpc/gromacs:2023.2.
- Comparison conditions: Comparison is documentation-scope-specific rather than a performance comparison; protocols differ because one source is the scoped hpc listing and the other is an alternate NVIDIA container listing.
- Evidence: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://catalog.ngc.nvidia.com/orgs/nvidia/containers/gromacs

## Limitations and safety

### Limitations

- No authoritative primary-source mapping from the Forge wrapper string ngc-2023.2-wrapper-20260602 to a specific container manifest, release artifact, or upstream revision was found in the checked sources. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/gromacs/2023.2/layers
- The scoped NGC container listing states that the container does not support multinode execution. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- The checked primary NVIDIA hpc/gromacs sources used here do not report NVIDIA container/runtime license terms for this exact container tag, so only upstream GROMACS licensing is directly established by primary evidence in this dossier. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs, https://manual.gromacs.org/2023.2/reference-manual/preface.html
- No primary-source numeric benchmark tied to the NVIDIA hpc/gromacs:2023.2 container tag was found in the checked scoped source. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/gromacs/2023.2

### Safety

- Do not infer clinical suitability, regulatory clearance, or clinical authorization from the scoped NVIDIA NGC source; the checked source documents research molecular-dynamics usage, not regulated clinical use. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- Treat molecular simulation inputs and outputs as research data requiring domain-expert review before any consequential life-science interpretation, because the checked scoped NVIDIA sources do not provide clinical validation or regulated-use guidance. Sources: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NGC Catalog — GROMACS (hpc org)

- URL: https://catalog.ngc.nvidia.com/orgs/hpc/containers/gromacs
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC container listing for the scoped hpc GROMACS container; supports exact tag identity, metadata, supported/unsupported runtime scope, and example command facts.
- Scope: NVIDIA NGC hpc/gromacs container listing including the 2023.2 tag context
- Supports: identity.upstreamName
- Supports: identity.checkpoint
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: avoidUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.outputs
- Supports: comparisons
- Supports: limitations
- Supports: safety

### NVIDIA NGC GROMACS container tag layers (2023.2)

- URL: https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/gromacs/2023.2/layers
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC layers page for the scoped 2023.2 tag; supports tag-layer and entrypoint facts and is relevant to provenance limitations.
- Scope: NVIDIA NGC hpc/gromacs:2023.2 layers page
- Supports: conditionalUseCases
- Supports: limitations

### NVIDIA NGC GROMACS container tag page (2023.2)

- URL: https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/gromacs/2023.2
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC tag page for the scoped 2023.2 container tag; used here specifically to verify absence of container-tied numeric benchmark reporting in the checked locator.
- Scope: NVIDIA NGC hpc/gromacs:2023.2 tag page
- Supports: researchSummary
- Supports: limitations
- Supports: evidenceGaps

### NVIDIA NGC Catalog — GROMACS (nvidia org)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/gromacs
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC container listing under the nvidia org; supports documented runtime prerequisites used only in a scoped comparison note.
- Scope: Alternate official NVIDIA GROMACS container listing with runtime prerequisite documentation
- Supports: comparisons

### GROMACS manual 2023.2 preface

- URL: https://manual.gromacs.org/2023.2/reference-manual/preface.html
- Publisher: GROMACS project
- Type: `official-documentation`
- Primary because: Official upstream GROMACS manual page establishing upstream licensing for GROMACS 2023.2.
- Scope: Upstream GROMACS 2023.2 licensing documentation
- Supports: identity.license
- Supports: limitations

### GROMACS user guide — getting started (2023)

- URL: https://manual.gromacs.org/documentation/2023/user-guide/getting-started.html
- Publisher: GROMACS project
- Type: `official-documentation`
- Primary because: Official upstream GROMACS workflow documentation for input preparation and typical outputs.
- Scope: Upstream GROMACS workflow documentation applicable to GROMACS 2023.x command-line usage
- Supports: identity.architecture
- Supports: recommendedUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: outputInterpretation.outputs

### GROMACS topology file formats (2023.2)

- URL: https://manual.gromacs.org/documentation/2023.2/reference-manual/topologies/topology-file-formats.html
- Publisher: GROMACS project
- Type: `official-documentation`
- Primary because: Official upstream GROMACS file-format documentation for topology and coordinate inputs.
- Scope: Upstream GROMACS 2023.2 topology and coordinate file documentation
- Supports: inputPreparation.acceptedFormats

### GROMACS user guide — mdrun features (2023.2)

- URL: https://manual.gromacs.org/2023.2/user-guide/mdrun-features.html
- Publisher: GROMACS project
- Type: `official-documentation`
- Primary because: Official upstream GROMACS documentation for mdrun operational features, rerun semantics, multi-simulation formatting, termination behavior, and checkpoint writing.
- Scope: Upstream GROMACS 2023.2 mdrun feature documentation
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.interpretation
- Supports: outputInterpretation.validation

## Evidence gaps

- Evidence gap: No primary-source numeric benchmark tied to the container tag was found at https://catalog.ngc.nvidia.com/orgs/hpc/-/containers/gromacs/2023.2 in the checked locator "2023.2 container tag metadata and example-command sections".
- Evidence gap: The research did not find a primary-source mapping from the Forge wrapper string ngc-2023.2-wrapper-20260602 to a specific manifest digest, release artifact, or upstream revision.
- Evidence gap: The checked primary NVIDIA hpc/gromacs sources do not provide a wrapper-exposed JSON input schema or a machine-readable Forge wrapper contract.
- Evidence gap: The checked primary NVIDIA hpc/gromacs sources do not provide container-tag-specific post-processing or scientific validation procedures beyond example invocation context.
- Evidence gap: The findings do not report primary-source numeric benchmarks or protocol-matched comparisons for hpc/gromacs:2023.2 against alternative runtimes, so performance comparison remains unsupported.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.
