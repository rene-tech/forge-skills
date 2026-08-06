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

- Research key: `huggingface-co-mistralai-devstral-small-2507-ac1faf9091`
- Independent audit: `revised`
- Researched: `2026-08-06T12:38:35.943548+00:00`

Devstral-Small-2507 (Devstral Small 1.1) is an agentic, text-only model released by Mistral AI and published in the Hugging Face repository mistralai/Devstral-Small-2507. Primary repository materials and a repository commit record report that Devstral Small 1.1 achieves 53.6% on the SWE‑bench Verified metric (README / commit), that it was fine-tuned from Mistral‑Small‑3.1 and that the vision encoder was removed during fine-tuning (PR README). The Hugging Face repository exposes large checkpoint file(s) and generation/configuration artifacts (repo tree and generation_config.json). Mistral's official announcement page records the model release and reports the model's licensing as Apache-2.0. Multiple required technical details are not present in the available primary-source artifacts in the findings: an immutable single-file SHA or file checksum mapping the Forge variant to a single upstream artifact; an authoritative numeric parameter count in the repo/announcement blobs included here; tokenizer implementation/version files and explicit tokenizer mappings; canonical SYSTEM_PROMPT contents in an upstream primary file; explicit decoding/default sampling parameter values in published generation_config contents; training-data provenance; and author-provided safety/PHI/clinical deployment guidance. These missing items are recorded as evidence gaps in the dossier.

## Identity

- Upstream name: mistralai/Devstral-Small-2507
- Checkpoint/version: Devstral-Small-2507
- Immutable revision: 3178e9e2d8880880098af656c1fe223927ce74f8
- Parameter scale: Evidence gap: parameter count (exact numeric parameter-scale claim) not stated in the primary sources available in the findings
- Architecture/head: Fine-tuned from Mistral-Small-3.1 (Devstral Small family, text-only after vision-encoder removal as stated in the HF PR README)
- License: Apache-2.0
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md, https://huggingface.co/mistralai/Devstral-Small-2507/commit/3178e9e2d8880880098af656c1fe223927ce74f8, https://mistral.ai/news/devstral-2507

## Selection

### Recommended

- **Agentic software-engineering workflows: tool-enabled codebase exploration, multi-file edits, and coding-agent tasks using the OpenHands scaffold.** — The Hugging Face repository and related README/PR content describe Devstral as an agentic model optimized for software-engineering agent workflows and recommend the OpenHands scaffold and agentic evaluation (README / PR README / commit).
  Scope: mistralai/Devstral-Small-2507 (Devstral Small 1.1)
  Evidence: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md, https://huggingface.co/mistralai/Devstral-Small-2507/commit/3178e9e2d8880880098af656c1fe223927ce74f8

### Conditional

- **Instruction-following or function-calling agent deployments under vLLM with tokenizer_mode mistral and config_format mistral (when served using the repository-recommended vLLM invocation and OpenHands scaffold).** — Must follow the repository's recommended vLLM serve invocation and tokenizer_mode/config_format flags; validate function-calling behavior in the intended runtime because the repo documents recommended serve flags but does not publish an authoritative, full function-calling format specification in the available primary files in the findings.
  Scope: mistralai/Devstral-Small-2507 (Devstral Small 1.1) when served with vLLM using repository-recommended flags
  Evidence: https://huggingface.co/mistralai/Devstral-Small-2507/blame/6c895c3bb1495411ee434c0ef7a1e1237119c1a0/README.md, https://huggingface.co/mistralai/Devstral-Small-2507/tree/main

### Avoid

- **Multimodal (vision) tasks that require an integrated vision encoder.** — The HF PR README states the vision encoder present in Mistral‑Small‑3.1 was removed before fine-tuning, and the model is described as text-only in the repository PR README and model card.
  Scope: mistralai/Devstral-Small-2507
  Evidence: https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md, https://huggingface.co/mistralai/Devstral-Small-2507
