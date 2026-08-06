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

- Research key: `huggingface-co-allenai-olmo-3-7b-instruct-c0cec6c2c6`
- Independent audit: `revised`
- Researched: `2026-08-06T10:47:41.553410+00:00`

The available primary-source blobs and repository commits indicate the checkpoint named allenai/Olmo-3-7B-Instruct corresponds to an Olmo3ForCausalLM architecture (model_type "olmo3") with 32 layers, hidden_size 4096, intermediate_size 11008, 32 attention heads and 32 key/value heads, vocab_size 100278, and parameter dtype bfloat16 as reported in the checked config.json blob. The config.json contains multiple positional-related fields (max_position_embeddings = 65536; rope_scaling.original_max_position_embeddings = 8192; sliding_window = 4096) with no authoritative reconciliation provided in the checked blobs. A tokenizer.json blob exists in the repo commit inspected and defines several token IDs and token properties; other low-level tokenizer artifacts (tokenizer_config.json, vocab.json, merges) were not present in the inspected commit listing. The generation_config.json blob lists generation defaults (do_sample=true, temperature=0.6, top_p=0.95, max_new_tokens=32768 and eos_token_id entries) and a transformers_version. The repository LICENSE file states Apache License, Version 2.0; no separate model-weight license metadata was found in that LICENSE blob. The Olmo 3 family paper/preprint and associated release PDF in the findings report family-level evaluation numbers and describe family-level training/evaluation practices, but the checked model blobs and commits do not publish an immutable checkpoint manifest tying the cited commit(s) to a named release artifact; this locator immutability is not reported in the checked repository blobs. Several checkpoint-scoped items are not present in the inspected primary blobs and are recorded as evidence gaps in the dossier.

## Identity

- Upstream name: allenai/Olmo-3-7B-Instruct
- Checkpoint/version: step_450
- Immutable revision: commit d42dc9de51ee481e02b8a35d8222b86c6d7c5b20 (tokenizer commit) and related commit evidence; exact immutable artifact manifest: not reported
- Parameter scale: 7 billion parameters
- Architecture/head: Olmo3ForCausalLM (model_type: olmo3; num_hidden_layers: 32; hidden_size: 4096; intermediate_size: 11008; num_attention_heads: 32; num_key_value_heads: 32; layer_types alternate between sliding_attention and full_attention; vocab_size: 100278; dtype: bfloat16; rope_type: "yarn"; rope_theta: 500000; rope_scaling.original_max_position_embeddings: 8192; sliding_window: 4096; max_position_embeddings: 65536)
- License: Apache-2.0 (repository LICENSE: Apache License, Version 2.0). No separate model-weight license metadata reported in the checked LICENSE blob.
- Evidence: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/commit/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20, https://github.com/allenai/OLMo/blob/main/LICENSE, https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961

## Selection

### Recommended

- **Instruction-following / chat-style system+user prompts** — Family-level description of Olmo 3 Instruct behavior (instruction-following) appears in the Olmo 3 writeup/preprint and the checkpoint's generation defaults and config indicate instruction-tuned sampling defaults and a causal LM architecture consistent with instruction-following usage.
  Scope: allenai/Olmo-3-7B-Instruct (checkpoint-level)
  Evidence: https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json
- **Long-context workflows (family-level long-context support reported)** — The config.json reports extended positional-related fields (max_position_embeddings = 65536 and rope_scaling.original_max_position_embeddings = 8192 and sliding_window = 4096) and the Olmo 3 family writeup describes long-context modeling as a family target; these blobs support using the checkpoint for long-context experiments but the config fields are not authoritatively reconciled in the checked blobs.
  Scope: allenai/Olmo-3-7B-Instruct (checkpoint-level)
  Evidence: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json, https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961

### Conditional

- **Benchmarking for coding, math, or reasoning tasks** — Family-level benchmark tables and numeric results are reported in the Olmo 3 writeup/preprint, but the checked model blobs and commits do not include a binding of those numeric rows to an explicit immutable checkpoint identifier or commit-level protocol details; downstream adopters must perform protocol-matched validation tied to the specific checkpoint commit before operational adoption.
  Scope: Olmo 3 Instruct family tables reported in olmo-3.pdf / arXiv (not bound to a named immutable checkpoint in the inspected blobs)
  Evidence: https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961
- **Developers experimenting with quantized inference (8-bit/bitsandbytes)** — No load_in_8bit usage examples or bitsandbytes runtime instructions were present in the inspected blobs; if quantized loading is attempted, perform downstream integration testing and memory/correctness validation using the specific runtime and quantization toolset.
  Scope: allenai/Olmo-3-7B-Instruct (checkpoint-level)
  Evidence: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json

### Avoid

