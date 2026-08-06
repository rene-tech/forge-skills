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

- Research key: `huggingface-co-nvidia-cosmos-ea-cosmos3-super-b558901695`
- Independent audit: `revised`
- Researched: `2026-08-06T13:04:49.731487+00:00`

Cosmos3‑Super is the Super‑scale checkpoint of NVIDIA's Cosmos3 omnimodal world models. Primary sources document Cosmos3‑Super as a multimodal generator that can produce dynamic video, images, audio, and action trajectories conditioned on text, images, or video. The family is released under the OpenMDW-1.1 license and checkpoints are published on Hugging Face. NVIDIA NIM documentation shows Cosmos3 serving components (Reasoner and Generator) expose model‑size options (Nano/Super) and a documented NIM HTTP API/serving contract; primary sources do not publish an immutable upstream checkpoint revision checksum, numeric end‑to‑end latency/throughput benchmarks for the exact Super upstream checkpoint, nor standardized numeric quality metrics (FVD/IS/SSIM/CLIP‑score) with dataset/split identifiers for Cosmos3‑Super. Several input/output contracts (accepted file types, sampling/resolution options, token limits for Reasoner, recommended frame‑rate guidance, and sampling parameters) are documented in Hugging Face model pages and NVIDIA NIM docs; where primary sources omit exact numeric protocol details (for example exact leaderboard dataset/split or an upstream immutable checksum), those items are recorded as evidence gaps.

## Identity

- Upstream name: Cosmos3 Super (Cosmos3‑Super)
- Checkpoint/version: Cosmos3‑Super (Super checkpoint)
- Immutable revision: not reported
- Parameter scale: 64 billion total parameters (reported as Super: 64B; reasoner 32B + generator 32B)
- Architecture/head: Mixture‑of‑Transformers (MoT) architecture described for the Cosmos3 family (reasoner + generator towers)
- License: OpenMDW-1.1
- Evidence: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason3/api.html, https://docs.nvidia.com/nim/cosmos/latest/introduction.html

## Selection

### Recommended

- **Omnimodal world generation for synthetic data and environment generation (text+image→video, text→image, text→video, audio, and action trajectory generation)** — Hugging Face model pages for Cosmos3‑Super state the checkpoint can generate dynamic video, image, audio, and action commands from multimodal inputs; the NVIDIA technical report describes Cosmos3 family capabilities for multimodal/world generation.
  Scope: Cosmos3‑Super checkpoint
  Evidence: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- **Physical AI research and synthetic environment generation for robotics policy training and agent pre‑training (research/experimental use with validation)** — Primary NVIDIA materials describe Cosmos3 and the family as intended for Physical AI use cases and world generation to support agent/robotics research.
  Scope: Cosmos3 family and Cosmos3‑Super checkpoint
  Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://huggingface.co/nvidia/Cosmos3-Super

### Conditional

- **Research or validation experiments for robotics control or decision‑support (not production safety‑critical control)** — Primary sources caution that outputs may be imperfect and require external validation, domain expert review, system‑level safety analysis, and guardrails before any safety‑sensitive deployment.
  Scope: Cosmos3‑Super checkpoint
  Evidence: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step
- **Low‑latency or single‑GPU inference using distilled/smaller variants derived from Super (e.g., 4‑step distilled variants)** — Primary sources describe 4‑step distilled variants that trade steps for speed; exact latency/throughput numbers on specific hardware for the distilled variants are not published in the inspected primary sources (evidence gap).
  Scope: Cosmos3‑Super‑Text2Image‑4Step and Cosmos3‑Super‑Image2Video‑4Step distilled variants
  Evidence: https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video

### Avoid

- **Safety‑critical closed‑loop autonomous control (e.g., direct robot control or safety‑critical vehicle control)** — Model pages and variant cards explicitly warn that generated outputs can be imperfect (temporal inconsistency, inaccurate physical interactions, action/state drift) and that users must implement guardrails; primary sources do not claim safety certification for closed‑loop control.
  Scope: Cosmos3‑Super checkpoint
  Evidence: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step
