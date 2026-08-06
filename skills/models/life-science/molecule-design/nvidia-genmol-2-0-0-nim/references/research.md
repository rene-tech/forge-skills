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

- Research key: `docs-nvidia-com-nim-bionemo-genmol-latest-908910ca42`
- Independent audit: `revised`
- Researched: `2026-07-23T22:05:23.382222+00:00`

NVIDIA GenMol 2.0.0 NIM is a serving package that, according to official NVIDIA release notes and NGC catalog documentation, serves GenMol v2.0 using the NV-GenMol-89M-v2 checkpoint. Primary NVIDIA sources consistently describe the upstream checkpoint as an 89M-parameter Transformer with a BERT network architecture and masked-diffusion generation over SAFE molecular representations. Directly supported uses in primary sources are de novo generation, linker design, motif extension, scaffold decoration or morphing, hit generation, and lead optimization. Official endpoint documentation provides parameter bounds for temperature, noise, gamma, min_add_len, scoring, and a deprecated step_size field. Important evidence limits remain: the findings do not provide an immutable checkpoint revision, a full official output JSON field schema, explicit score calibration semantics, or checkpoint-specific clinical validation. Benchmark evidence is split between NIM runtime benchmark pages and upstream repository results, and some benchmark protocols are not fully specified in the findings.

## Identity

- Upstream name: GenMol v2.0 (NV-GenMol-89M-v2)
- Checkpoint/version: NV-GenMol-89M-v2
- Immutable revision: not reported
- Parameter scale: 89 million parameters
- Architecture/head: Transformer with a BERT network architecture; masked diffusion model trained on Sequential Attachment-based Fragment Embedding (SAFE) representations.
- License: Model weights: NVIDIA Open Model License; source code: Apache 2.0; NIM service/container: NVIDIA Software License Agreement and Product-Specific Terms for NVIDIA AI Products.
- Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html, https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md, https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol

## Selection

### Recommended

- **De novo molecule generation** — Primary NVIDIA model-card and container sources explicitly list de novo generation as a supported GenMol use.
  Scope: NVIDIA GenMol 2.0.0 NIM serving GenMol v2.0 (NV-GenMol-89M-v2)
  Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol
- **Linker design** — Primary NVIDIA sources explicitly list linker design as a GenMol capability; repository benchmark findings also report a linker-design (1-step) result for GenMol V2.
  Scope: NVIDIA GenMol 2.0.0 NIM serving GenMol v2.0 (NV-GenMol-89M-v2)
  Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://github.com/NVIDIA-BioNeMo/genmol
- **Motif extension and scaffold decoration or morphing** — Primary NVIDIA sources list motif extension and scaffold decoration or morphing as intended GenMol uses, and NVIDIA benchmark pages report task-specific validity, uniqueness, diversity, novelty, quality, and wall-time figures for these tasks.
  Scope: NVIDIA GenMol 2.0.0 NIM serving GenMol v2.0 (NV-GenMol-89M-v2)
  Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- **Hit generation and lead optimization in research or discovery workflows** — Primary NVIDIA sources explicitly list hit generation and lead optimization among GenMol use cases.
  Scope: NVIDIA GenMol 2.0.0 NIM serving GenMol v2.0 (NV-GenMol-89M-v2)
  Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol

### Conditional

- **Use with masked fragment templates for fragment-guided molecular generation** — Use only when inputs can be expressed as SAFE-formatted text sequences with masked fragments denoted by asterisk symbols; the overview describes masking-unmasking inference over masked positions.
  Scope: NVIDIA GenMol 2.0.0 NIM serving GenMol v2.0 (NV-GenMol-89M-v2)
  Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- **Score-ranked generation using QED or LogP** — Applicable only within the officially documented endpoint scoring enum values QED or LogP; the findings do not specify broader score semantics or calibration, so downstream validation is required.
  Scope: NVIDIA GenMol 2.0.0 NIM endpoint parameters
  Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- **Commercial deployment** — Primary checkpoint sources say GenMol v2.0 is ready for commercial use, but deployment remains subject to the NVIDIA Open Model License for weights plus NVIDIA NIM service terms and any downstream validation requirements.
  Scope: GenMol v2.0 checkpoint and NVIDIA GenMol NIM packaging
  Evidence: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol

### Avoid

- **Clinical decision making or regulated clinical diagnostics** — Primary findings describe molecular-generation and discovery uses, but the findings do not report clinical validation, regulatory approval, or clinical-grade evaluation for this checkpoint or NIM service.
  Scope: NVIDIA GenMol 2.0.0 NIM / GenMol v2.0 (NV-GenMol-89M-v2)
  Evidence: documented evidence gap
