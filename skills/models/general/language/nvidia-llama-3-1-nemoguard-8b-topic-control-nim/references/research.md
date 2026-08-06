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

- Research key: `build-nvidia-com-nvidia-llama-3-1-nemoguard-8b-topic-control-6ea6a06a4f`
- Independent audit: `revised`
- Researched: `2026-07-23T21:51:53.408283+00:00`

Primary NVIDIA and checkpoint sources consistently describe this artifact as a specialized topic-control/dialog moderation model, not a general-purpose generator. It is based on Llama 3.1 8B Instruct and uses PEFT/LoRA tuning to return a binary text decision about whether the last user message is on-topic or off-topic relative to a supplied topical instruction and dialogue context. Primary evidence supports use in task-oriented dialogue moderation and NeMo Guardrails integration. Important gaps remain for immutable revision, exact request-field constraints for this specific service page, tokenizer metadata, exact prompt restriction strings, and checkpoint-matched numeric benchmark values for the served artifact.

## Identity

- Upstream name: Llama 3.1 NemoGuard 8B Topic Control
- Checkpoint/version: Model version identifier is Llama-3.1-Nemotron-Topic-Guard-8B-v1.; NVIDIA NIM/container model name is llama-3.1-nemoguard-8b-topic-control
- Immutable revision: not reported
- Parameter scale: 8B
- Architecture/head: Transformer dialog moderation model based on the Llama architecture and trained from a Llama 3.1 8B Instruct base model; PEFT/LoRA-tuned specialized topic-control guardrail model
- License: Build page states NVIDIA Community Model License and the Llama 3.1 Community License Agreement apply; NIM docs state model artifact is licensed under the NVIDIA Community Model License Agreement and the Llama 3.1 Community License Agreement, while the container artifact is licensed under the NVIDIA Software License Agreement and the Product-Specific Terms for NVIDIA AI Products.
- Evidence: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemoguard-8b-topic-control

## Selection

### Recommended

- **Topical moderation of user prompts in human-assistant task-oriented dialogue** — The NVIDIA NIM reference states the model can be used for topical and dialogue moderation of user prompts in human-assistant interactions for task-oriented dialogue agents, and returns a binary response indicating whether the user message respects the topical instruction.
  Scope: Exact checkpoint/service family Llama 3.1 NemoGuard 8B Topic Control as documented by NVIDIA NIM reference
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control
- **Topical guardrail integration in NeMo Guardrails** — The Hugging Face model card states intended users include developers building task-oriented dialogue assistants and using the model as a topical guardrail in NeMo Guardrails. NeMo Guardrails documentation shows the model configured with type topic_control, engine nim, and model_name llama-3.1-nemoguard-8b-topic-control.
  Scope: Upstream checkpoint used as a NeMo Guardrails topic_control model via NVIDIA NIM
  Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/topic-control

### Conditional

- **Custom policy-based moderation where developers define allowed and disallowed topics in natural language** — Use only when the application can provide a system topical instruction and conversation history ending with the last user prompt, and validate downstream that the binary text label is suitable for the policy workflow.
  Scope: Llama 3.1 NemoGuard 8B Topic Control used as a dialog moderation model
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control

### Avoid

- **General-purpose instruction following, summarization, or open-ended text generation** — Primary sources describe the artifact as a specialized topic-control/dialog moderation model whose output is a binary text label, not a general-purpose generative assistant.
  Scope: Exact checkpoint/service family Llama 3.1 NemoGuard 8B Topic Control
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html
- **Using the output as calibrated probabilities or fine-grained moderation scores** — Primary sources only document text output as the binary label "on-topic" or "off-topic" and do not document probabilities, scores, or calibration.
  Scope: Exact checkpoint/service family Llama 3.1 NemoGuard 8B Topic Control
  Evidence: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control

## Input preparation

### Semantic inputs

- The model expects a system topical instruction/context defining on-topic and off-topic behavior plus dialogue context ending with the final user prompt. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control

### Accepted formats

- The NIM microservice exposes the standard OpenAI interface on /v1/completions and /v1/chat/completions endpoints. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blob/refs%2Fpr%2F4/README.md?code=true
- General NIM API documentation states OpenAI-style endpoints include POST /v1/chat/completions, POST /v1/completions, POST /v1/responses, POST /v1/messages, GET /v1/models, and POST /tokenize; an Anthropic-compatible messages endpoint is /v1/messages. Sources: https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html
- General NIM API documentation states a Completions API request includes JSON fields model, prompt, and max_tokens, and an Anthropic-compatible message request includes model, messages, and max_tokens. Sources: https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html

### Preprocessing

- Provide a system/topical instruction and the conversation history ending with the last user prompt so the model can judge whether the final user message respects the instruction. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control
- Evidence gap: The research findings do not specify an exact required prompt suffix, restriction string, or official prompt template text for this exact checkpoint/service.
- Evidence gap: The research findings do not specify tokenizer name, tokenizer revision, vocabulary details, or other tokenizer metadata for this exact checkpoint/service.

