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

- Research key: `github-com-dauparas-proteinmpnn-9039aae134`
- Independent audit: `revised`
- Researched: `2026-07-23T23:40:23.889475+00:00`

Primary-source inspection of the official ProteinMPNN GitHub repository and canonical paper/preprint sources shows: the repository contains top-level files README.md, protein_mpnn_run.py, protein_mpnn_utils.py, LICENSE and weight directories vanilla_model_weights, soluble_model_weights, ca_model_weights with the checkpoint filenames enumerated in identity.checkpoint. The runtime script protein_mpnn_run.py sets default hyperparameters hidden_dim = 128 and num_layers = 3, exposes flags including --ca_only and --use_soluble_model, defines --model_name with default "v_48_020" and allowed values including v_48_002, v_48_010, v_48_020, v_48_030, constructs checkpoint paths by concatenating folder + model_name + ".pt", and prints CA-only related messages when applicable. The utils file protein_mpnn_utils.py implements ProteinFeatures, positional encodings and edge-embedding layers, and initializes masks and PSSM-related arrays as part of featurization. The repository LICENSE file contains the MIT license. Canonical paper/preprint sources describe ProteinMPNN model design and benchmark-level results (sequence recovery, experimental validation) but do not provide an explicit, checkpoint-matched numeric benchmark row tying the repository .pt filenames to a dataset split/metric/value in the checked locations; therefore no checkpoint-matched numeric benchmark could be verified from the inspected primary sources.

## Identity

- Upstream name: ProteinMPNN suite variants: vanilla, soluble, and CA-only (as distributed in the upstream repository)
- Checkpoint/version: vanilla_model_weights/{v_48_002.pt, v_48_010.pt, v_48_020.pt, v_48_030.pt}; soluble_model_weights/{v_48_010.pt, v_48_020.pt}; ca_model_weights/{v_48_002.pt, v_48_010.pt, v_48_020.pt}
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: hidden_dim = 128; num_layers = 3 (defaults defined in protein_mpnn_run.py)
- License: MIT (repository LICENSE file)
- Evidence: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py, https://github.com/dauparas/ProteinMPNN/blob/main/LICENSE, https://github.com/dauparas/ProteinMPNN/tree/main/vanilla_model_weights, https://github.com/dauparas/ProteinMPNN/tree/main/soluble_model_weights, https://github.com/dauparas/ProteinMPNN/tree/main/ca_model_weights, https://github.com/dauparas/ProteinMPNN/releases

## Selection

### Recommended

- **Structure-conditioned protein sequence design / inverse folding (vanilla ProteinMPNN)** — Repository contains vanilla model weight directory and end-to-end runtime and utility scripts implementing structure-conditioned sequence-design workflows; protein_mpnn_run.py and protein_mpnn_utils.py implement backbone parsing, featurization, and design/scoring paths consistent with inverse-folding usage.
  Scope: vanilla_model_weights directory files as distributed in the upstream repository (see model_name defaults and allowed values in protein_mpnn_run.py)
  Evidence: https://github.com/dauparas/ProteinMPNN/tree/main/vanilla_model_weights, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py, https://github.com/dauparas/ProteinMPNN/blob/main/README.md

### Conditional

- **Soluble-trained variant sequence design (soluble_model_weights)** — Use only when caller intends to design soluble-protein-biased sequences and performs downstream validation; CA+full-backbone interchangeability and experimental validation are caller responsibilities.
  Scope: soluble_model_weights directory files as distributed in the upstream repository
  Evidence: https://github.com/dauparas/ProteinMPNN/tree/main/soluble_model_weights, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/README.md
- **CA-only sequence design when only Cα coordinates are available** — CA-only mode is supported by the run script and utilities; callers must validate designed sequences because direct equivalence to full-backbone models is not established in the inspected repository files.
  Scope: ca_model_weights directory files as distributed in the upstream repository
  Evidence: https://github.com/dauparas/ProteinMPNN/tree/main/ca_model_weights, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py

### Avoid

- **Clinical or regulated use without expert review and experimental validation** — Evidence gap: No primary-source evidence in the inspected repository files documents clinical validation, regulated-use approval, or operationalized safety validations for any upstream weight variant.
  Scope: All upstream ProteinMPNN suite variants
  Evidence: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py

## Input preparation

### Semantic inputs

- Backbone structure files and design-assignment metadata are consumed by repository helper scripts; helper scripts support parsing PDB files, assigning which chains to design, fixing residues, adding amino‑acid bias, and tying residues. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py
- The run script exposes runtime-selection flags (for example --ca_only) to select CA-only versus full-backbone modes at inference time and to select model_name corresponding to checkpoint filenames. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py
- Evidence gap: No machine-readable JSON input schema (field names, required fields, types) was found in the inspected primary sources; callers must derive input validation from helper scripts or create an external schema. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py

