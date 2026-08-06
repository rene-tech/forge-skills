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

- Research key: `huggingface-co-facebook-esmfold-v1-421dc564b0`
- Independent audit: `revised`
- Researched: `2026-08-06T11:46:48.935778+00:00`

facebook/esmfold_v1 (checkpoint/revision 75a3841ee059df2bf4d56688166c8fb459ddd97a) pairs an ESM-2 3B trunk (esm2_3B) with a folding/structure module (ESMFold v1). The Hugging Face snapshot README for the named commit and the checkpoint config.json document that ESMFold performs end-to-end structure prediction from a single amino-acid sequence without MSA lookup and that the trunk/structure-module architecture fields are present in the config.json. Primary-code/archive summary evidence reports the combined parameter counts as 690M (+3B) and the trunk type as esm2_3B. The checked primary sources do not provide checkpoint-scoped numeric per-target benchmark tables (TM-score/RMSD/runtimes) or an explicit checkpoint-scoped weights license statement; those absences are recorded as evidence gaps below.

## Identity

- Upstream name: facebook/esmfold_v1
- Checkpoint/version: 75a3841ee059df2bf4d56688166c8fb459ddd97a
- Immutable revision: 75a3841ee059df2bf4d56688166c8fb459ddd97a
- Parameter scale: 690M folding/head + 3B ESM-2 trunk (reported together in archive snapshot summary)
- Architecture/head: ESMFold v1: ESM-2 language-model trunk (esm2_3B) paired with a folding/structure module; checkpoint config.json lists trunk and structure_module fields (trunk.num_blocks=48, trunk.num_hidden_layers=36, trunk.num_attention_heads=40, trunk.max_position_embeddings=1026, structure_module.num_blocks=8, structure_module.sequence_dim=384, structure_module.pairwise_dim=128)
- License: Code: MIT (repository LICENSE). Weights license: not reported for this exact checkpoint in the checked primary sources.
- Evidence: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json, https://huggingface.co/facebook/esmfold_v1/commit/75a3841ee059df2bf4d56688166c8fb459ddd97a, https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20, https://github.com/facebookresearch/esm/blob/main/esm/model/esm2.py, https://github.com/facebookresearch/esm/blob/main/LICENSE

## Selection

### Recommended

- **Research-scale prediction of protein tertiary structure from a single amino-acid sequence for exploratory structural hypotheses and visualization (single-sequence monomer prediction)** — Hugging Face model snapshot README for the cited commit documents ESMFold as an end-to-end, single-sequence predictor that does not require MSA or external databases; the checkpoint config.json contains folding/structure module fields indicating model produces structures.
  Scope: facebook/esmfold_v1 (checkpoint revision 75a3841ee059df2bf4d56688166c8fb459ddd97a)
  Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://huggingface.co/facebook/esmfold_v1/blob/main/config.json
- **High-throughput, single-sequence scanning of large sequence sets when alignment-free inference and speed are prioritized over MSA-based accuracy** — The Hugging Face snapshot README claims ESMFold does not require MSA or external databases and asserts inference is significantly faster than AlphaFold2; archive/repository summary notes ESMFold is an alignment-free end-to-end predictor harnessing an ESM-2 trunk.
  Scope: facebook/esmfold_v1 (checkpoint revision 75a3841ee059df2bf4d56688166c8fb459ddd97a)
  Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

### Conditional

- **Prediction for proteins with limited homologs (low MSA depth) where MSA-based methods may be disadvantaged — use with careful validation** — Validate predictions on similar proteins and perform orthogonal experimental validation when possible because the alignment-free architecture yields a different error profile; verify model outputs against experimental structures and perform downstream checks before use in high-value decisions.
  Scope: facebook/esmfold_v1 (checkpoint revision 75a3841ee059df2bf4d56688166c8fb459ddd97a)
  Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20
- **Rapid approximate structures for downstream triage where approximate topology suffices and expert/experimental follow-up is planned** — Use only when approximate results are acceptable; perform targeted experimental validation for high-value targets because calibration and error profiles differ from MSA-based methods.
  Scope: facebook/esmfold_v1 (checkpoint revision 75a3841ee059df2bf4d56688166c8fb459ddd97a)
  Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

### Avoid

- **Clinical diagnostic decision making or making safety-critical structure-based diagnoses without expert review and experimental validation** — No primary-source evidence in the checked sources establishes regulatory approval or validated acceptance criteria for clinical diagnostic use of this checkpoint; the checked model README and repository/ archive summaries describe research usage and do not claim regulatory approval.
  Scope: facebook/esmfold_v1 (checkpoint revision 75a3841ee059df2bf4d56688166c8fb459ddd97a)
  Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20
