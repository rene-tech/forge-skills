# Video Generation model selection

- Category: `general`
- Group: `video-generation`
- Independent audit: `revised`
- Researched: `2026-07-23T23:49:40.999031+00:00`

Compare and select among the exact Forge slugs listed for video generation including: text->video, image->video, and text+image->video+audio where supported. Scope: only facts explicitly present in the assembled primary sources (Hugging Face model pages, official GitHub repository paths that host or document the named checkpoint/variant, and canonical arXiv preprints). Out of scope: any performance, configuration, license, modality, or operational claim not explicitly documented in those primary sources; such missing items are recorded in evidenceGaps.

## Questions to answer before selecting

- What is the canonical primary source URL for this exact Forge slug (Hugging Face model page or official GitHub repo path or arXiv/publisher PDF) and which exact checkpoint name/versionKey is cited there?
- What licenses and explicit usage restrictions are documented by the canonical primary sources for this exact slug and for the model weights vs repository/code?
- Which input modalities and declared output modalities does the canonical primary source state for this exact slug (text, image, audio, video)?
- What input shapes or limits (resolution, frame count, FPS, latent shape or VAE compression) are declared by the canonical primary source for this exact slug?
- Which official inference configurations (documented sampler, documented step counts, documented guidance/CFG scale, and any documented postprocessors or upscalers) are specified for this exact slug by the canonical primary sources?
- Which evaluation numbers (datasets, splits, metrics, prompt templates, step counts, video length/FPS, and any postprocessors) are published for this exact slug and to which exact checkpoint/variant are they attributed?
- Does the canonical primary source provide official fine‑tuning/adaptation instructions (LoRA, trainer scripts, README) that apply to this exact slug?
- Does the canonical primary source claim native audio generation or synchronized audio/video, and if so which evaluation metrics and numeric values are supplied for that exact slug?
- Is the Forge slug delivered/mapped as a Diffusers pipeline or other wrapper and does the canonical primary source document that mapping for the exact checkpoint/variant?

## Comparability rules


## Conditional routing

### Prefer `genmo-mochi-1-preview` when Need the Mochi 1 exact preview checkpoint and repository artifacts (AsymmDiT architecture, 10B parameter claim, 480p example behavior and AsymmVAE latent compression described on the model page).

- Why: The Genmo Mochi 1 preview Hugging Face model page documents Mochi 1 as a 10B-parameter model built on AsymmDiT and the HF-hosted repository and README show example generation shapes (480p/84 frames export) and utility calls; the GitHub repository hosts demo/training materials referenced by the model card.
- Alternative: wan-ai-wan2-2-t2v-a14b
- Alternative: zai-org-cogvideox-2b
- Evidence: https://huggingface.co/genmo/mochi-1-preview, https://github.com/genmoai/mochi, https://huggingface.co/genmo/mochi-1-preview/blob/refs%2Fpr%2F24/README.md

### Prefer `hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v` when Need a documented HunyuanVideo-1.5 480P T2V variant with the inference steps and cfg/flow parameters the primary source documents.

- Why: The Tencent HunyuanVideo-1.5 Hugging Face model page and the Tencent-Hunyuan GitHub repository document a 480P T2V variant and the model card/example code shows num_inference_steps set to 50 and num_frames set to 121 in the documented example.
- Alternative: genmo-mochi-1-preview
- Alternative: wan-ai-wan2-2-ti2v-5b
- Evidence: https://huggingface.co/tencent/HunyuanVideo-1.5, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5, https://arxiv.org/abs/2511.18870

### Prefer `lightricks-ltx-2-3-sglang` when Need an LTX-2.3 checkpoint documented as an audio+video model with documented inference-stage settings.

- Why: The Lightricks LTX-2.3 Hugging Face model page documents LTX-2.3 as an updated LTX-2 family model with improved audio/visual quality; the LTX-2 repository files in the assembled sources document that LTX-2 supports synchronized audio/video and the project README/materials describe staged inference modes.
- Alternative: lightricks-ltx-video
- Alternative: openmoss-team-mova-360p-sglang
- Evidence: https://huggingface.co/Lightricks/LTX-2.3, https://github.com/Lightricks/LTX-2

