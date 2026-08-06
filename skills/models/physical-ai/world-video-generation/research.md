# World Video Generation model selection

- Category: `physical-ai`
- Group: `world-video-generation`
- Independent audit: `revised`
- Researched: `2026-07-23T23:34:05.620005+00:00`

Physical-AI world-video-generation comparing five exact Forge artifacts: nvidia-cosmos-predict1-7b-text2world (Predict1 Text2World — text-only conditioning), nvidia-cosmos-predict1-7b-video2world (Predict1 Video2World — image/video conditioning), nvidia-cosmos-transfer2-5-2b (Transfer2.5 2B — controllable generation from structured control-video inputs such as edges, blur, depth, segmentation), nvidia-cosmos3-omni-nano (Cosmos3 Nano — smaller omni generator upstream checkpoint), and nvidia-cosmos3-omni-super (Cosmos3 Super — larger omni generator upstream checkpoint). Scope: only claims and numeric evidence that explicitly name one of these five exact Forge slugs or an upstream checkpoint explicitly mapped to a Forge slug within the same primary source. Included evidence types: serving-runtime/container listings (NGC catalog pages), official NVIDIA NIM/docs pages, research.nvidia.com pages, canonical arXiv preprints, official NVIDIA GitHub repositories, and official Hugging Face model pages when present in the research findings. Out of scope: family-level Cosmos claims or parameter/benchmark mappings that are not explicitly and unambiguously mapped to one of the five exact Forge slugs in the primary sources in the research findings. If NVIDIA packages an upstream checkpoint, that mapping is treated as upstream-checkpoint evidence only if an explicit mapping appears in a single primary source.

## Questions to answer before selecting

- Do you require text-only conditioning (use nvidia-cosmos-predict1-7b-text2world) or image/video conditioning (use nvidia-cosmos-predict1-7b-video2world)?
- Do you require explicit structured spatial control modalities (blur, edge, depth, segmentation) as primary inputs (consider nvidia-cosmos-transfer2-5-2b) rather than free-form prompts?
- Must the artifact be an exact NIM/NGC container slug (serving-runtime identity) rather than only an upstream checkpoint or Hugging Face model card?
- Are you evaluating upstream-checkpoint model-quality (research/arXiv/model-card) or serving/runtime packaging and operational guidance (NGC, NIM docs)?
- Do you require a Cosmos3 size-variant mapping (nvidia-cosmos3-omni-nano vs nvidia-cosmos3-omni-super) to be unambiguously documented for your runtime?
- Are per-artifact license distinctions between model weights and code/runtime material to your deployment?
- Do you require exact output specs (frame count, FPS, resolution) and per-artifact runtime limits verified for the exact Forge slug and runtime?

## Comparability rules

- Compare only when a single primary source explicitly names the exact Forge artifact identity (exact NGC/container slug or an explicit Forge→upstream checkpoint mapping) together with dataset name (and split, if used), metric definition (including pooling/normalization), and the exact evaluation protocol (prompt template, frame counts/sampling and any special downstream head/service).
- Serving-runtime/container evidence (catalog.ngc.nvidia.com, docs.nvidia.com NIM pages, build.nvidia.com modelcards) is distinct from upstream-checkpoint evidence (research.nvidia.com, arXiv, official GitHub checkpoints, huggingface.co model pages). Do not conflate packaging/serving claims with upstream-checkpoint numeric evaluation evidence; label each result as serving-runtime or upstream-checkpoint accordingly.
- Do not transfer family-level parameter counts, benchmark numbers, or packaging claims to an exact Forge slug unless a single primary source explicitly maps that number to the exact Forge slug in the same source.
- Control-condition comparisons (e.g., Transfer2.5 modalities) are valid only when the primary source documents the exact control format/schema, dataset (and split), metric, and the exact artifact identity together.
- If an evaluated result requires a downstream head, additional service, or an off-process upsampler not exposed by the named Forge slug, that dependency must be declared in comparison/conditions and the numeric value must be labeled as depending on that external component.

## Conditional routing

### Prefer `nvidia-cosmos-predict1-7b-text2world` when You need a text-only world-video generation artifact (text-only conditioning) with an explicit Predict1 Text2World serving identity.