- **Assuming readiness for regulated clinical/PHI-handling tasks without additional validation.** — No author-provided PHI/clinical guidance, safety mitigations, or deployment guardrails are present in the available primary-source artifacts in the findings; therefore regulated uses lack upstream author endorsement in the cited primary sources.
  Scope: mistralai/Devstral-Small-2507
  Evidence: https://huggingface.co/mistralai/Devstral-Small-2507, https://mistral.ai/news/devstral-2507

## Input preparation

### Semantic inputs

- Text-only natural language and programming-language source code inputs intended for software-engineering agent workflows and code editing/exploration. Sources: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md

### Accepted formats

- Repository and README recommend serving/usage via chat/instruct text-generation pipelines and provide example 'mistral-chat' and 'mistral-chat --instruct' commands for interactive generation. Sources: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/README.md
- A generation_config.json file is present in the repository and is part of the repo-provided artifacts for generation configuration. Sources: https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/generation_config.json, https://huggingface.co/mistralai/Devstral-Small-2507/tree/main

### Preprocessing

- The README's snapshot_download example references allow_patterns that include 'tekken.json', indicating a Tekken tokenizer artifact is among repo artifacts to download (repository snapshot patterns). Sources: https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/README.md, https://huggingface.co/mistralai/Devstral-Small-2507/tree/main
- The repository README/blame view recommends using vLLM with the flag --tokenizer_mode mistral and --config_format mistral for serving. Sources: https://huggingface.co/mistralai/Devstral-Small-2507/blame/6c895c3bb1495411ee434c0ef7a1e1237119c1a0/README.md
- Evidence gap: exact tokenizer artifact files (tokenizer config JSON contents, tokenizer version string, full vocabulary files, and explicit special-token definitions) are not present in the available primary-source content in the findings.

### Pre-submit validation

- Evidence gap: the available primary-source artifacts in the findings do not publish explicit input-validation rules (e.g., accepted maximum/minimum lengths per field beyond context length) or a documented set of invalid/ambiguous-case checks.

### Task-specific formatting

- generation_config.json and a SYSTEM_PROMPT.txt are referenced by the repository tree and README as canonical files for generation settings and system prompt loading, but the SYSTEM_PROMPT.txt full contents are not available in the primary files provided in the findings. Sources: https://huggingface.co/mistralai/Devstral-Small-2507/tree/main, https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/generation_config.json, https://huggingface.co/mistralai/Devstral-Small-2507/blame/6c895c3bb1495411ee434c0ef7a1e1237119c1a0/README.md

## Output interpretation

### Outputs

- Upstream materials present the model as a text-generation/chat model (interactive 'mistral-chat' example) and the repository supplies generation_config.json controlling token IDs and basic generation fields. Sources: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/generation_config.json

### Interpretation

- Authors report task-level SWE‑bench Verified metric numeric results (e.g., 53.6% for Devstral Small 1.1) as an evaluation of coding-agent performance; no author-provided general output calibration guidance or numeric confidence thresholds are published in the available primary-source artifacts. Sources: https://huggingface.co/mistralai/Devstral-Small-2507/commit/3178e9e2d8880880098af656c1fe223927ce74f8, https://huggingface.co/mistralai/Devstral-Small-2507

### Post-inference validation

- Evidence gap: the primary sources in the findings do not provide a post-inference metadata contract (token logits/probabilities field names) or author-specified calibration/score-interpretation thresholds.

## Public benchmarks

### Coding-agent evaluation (SWE‑bench Verified)

- Dataset/split: SWE‑bench (Verified metric) using the OpenHands scaffold / not reported
- Metric/value: Verified (percent, task-level evaluation reported by authors) / 53.6% (`higher-is-better`)
- Model scope: Devstral Small 1.1 (mistralai/Devstral-Small-2507) as reported in the repository README and commit
- Conditions: Reported using the OpenHands scaffold per repository README/PR; exact dataset split and scoring script/config are not published in the available primary artifacts.
- Source: https://huggingface.co/mistralai/Devstral-Small-2507
- Locator: README benchmark table and repository commit 3178e9e2d8880880098af656c1fe223927ce74f8
- Caveat: Exact dataset split, scoring script, and full evaluation configuration are not present in the available primary-source artifacts (reproduction details absent).
- Caveat: The benchmark is reported in the repository README/commit and attributed to evaluation under the OpenHands scaffold; the primary files do not include the evaluation script or split identifiers.