### Prefer `lightricks-ltx-video` when Need the Lightricks Diffusers pipeline wrapper variant and repository mapping for LTX-Video (pipeline wrapper/LoRA/control model documentation).

- Why: The Lightricks LTX-Video Hugging Face model page and the official ltx-video GitHub repository are the canonical locations in the assembled sources documenting the LTX-Video pipeline mapping and repository artifacts.
- Alternative: lightricks-ltx-2-3-sglang
- Alternative: genmo-mochi-1-preview
- Evidence: https://huggingface.co/Lightricks/LTX-Video, https://github.com/Lightricks/ltx-video

### Prefer `openmoss-team-mova-360p-sglang` when Need a MOVA variant documented for native synchronized video+audio generation at the 360p checkpoint documented in the MOVA repository.

- Why: The OpenMOSS MOVA GitHub repository and the MOVA-360p Hugging Face model page in the assembled sources document MOVA as synthesizing video and audio simultaneously and expose the 360p checkpoint for Diffusers usage.
- Alternative: openmoss-team-mova-720p-sglang
- Alternative: lightricks-ltx-2-3-sglang
- Evidence: https://github.com/OpenMOSS/MOVA, https://huggingface.co/OpenMOSS-Team/MOVA-360p

### Prefer `openmoss-team-mova-720p-sglang` when Need the higher-resolution MOVA checkpoint variant documented in the paper and model pages for 720p evaluation claims.

- Why: The MOVA-720p Hugging Face model page, the MOVA GitHub repository, and the MOVA arXiv preprint in the assembled sources document the 720p checkpoint, modality support, and attribute numeric audio/video evaluations to MOVA variants.
- Alternative: openmoss-team-mova-360p-sglang
- Alternative: lightricks-ltx-2-3-sglang
- Evidence: https://huggingface.co/OpenMOSS-Team/MOVA-720p, https://github.com/OpenMOSS/MOVA, https://arxiv.org/abs/2602.08794

### Prefer `skywork-skyreels-v2-df-1-3b-540p` when Require the SkyReels-V2 DF-1.3B-540P pipeline or paper-documented pipeline behavior for SkyReels-V2 claims.

- Why: The SkyReels-V2 Hugging Face model page for the DF-1.3B-540P variant documents the AutoRegressive Diffusion-Forcing architecture and recommended generation shapes (recommended resolution and frame counts) for that exact variant in the assembled sources.
- Alternative: genmo-mochi-1-preview
- Alternative: wan-ai-wan2-2-t2v-a14b
- Evidence: https://huggingface.co/Skywork/SkyReels-V2-DF-1.3B-540P

### Prefer `stabilityai-stable-video-diffusion-img2vid-xt` when Require the Stable Video Diffusion Img2Vid-XT canonical checkpoint and example image->video generation settings documented by the model page.

- Why: The Stability AI Hugging Face model page for Stable Video Diffusion Img2Vid-XT documents the checkpoint identifier and provides documented runtime example behavior (timing and watermarking) in the assembled sources.
- Alternative: wan-ai-wan2-2-ti2v-5b
- Alternative: wan-ai-wan2-2-ti2v-5b-sglang
- Evidence: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt

### Prefer `wan-ai-wan2-2-t2v-a14b` when Need the Wan2.2 T2V A14B Mixture-of-Experts checkpoint with the documented resolution/length example claims.

- Why: The Wan2.2 T2V-A14B Hugging Face model page and the Wan2.2 GitHub repository document the Mixture-of-Experts design and state supported resolutions and example generation settings for the A14B checkpoint in the assembled sources.
- Alternative: wan-ai-wan2-2-ti2v-5b
- Alternative: skywork-skyreels-v2-df-1-3b-540p
- Evidence: https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B, https://github.com/Wan-Video/Wan2.2

### Prefer `wan-ai-wan2-2-ti2v-5b` when Need the Wan2.2 TI2V 5B documented dense/high-compression TI2V checkpoint that the Wan2.2 sources describe as supporting 720P@24FPS and combined text/image conditioning.