### Accepted formats

- PDB-format backbone files and repository helper-script workflows are accepted by repository utilities and scripts used in preprocessing workflows. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py

### Preprocessing

- Featurization and edge-feature computations (ProteinFeatures, positional encodings, RBF-like edge features) are implemented in protein_mpnn_utils.py and used in preprocessing. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py
- When CA-only mode is active, CA-only coordinates are parsed and CA-only models are selected; otherwise full-backbone coordinates are stacked for featurization per the utilities and run script. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py

### Pre-submit validation

- The repository initializes fixed_position_mask and omit_AA_mask arrays and PSSM-related arrays in protein_mpnn_utils.py as part of input featurization and mask handling. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py
- Evidence gap: No explicit machine-readable input-schema with field types, required/optional markers, or example JSONL schema was found in the inspected primary sources. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/README.md, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py

### Task-specific formatting

- Command-line flags in protein_mpnn_run.py (for example --model_name, --path_to_model_weights, --ca_only, --use_soluble_model, --omit_AAs) control model selection, weights folder, CA-only parsing, soluble-model usage, and omitted amino acids. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/README.md

## Output interpretation

### Outputs

- The runtime script writes output lines that include native sequence, per-position score, global score, visible and designed chains, model name, git hash, and random seed. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/README.md
- Evidence gap: No canonical machine-readable JSON output schema (field names, tensor shapes, or numeric score contracts) was found in the inspected primary sources. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/README.md

### Interpretation

- Evidence gap: No formal calibrated score semantics or absolute confidence calibration for generated outputs is documented in the inspected primary sources; downstream validation is required to interpret numeric outputs. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/README.md, https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf

### Post-inference validation

- Evidence gap: The repository does not provide explicit post-inference numeric calibration rules or canonical downstream validation scripts in a machine-readable schema in the inspected primary sources; users must perform independent structural and experimental validation. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### other protein-design model checkpoints — `insufficient-evidence`

- Task: structure-conditioned sequence design (inverse folding)
- Criteria: No checkpoint-matched, protocol-aligned benchmark rows tying exact upstream .pt filenames to dataset splits, metrics, and values were found in the inspected primary sources; therefore direct task-and-protocol-aligned comparison to other checkpoints cannot be verified from primary sources.
- Rationale: Canonical publication and repository report performance metrics and available checkpoint filenames, but the inspected primary-source locations did not provide explicit rows mapping metrics to specific .pt filenames, preventing a validated comparison.
- Comparison conditions: Inspected repository README, runtime script, releases page, and canonical preprint/paper Methods and Supplementary Tables; protocols and checkpoints could not be matched deterministically between reported metrics and repository .pt filenames in the inspected locations.
- Evidence: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/releases, https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf, https://ipd.uw.edu/publication-pdfs/275/3d98c978aed6d429d315317432f674b9/science.add2187.pdf

## Limitations and safety

### Limitations

- The repository exposes runtime-selection flags (for example --ca_only and --use_soluble_model) and a --model_name default of v_48_020, but the inspected run script and helper files do not provide an explicit deterministic mapping from runtime-selection flags alone to an immutable .pt checkpoint filename across releases. Sources: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/releases, https://github.com/dauparas/ProteinMPNN
- Evidence gap: Parameter count and explicit model-size reporting are not present in the inspected primary sources; parameterScale is not reported. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py
- Evidence gap: No checkpoint-matched numeric benchmark tables tying exact .pt filenames to dataset splits and metric values were found in the inspected primary sources; numeric benchmark claims in the canonical paper/preprint are not mapped to exact repository .pt filenames in the checked locations. Sources: https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf, https://ipd.uw.edu/publication-pdfs/275/3d98c978aed6d429d315317432f674b9/science.add2187.pdf, https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/releases

### Safety

- Evidence gap: No creator-provided biosecurity safeguards, PHI handling policies, or privacy guarantees were found in the inspected primary sources; apply conservative expert oversight for sensitive or dual-use objectives. Sources: https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/README.md, https://github.com/dauparas/ProteinMPNN/blob/main/LICENSE
- Evidence gap: No primary-source evidence of clinical validation or regulated-use approval for any upstream weight variant was found in the inspected primary sources; expert review and experimental validation are required prior to consequential biological use. Sources: https://github.com/dauparas/ProteinMPNN, https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf, https://ipd.uw.edu/publication-pdfs/275/3d98c978aed6d429d315317432f674b9/science.add2187.pdf

