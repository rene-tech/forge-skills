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

- Research key: `github-com-openmm-openmm-bf9d80932d`
- Independent audit: `revised`
- Researched: `2026-08-06T08:38:45.155254+00:00`

Primary-source inspection of the OpenMM project per the provided findings shows (1) an official GitHub release page for OpenMM 8.5.1 at https://github.com/openmm/openmm/releases/tag/8.5.1 that documents enumerated bug fixes and includes a recorded GPG key ID (B5690EEEBB952194) as reported in the findings; (2) the repository tags index at https://github.com/openmm/openmm/tags which the findings state shows tag 8.5.1 pointing to commit SHA f7fa0c2 and indicates the tag was created on Apr 3, 2026; (3) the releases index at https://github.com/openmm/openmm/releases which includes the 8.5.1 release; and (4) a Licenses.txt file in the project documentation at https://github.com/openmm/openmm/blob/master/docs-source/licenses/Licenses.txt that states the OpenMM API, Reference Platform, and CPU platform are licensed under the MIT License. The provided findings do not include (and thus do not prove) an upstream repository-tree URL for the explicit tag snapshot (a tag tree URL or explicit commit page for f7fa0c2 was not provided in the findings), do not include checkpoint-scoped numeric benchmark tables/figures for 8.5.1, do not include checkpoint-scoped authoritative documentation of RNG/determinism semantics, do not include checkpoint-scoped authoritative trajectory I/O reporter signatures or conventions, and do not include a packaging manifest/checksum or explicit asset listing tied to an unchanged upstream binary for 8.5.1 within the provided findings. Exact primary URLs inspected and relied on for these conclusions are enumerated in the dossier sources and evidenceGaps fields.

## Identity

- Upstream name: OpenMM
- Checkpoint/version: 8.5.1
- Immutable revision: f7fa0c2
- Parameter scale: not reported
- Architecture/head: Source code snapshot of the OpenMM project at the reported checkpoint; the provided findings describe a code/release snapshot but do not report a model architecture or parameter-scale (this is a software library/source snapshot rather than a parameterized ML model).
- License: Licenses.txt in the project documentation states that the OpenMM API, Reference Platform, and CPU platform are licensed under the MIT License (see the provided Licenses.txt path). The provided findings do not supply other explicit per-component license attributions beyond the Licenses.txt file excerpt.
- Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags, https://github.com/openmm/openmm/releases, https://github.com/openmm/openmm/blob/master/docs-source/licenses/Licenses.txt

## Selection

### Recommended

- **Inspect and build the OpenMM 8.5.1 source snapshot for code-level inspection, compilation, and testing.** — The project provides an official release page for 8.5.1 documenting the release contents and a tags index mapping the release to commit f7fa0c2; these primary artifacts support treating the release as a canonical source snapshot to inspect and build from.
  Scope: OpenMM tag 8.5.1 (commit f7fa0c2)
  Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

### Conditional

- **Workflows that require cross-platform reproducible RNG/determinism (use only after system- and platform-specific reproducibility testing and verification).** — Primary findings do not include a checkpoint-scoped RNG seeding/determinism contract for 8.5.1; users must derive determinism behavior from implementation and validate experimentally on their target platforms.
  Scope: OpenMM tag 8.5.1 (commit f7fa0c2)
  Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags
- **Using repository source to derive or validate application-layer file-format handling (trajectory writers/readers) and reporter class signatures.** — The provided findings do not include checkpoint-scoped authoritative reporter signatures or trajectory-format documentation for 8.5.1; derive exact signatures from implementation code in the tag snapshot (not present in provided findings) and validate with tests.
  Scope: OpenMM tag 8.5.1 (commit f7fa0c2)
  Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

### Avoid

- **Clinical decision-making or clinical-readiness deployment** — The provided primary findings do not document clinical validation, PHI-specific processing guarantees, or regulatory compliance statements tied to OpenMM 8.5.1; therefore the checkpoint cannot be relied upon as clinically validated from the inspected upstream artifacts.
  Scope: OpenMM tag 8.5.1 (commit f7fa0c2)
  Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

## Input preparation

### Semantic inputs

- Evidence gap: The provided findings do not include a checkpoint-scoped canonical per-field input schema, unit table, or standalone accepted-input-format specification for OpenMM 8.5.1. Consumers must derive accepted formats from source code or other documentation outside the supplied findings. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

### Accepted formats

- Evidence gap: The provided findings do not include a standalone, checkpoint-scoped authoritative list of accepted input file formats or byte-order conventions for OpenMM 8.5.1. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

### Preprocessing

- Evidence gap: The provided findings contain source/release artifacts but do not enumerate explicit preprocessing steps, normalization, or unit-conversion rules for accepted inputs at the 8.5.1 checkpoint; derive preprocessing from implementation code in the tag snapshot (not present in provided findings) and validate. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

### Pre-submit validation

- Evidence gap: The provided findings do not include a checkpoint-scoped list of per-field input validation checks tied to OpenMM 8.5.1; users must construct system-specific validation and tests based on the source snapshot and release materials provided. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1