- **Fully automated high-consequence biological design (therapeutics, biological agent modification) without expert review and experimental validation** — The checked primary sources describe research and benchmarking contexts and do not provide checkpoint-scoped validated acceptance thresholds for unattended safety-critical design workflows.
  Scope: facebook/esmfold_v1 (checkpoint revision 75a3841ee059df2bf4d56688166c8fb459ddd97a)
  Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

## Input preparation

### Semantic inputs

- Single amino-acid primary sequence (protein sequence string) is the canonical semantic input for ESMFold v1 as documented in the Hugging Face model snapshot README for the checkpoint. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://huggingface.co/facebook/esmfold_v1/commit/75a3841ee059df2bf4d56688166c8fb459ddd97a

### Accepted formats

- The model snapshot and README present the model as accepting single protein sequence strings for inference; the checked repository snapshot does not enumerate an authoritative list of accepted container file formats (e.g., FASTA) for this checkpoint. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://huggingface.co/facebook/esmfold_v1/commit/75a3841ee059df2bf4d56688166c8fb459ddd97a

### Preprocessing

- Tokenization vocabulary, trunk type, and maximum input length constraints are present in the checkpoint config.json (fields include trunk.model_type 'esm', trunk.num_hidden_layers=36, trunk.num_attention_heads=40, trunk.max_position_embeddings=1026, and esmfold_config.esm_type='esm2_3B'). Sources: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json
- Config.json lists model numerical hyperparameters and flags relevant to preprocessing and runtime (e.g., hidden_size=2560, intermediate_size=10240, position_embedding_type='rotary', token_dropout=true) which should guide tokenizer/featurizer implementation. Sources: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json
- Evidence gap: The checked primary sources do not include a canonical, checkpoint-scoped statement enumerating service-level batch-size limits, server-side truncation/cropping policies, or exact recommended chunking settings for production inference.

### Pre-submit validation

- Input alphabet and maximum input length constraints should be validated against the checkpoint config.json (max_position_embeddings=1026); inputs exceeding this require application-level handling. Sources: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json
- Evidence gap: No canonical, checkpoint-scoped documentation in the checked primary sources specifies exact handling rules for nonstandard residues, post-translational modifications, or ambiguous token mappings beyond the vocab implied by config.json.

### Task-specific formatting

- No natural-language prompt format is required; the checked model snapshot and README describe sequence-string inputs for inference. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md

## Output interpretation

### Outputs

- The checkpoint is described in the Hugging Face model snapshot README as producing atomic-level structure predictions from single-sequence input (end-to-end structure prediction). Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://huggingface.co/facebook/esmfold_v1/commit/75a3841ee059df2bf4d56688166c8fb459ddd97a
- Evidence gap: The checked primary sources do not include a definitive, checkpoint-scoped listing of exact packaged output field names/keys (for example, an explicit per-residue confidence key name, or a canonical mapping of pLDDT to PDB B-factor) in the checkpoint snapshot files or config.json.

### Interpretation

- Interpret outputs cautiously and validate against experimental structures where available; the checked model snapshot and repository/ archive summaries emphasize research usage and different error profiles for alignment-free predictors. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

### Post-inference validation

- Post-inference validation should include comparison to experimental structures (PDB) and contextual assessment of confidence measures; checked primary sources direct users to accompanying papers for details but do not publish checkpoint-scoped acceptance thresholds. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md
- Evidence gap: No canonical, checkpoint-scoped specification for automatic acceptance thresholds or validated pass/fail criteria for safety-critical decisions was found in the checked primary sources.

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### deepmind-alphafold2-nim — `tradeoff`

- Task: Single-sequence protein structure prediction quality (aggregate accuracy) and runtime tradeoffs
- Criteria: Runtime (inference speed) versus MSA-dependent accuracy; README snapshot claims ESMFold inference is significantly faster than AlphaFold2 and archive summary highlights alignment-free design, but the checked sources do not provide protocol-matched numeric accuracy vs runtime tables for the exact checkpoint.
- Rationale: README for the named checkpoint asserts significantly faster inference than AlphaFold2; archive snapshot and repository summary describe ESMFold as alignment-free and note combined parameter accounting (690M + 3B). The checked sources do not contain detailed checkpoint-scoped numeric accuracy tables for direct protocol-matched comparison.
- Comparison conditions: Direct comparability requires matching exact checkpoints, MSA/recycling protocols, and numeric tables; those protocol-matched numeric rows for both sides are not present in the checked sources.
- Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