- Why: The NGC container listing and Predict1 documentation identify a Predict1 Text2World 7B serving/container artifact and the Predict1 repository and model card describe a Text2World diffusion variant suitable for text-only conditioning (serving-runtime and upstream-checkpoint evidence).
- Alternative: nvidia-cosmos-predict1-7b-video2world
- Alternative: nvidia-cosmos-transfer2-5-2b
- Alternative: nvidia-cosmos3-omni-nano
- Alternative: nvidia-cosmos3-omni-super
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-text2world, https://docs.nvidia.com/cosmos/latest/predict1/index.html, https://github.com/nvidia-cosmos/cosmos-predict1, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://research.nvidia.com/labs/cosmos-lab/cosmos-predict1, https://arxiv.org/html/2501.03575v2

### Prefer `nvidia-cosmos-predict1-7b-video2world` when You need image-conditioned or video-conditioned world generation (the Predict1 Video2World head rather than the text-only head).

- Why: The NGC container listing and Predict1 documentation identify a Predict1 Video2World 7B serving/container artifact and the Predict1 repository and model card describe Video2World usage for image/video-conditioned generation (serving-runtime and upstream-checkpoint evidence).
- Alternative: nvidia-cosmos-predict1-7b-text2world
- Alternative: nvidia-cosmos-transfer2-5-2b
- Alternative: nvidia-cosmos3-omni-nano
- Alternative: nvidia-cosmos3-omni-super
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world, https://docs.nvidia.com/cosmos/latest/predict1/index.html, https://github.com/nvidia-cosmos/cosmos-predict1, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://arxiv.org/html/2501.03575v3

### Prefer `nvidia-cosmos-transfer2-5-2b` when You need controllable generation using structured control-video inputs (blur/edge/depth/segmentation) with a documented Transfer2.5 artifact.

- Why: The NGC container listing, the Transfer2.5 research page, the Transfer2.5 GitHub repository, and the Transfer2.5 Hugging Face model page document a Transfer2.5 2B artifact that accepts multi-modal control inputs (serving-runtime and upstream-checkpoint evidence).
- Alternative: nvidia-cosmos-predict1-7b-video2world
- Alternative: nvidia-cosmos-predict1-7b-text2world
- Alternative: nvidia-cosmos3-omni-nano
- Alternative: nvidia-cosmos3-omni-super
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://github.com/nvidia-cosmos/cosmos-transfer2.5, https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html

### Prefer `nvidia-cosmos3-omni-nano` when You specifically require a Cosmos3 Generator smaller packaged/variant identity (Nano) and want the Nano upstream/packaging identity verified.

- Why: The Cosmos3 Hugging Face model page and NVIDIA research/packaging framework materials document a Cosmos3-Nano upstream checkpoint and the Cosmos3 family packaging framework (upstream-checkpoint and packaging evidence).
- Alternative: nvidia-cosmos3-omni-super
- Alternative: nvidia-cosmos-predict1-7b-text2world
- Alternative: nvidia-cosmos-predict1-7b-video2world
- Alternative: nvidia-cosmos-transfer2-5-2b
- Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://research.nvidia.com/labs/cosmos-lab/cosmos3, https://github.com/NVIDIA/cosmos-framework

### Prefer `nvidia-cosmos3-omni-super` when You specifically require a Cosmos3 Generator larger packaged/variant identity (Super) and want the Super upstream/packaging identity verified.

- Why: The Cosmos3 Hugging Face model page and NVIDIA research/packaging materials document a Cosmos3-Super upstream checkpoint and the Cosmos3 family packaging framework (upstream-checkpoint and packaging evidence).
- Alternative: nvidia-cosmos3-omni-nano
- Alternative: nvidia-cosmos-predict1-7b-text2world
- Alternative: nvidia-cosmos-predict1-7b-video2world
- Alternative: nvidia-cosmos-transfer2-5-2b
- Evidence: https://huggingface.co/nvidia/Cosmos3-Super, https://research.nvidia.com/labs/cosmos-lab/cosmos3, https://github.com/NVIDIA/cosmos-framework

### Prefer `insufficient-evidence` when You need a defensible head-to-head winner across all five exact Forge candidates on a single identical benchmark protocol (identical dataset+split, identical prompt/frame inputs, identical metric definitions and pooling).