- Why: The Wan2.2 TI2V-5B Hugging Face model page and the Wan2.2 GitHub repository document TI2V-5B and state that it supports 720P video generation at 24 FPS and combined text/image conditioning in the assembled sources.
- Alternative: wan-ai-wan2-2-ti2v-5b-sglang
- Alternative: stabilityai-stable-video-diffusion-img2vid-xt
- Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B, https://github.com/Wan-Video/Wan2.2

### Prefer `wan-ai-wan2-2-ti2v-5b-sglang` when Need the documented Wan2.2 TI2V 5B variant specifically cited for image+text conditioning and Diffusers mapping.

- Why: The Wan2.2 TI2V-5B Hugging Face model page and the Wan2.2 GitHub repository document combined text+image modality support and capability claims for the TI2V-5B variant in the assembled sources.
- Alternative: wan-ai-wan2-2-ti2v-5b
- Alternative: zai-org-cogvideox-2b
- Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B, https://github.com/Wan-Video/Wan2.2

### Prefer `zai-org-cogvideox-2b` when Need a small-parameter (2B) CogVideoX Diffusers checkpoint documented for constrained compute/prototyping with sampling frame counts and prompt length limits.

- Why: The zai-org CogVideoX-2b Hugging Face model page documents CogVideoX-2B as a 2B-parameter text->video model and the THUDM SAT README in the assembled sources documents example sampling/frame-count guidance for CogVideo-family inference examples.
- Alternative: genmo-mochi-1-preview
- Alternative: wan-ai-wan2-2-ti2v-5b
- Evidence: https://huggingface.co/zai-org/CogVideoX-2b, https://github.com/THUDM/CogVideo/blob/main/sat/README.md

## Benchmark taxonomy

### text-to-video generation

- Datasets: VBench (text-to-video benchmark suite)
- Metrics: Fréchet Video Distance (FVD), Fréchet Video Motion Distance (FVMD), CLIPScore (frame or video-level), LPIPS, Inception Score (IS)
- Compare only when: Match exact checkpoint/variant name and any resolution/frame count/step counts documented in the cited primary source.

### image-to-video generation

- Datasets: VBench++ Image Suite
- Metrics: FVD, FVMD, CLIPScore, LPIPS
- Compare only when: Match the exact image->video checkpoint and any documented frame count/resolution/inference settings present in the canonical primary source for that checkpoint.

### text+image -> video with native audio output (audio-video synthesis)

- Datasets: VBench (audio-capable evaluation subsets where provided by primary sources)
- Metrics: DNSMOS / MOS (audio quality), LSE-D / LSE-C (lip-sync / semantic alignment), FVD, CLIPScore (when reported together with audio metrics)
- Compare only when: Match the exact MOVA or LTX checkpoint variant (360p or 720p, LTX-2.3) and only compare reported audio/video numbers when the primary source attributes them to that exact variant.

## Primary sources

