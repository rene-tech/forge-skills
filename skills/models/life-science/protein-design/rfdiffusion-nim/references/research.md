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

- Research key: `build-nvidia-com-ipd-rfdiffusion-9028cdc37c`
- Independent audit: `revised`
- Researched: `2026-07-23T22:46:09.522777+00:00`

The NVIDIA NIM package rfdiffusion-nim (version key nim-2-3-0-regional-mirror-onboarding, family build-nvidia-com-ipd-rfdiffusion-9028cdc37c) packages an upstream RFdiffusion implementation (RoseTTAFold Diffusion) for de novo protein backbone generation, motif scaffolding, and binder-design tasks. NVIDIA packaging materials (model card, NIM docs, NGC listing) state the package contains inference code and model weights and is governed by NVIDIA Community Model License and NVIDIA API Trial Service Terms; upstream RFdiffusion is released under a BSD license. The NIM documentation and benchmarking pages report serving-runtime performance (amino acids per second per step) on specific NVIDIA GPUs and document support/optimizations using NVIDIA Warp and TensorRT. The exact immutable upstream checkpoint identifier, immutable revision, and parameter count used by the NVIDIA NIM 2.3.0 packaging are not reported in the checked primary sources; several input/output semantics (presence of input_pdb, contigs, diffusion_steps, hotspot_res, output_pdb, elapsed_ms) and single-GPU runtime prerequisites are documented in NIM endpoint and prerequisites pages. Precise contigs DSL grammar, canonical sidechain-vs-backbone output semantics, canonical NIM post-inference validation pipeline, and protocol-matched comparisons to other Forge peers are not present in the checked primary sources and are recorded as evidence gaps.

## Identity

- Upstream name: RFdiffusion (RoseTTAFold Diffusion)
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: RoseTTAFold-based diffusion model (RoseTTAFold Diffusion); SE(3)-equivariant diffusion backbone generator
- License: NVIDIA Community Model License; NVIDIA API Trial Service Terms of Use; upstream RFdiffusion released under a BSD license (per upstream repository).
- Evidence: https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://docs.api.nvidia.com/nim/reference/ipd-rfdiffusion, https://github.com/RosettaCommons/RFdiffusion, https://github.com/RosettaCommons/RFdiffusion/blob/main/LICENSE, https://www.nature.com/articles/s41586-023-06415-8, https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/release-notes.html

## Selection

### Recommended

- **De novo protein backbone generation** — Upstream RFdiffusion is designed to generate novel protein backbones and scaffolds via a RoseTTAFold-based diffusion model; NVIDIA materials expose backbone-generation functionality in the NIM packaging.
  Scope: nim-2-3-0-regional-mirror-onboarding (NIM packaging of RFdiffusion)
  Evidence: https://www.nature.com/articles/s41586-023-06415-8, https://github.com/RosettaCommons/RFdiffusion, https://build.nvidia.com/ipd/rfdiffusion/modelcard
- **Binder design (structure-level binder backbone generation conditioned on a target)** — Upstream RFdiffusion and the NIM packaging document binder-design capability (generation of binder backbones conditioned on a target).
  Scope: nim-2-3-0-regional-mirror-onboarding (NIM packaging of RFdiffusion)
  Evidence: https://www.nature.com/articles/s41586-023-06415-8, https://github.com/RosettaCommons/RFdiffusion, https://build.nvidia.com/ipd/rfdiffusion/modelcard
- **Motif scaffolding (scaffolding specified motif regions into designed backbones)** — Upstream RFdiffusion and the NIM packaging document motif-scaffolding capability.
  Scope: nim-2-3-0-regional-mirror-onboarding (NIM packaging of RFdiffusion)
  Evidence: https://www.nature.com/articles/s41586-023-06415-8, https://github.com/RosettaCommons/RFdiffusion, https://build.nvidia.com/ipd/rfdiffusion/modelcard

### Conditional

- **Downstream structural-prediction and experimental validation required before practical deployment** — Evidence gap: primary-source documentation in the checked NVIDIA and upstream RFdiffusion materials does not provide an explicit, canonical validation protocol tied to this NIM packaging; downstream structural-prediction (e.g., recommended predictors and thresholds) and experimental verification are recommended practice but not documented as a canonical pipeline for this NIM in the checked sources.
  Scope: nim-2-3-0-regional-mirror-onboarding
  Evidence:

### Avoid