- **Inputs highly divergent from the ZINC-15 dataset** — The repository model card states a technical limitation that the model may not perform well on sequences highly divergent from the ZINC-15 dataset.
  Scope: GenMol v2.0 (NV-GenMol-89M-v2) upstream checkpoint evidence
  Evidence: https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md

## Input preparation

### Semantic inputs

- The model consumes molecular sequences represented as SAFE-formatted text strings. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- The endpoint also accepts numeric and control inputs for molecules to generate, temperature scaling factor, noise scaling factor, scoring method, and whether to show unique molecules only. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-genmol, https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- For masked-fragment workflows, SAFE sequences may contain masked fragments denoted by asterisk symbols. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html

### Accepted formats

- The molecular sequence input format is a SAFE-formatted text string. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- Input types officially reported are Text (Molecular Sequence), Number, Enumeration, and Binary. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol

### Preprocessing

- Inference uses a masking-unmasking process inspired by masked discrete diffusion, predicting tokens at masked positions and iteratively recovering all masks. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html
- Evidence gap: the findings do not specify canonical tokenization, SAFE normalization, fragment ordering, stereochemistry handling, or other preprocessing details beyond SAFE-formatted molecular-sequence inputs.

### Pre-submit validation

- Maximum input length is 512 tokens. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- The temperature parameter must be a float from 0.01 to 10.0. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- The noise parameter must be a float from 0.0 to 2.0, default 1.0. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- The gamma parameter must be a float from 0.0 to 1.0, default 0.0. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- The min_add_len parameter must be an integer from 1 to 128, default 24. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- The scoring parameter is restricted to the enum values QED or LogP, default QED. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- The step_size parameter is deprecated in v2.0.0 and ignored by the service. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html

### Task-specific formatting

- For fragment-guided generation, use SAFE-formatted text with masked fragments denoted by asterisk symbols. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html
- The official endpoint exposes temperature, noise, gamma, min_add_len, scoring, and deprecated step_size controls for generation behavior. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html

## Output interpretation

### Outputs

- Officially reported output types are Text (list of molecule sequences) and Number (list of scores). Sources: https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- The output sequence format is an array of SAFE strings, and scores are an array of FP32 numbers. Sources: https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- Maximum output length is 512 tokens. Sources: https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol

### Interpretation

- Interpret generated text outputs as candidate molecular sequences in SAFE format, not as validated molecules for a specific end use without downstream checks. Sources: https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- Interpret scores conservatively: the endpoint documents a scoring selector of QED or LogP, but the findings do not specify score calibration, uncertainty, or broader semantics beyond reporting an array of FP32 scores. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html, https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol

### Post-inference validation

- Potential known risk: the model may produce molecules that are difficult or impossible to synthesize, so downstream synthesis or feasibility review is required. Sources: https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md
- Evidence gap: the findings do not provide an official full output JSON object schema, named response fields, or a checkpoint-specific post-inference validation workflow beyond reported output types and score arrays.