- **Safety-critical or high-stakes decision making** — Evidence gap: the inspected checkpoint-scoped blobs and commits do not contain a checkpoint-scoped upstream risk/bias mitigation statement, calibrated-probability guidance, or documented post-deployment monitoring protocol tied to this exact checkpoint commit.
  Scope: allenai/Olmo-3-7B-Instruct (checkpoint-level)
  Evidence: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json, https://kyleclo.com/assets/pdf/olmo-3.pdf

## Input preparation

### Semantic inputs

- Causal-LM text inputs, including instruction-style prompts and chat-style system/user prompting described at family-level in the Olmo 3 writeup; the checkpoint blobs reflect a causal LM architecture appropriate for single-prompt or chat-style causal input. Sources: https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json

### Accepted formats

- Model checkpoint and tokenizer blobs present are in Hugging Face repository blob format compatible with Transformers-style loading; config.json and generation_config.json are present as HF blobs for this checkpoint. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json

### Preprocessing

- The inspected repository blobs do not document a canonical string-unicode normalization or a checkpoint-scoped explicit input normalization pipeline; use standard Transformers tokenization behavior unless downstream guidance is provided. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json

### Pre-submit validation

- Evidence gap: no checkpoint-scoped input validation rules (allowed character sets, rejection criteria, per-token bounds) were found in the inspected blobs; implementers must add downstream input validation tied to their application. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json

### Task-specific formatting

- Tokenizer JSON in the inspected commit defines token IDs and token properties; no separate canonical prompt-template file for Instruct/chat was found in the inspected blobs. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json, https://kyleclo.com/assets/pdf/olmo-3.pdf
- Evidence gap: low-level tokenizer artifact files such as vocab.json, merges.txt, or tokenizer_config.json were not present in the inspected commit listing; tokenizer.json exists but separate vocab/merge blobs were not found at the checked commit. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/commit/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20

## Output interpretation

### Outputs

- Evidence gap: no inspected primary source in the provided findings defines a checkpoint-scoped model output contract file (e.g., an OLMoOutput definition) in the checked blobs; do not assume named output tuple shapes from unverified files. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json
- The generation_config.json blob lists generation-related fields (eos_token_id entries and generation defaults) and therefore documents expected sampling outputs governed by those defaults. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json

### Interpretation

- Evidence gap: the inspected checkpoint-scoped blobs do not include a checkpoint-specific statement about probability calibration or recommended post-hoc calibration procedures; interpret raw model scores conservatively and apply downstream calibration as required. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json, https://kyleclo.com/assets/pdf/olmo-3.pdf

### Post-inference validation

- Evidence gap: no checkpoint-scoped post-inference calibration checks, confidence thresholds, or token-level probability semantics were documented in the inspected blobs; downstream validation is required before using probabilities as calibrated confidences. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json

## Public benchmarks

### BBH / GPQA / MATH / GSM8K / OMEGA / CHE / MBPP / LCB / AE / IFEval (family-level Instruct benchmark table entries)

- Dataset/split: Olmo 3 Instruct benchmark table (multiple datasets: BBH, GPQA, MATH, GSM8K, OMEGA, CHE, MBPP, LCB, AE, IFEval) / not reported
- Metric/value: reported dataset-specific scores as listed in the Olmo 3 Instruct benchmark table / Multiple numeric values reported at family-level (e.g., BBH 44.5 / 47.8 with thinking SFT; GPQA 46.5 / 46.6; MATH 29.7 / 34.4; GSM8K 60.3 / 65.9; OMEGA 87.6 / 91.1; CHE 8.6 / 12.2; MBPP 63.8 / 68.7; LCB 54.1 / 57.1; AE 13.0 / 17.1; IFEval 27.0 / 27.1; overall averages 81.0 / 84.7) as reported in the Olmo 3 writeup (`context-only`)
- Model scope: family-level Olmo 3 Instruct table in olmo-3.pdf / arXiv (no explicit binding to the inspected checkpoint commit was found in the checked blobs)
- Conditions: Reported values appear in the Olmo 3 writeup/preprint benchmark table; the inspected model blobs and commits do not provide checkpoint-scoped protocol fields (exact checkpoint ID binding, dataset split, prompt template, temperature/seed) tying these numeric rows to a named immutable checkpoint in the checked repository blobs.
- Source: https://kyleclo.com/assets/pdf/olmo-3.pdf
- Locator: Olmo 3 Instruct benchmark table (table labelled in the Olmo 3 writeup / PDF); corresponding arXiv preprint section describing Instruct benchmark table
- Caveat: No checkpoint commit ID, dataset split, prompting template, temperature/seed, or exact protocol fields were found in the inspected model blobs that tie these numeric rows to the specific allenai/Olmo-3-7B-Instruct checkpoint commit.
- Caveat: Reported numbers are family-level Instruct table entries in the Olmo 3 writeup/preprint and are not verified as checkpoint-scoped in the inspected repository blobs.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: 7B instruct protocol-matched head-to-head comparisons
- Criteria: No primary, protocol-matched checkpoint-level evidence for both sides (exact checkpoint IDs, dataset/split, prompting templates, temperature/seed, and metric values) was found in the inspected blobs and writeup binding to the specific checkpoint commit.
- Rationale: Family-level benchmark tables exist in the Olmo 3 writeup, but the inspected model blobs and commits do not include the required checkpoint-scoped protocol fields to support strict head-to-head comparisons tied to the exact checkpoint commit.
- Comparison conditions: Missing explicit checkpoint identifier binding and missing protocol details in the inspected repository blobs; the writeup reports family-level results without commit-level artifact manifest in the checked blobs.
- Evidence: https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961, https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json