## Related upstream agent skills

### `related-runtime-workflow`

Forge packages an upstream ProteinMPNN suite rather than the exact BioNeMo NIM contract. NVIDIA's skill remains useful for inverse-folding intent, PDB input preparation, fixed-chain/residue controls, multi-FASTA outputs, and validation, but every payload field, image, and route must be taken from the Forge wrapper.
- [proteinmpnn-nim](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/a2ed0669325a156c1a58aea8bc3eb2ec0df17f4b/nim-skills/proteinmpnn-nim)

## Primary sources

### ProteinMPNN repository

- URL: https://github.com/dauparas/ProteinMPNN
- Publisher: dauparas
- Type: `repository`
- Primary because: Official upstream code repository containing runtime script, utilities, README, license, and weight directories cited in the dossier.
- Scope: Repository root and directory listings
- Supports: presence of top-level files README.md, protein_mpnn_run.py, protein_mpnn_utils.py, LICENSE
- Supports: presence of helper_scripts and weight directories

### README.md (ProteinMPNN)

- URL: https://github.com/dauparas/ProteinMPNN/blob/main/README.md
- Publisher: dauparas
- Type: `repository`
- Primary because: Repository README documents usage examples and example outputs used to validate runtime output fields.
- Scope: Repository README
- Supports: example output sequences with associated scores and sequence-recovery metrics
- Supports: usage and runtime-flag documentation

### protein_mpnn_run.py

- URL: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py
- Publisher: dauparas
- Type: `repository`
- Primary because: Runtime script documenting command-line flags, model hyper-parameter defaults, model_name defaults and allowed values, checkpoint path construction, and runtime output formatting.
- Scope: Runtime script used to run/design/score sequences
- Supports: definition of hidden_dim = 128 and num_layers = 3
- Supports: flags --ca_only, --use_soluble_model, --model_name and their behaviors
- Supports: construction of checkpoint path as selected model folder + model_name + .pt
- Supports: printing CA-only messages and output fields

### protein_mpnn_utils.py

- URL: https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py
- Publisher: dauparas
- Type: `repository`
- Primary because: Helper utilities implementing featurization primitives, masks, PSSM arrays, and CA-only vs full-backbone handling used by the runtime script.
- Scope: Featurization and helper utilities
- Supports: ProteinFeatures class, positional encodings and edge-embedding layer definitions
- Supports: initialization of fixed_position_mask, omit_AA_mask, and related preprocessing arrays
- Supports: CA-only and full-backbone coordinate handling used in featurization

### ProteinMPNN LICENSE

- URL: https://github.com/dauparas/ProteinMPNN/blob/main/LICENSE
- Publisher: dauparas
- Type: `repository`
- Primary because: Repository LICENSE file provides the license terms for repository contents.
- Scope: Repository license
- Supports: MIT license text present in the repository

### vanilla_model_weights directory (ProteinMPNN)

- URL: https://github.com/dauparas/ProteinMPNN/tree/main/vanilla_model_weights
- Publisher: dauparas
- Type: `repository`
- Primary because: Repository directory containing the vanilla model checkpoint filenames reported in the findings.
- Scope: vanilla_model_weights directory
- Supports: presence of v_48_002.pt, v_48_010.pt, v_48_020.pt, v_48_030.pt

### soluble_model_weights directory (ProteinMPNN)

- URL: https://github.com/dauparas/ProteinMPNN/tree/main/soluble_model_weights
- Publisher: dauparas
- Type: `repository`
- Primary because: Repository directory containing the soluble-trained model checkpoint filenames reported in the findings.
- Scope: soluble_model_weights directory
- Supports: presence of v_48_010.pt, v_48_020.pt

### ca_model_weights directory (ProteinMPNN)

- URL: https://github.com/dauparas/ProteinMPNN/tree/main/ca_model_weights
- Publisher: dauparas
- Type: `repository`
- Primary because: Repository directory containing the CA-only model checkpoint filenames reported in the findings.
- Scope: ca_model_weights directory
- Supports: presence of v_48_002.pt, v_48_010.pt, v_48_020.pt

### ProteinMPNN releases (repository releases view)

- URL: https://github.com/dauparas/ProteinMPNN/releases
- Publisher: dauparas
- Type: `repository`
- Primary because: Repository releases page lists release entries and commit-hash strings associated with the repository.
- Scope: Repository releases
- Supports: release entries in the repository and commit-hash strings

### ProteinMPNN canonical preprint (bioRxiv)

