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

- Research key: `build-nvidia-com-mit-boltz2-596898d726`
- Independent audit: `revised`
- Researched: `2026-07-23T20:57:32.208236+00:00`

Boltz-2 NIM is NVIDIA’s packaged Boltz-2 structural-biology foundation model enabling both biomolecular structure prediction and binding-affinity prediction. The exact upstream architecture is the Boltz-2 PairFormer-based model; the NVIDIA NIM wrapper provides an affinity head and inference workflow. Primary evidence documents include the Boltz-2 model card, Boltz-2 inference docs, and the Boltz-2 upstream paper; canonical upstream sources include the Boltz-2 GitHub repository and the arXiv/bioRxiv preprints. Licensing details are distributed across the upstream MIT-licensed Boltz-2 code and the NVIDIA NIM terms. Exact upstream checkpoint identifiers, revision, and parameter-scale are not reported in the primary sources checked, leaving evidence gaps for those items.

## Identity

- Upstream name: Boltz-2
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: PairFormer trunk with a diffusion-based structure generator, a denoising network with steering, a confidence module, and a dedicated affinity module; upstream Boltz-2 architecture uses a PairFormer trunk and is explicitly described as 'PairFormer' in canonical papers and repositories
- License: Upstream Boltz-2 code licensed under MIT; NVIDIA NIM wrapper uses NVIDIA Software License Agreement and Product-Specific Terms for AI Products; model usage license for Boltz-2 NIM is NVIDIA Open Model Agreement; additional licensing information lists Apache License 2.0 and MIT License for the model code
- Evidence: https://build.nvidia.com/mit/boltz2, https://build.nvidia.com/mit/boltz2/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2, https://github.com/jwohlwend/boltz

## Selection

### Recommended

- **High-throughput binding-affinity prediction and hit-discovery workflows for small molecules and ligands** — Primary sources describe Boltz-2 as capable of both structure prediction and binding-affinity prediction with an affinity head and high-throughput screening utility; the MF-PCBA benchmark results reported in canonical sources support affinity-screening usage
  Scope: Boltz-2 upstream checkpoint with PairFormer trunk and affinity head used in NIM wrapper
  Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699

### Conditional


### Avoid

- **Clinical or patient-data-driven predictions** — No primary evidence supporting clinical applicability; licensing and safety boundaries apply per NVIDIA NIM terms and model-card scope
  Scope: Boltz-2 NIM container use cases with general bio/chem informatics workflows
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2

## Input preparation

### Semantic inputs

- Boltz-2 accepts biomolecular sequences (protein, DNA, RNA), ligand representations (SMILES or CCD strings), restraints, and JSON inputs for conditioning and constraints. Sources: https://build.nvidia.com/mit/boltz2/modelcard

### Accepted formats

- Input formats are described as a dictionary containing sequence strings, modification records, and constraint parameters. Sources: https://build.nvidia.com/mit/boltz2/modelcard

### Preprocessing

- Maximum sequence length per chain is 4096 residues; up to 12 input polymers per request; up to 20 input ligands per request. Sources: https://build.nvidia.com/mit/boltz2/modelcard

### Pre-submit validation

- Evidence gap: explicit input-validation rules (out-of-range checks, invalid token handling, and cross-checks) are not documented in primary sources. Sources: https://build.nvidia.com/mit/boltz2/modelcard

### Task-specific formatting

- Evidence gap: official prompt templates, paired-input ordering, and control fields are not documented in primary sources. Sources: https://build.nvidia.com/mit/boltz2/modelcard

## Output interpretation

### Outputs

- Official outputs include a structure prediction, affinity prediction, and confidence metrics in JSON outputs (affinity_pred_value, affinity_probability_binary, confidence_score, ptm, plddt, etc.). Sources: https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md

### Interpretation

- Higher affinity_pred_value indicates stronger predicted binding; affinity_probability_binary (0-1) indicates binder probability and is recommended for hit-discovery to distinguish binders from decoys. Sources: https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md

### Post-inference validation

- Evidence gap: no documented post-inference validation protocol beyond general model-card and docs; explicit validation steps are not enumerated in primary sources. Sources: https://build.nvidia.com/mit/boltz2/modelcard, https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md

## Public benchmarks

### Binding-affinity prediction / hit discovery (MF-PCBA)