### Task-specific formatting

- Evidence gap: The provided findings do not include a checkpoint-scoped application-layer API reference enumerating reporter class signatures or constructor templates for OpenMM 8.5.1; derive exact signatures from implementation code in the tag snapshot (not present in provided findings) and validate with tests. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

## Output interpretation

### Outputs

- Evidence gap: The provided findings do not include checkpoint-scoped authoritative documentation for trajectory writer/reader semantics, explicit reporter signatures, or per-file-format unit conventions for OpenMM 8.5.1; interpretation of produced trajectory files should be validated against implementation code and tests (implementation code not provided in the supplied findings). Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

### Interpretation

- Outputs produced by building and running the OpenMM 8.5.1 snapshot are implementation-defined numerical data; the provided findings do not include checkpoint-scoped guarantees for downstream application semantics and advise users to validate outputs for their use case. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1

### Post-inference validation

- Evidence gap: The provided findings do not include a checkpoint-scoped post-simulation validation checklist or authoritative post-run validation guidance tied to OpenMM 8.5.1; construct validation tests from the source snapshot and release notes as needed. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### gromacs-md-ngc-wrapper — `insufficient-evidence`

- Task: General GPU-accelerated molecular dynamics simulation
- Criteria: No checkpoint-matched primary-source numeric benchmarks for OpenMM 8.5.1 were provided in the findings; peer-side primary-source benchmarks necessary for a matched comparison were not supplied in the provided findings.
- Rationale: The provided primary OpenMM locators (release page, tags index, releases index) document the release and tag mapping but do not contain matched numerical benchmark data for 8.5.1 in the supplied findings.
- Comparison conditions: Compared on the basis of inspected OpenMM primary locators only (no peer-side checkpoint-matched primary benchmark evidence was provided in the findings).
- Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags, https://github.com/openmm/openmm/releases

### lammps-kokkos-md-wrapper — `insufficient-evidence`

- Task: General GPU-accelerated molecular dynamics simulation
- Criteria: No checkpoint-matched primary-source numeric benchmarks for OpenMM 8.5.1 were provided in the findings; peer-side primary-source benchmarks necessary for matched protocol comparisons were not present in the provided findings.
- Rationale: Provided OpenMM primary locators document code and release notes but do not include numeric benchmark tables/figures tied to 8.5.1 in the supplied findings.
- Comparison conditions: Comparison withheld due to absence of checkpoint-scoped numeric benchmarks in the provided OpenMM findings.
- Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags, https://github.com/openmm/openmm/releases

### microsoft-bioemu-v1-1 — `insufficient-evidence`

- Task: Molecular simulation workflows and emulation
- Criteria: No checkpoint-matched primary-source numeric measurements for OpenMM 8.5.1 were provided in the findings; peer-side primary benchmark data required for comparison are not supplied in the provided findings.
- Rationale: The provided OpenMM primary locators (release page, tags index, releases index) show the release and tag mapping but do not include matched benchmark data for the checkpoint in the supplied findings.
- Comparison conditions: Peer-side primary evidence was not present in the provided findings; comparisons therefore are insufficient-evidence.
- Evidence: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags, https://github.com/openmm/openmm/releases

## Limitations and safety

### Limitations

- Evidence gap: The provided primary findings do not include a packaging manifest, checksum, signed binary assets, or container/wrapper metadata proving that any external serving/wrapper variant contains an unchanged upstream OpenMM 8.5.1 binary. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/releases, https://github.com/openmm/openmm/tags
- The provided primary findings do not include checkpoint-scoped numeric performance or accuracy benchmark tables/figures explicitly tied to OpenMM 8.5.1; therefore numeric performance guidance for this exact checkpoint is not present in the supplied upstream artifacts. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags, https://github.com/openmm/openmm/releases
- Licensing evidence in the provided findings is limited to the project Licenses.txt path in the documentation which states that the OpenMM API, Reference Platform, and CPU platform are licensed under the MIT License; the provided findings do not include additional reconciliation artifacts beyond that Licenses.txt path. Sources: https://github.com/openmm/openmm/blob/master/docs-source/licenses/Licenses.txt

### Safety

- Evidence gap: The provided findings do not document clinical validation, PHI-specific processing guarantees, or regulatory compliance statements tied to OpenMM tag 8.5.1; treat outputs as research-grade and require expert review and separate validation before any clinical use. Sources: https://github.com/openmm/openmm/releases/tag/8.5.1, https://github.com/openmm/openmm/tags

## Related upstream agent skills

### `agent-integration`

The cookbook maps these exact Forge slugs to BioNeMo-style capability names and Serverless shapes. Use it for routing and tool integration, never as model-quality evidence.
- [BioNeMo capability catalog](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/catalog.py)
- [BioNeMo named tool contracts](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/tools.py)
- [BioNeMo agent routing and safety instructions](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/configs/config.yml)

## Primary sources

### OpenMM release page for 8.5.1