- Why: No single primary source in the research findings evaluates all five exact Forge slugs under one identical benchmark protocol naming artifact identity, dataset/split, metric definition (including pooling), and the exact evaluation protocol together; therefore a defensible single winner cannot be selected from available primary sources.
- Alternative: nvidia-cosmos-predict1-7b-text2world
- Alternative: nvidia-cosmos-predict1-7b-video2world
- Alternative: nvidia-cosmos-transfer2-5-2b
- Alternative: nvidia-cosmos3-omni-nano
- Alternative: nvidia-cosmos3-omni-super
- Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://arxiv.org/html/2501.03575v3, https://huggingface.co/nvidia/Cosmos3-Nano

## Benchmark taxonomy

### Text-to-world video generation

- Datasets:
- Metrics: PSNR (higher is better), SSIM (higher is better), Latent L2 (lower is better), FVD (lower is better), TAE-ATE (lower is better)
- Compare only when: Primary evidence must name the exact Predict1 checkpoint/variant and the exact evaluation protocol (prompt template, frame-counts, dataset name and split) in the same research source to compare numeric values.
- Compare only when: If the research source does not provide dataset name or split together with artifact identity and metric definitions, that numeric row is not comparable and must be treated as an evidence gap.

### Image-conditioned or video-conditioned world generation

- Datasets:
- Metrics: PSNR (higher is better), SSIM (higher is better), Latent L2 (lower is better), FVD (lower is better)
- Compare only when: Conditioning modality must match exactly (single-frame image vs multi-frame video vs trajectory/action conditioning).
- Compare only when: Primary evidence must explicitly map the evaluated conditioning variant to the exact Predict1 or other named artifact in the same source.

### Controllable generation from structured control-video inputs (Transfer2.5 control-specific evaluation)

- Datasets:
- Metrics:
- Compare only when: Control modality and format must be explicitly documented for the exact artifact (e.g., blur/edge/depth/segmentation and accepted input codec/format) in a primary source to allow comparison.
- Compare only when: Serving-runtime evidence is distinct from upstream-checkpoint evaluation evidence; compare only like-for-like evidence types.

### Cross-family head-to-head evaluation (Predict1 vs Transfer2.5 vs Cosmos3)

- Datasets:
- Metrics:
- Compare only when: Only compare results reported on the same benchmark protocol when a single primary source names the exact artifact identity and provides dataset split, evaluation protocol, and metric definitions together.
- Compare only when: If a single primary source does not provide identical dataset+split, identical prompt/frame inputs, metric definition, and artifact identity for each candidate, treat cross-artifact comparisons as unsupported.

## Primary sources