### openfold3-nim — `insufficient-evidence`

- Task: Protein structure prediction (quality/modality/input limits)
- Criteria: No checkpoint-to-checkpoint, protocol-matched comparison data available in the checked primary sources for OpenFold3 versus this exact facebook/esmfold_v1 checkpoint.
- Rationale: The checked primary sources for facebook/esmfold_v1 do not include OpenFold3 checkpoint metadata or protocol-matched benchmark rows that would allow a direct head-to-head comparison.
- Comparison conditions: Absent protocol-matched numeric benchmark rows and absent OpenFold3 checkpoint artifacts in the checked sources.
- Evidence: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

## Limitations and safety

### Limitations

- ESMFold v1 is an alignment-free, single-sequence predictor (omits external MSA and template branches) which yields a different error profile from MSA-based methods and may reduce accuracy where evolutionary or template information is critical. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20
- The checkpoint config.json documents architecture and numerical sizes but does not itself provide protocol-matched numeric benchmark tables (TM-score/RMSD) or per-target runtime tables for the named checkpoint in the checked sources. Sources: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json, https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md
- Evidence gap: No canonical, checkpoint-scoped microbenchmark tables enumerating per-target runtimes, seeds, and exact compute/hardware measurement protocols for facebook/esmfold_v1 were found in the checked primary sources.

### Safety

- No primary-source evidence in the checked materials indicates facebook/esmfold_v1 is approved for clinical or diagnostic use; do not use this checkpoint alone for safety-critical clinical decisions without regulatory approval and expert experimental validation. Sources: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md, https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20
- Model code in the facebookresearch/esm repository is provided under the MIT License per the repository LICENSE file (code license). Sources: https://github.com/facebookresearch/esm/blob/main/LICENSE
- Evidence gap: No checkpoint-scoped weights license statement was found for the exact facebook/esmfold_v1 snapshot in the checked primary sources.
- Evidence gap: No primary-source, checkpoint-scoped guidance for safe handling, provenance logging, or regulatory-compliance workflows for deployment of facebook/esmfold_v1 was found in the checked sources.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### facebook/esmfold_v1 config.json (Hugging Face repo)

- URL: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official checkpoint configuration file extracted from the Hugging Face model repository snapshot; contains the trunk and structure_module JSON fields used to verify architecture, num_blocks, attention/head sizes, and max_position_embeddings.
- Scope: facebook/esmfold_v1 configuration (config.json)
- Supports: Architecture fields such as model_type, num_hidden_layers, num_attention_heads, is_folding_model, structure_module.num_blocks, vocab-related and max_position_embeddings
- Supports: Trunk parameterization fields including trunk.num_blocks=48, trunk.num_hidden_layers=36, trunk.num_attention_heads=40, trunk.max_position_embeddings=1026
- Supports: Structure module fields including structure_module.num_blocks=8 and sequence_dim/pairwise_dim

### ESMFold README at commit 75a3841 (facebook/esmfold_v1 snapshot)

- URL: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md
- Publisher: Hugging Face (model repository snapshot)
- Type: `model-card`
- Primary because: Snapshot README corresponding to the named checkpoint commit; documents single-sequence inference behavior and asserts inference-time speed characteristics relative to AlphaFold2 and points users to accompanying papers/tutorials.
- Scope: facebook/esmfold_v1 README at commit 75a3841ee059df2bf4d56688166c8fb459ddd97a
- Supports: High-level usage description that ESMFold performs end-to-end single-sequence structure prediction without requiring MSA or external databases
- Supports: Claim in the snapshot README that ESMFold inference is significantly faster than AlphaFold2
- Supports: Commit-level snapshot context (used to verify checkpoint identity in the model repository)

### Hugging Face model page commit snapshot (commit view)

- URL: https://huggingface.co/facebook/esmfold_v1/commit/75a3841ee059df2bf4d56688166c8fb459ddd97a
- Publisher: Hugging Face (model repository snapshot)
- Type: `model-card`
- Primary because: Model repository commit view for the named checkpoint revision used to corroborate the snapshot README and checkpoint identity.
- Scope: facebook/esmfold_v1 at commit 75a3841ee059df2bf4d56688166c8fb459ddd97a
- Supports: Checkpoint revision identity and snapshot-level README/license field shown in the commit
- Supports: Repository-level snapshot metadata for the named checkpoint

### Archive snapshot of facebookresearch/esm repository (archive.org capture)