### Pre-submit validation

- Validate that the request includes the topical instruction/context and the final user message in conversation context, because the documented task is to classify whether the last user message respects that instruction. Sources: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control
- Evidence gap: The research findings do not specify exact per-field bounds, truncation rules, batching limits, required sampling parameters, or client-side schema constraints for this exact model page.

### Task-specific formatting

- For NeMo Guardrails integration, the model is configured with type "topic_control", engine "nim", and model_name "llama-3.1-nemoguard-8b-topic-control"; a prompt task "topic_safety_check_input $model=topic_control" invokes it. Sources: https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/topic-control
- Evidence gap: The research findings do not provide an exact official message ordering template or system-message suffix requirement for the raw NIM callable variant beyond needing topical instruction plus conversation history.

## Output interpretation

### Outputs

- The output is text: a binary label indicating whether the last user turn respects the topical instruction. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blob/refs%2Fpr%2F4/README.md?code=true
- The model responds to the final user prompt with the string "off-topic" or "on-topic". Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control

### Interpretation

- Interpret "on-topic" as the model judging that the final user message respects the supplied topical/system instruction, and "off-topic" as not respecting that instruction. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control
- Do not interpret the output as a probability, score, or calibrated confidence because primary sources only document binary text labels. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control

### Post-inference validation

- Downstream systems should validate that returned text is one of the documented labels "on-topic" or "off-topic" before enforcing policy decisions. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control
- Evidence gap: The research findings do not specify thresholding, calibration, or numeric post-processing guidance for this exact checkpoint/service.

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The model is specialized for topical/dialog moderation rather than a predefined content-moderation taxonomy; it is not documented as a general content safety classifier across broad moderation labels. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html
- Potential risk documented by the model card is that the dialogue agent may engage in user content that is not on-topic. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md
- Evidence gap: The research findings mention that metrics reported for the model include F1 and Accuracy, but they do not provide checkpoint-matched numeric values, splits, or evaluation tables for this exact artifact. Sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md

### Safety

- Use the model as a guardrail or moderation component for dialogue agents rather than as a sole unrestricted conversational assistant, because the documented purpose is topical and dialogue moderation. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control, https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control
- Access to the NIM containers and models is restricted and requires an active subscription to an NVIDIA AI Enterprise product or membership in the NVIDIA Developer Program. Sources: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/getting-started.html
- Developers can define specific conversation rules and boundaries, including not answering unrelated enquiries or sensitive topics such as politics or religion, when using the Topic Control model in NeMo Guardrails. Sources: https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/topic-control

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA Build page for Llama 3.1 NemoGuard 8B Topic Control

- URL: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical first-party NVIDIA Build product page for the exact model family served via Build/Forge.
- Scope: Forge starting source for NVIDIA Llama 3.1 NemoGuard 8B Topic Control
- Supports: identity.upstreamName
- Supports: identity.architecture
- Supports: identity.license
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.validation

### NVIDIA API reference for nvidia-llama-3_1-nemoguard-8b-topic-control

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party NVIDIA API reference for the exact NIM-served model behavior and intended use.
- Scope: Exact NIM/API behavior for Llama 3.1 NemoGuard 8B Topic Control
- Supports: identity.architecture
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: avoidUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation.interpretation
- Supports: safety

### Hugging Face model card for nvidia/llama-3.1-nemoguard-8b-topic-control

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Canonical first-party upstream model card under NVIDIA publisher for checkpoint identity, intended users, output contract, and PEFT/base-model statements.
- Scope: Upstream checkpoint/model card for Llama 3.1 NemoGuard 8B Topic Control
- Supports: identity.upstreamName
- Supports: identity.architecture
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: avoidUseCases
- Supports: inputPreparation.acceptedFormats
- Supports: outputInterpretation.outputs
- Supports: outputInterpretation.interpretation
- Supports: outputInterpretation.validation
- Supports: safety

### NVIDIA NIM documentation index for Llama 3.1 NemoGuard 8B TopicControl

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party NVIDIA documentation for the exact NIM model, licensing, dataset summary, and task framing.
- Scope: Exact NIM documentation for Llama 3.1 NemoGuard 8B TopicControl
- Supports: identity.architecture
- Supports: identity.license
- Supports: conditionalUseCases
- Supports: avoidUseCases
- Supports: limitations

### Hugging Face README code view for nvidia/llama-3.1-nemoguard-8b-topic-control

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blob/refs%2Fpr%2F4/README.md?code=true
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party model card content view confirming endpoint compatibility and output contract.
- Scope: Upstream checkpoint/model card content for Llama 3.1 NemoGuard 8B Topic Control
- Supports: inputPreparation.acceptedFormats
- Supports: outputInterpretation.outputs

