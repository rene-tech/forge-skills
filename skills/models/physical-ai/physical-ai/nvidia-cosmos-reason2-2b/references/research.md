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

- Research key: `build-nvidia-com-nvidia-cosmos-reason2-8b-modelcard-ef0d7d8880`
- Independent audit: `revised`
- Researched: `2026-07-23T21:14:58.325546+00:00`

The audited primary evidence supports Cosmos-Reason2-8B as an NVIDIA multimodal reasoning VLM for physical AI and robotics, with text, image, and video inputs and text outputs focused on spatial-temporal and embodied reasoning. Primary sources also support object-detection-style reasoning capabilities and long-context support at the family/documentation level, but key checkpoint-scoped gaps remain: no immutable revision was reported, benchmark protocol details are incomplete, and exact output contract, tokenizer, and full preprocessing details are not fully specified for this Forge scope.

## Identity

- Upstream name: Cosmos Reason 2
- Checkpoint/version: Cosmos-Reason2-8B
- Immutable revision: not reported
- Parameter scale: 8,767,123,696 parameters
- Architecture/head: Open, customizable reasoning vision-language model (VLM) for physical AI and robotics; multi-modal LLM consisting of a Vision Transformer (ViT) vision encoder and a dense Transformer LLM; network architecture Qwen3-VL-8B-Instruct; post-trained based on Qwen3-VL-8B-Instruct and follows the same architecture.
- License: Model weights: NVIDIA Open Model License. Code: Apache 2.0 License.
- Evidence: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://github.com/nvidia-cosmos/cosmos-reason2

## Selection

### Recommended

- **Physical-AI and robotics reasoning over text, image, and video inputs** — Primary NVIDIA model-card and documentation sources describe Cosmos Reason 2 as an open reasoning VLM for physical AI and robotics that understands space, time, and fundamental physics and can support embodied-agent reasoning.
  Scope: Cosmos-Reason2-8B upstream checkpoint evidence served from Forge source scope https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard
  Evidence: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://docs.nvidia.com/cosmos/latest/reason2/index.html
- **Text-only or multimodal query answering for Cosmos-Reason2-8B** — Official NVIDIA API documentation states that text-only queries are supported for nvidia/cosmos-reason2-8b, and the model card reports support for text, image, and video inputs.
  Scope: Cosmos-Reason2-8B in official NVIDIA API/documentation scope
  Evidence: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html, https://huggingface.co/nvidia/Cosmos-Reason2-8B

### Conditional

- **Object detection with reasoning explanations, 2D/3D point localization, and bounding-box coordinates** — Use only after downstream validation of the exact serving output contract, because official documentation describes these capabilities but the audited findings do not provide a checkpoint-specific Forge response schema, units, or post-output validation protocol.
  Scope: Cosmos-Reason2 family documentation applied cautiously to Cosmos-Reason2-8B upstream checkpoint evidence
  Evidence: https://docs.nvidia.com/cosmos/latest/reason2/index.html, https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard
- **Long-context video reasoning workflows** — Use conditionally because official documentation reports long-context support up to 256K tokens and API defaults for video sampling, but benchmarked throughput, full preprocessing contract, and exact Forge runtime limits are not fully specified in the audited findings.
  Scope: Cosmos-Reason2-8B with official NVIDIA documentation on API behavior and family capabilities
  Evidence: https://docs.nvidia.com/cosmos/latest/reason2/index.html, https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html

### Avoid

- **Clinical or other safety-critical decision-making without expert review and external guardrails** — Primary NVIDIA sources say users are responsible for model inputs and outputs and must implement guardrails before deployment, while the audited findings do not provide clinical validation, calibration, or safety-critical deployment guarantees for this checkpoint.
  Scope: Cosmos-Reason2-8B and associated NVIDIA deployment documentation
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- **Tasks requiring an immutable published checkpoint revision for strict reproducibility** — The audited primary findings do not report an immutable revision identifier for this exact checkpoint.
  Scope: Cosmos-Reason2-8B upstream checkpoint
  Evidence: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://huggingface.co/nvidia/Cosmos-Reason2-8B

## Input preparation

### Semantic inputs

- The model supports text, image, and video as input modalities. Sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://huggingface.co/nvidia/Cosmos-Reason2-8B
- The model is intended for physical-AI and robotics reasoning contexts involving space, time, and fundamental physics. Sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://docs.nvidia.com/cosmos/latest/reason2/index.html

### Accepted formats

- Supported input formats reported in the model card are String for text, mp4 for video, and jpg for image. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Official API documentation discusses video-processing parameters for the model API and confirms text-only query support for nvidia/cosmos-reason2-8b. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html

### Preprocessing