## Limitations and safety

### Limitations

- Ambiguity in context-window/positional-spec reporting: config.json lists max_position_embeddings = 65536 while rope_scaling.original_max_position_embeddings = 8192 and sliding_window = 4096 are also present; the inspected blobs do not provide an authoritative reconciliation of these fields. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json
- Evidence gap: low-level tokenizer artifact files (vocab.json, merges.txt/merges, tokenizer_config.json) were not present in the inspected commit listing; tokenizer metadata is present in tokenizer.json but separate vocab/merge blobs are not reported in the checked commit. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json, https://huggingface.co/allenai/Olmo-3-7B-Instruct/commit/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20
- Evidence gap: no published immutable checkpoint manifest or named release mapping the inspected commit(s) to a stable sharded model-file manifest was found in the checked repository blobs; the commit labeled 'Upload checkpoint from step_450' is present but an explicit immutable artifact manifest is not reported in the inspected blobs. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/commit/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20, https://github.com/allenai/OLMo/blob/main/LICENSE
- Evidence gap: training-data provenance at the checkpoint scope (explicit datasets, versions, and training-token counts tied to this exact checkpoint commit) is not present in the inspected blobs; family-level training-data descriptions exist in the writeup but the commit-level binding is not reported in the checked blobs. Sources: https://kyleclo.com/assets/pdf/olmo-3.pdf, https://arxiv.org/abs/2512.13961

### Safety

- Evidence gap: the inspected checkpoint-scoped blobs and commits do not include a checkpoint-scoped upstream safety/bias mitigation statement or calibrated-probability guidance; downstream deployments should require human review and mitigation steps. Sources: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json, https://kyleclo.com/assets/pdf/olmo-3.pdf
- Model-weight and code license: the checked OLMo repository LICENSE file indicates Apache License, Version 2.0. The inspected LICENSE blob does not provide a separate model-weight licensing statement. Sources: https://github.com/allenai/OLMo/blob/main/LICENSE

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### allenai/Olmo-3-7B-Instruct config.json (blob)

- URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json
- Publisher: Hugging Face (allenai model repository blob)
- Type: `model-card`
- Primary because: Repository config JSON contains architecture fields, positional/rope parameters, vocab_size, token ids, layer counts, and other checkpoint-level configuration parameters used to verify architecture and tokenizer metadata for this checkpoint.
- Scope: allenai/Olmo-3-7B-Instruct (checkpoint config)
- Supports: Architecture: Olmo3ForCausalLM and model_type olmo3
- Supports: num_hidden_layers, hidden_size, intermediate_size, num_attention_heads, num_key_value_heads
- Supports: max_position_embeddings, rope_scaling object, rope_theta, sliding_window, vocab_size, eos_token_id, pad_token_id, dtype

### allenai/Olmo-3-7B-Instruct generation_config.json (blob blame view)

- URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blame/096bb5469fe34348bc88d851a69edb3bf6f40df4/generation_config.json
- Publisher: Hugging Face (allenai model repository blob)
- Type: `model-card`
- Primary because: Repository generation_config JSON lists checkpoint-scoped generation defaults used to verify sampling/decoding default claims.
- Scope: allenai/Olmo-3-7B-Instruct (generation defaults)
- Supports: do_sample = true; temperature = 0.6; top_p = 0.95; max_new_tokens = 32768; eos_token_id entries; transformers_version

### allenai/Olmo-3-7B-Instruct tokenizer.json (blob)

- URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json
- Publisher: Hugging Face (allenai model repository blob)
- Type: `model-card`
- Primary because: Tokenizer JSON blob in the inspected commit defines token IDs and tokenizer properties for the checked checkpoint commit; used to verify presence of tokenizer.json and token id entries.
- Scope: allenai/Olmo-3-7B-Instruct (tokenizer blob at checked commit)
- Supports: Presence of tokenizer.json; token definitions for token IDs including special tokens; add_prefix_space setting

