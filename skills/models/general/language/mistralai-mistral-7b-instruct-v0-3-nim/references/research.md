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

- Research key: `build-nvidia-com-mistralai-mistral-7b-instruct-v0-3-7fdb5ba9c3`
- Independent audit: `revised`
- Researched: `2026-07-23T21:10:06.221491+00:00`

I verified the upstream checkpoint identity and repository artifacts for Mistral-7B-Instruct-v0.3 from the official Hugging Face model page and repository blobs (config.json, tokenizer.json, README) and inspected NVIDIA NGC/NGC catalog entries and the NVIDIA NIM reference page. Upstream-checkpoint evidence (Hugging Face model page and config blobs) lists architecture fields consistent with a MistralForCausalLM Transformer (hidden_size 4096, num_hidden_layers 32, num_attention_heads 32, vocab_size 32768, max_position_embeddings 32768) and the model card/README provide usage examples and note absence of built-in moderation. NVIDIA NGC catalog entries document quantized ONNX-INT4 and NeMo/TensorRT-LLM variants derived from the upstream checkpoint and describe a conversion workflow (download HF PyTorch bfloat16 model -> convert to ONNX FP16 -> quantize to INT4 via TensorRT Model Optimizer). I found no primary-source mapping (commit, checksum, or explicit locator) in the inspected NVIDIA or upstream blobs that ties the Forge serving slug/tag "7fdb5ba9c3" to an exact upstream commit or release artifact; this mapping is therefore an evidence gap. I also did not find primary-source numeric benchmark tables or explicit calibration/confidence semantics in the inspected upstream or NVIDIA blobs. Where repository discussions were observed in research notes, I did not use discussion threads as primary evidence; when a claim depended only on a discussion (for example, explicit chat-template JSON content), I recorded an evidence gap and cited the upstream repository blobs and commits that were inspected.

## Identity

- Upstream name: Mistral-7B-Instruct-v0.3
- Checkpoint/version: Mistral-7B-Instruct-v0.3
- Immutable revision: not reported
- Parameter scale: 7B
- Architecture/head: MistralForCausalLM (Transformer)
- License: Apache-2.0
- Evidence: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/config.json, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/adadfb3fbae87ecc77cd5bf2c3318434d5da04cf/config.json, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/main/tokenizer.json, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b8ef225287903940a8fcc1f6e1016b29c5cc01f3

## Selection

### Recommended

- **Instruction-following text tasks (general QA, summarization, instruction-following dialogue)** — Upstream model card and README describe Mistral-7B-Instruct-v0.3 as an instruct-fine-tuned variant and provide examples demonstrating instruction-following and chat usage.
  Scope: Mistral-7B-Instruct-v0.3 upstream checkpoint
  Evidence: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

### Conditional

- **Safety-sensitive or high-stakes decision support (clinical, legal, safety-critical) only after additional downstream validation and human/expert oversight** — Requires external moderation/guardrails, domain-specific expert review, and validation because the upstream checkpoint README and model card indicate absence of built-in moderation mechanisms.
  Scope: Mistral-7B-Instruct-v0.3 upstream checkpoint
  Evidence: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

### Avoid

- **Deploying as an autonomous safety- or clinical-decision-maker without human/expert oversight** — Upstream README and model-card explicitly state the model does not include built-in moderation mechanisms and recommend applying external guardrails before high-stakes use.
  Scope: Mistral-7B-Instruct-v0.3 upstream checkpoint
  Evidence: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

## Input preparation

### Semantic inputs

- Primary input type is natural-language text prompts for instruction-following/chat usage. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

### Accepted formats

- Evidence gap: the inspected primary sources do not provide an explicit, single-line specification labeled 'accepted input formats' (for example, a formal statement such as 'inputs must be provided as a 1-D string tensor of token ids' was not found in the checked model-card blobs and NVIDIA pages). Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md, https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03

### Preprocessing

- Tokenizer assets (tokenizer.json) are present in the upstream repository indicating the canonical tokenizer is published alongside model files; repository commits reference tokenizer uploads. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/main/tokenizer.json, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b8ef225287903940a8fcc1f6e1016b29c5cc01f3

### Pre-submit validation

