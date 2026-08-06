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

- Research key: `huggingface-co-allenai-olmo-2-1124-7b-instruct-aa6456fc5a`
- Independent audit: `revised`
- Researched: `2026-08-06T10:56:02.773754+00:00`

Prioritize verifying the Hugging Face model card and repository files for this exact checkpoint first: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct (model card and Files view), the checkpoint config at https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json, and the generation config at https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/generation_config.json. Also consult the repository tree view at https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main and the canonical family preprint at https://arxiv.org/abs/2501.00656 and the family GitHub repo at https://github.com/allenai/olmo for family-level context. Verified checkpoint-scoped artifacts found in these primary sources: config.json reports architecture name "Olmo2ForCausalLM" and numeric configuration fields (see identity.evidenceUrls); generation_config.json repeats EOS/PAD token IDs and records a transformers-version marker. Important verification steps/files to open first (as indicated by the primary sources): config.json, generation_config.json, the Files/tree listing on the Hugging Face model page, and the canonical arXiv preprint and GitHub repository for family-level training/fine-tuning descriptions. The checked primary sources do not provide an immutable release SHA for the exact checkpoint, an explicit code-vs-weights license distinction for this checkpoint, a checkpoint-scoped tokenizer artifact listing, nor a checkpoint-scoped numeric benchmark table; those are recorded as evidence gaps below. Do not rely on secondary blog posts, mirrors, or aggregators for checkpoint-scoped numeric or license claims.

## Identity

- Upstream name: allenai/OLMo-2-1124-7B-Instruct
- Checkpoint/version: OLMo-2-1124-7B-Instruct
- Immutable revision: Evidence gap: No immutable revision or release commit SHA for the exact checkpoint was found in the checked primary sources.
- Parameter scale: Evidence gap: Parameter count (e.g., "7 billion") not verified in the available primary sources.
- Architecture/head: Olmo2ForCausalLM (architecture name as reported in config.json)
- License: Evidence gap: No separately verified code-license versus model-weights license distinction for the exact checkpoint found in the checked primary sources.
- Evidence: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/generation_config.json, https://arxiv.org/abs/2501.00656, https://github.com/allenai/olmo, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main

## Selection

### Recommended

- **English instruction-following and chat-style text generation** — The Hugging Face model card for the exact checkpoint names this model among the family final instruction-tuned (RLVR) checkpoints and the model page provides usage instructions; the family-level preprint and repository provide contextual evidence that the family includes instruction-finetuned checkpoints.
  Scope: allenai/OLMo-2-1124-7B-Instruct upstream checkpoint
  Evidence: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://arxiv.org/abs/2501.00656, https://github.com/allenai/olmo

### Conditional

- **Downstream benchmark-style evaluation (e.g., MATH, GSM8K, IFEval) and trust-sensitive reasoning tasks** — Require task-specific validation using the exact allenai/OLMo-2-1124-7B-Instruct checkpoint and the exact dataset/split because the checked primary sources do not present a verified numeric benchmark row for this exact checkpoint; validate protocol, prompting, and any downstream heads used for evaluation.
  Scope: allenai/OLMo-2-1124-7B-Instruct upstream checkpoint (family-level evidence may exist in the paper but exact-checkpoint numeric rows were not found in the checked primary sources)
  Evidence: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://arxiv.org/abs/2501.00656

### Avoid

- **Any workflow that requires inputs longer than the documented context window without truncation or chunking** — The official checkpoint config.json documents max_position_embeddings = 4096, which constrains single-sequence input length for this exact checkpoint.
  Scope: allenai/OLMo-2-1124-7B-Instruct upstream checkpoint
  Evidence: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json
- **High-stakes decisions made from the model output without downstream validation** — Evidence gap: The checked primary sources do not report calibrated confidence semantics, a certified decision-use policy, or a documented post-output validation pipeline for this exact checkpoint.
  Scope: allenai/OLMo-2-1124-7B-Instruct upstream checkpoint
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- The checkpoint is presented and documented on the Hugging Face model page as an instruction-tuned family checkpoint intended for English natural-language text use (family-level instruction tuning is described on the model page and in the family preprint/repository). Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://arxiv.org/abs/2501.00656, https://github.com/allenai/olmo
- The model configuration (config.json) identifies the architecture name used by the checkpoint (Olmo2ForCausalLM), indicating causal-language modeling-related input framing in the checkpoint metadata. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json

### Accepted formats

- Accepted upstream input format is tokenized text as presented on the Hugging Face model page and usage instructions; the model card provides usage instructions for Transformers and other runtimes. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main
- Evidence gap: The checked primary sources do not provide a checkpoint-scoped tokenizer artifact listing or an explicit tokenizer algorithm/type for this exact Instruct checkpoint.

### Preprocessing

- Respect the checkpoint special token IDs as reported in official files: eos_token_id = 100257 and pad_token_id = 100277 (reported in both config.json and generation_config.json). Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/generation_config.json
- Prepare inputs within the documented max_position_embeddings limit of 4096 tokens as reported in the checkpoint config.json. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json