## Comparisons

### allenai/OLMo-2-1124-7B-Instruct (candidate allenai-olmo-2-1124-7b-instruct) — `insufficient-evidence`

- Task: Coding-agent / document-ai (task group)
- Criteria: No protocol-matched, primary-source benchmark data for the alternative on the same dataset/split/metric/checkpoint was present in the findings; Devstral's SWE‑bench number is present for Devstral Small 1.1 but no matching primary-source benchmark for the alternative was found in the provided primary sources.
- Rationale: Devstral's SWE‑bench Verified result is present in the HF repo/commit, but the findings do not contain the alternative's matched benchmark on the same protocol for a direct comparison.
- Comparison conditions: Missing matching dataset split, metric, and explicit checkpoint-level numbers for the alternative in the available primary sources.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### ByteDance-Seed/Seed-OSS-36B-Instruct (candidate bytedance-seed-oss-36b-instruct) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark data linking Devstral Small 1.1 to this alternative checkpoint is present in the findings.
- Rationale: Devstral's SWE‑bench result is available but no equivalent primary-source SWE‑bench results for the alternative checkpoint were present in the findings.
- Comparison conditions: Dataset split, scoring protocol, and exact checkpoint numbers for the alternative are absent in the available primary sources.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### deepseek-ai/DeepSeek-R1-0528-Qwen3-8B (candidate deepseek-ai-deepseek-r1-0528-qwen3-8b) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark for this exact alternative checkpoint is present in the findings.
- Rationale: HF model card claims Devstral outperforms some larger variants, but the findings do not include a checkpoint-to-checkpoint SWE‑bench comparison that matches this candidate's exact slug and evaluation protocol.
- Comparison conditions: Protocol mismatch and absence of candidate-specific primary benchmark data in the findings.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### deepseek-ai/DeepSeek-R1-Distill-Qwen-14B (candidate deepseek-ai-deepseek-r1-distill-qwen-14b) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark for this exact alternative checkpoint is present in the findings.
- Rationale: Devstral's HF and PR README benchmarks are present, but no equivalent primary-source numbers for this alternative checkpoint were found in the provided primary sources.
- Comparison conditions: Missing matched dataset/split/metric/checkpoint numbers for direct comparison.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### HuggingFaceTB/SmolLM3-3B (candidate huggingfacetb-smollm3-3b-vllm) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No protocol-matched primary benchmark for SmolLM3-3B versus Devstral Small 1.1 is present in the available primary sources.
- Rationale: Devstral's SWE‑bench numbers exist in the HF repo, but the findings lack matching primary-source results for this alternative on the same protocol.
- Comparison conditions: Absence of candidate-specific benchmark numbers in the available primary sources.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### ibm-granite/granite-3.3-8b-instruct (candidate ibm-granite-granite-3-3-8b-instruct) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark comparing this alternative checkpoint to Devstral Small 1.1 was found in the available primary sources.
- Rationale: Findings include Devstral benchmarks but do not include matched Granite 3.3 checkpoint results on the same dataset/protocol.
- Comparison conditions: Missing dataset/split/metric/checkpoint-level numbers for direct comparison.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### ibm-granite/granite-4.1-8b (candidate ibm-granite-granite-4-1-8b) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source direct comparison in the available findings between Devstral Small 1.1 and this alternative was found.
- Rationale: Devstral's SWE‑bench reported numbers exist, but no matching primary-source numbers for this alternative on the same protocol were found in the provided primary sources.
- Comparison conditions: Missing equivalent benchmark entries for the alternative.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### microsoft-phi-4-mini-instruct (candidate microsoft-phi-4-mini-instruct-nim) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark comparing Devstral Small 1.1 to this alternative was found in the available primary sources.
- Rationale: Devstral benchmark exists in upstream docs but no matching primary-source SWE‑bench (or equivalent) result for this alternative was present in the findings.
- Comparison conditions: Lack of shared dataset/metric/checkpoint details in the available primary sources.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### openbmb/MiniCPM4-8B (candidate openbmb-minicpm4-8b-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source benchmark in the findings provides a matched comparison between Devstral Small 1.1 and this alternative.
- Rationale: Devstral's SWE‑bench number is present but the required matching benchmark evidence for the alternative is not present in the available primary sources.
- Comparison conditions: Missing alternative checkpoint benchmark numbers and protocol details.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### openbmb/MiniCPM5-1B (candidate openbmb-minicpm5-1b-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source protocol-matched benchmark evidence available in the findings for this alternative versus Devstral Small 1.1.
- Rationale: The findings do not contain candidate-specific benchmark numbers on the same protocol.
- Comparison conditions: Missing dataset/split/metric/checkpoint-level matches.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### Qwen/Qwen3-0.6B (candidate qwen-qwen3-0-6b-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, matched benchmark for this alternative against Devstral Small 1.1 is present in the available primary sources.
- Rationale: Devstral is reported on SWE‑bench but the findings lack matched results for this Qwen3 0.6B checkpoint.
- Comparison conditions: Missing matched dataset/split/metric/checkpoint data for the alternative.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### Qwen/Qwen3-1.7B (candidate qwen-qwen3-1-7b-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source matched benchmark evidence in the findings for this Qwen3 1.7B checkpoint versus Devstral Small 1.1.
- Rationale: Required checkpoint-level, protocol-matched numbers for direct comparison are absent from the available primary sources.
- Comparison conditions: Missing alternative checkpoint benchmark entries.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### Qwen/Qwen3-14B (candidate qwen-qwen3-14b-vllm and qwen-qwen3-14b-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark comparing Devstral Small 1.1 to Qwen3-14B was found in the available primary sources.
- Rationale: Although the HF model card/README asserts outperforming some larger variants, the specific alternative candidate numbers on the same protocol are not present in the available primary sources.
- Comparison conditions: Missing matched metric/split/checkpoint details for the alternative.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 (candidate qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source matched benchmark evidence for the alternative against Devstral Small 1.1 exists in the available primary sources.
- Rationale: Devstral report exists but the alternative's checkpoint-level SWE‑bench (or protocol-matched) numbers are missing from the available primary sources.
- Comparison conditions: Missing dataset/split/metric for the alternative in available findings.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### Qwen/Qwen3-8B (candidate qwen-qwen3-8b-vllm-cuda13) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source matched benchmark evidence for Qwen3-8B versus Devstral Small 1.1 is present in the available primary sources.
- Rationale: Findings include Devstral SWE‑bench claims but do not provide matching candidate checkpoint numbers on the same protocol.
- Comparison conditions: Absence of candidate-specific benchmark protocol and numeric values in the available primary sources.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

### Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 (candidate qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm) — `insufficient-evidence`

- Task: Coding-agent / document-ai
- Criteria: No primary-source, protocol-matched benchmark comparing this candidate to Devstral Small 1.1 is present in the available primary sources.
- Rationale: The available primary-source findings do not include matching numerical results for this specific candidate checkpoint.
- Comparison conditions: Missing required matched protocol and numeric benchmark evidence for the alternative.
- Evidence: https://huggingface.co/mistralai/Devstral-Small-2507

## Limitations and safety

### Limitations

- Parameter-scale and detailed architectural internals (layer counts, attention/position-encoding specifics) are not published in the available primary-source artifacts for this checkpoint. Sources: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md
- Training-data composition, dataset lists, filtering/deduplication procedures, and token counts for the Devstral-Small-2507 fine-tune are not disclosed in the available primary-source artifacts. Sources: https://huggingface.co/mistralai/Devstral-Small-2507, https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md
- The model is text-only (vision encoder removed during fine-tuning), therefore multimodal vision tasks requiring an encoder are out of scope for this checkpoint. Sources: https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md
- License conflict reported in secondary aggregators is not resolvable from secondary sources; primary upstream pages in the findings (Hugging Face repo and Mistral announcement) report Apache-2.0 for Devstral Small 1.1. Sources: https://huggingface.co/mistralai/Devstral-Small-2507, https://mistral.ai/news/devstral-2507

### Safety

- Evidence gap: author-provided safety mitigations, deployment guardrails, PHI/clinical guidance, and dual-use handling instructions for Devstral-Small-2507 are not present in the primary-source artifacts included in the findings.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: mistralai/Devstral-Small-2507

- URL: https://huggingface.co/mistralai/Devstral-Small-2507
- Publisher: Hugging Face (model repository owner)
- Type: `model-card`
- Primary because: Official Hugging Face model repository and model card for Devstral-Small-2507; contains the published model card, usage examples, and links to repository files used in this dossier.
- Scope: mistralai/Devstral-Small-2507 (Devstral Small 1.1)
- Supports: model-card usage examples and chat/instruct invocation snippets
- Supports: general repository-level claims about the checkpoint and artifacts
- Supports: public presentation of the model and links to repo artifacts

### Hugging Face repository tree: Devstral-Small-2507 (main)

- URL: https://huggingface.co/mistralai/Devstral-Small-2507/tree/main
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository file listing showing presence of checkpoint files (consolidated.safetensors), configuration files, and other repo artifacts referenced in the dossier.
- Scope: mistralai/Devstral-Small-2507 (repo contents)
- Supports: existence of checkpoint files and repository artifacts
- Supports: presence of generation_config.json and other repo files

### Hugging Face README (blame view) for Devstral-Small-2507

- URL: https://huggingface.co/mistralai/Devstral-Small-2507/blame/6c895c3bb1495411ee434c0ef7a1e1237119c1a0/README.md
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository README (blame view) contains recommended serve commands, snapshot_download patterns referencing tekken.json, vLLM invocation flags, and notes about required runtime versions used to derive input-prep and serving recommendations.
- Scope: mistralai/Devstral-Small-2507 (README and serve instructions)
- Supports: recommended vLLM serve invocation and --tokenizer_mode mistral recommendation
- Supports: snapshot_download allow_patterns mentioning tekken.json
- Supports: runtime dependency notes (mistral_inference >= 1.6.0, mistral-common >= 1.7.0)

### Hugging Face generation_config.json for Devstral-Small-2507

- URL: https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/generation_config.json
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository-hosted generation_config.json file provides the repository's declared token id mappings and identifies the transformers_version field used in the repo artifact.
- Scope: mistralai/Devstral-Small-2507 (repo generation configuration)
- Supports: presence of generation_config.json and its declared token-id mappings and transformers_version

### Hugging Face repository commit: 3178e9e2d8880880098af656c1fe223927ce74f8

- URL: https://huggingface.co/mistralai/Devstral-Small-2507/commit/3178e9e2d8880880098af656c1fe223927ce74f8
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository commit that updated README content to assert the SWE‑bench Verified numeric claim and provides a repository-level audit trail entry used to verify the reported benchmark value.
- Scope: mistralai/Devstral-Small-2507 (commit metadata and README update)
- Supports: reporting of 53.6% SWE‑bench Verified for Devstral Small 1.1 in the repository history
- Supports: commit-level evidence for the README benchmark text

### Hugging Face PR README: Devstral-Small-2507 (refs/pr/8 README)

- URL: https://huggingface.co/mistralai/Devstral-Small-2507/blob/refs%2Fpr%2F8/README.md
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository PR README contains statements that the model is fine-tuned from Mistral-Small-3.1, that the vision encoder was removed making the model text-only, the context window claim, and the README benchmark table referenced in the dossier.
- Scope: mistralai/Devstral-Small-2507 (PR README content)
- Supports: statement that Devstral is fine-tuned from Mistral-Small-3.1
- Supports: statement that the vision encoder was removed before fine-tuning (text-only)
- Supports: README benchmark table listing SWE‑bench values and OpenHands scaffold recommendation

### Mistral AI official announcement: Devstral-2507

- URL: https://mistral.ai/news/devstral-2507
- Publisher: Mistral AI (official website)
- Type: `official-documentation`
- Primary because: Official announcement from the model author naming the API/model id and asserting license information for Devstral Small 1.1.
- Scope: devstral-small-2507 (Mistral API naming and announcement)
- Supports: announcement of devstral-small-2507 availability and statement that Devstral Small 1.1 is released under Apache-2.0

### Hugging Face model card: mistralai/Devstral-Small-2507 — cited revision/file

- URL: https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/README.md
- Publisher: Hugging Face (model repository owner)
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: mistralai/Devstral-Small-2507 (Devstral Small 1.1)
- Supports: Exact audited claim citation

## Evidence gaps

- Exact immutable checkpoint file-hash or single-file SHA mapping the Forge variant 'mistralai/Devstral-Small-2507' (Forge key huggingface-co-mistralai-devstral-small-2507-ac1faf9091) to an upstream artifact: the repository files and commits are present but no single canonical checksum or release-tagged immutable artifact was published in the available primary-source artifacts in the findings.
- Exact numeric parameter-scale (precise parameter count) for the Devstral-Small-2507 checkpoint is not published in the available primary-source artifacts included in the findings.
- Exact tokenizer artifact contents, tokenizer-version string, full vocabulary files, and explicit special-token definitions are not present in the primary-source artifacts in the findings (tekken.json is referenced in snapshot patterns but the file contents and tokenizer-version are not available in the provided primary items).
- Complete generation/decoding defaults (explicit temperature, top_k, top_p, num_beams default values) are not exposed in the available primary generation_config.json or README files in the findings; generation_config.json exposes token id mappings and transformers_version but not explicit sampling defaults in the available primary-source artifact content.
- Full SYSTEM_PROMPT.txt canonical contents are not available in the primary upstream repository artifacts in the findings; a SYSTEM_PROMPT.txt content example is present only on a third-party mirror in the findings and therefore is not treated as a primary-source artifact here.
- Tokenization mapping examples (example strings with token counts) and explicit truncation semantics (where truncation occurs and exact behavior) are not documented in the available primary-source artifacts in the findings.
- Training-data provenance (dataset names, filtering/deduplication steps, token counts) for the Devstral-Small-2507 fine-tune is not disclosed in the available primary-source artifacts in the findings.
- Post-inference output metadata contract (token logits/probabilities field names, per-token score formats) and any author-specified calibration guidance are not published in the primary-source artifacts in the findings.
- Function-calling format: while the repository README recommends vLLM serve flags and tokenizer_mode, the findings do not include a primary-source, repository-published authoritative specification of Devstral's function-calling JSON schema or a canonical function-calling format document; thus function-calling format details are an evidence gap.
- Protocol-matched primary-source benchmark numbers for the listed Forge candidate alternatives (checkpoint-level, same dataset/split/prompt/metric) are not present in the available primary-source artifacts in the findings; therefore all comparisons to candidates are marked insufficient-evidence.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 12 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'redhatai' for this exact model scope: $.sources[7] uses unapproved repository owner 'redhatai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses unapproved repository owner 'unsloth' for this exact model scope: $.sources[9] uses unapproved repository owner 'unsloth' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'vllm-project' for this exact model scope: $.sources[11] uses unapproved repository owner 'vllm-project' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'unsloth' for this exact model scope: $.sources[12] uses unapproved repository owner 'unsloth' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/mistralai/Devstral-Small-2507/blob/main/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