- **Use of generated designs for clinical decision-making, diagnostic, or therapeutic deployment without experimental validation and regulatory process** — Primary NVIDIA packaging materials do not provide explicit healthcare/clinical safety guidance or tested clinical validation; the model is presented as a design tool rather than clinical-grade software.
  Scope: nim-2-3-0-regional-mirror-onboarding
  Evidence: https://build.nvidia.com/ipd/rfdiffusion/modelcard

## Input preparation

### Semantic inputs

- NIM endpoint accepts target constraints in PDB format (input_pdb) and contigs as a string parameter to specify which regions to keep and the binder length; hotspot_res is an optional field for specifying hotspot residues. Sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/overview.html, https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html

### Accepted formats

- Official NIM accepted input/output fields documented include input_pdb (string or pre-uploaded asset reference), input_pdb_asset (optional asset id), contigs (string), hotspot_res (optional array), diffusion_steps (optional integer), random_seed (optional integer); outputs include output_pdb (string) and elapsed_ms (integer). Sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html, https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/overview.html

### Preprocessing

- Evidence gap: precise contigs DSL grammar and indexing conventions (for example, explicit chain-id syntax, whether indices are 1-based inclusive/exclusive, and exact allowable token forms) are not published in the checked NIM endpoint documentation.

### Pre-submit validation

- NIM endpoint parameter validation documented in NVIDIA endpoints includes that diffusion_steps is an integer (1.0.0 endpoints state default/minimum values are documented though references conflict on default); random_seed is optional; presence and syntactic correctness of input_pdb and contigs are validated by the service per endpoints page. Sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html

### Task-specific formatting

- The NIM API fields and example request/response shapes (input_pdb, contigs, hotspot_res, diffusion_steps, output_pdb, elapsed_ms) are documented in the NIM endpoints reference. Sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html, https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/overview.html

## Output interpretation

### Outputs

- The official NIM endpoint returns output_pdb (a string containing the generated protein structure in PDB format) and elapsed_ms (integer server-side elapsed time); input_pdb_asset may be used to reference uploaded assets. Sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html

### Interpretation

- Upstream RFdiffusion and RosettaCommons materials describe generated backbone coordinates as the primary structural output of RFdiffusion; sequence design is typically performed in separate downstream steps and the NIM returns PDB-format structure artifacts as its primary output. Sources: https://github.com/RosettaCommons/RFdiffusion, https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://www.nature.com/articles/s41586-023-06415-8
- Evidence gap: the checked primary sources do not explicitly state whether the NIM-packaged RFdiffusion output_pdb contains reconstructed sidechains (full sidechain modelling) or only backbone coordinates; endpoints document output_pdb but do not clarify sidechain presence/absence for the packaged NIM in the checked materials.

### Post-inference validation

- Evidence gap: canonical, NIM-specific post-inference validation pipelines (exact recommended use of specific structure-prediction tools, recommended thresholds, or a validated pipeline for NIM outputs) are not documented in the checked NVIDIA NIM materials.

## Public benchmarks

### RFdiffusion NIM single-GPU backbone generation throughput

- Dataset/split: RFdiffusion NIM benchmarking (2.x release benchmarking page) / not reported
- Metric/value: amino acids per second per step / 969.1 amino acids per second per step (`higher-is-better`)
- Model scope: RFdiffusion NIM 2.3.0 on H100 (measured on NIM packaging)
- Conditions: NIM serving-runtime measurement; optimizations using NVIDIA Warp and TensorRT reported; measured per NIM benchmarking page (single-GPU measurement).
- Source: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Locator: benchmarking page
- Caveat: Measurement reported by NVIDIA NIM benchmarking for the NIM packaging (serving-runtime measurement).
- Caveat: Reported conditions reference TensorRT/FP32-FP16 support and Warp optimizations in NVIDIA support/benchmarking documentation.

### RFdiffusion NIM single-GPU backbone generation throughput

- Dataset/split: RFdiffusion NIM benchmarking (2.x release benchmarking page) / not reported
- Metric/value: amino acids per second per step / 932.2 amino acids per second per step (`higher-is-better`)
- Model scope: RFdiffusion NIM 2.3.0 on GB200 (measured on NIM packaging)
- Conditions: NIM serving-runtime measurement; optimizations using NVIDIA Warp and TensorRT reported; measured per NIM benchmarking page (single-GPU measurement).
- Source: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Locator: benchmarking page
- Caveat: Measurement reported by NVIDIA NIM benchmarking for the NIM packaging (serving-runtime measurement).
- Caveat: Reported conditions reference TensorRT/FP32-FP16 support and Warp optimizations in NVIDIA support/benchmarking documentation.

### RFdiffusion NIM single-GPU backbone generation throughput

