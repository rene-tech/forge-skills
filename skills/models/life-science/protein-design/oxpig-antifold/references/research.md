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

- Research key: `github-com-oxpig-antifold-aef5c06bce`
- Independent audit: `revised`
- Researched: `2026-07-23T23:37:13.142732+00:00`

From the inspected canonical AntiFold repository and example files: the repository contains a file named model.pt and README references "Model: model.pt"; example sampled FASTA outputs and CSV residue log‑likelihood outputs are present in the repository's output folder; a Jupyter notebook (notebook.ipynb) exists with a recorded commit (SHA e353534) for that notebook file. The repository metadata and files indicate AntiFold is based on and fine‑tuned from ESM‑IF1 and trained on solved and predicted antibody structures; however, the inspected repository files do not provide an immutable commit SHA or release tag that uniquely identifies the model.pt artifact, do not report an explicit parameter count for the model.pt checkpoint, and do not present numbered/figured benchmark tables or numeric benchmark rows traceable to model.pt. Additional expected details (immutable checkpoint locator for model.pt, numeric benchmark tables tied to model.pt, explicit input‑validation specifications, inference hyperparameters, and probabilistic calibration bounds) are not reported in the inspected primary sources.

## Identity

- Upstream name: AntiFold
- Checkpoint/version: model.pt (file present in repository at repository root; exact commit SHA for this file not reported in inspected sources)
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Based on the ESM-IF1 backbone (AntiFold described as fine‑tuned from ESM‑IF1)
- License: BSD-3-Clause
- Evidence: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta, https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb

## Selection

### Recommended

- **Antibody variable‑domain inverse folding (predict amino‑acid sequences conditioned on a provided variable‑domain backbone structure).** — Repository materials and files indicate AntiFold is implemented to predict sequences that fit antibody variable‑domain backbone structures and are fine‑tuned on antibody structure data.
  Scope: AntiFold checkpoint artifact referenced as model.pt in https://github.com/oxpig/AntiFold (repository files demonstrate sequence prediction conditioned on antibody backbone structures).
  Evidence: https://github.com/oxpig/AntiFold
- **Generate sampled candidate antibody sequences in FASTA format for downstream structural validation and design workflows.** — The repository contains example sampled FASTA outputs demonstrating sampling functionality and per‑sample metadata fields.
  Scope: AntiFold repository sampling code using model.pt producing FASTA outputs (example file present at output/example_pdbs/6y1l_imgt.fasta).
  Evidence: https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta, https://github.com/oxpig/AntiFold
- **Produce per‑residue log‑likelihood CSV outputs for sequence‑to‑structure compatibility analysis and ranking candidate sequences.** — The repository includes CSV residue log‑likelihood outputs as part of inference outputs according to repository files/README.
  Scope: AntiFold inference outputs produced by model.pt (CSV residue log‑likelihood outputs as present in repository artifacts).
  Evidence: https://github.com/oxpig/AntiFold

### Conditional

- **Use designed sequences in workflows that perform downstream structure prediction (refolding) to validate structural agreement before experimental follow‑up.** — Repository example outputs and statements indicate sampled sequences show structural agreement with experimental structures, but no numeric refolding protocol, refolding model name, or hyperparameters are provided in the inspected sources; downstream refolding/validation must therefore be performed by the user and the exact refolding method/hyperparameters must be selected and documented externally.
  Scope: AntiFold (model.pt in repository) used with externally run structure‑prediction/refolding tools (refolding method and parameters not specified in inspected repository files).
  Evidence: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta
- **Condition sequence generation on antigen context only after verifying repository codepaths for antigen conditioning.** — The repository contains implementation materials but does not present a numbered protocol or enumerated input format fields for antigen conditioning in the inspected files; users must verify antigen‑conditioning input parsing in the code before assuming compatibility.
  Scope: AntiFold (model.pt in repository) with conditioning behavior dependent on inspected repository code and user verification.
  Evidence: https://github.com/oxpig/AntiFold

### Avoid

- **Clinical diagnostic or therapeutic deployment without further validation or regulatory review.** — The inspected repository does not include regulatory approvals, clinical‑use documentation, or materials establishing suitability for clinical deployment; additionally, the repository does not provide an immutable release tag or commit SHA uniquely identifying model.pt to support reproducible checkpoint identification.
  Scope: AntiFold (model.pt in repository)
  Evidence: https://github.com/oxpig/AntiFold
- **Assuming built‑in PHI handling, clinical data governance, or production clinical data pipelines.** — Evidence gap: the inspected repository does not include explicit PHI/data‑handling instructions, governance procedures, or clinical data mitigation measures.
  Scope: AntiFold repository and associated materials inspected
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- Antibody variable‑domain backbone structure representations (structure modality) are the primary inputs consumed to predict sequences. Sources: https://github.com/oxpig/AntiFold

### Accepted formats