- Dataset/split: MF-PCBA / not reported
- Metric/value: Enrichment factor (EF) at 0.5% threshold; average precision (AP); AUROC / EF=18.4; AP≈0.025; AUROC≈0.81 (`higher-is-better`)
- Model scope: Boltz-2 upstream checkpoint evaluated on MF-PCBA without downstream task-head customization; context: MF-PCBA results reported in canonical literature
- Conditions: Standard MF-PCBA evaluation as described in canonical sources; exact experimental protocol location not clearly locatable in the primary sources referenced
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699
- Locator: Evidence gap: exact table/figure/section locator not provided in the cited source
- Caveat: Dataset downsampling to 50,000 complexes per MF-PCBA assay as described in sources; potential lack of absolute comparability to other MF-PCBA studies

## Comparisons

### Chemgauss4 docking — `prefer-this`

- Task: MF-PCBA enrichment
- Criteria: Enrichment factor and downstream metrics in MF-PCBA favor Boltz-2 over Chemgauss4 under described protocol
- Rationale: Boltz-2 shows substantially higher enrichment factor and competitive AP/AUROC compared with conventional docking baselines in canonical MF-PCBA reporting
- Comparison conditions: Direct, equal-protocol MF-PCBA evaluation; exact procedural parity not verifiable from the cited sources
- Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699

## Limitations and safety

### Limitations

- Training data consists of all Protein Data Bank structures before 2021-09-30 with resolution at least 9 Å. Sources: https://arxiv.org/abs/2602.13249v1, https://build.nvidia.com/mit/boltz2/modelcard

### Safety

- Evidence gap: explicit safety guidelines or clinical-use restrictions beyond licensing terms are not described in primary sources; use is governed by NVIDIA licenses and model-card scope. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2, https://build.nvidia.com/mit/boltz2/modelcard

## Related upstream agent skills

### `exact-nim-operating-skill`

NVIDIA BioNeMo's Boltz2 NIM skill documents entity preparation, structure and affinity modes, confidence and mmCIF interpretation, exact NIM artifacts, validation, failure modes, and hosted/local operation. Use the Forge skill's live route, source image, support matrix, authentication, and Nebius deployment contract; do not transfer a different NIM tag or the BioNeMo agent-skill benchmark into model-quality claims.
- [boltz2-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/boltz2-nim)
- [cuEquivariance](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/cuEquivariance)

### `related-multi-model-pipeline`

The NVIDIA BioNeMo drug-discovery meta-skill composes GenMol, DiffDock, and Boltz2. Use it as a workflow template only after independently selecting exact Forge versions, reconciling SAFE/SMILES and structure artifacts at every boundary, and validating each intermediate result; it is not a head-to-head quality benchmark.
- [drug-discovery-pipeline](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/meta-skills/drug-discovery-pipeline)

### `related-cheminformatics-validation`

NVIDIA BioNeMo's nvMolKit skill is related GPU-batched cheminformatics guidance for fingerprints, similarity, conformers, force-field optimization, clustering, and substructure checks. Use it for large-batch ligand or generated-molecule validation when installed; it does not establish any model's request schema, quality, or Forge runtime behavior, and plain RDKit is generally more appropriate for one-off molecules.
- [nvmolkit-usage](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/nvMolKit)

### `agent-integration`