- Dataset/split: RFdiffusion NIM benchmarking (2.x release benchmarking page) / not reported
- Metric/value: amino acids per second per step / 799.6 amino acids per second per step (`higher-is-better`)
- Model scope: RFdiffusion NIM 2.3.0 on L40S (measured on NIM packaging)
- Conditions: NIM serving-runtime measurement; optimizations using NVIDIA Warp and TensorRT reported; measured per NIM benchmarking page (single-GPU measurement).
- Source: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Locator: benchmarking page
- Caveat: Measurement reported by NVIDIA NIM benchmarking for the NIM packaging (serving-runtime measurement).
- Caveat: Reported conditions reference TensorRT/FP32-FP16 support and Warp optimizations in NVIDIA support/benchmarking documentation.

### RFdiffusion NIM single-GPU backbone generation throughput

- Dataset/split: RFdiffusion NIM benchmarking (2.x release benchmarking page) / not reported
- Metric/value: amino acids per second per step / 673.4 amino acids per second per step (`higher-is-better`)
- Model scope: RFdiffusion NIM 2.3.0 on A100 (measured on NIM packaging)
- Conditions: NIM serving-runtime measurement; optimizations using NVIDIA Warp and TensorRT reported; measured per NIM benchmarking page (single-GPU measurement).
- Source: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Locator: benchmarking page
- Caveat: Measurement reported by NVIDIA NIM benchmarking for the NIM packaging (serving-runtime measurement).
- Caveat: Reported conditions reference TensorRT/FP32-FP16 support and Warp optimizations in NVIDIA support/benchmarking documentation.

### RFdiffusion NIM single-GPU backbone generation throughput

- Dataset/split: RFdiffusion NIM benchmarking (2.x release benchmarking page) / not reported
- Metric/value: amino acids per second per step / 475.9 amino acids per second per step (`higher-is-better`)
- Model scope: RFdiffusion NIM 2.3.0 on A10G-20GB (measured on NIM packaging)
- Conditions: NIM serving-runtime measurement; optimizations using NVIDIA Warp and TensorRT reported; measured per NIM benchmarking page (single-GPU measurement).
- Source: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Locator: benchmarking page
- Caveat: Measurement reported by NVIDIA NIM benchmarking for the NIM packaging (serving-runtime measurement).
- Caveat: Reported conditions reference TensorRT/FP32-FP16 support and Warp optimizations in NVIDIA support/benchmarking documentation.

### RFdiffusion NIM single-GPU backbone generation throughput

- Dataset/split: RFdiffusion NIM benchmarking (2.x release benchmarking page) / not reported
- Metric/value: amino acids per second per step / 448.4 amino acids per second per step (`higher-is-better`)
- Model scope: RFdiffusion NIM 2.3.0 on A10G-24GB (measured on NIM packaging)
- Conditions: NIM serving-runtime measurement; optimizations using NVIDIA Warp and TensorRT reported; measured per NIM benchmarking page (single-GPU measurement).
- Source: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Locator: benchmarking page
- Caveat: Measurement reported by NVIDIA NIM benchmarking for the NIM packaging (serving-runtime measurement).
- Caveat: Reported conditions reference TensorRT/FP32-FP16 support and Warp optimizations in NVIDIA support/benchmarking documentation.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The NVIDIA NIM packaging contains an upstream RFdiffusion implementation developed by a third party; NVIDIA materials state the model is not owned or developed by NVIDIA. Sources: https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://docs.api.nvidia.com/nim/reference/ipd-rfdiffusion
- Exact upstream checkpoint identifier (immutable artifact name, commit hash, or revision) and parameter count used by the NVIDIA NIM 2.3.0 packaging are not disclosed in the checked primary sources. Sources: https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://github.com/RosettaCommons/RFdiffusion
- Service/runtime support matrix documents tested GPU configurations and indicates FP32/FP16 and TensorRT optimization support; the packaging documents GPU memory and prerequisites but does not document multinode deployment for RFdiffusion in the checked support-matrix. Sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/2.2.0/support-matrix.html, https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/prerequisites.html
- Direct, primary-source protocol-matched comparisons between RFdiffusion NIM (this NIM packaging) and other Forge peers (e.g., ProteinMPNN Suite, AntiFold) for the same task/protocol/metric are not present in the checked primary sources. Sources: https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://github.com/RosettaCommons/RFdiffusion

### Safety