- Repository example outputs demonstrate FASTA sampled outputs; an example sampled FASTA is present at output/example_pdbs/6y1l_imgt.fasta. Sources: https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta
- Evidence gap: the inspected repository does not provide a formalized, enumerated input specification (required PDB/mmCIF fields, coordinate units, chain ID conventions) in a numbered table, figure, or dedicated input specification file. Sources: https://github.com/oxpig/AntiFold

### Preprocessing

- AntiFold is described in the repository as fine‑tuned on solved and predicted antibody structures derived from antibody structure datasets. Sources: https://github.com/oxpig/AntiFold
- Evidence gap: the inspected repository does not enumerate detailed preprocessing normalization, tokenization, or coordinate normalization steps in a numbered table/figure or dedicated file. Sources: https://github.com/oxpig/AntiFold

### Pre-submit validation

- Evidence gap: the inspected repository does not specify a formal set of input‑validation rules (e.g., required PDB/mmCIF fields, coordinate units, chain ID conventions) in a dedicated, numbered locator. Sources: https://github.com/oxpig/AntiFold

### Task-specific formatting

- Example sampled FASTA outputs in the repository include per‑sample metadata fields in FASTA headers (metadata visible in the example file output/example_pdbs/6y1l_imgt.fasta). Sources: https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta
- The repository exposes CSV residue log‑likelihood outputs as part of inference outputs according to repository files/README, but no enumerated API prompt template or numbered input/output schema is present in a dedicated locator in the inspected files. Sources: https://github.com/oxpig/AntiFold

## Output interpretation

### Outputs

- Repository example FASTA files contain per‑sample metadata fields in FASTA headers used for ranking and evaluation (visible in output/example_pdbs/6y1l_imgt.fasta). Sources: https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta
- Residue log‑likelihoods are emitted in CSV format as part of the inference outputs according to repository files and examples. Sources: https://github.com/oxpig/AntiFold

### Interpretation

- Seq_recovery and residue log‑likelihood scores are presented in repository outputs and used for ranking; the inspected sources do not provide probabilistic calibration bounds or per‑residue confidence thresholds. Sources: https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta, https://github.com/oxpig/AntiFold

### Post-inference validation

- Evidence gap: a numbered refolding/structural validation protocol (model, version, hyperparameters) is not present in the inspected repository; structural agreement is illustrated in example outputs but not specified with a reproducible refolding protocol. Sources: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### dauparas-proteinmpnn-suite (ProteinMPNN) — `insufficient-evidence`

- Task: Antibody inverse folding / sequence recovery
- Criteria: No primary, numbered/figured repository table or figure was found that reports side‑by‑side numeric comparisons between AntiFold (model.pt) and ProteinMPNN under identical protocols in the inspected sources.
- Rationale: The inspected AntiFold repository contains implementation files and example outputs but does not present a benchmark table or figure providing numeric comparisons traceable to model.pt; no primary ProteinMPNN benchmark locators were inspected in these findings.
- Comparison conditions: Repository search of the AntiFold project (root files, output/example_pdbs/6y1l_imgt.fasta, notebook.ipynb) yielded no like‑for‑like numeric comparison table/figure; no ProteinMPNN primary benchmark source was part of the inspected findings to allow a like‑for‑like comparison.
- Evidence: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb

### rfdiffusion-nim (RFdiffusion) — `insufficient-evidence`

- Task: Antibody inverse folding / sequence recovery
- Criteria: No primary, numbered/figured repository table or figure was found in the inspected AntiFold sources that reports RFdiffusion results alongside AntiFold results under identical protocols.
- Rationale: Inspected AntiFold repository files do not include numeric benchmark tables keyed to model.pt; no primary RFdiffusion benchmark locators were inspected within the provided findings.
- Comparison conditions: Checked repository root, example outputs, and notebook.ipynb for benchmark tables; none reported side‑by‑side numeric comparisons with RFdiffusion.
- Evidence: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb

### abmpnn (AbMPNN) — `insufficient-evidence`

- Task: Antibody inverse folding / sequence recovery
- Criteria: No primary, numbered/figured comparison table or figure in the inspected AntiFold repository reports numeric results for AbMPNN and AntiFold under identical protocols traceable to model.pt.
- Rationale: The inspected repository contains example outputs and implementation materials but lacks numeric side‑by‑side benchmark tables; no primary AbMPNN benchmark locators were part of the inspected findings.
- Comparison conditions: Inspected repository root, example outputs, and notebook.ipynb for benchmark tables; none reported AbMPNN comparisons.
- Evidence: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb

### esm-if1 (ESM‑IF1) — `insufficient-evidence`

- Task: Antibody inverse folding / sequence recovery (base vs. fine‑tuned performance)
- Criteria: While AntiFold is described as fine‑tuned from ESM‑IF1 in the inspected repository, no numbered/figured table or repository path in the inspected files reports a direct numeric comparison between the base ESM‑IF1 checkpoint and the AntiFold model.pt under identical evaluation protocols.
- Rationale: Inspected repository indicates lineage (fine‑tuning from ESM‑IF1) but does not contain numeric head‑to‑head benchmark tables or figures tied to model.pt and an explicit ESM‑IF1 checkpoint.
- Comparison conditions: Checked repository root, example outputs, and notebook.ipynb for numeric comparison tables; none found in inspected sources.
- Evidence: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb

