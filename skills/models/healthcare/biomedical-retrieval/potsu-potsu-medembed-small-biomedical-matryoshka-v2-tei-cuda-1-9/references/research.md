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

- Research key: `huggingface-co-potsu-potsu-medembed-small-biomedical-matryoshka-v2-8730ebfc38`
- Independent audit: `revised`
- Researched: `2026-08-06T13:26:50.295182+00:00`

Primary verified facts come from the model repository file at https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json. That file contains a top-level "__version__" key whose entries include sentence_transformers = "4.1.0", transformers = "4.52.4", and pytorch = "2.6.0+cu124"; it contains a top-level key "prompts" with an empty object; it contains a top-level key "default_prompt_name" with a null value; and it contains a top-level key "similarity_fn_name" with the value "cosine". The checked primary source does not provide checkpoint-scoped numeric benchmarks, tokenizer metadata (tokenizer type, vocab/merges, or max token length), embedding dimensionality, is_matryoshka or matryoshka_dimensions keys, checkpoint revision identifier, parameter count, or model-weight license text in that file (these items were not present in the checked config file).

## Identity

- Upstream name: not reported
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: not reported
- License: not reported
- Evidence: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

## Selection

### Recommended

- **Extract dense text embeddings for cosine-based semantic similarity or retrieval** — The checked checkpoint configuration file sets similarity_fn_name = "cosine", indicating embeddings are intended for cosine-similarity comparisons as recorded in the model config file.
  Scope: checked source file: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
  Evidence: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Conditional

- **Adjustable-dimension (Matryoshka) embeddings via runtime dimension overrides** — Only applicable if the upstream checkpoint's configuration explicitly declares Matryoshka support (for example an explicit is_matryoshka boolean or a matryoshka_dimensions list) in the checkpoint files; such an explicit key or list must be present for this checkpoint before assuming adjustable output dimensions.
  Scope: checked source file: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
  Evidence: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Avoid

- **Direct use for clinical decision-making, diagnosis, or other high-stakes clinical automation without expert review** — The checked primary-source configuration file contains only model configuration metadata (library-version requirements, similarity function, empty prompts) and does not provide checkpoint-scoped certification, clinical-use claims, PHI-handling guidance, or clinical benchmarks in the inspected file.
  Scope: checked source file: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
  Evidence: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

## Input preparation

### Semantic inputs

- Evidence gap: The checked config file does not explicitly declare the accepted input formats (for example plain text, tokenized inputs, or paired-input formats); confirm accepted input formats in repository files or model card. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Accepted formats

- Evidence gap: The checked config file does not report tokenizer type, vocabulary/merges files, SentencePiece model, or max token length; tokenizer identity and accepted input encoding must be confirmed from repository tokenizer files. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Preprocessing

- The checked config file contains an explicit __version__ block that records required library versions which can affect preprocessing and tokenization behavior: sentence_transformers = "4.1.0", transformers = "4.52.4", pytorch = "2.6.0+cu124". Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
- Evidence gap: The checked config file does not specify tokenization rules, truncation behavior, or tokenizers' max_length; confirm tokenization/truncation semantics from tokenizer files in the repository. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Pre-submit validation

- Evidence gap: The checked config file does not provide input validation rules (bounds, prohibited content, or PHI handling guidance); add validation checks and governance controls before production use. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Task-specific formatting

- Evidence gap: The checked config file contains no prompt templates, and default_prompt_name is null and prompts is an empty object; there is no upstream-provided prompt/template guidance in the inspected file. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

## Output interpretation

### Outputs

- The checked configuration sets similarity_fn_name = "cosine", indicating the intended similarity metric for embedding outputs in this config file is cosine similarity. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Interpretation

- Use cosine similarity to compare embeddings when following the checkpoint's configured similarity function as recorded in the config file. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
- Evidence gap: The checked config file does not state whether embeddings are L2-normalized by default, nor does it provide calibration or reliability statistics for embeddings; downstream calibration and validation are required for risk-sensitive applications. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Post-inference validation

