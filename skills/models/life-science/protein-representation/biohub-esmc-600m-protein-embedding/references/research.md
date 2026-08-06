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

- Research key: `huggingface-co-biohub-esmc-600m-50cdefa50a`
- Independent audit: `revised`
- Researched: `2026-08-06T11:20:37.793421+00:00`

Primary-source inspection of the Hugging Face model landing page and repository commits for biohub/esmc-600m-2024-12, the upstream Biohub GitHub repository (Biohub/esm), and the official ESMC cookbook Colab notebook verifies the existence of the checkpoint biohub/esmc-600m-2024-12, the association to the ESMC family, the 600M parameter scale, and the architectural hyperparameters (36 layers; model dim 1152; 18 heads; head dim 64; FFN 3072; vocab size 64) as reported in the model card and commit-level repository blobs. The repository initial commit records a license name value of "cambrian-non-commercial-license-agreement" and LFS filters for large model artifacts. The Colab cookbook demonstrates programmatic usage with model_name set to "esmc-600m-2024-12". Primary gaps found in the inspected canonical locators include: no checkpoint-scoped tokenizer.json or explicit tokenizer artifact path for esmc-600m-2024-12 in the checked blobs, no explicit checkpoint-scoped JSON output schema or numeric embedding-dimension declaration for per-residue vs per-sequence outputs in the checked locators, no checkpoint-scoped numeric benchmark table/figure rows for this checkpoint in the checked model card/README/commits, and no authoritative Forge wrapper manifest mapping (hf-465f758-python312-cuda128-wrapper-20260529) discovered in the checked primary sources.

## Identity

- Upstream name: ESMC
- Checkpoint/version: biohub/esmc-600m-2024-12
- Immutable revision: 7b9acd43a0736e7d5027ac3eb8a011783ecc4590
- Parameter scale: 600M
- Architecture/head: Transformer; 36 layers; model dimension 1,152; 18 attention heads; head dimension 64; feed-forward hidden dimension 3,072; vocabulary size 64
- License: cambrian-non-commercial-license-agreement
- Evidence: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commit/7b9acd43a0736e7d5027ac3eb8a011783ecc4590, https://huggingface.co/biohub/esmc-600m-2024-12/commit/4bd0526d5e04a7d088c00c8884c18f0f8eaa9d8c

## Selection

### Recommended

- **Research and development: loading and experimentation with the esmc-600m-2024-12 checkpoint for protein representation and exploratory embedding extraction.** — The Hugging Face model page and repository README identify the checkpoint and packaging format; the upstream Biohub README demonstrates programmatic usage and the Colab cookbook sets model_name to "esmc-600m-2024-12" and shows encode/logits usage patterns.
  Scope: biohub/esmc-600m-2024-12
  Evidence: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### Conditional

- **Use in downstream wet-lab, clinical pipelines, or other high-consequence decision workflows only after independent wet-lab validation and explicit license confirmation.** — Evidence gap: The inspected primary sources do not publish checkpoint-scoped clinical-validation guidance, dataset-specific clinical evaluation, or an explicit, unambiguous mapping of model-weights vs code/documentation license terms for biohub/esmc-600m-2024-12 at the checked locations.
  Scope: biohub/esmc-600m-2024-12
  Evidence: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commit/4bd0526d5e04a7d088c00c8884c18f0f8eaa9d8c, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### Avoid

- **Unverified clinical decision-making or deployment without independent validation and explicit licensing confirmation.** — Evidence gap: The inspected primary sources for this checkpoint do not include explicit checkpoint-scoped clinical-validation guidance or an unambiguous, separate model-weights vs code license mapping; therefore high-consequence clinical deployment is not supported by the checked primary documents.
  Scope: biohub/esmc-600m-2024-12
  Evidence: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commit/4bd0526d5e04a7d088c00c8884c18f0f8eaa9d8c, https://github.com/Biohub/esm/blob/main/README.md

## Input preparation

### Semantic inputs

- Protein-sequence inputs (the model and repository README identify this artifact as an ESMC protein model). Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md

### Accepted formats