## Limitations and safety

### Limitations

- AntiFold is based on and described in the repository as fine‑tuned from the ESM‑IF1 backbone and is trained on solved and predicted antibody structures derived from antibody structure datasets. Sources: https://github.com/oxpig/AntiFold
- Training and benchmarking rely on solved and predicted antibody structures (the inspected repository states fine‑tuning on solved and predicted antibody structures), but the repository does not provide numbered/figured tables with per‑split numeric coverage or detailed dataset split files for independent reconstruction in the inspected files. Sources: https://github.com/oxpig/AntiFold
- Evidence gap: no immutable release tag or commit SHA uniquely identifying the repository model file model.pt was reported in the inspected repository files; this limits reproducible identification of the exact checkpoint. Sources: https://github.com/oxpig/AntiFold
- Evidence gap: the inspected repository does not enumerate exact inference hyperparameters (sampling temperatures, seeds, batch sizes) or refolding tool hyperparameters in a dedicated numbered locator, which reduces reproducibility of reported numeric comparisons. Sources: https://github.com/oxpig/AntiFold, https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb

### Safety

- Evidence gap: the inspected repository does not include explicit PHI/data‑handling instructions, clinical‑use mitigation measures, or regulatory authorization statements tied to AntiFold in the files checked.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### AntiFold (GitHub repository)

- URL: https://github.com/oxpig/AntiFold
- Publisher: oxpig (GitHub)
- Type: `repository`
- Primary because: Official project repository containing code, model artifact reference (model.pt), example outputs, and notebooks used as primary evidence.
- Scope: AntiFold repository; checkpoint artifact referenced as model.pt (no immutable commit SHA for model.pt identified in the inspected files).
- Supports: The AntiFold repository includes a file named model.pt and README references 'Model: model.pt'.
- Supports: Repository indicates AntiFold is based on and fine‑tuned from ESM‑IF1 and trained on solved and predicted antibody structures.
- Supports: Repository contains CSV residue log‑likelihood outputs and sampling/inference code examples.

### AntiFold example sampled FASTA (repository path)

- URL: https://github.com/oxpig/AntiFold/blob/master/output/example_pdbs/6y1l_imgt.fasta
- Publisher: oxpig (GitHub)
- Type: `repository`
- Primary because: Concrete example output file from the project demonstrating sampled FASTA headers and per‑sample metadata used as evidence.
- Scope: Example sampled FASTA illustrating inference output format and sample metadata.
- Supports: Example sampled FASTA contains sequences with metadata fields used for ranking (e.g., score, global_score, seq_recovery visible in headers).
- Supports: Demonstrates sampling output format produced by the repository.

### AntiFold notebook (repository file)

- URL: https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb
- Publisher: oxpig (GitHub)
- Type: `repository`
- Primary because: Repository notebook file present in the project; commit metadata for this file (commit SHA for a recorded commit) was inspected and used as evidence for notebook provenance.
- Scope: Repository notebook usage examples and code (notebook.ipynb).
- Supports: The repository includes notebook.ipynb; the notebook file has a recorded commit (inspected commit SHA e353534 for the May 21, 2024 update to notebook.ipynb as reported in the findings).

## Evidence gaps

- No immutable release tag, commit SHA, or other immutable identifier for the repository model file model.pt was found in the inspected repository at https://github.com/oxpig/AntiFold; exact checkout/commit for model.pt is not reported in the inspected files.
- Parameter count for the specific model.pt checkpoint is not reported in the inspected repository files (https://github.com/oxpig/AntiFold).
- The inspected repository does not contain numbered/figured benchmark tables or repository paths reporting aggregate numeric benchmarks (sequence‑recovery, CDR RMSD, per‑dataset Spearman correlations) traceable to model.pt; checked locations: repository root, output/example_pdbs/6y1l_imgt.fasta, notebook.ipynb.
- No repository locator was found that enumerates inference hyperparameters (sampling temperatures, seeds, batch sizes) used for any numeric benchmarking in the inspected files (checked: https://github.com/oxpig/AntiFold and https://github.com/oxpig/AntiFold/blob/master/notebook.ipynb).
- No formal input specification file or numbered locator describing required PDB/mmCIF fields, coordinate units, or chain ID conventions was found in the inspected repository (checked: https://github.com/oxpig/AntiFold).
- No numbered refolding protocol (refolding model name/version and hyperparameters) was found in the inspected repository; structural validation appears qualitatively in example outputs but lacks a reproducible refolding protocol locator (checked: https://github.com/oxpig/AntiFold and output/example_pdbs/6y1l_imgt.fasta).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[2].direction: $.benchmarks[2].direction: 'higher-is-better (for correlation magnitude)' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].value must contain a reported numeric result: $.benchmarks[2].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