- Official API documentation reports a default video sampling rate of 4.0 FPS, matching the training data. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Official API documentation reports default video frame preprocessing values of shortest_edge 3136 pixels and longest_edge 12,845,056 pixels. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Evidence gap: the audited findings do not specify tokenizer name, tokenization parameters, or a complete checkpoint-specific preprocessing pipeline beyond the documented API defaults.

### Pre-submit validation

- Specifying fps or num_frames higher than the actual video values results in a 400 error code. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Evidence gap: the audited findings do not specify complete input bounds such as maximum image size, maximum video duration, or full token limits for the exact Forge callable entry beyond documentation-level long-context claims.

### Task-specific formatting

- Text-only queries are supported for nvidia/cosmos-reason2-8b according to the official API documentation. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Evidence gap: the audited findings do not provide a canonical prompt template or complete official request-body example for all supported task patterns in this exact Forge scope.

## Output interpretation

### Outputs

- The Forge scope and model card support text output modality. Sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Official Cosmos documentation states that object detection provides 2D/3D point localization, bounding-box coordinates, and reasoning explanations with labels. Sources: https://docs.nvidia.com/cosmos/latest/reason2/index.html

### Interpretation

- At 2 FPS, timestamp precision in generated output is within +/- 0.25 seconds of the true values, per official API documentation. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Evidence gap: the audited findings do not define confidence-score semantics, probability calibration, or a complete schema for interpreting any structured detection fields for this exact Forge entry.

### Post-inference validation

- Users are responsible for model inputs and outputs and must implement guardrails before deployment. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- Evidence gap: the audited findings do not provide an official post-inference validation procedure, thresholding rule, or human-review checklist specific to Cosmos-Reason2-8B outputs.

## Public benchmarks

### Physical AI benchmark leaderboard overall

- Dataset/split: Physical AI Bench Leaderboard / not reported
- Metric/value: General Overall score / 73.73 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Benchmark scores were presented on 04/28/2026; the audited findings do not report the exact split or full evaluation protocol in the cited evidence.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Split not reported in the audited findings.
- Caveat: Full evaluation protocol not reported in the audited findings.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Depth reasoning benchmark

- Dataset/split: BlinkDepth / not reported
- Metric/value: score / 82.26 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Spatial reasoning benchmark

- Dataset/split: BlinkSpatial / not reported
- Metric/value: score / 75.52 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Computer vision benchmark

- Dataset/split: CVBench / not reported
- Metric/value: score / 78.74 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Video physics benchmark

- Dataset/split: VideoPhy2 / not reported
- Metric/value: score / 12.33 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Robotics benchmark overall

- Dataset/split: Robotics Overall / not reported
- Metric/value: score / 45.52 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Split not reported.
- Caveat: Full evaluation protocol not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Robotics sub-benchmark

- Dataset/split: ERQA / not reported
- Metric/value: score / 37.75 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Robotics sub-benchmark

- Dataset/split: CR Common / not reported
- Metric/value: score / 54.30 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Robotics sub-benchmark

- Dataset/split: CR Embodied / not reported
- Metric/value: score / 58.03 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Robotics sub-benchmark

- Dataset/split: Where2Place / not reported
- Metric/value: score / 32.00 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Self-driving benchmark overall

- Dataset/split: Self-Driving Overall / not reported
- Metric/value: score / 57.37 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Split not reported.
- Caveat: Full evaluation protocol not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Self-driving sub-benchmark

- Dataset/split: AV Collision / not reported
- Metric/value: score / 74.33 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Self-driving sub-benchmark

- Dataset/split: AV Stop / not reported
- Metric/value: score / 38.78 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Smart spaces benchmark

- Dataset/split: LingoQA / not reported
- Metric/value: score / 59.00 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Metric definition not further specified in the audited findings.
- Caveat: Split not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Smart spaces benchmark overall

- Dataset/split: Smart Spaces Overall / not reported
- Metric/value: score / 64.14 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Split not reported.
- Caveat: Full evaluation protocol not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

### Warehouse AI benchmark overall

- Dataset/split: Warehouse AI Overall / not reported
- Metric/value: score / 64.14 (`higher-is-better`)
- Model scope: Cosmos-Reason2-8B checkpoint as reported in the Hugging Face README/model card path
- Conditions: Reported in the benchmark listing dated 04/28/2026; exact protocol details are not provided in the audited findings.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Locator: README.md benchmark listing
- Caveat: Split not reported.
- Caveat: Full evaluation protocol not reported.
- Caveat: This is upstream-checkpoint evidence, not a Forge runtime benchmark.

## Comparisons

### Cosmos-Reason2-2B — `insufficient-evidence`