- URL: https://github.com/openmm/openmm/releases/tag/8.5.1
- Publisher: OpenMM Project / GitHub
- Type: `repository`
- Primary because: Official GitHub release page documenting the 8.5.1 release contents and metadata as provided in the findings.
- Scope: OpenMM release 8.5.1
- Supports: Provides the official release page for OpenMM 8.5.1 and documents enumerated bug fixes and a reported GPG key ID as stated in the provided findings.

### OpenMM Git tags index

- URL: https://github.com/openmm/openmm/tags
- Publisher: OpenMM Project / GitHub
- Type: `repository`
- Primary because: Repository tags index showing tag entries and mapping tag 8.5.1 to commit SHA f7fa0c2 as reported in the findings.
- Scope: OpenMM Git tags index (includes 8.5.1)
- Supports: Shows that tag 8.5.1 points to commit SHA f7fa0c2 and reports tag creation metadata per the provided findings.

### OpenMM releases index

- URL: https://github.com/openmm/openmm/releases
- Publisher: OpenMM Project / GitHub
- Type: `repository`
- Primary because: Canonical releases index used to verify release metadata for 8.5.1 as present in the provided findings.
- Scope: OpenMM releases index (includes 8.5.1)
- Supports: Contains the listing for the 8.5.1 release and related release metadata as reported in the provided findings.

### OpenMM Licenses.txt (documentation source path)

- URL: https://github.com/openmm/openmm/blob/master/docs-source/licenses/Licenses.txt
- Publisher: OpenMM Project / GitHub
- Type: `official-documentation`
- Primary because: Project-hosted Licenses.txt in the documentation tree cited in the provided findings and used to support license statements in this dossier.
- Scope: Project documentation Licenses.txt (documentation/master path provided in findings)
- Supports: States that portions of the project are copyrighted by Stanford University and the Authors, and states that the OpenMM API, Reference Platform, and CPU platform are licensed under the MIT License as reported in the provided findings.

### Exact official starting source declared by Forge

- URL: https://github.com/openmm/openmm
- Publisher: github.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: openmm-md
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No repository tree URL or explicit commit page URL for commit f7fa0c2 was present in the provided findings. The provided findings show tag 8.5.1 points to f7fa0c2 via the tags index and release page, but an explicit commit/sha page URL for f7fa0c2 was not supplied in the provided findings (checked: https://github.com/openmm/openmm/tags; https://github.com/openmm/openmm/releases/tag/8.5.1).
- Evidence gap: No checkpoint-scoped numeric performance or accuracy benchmark tables/figures explicitly tied to OpenMM tag 8.5.1 were present in the provided findings (checked: https://github.com/openmm/openmm/releases/tag/8.5.1; https://github.com/openmm/openmm/tags; https://github.com/openmm/openmm/releases).
- Evidence gap: No packaging manifest, checksum, signed binary assets, or container/wrapper metadata proving an unchanged upstream OpenMM 8.5.1 binary was present in the provided findings (checked: https://github.com/openmm/openmm/releases/tag/8.5.1; https://github.com/openmm/openmm/releases; https://github.com/openmm/openmm/tags).
- Evidence gap: The provided findings do not include checkpoint-scoped authoritative documentation of RNG seeding/determinism semantics for OpenMM 8.5.1 (checked: https://github.com/openmm/openmm/releases/tag/8.5.1; https://github.com/openmm/openmm/tags).
- Evidence gap: The provided findings do not include checkpoint-scoped authoritative trajectory writer/reader documentation or explicit reporter class signatures for OpenMM 8.5.1 (checked: https://github.com/openmm/openmm/releases/tag/8.5.1; https://github.com/openmm/openmm/tags).
- Evidence gap: The provided findings do not include a checkpoint-scoped per-field input schema, accepted-format listing, preprocessing rules, or post-simulation validation checklist tied to OpenMM 8.5.1 (checked: https://github.com/openmm/openmm/releases/tag/8.5.1; https://github.com/openmm/openmm/tags).
- Evidence gap: The provided findings do not include additional reconciliation artifacts beyond the documented Licenses.txt path for component-level license attribution at the checkpoint scope (checked: https://github.com/openmm/openmm/blob/master/docs-source/licenses/Licenses.txt).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 15 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://github.com/openmm/openmm Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://github.com/openmm/openmm/discussions/5194 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/7.5.0/userguide/library.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/latest/userguide/library/04_platform_specifics.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/latest/userguide/library/04_platform_specifics.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/latest/library/08_amoeba_plugin.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/7.5.0/userguide/library.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/latest/userguide/library/04_platform_specifics.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/7.5.0/userguide/library.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.openmm.org/latest/userguide/library/04_platform_specifics.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.identity.checkpointEvidenceUrls: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.identity.checkpointEvidenceNotes: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.identity.checkpointCommitId: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.identity.revisionEvidenceUrls: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.identity.revisionEvidenceNotes: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.benchmarksEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisonsEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.limitationsEvidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://github.com/openmm/openmm: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