- Explicit healthcare/clinical safety guidance is not documented in the checked primary NVIDIA packaging materials; the model is presented as a design tool for protein structures rather than clinical-grade software. Sources: https://build.nvidia.com/ipd/rfdiffusion/modelcard
- Dual-use and data-handling specifics are not detailed in the checked NVIDIA model packaging materials; users should consult licensing and governance documents prior to commercial or regulated deployments. Sources: https://build.nvidia.com/ipd/rfdiffusion/modelcard, https://docs.api.nvidia.com/nim/reference/ipd-rfdiffusion

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's RFdiffusion skill documents de novo, motif-scaffolding, and binder-design modes; contigs and hotspots; PDB artifacts; ProteinMPNN handoff; validation; and hosted/local operation. Use Forge's live route and deployed NIM version for the actual call.
- [rfdiffusion-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/rfdiffusion-nim)

## Primary sources

### RFdiffusion model card

- URL: https://build.nvidia.com/ipd/rfdiffusion/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card for the NIM packaging; authoritative for licensing, intended uses, and NVIDIA statements about ownership and governance.
- Scope: RFdiffusion NIM packaging (nim-2-3-0-regional-mirror-onboarding)
- Supports: licensing
- Supports: ownership statements
- Supports: high-level use cases

### NIM reference (service/API reference) for RFdiffusion

- URL: https://docs.api.nvidia.com/nim/reference/ipd-rfdiffusion
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Authoritative API/reference documentation for the NIM packaging and its governance terms in the docs.api namespace.
- Scope: RFdiffusion NIM packaging (API/reference)
- Supports: API reference
- Supports: ownership and governance statements

### NGC container listing for RFdiffusion (catalog)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/ipd/containers/rfdiffusion/-
- Publisher: NVIDIA (NGC)
- Type: `official-documentation`
- Primary because: NGC container listing accompanying the NIM packaging; authoritative for container release metadata and availability.
- Scope: RFdiffusion NIM packaging and container release metadata
- Supports: release date
- Supports: packaging contents
- Supports: deployment geography

### RFdiffusion NIM overview (NIM docs)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM documentation overview describing model purpose, inputs/outputs at a high level.
- Scope: NIM documentation overview
- Supports: high-level I/O semantics
- Supports: model description

### RFdiffusion NIM endpoints (1.0.0) - NVIDIA documentation

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/endpoints.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Endpoint reference documenting input and output fields (input_pdb, contigs, diffusion_steps, output_pdb, elapsed_ms, hotspot_res).
- Scope: NIM endpoints reference (1.0.0)
- Supports: input fields
- Supports: output fields
- Supports: parameter validation constraints

### RFdiffusion NIM quickstart guide (NIM docs)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/quickstart-guide.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Quickstart and prerequisites guidance for deploying the NIM.
- Scope: NIM quickstart
- Supports: prerequisite software
- Supports: NGC API key usage

### RFdiffusion NIM prerequisites (latest)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/prerequisites.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Detailed hardware requirements and supported GPU configurations as published by NIM docs.
- Scope: NIM prerequisites
- Supports: hardware requirements
- Supports: NGC access requirements

### RFdiffusion upstream repository — RosettaCommons

- URL: https://github.com/RosettaCommons/RFdiffusion
- Publisher: RosettaCommons
- Type: `repository`
- Primary because: Canonical upstream implementation repository documenting algorithm, capabilities, and README notes about inference parameters.
- Scope: Upstream RFdiffusion codebase
- Supports: architecture
- Supports: capabilities
- Supports: license (BSD)

### RFdiffusion upstream README (canonical)

- URL: https://github.com/RosettaCommons/RFdiffusion/blob/main/README.md
- Publisher: RosettaCommons
- Type: `repository`
- Primary because: README describing upstream architecture and use cases.
- Scope: Upstream RFdiffusion README
- Supports: architecture
- Supports: capabilities

### RFdiffusion upstream LICENSE (BSD)

- URL: https://github.com/RosettaCommons/RFdiffusion/blob/main/LICENSE
- Publisher: RosettaCommons
- Type: `repository`
- Primary because: Upstream license file establishing BSD licensing for the upstream code/weights.
- Scope: Upstream RFdiffusion licensing
- Supports: BSD license

### RFdiffusion NIM benchmarking (latest)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/benchmarking.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA benchmarking page reporting per-step throughput numbers and reported RMSEs across GPUs.
- Scope: NIM benchmarking (serving-runtime)
- Supports: amino acids per second per step values on listed GPUs
- Supports: reported RMSE between atoms across GPU architectures

### RFdiffusion NIM support-matrix (2.2.0)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/2.2.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Support-matrix documenting tested GPU configurations, memory requirements, and optimization support.
- Scope: NIM support-matrix (2.2.0)
- Supports: GPU memory requirements
- Supports: tested GPUs and TensorRT/precision support
- Supports: pre-compiled TensorRT engines included for many GPUs