- Task: Selecting between official Cosmos Reason2 sizes for physical-AI reasoning
- Criteria: Primary evidence confirms that the model is available in 2B and 8B sizes, but the audited findings do not provide directly comparable benchmark protocol details for both sizes in the same cited source set.
- Rationale: Without matched checkpoint-level protocol details for both 2B and 8B, a task-specific winner cannot be verified from the audited primary evidence alone.
- Comparison conditions: Availability of both 2B and 8B is documented, but apples-to-apples evaluation conditions are not reported in the findings for a direct comparison.
- Evidence: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html, https://github.com/nvidia-cosmos/cosmos-reason2, https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md

## Limitations and safety

### Limitations

- No immutable checkpoint revision identifier was reported for this exact checkpoint in the audited findings. Sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard, https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Benchmark rows are available, but many protocol details such as exact splits and full metric definitions are not reported in the audited findings, limiting strict comparability. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- The audited findings do not provide complete tokenizer documentation or a full checkpoint-specific preprocessing specification beyond selected API defaults. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html, https://huggingface.co/nvidia/Cosmos-Reason2-8B
- The audited findings do not provide a complete official output schema for structured detection-style results in this exact Forge scope. Sources: https://docs.nvidia.com/cosmos/latest/reason2/index.html, https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard
- Code and model weights use different licenses, so deployment and redistribution review must distinguish Apache 2.0 code from NVIDIA Open Model License model weights. Sources: https://github.com/nvidia-cosmos/cosmos-reason2

### Safety

- Users are responsible for model inputs and outputs and must implement guardrails before deployment. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- NVIDIA states that Trustworthy AI is a shared responsibility. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- Users should report security vulnerabilities or NVIDIA AI concerns to NVIDIA. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA Build model card for Cosmos Reason2 8B

- URL: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA Build model card and mandatory starting source for the exact Forge scope.
- Scope: Forge source scope for Cosmos-Reason2-8B model card
- Supports: identity
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: avoidUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs

### NVIDIA Hugging Face model card for Cosmos-Reason2-8B

- URL: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA-published model card for the exact upstream checkpoint.
- Scope: Cosmos-Reason2-8B upstream checkpoint
- Supports: identity
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: avoidUseCases
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.acceptedFormats
- Supports: limitations

### Official Cosmos-Reason2 GitHub repository

- URL: https://github.com/nvidia-cosmos/cosmos-reason2
- Publisher: NVIDIA
- Type: `repository`
- Primary because: Official NVIDIA repository documenting the Cosmos-Reason2 family, architecture basis, and licensing distinctions.
- Scope: Cosmos-Reason2 family repository with checkpoint-family implementation and license information
- Supports: identity
- Supports: limitations
- Supports: comparisons

### Official Cosmos Reason2 documentation

- URL: https://docs.nvidia.com/cosmos/latest/reason2/index.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA documentation for Cosmos-Reason2 capabilities and documented feature descriptions.
- Scope: Cosmos-Reason2 family official documentation relevant to 8B unless otherwise unspecified
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: inputPreparation.semanticInputs
- Supports: outputInterpretation.outputs
- Supports: limitations

### Official NVIDIA Vision-Language Models API documentation for Cosmos-Reason2

- URL: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA API documentation specifying supported query modes, video defaults, and input validation behavior.
- Scope: Official API usage documentation for Cosmos-Reason2 2B and 8B
- Supports: recommendedUseCases
- Supports: conditionalUseCases
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.interpretation
- Supports: limitations
- Supports: comparisons

### NVIDIA NGC catalog entry for cosmos-reason2-8b

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA catalog source for deployment and safety-responsibility statements tied to the published container/service artifact.
- Scope: cosmos-reason2-8b NGC container/service metadata
- Supports: avoidUseCases
- Supports: outputInterpretation.validation
- Supports: safety

### NVIDIA Hugging Face README for Cosmos-Reason2-8B benchmark listing

- URL: https://huggingface.co/nvidia/Cosmos-Reason2-8B/blob/main/README.md
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA-hosted README path containing benchmark values for the exact checkpoint.
- Scope: Cosmos-Reason2-8B upstream checkpoint benchmark listing
- Supports: benchmarks
- Supports: comparisons
- Supports: limitations

## Evidence gaps

- The audited findings do not report an immutable revision identifier for Cosmos-Reason2-8B.
- The audited findings do not provide a complete tokenizer specification or full tokenization settings for Cosmos-Reason2-8B.
- The audited findings do not provide a complete checkpoint-specific prompt template set for this exact Forge entry.
- The audited findings do not provide a complete official structured output schema for any detection-style outputs in this exact Forge scope.
- Benchmark values are available for Cosmos-Reason2-8B, but the audited findings do not report full protocol details such as exact splits and full metric definitions for all rows.
- Direct checkpoint-matched comparisons between Cosmos-Reason2-8B and alternative official models under the same protocol are insufficiently documented in the audited findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 5 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