### NGC container catalog for llama-3.1-nemoguard-8b-topic-control

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemoguard-8b-topic-control
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical first-party NVIDIA container catalog entry for runtime packaging identity and container pull name.
- Scope: NVIDIA NIM container packaging for llama-3.1-nemoguard-8b-topic-control
- Supports: identity.checkpoint

### NVIDIA NIM support matrix 1.0.0 for Llama 3.1 NemoGuard 8B TopicControl

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/1.0.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party versioned support matrix for the exact NIM runtime version.
- Scope: NIM runtime version 1.0.0 support matrix for Llama 3.1 NemoGuard 8B TopicControl
- Supports: evidenceGaps runtime/version context

### NVIDIA NIM latest support matrix for Llama 3.1 NemoGuard 8B TopicControl

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party support matrix for current documented deployment requirements.
- Scope: Latest NIM support matrix for Llama 3.1 NemoGuard 8B TopicControl
- Supports: evidenceGaps runtime/version context

### Hugging Face blame view README for nvidia/llama-3.1-nemoguard-8b-topic-control

- URL: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: First-party model card history view containing model version identifier, dataset details, license statement, and benchmark-metric mention.
- Scope: Upstream checkpoint/model card history for Llama 3.1 NemoGuard 8B Topic Control
- Supports: identity.checkpoint
- Supports: identity.license
- Supports: limitations
- Supports: evidenceGaps benchmarks

### NVIDIA NIM getting started for Llama 3.1 NemoGuard 8B TopicControl

- URL: https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party deployment access requirements for the exact NIM artifact.
- Scope: Deployment and access requirements for Llama 3.1 NemoGuard 8B TopicControl NIM
- Supports: safety

### NVIDIA NeMo Guardrails topic control configuration documentation

- URL: https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/topic-control
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party NeMo Guardrails documentation describing how the exact topic control model is integrated and configured.
- Scope: NeMo Guardrails integration for topic_control model_name llama-3.1-nemoguard-8b-topic-control
- Supports: recommendedUseCases
- Supports: inputPreparation.taskSpecificFormatting
- Supports: safety

### NVIDIA NIM large language models API reference

- URL: https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: First-party generic NIM API reference used only for interface-level request/endpoint facts applicable to NIM services.
- Scope: Generic NVIDIA NIM API interface documentation
- Supports: inputPreparation.acceptedFormats

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-topic-control
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-llama-3-1-nemoguard-8b-topic-control
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- The research findings do not report an immutable upstream revision identifier such as a commit hash, checksum, or exact model snapshot for this checkpoint; revision remains not reported. Checked primary sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control , https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md , and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html .
- The research findings indicate PEFT/LoRA tuning and a Llama 3.1 8B Instruct base model, but do not include primary file-level adapter metadata such as adapter_config.json for this exact artifact; exact PEFT configuration details remain unverified. Checked primary source: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control .
- The exact Build-page URL provided in expected scope differs from a finding URL by hyphen versus underscore formatting; only the underscore-form Build URL appears in the findings, so exact source-page aliasing cannot be verified from the findings alone. Checked primary source: https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control .
- The research findings do not specify exact tokenizer metadata, tokenizer package, or tokenizer revision for this checkpoint/service. Checked primary sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html .
- The research findings do not specify an exact required prompt suffix or restriction string such as TOPIC_SAFETY_OUTPUT_RESTRICTION for this exact checkpoint/service. Checked primary sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control and https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/topic-control .
- The research findings do not provide exact request defaults, sampling guidance, truncation rules, or field constraints specific to this model page beyond generic NIM interface fields. Checked primary sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemoguard-8b-topic-control and https://docs.nvidia.com/nim/large-language-models/latest/api-reference.html .
- Benchmark-specific evidence gap: metrics are said to include F1 and Accuracy in https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md , but the findings do not provide any exact numeric values, splits, tables, figures, or evaluation sections for this checkpoint, so no benchmark row can be safely retained. Checked locator: README.md benchmark/metrics mention in the blame view.
- Comparison-specific evidence gap: the findings do not provide protocol-matched primary-source benchmark values for this checkpoint and named alternatives, so no valid task-specific comparison can be established. Checked primary sources: https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control/blame/main/README.md and https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-topiccontrol/latest/index.html .
- The exact NIM/service version served by Forge is not directly reported in the findings. Primary sources show a versioned container 1.0.0 at https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemoguard-8b-topic-control and a separate tutorial mentioning image tag 1.10.1 in an uncited finding source not included here; therefore the precise Forge-served runtime version remains unresolved from the retained primary evidence.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-topic-control Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].value must contain a reported numeric result: $.benchmarks[0].value must contain a reported numeric result Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/llama-3.1-nemoguard-8b-topic-control: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