- URL: https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20
- Publisher: Internet Archive (archival capture of the official repository)
- Type: `repository`
- Primary because: Archived snapshot of the upstream facebookresearch/esm repository used as a primary-code summary source in the checked findings; contains high-level repository descriptions including parameter-scale accounting for esm2 models and ESMFold composition statements.
- Scope: facebookresearch/esm repository archive snapshot
- Supports: Summary statements that ESMFold harnesses ESM-2 and combined parameter accounting for esmfold_v1 as 690M (+3B)
- Supports: Repository-level descriptions of ESM-2 trunk sizes and layer counts (e.g., esm2_t36_3B with 36 layers and 3B parameters) used to corroborate trunk scale

### ESM model implementation file (esm/model/esm2.py) — facebookresearch/esm

- URL: https://github.com/facebookresearch/esm/blob/main/esm/model/esm2.py
- Publisher: Meta / Facebook Research (GitHub)
- Type: `repository`
- Primary because: Upstream model implementation file included in the checked findings; used to corroborate token/representation output keys and some implementation-level behaviors for ESM-2 trunk components.
- Scope: ESM-2 model implementation (esm2.py) in facebookresearch/esm
- Supports: Implementation-level outputs for ESM-2 trunk such as returned dict keys ('logits', 'representations') and token-handling behavior documented in the file

### facebookresearch/esm LICENSE

- URL: https://github.com/facebookresearch/esm/blob/main/LICENSE
- Publisher: Meta / Facebook Research (GitHub)
- Type: `repository`
- Primary because: Official repository license file for the upstream facebookresearch/esm repository.
- Scope: facebookresearch/esm repository licensing
- Supports: Repository LICENSE declares the MIT License (code license)

### Exact official starting source declared by Forge

- URL: https://huggingface.co/facebook/esmfold_v1
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: facebook-esmfold
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No primary-source, checkpoint-scoped numeric benchmark table (TM-score, RMSD, per-target runtimes, median runtimes) for facebook/esmfold_v1 was found in the checked primary sources (checked: README at commit, config.json, archive snapshot). Locator(s) checked: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md ; https://huggingface.co/facebook/esmfold_v1/blob/main/config.json ; https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20
- Evidence gap: No checkpoint-scoped weights license statement was found for the exact facebook/esmfold_v1 snapshot in the checked primary sources (checked: README at commit, repository LICENSE). Locator(s) checked: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md ; https://github.com/facebookresearch/esm/blob/main/LICENSE
- Evidence gap: No canonical, checkpoint-scoped listing of exact packaged output field names/keys (e.g., explicit per-residue confidence key name or mapping of pLDDT to PDB B-factor) was found in the checked primary sources (checked: config.json, README at commit, esm2.py). Locator(s) checked: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json ; https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md ; https://github.com/facebookresearch/esm/blob/main/esm/model/esm2.py
- Evidence gap: No canonical, checkpoint-scoped documentation for handling nonstandard residues, post-translational modifications, or ambiguous token mappings was found in the checked primary sources (checked: config.json, README at commit). Locator(s) checked: https://huggingface.co/facebook/esmfold_v1/blob/main/config.json ; https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md
- Evidence gap: No primary-source, checkpoint-scoped microbenchmark tables enumerating per-target runtimes with fully specified hardware/protocol (A100 or other GPU, batch, residue length, recycling/chunking) for facebook/esmfold_v1 were found in the checked primary sources (checked: README at commit, archive snapshot). Locator(s) checked: https://huggingface.co/facebook/esmfold_v1/blob/75a3841ee059df2bf4d56688166c8fb459ddd97a/README.md ; https://archive.org/details/github.com-facebookresearch-esm_-_2022-11-03_04-01-20

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 25 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].direction: $.benchmarks[0].direction: 'higher-is-better (TM‑score) / lower-is-better (RMSD)' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].direction: $.benchmarks[1].direction: 'lower-is-better (runtime)' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].direction: $.benchmarks[2].direction: 'lower-is-better (runtime)' is not in ['higher-is-better', 'lower-is-better', 'context-only'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary URL https: $.sources[10] uses forbidden secondary URL https://rewire.it/blog/structure-without-alignment Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/facebook/esmfold_v1/discussions/5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'oliverlaboratory' for this exact model scope: $.sources[18] uses unapproved repository owner 'oliverlaboratory' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.clore.ai/guides/science-and-research/esmfold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://biorxiv.org/content/10.1101/2025.06.20.660709v1.full-text Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.clore.ai/guides/science-and-research/esmfold Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/facebookresearch/esm/issues/636 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/facebookresearch/esm/issues/636 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/facebookresearch/esm/issues/636 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretationExtras: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://huggingface.co/facebook/esmfold_v1: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