- [Cosmos-Predict1-7B-Text2World NGC container listing](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-text2world) — NVIDIA NGC; supports Serves as the NGC/container listing for the cosmos-predict1-7b-text2world serving artifact (serving-runtime evidence)., Documents that a Predict1 Text2World 7B serving/container artifact is provided for deployment via NIM (serving-runtime identity).
- [Cosmos-Predict1-7B-Video2World NGC container listing](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world) — NVIDIA NGC; supports Serves as the NGC/container listing for the cosmos-predict1-7b-video2world serving artifact (serving-runtime evidence)., Documents that a Predict1 Video2World 7B serving/container artifact is provided for deployment via NIM (serving-runtime identity).
- [Cosmos-Transfer2.5-2B NGC container listing](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b) — NVIDIA NGC; supports Serves as the NGC/container listing for the cosmos-transfer2.5-2b serving artifact (serving-runtime evidence)., Documents that a Transfer2.5 2B serving/container artifact is provided for deployment via NIM (serving-runtime identity).
- [Cosmos NIM introduction (docs.nvidia.com)](https://docs.nvidia.com/nim/cosmos/latest/introduction.html) — NVIDIA Docs; supports Documents that Cosmos Predict and Transfer families are available via NIM micro-services and describes family-level serving/runtime integration guidance (serving-runtime documentation evidence)., Provides high-level descriptions of Predict and Transfer model variant usage patterns referenced in decision rules (serving-runtime documentation).
- [Cosmos Predict1 docs (docs.nvidia.com)](https://docs.nvidia.com/cosmos/latest/predict1/index.html) — NVIDIA Docs; supports Provides Predict1 family documentation and describes Predict1 architecture variants and usage (upstream-checkpoint and serving-runtime documentation)., Referenced for Predict1 variant descriptions used in selection and decision rules (documentation evidence).
- [Cosmos Transfer2.5 docs (docs.nvidia.com)](https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html) — NVIDIA Docs; supports Documents that Cosmos-Transfer2.5 accepts structured input including RGB, depth, and segmentation and provides JSON-configurable controlnet_specs examples (serving-runtime/upstream-checkpoint documentation)., Provides Transfer2.5 pipeline descriptions and control-mode descriptions referenced in decision rules (documentation evidence).
- [Cosmos-Predict1 repository (GitHub)](https://github.com/nvidia-cosmos/cosmos-predict1) — NVIDIA GitHub; supports Contains Predict1 model README, inference examples, and variant notes used as upstream-checkpoint evidence for Predict1 Text2World and Video2World (upstream-checkpoint evidence).
- [Cosmos-Transfer2.5 repository (GitHub)](https://github.com/nvidia-cosmos/cosmos-transfer2.5) — NVIDIA GitHub; supports Contains Transfer2.5 repository code, README, and examples that document control modalities and provide JSON-configurable examples referenced in the dossier (upstream-checkpoint evidence).
- [Cosmos3 family code / packaging (NVIDIA cosmos-framework GitHub)](https://github.com/NVIDIA/cosmos-framework) — NVIDIA GitHub; supports Documents Cosmos3 packaging and framework materials referenced as upstream-packaging evidence for Cosmos3 Nano/Super (packaging/upstream-checkpoint evidence).
- [Cosmos Predict1 research page (NVIDIA Research)](https://research.nvidia.com/labs/cosmos-lab/cosmos-predict1) — NVIDIA Research; supports Provides upstream-checkpoint evaluation context and descriptive statements about Predict1 variants referenced in decision rules (upstream-checkpoint research evidence).
- [Cosmos Transfer2.5 research page (NVIDIA Research)](https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5) — NVIDIA Research; supports Provides upstream-checkpoint evaluation context and control-mode descriptions for Transfer2.5 referenced in decision rules (upstream-checkpoint research evidence).
- [Cosmos3 research page (NVIDIA Research)](https://research.nvidia.com/labs/cosmos-lab/cosmos3) — NVIDIA Research; supports Documents Cosmos3 family claims and references to Nano and Super upstream checkpoints used as upstream-checkpoint evidence in decision rules (upstream-checkpoint research evidence).
- [Cosmos-Predict1-7B-Text2World Hugging Face model page](https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World) — huggingface.co; supports Provides upstream model-card evidence for Cosmos-Predict1-7B-Text2World describing architecture and conditioning behavior (upstream-checkpoint/model-card evidence).
- [Cosmos-Predict1-7B-Video2World Hugging Face model page (README)](https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World) — huggingface.co; supports Provides upstream model-card evidence and README content for Cosmos-Predict1-7B-Video2World (upstream-checkpoint/model-card evidence).
- [Cosmos-Transfer2.5-2B Hugging Face model page](https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B) — huggingface.co; supports Provides upstream model-card evidence for Cosmos-Transfer2.5-2B including example output-resolution/FPS claims and model-card metadata referenced in the dossier (upstream-checkpoint/model-card evidence).
- [Cosmos3-Nano Hugging Face model page](https://huggingface.co/nvidia/Cosmos3-Nano) — huggingface.co; supports Provides upstream model-card evidence for Cosmos3-Nano describing capabilities and checkpoint identity referenced in decision rules (upstream-checkpoint/model-card evidence).
- [Cosmos3-Super Hugging Face model page](https://huggingface.co/nvidia/Cosmos3-Super) — huggingface.co; supports Provides upstream model-card evidence for Cosmos3-Super describing capabilities and checkpoint identity referenced in decision rules (upstream-checkpoint/model-card evidence).
- [Cosmos-Predict1 arXiv preprint (v2)](https://arxiv.org/html/2501.03575v2) — arXiv; supports Contains Predict1-related architecture variants and example evaluation statements referenced in the research findings (upstream-checkpoint research evidence).
- [Cosmos-Predict1 arXiv preprint (v3)](https://arxiv.org/html/2501.03575v3) — arXiv; supports Reports Predict1 Video2World numeric metrics for a Video2World evaluation variant referenced in the research findings (upstream-checkpoint research evidence).
- [Exact official starting source declared by Forge](https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard) — build.nvidia.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No single primary source in the research findings evaluates all five exact Forge slugs (nvidia-cosmos-predict1-7b-text2world, nvidia-cosmos-predict1-7b-video2world, nvidia-cosmos-transfer2-5-2b, nvidia-cosmos3-omni-nano, nvidia-cosmos3-omni-super) under one identical benchmark protocol (identical dataset name+split, identical prompt template and frame inputs, identical metric definitions and pooling/normalization).
- Evidence gap: Predict1 numeric benchmark rows (PSNR, SSIM, Latent L2, FVD, TAE-ATE) are reported in upstream sources, but the research findings do not consistently provide a single source that lists the exact Predict1 checkpoint identity together with dataset name/split and the exact prompt+frames evaluation protocol in the same source for cross-artifact comparability.
- Evidence gap: For image/video-conditioned Predict1 comparisons the research findings do not co-locate dataset splits or a canonical prompt template and pooling/normalization procedure together with numeric values and artifact identity; therefore numeric rows for image/video-conditioned evaluations are not verifiable as directly comparable across artifacts from the provided primary sources.
- Evidence gap: Cosmos3 Nano vs Super parameter-count and packaging claims are present in upstream materials, but the research findings do not contain a single authoritative primary-source mapping that unambiguously reconciles parameter-count and packaging claims to the exact Forge slug identities; do not transfer family-level parameter counts to exact Forge slugs without explicit single-source mapping.
- Evidence gap: The research findings do not provide an unambiguous Forge-to-upstream exact-version mapping string for nvidia-cosmos3-omni-nano or nvidia-cosmos3-omni-super (no single primary source in the findings explicitly documents container/NIM → exact upstream checkpoint ID mapping for these Forge slugs).
- Evidence gap: For Transfer2.5 the research findings reference JSON-configurable control specifications and examples, but do not present a single canonical, machine-readable normative specification enumerating every accepted control-input codec/format and an exhaustive input-validation schema for all serving runtimes; the exact full input codec/format schema required by Forge-serving runtimes is not fully documented in the provided primary sources.
- Evidence gap: The research findings do not uniformly enumerate a per-slug license mapping that distinguishes model-weights license versus code/runtime license for every exact Forge slug; a complete per-slug weight-vs-code license table is not present in the provided primary sources.
- Evidence gap: The research findings do not provide an authoritative per-artifact table listing maximum output duration, maximum frame count, and strict runtime output-size limits for the Predict1 NGC containers; these per-artifact operational limits are not specified in a single primary source in the findings.
- Evidence gap: Head-to-head numeric comparisons across families (Predict1 vs Transfer2.5 vs Cosmos3) are unsupported by the research findings because identical evaluation protocol elements (dataset split, prompt templates, frame sampling, pooling/normalization) are not co-located with numeric values and artifact identity in a single primary source.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 18 deterministic draft defect(s) were supplied to the audit.

- `medium` $.decisionRules[0]: $.decisionRules[0]: missing required property when Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[0]: $.decisionRules[0]: unexpected property description Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[0]: $.decisionRules[0]: unexpected property name Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[1]: $.decisionRules[1]: missing required property when Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[1]: $.decisionRules[1]: unexpected property description Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[1]: $.decisionRules[1]: unexpected property name Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[2]: $.decisionRules[2]: missing required property when Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[2]: $.decisionRules[2]: unexpected property description Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[2]: $.decisionRules[2]: unexpected property name Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[3]: $.decisionRules[3]: missing required property when Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[3]: $.decisionRules[3]: unexpected property description Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[3]: $.decisionRules[3]: unexpected property name Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[4]: $.decisionRules[4]: missing required property when Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[4]: $.decisionRules[4]: unexpected property description Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.decisionRules[4]: $.decisionRules[4]: unexpected property name Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarkTaxonomySources: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Nano: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia-cosmos-ea/Cosmos3-Super: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