- URL: https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf
- Publisher: bioRxiv / Dauparas et al.
- Type: `paper`
- Primary because: Canonical preprint describing ProteinMPNN model, training, datasets, and numeric benchmark-level results cited in the dossier.
- Scope: ProteinMPNN preprint main text, Methods, and Supplementary Materials
- Supports: reports of numeric benchmarks (native sequence recovery and experimental validations)
- Supports: dataset splits and training/validation/test cluster counts described in Methods and Supplement

### ProteinMPNN Science paper PDF (publisher supplementary PDF)

- URL: https://ipd.uw.edu/publication-pdfs/275/3d98c978aed6d429d315317432f674b9/science.add2187.pdf
- Publisher: Science (publisher PDF mirror listed in findings)
- Type: `paper`
- Primary because: Publisher/paper PDF and supplementary materials for the ProteinMPNN Science publication as listed in the research findings.
- Scope: Published paper and supplementary materials
- Supports: supplementary methods, figures and tables referenced in the preprint/paper

### PubMed entry for ProteinMPNN (Science)

- URL: https://pubmed.ncbi.nlm.nih.gov/36108050
- Publisher: PubMed / Science
- Type: `paper`
- Primary because: Bibliographic entry for the published ProteinMPNN paper referenced in the findings.
- Scope: Published paper metadata
- Supports: publication bibliographic metadata (DOI, authors, journal)

### arXiv preprint (version noting generative/inverse folding commentary)

- URL: https://arxiv.org/html/2312.02447v1
- Publisher: arXiv
- Type: `paper`
- Primary because: ArXiv-hosted document in the research findings discussing ProteinMPNN and generative inverse folding approaches; used for background benchmark and method facts present in the findings.
- Scope: ArXiv HTML content (version noted in findings)
- Supports: descriptive and benchmark-level statements about ProteinMPNN usage and training regimen (as included in the provided findings)

### arXiv entry mentioning official checkpoint v_48_020

- URL: https://arxiv.org/html/2605.18552v1
- Publisher: arXiv
- Type: `paper`
- Primary because: ArXiv-hosted content in the findings that references an official checkpoint version v_48_020 and CA-only behavior.
- Scope: ArXiv HTML content (version noted in findings)
- Supports: statement that official checkpoint version v_48_020 extracts full backbone representations (ca_only=False) as reported in the findings

### PMC article referencing ProteinMPNN benchmarks and experimental validation

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10862708
- Publisher: PubMed Central
- Type: `paper`
- Primary because: PMC-hosted article in the findings that reports benchmark/validation-level outcomes associated with ProteinMPNN designs.
- Scope: PMC article content
- Supports: statements about ProteinMPNN benchmark outcomes and applicability to design tasks (as included in the provided findings)

## Evidence gaps

- No canonical publication URL-to-checkpoint mapping found in inspected sources: checked https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf (main text, Methods, Supplementary Tables), https://ipd.uw.edu/publication-pdfs/275/3d98c978aed6d429d315317432f674b9/science.add2187.pdf (supplementary), and repository releases at https://github.com/dauparas/ProteinMPNN/releases; no explicit table/row mapping specific .pt filenames to numeric benchmark rows was located.
- No machine-readable JSON input schema found: inspected https://github.com/dauparas/ProteinMPNN, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, and helper_scripts directory; no explicit JSON schema file or schema section in README was found.
- No machine-readable JSON output schema found: inspected https://github.com/dauparas/ProteinMPNN and https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py and README; no JSON output-schema file or explicit output-schema documentation located.
- No explicit parameter count reported: inspected https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py, https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_utils.py, and canonical preprint https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf; no explicit number-of-parameters value was reported in these checked locations.
- No deterministic immutable mapping from runtime flags to a specific commit-locked .pt file found: inspected https://github.com/dauparas/ProteinMPNN/blob/main/protein_mpnn_run.py and https://github.com/dauparas/ProteinMPNN/releases for evidence tying a given --model_name flag to a specific release commit; explicit immutable mapping was not present in the inspected locations.
- No checkpoint-matched numeric benchmark rows tying exact .pt filenames to dataset splits and metric values were found: inspected https://biorxiv.org/content/10.1101/2022.06.03.494563v1.full.pdf (main text, Methods, Supplementary Tables), https://ipd.uw.edu/publication-pdfs/275/3d98c978aed6d429d315317432f674b9/science.add2187.pdf (supplementary), and https://github.com/dauparas/ProteinMPNN/releases.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[0] without evidence must be labeled as a Forge policy or evidence gap: $.safety[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety[3] without evidence must be labeled as a Forge policy or evidence gap: $.safety[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