- Evidence gap: the inspected primary sources do not include a formal input-validation checklist (bounds, prohibited content filtering rules, or exact tokenization failure modes) for submission to the checkpoint; the model README and card instead note the absence of moderation and recommend external guardrails. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

### Task-specific formatting

- Evidence gap: I did not find an upstream commit blob or README fragment that contains the canonical chat-template JSON for this checkpoint; repository commits reference chat-template/tool-calling updates but the explicit template JSON content was only observed in discussion threads (which are treated as secondary and excluded). Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b0693ea4ce84f1a6a70ee5ac7c8efb0df82875f6, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

## Output interpretation

### Outputs

- Model emits natural-language text strings as its primary output; the README and model card provide example generation and chat CLI usage. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md

### Interpretation

- Evidence gap: the inspected primary sources do not provide explicit statements about calibrated confidence scores, per-token probability semantics, or recommended numeric score interpretation for generated tokens/outputs. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/config.json

### Post-inference validation

- Post-inference validation: repository README and model-card guidance recommend applying external QA and moderation given absence of built-in moderation mechanisms; users should apply domain-appropriate validation pipelines. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: checkpoint-specific numeric or protocol-matched comparisons
- Criteria: No primary, checkpoint-scoped comparative benchmark rows or protocol-matched evaluations were found naming Mistral-7B-Instruct-v0.3; comparisons in secondary sources were excluded.
- Rationale: I inspected the upstream model card, README blobs, config blobs, and NVIDIA NGC/NGC listings for any task- and protocol-matched comparisons naming this exact checkpoint and found none in primary artifacts. Therefore there is insufficient primary evidence to prefer this checkpoint versus an alternative under a specific protocol.
- Comparison conditions: Inspected canonical upstream model card, repository blobs (config/README), and NVIDIA NGC catalog pages; no checkpoint-specific comparative benchmark tables or protocol statements were found.
- Evidence: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/config.json, https://catalog.ngc.nvidia.com/orgs/nvidia/models/mistral-7b-instruct-v0.3-onnx-int4-rtx

## Limitations and safety

### Limitations

- The upstream checkpoint does not include built-in moderation mechanisms; authors/repository recommend external guardrails. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md
- Vocabulary size and maximum position embeddings as specified in upstream config blobs indicate a vocab_size of 32768 and max_position_embeddings of 32768 for this checkpoint. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/config.json, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/adadfb3fbae87ecc77cd5bf2c3318434d5da04cf/config.json
- Evidence gap: No primary-source mapping was found in the inspected NVIDIA or upstream repository blobs that ties the Forge serving slug/tag '7fdb5ba9c3' to an exact upstream commit ID or release artifact. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b8ef225287903940a8fcc1f6e1016b29c5cc01f3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b0693ea4ce84f1a6a70ee5ac7c8efb0df82875f6, https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03

### Safety

- The upstream checkpoint does not include built-in moderation; external moderation/guardrails are advised for deployments. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md
- Evidence gap: No primary-source statement was found in the inspected upstream blobs or NVIDIA pages that provides formal guidance on clinical/medical safety validation or specific data-handling procedures for regulated data when using this checkpoint; users should assume external procedures are required. Sources: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NIM reference: Mistralai Mistral-7B-Instruct-v0.3

- URL: https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM reference page listing the Mistral-7B-Instruct-v0.3 serving entry and describing the model as provided via NVIDIA NIM/serving.
- Scope: NVIDIA NIM / serving listing for Mistral-7B-Instruct-v0.3
- Supports: Forge/NIM serving listing
- Supports: high-level model description (instruction-following)

### Hugging Face model page: mistralai/Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
- Publisher: Mistral AI / Hugging Face model hub
- Type: `model-card`
- Primary because: Official upstream model card / repository landing page for the checkpoint; contains README, license declaration, and usage examples.
- Scope: Mistral-7B-Instruct-v0.3 upstream checkpoint
- Supports: model-card metadata
- Supports: usage examples
- Supports: license declaration

### README.md blob (commit b8ef2252...) for Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md
- Publisher: Mistral AI / Hugging Face model repository
- Type: `repository`
- Primary because: Repository README blob at a named commit containing usage examples, mistral_inference guidance, and safety/guardrail commentary for this exact checkpoint.
- Scope: Mistral-7B-Instruct-v0.3 upstream checkpoint (README blob)
- Supports: usage examples (mistral_inference, mistral-chat)
- Supports: notes on moderation and guardrails
- Supports: snapshot_download allow_patterns claims