### Pre-submit validation

- Validate that any prepared sequence length does not exceed 4096 tokens (documented max_position_embeddings in the checkpoint config.json). Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json
- Evidence gap: The checked primary sources do not provide additional official input rejection rules, language filters, or schema constraints specific to this exact checkpoint.

### Task-specific formatting

- Evidence gap: The checked primary sources do not provide a verified official prompt template or canonical chat/role tag format for this exact checkpoint (no checkpoint-scoped prompt/chat templates found in the checked primary sources). Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct

## Output interpretation

### Outputs

- The checkpoint configuration names the architecture Olmo2ForCausalLM and the Hugging Face model card lists this checkpoint as an instruction-tuned family member; interpret outputs as instruction-following continuations produced by the named ForCausalLM checkpoint metadata. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct
- Generation-related files report eos_token_id = 100257 and pad_token_id = 100277 for the exact checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/generation_config.json, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json

### Interpretation

- Interpret generated text conservatively; do not assume outputs are calibrated probabilities or authoritative facts without downstream validation using the exact checkpoint and dataset. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct
- Evidence gap: The checked primary sources do not report an official low-level output contract (e.g., explicit documented access or guarantees for logits, hidden states, or token-level confidence scores) for this exact checkpoint.

### Post-inference validation

- Forge policy: Post-inference checks and human review are required for high-stakes or regulated outputs; do not rely on undocumented calibration or factuality guarantees from the upstream checkpoint.
- Evidence gap: The checked primary sources do not provide a checkpoint-specific post-output validation checklist for hallucination detection, confidence thresholding, or safety review. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Evidence gap: No immutable release revision or commit SHA for the exact allenai/OLMo-2-1124-7B-Instruct checkpoint was found in the checked primary sources. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main
- Evidence gap: The checked primary sources do not provide an explicit code-license versus model-weights license distinction for this exact checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main
- The checkpoint config documents max_position_embeddings = 4096, constraining single-sequence input length for this exact checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json
- Evidence gap: The checked primary sources do not include a checkpoint-specific tokenizer artifact listing or explicit tokenizer algorithm/type for this exact checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct
- Evidence gap: No checkpoint-scoped numeric benchmark table or verified benchmark row for allenai/OLMo-2-1124-7B-Instruct was found in the checked primary sources; family-level paper includes results for other scales but not a verified 7B checkpoint row in the checked sources. Sources: https://arxiv.org/abs/2501.00656, https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct

### Safety

- Forge policy: Do not use this checkpoint as the sole basis for medical, legal, regulatory, or other high-stakes decisions without qualified human review and downstream validation.
- Evidence gap: The checked primary sources do not report checkpoint-specific PHI handling guidance, clinical certification, or regulated-use authorization for this exact checkpoint. Sources: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct, https://arxiv.org/abs/2501.00656

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### allenai/OLMo-2-1124-7B-Instruct

- URL: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct
- Publisher: Allen Institute for AI via Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card and Files/tree view for the exact named checkpoint; authoritative for checkpoint naming, usage instructions, and Files listing.
- Scope: allenai/OLMo-2-1124-7B-Instruct upstream checkpoint
- Supports: identity.upstreamName
- Supports: identity.checkpoint
- Supports: recommendedUseCases
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.semanticInputs
- Supports: researchSummary
- Supports: outputInterpretation.outputs
- Supports: limitations

### allenai/OLMo-2-1124-7B-Instruct config.json

- URL: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json
- Publisher: Allen Institute for AI via Hugging Face
- Type: `repository`
- Primary because: Official checkpoint configuration file; authoritative for architecture name and numeric configuration fields such as hidden_size, intermediate_size, num_attention_heads, num_hidden_layers, num_key_value_heads, max_position_embeddings, rope_theta, eos_token_id, pad_token_id, and torch_dtype when present in the file.
- Scope: allenai/OLMo-2-1124-7B-Instruct upstream checkpoint config
- Supports: identity.architecture
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: outputInterpretation.outputs
- Supports: avoidUseCases
- Supports: limitations

### allenai/OLMo-2-1124-7B-Instruct generation_config.json

- URL: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/generation_config.json
- Publisher: Allen Institute for AI via Hugging Face
- Type: `repository`
- Primary because: Official generation configuration file for the exact checkpoint; authoritative for reported eos_token_id, pad_token_id, and transformers_version metadata when present.
- Scope: allenai/OLMo-2-1124-7B-Instruct generation config
- Supports: outputInterpretation.outputs
- Supports: inputPreparation.preprocessing
- Supports: identity.evidenceUrls

### allenai/OLMo-2-1124-7B-Instruct Files/tree view