- [Genmo Mochi 1 Preview — Hugging Face model card](https://huggingface.co/genmo/mochi-1-preview) — Genmo / Hugging Face; supports Mochi 1 is a 10 billion parameter diffusion model built on the Asymmetric Diffusion Transformer (AsymmDiT) architecture., The initial release of Mochi 1 generates videos at 480p resolution., Mochi 1 uses an asymmetric encoder-decoder called AsymmVAE that compresses videos 128× smaller with 8×8 spatial and 6× temporal compression to a 12-channel latent space., In edge cases with extreme motion, Mochi 1 may produce minor warping and distortions.
- [Mochi GitHub repository (genmoai/mochi)](https://github.com/genmoai/mochi) — genmoai (GitHub); supports The Mochi repository hosts the Mochi preview model artifacts and demo/training materials., Mochi 1 preview is released under the Apache 2.0 license., The repository notes example consumer-GPU support and community fine-tuning notes.
- [Mochi README (cited revision/file)](https://huggingface.co/genmo/mochi-1-preview/blob/refs%2Fpr%2F24/README.md) — Genmo / Hugging Face (repo file); supports The example code for Mochi 1 shows loading a bf16 variant and calls such as pipe.enable_model_cpu_offload() and pipe.enable_vae_tiling()., The example generates 84 frames and exports the video at 30 fps in the cited README example.
- [HunyuanVideo-1.5 — Hugging Face model page](https://huggingface.co/tencent/HunyuanVideo-1.5) — Tencent-Hunyuan / Hugging Face; supports HunyuanVideo-1.5 is documented as a video generation model and the model page includes example code showing num_inference_steps set to 50 and num_frames set to 121 in a documented example., HunyuanVideo-1.5 provides multiple variants including 480P-T2V as shown by the model card and diffusers mapping pages.
- [HunyuanVideo-1.5 GitHub repository](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) — Tencent-Hunyuan (GitHub); supports The HunyuanVideo-1.5 repository hosts model code and documents multiple variants including 480P-T2V., Repository materials accompany the model page's example usage and recommended inference shapes.
- [HunyuanVideo-1.5 technical report — arXiv](https://arxiv.org/abs/2511.18870) — arXiv (Tencent-Hunyuan authors); supports The HunyuanVideo-1.5 Technical Report is archived on arXiv with identifier 2511.18870 and is part of the assembled primary sources.
- [Lightricks LTX-2.3 model card — Hugging Face](https://huggingface.co/Lightricks/LTX-2.3) — Lightricks / Hugging Face; supports LTX-2.3 is documented on Hugging Face and described as an updated version of LTX-2 with improved audio and visual quality.
- [LTX-2 repository (Lightricks)](https://github.com/Lightricks/LTX-2) — Lightricks (GitHub); supports LTX-2 is described in the repository materials as a DiT-based audio-video foundation model that includes synchronized audio and video generation capabilities.
- [LTX-Video Hugging Face model page](https://huggingface.co/Lightricks/LTX-Video) — Lightricks / Hugging Face; supports LTX-Video is a DiT-based video generation model and the Hugging Face model page documents example generation settings and modality claims in the assembled sources.
- [LTX-Video GitHub repository (ltx-video)](https://github.com/Lightricks/ltx-video) — Lightricks (GitHub); supports The ltx-video repository hosts code and documents example generation shapes/frames and released control/distilled model artifacts.
- [MOVA GitHub repository (OpenMOSS)](https://github.com/OpenMOSS/MOVA) — OpenMOSS (GitHub); supports The MOVA repository hosts code and workflow materials and documents MOVA as synthesizing video and audio simultaneously and references 360p and 720p checkpoints.
- [MOVA-360p model page — Hugging Face](https://huggingface.co/OpenMOSS-Team/MOVA-360p) — OpenMOSS / Hugging Face; supports The MOVA-360p model page documents that the 360p checkpoint can be used with Diffusers and related tooling and is part of the assembled primary sources.
- [MOVA-720p model page — Hugging Face](https://huggingface.co/OpenMOSS-Team/MOVA-720p) — OpenMOSS / Hugging Face; supports MOVA-720p model page documents the 720p checkpoint, architecture description, and modality support attributed to the 720p variant.
- [MOVA technical paper — arXiv](https://arxiv.org/abs/2602.08794) — arXiv (OpenMOSS authors); supports The MOVA technical report is archived on arXiv with identifier 2602.08794 and the paper reports numeric audio/video evaluations attributed to MOVA variants in the assembled sources.
- [SkyReels-V2 DF 1.3B 540P — Hugging Face model page](https://huggingface.co/Skywork/SkyReels-V2-DF-1.3B-540P) — Skywork / Hugging Face; supports SkyReels V2 employs an AutoRegressive Diffusion-Forcing architecture and the SkyReels V2 1.3B-540P variant documents recommended resolution and frame-count guidance for that exact variant in the assembled sources.
- [Stable Video Diffusion Img2Vid XT — Hugging Face model page](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) — Stability AI / Hugging Face; supports The Stable Video Diffusion Img2Vid-XT model page documents example generation timing and that image-level watermarking is enabled by default on the documented checkpoint in the assembled sources.
- [Wan2.2 GitHub repository (Wan-Video)](https://github.com/Wan-Video/Wan2.2) — Wan-Video (GitHub); supports The Wan2.2 repository hosts Wan2.2 model artifacts and documents model variants including T2V-A14B and TI2V-5B and technical details about VAE compression and supported resolutions for those variants.
- [Wan2.2 T2V A14B — Hugging Face model page](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B) — Wan-AI / Hugging Face; supports Wan2.2 T2V-A14B model page documents Mixture-of-Experts architecture claims and example generation settings including support for 480P and 720P resolutions.
- [Wan2.2 TI2V 5B — Hugging Face model page](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B) — Wan-AI / Hugging Face; supports Wan2.2 TI2V-5B model page documents that the TI2V-5B variant supports 720P video generation at 24 FPS and combined text/image conditioning and describes the high-compression VAE used.
- [CogVideoX-2b — Hugging Face model page](https://huggingface.co/zai-org/CogVideoX-2b) — zai-org / Hugging Face; supports CogVideoX-2B model page documents that CogVideoX-2B is a 2B-parameter open-source text-to-video model and that it can be deployed via the Hugging Face Diffusers library.
- [CogVideo SAT README (THUDM repository)](https://github.com/THUDM/CogVideo/blob/main/sat/README.md) — THUDM (GitHub); supports The THUDM SAT README documents CogVideo checkpoint composition and example sampling frame counts used for inference examples.
- [Exact official starting source declared by Forge](https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://github.com/Lightricks/LTX-Video) — github.com; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/docs/diffusers/v0.37.1/en/api/pipelines/skyreels_v2) — huggingface.co; supports Forge-to-upstream exact-version identity
- [Exact official starting source declared by Forge](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers) — huggingface.co; supports Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: There is no single canonical primary source in the assembled sources that provides standardized, head-to-head benchmark evaluations across all listed Forge slugs on the same dataset/splits/metric implementations; reproducing numeric cross-model comparisons requires running matched re-evaluations.
- Evidence gap: The dataset string 'VBench (text-to-video benchmark suite)' and 'VBench++ Image Suite' appear in the dossier taxonomy but were not found in any of the assembled primary sources; the canonical primary sources do not provide a shared dataset name or cross-model prompt corpus applicable to all listed checkpoints.
- Evidence gap: Exact metric implementation details required to reproduce reported numeric metrics (the precise feature extractor/checkpoint used to compute FVD or I3D features, pooling method, normalization, and exact DNSMOS/MOS pipeline config) are not consistently documented across the assembled primary sources; where a primary source omits these details reproduction requires protocol decisions referencing non-canonical artifacts.
- Evidence gap: Some per-model inference configuration items referenced in the draft (e.g., explicit sampler name, diffusion step counts, guidance/CFG scales for every checkpoint) are missing or only partially documented for some checkpoints in the assembled primary sources. Examples: Stable Video Diffusion Img2Vid-XT's canonical page documents timing and watermarking but does not provide a complete, harmonized list of sampler/step/CFG settings across all models.
- Evidence gap: For several models the primary sources do not provide separate, explicit license statements that distinguish model weights license versus repository/code license in a manner that covers all Forge slugs; where a primary source omits this separation the dossier records the omission.
- Evidence gap: For audio-capable models (MOVA, LTX) the assembled primary sources document claims of native audio synthesis and list evaluation metrics in the MOVA paper, but the primary sources do not uniformly provide full metric implementation details (e.g., exact DNSMOS extractor/checkpoint and pooling) necessary for reproduction.
- Evidence gap: There is no canonical, shared prompt corpus or exact prompt template across the assembled primary sources that would permit direct numeric comparisons without re-running evaluations under harmonized protocols.
- Evidence gap: comparabilityRules is empty; the dossier-level comparability conditions that must match before comparing benchmark values are not defined in primary sources and must be specified to permit cross-model comparisons.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25].primary must be true: $.sources[25].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[28] uses forbidden secondary host emergentmind.com: $.sources[28] uses forbidden secondary host emergentmind.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[28].primary must be true: $.sources[28].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[33].primary must be true: $.sources[33].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[34].primary must be true: $.sources[34].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[35].primary must be true: $.sources[35].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://ltx.io/blog/training-your-first-lora-on-ltx Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://ltx-23.app/blog/ltx-23-lora-training Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://github.com/Lightricks/LTX-Video: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/docs/diffusers/v0.37.1/en/api/pipelines/skyreels_v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