- Evidence gap: The checked config file does not report output dimensionality or dtype defaults for embeddings; confirm returned vector dimensionality and numeric dtype from the model weights or serving metadata before downstream use. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Evidence gap: No checkpoint-scoped numeric benchmark data were found to enable a primary-evidence comparison versus alternative checkpoints.
- Criteria: No comparable numeric benchmarks in the inspected primary source file.
- Rationale: The inspected config file contains configuration metadata only and no numeric evaluation results to support task- or dataset-specific comparisons.
- Comparison conditions: Checked file: config_sentence_transformers.json; no benchmark tables/rows present.
- Evidence: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

## Limitations and safety

### Limitations

- The checked config file declares required library versions in a __version__ block: sentence_transformers = "4.1.0", transformers = "4.52.4", pytorch = "2.6.0+cu124"; mismatching runtime libraries may cause incompatibilities. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
- The checked config file contains similarity_fn_name = "cosine" and contains no prompt templates (prompts is an empty object and default_prompt_name is null). Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
- Evidence gap: The inspected primary-source file does not provide tokenizer metadata (tokenizer type, vocab/merges, or max token length); tokenizer identity and tokenization constraints must be confirmed from repository tokenizer files. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
- Evidence gap: The inspected primary-source file does not report embedding dimensionality, checkpoint revision identifier, parameter count, or model-weight license text for this specific checkpoint. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

### Safety

- Evidence gap: The inspected configuration file does not contain explicit clinical-use claims, PHI handling guidance, or certified clinical suitability statements; do not assume suitability for clinical decision-making without independent validation and expert review. Sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### config_sentence_transformers.json (potsu-potsu/medembed-small-biomedical-matryoshka-v2)

- URL: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Official model repository configuration file containing the checkpoint's sentence-transformers configuration keys and values as inspected.
- Scope: config_sentence_transformers.json in potsu-potsu/medembed-small-biomedical-matryoshka-v2 repository (file-level)
- Supports: The config_sentence_transformers.json file contains a top-level key "__version__".
- Supports: Within "__version__", the key "sentence_transformers" has the value "4.1.0".
- Supports: Within "__version__", the key "transformers" has the value "4.52.4".
- Supports: Within "__version__", the key "pytorch" has the value "2.6.0+cu124".
- Supports: The config file includes a top-level key "prompts" with an empty object as its value.
- Supports: The config file includes a top-level key "default_prompt_name" with a null value.
- Supports: The config file includes a top-level key "similarity_fn_name" with the value "cosine".

### Exact official starting source declared by Forge

- URL: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: potsu-potsu-medembed-small-biomedical-matryoshka
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No numeric benchmark results (datasets, splits, metrics, or values) for potsu-potsu/medembed-small-biomedical-matryoshka-v2 were found in the checked primary-source file: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json (file: config_sentence_transformers.json — no Evaluation section or benchmark table rows present).
- Evidence gap: The checkpoint's tokenizer metadata (tokenizer type, vocabulary files, merges, or max token length) is not reported in the checked config file: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json (file: config_sentence_transformers.json).
- Evidence gap: The embedding dimensionality (vector size) for this checkpoint is not reported in the checked config file: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json (file: config_sentence_transformers.json).
- Evidence gap: No explicit is_matryoshka flag or matryoshka_dimensions list was found in the checked config file; Matryoshka support for this checkpoint is therefore unconfirmed: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json (file: config_sentence_transformers.json).
- Evidence gap: The checkpoint's revision identifier, parameter count, and model-weight license text are not reported in the checked config file and must be obtained from upstream model page metadata or repository files: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json (file: config_sentence_transformers.json).
- Evidence gap: No checkpoint-scoped numeric benchmark or evaluation data were found to enable evidence-backed task-specific comparisons versus alternative checkpoints; additional primary-source benchmark data are required. Checked path: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2/blob/main/config_sentence_transformers.json (file: config_sentence_transformers.json).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 7 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses forbidden secondary host docs.vllm.ai: $.sources[3] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses forbidden secondary URL https: $.sources[4] uses forbidden secondary URL https://ashraf-bhuiyan.com/blog/embed-03-serving Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'blog' for this exact model scope: $.sources[5] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://huggingface.co/blog/matryoshka Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary host docs.vllm.ai: $.sources[6] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/potsu-potsu/medembed-small-biomedical-matryoshka-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