- URL: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main
- Publisher: Allen Institute for AI via Hugging Face
- Type: `repository`
- Primary because: Files/tree listing on the official Hugging Face model card; authoritative for which artifacts (config, generation_config, tokenizers, quantized files) are present in the model's repository view.
- Scope: allenai/OLMo-2-1124-7B-Instruct repository tree
- Supports: inputPreparation.acceptedFormats
- Supports: limitations
- Supports: researchSummary

### OLMo 2 family preprint (arXiv:2501.00656)

- URL: https://arxiv.org/abs/2501.00656
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical family-level preprint describing the OLMo 2 family; authoritative for family-level descriptions and reported results in the paper (note: the preprint includes results for larger scales and does not provide a verified numeric row for the exact 7B Instruct checkpoint in the checked sources).
- Scope: OLMo 2 family
- Supports: conditionalUseCases
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: limitations

### OLMo GitHub repository

- URL: https://github.com/allenai/olmo
- Publisher: Allen Institute for AI (GitHub)
- Type: `repository`
- Primary because: Official family GitHub repository referenced by the family preprint; authoritative for family-level training and fine-tuning descriptions and for linking the canonical paper.
- Scope: OLMo family repository
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: conditionalUseCases

### OLMo-2-1124-7B-Instruct-GGUF commit e9ecde1c0cea4924e409a5426196cf5d9e7cd09e

- URL: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct-GGUF/commit/e9ecde1c0cea4924e409a5426196cf5d9e7cd09e
- Publisher: Allen Institute for AI via Hugging Face
- Type: `repository`
- Primary because: Primary artifact listing for a quantized GGUF file produced for the 7B-Instruct checkpoint; authoritative for the specific uploaded quantized file metadata (size and SHA256) in that GGUF repository view.
- Scope: allenai/OLMo-2-1124-7B-Instruct-GGUF artifacts
- Supports: researchSummary

### OLMo-2-1124-7B-Instruct-GGUF commit caedbd2dcb1a9aa5ee9450a091c5db5632aebccb

- URL: https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct-GGUF/commit/caedbd2dcb1a9aa5ee9450a091c5db5632aebccb
- Publisher: Allen Institute for AI via Hugging Face
- Type: `repository`
- Primary because: Primary artifact listing for an alternate quantized GGUF file produced for the 7B-Instruct checkpoint; authoritative for the specific uploaded quantized file metadata (size and SHA256) in that GGUF repository view.
- Scope: allenai/OLMo-2-1124-7B-Instruct-GGUF artifacts
- Supports: researchSummary

## Evidence gaps

- Evidence gap: No immutable revision or release commit SHA for allenai/OLMo-2-1124-7B-Instruct was found in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main).
- Evidence gap: No separately verified code-license versus model-weights license distinction for the exact checkpoint was reported in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main).
- Evidence gap: The checked primary sources do not provide a verified official prompt template or canonical chat/role tag format for this exact checkpoint (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct).
- Evidence gap: The checked primary sources do not include a checkpoint-specific tokenizer artifact listing or explicit tokenizer algorithm/type for this exact checkpoint (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main).
- Evidence gap: No checkpoint-scoped numeric benchmark table or verified benchmark row for allenai/OLMo-2-1124-7B-Instruct was found in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://arxiv.org/abs/2501.00656).
- Evidence gap: No task- and protocol-matched primary comparison set for this exact checkpoint was reported in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://arxiv.org/abs/2501.00656).
- Evidence gap: The checked primary sources do not report an official low-level output contract for access to logits, hidden states, or calibrated confidence scores for this exact checkpoint (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/config.json).
- Evidence gap: The checked primary sources do not report checkpoint-specific PHI handling guidance, clinical certification, or regulated-use authorization for this exact checkpoint (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://arxiv.org/abs/2501.00656).
- Evidence gap: Parameter count (numeric parameterScale) for the exact checkpoint was not verified from the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main).
- Evidence gap: No checkpoint-scoped tokenizer files were found in the checked primary repository Files/tree listing; if tokenizer files are present in another path or external repo, they were not discovered in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/tree/main).
- Evidence gap: No explicit transformers library runtime compatibility guarantees beyond a recorded transformers version marker in generation_config.json were verified for the exact checkpoint (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct/blob/main/generation_config.json).
- Evidence gap: No checkpoint-scoped official prompt/chat templates or canonical role tags were found in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct).
- Evidence gap: No checkpoint-scoped, source-authoritative numeric benchmarks suitable for direct comparison were found; verify before relying on performance claims (checked https://arxiv.org/abs/2501.00656 and https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct).
- Evidence gap: No primary-source task- and protocol-matched comparisons for this exact checkpoint were found in the checked primary sources (checked https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct and https://arxiv.org/abs/2501.00656).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[1] uses forbidden secondary URL https: $.sources[1] uses forbidden secondary URL https://allenai.org/blog/olmo2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'itlwas' for this exact model scope: $.sources[6] uses unapproved repository owner 'itlwas' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'mistralai' for this exact model scope: $.sources[8] uses unapproved repository owner 'mistralai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