The cookbook maps these exact Forge slugs to BioNeMo-style capability names and Serverless shapes. Use it for routing and tool integration, never as model-quality evidence.
- [BioNeMo capability catalog](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/catalog.py)
- [BioNeMo named tool contracts](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/bionemo_agent/tools.py)
- [BioNeMo agent routing and safety instructions](https://github.com/nebius/serverless-ai-cookbook/blob/e5f72b6dee788f7f802a8aed6ab73d0dc4346f90/life-science/bionemo-agent/configs/config.yml)

## Primary sources

### Boltz-2 NIM model card

- URL: https://build.nvidia.com/mit/boltz2/modelcard
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA model card for Boltz-2 NIM; primary evidence for inputs/outputs/format, and licensing context
- Scope: Boltz-2 NIM wrapper documentation
- Supports: input modalities
- Supports: output modalities
- Supports: input/output formats
- Supports: runtime details

### Boltz-2 NIM build page

- URL: https://build.nvidia.com/mit/boltz2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA page introducing Boltz-2 NIM product; primary evidence for deployment, licensing context, and service scope
- Scope: Boltz-2 NIM wrapper deployment page
- Supports: deployment scope
- Supports: licensing context
- Supports: service terms

### Boltz-2 NIM container in NVIDIA NGC catalog

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NGC catalog entry for the Boltz-2 NIM container; primary evidence for container version, licensing, and operational terms
- Scope: Boltz-2 NIM container versioning and terms
- Supports: containerVersion
- Supports: license
- Supports: runtimeEnvironment

### Boltz-2 upstream repository

- URL: https://github.com/jwohlwend/boltz
- Publisher: GitHub, Inc.
- Type: `repository`
- Primary because: Canonical upstream Boltz-2 codebase; primary source for architecture, license, and core model definitions
- Scope: Boltz-2 upstream checkpoint and codebase
- Supports: architecture
- Supports: training
- Supports: license

### Boltz-2 upstream arXiv preprint

- URL: https://arxiv.org/abs/2602.13249v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing Boltz-2 architecture and capabilities; primary source for architecture (PairFormer trunk) and core design
- Scope: Boltz-2 upstream model paper
- Supports: architecture
- Supports: scale
- Supports: capabilities

### Affinity Fine-Tuning of Boltz-2 (bioRxiv preprint)

- URL: https://biorxiv.org/content/10.64898/2026.05.26.727958v1
- Publisher: bioRxiv
- Type: `paper`
- Primary because: Canonical preprint detailing affinity-fine-tuning of Boltz-2; primary source for affinity-head extension and training approach
- Scope: Affinity fine-tuning of Boltz-2
- Supports: affinityHead
- Supports: trainingApproach
- Supports: results

### Boltz-2 MF-PCBA results (PMC article)

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699
- Publisher: PubMed Central
- Type: `paper`
- Primary because: Canonical scientific report of Boltz-2 MF-PCBA benchmarking; primary source for benchmarks and performance claims
- Scope: MF-PCBA benchmarking for Boltz-2
- Supports: EF
- Supports: AP
- Supports: AUROC
- Supports: benchmarks

### Boltz-2 prediction docs (docs/prediction.md)

- URL: https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md
- Publisher: GitHub, Inc.
- Type: `repository`
- Primary because: Canonical upstream model documentation detailing outputs, formats, and interpretation rules for affinity and confidence outputs
- Scope: Boltz-2 output schema and interpretation
- Supports: outputs
- Supports: interpretation
- Supports: JSONFields

### Boltz-2 training docs (docs/training.md)

- URL: https://github.com/jwohlwend/boltz/blob/main/docs/training.md
- Publisher: GitHub, Inc.
- Type: `repository`
- Primary because: Canonical upstream training configuration details; primary for parameter counts/scale hints and training setup
- Scope: Boltz-2 training configuration
- Supports: trainingParameters
- Supports: scale

## Evidence gaps

- Evidence gap: exact upstream checkpoint identifiers (checkpoint tag, commit hash) for NVIDIA Boltz-2 NIM wrapper are not reported in primary sources.
- Evidence gap: exact revision and parameterScale for the NVIDIA NIM container are not reported in primary sources.
- Evidence gap: explicit input-validation rules and exact post-inference validation steps are not clearly documented in primary sources.
- Evidence gap: official prompt templates, paired-input ordering, and control fields are not documented upstream.
- Evidence gap: exact MF-PCBA table/figure locator for reported metrics (EF, AP, AUROC) within the canonical source could not be located from the cited sources.
- Evidence gap: CASP16 affinity track evaluation protocol and exact locator in canonical source not locatable from primary sources.
- Evidence gap: exact locator for comparison benchmarks (Chemgauss4, FEP+) within canonical sources is not locatable; cannot verify the precise protocol parity.
- Evidence gap: precise upstream checkpoint identifiers and model-scale information (parameter count) for Boltz-2 upstream checkpoint as used in the NIM wrapper are not reported in primary sources.
- Evidence gap: exact model-card/bundle scope for licensing distinctions between upstream code license, model weights license, and NIM terms requires more granular primary verification.
- Evidence gap: input dimensionality and shapes for all modalities, and detailed preprocessing steps beyond high-level statements, are not exhaustively documented in primary sources.
- Evidence gap: exact post-output validation and quality checks beyond general guidance are not documented in primary sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 32 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property avoidUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property conditionalUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property inputPreparation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property recommendedUseCases Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA: $.sources must include the original creator's primary source for this third-party model packaged by NVIDIA Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/mit/boltz2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/mit/boltz2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/mit/boltz2/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/jwohlwend/boltz Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.recommendedUseCases must contain at least one scoped item: $.recommendedUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs is empty without a section-specific evidence gap: $.inputPreparation.semanticInputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap: $.inputPreparation.acceptedFormats is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing is empty without a section-specific evidence gap: $.inputPreparation.preprocessing is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation is empty without a section-specific evidence gap: $.inputPreparation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.comparisons[0].sourceUrl: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons[0].sourceLocator: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` discarded:$.benchmarks[1]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