### tokenizer.json blob (main) for Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/main/tokenizer.json
- Publisher: Mistral AI / Hugging Face model repository
- Type: `repository`
- Primary because: Concrete tokenizer asset in the upstream model repository; file-level metadata in the blob indicates licensing and presence of tokenizer artifacts.
- Scope: Mistral-7B-Instruct-v0.3 tokenizer assets
- Supports: tokenizer asset presence
- Supports: tokenizer licensing note

### config.json blob (commit b8ef2252...) for Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/config.json
- Publisher: Mistral AI / Hugging Face model repository
- Type: `repository`
- Primary because: Upstream config blob at a named commit enumerating architecture fields (model_type, hidden_size, num_hidden_layers, num_attention_heads, vocab_size, max_position_embeddings) for this exact checkpoint.
- Scope: Mistral-7B-Instruct-v0.3 upstream config
- Supports: architecture parameters
- Supports: vocabulary size
- Supports: maximum position embeddings

### config.json blob (alternate commit adadfb3f...) for Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/adadfb3fbae87ecc77cd5bf2c3318434d5da04cf/config.json
- Publisher: Mistral AI / Hugging Face model repository
- Type: `repository`
- Primary because: Alternate upstream config blob in repository history confirming the same model parameterization values (hidden_size, num_hidden_layers, num_attention_heads, vocab_size, max_position_embeddings).
- Scope: Mistral-7B-Instruct-v0.3 upstream config (alternate blob)
- Supports: architecture parameters confirmation
- Supports: vocabulary size confirmation
- Supports: max position embeddings confirmation

### Commit history locator (commit b8ef2252...) for Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b8ef225287903940a8fcc1f6e1016b29c5cc01f3
- Publisher: Mistral AI / Hugging Face model repository
- Type: `repository`
- Primary because: Repository commit listing page at the referenced commit showing file uploads (config, tokenizer) and history for the upstream checkpoint.
- Scope: Mistral-7B-Instruct-v0.3 commit history
- Supports: tokenizer and config uploads
- Supports: repository management evidence

### Commit history locator (commit b0693ea4...) for Mistral-7B-Instruct-v0.3

- URL: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b0693ea4ce84f1a6a70ee5ac7c8efb0df82875f6
- Publisher: Mistral AI / Hugging Face model repository
- Type: `repository`
- Primary because: Repository commit listing page referencing a commit titled indicating chat-template/tool-calling support updates; used to inspect repository-level changes related to chat tooling.
- Scope: Mistral-7B-Instruct-v0.3 commit history (tool-calling/chat template changes)
- Supports: commit-level evidence of README/templating updates

### NGC catalog: mistral-7b-instruct-v0.3-onnx-int4-rtx (model page)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/models/mistral-7b-instruct-v0.3-onnx-int4-rtx
- Publisher: NVIDIA NGC (catalog.ngc.nvidia.com)
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC model listing for the ONNX-INT4 RTX quantized build derived from the upstream Mistral-7B-Instruct-v0.3 model; includes description of the quantization/conversion workflow.
- Scope: NVIDIA ONNX-INT4 quantized derivative listing for Mistral-7B-Instruct-v0.3
- Supports: quantized derivative description
- Supports: conversion workflow steps (download from Hugging Face, convert to ONNX FP16, quantize to INT4 using TensorRT Model Optimizer)

### NGC file browser for mistral-7b-instruct-v0.3-onnx-int4-rtx (artifact listing)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/-/models/mistral-7b-instruct-v0.3-onnx-int4-rtx/-/file-browser
- Publisher: NVIDIA NGC (catalog.ngc.nvidia.com)
- Type: `official-documentation`
- Primary because: Official artifact file listing for the NGC ONNX-INT4 model distribution (file manifest for the quantized derivative), used to verify included files and licensing artifacts shipped with the NGC package.
- Scope: NVIDIA ONNX-INT4 distribution file listing
- Supports: artifact listing (model.onnx, model.onnx_data, license files, special_tokens_map.json)

