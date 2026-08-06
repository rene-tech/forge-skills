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

- Research key: `huggingface-co-qwen-qwen2-5-7b-instruct-f5949308c7`
- Independent audit: `revised`
- Researched: `2026-08-06T08:59:38.042267+00:00`

Primary-source inspection used two authoritative upstream files: the Hugging Face model landing page (https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) and the repository config.json (https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json). The config.json records checkpoint-scoped architecture fields (architecture: "Qwen2ForCausalLM", model_type: "qwen2") and detailed model hyperparameters including hidden_size (3584), intermediate_size (18944), num_hidden_layers (28), num_attention_heads (28), num_key_value_heads (4), max_position_embeddings (32768), sliding_window (131072), rope_theta (1000000.0), bos_token_id (151643), eos_token_id (151645), use_cache true, and torch_dtype bfloat16. The Hugging Face model page documents license (Apache-2.0), long-context support up to 128,000 tokens, generation response length up to 8,000 tokens, multilingual support across 29+ languages, and counts of associated adapters/variants/quantized builds. The primary sources do not report an explicit parameter count or an immutable model revision identifier; tokenizer artifact files and an explicit checkpoint-scoped model card README or numeric benchmark tables for this exact checkpoint were not present among the inspected primary files. All claims and gaps in this dossier are sourced to one or both of the two inspected primary files listed in evidenceUrls.

## Identity

- Upstream name: Qwen/Qwen2.5-7B-Instruct
- Checkpoint/version: Qwen2.5-7B-Instruct
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Qwen2ForCausalLM
- License: Apache-2.0
- Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Selection

### Recommended

- **Long-context multilingual text generation and summarization where large context windows are required (contexts up to 128,000 tokens; responses up to ~8,000 tokens).** — The Hugging Face model page for Qwen2.5-7B-Instruct documents long-context window capability of up to 128,000 tokens and generation output up to 8,000 tokens, and lists multilingual support for 29+ languages.
  Scope: Qwen2.5-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Conditional

- **Use of adapters, fine-tuned variants, merges, or quantized builds derived from this checkpoint for specialized tasks (e.g., domain fine-tuning, quantized inference).** — These modes are available only as separately packaged variants (adapters, fine-tuned models, merges, quantized versions) referenced on the model page; validate the specific adapter/variant metadata and compatibility with the exact checkpoint before deployment.
  Scope: Qwen2.5-7B-Instruct and its listed adapter/variant builds
  Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Avoid

- **Evidence gap: No checkpoint-scoped avoidance guidance (for example, explicit prohibitions for clinical, legal, or other high-stakes domains) was found in the inspected primary sources.** — Evidence gap: The inspected primary sources do not contain checkpoint-scoped avoid-use boundaries or task-specific prohibitions.
  Scope: Qwen2.5-7B-Instruct
  Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Input preparation

### Semantic inputs

- The config.json defines BOS and EOS token IDs (bos_token_id = 151643, eos_token_id = 151645), indicating tokenized text inputs delimited by these special token IDs at the checkpoint level. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Accepted formats

- Evidence gap: The inspected primary sources do not list official accepted input file formats or transport envelopes for this checkpoint (for example, exact tokenizer files or hosted model-card input-format examples). Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Preprocessing

- The config.json documents model tokenization-related parameters (bos_token_id, eos_token_id, max_position_embeddings = 32768, sliding_window = 131072) but does not include tokenizer artifact files in the inspected paths. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Evidence gap: Tokenizer artifact files (e.g., tokenizer.json, tokenizer_config.json, merges/vocab, special_tokens_map.json, sentencepiece.model) were not found in the inspected primary-source locations and thus exact tokenization scheme and special token mappings beyond the BOS/EOS IDs are not documented for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Pre-submit validation

- Evidence gap: No checkpoint-scoped input validation rules (bounds, allowed/forbidden tokens, or ambiguity-handling procedures) were documented in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Task-specific formatting

- Evidence gap: No official prompt templates, paired-input ordering, or task-formatting prescriptions for this exact checkpoint were present in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Output interpretation