## Public benchmarks

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: wall-time on H100 GPU / 1.051 s for v2 versus 1.824 s for v1; 42.4% reduction (`lower-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1; serving/runtime benchmark, not a pure upstream checkpoint-only benchmark
- Conditions: Measured on an H100 GPU; the findings do not specify dataset, split, or full generation hyperparameters at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, motif-extension wall-time row
- Caveat: This is a runtime/task benchmark from the NIM documentation rather than a checkpoint-only evaluation.
- Caveat: Dataset, split, and full protocol are not reported in the findings.

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: validity / 0.889 for v2 versus 0.915 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, motif-extension validity row
- Caveat: Protocol details are incomplete in the findings.
- Caveat: Comparability to external benchmarks is limited by missing dataset and split metadata.

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: uniqueness / 0.670 for v2 versus 0.671 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, motif-extension uniqueness row
- Caveat: Protocol details are incomplete in the findings.

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: diversity / 0.674 for v2 versus 0.604 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, motif-extension diversity row
- Caveat: Protocol details are incomplete in the findings.

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: novelty / 0.691 for v2 versus 0.684 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, motif-extension novelty row
- Caveat: Protocol details are incomplete in the findings.

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: quality / 0.188 for v2 versus 0.273 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings note that motif-extension quality is sensitive to hyperparameter selection including temperature, noise, and mask-length.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, motif-extension quality row and quality note
- Caveat: Quality is explicitly reported as hyperparameter-sensitive.
- Caveat: Dataset and split are not reported in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: wall-time on H100 GPU / 0.961 s for v2 versus 0.972 s for v1; 1.1% reduction (`lower-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1; serving/runtime benchmark
- Conditions: Measured on an H100 GPU; the findings do not specify dataset, split, or full generation hyperparameters at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, scaffold-decoration wall-time row
- Caveat: This is a runtime/task benchmark from the NIM documentation.
- Caveat: Dataset, split, and full protocol are not reported in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: validity / 0.995 for v2 versus 0.967 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, scaffold-decoration validity row
- Caveat: Protocol details are incomplete in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: uniqueness / 0.756 for v2 versus 0.763 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, scaffold-decoration uniqueness row
- Caveat: Protocol details are incomplete in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: diversity / 0.564 for v2 versus 0.555 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, scaffold-decoration diversity row
- Caveat: Protocol details are incomplete in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: novelty / 0.624 for v2 versus 0.655 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, scaffold-decoration novelty row
- Caveat: Protocol details are incomplete in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: quality / 0.354 for v2 versus 0.346 for v1 (`higher-is-better`)
- Model scope: NVIDIA GenMol NIM benchmark page comparing v2 to v1
- Conditions: The findings do not specify dataset, split, or exact generation protocol at this locator.
- Source: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Locator: benchmarks page, scaffold-decoration quality row
- Caveat: Protocol details are incomplete in the findings.

### Motif extension

- Dataset/split: not reported / not reported
- Metric/value: validity, uniqueness, quality, diversity, distance / validity 99.4%; uniqueness 84.5%; quality 49.0%; diversity 0.626; distance 0.659 (`context-only`)
- Model scope: GenMol V2 upstream repository benchmark result
- Conditions: The findings provide values from the NVIDIA-BioNeMo repository root but do not specify the exact benchmark page locator, dataset, split, or full protocol in the provided evidence.
- Source: https://github.com/NVIDIA-BioNeMo/genmol
- Locator: repository root benchmark summary as captured in findings
- Caveat: Not directly comparable to the NIM benchmark page values because the reported metric sets and protocols differ.
- Caveat: Dataset and split are not reported in the findings.

### Scaffold decoration

- Dataset/split: not reported / not reported
- Metric/value: validity, uniqueness, quality, diversity, distance / validity 99.2%; uniqueness 90.5%; quality 39.7%; diversity 0.571; distance 0.604 (`context-only`)
- Model scope: GenMol V2 upstream repository benchmark result
- Conditions: The findings provide values from the NVIDIA-BioNeMo repository root but do not specify the exact benchmark page locator, dataset, split, or full protocol in the provided evidence.
- Source: https://github.com/NVIDIA-BioNeMo/genmol
- Locator: repository root benchmark summary as captured in findings
- Caveat: Not directly comparable to the NIM benchmark page values because the reported metric sets and protocols differ.
- Caveat: Dataset and split are not reported in the findings.

### Superstructure generation

- Dataset/split: not reported / not reported
- Metric/value: validity, uniqueness, quality, diversity, distance / validity 99.7%; uniqueness 89.8%; quality 39.0%; diversity 0.551; distance 0.769 (`context-only`)
- Model scope: GenMol V2 upstream repository benchmark result
- Conditions: The findings provide values from the NVIDIA-BioNeMo repository root but do not specify the exact benchmark page locator, dataset, split, or full protocol in the provided evidence.
- Source: https://github.com/NVIDIA-BioNeMo/genmol
- Locator: repository root benchmark summary as captured in findings
- Caveat: Dataset and split are not reported in the findings.

### Linker design (1-step)

- Dataset/split: not reported / not reported
- Metric/value: validity, uniqueness, quality, diversity, distance / validity 81.8%; uniqueness 87.1%; quality 28.6%; diversity 0.566; distance 0.545 (`context-only`)
- Model scope: GenMol V2 upstream repository benchmark result
- Conditions: The findings provide values from the NVIDIA-BioNeMo repository root but do not specify the exact benchmark page locator, dataset, split, or full protocol in the provided evidence.
- Source: https://github.com/NVIDIA-BioNeMo/genmol
- Locator: repository root benchmark summary as captured in findings
- Caveat: Dataset and split are not reported in the findings.

## Comparisons

### GenMol v1 — `tradeoff`

- Task: Motif extension and scaffold decoration under the official NIM benchmark page
- Criteria: v2 shows lower motif-extension wall-time and higher motif-extension diversity and novelty, but lower motif-extension validity and quality; for scaffold decoration, v2 improves validity, diversity, quality, and wall-time while reducing uniqueness and novelty.
- Rationale: Official NIM benchmarks report mixed changes from v1 to v2 rather than a uniform win. Motif-extension quality is also noted as sensitive to hyperparameter selection.
- Comparison conditions: Comparison is limited to the official NIM benchmark page values; dataset, split, and full protocol are not reported in the findings, and motif-extension quality is explicitly hyperparameter-sensitive.
- Evidence: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html

## Limitations and safety

### Limitations

- Maximum input length is 512 tokens. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://huggingface.co/nvidia/NV-GenMol-89M-v2, https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- Technical limitation: the model may not perform well on sequences highly divergent from the ZINC-15 dataset. Sources: https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md
- Potential known risk: the model may produce molecules that are difficult or impossible to synthesize. Sources: https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md
- The step_size parameter is deprecated in v2.0.0 and ignored by the service. Sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Evidence gap: the findings do not report an immutable checkpoint revision for NV-GenMol-89M-v2.
- Evidence gap: the findings do not provide a full official output JSON schema or explicit score calibration semantics for the service outputs.

### Safety

- Model use is governed by the NVIDIA Open Model License for weights, Apache 2.0 for source code, and NVIDIA Software License Agreement plus Product-Specific Terms for NVIDIA AI Products for the NIM service/container; deployments must comply with all applicable terms. Sources: https://build.nvidia.com/nvidia/genmol-generate/modelcard, https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol, https://huggingface.co/nvidia/NV-GenMol-89M-v2
- Generated molecules should receive downstream feasibility review because primary sources note the model may produce molecules that are difficult or impossible to synthesize. Sources: https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md
- Forge policy: Do not use this model as a substitute for clinical validation, regulated diagnostics, or treatment decision making without appropriate domain-specific review and validation.

## Related upstream agent skills

### `related-version-workflow`

The BioNeMo GenMol skill currently demonstrates a different named NIM tag than Forge's GenMol 2.0.0 entry. Use it for scientific workflow concepts and SAFE preparation only after reconciling every field, response, and deployment flag against the Forge 2.0.0 route; do not transfer version-specific behavior or benchmark claims.
- [genmol-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/genmol-nim)

### `related-multi-model-pipeline`

The NVIDIA BioNeMo drug-discovery meta-skill composes GenMol, DiffDock, and Boltz2. Use it as a workflow template only after independently selecting exact Forge versions, reconciling SAFE/SMILES and structure artifacts at every boundary, and validating each intermediate result; it is not a head-to-head quality benchmark.
- [drug-discovery-pipeline](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/meta-skills/drug-discovery-pipeline)

### `related-cheminformatics-validation`

NVIDIA BioNeMo's nvMolKit skill is related GPU-batched cheminformatics guidance for fingerprints, similarity, conformers, force-field optimization, clustering, and substructure checks. Use it for large-batch ligand or generated-molecule validation when installed; it does not establish any model's request schema, quality, or Forge runtime behavior, and plain RDKit is generally more appropriate for one-off molecules.
- [nvmolkit-usage](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/library-skills/nvMolKit)

## Primary sources

### Exact official starting source declared by Forge

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA documentation root for the exact GenMol NIM source scope under audit.
- Scope: NVIDIA GenMol NIM documentation root
- Supports: official starting source requirement
- Supports: source scope for the exact Forge model entry

### GenMol NIM release notes

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA release notes for the GenMol NIM service version and integrated checkpoint.
- Scope: NVIDIA GenMol NIM 2.0.0 serving GenMol v2.0
- Supports: NIM version identity
- Supports: integration of NV-GenMol-89M-v2 checkpoint
- Supports: validated GPU matrix

### GenMol NIM endpoints documentation

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/endpoints.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA endpoint documentation for accepted parameters, bounds, defaults, and deprecated fields.
- Scope: NVIDIA GenMol NIM endpoint parameter interface
- Supports: temperature/noise/gamma/min_add_len bounds
- Supports: scoring enum values
- Supports: deprecated step_size behavior

### GenMol NIM benchmarks

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/benchmarks.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA benchmark page for GenMol NIM runtime and task-level benchmark claims.
- Scope: NVIDIA GenMol NIM benchmark comparisons between v1 and v2
- Supports: motif-extension metrics
- Supports: scaffold-decoration metrics
- Supports: wall-time claims
- Supports: hyperparameter-sensitivity note

### GenMol model card (NVIDIA Build)

- URL: https://build.nvidia.com/nvidia/genmol-generate/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA-hosted model card for GenMol v2.0 with architecture, scale, input types, intended uses, and license statement.
- Scope: GenMol v2.0 (NV-GenMol-89M-v2) upstream checkpoint evidence
- Supports: checkpoint identity
- Supports: architecture
- Supports: parameter count
- Supports: SAFE input format
- Supports: intended use cases
- Supports: maximum input length
- Supports: weight license

### GenMol project MODEL_CARD.md

- URL: https://github.com/NVIDIA-BioNeMo/genmol/blob/main/MODEL_CARD.md
- Publisher: NVIDIA-BioNeMo
- Type: `repository`
- Primary because: Official NVIDIA-BioNeMo repository model card for upstream checkpoint characteristics, source-code license, and documented limitations or risks.
- Scope: GenMol v2.0 (NV-GenMol-89M-v2) upstream checkpoint evidence
- Supports: checkpoint identity
- Supports: source-code license
- Supports: commercial-use statement
- Supports: technical limitation on ZINC-15 divergence
- Supports: synthesis risk

### NGC Catalog: GenMol container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC container entry describing the GenMol NIM container, included checkpoint, and service license terms.
- Scope: NVIDIA GenMol NIM container packaging
- Supports: NIM serves GenMol v2.0 (NV-GenMol-89M-v2)
- Supports: container includes model weights and runtime components
- Supports: NIM service license terms
- Supports: supported use-case summary

### NV-GenMol-89M-v2 model page

- URL: https://huggingface.co/nvidia/NV-GenMol-89M-v2
- Publisher: NVIDIA
- Type: `repository`
- Primary because: Official NVIDIA-hosted checkpoint page reporting architecture, parameter count, I/O types, formats, limits, and licensing.
- Scope: GenMol v2.0 (NV-GenMol-89M-v2) upstream checkpoint evidence
- Supports: architecture
- Supports: parameter count
- Supports: input types
- Supports: output types
- Supports: SAFE array outputs
- Supports: maximum input and output lengths
- Supports: license statements

### NIM reference: NVIDIA GenMol

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-genmol
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA API reference for model identity and I/O contract as exposed by the NIM interface.
- Scope: NVIDIA GenMol NIM API interface
- Supports: architecture
- Supports: parameter count
- Supports: input types
- Supports: SAFE input format
- Supports: maximum input length
- Supports: output types and formats
- Supports: maximum output length

### BioNeMo framework model benchmarks definitions

- URL: https://docs.nvidia.com/bionemo-framework/1.10/models/model-benchmarks.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA benchmark-definition documentation used to interpret validity, uniqueness, and novelty metric meanings where explicitly defined in findings.
- Scope: Metric-definition context for molecular generation benchmarks
- Supports: validity definition
- Supports: uniqueness definition
- Supports: novelty definition
- Supports: benchmark-protocol context

### GenMol NIM overview

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA overview page describing the masking-unmasking inference process and masked SAFE input representation.
- Scope: NVIDIA GenMol NIM inference overview
- Supports: masking-unmasking inference process
- Supports: SAFE masked-fragment formatting

### GenMol project repository

- URL: https://github.com/NVIDIA-BioNeMo/genmol
- Publisher: NVIDIA-BioNeMo
- Type: `repository`
- Primary because: Official NVIDIA-BioNeMo repository root containing benchmark summary values for GenMol V2 tasks in the findings.
- Scope: GenMol V2 upstream repository benchmark summary
- Supports: motif-extension benchmark summary
- Supports: scaffold-decoration benchmark summary
- Supports: superstructure-generation benchmark summary
- Supports: linker-design benchmark summary

### Exact official starting source declared by Forge

- URL: https://docs.nvidia.com/nim/bionemo/genmol/latest
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-genmol
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- The findings do not report an immutable checkpoint revision for NV-GenMol-89M-v2.
- The findings do not provide a full official output JSON schema with named response fields for NVIDIA GenMol 2.0.0 NIM.
- The findings do not specify score calibration, uncertainty, or broader semantics beyond reporting arrays of FP32 scores and a scoring selector of QED or LogP.
- The findings do not report checkpoint-scoped clinical validation, regulatory approval, or clinical-grade evaluation.
- Several benchmark entries lack dataset names, split identifiers, and full protocol details in the provided findings, which limits direct comparability.
- Comparison evidence in the findings is limited to GenMol v2 versus GenMol v1 on the official NIM benchmark page; the findings do not provide primary protocol-matched comparisons against other Forge candidates.
- The findings do not specify canonical tokenization, SAFE normalization, fragment ordering, or stereochemistry preprocessing details beyond SAFE-formatted sequence inputs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/latest/ Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/bionemo/genmol/1.0.1/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://docs.nvidia.com/nim/bionemo/genmol/latest: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