### RFdiffusion NIM release notes (2.3.0)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes documenting new platform support (GB200) and tooling changes for 2.3.0.
- Scope: NIM release notes 2.3.0
- Supports: GB200 support
- Supports: NIMTools update
- Supports: telemetry control

### RFdiffusion NIM prerequisites (1.0.0)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/1.0.0/prerequisites.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NIM prerequisites documenting single-GPU expectation and minimum GPU memory.
- Scope: NIM prerequisites (1.0.0)
- Supports: single-GPU configuration
- Supports: minimum GPU memory and software prerequisites

### RFdiffusion NIM advanced usage (latest)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/latest/advanced-usage.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Advanced usage documentation (logging and environment variables).
- Scope: NIM advanced usage
- Supports: logging configuration via NIM_LOG_LEVEL

### RFdiffusion NIM advanced usage (2.0.0)

- URL: https://docs.nvidia.com/nim/bionemo/rfdiffusion/2.0.0/advanced-usage.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Historical advanced-usage doc supporting logging configuration.
- Scope: NIM advanced usage (2.0.0)
- Supports: logging configuration via NIM_LOG_LEVEL

### Blueprint / RFdiffusion usage note (build.nvidia.com blueprint card)

- URL: https://build.nvidia.com/nvidia/protein-binder-design-for-drug-discovery/blueprintcard
- Publisher: NVIDIA (build.nvidia.com)
- Type: `official-documentation`
- Primary because: Blueprint card describing combined usage of RFdiffusion with other NIMs (e.g., ProteinMPNN) in a design workflow.
- Scope: Blueprint usage for binder-design workflows
- Supports: integrated workflow examples
- Supports: combination of RFdiffusion and ProteinMPNN in workflows

### RFdiffusion Nature paper (version of record)

- URL: https://www.nature.com/articles/s41586-023-06415-8
- Publisher: Nature
- Type: `paper`
- Primary because: Canonical upstream publication describing the RFdiffusion algorithm and capabilities.
- Scope: Upstream RFdiffusion algorithm and evaluation
- Supports: architecture description
- Supports: task capabilities (backbone generation, binder design, motif scaffolding)

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/ipd/rfdiffusion
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: ipd-rfdiffusion
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Exact upstream immutable checkpoint identifier (commit hash, curated artifact name as an immutable release, or exact model artifact reference) used inside NVIDIA NIM nim-2-3-0-regional-mirror-onboarding is not disclosed in the checked primary sources (NVIDIA model card, NIM docs, NGC listing) — checkpoint provenance is therefore unknown.
- Exact parameter count / model scale for the packaged RFdiffusion weights in the NIM 2.3.0 distribution is not reported in the checked primary sources.
- Precise contigs DSL grammar and indexing conventions (for example, explicit chain-id syntax, whether indices are 1-based inclusive/exclusive, and exact allowable token forms) are not published in the checked NVIDIA endpoint documentation.
- Whether the NIM-packaged RFdiffusion output_pdb contains reconstructed sidechains, or only backbone coordinates, is not specified in the checked primary sources and thus is an evidence gap for output content semantics.
- Canonical, NIM-specific post-inference validation pipelines (exact recommended use of specific structure-prediction tools, recommended thresholds, or a validated pipeline for NIM outputs) are not documented in the checked primary sources; recommended downstream validation practices are therefore evidence gaps for this packaging.
- Primary-source, protocol-matched comparisons between RFdiffusion NIM (this packaging) and the Forge peers (ProteinMPNN Suite, AntiFold) for the same tasks/protocols/metrics are not present in the checked primary sources; this comparison is an evidence gap.
- Any alternate benchmark rows, additional datasets/splits, or per-split accuracy/quality metrics beyond the reported per-step throughput numbers are not present in the checked primary sources and are therefore an evidence gap.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 17 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12820799 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://support.levitate.bio/api/api-rfdiffusion Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://salt.ai/nodes/md/biotech/protein-generation/saasrfdiffusioncontigmapconfignode Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://support.levitate.bio/api/api-rfdiffusion Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://zitniklab.hms.harvard.edu/ToolUniverse/tools/nvidia_nim_tools.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://salt.ai/nodes/md/biotech/protein-generation/saasrfdiffusioncontigmapconfignode Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC12820799 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/dauparas/ProteinMPNN Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/oxpig/AntiFold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/rfdiffusion/2.2.0/support-matrix.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretation_addendum: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` discarded:$.sources[10]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.sources[17]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://build.nvidia.com/ipd/rfdiffusion: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