- **Substituting Cosmos3‑Super outputs as a certified physics simulator or guaranteed high‑fidelity physical engine** — Primary sources state the model lacks an explicit physics simulator and does not provide guaranteed correct 3D geometry, contact dynamics, or full physical laws — physical reasoning is approximated.
  Scope: Cosmos3 family and Cosmos3‑Super checkpoint
  Evidence: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- **Treating generated outputs as calibrated probabilistic confidence scores or ground‑truth labels for certification** — Primary sources do not document calibration semantics or per‑output probabilistic confidence scores; model cards caution against treating outputs as reliable ground truth without downstream validation.
  Scope: Cosmos3‑Super checkpoint and its distilled variants
  Evidence: https://huggingface.co/nvidia/Cosmos3-Super, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step

## Input preparation

### Semantic inputs

- Text prompts: free‑form text instructions or descriptions are accepted as a primary modality to condition generation. Sources: https://huggingface.co/nvidia/Cosmos3-Super, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Images: RGB color images in common image formats (e.g., jpg, png, webp) used as visual context for image→video or image‑conditioned generation. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Video: MP4 encoded video inputs are accepted as temporally structured context for generation/reasoning (NIM Generator endpoints support T2V and I2V modes). Sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Action trajectories / embodiment inputs: per‑frame numeric arrays (T, D) are supported as action conditioning where enumerated embodiments are described in model variant pages. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step

### Accepted formats

- Text input: UTF‑8 text strings (free text prompts). Sources: https://huggingface.co/nvidia/Cosmos3-Super
- Image input file types commonly used (jpg, png, webp) in RGB color; model cards indicate RGB inputs for image conditioning. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Video input: MP4 container files for temporally structured inputs as documented in NIM Generator and model variant pages. Sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video

### Preprocessing

- Sampling parameters and preprocessing options (resolution, num_output_frames, fps, num_steps, guidance scale) are documented in NVIDIA NIM sampling parameters; input videos are resampled to selected resolution. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/sampling-params.html
- NIM Generator documentation states the Generator uses the Reasoner tower for input understanding and the Generator tower for output generation (serving‑level architecture). Sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html
- Model variant pages document that some distilled variants (4‑step) reduce diffusion steps (e.g., from 50 to 4) to accelerate inference. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step

### Pre-submit validation

- NIM sampling parameters set permitted ranges for resolution, num_output_frames, and fps (e.g., num_output_frames default and ranges documented in sampling parameters). Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/sampling-params.html
- Model pages and variant cards warn that users should validate color space (sRGB) and input formats prior to downstream use; explicit numeric acceptance or truncation rules for tokens and exact per‑modality preprocessing implementations are not published as immutable upstream details (evidence gaps). Sources: https://huggingface.co/nvidia/Cosmos3-Super, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Primary sources do not publish exact tokenizer name/version, vocabulary, truncation rules, or batching semantics for the upstream Cosmos3‑Super checkpoint (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Task-specific formatting

- Text→Image and Image→Video generative prompts are provided as text strings with optional input images; 4‑step distilled variants specify a reduced denoising schedule in their model cards. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- NIM Generator API exposes parameters for resolution, frame count, fps, guidance scale, and num_steps which must be used per the documented sampling parameters when invoking the Generator. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/sampling-params.html, https://docs.nvidia.com/nim/cosmos/latest/introduction.html

## Output interpretation

### Outputs