### allenai/Olmo-3-7B-Instruct commit: tokenizer commit (Upload checkpoint / tokenizer commit)

- URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct/commit/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20
- Publisher: Hugging Face (allenai model repository commits)
- Type: `model-card`
- Primary because: Commit in the model repository used to locate the tokenizer.json blob and to record the presence of the commit-level upload event inspected.
- Scope: allenai/Olmo-3-7B-Instruct (checked commit)
- Supports: Tokenizer.json definitions at that commit

### OLMo repository LICENSE (Apache-2.0)

- URL: https://github.com/allenai/OLMo/blob/main/LICENSE
- Publisher: Allen Institute for AI (GitHub repository)
- Type: `repository`
- Primary because: Official repository LICENSE file indicating Apache License, Version 2.0 for the OLMo project in the inspected findings.
- Scope: OLMo project repository (license)
- Supports: Apache-2.0 license statement for the repository

### Olmo 3 writeup / release PDF

- URL: https://kyleclo.com/assets/pdf/olmo-3.pdf
- Publisher: Olmo 3 writeup (distribution PDF as provided in findings)
- Type: `technical-report`
- Primary because: Document in the provided findings that contains family-level descriptions of Olmo 3, training recipes, and the Instruct benchmark table used by this dossier to represent family-level benchmark claims.
- Scope: Olmo 3 family (writeup / release PDF)
- Supports: Family-level training-data composition, evaluation suite, and Instruct benchmark table numeric entries

### Olmo 3 arXiv preprint

- URL: https://arxiv.org/abs/2512.13961
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical arXiv preprint entry for the Olmo 3 writeup included in the provided findings; used to corroborate family-level claims and benchmark table presence.
- Scope: Olmo 3 family (preprint)
- Supports: Family-level description and benchmark table references

### Exact official starting source declared by Forge

- URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: allenai-olmo-3-7b-instruct
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- No checkpoint-scoped published immutable artifact manifest or named release mapping the inspected commit(s) to stable model-file shards was found in the checked repository blobs (checked URLs: https://huggingface.co/allenai/Olmo-3-7B-Instruct/commit/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20 ; https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json).
- Canonical low-level tokenizer artifact files (vocab.json, merges.txt/merges, tokenizer_config.json) for allenai/Olmo-3-7B-Instruct were not present in the inspected commit listing (checked URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json and the associated commit).
- No authoritative reconciliation of positional/context-window semantics for the checkpoint was found in the inspected blobs: config.json contains max_position_embeddings=65536 plus rope_scaling.original_max_position_embeddings=8192 and sliding_window=4096 but no upstream blob in the checked commits reconciles these fields (checked URL: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json).
- No checkpoint-scoped training-data provenance (explicit dataset lists, versions, and training-token counts tied to this exact checkpoint commit) was present in the inspected blobs; family-level training descriptions exist in the writeup but not checkpoint-level provenance in the checked blobs (checked URLs: https://kyleclo.com/assets/pdf/olmo-3.pdf ; https://arxiv.org/abs/2512.13961 ; https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json).
- No checkpoint-scoped numeric benchmark rows with explicit checkpoint identifier, dataset split, prompt template, temperature/seed, and protocol were found in the inspected model blobs; family-level numeric rows exist in the writeup but are not bound to the checked commit (checked URLs: https://kyleclo.com/assets/pdf/olmo-3.pdf ; https://arxiv.org/abs/2512.13961 ; https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json).
- No checkpoint-scoped safety/bias mitigation statements or calibrated-probability guidance were found in the inspected blobs (checked URLs: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json ; https://kyleclo.com/assets/pdf/olmo-3.pdf).
- No inspected primary-source mapping was found that ties a Forge-serving vLLM/CUDA13 wrapper or other runtime packaging to an unchanged identical upstream checkpoint manifest in the checked blobs (checked URLs: https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/096bb5469fe34348bc88d851a69edb3bf6f40df4/config.json ; https://huggingface.co/allenai/Olmo-3-7B-Instruct/blob/d42dc9de51ee481e02b8a35d8222b86c6d7c5b20/tokenizer.json).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[3] uses unapproved repository owner 'unsloth' for this exact model scope: $.sources[3] uses unapproved repository owner 'unsloth' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://huggingface.co/allenai/Olmo-3-7B-Instruct/discussions/14/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary host benchmarklist.com: $.sources[9] uses forbidden secondary host benchmarklist.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/allenai/Olmo-3-7B-Instruct: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