- Evidence gap: No checkpoint-scoped tokenizer.json, vocab file, or explicit tokenizer artifact path for biohub/esmc-600m-2024-12 was found in the inspected repository blobs/commits and model page; the esmc-6b tokenizer.json exists at a sibling repo path but does not establish an esmc-600m tokenizer artifact at the checked locations. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://huggingface.co/biohub/esmc-6b-2024-12/blob/6ae7b4dd8630350e620a806d0b7ba67e53bcfd46/tokenizer.json

### Preprocessing

- Evidence gap: The inspected primary sources (model page, repository commits, and Colab notebook) do not publish checkpoint-scoped preprocessing/tokenization implementation files or explicit tokenization step-by-step code for biohub/esmc-600m-2024-12 at the checked paths. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### Pre-submit validation

- Evidence gap: The inspected primary sources do not include explicit checkpoint-scoped input-validation rules (allowed alphabet, explicit maximum sequence length, or sanity bounds) for biohub/esmc-600m-2024-12 at the checked model page, README, or commit blobs. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://github.com/Biohub/esm/blob/main/README.md

### Task-specific formatting

- The upstream Colab cookbook demonstrates programmatic usage patterns and sets model_name to "esmc-600m-2024-12" in example code cells (usage example for sequence encoding/workflows). Sources: https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

## Output interpretation

### Outputs

- Evidence gap: The inspected primary sources (model page, README, commits, and Colab cookbook) do not publish a checkpoint-scoped JSON output schema nor do they declare explicit numeric embedding-dimension values or a definitive per-residue vs per-sequence output shape for biohub/esmc-600m-2024-12 at the checked locations. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### Interpretation

- Evidence gap: No recommended normalization, pooling, calibration, or interpretation guidance for embedding outputs specific to biohub/esmc-600m-2024-12 was found in the inspected primary sources. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### Post-inference validation

- Evidence gap: The inspected primary sources do not document post-inference quality-calibration procedures or explicit downstream validation checks for checkpoint outputs at the checked model repository blobs, commits, or Colab cells. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### facebook/esm2_t36_3B_UR50D — `insufficient-evidence`

- Task: protein-embedding
- Criteria: No primary, checkpoint-scoped numeric benchmark rows or identical-protocol comparisons for biohub/esmc-600m-2024-12 were found in the inspected primary locators; therefore a direct numeric comparison cannot be supported from the checked sources.
- Rationale: The inspected primary locators for biohub/esmc-600m-2024-12 (model card, README blobs, commit history, and Colab cookbook) contain model identification and usage examples but do not contain same-protocol numeric evaluation rows for this checkpoint to compare against the named alternative.
- Comparison conditions: Inspected locators: model card root, README blobs, commit history, and Colab notebook; no checkpoint-scoped numeric benchmark rows present for this checkpoint at these locators.
- Evidence: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### facebook/esm2_t33_650M_UR50D — `insufficient-evidence`

- Task: protein-embedding
- Criteria: No primary, checkpoint-scoped numeric benchmark rows or identical-protocol comparisons for biohub/esmc-600m-2024-12 were found in the inspected primary locators; therefore a direct numeric comparison cannot be supported from the checked sources.
- Rationale: The inspected primary locators for biohub/esmc-600m-2024-12 provide identification and example usage but do not contain same-protocol numeric evaluation rows for this checkpoint for direct comparison.
- Comparison conditions: Inspected locators: model card root, README blobs, commit history, and Colab notebook; no checkpoint-scoped numeric benchmark rows present for this checkpoint at these locators.
- Evidence: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

## Limitations and safety

### Limitations

- Training-data provenance and dataset-composition limitations: the ESMC family documentation and repository-level materials report pretraining data sources and sampling regimes at the family/variant level (used to inform model limitations), but checkpoint-scoped dataset-split or per-checkpoint provenance tables were not located at the checked model-card/commit blobs for biohub/esmc-600m-2024-12. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md
- Model-size and architecture reporting: architectural hyperparameters for the 600M variant (36 layers, model dim 1,152, 18 heads, head dim 64, FFN 3,072, vocab size 64) are reported in the model-card/commit-level repository blobs for the ESMC family and the 600M variant. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commit/7b9acd43a0736e7d5027ac3eb8a011783ecc4590
- Evidence gap: Exact context-length (maximum sequence length), checkpoint-scoped tokenizer files (tokenizer.json, vocab files) in the model repository blobs, explicit numeric embedding-dimension declarations for per-residue/per-sequence outputs, and a checkpoint-scoped JSON output schema were not found in the inspected primary locators for biohub/esmc-600m-2024-12. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