- Generator image outputs and video outputs are produced at supported processing resolutions (documented processing resolutions include 256, 480, 512, and 720) as described in NIM sampling parameters and model variant cards. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/sampling-params.html, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Video outputs are returned by NIM Generator endpoints as MP4 artifacts in the service contract; NIM documentation describes a JSON field (b64_video) used in some provider examples to carry base64‑encoded MP4 content (serving contract). Sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason3/api.html
- Reasoner text outputs function as LLM responses with documented token limits for Reasoner sizes in NIM docs (Reasoner Super 32B noted); explicit upstream token‑probability/calibration semantics for generated modalities are not published in the inspected primary sources (evidence gap). Sources: https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason3/api.html, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step
- Action outputs: model variant pages describe per‑frame numeric arrays for action embodiments, but a machine‑readable standard schema or downloadable schema file for embodiment dimensionalities is not provided in the inspected primary sources (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video

### Interpretation

- Generated outputs are not guaranteed to be physically accurate or temporally consistent in long horizons; users should not treat outputs as ground truth and must validate downstream before use in critical systems. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step
- Primary sources do not provide per‑output calibration scores, confidence intervals, or probabilistic semantics for generator outputs; downstream calibration and validation are required (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super

### Post-inference validation

- For NIM deployments, follow the NIM serving contract to decode base64 MP4 payloads and validate container and codec compliance as part of postprocessing. Sources: https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason3/api.html, https://docs.nvidia.com/nim/cosmos/latest/introduction.html
- Primary sources do not supply numeric calibration thresholds or acceptance criteria; users must design and validate their own post‑inference checks (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super

## Public benchmarks

### Image→Video ranking (open‑source leaderboard placement reported)

- Dataset/split: leaderboard placement reported (dataset/split not specified in primary source) / not reported
- Metric/value: leaderboard rank (claim: #1 among open‑source models for Image→Video as stated in model card) / #1 (rank reported; numeric protocol not provided) (`context-only`)
- Model scope: Cosmos3‑Super‑Image2Video‑4Step (4‑step distilled variant)
- Conditions: Model card asserts leaderboard placement but does not provide numeric metric values, dataset identifiers, split, or evaluation protocol in the inspected primary source.
- Source: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Locator: model card text asserting leaderboard rank; exact table/figure/metric name/dataset/split is not reported on the primary model page (evidence gap)
- Caveat: Leaderboard rank is reported without underlying dataset name, split, metric definition, numeric score, or evaluation protocol in the inspected primary source.

## Comparisons

### Cosmos3‑Nano (Cosmos3 Nano 16B) — `tradeoff`

- Task: General omnimodal world generation and Physical AI tasks (quality vs. compute tradeoff)
- Criteria: Parameter scale and intended hardware targets (Super reported as larger aggregate parameterization vs. Nano reported smaller sizes), implying resource vs. fidelity tradeoffs; no matched numeric quality protocol published in inspected primary sources to enable direct numeric comparison.
- Rationale: NVIDIA primary sources document multiple family sizes (Nano and Super) for Reasoner/Generator towers; parameter‑scale implication and differing hardware targets are described but no direct numeric task metrics for both checkpoints under a matched protocol are published in the inspected primary sources.
- Comparison conditions: No checkpoint‑matched numeric benchmarks or dataset/split/protocol presented for both Nano and Super in the inspected primary sources.
- Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason3/api.html, https://docs.nvidia.com/nim/cosmos/latest/introduction.html

### NVIDIA Predict1 7B (candidate alternative listed by user) — `insufficient-evidence`

- Task: Text2World / Video2World world generation
- Criteria: No checkpoint‑scoped numeric performance or protocol‑matched evaluation data for Predict1 7B in the inspected primary Cosmos3 sources; NIM provider docs do not provide matched quality metrics for an external candidate.
- Rationale: NIM documentation provides serving and API contract details but does not publish protocol‑matched quality comparisons between Cosmos3‑Super and external alternative checkpoints in the inspected primary sources.
- Comparison conditions: Protocol mismatch / lack of comparable numeric benchmarks in inspected sources.
- Evidence: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Cosmos Transfer2.5 2B (candidate alternative listed by user) — `insufficient-evidence`

- Task: World generation / multimodal generation
- Criteria: No checkpoint‑scoped numeric benchmark or direct protocol comparison for Transfer2.5 2B is present in the inspected primary Cosmos3 sources.
- Rationale: The inspected primary sources for Cosmos3 do not provide numeric, protocol‑matched comparisons to Transfer2.5 2B; therefore direct evidence is absent.
- Comparison conditions: No matched evaluation protocol or dataset/split published in the inspected primary sources for both checkpoints.
- Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

## Limitations and safety

### Limitations

- Cosmos3‑Super and its variants can produce imperfect outputs (temporal inconsistency, unstable camera/object motion, imprecise physical interactions, inaccurate audio‑video synchronization, and action‑state drift), especially in long‑horizon or high‑resolution generations. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step
- Cosmos3 lacks an explicit physics simulator and does not guarantee correct 3D geometry, contact dynamics, object permanence, or exact physical laws; physical reasoning is approximated by the model. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Primary sources do not publish an immutable upstream checkpoint revision identifier or checksum for the Cosmos3‑Super checkpoint (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Primary sources do not provide numeric end‑to‑end latency, throughput, or memory (GB) measurements for Cosmos3‑Super on specific hardware configurations (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://docs.nvidia.com/nim/cosmos/latest/introduction.html
- Details of tokenizer name/version, vocabulary, truncation rules, batching semantics, and exact per‑modality preprocessing implementations for the upstream Cosmos3‑Super checkpoint are not published in the inspected primary sources (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf

### Safety

- Primary model pages and variant cards place responsibility on users to implement guardrails and safety mechanisms; outputs are not safety‑certified and require system‑level validation for any safety‑critical deployments. Sources: https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step, https://huggingface.co/nvidia/Cosmos3-Super
- The model is not a certified simulator; outputs can hallucinate entities, misinfer object states or causal relations, and produce implausible or unsafe action sequences — domain expert review and system‑level safety analysis are required. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Primary sources do not provide specialized privacy/PHI handling guidance or clinical use certifications; clinical or PHI‑sensitive use requires separate review and controls (evidence gap). Sources: https://huggingface.co/nvidia/Cosmos3-Super

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: Cosmos3‑Super

- URL: https://huggingface.co/nvidia/Cosmos3-Super
- Publisher: Hugging Face / NVIDIA
- Type: `model-card`
- Primary because: Canonical Hugging Face model landing page for the Cosmos3‑Super checkpoint published by NVIDIA.
- Scope: Cosmos3‑Super checkpoint and family metadata
- Supports: identity
- Supports: license
- Supports: general capabilities
- Supports: semanticInputs
- Supports: acceptedFormats
- Supports: limitations

### Hugging Face model card: Cosmos3‑Super‑Image2Video

- URL: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video
- Publisher: Hugging Face / NVIDIA
- Type: `model-card`
- Primary because: Canonical Hugging Face model card for the Cosmos3‑Super Image→Video variant published by NVIDIA.
- Scope: Cosmos3‑Super Image2Video variant
- Supports: input/output formats
- Supports: limitations
- Supports: conditional use guidance
- Supports: leaderboard/placement claim (leaderboard metadata without numeric protocol)

### Hugging Face model card: Cosmos3‑Super‑Text2Image‑4Step

- URL: https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step
- Publisher: Hugging Face / NVIDIA
- Type: `model-card`
- Primary because: Canonical Hugging Face model card for the 4‑step distilled Text2Image variant derived from Cosmos3‑Super.
- Scope: Cosmos3‑Super‑Text2Image‑4Step distilled variant
- Supports: distilled variant description
- Supports: inference schedule (4‑step)
- Supports: speedup claim (stated by model card)
- Supports: safety guidance

### NVIDIA Cosmos3 technical report (Cosmos3 technical‑report.pdf)

- URL: https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- Publisher: NVIDIA Research / Cosmos Lab
- Type: `technical-report`
- Primary because: Canonical NVIDIA Research technical report describing Cosmos3 architecture, family design, and released artifacts.
- Scope: Cosmos3 family design and technical details (family‑level architecture and release policy)
- Supports: architecture (Mixture‑of‑Transformers family description)
- Supports: family descriptions
- Supports: release of open‑weight checkpoints on Hugging Face
- Supports: limitations regarding physics simulation

### NVIDIA NIM Cosmos introduction (NIM documentation)

- URL: https://docs.nvidia.com/nim/cosmos/latest/introduction.html
- Publisher: NVIDIA NIM / official documentation
- Type: `official-documentation`
- Primary because: Official NIM documentation describing the Generator and Reasoner roles, supported generation endpoints, and model‑size options exposed by NIM.
- Scope: NIM serving contract and Generator/Reasoner roles
- Supports: NIM API contract (service roles)
- Supports: supported generation endpoints (T2V, I2V, etc.)
- Supports: serving relationship (Generator uses Reasoner for input understanding)

### NVIDIA NIM Cosmos Reasoner API examples (vision‑language models docs)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason3/api.html
- Publisher: NVIDIA NIM / official documentation
- Type: `official-documentation`
- Primary because: NIM API examples and Reasoner size statements published in NVIDIA documentation.
- Scope: Cosmos3 Reasoner sizes and API examples
- Supports: Reasoner model sizes (Nano 8B, Super 32B)
- Supports: Reasoner API examples and behavior
- Supports: token limits and Reasoner usage notes

### NVIDIA NIM Cosmos support matrix and precision options

- URL: https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html
- Publisher: NVIDIA NIM / official documentation
- Type: `official-documentation`
- Primary because: Official NIM support matrix documenting precision options and GPU architecture compatibility for Cosmos3 Generator.
- Scope: NIM precision options and hardware compatibility
- Supports: supported precisions (bf16, fp8, nvfp4)
- Supports: hardware compatibility notes for Hopper/Blackwell

### NVIDIA NIM Cosmos sampling parameters documentation

- URL: https://docs.nvidia.com/nim/cosmos/3.0.0/sampling-params.html
- Publisher: NVIDIA NIM / official documentation
- Type: `official-documentation`
- Primary because: Official documentation of sampling parameters (resolution, num_output_frames, fps, guidance scale, num_steps) and processing resolution options.
- Scope: Sampling parameters and supported processing resolutions
- Supports: processing resolution options (256, 480, 512, 720)
- Supports: num_output_frames defaults and range, fps recommendations, guidance scale and num_steps constraints

### Exact official starting source declared by Forge

- URL: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-cosmos3-omni
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Immutable upstream checkpoint revision identifier or checksum for the Cosmos3‑Super checkpoint is not reported in the inspected primary sources. Checked: https://huggingface.co/nvidia/Cosmos3-Super (model landing page), https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf (technical report).
- No numeric benchmark metrics (FVD, IS, SSIM, PSNR, CLIP‑score) with dataset names, splits, seeds, and numeric values are published for Cosmos3‑Super in the inspected primary sources. Checked: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video (variant page), https://huggingface.co/nvidia/Cosmos3-Super (model landing page), https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf (technical report).
- Exact mapping between an NVIDIA NIM serving/container artifact and an unchanged named upstream Cosmos3‑Super checkpoint (i.e., whether the NIM container serves an unchanged upstream checkpoint or a packaged/quantized/modified variant) is not explicit in the inspected primary sources. Checked: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://huggingface.co/nvidia/Cosmos3-Super.
- Latency, throughput, and memory (GB) measurements for Cosmos3‑Super on specific hardware configurations (H100/H200/B200 or exact GPU counts) are not provided as numeric values in the inspected primary sources. Checked: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf, https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html.
- Exact dataset names, splits, and evaluation protocols underlying the 'rank #1 among open‑source models' leaderboard placement claimed on the Cosmos3‑Super Image2Video model page are not provided on the inspected primary source page. Checked: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video.
- Precise tokenizer identity (name/version), vocabulary, tokenization/truncation rules, batching semantics, and per‑modality preprocessing implementation details for the upstream Cosmos3‑Super checkpoint are not documented in the inspected primary sources. Checked: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf.
- Per‑output calibration semantics (per‑token probabilities, per‑frame likelihoods, aggregated uncertainty measures) are not documented in the inspected primary sources. Checked: https://huggingface.co/nvidia/Cosmos3-Super, https://huggingface.co/nvidia/Cosmos3-Super-Text2Image-4Step.
- A machine‑readable embodiment schema file enumerating exact action‑output dimensionalities is not published in the inspected primary sources; embodiment dimensionalities are described but no downloadable schema file was found. Checked: https://huggingface.co/nvidia/Cosmos3-Super-Image2Video.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary URL https: $.sources[9] uses forbidden secondary URL https://huggingface.co/nvidia/Cosmos3-Super/discussions/12/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'blog' for this exact model scope: $.sources[12] uses unapproved repository owner 'blog' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