### NGC / NeMo model page: Mistral-7B-v03-Instruct (NeMo/NeMo checkpoint listing)

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/mistral-7b-v03-instruct
- Publisher: NVIDIA NGC (catalog.ngc.nvidia.com)
- Type: `official-documentation`
- Primary because: Official NGC listing indicating a NeMo-format/NeMo-optimized checkpoint for the instruct variant and supported runtimes (NeMo/TensorRT-LLM) for NVIDIA distributions.
- Scope: NVIDIA NeMo/NeMo-format model listing for Mistral-7B-Instruct-v0.3
- Supports: NeMo checkpoint listing
- Supports: runtime/optimization targets (TensorRT-LLM)

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/mistralai/mistral-7b-instruct-v0.3
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: mistralai-mistral-7b-instruct-v0-3
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No primary-source mapping found between the Forge serving slug/tag '7fdb5ba9c3' and an exact upstream commit ID or release artifact. URLs inspected: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b8ef225287903940a8fcc1f6e1016b29c5cc01f3 , https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b0693ea4ce84f1a6a70ee5ac7c8efb0df82875f6 , https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03 .
- Evidence gap: No primary-source numeric benchmark tables or leaderboard rows were found that explicitly name the exact checkpoint Mistral-7B-Instruct-v0.3 with dataset/split/metric/value in the inspected upstream artifacts and NVIDIA listings. URLs inspected: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 , https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md , https://catalog.ngc.nvidia.com/orgs/nvidia/models/mistral-7b-instruct-v0.3-onnx-int4-rtx , https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03 .
- Evidence gap: The inspected primary sources do not contain an explicit, consolidated statement labeled 'accepted input formats' (for example, a formal declaration 'inputs must be provided as a 1-D string tensor of token ids' was not found). URLs inspected: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 , https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md , https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03 .
- Evidence gap: No explicit primary-source documentation on calibrated confidence scores, per-token probability semantics, or recommended numeric score interpretation was found in the inspected model-card/config blobs. URLs inspected: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 , https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/config.json .
- Evidence gap: Chat-template JSON content for the canonical MistralTokenizer.v3 chat template was not found in upstream commit blobs or README fragments inspected; the repository contains commit messages referencing chat-template/tool-calling updates but the explicit template JSON artifact was observed only in discussion threads (excluded as secondary). Inspected URLs: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/commits/b0693ea4ce84f1a6a70ee5ac7c8efb0df82875f6 , https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md .
- Evidence gap: No primary-source statement was found in the inspected NIM/NGC pages or the upstream model blobs that explicitly states whether NVIDIA NGC/ONNX-INT4/RTX builds are bit-for-bit identical to the upstream checkpoint; NGC documentation describes a conversion/quantization workflow implying a derivative, but an explicit checksum-level mapping was not provided in the inspected artifacts. Inspected URLs: https://catalog.ngc.nvidia.com/orgs/nvidia/models/mistral-7b-instruct-v0.3-onnx-int4-rtx , https://catalog.ngc.nvidia.com/orgs/nvidia/-/models/mistral-7b-instruct-v0.3-onnx-int4-rtx/-/file-browser , https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03 .
- Evidence gap: No primary-source formal input-validation checklist (bounds, prohibited content filtering rules, exact tokenization failure modes) was found in the upstream repository or NVIDIA listings; repository README recommends external guardrails instead. Inspected URLs: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 , https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/blob/b8ef225287903940a8fcc1f6e1016b29c5cc01f3/README.md .
- Evidence gap: No primary-source, checkpoint-scoped numeric benchmark comparisons were located for Mistral-7B-Instruct-v0.3 in the inspected upstream or NVIDIA artifacts; comparisons in third-party or secondary pages were not considered primary. Inspected URLs: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 , https://catalog.ngc.nvidia.com/orgs/nvidia/models/mistral-7b-instruct-v0.3-onnx-int4-rtx , https://docs.api.nvidia.com/nim/reference/mistralai-mistral-7b-instruct-v03 .

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/mistralai/mistral-7b-instruct-v0.3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary host ollama.com: $.sources[9] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.inputPreparation_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://build.nvidia.com/mistralai/mistral-7b-instruct-v0.3: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