### Safety

- Evidence gap: The inspected primary sources (model card, README blobs, commit history, and Colab cookbook) do not contain explicit checkpoint-scoped safety, privacy, or data-handling guidance specific to biohub/esmc-600m-2024-12 at the checked locations; consult repository owners or additional authoritative documents for safety-critical guidance. Sources: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### biohub/esmc-600m-2024-12 model page

- URL: https://huggingface.co/biohub/esmc-600m-2024-12
- Publisher: HuggingFace
- Type: `model-card`
- Primary because: Official Hugging Face model landing page for the checkpoint; used to verify model identifier, high-level metadata, and links to repository blobs/commits.
- Scope: biohub/esmc-600m-2024-12
- Supports: identity
- Supports: model-identification
- Supports: distribution
- Supports: repositoryMetadata

### biohub/esmc-600m-2024-12 commit 7b9acd43a0736e7d5027ac3eb8a011783ecc4590

- URL: https://huggingface.co/biohub/esmc-600m-2024-12/commit/7b9acd43a0736e7d5027ac3eb8a011783ecc4590
- Publisher: HuggingFace
- Type: `repository`
- Primary because: Repository commit blob containing model-card lines and variant table entries that report the 600M variant hyperparameters and parameter counts.
- Scope: biohub/esmc-600m-2024-12
- Supports: identity
- Supports: architecture
- Supports: model-identification

### biohub/esmc-600m-2024-12 commit 4bd0526d5e04a7d088c00c8884c18f0f8eaa9d8c (LFS filters and license entry)

- URL: https://huggingface.co/biohub/esmc-600m-2024-12/commit/4bd0526d5e04a7d088c00c8884c18f0f8eaa9d8c
- Publisher: HuggingFace
- Type: `repository`
- Primary because: Initial commit that adds LFS filters for model file extensions and records the repository license name value (cambrian-non-commercial-license-agreement).
- Scope: biohub/esmc-600m-2024-12
- Supports: distribution
- Supports: license
- Supports: repositoryMetadata

### biohub/esmc-600m-2024-12 .gitattributes (blame view)

- URL: https://huggingface.co/biohub/esmc-600m-2024-12/blame/main/.gitattributes
- Publisher: HuggingFace
- Type: `repository`
- Primary because: Repository blob recording LFS/diff rules for model artifact file extensions, used to verify storage conventions for large model files.
- Scope: biohub/esmc-600m-2024-12
- Supports: distribution
- Supports: repositoryMetadata

### biohub/esmc-600m-2024-12 commit history (commits main)

- URL: https://huggingface.co/biohub/esmc-600m-2024-12/commits/main
- Publisher: HuggingFace
- Type: `repository`
- Primary because: Commit history page for the checkpoint repository used to inspect listed commits, README updates, and config additions/changes.
- Scope: biohub/esmc-600m-2024-12
- Supports: revision
- Supports: repositoryMetadata

### Biohub/esm upstream GitHub repository

- URL: https://github.com/Biohub/esm
- Publisher: Biohub (GitHub)
- Type: `repository`
- Primary because: Canonical upstream project repository for the ESMC family; used to verify cookbook locations, README usage examples, and upstream tooling.
- Scope: ESMC family / upstream tooling
- Supports: implementation
- Supports: usage-example
- Supports: upstream-code

### Biohub/esm README (upstream repository README)

- URL: https://github.com/Biohub/esm/blob/main/README.md
- Publisher: Biohub (GitHub)
- Type: `repository`
- Primary because: Upstream README demonstrating example code that creates an ESMC client with model="esmc-600m-2024-12" and example encoding calls.
- Scope: ESMC family / upstream README
- Supports: usage-example
- Supports: implementation-example
- Supports: model-identification