### Outputs

- The checkpoint architecture is Qwen2ForCausalLM (config.json), which corresponds to a causal language modeling head; explicit runtime output tensor shapes, logits/probabilities units, or embedding shapes are not documented in the inspected primary files. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No checkpoint-scoped documentation of returned tensor shapes, probabilities vs logits semantics, or example runtime responses was found in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Interpretation

- Interpretation constraint: Given architecture = Qwen2ForCausalLM (config.json), outputs should be interpreted in the context of causal next-token generation; however, the primary files do not provide calibration guidance or explicit mapping from model outputs to probabilistic/confidence scores. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

### Post-inference validation

- Evidence gap: No post-inference validation, calibration, or sanity-check procedures for this checkpoint were documented in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: evidence_gap: No primary-source, checkpoint-scoped comparative benchmark data found for pairwise task-level comparisons.
- Criteria: Evidence gap: The inspected primary sources do not contain numeric benchmarks or head-to-head comparison tables for this checkpoint; therefore no evidence-supported comparison is possible.
- Rationale: Checked primary locations (model landing page and config.json) contain architecture and capability facts but not task-level comparative metrics for Qwen2.5-7B-Instruct.
- Comparison conditions: Checked locations: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Limitations and safety

### Limitations

- Evidence gap: The inspected primary sources do not provide checkpoint-scoped safety, privacy, clinical, or deployment limitations beyond the stated license and architecture/configuration fields. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

### Safety

- Evidence gap: No checkpoint-scoped safety, privacy, dual-use, clinical, or data-handling guidance was present in the inspected primary sources. Sources: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen2.5-7B-Instruct model landing page

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: Official Hugging Face model landing page for the Qwen2.5-7B-Instruct checkpoint; provides license and checkpoint-level capability statements such as long-context support and multilingual capability.
- Scope: Qwen2.5-7B-Instruct
- Supports: license
- Supports: long-context capability
- Supports: generation length capability
- Supports: multilingual support
- Supports: counts of adapters/variants/quantized builds

### Qwen2.5-7B-Instruct config.json

- URL: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Publisher: huggingface.co
- Type: `repository`
- Primary because: Repository config.json contains checkpoint-scoped architecture, token IDs, and model hyperparameters used to identify architecture and model configuration facts.
- Scope: Qwen2.5-7B-Instruct
- Supports: architecture
- Supports: model-configuration
- Supports: special-token-IDs
- Supports: position-embeddings and sliding-window fields

## Evidence gaps

- Evidence gap: Exact parameter count (number of model parameters) for Qwen2.5-7B-Instruct was not reported in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No immutable model revision identifier (git SHA or immutable build id) for this checkpoint was present in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: Tokenizer artifact files (tokenizer.json, tokenizer_config.json, merges/vocab, special_tokens_map.json, sentencepiece.model) were not found in the inspected primary-source locations; exact tokenization scheme and special token mappings beyond bos/eos IDs are therefore not documented. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No checkpoint-scoped model-card README content or human-readable capability/motivation text was present in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No checkpoint-scoped numeric benchmark tables or figures were present in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (model landing page root) and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No explicit input/output runtime contract documentation (returned tensor shapes, logits/probabilities semantics, or example inference I/O) was present in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No checkpoint-scoped recommended-use guidance (example tasks or official recommended applications) was present in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json
- Evidence gap: No checkpoint-scoped conditional operating-mode documentation (for example, official long-context runtime flags, official adapters packaged in the upstream repo, or official quantization builds documented in the upstream repo) was present in the inspected primary files. Checked: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct and https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 29 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: unexpected property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0]: $.benchmarks[0]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1]: $.benchmarks[1]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2]: $.benchmarks[2]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3]: $.benchmarks[3]: missing required property caveats Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9]: $.sources[9]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7] uses unapproved repository owner 'collections' for this exact model scope: $.sources[7] uses unapproved repository owner 'collections' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: {'url': 'https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html', 'title': 'Qwen 2.5 speed benchmark'} Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/AllenAI/OLMo-2-0425-1B-Instruct Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