### ESM cookbook — ESMC layer-sweep tutorial (Colab notebook)

- URL: https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb
- Publisher: Google Colab / Biohub
- Type: `official-documentation`
- Primary because: Official Colab tutorial demonstrating usage examples and showing model_name set to "esmc-600m-2024-12" in example notebook cells.
- Scope: ESMC family / cookbook
- Supports: usage-example
- Supports: tokenizer-retrieval-example
- Supports: implementation-example

### biohub/esmc-6b-2024-12 tokenizer.json (sibling variant artifact)

- URL: https://huggingface.co/biohub/esmc-6b-2024-12/blob/6ae7b4dd8630350e620a806d0b7ba67e53bcfd46/tokenizer.json
- Publisher: HuggingFace
- Type: `repository`
- Primary because: Tokenizer artifact observed for a sibling ESMC variant (esmc-6b-2024-12); inspected to check tokenization artifact conventions though it does not establish a tokenizer artifact for esmc-600m-2024-12.
- Scope: ESMC family / esmc-6b-2024-12 (sibling artifact)
- Supports: tokenizer-artifact-example
- Supports: artifact-format

### Exact official starting source declared by Forge

- URL: https://huggingface.co/biohub/ESMC-600M
- Publisher: HuggingFace
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official starting source for the covered serving variant in the expected scope.
- Scope: biohub/ESMC-600M (Forge starting source)
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No checkpoint-scoped tokenizer.json, vocab file, or explicit tokenizer artifact path was found for biohub/esmc-600m-2024-12 at the inspected primary URLs: https://huggingface.co/biohub/esmc-600m-2024-12 and https://huggingface.co/biohub/esmc-600m-2024-12/commits/main. (A tokenizer.json exists for the sibling variant esmc-6b at https://huggingface.co/biohub/esmc-6b-2024-12/blob/6ae7b4dd8630350e620a806d0b7ba67e53bcfd46/tokenizer.json but that file path does not establish a tokenizer artifact for esmc-600m-2024-12 at the checked locations.)
- Evidence gap: No checkpoint-scoped JSON output schema, explicit numeric embedding-dimension values, or definitive per-residue vs per-sequence output shape declaration for biohub/esmc-600m-2024-12 were found at the inspected primary URLs: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb.
- Evidence gap: No checkpoint-scoped numeric benchmark tables or figures for biohub/esmc-600m-2024-12 were found at the inspected primary URLs: https://huggingface.co/biohub/esmc-600m-2024-12 (model card root and README blobs) and https://github.com/Biohub/esm/blob/main/README.md (upstream README).
- Evidence gap: No authoritative Forge wrapper manifest or manifest-equivalent mapping was discovered in the inspected primary sources that maps hf-465f758-python312-cuda128-wrapper-20260529 to the upstream checkpoint; inspected primary URLs: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://github.com/Biohub/esm/blob/main/README.md.
- Evidence gap: The inspected primary sources do not include explicit checkpoint-scoped input-validation rules (allowed alphabet, explicit maximum sequence length) for biohub/esmc-600m-2024-12 at these locations: https://huggingface.co/biohub/esmc-600m-2024-12, https://huggingface.co/biohub/esmc-600m-2024-12/commits/main, https://github.com/Biohub/esm/blob/main/README.md.
- Evidence gap: The inspected primary sources do not provide checkpoint-scoped post-inference calibration, normalization, or downstream validation procedures for biohub/esmc-600m-2024-12 at these locations: https://huggingface.co/biohub/esmc-600m-2024-12, https://github.com/Biohub/esm/blob/main/README.md, https://colab.research.google.com/github/biohub/esm/blob/main/cookbook/tutorials/esmc_layer_sweep.ipynb.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 15 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/biohub/ESMC-600M Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://biohub.org/blog/esm-cambrian-unsupervised-learning Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'facebook' for this exact model scope: $.sources[8] uses unapproved repository owner 'facebook' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'facebookresearch' for this exact model scope: $.sources[10] uses unapproved repository owner 'facebookresearch' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/facebook/esm2_t33_650M_UR50D Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://www.youtube.com/watch?v=gAHKQmPnjao Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[5] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[5] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
