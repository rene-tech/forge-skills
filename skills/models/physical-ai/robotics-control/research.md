# Robotics Control model selection

- Category: `physical-ai`
- Group: `robotics-control`
- Independent audit: `revised`
- Researched: `2026-07-23T20:35:47.519052+00:00`

Primary-source-verified selection among exactly ten Forge robotics-control candidates that expose robot-policy checkpoints taking some combination of language, image, and sometimes robot-state inputs to produce robot actions. In scope: choosing among the exact listed checkpoints based on stated embodiment alignment, dataset/task alignment, disclosed observation and action interface details, and whether primary evidence supports protocol-compatible comparison. Out of scope: transferring family-level benchmark claims to an exact checkpoint when the findings do not state that checkpoint-specific evidence; comparing models across mismatched datasets, embodiments, action spaces, or undisclosed evaluation protocols; inferring runtime latency, safety gating, prompt templates, camera ordering, image normalization, robot-state semantics, or deployment readiness when the findings do not specify them.

## Questions to answer before selecting

- Which exact robot embodiment or platform must the policy target: SO-100/101, Google Robot, Bridge/WidowX-style manipulation, Open X-Embodiment-style mixed embodiments, or a task suite such as LIBERO, RoboCasa, RobotWin, or VLABench?
- Is the use case tied to one named dataset or benchmark family in the primary sources: SO-100/101, LIBERO, RoboCasa, RobotWin, VLABench, or an Open X-Embodiment dataset mix?
- Do you need checkpoint evidence for cross-embodiment control, or is an embodiment-specific fine-tuned checkpoint acceptable?
- What observation inputs are required by the deployment stack: how many camera views, which camera names/order, and whether robot_state is required?
- What exact image shapes are required, and are they specified by the candidate's primary source rather than inferred from a family paper or another checkpoint?
- Is robot_state required, and if so, what dimensionality and semantics must match the target robot?
- What exact action interface must match the robot: dimensionality, units, coordinate frame, absolute versus other parameterization, prediction horizon, and control frequency?
- Is the setting simulation-only, real-robot, or mixed, and does the primary evidence for the exact checkpoint cover that setting?
- Do you need only upstream-checkpoint identity evidence, or do you require checkpoint-specific benchmark evidence under a disclosed evaluation protocol?
- Are code-license and weight-license constraints acceptable for the intended deployment, and do you need Apache-2.0 versus MIT alignment?
- Do you require a compact model positioned for consumer-grade hardware, or is that claim unsupported for the exact checkpoint you are considering?
- Before comparing any two candidates, is there primary evidence that their dataset, task definition, embodiment, observation keys, action space, and evaluation procedure are actually compatible?

## Comparability rules

- Only compare benchmark results when the primary sources show the same named task family or dataset context for both exact checkpoints; dataset-family labels such as LIBERO, SO-100/101, VLABench, RobotWin, RoboCasa, Google Robot, Bridge/WidowX-style manipulation, or Open X-Embodiment are not interchangeable.
- Embodiment must match before comparing quality claims unless a source for the exact checkpoint explicitly frames it as cross-embodiment; embodiment-specific fine-tunes should not be compared as if they were generalist policies.
- Observation interfaces must match, including camera keys/counts and robot_state presence. If one source omits these details, direct comparison is unsupported.
- Action interfaces must match exactly: dimensionality, absolute versus other parameterization, prediction horizon, and any reported bounds or control frequency. If these are unspecified for either checkpoint, benchmark comparison is not valid.
- Use upstream-checkpoint evidence only to establish checkpoint identity or stated training alignment for the exact model card; do not treat family or paper-level numbers as benchmark evidence for an exact fine-tuned variant unless the findings explicitly tie them to that variant.
- Simulation and real-robot evidence are not directly comparable unless the exact sources disclose aligned evaluation conditions across candidates.
- Protocol details such as number of episodes per task, primitive versus composite suites, history window, and future prediction steps must match when comparing results; otherwise route to insufficient-evidence.
- Do not compare compactness or hardware-deployability claims across candidates unless the exact checkpoint source states them; avoid importing such claims from third-party mirrors or non-candidate checkpoints.
- For LeRobot fine-tuned variants whose model cards only state that the policy was trained and pushed with LeRobot, treat detailed preprocessing, prompt, and benchmark assumptions as evidence gaps unless another listed primary source explicitly covers the exact checkpoint or benchmark path.
- When source evidence is split between a checkpoint card and an official repository or official doc, comparison is allowed only for the details actually stated in those primary findings; unresolved fields remain evidence gaps.

## Conditional routing

### Prefer `allenai-molmoact2-so100-101` when Target embodiment is explicitly SO-100/101 and you need exact checkpoint evidence of fine-tuning on the SO-100/101 mixture with absolute joint-pose control and annotated language instructions.

- Why: The exact AllenAI checkpoint is stated to be fine-tuned on the SO-100/101 mixture with absolute joint-pose control and annotated language instructions, and is intended for SO-100/101 policy inference. The official MolmoAct2 repository also states that this checkpoint is fine-tuned on SO-100/SO-101 datasets and that MolmoAct2 deployment has been empirically verified on SO-100 and Franka DROID embodiments.
- Alternative: huggingface-lerobot-smolvla-libero
- Alternative: rail-berkeley-octo-small-1-5
- Evidence: https://huggingface.co/allenai/MolmoAct2-SO100_101, https://github.com/allenai/molmoact2

### Prefer `huggingface-lerobot-xvla-google-robot` when You need a checkpoint explicitly adapted for Google Robot platforms.

- Why: The exact LeRobot checkpoint is stated to be adapted for Google Robot platforms and to use the X-VLA foundation model. This is more checkpoint-specific than the general X-VLA base description for a Google Robot requirement.
- Alternative: huggingface-lerobot-xvla-base
- Alternative: sberroboticscenter-greenvla-2b-base
- Evidence: https://huggingface.co/lerobot/xvla-google-robot, https://huggingface.co/lerobot/xvla-base

### Prefer `huggingface-lerobot-xvla-base` when You need an X-VLA checkpoint positioned for cross-embodiment and cross-domain robot control without a narrower platform-specific adaptation requirement.

- Why: The exact xvla-base model card states that XVLA is a Vision-Language-Action foundation model using soft prompts to handle cross-embodiment and cross-domain robot control within a unified Transformer architecture.
- Alternative: huggingface-lerobot-xvla-google-robot
- Alternative: rail-berkeley-octo-small-1-5
- Evidence: https://huggingface.co/lerobot/xvla-base

### Prefer `huggingface-lerobot-smolvla-vlabench` when The task is specifically VLABench and you need checkpoint alignment to that benchmark family.

- Why: The official VLABench documentation states that a SmolVLA base model can be fine-tuned on the VLABench primitive suite via the checkpoint lerobot/smolvla_vlabench, and it specifies VLABench observation keys and a 7-dimensional bounded action output for that benchmark context.
- Alternative: huggingface-lerobot-smolvla-libero
- Alternative: huggingface-lerobot-smolvla-robocasa
- Evidence: https://huggingface.co/lerobot/smolvla_vlabench, https://huggingface.co/docs/lerobot/en/vlabench

### Prefer `insufficient-evidence` when The use case is explicitly LIBERO-style manipulation and you only have exact checkpoint identity evidence for LeRobot SmolVLA LIBERO variants rather than verified head-to-head benchmark numbers.

- Why: The exact model cards confirm the existence of smolvla_libero and smolvla_libero_plus and that they were trained and pushed using LeRobot, but the findings do not provide checkpoint-specific benchmark numbers or protocol details to justify a primary-evidence winner between the two exact LIBERO variants.
- Alternative: huggingface-lerobot-smolvla-libero
- Alternative: huggingface-lerobot-smolvla-libero-plus
- Evidence: https://huggingface.co/lerobot/smolvla_libero, https://huggingface.co/lerobot/smolvla_libero_plus

### Prefer `huggingface-lerobot-smolvla-robocasa` when The task is specifically RoboCasa-style manipulation and you want the exact SmolVLA fine-tuned variant aligned to that dataset family.

- Why: The exact smolvla_robocasa model card identifies this checkpoint as the RoboCasa variant and states that it was trained and pushed with LeRobot. This is the strongest checkpoint-specific alignment in the findings for a RoboCasa requirement.
- Alternative: huggingface-lerobot-smolvla-vlabench
- Alternative: huggingface-lerobot-smolvla-libero
- Evidence: https://huggingface.co/lerobot/smolvla_robocasa

### Prefer `huggingface-lerobot-smolvla-robotwin` when The task is specifically RobotWin and you want the exact SmolVLA fine-tuned variant aligned to that dataset family.

- Why: The exact smolvla_robotwin model card identifies this checkpoint as the RobotWin variant and states that it was trained and pushed with LeRobot. The findings provide no stronger competing checkpoint-specific RobotWin evidence among the listed candidates.
- Alternative: huggingface-lerobot-smolvla-libero
- Alternative: huggingface-lerobot-smolvla-vlabench
- Evidence: https://huggingface.co/lerobot/smolvla_robotwin

### Prefer `rail-berkeley-octo-small-1-5` when You need a small generalist policy with explicitly stated observation shapes, language-token shapes, 7-dimensional actions, and Open X-Embodiment training mix evidence.

- Why: The exact Octo Small 1.5 model card states it is a 27M-parameter Transformer trained on a mix of Open X-Embodiment datasets, with observation specifications for image_primary and image_wrist, language token shapes, a history window up to 2 timesteps, and 7-dimensional actions predicted 4 steps into the future using a diffusion policy.
- Alternative: huggingface-lerobot-xvla-base
- Alternative: sberroboticscenter-greenvla-2b-base
- Evidence: https://huggingface.co/rail-berkeley/octo-small-1.5

### Prefer `sberroboticscenter-greenvla-2b-base` when The use case targets Bridge/WidowX-style manipulation and you want the exact GreenVLA base checkpoint identified for that family.

- Why: The exact GreenVLA-2b-base model card states that it is a lightweight base checkpoint of the Green-VLA family with approximately 2 billion parameters, pretrained on general-domain and robotics data, and the expected-scope description identifies it for Bridge/WidowX-style manipulation. The findings do not provide a stronger exact-checkpoint benchmark match from another listed candidate for that named platform family.
- Alternative: rail-berkeley-octo-small-1-5
- Alternative: huggingface-lerobot-xvla-google-robot
- Evidence: https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base

## Benchmark taxonomy

### SO-100/101 policy inference and embodiment-aligned fine-tuning

- Datasets: SO-100/101 mixture, MolmoAct2-SO100/101 corpus
- Metrics: Task-specific policy success metrics as reported by the exact evaluation source; direction higher is better, Evidence gap: the findings do not provide a verified numeric metric name/value for the exact Forge checkpoint
- Compare only when: Use only the exact SO-100/101-aligned checkpoint or another candidate with primary evidence on the same embodiment and task family.
- Compare only when: Match embodiment, action parameterization, and language-conditioning setup.
- Compare only when: For MolmoAct2-SO100_101, preserve that the checkpoint is stated to use absolute joint-pose control with annotated language instructions.
- Compare only when: Do not compare with checkpoints evaluated only on other suites such as VLABench, LIBERO, Google Robot, or Open X-Embodiment without explicit aligned evidence.

### LIBERO-aligned SmolVLA fine-tuned policy selection

- Datasets: HuggingFaceVLA/libero, full LIBERO training mixture
- Metrics: Evidence gap: the findings do not provide exact checkpoint-specific LIBERO metric names or values for smolvla_libero or smolvla_libero_plus
- Compare only when: Restrict comparison to checkpoints whose primary sources explicitly tie them to LIBERO.
- Compare only when: Do not import benchmark numbers from non-candidate SmolVLA variants or third-party mirrors.
- Compare only when: Because the findings only confirm checkpoint identity and LeRobot training for the exact LIBERO variants, comparisons between smolvla_libero and smolvla_libero_plus require additional primary protocol evidence.

### RoboCasa-aligned SmolVLA fine-tuned policy selection

- Datasets: RoboCasa
- Metrics: Evidence gap: the findings do not provide exact checkpoint-specific RoboCasa metric names or values for smolvla_robocasa
- Compare only when: Use only exact checkpoints explicitly identified as RoboCasa variants.
- Compare only when: Do not compare to LIBERO, VLABench, RobotWin, or SO-100/101 outcomes without shared protocol evidence.
- Compare only when: Observation, robot_state, and action details remain unresolved unless disclosed by the exact source.

### RobotWin-aligned SmolVLA fine-tuned policy selection

- Datasets: RobotWin
- Metrics: Evidence gap: the findings do not provide exact checkpoint-specific RobotWin metric names or values for smolvla_robotwin
- Compare only when: Use only exact checkpoints explicitly identified as RobotWin variants.
- Compare only when: Do not infer action semantics, robot-state semantics, or camera layout from other SmolVLA variants.
- Compare only when: Cross-suite comparison is unsupported without matched benchmark protocol evidence.

### VLABench primitive/composite language-conditioned manipulation evaluation

- Datasets: VLABench/vlabench_primitive_ft_lerobot_video, VLABench/vlabench_composite_ft_lerobot_video
- Metrics: Episodes per task under the recommended evaluation protocol: 10 episodes per task, Suite totals under the recommended evaluation protocol: 210 primitive episodes and 220 composite episodes, Evidence gap: the findings do not provide a checkpoint-specific success metric name/value for smolvla_vlabench
- Compare only when: Use the official VLABench observation keys: observation.state, observation.images.image, observation.images.second_image, and observation.images.wrist_image.
- Compare only when: Use the VLABench action output format: Box shape (7,) with values in [-1, 1].
- Compare only when: Keep primitive and composite suites distinct unless both sides are evaluated on the same suite.
- Compare only when: Use the recommended 10 episodes per task protocol when comparing results.
- Compare only when: The findings tie lerobot/smolvla_vlabench to fine-tuning on the VLABench primitive suite; broader claims need explicit exact-checkpoint evidence.

### X-VLA checkpoint selection for cross-embodiment or Google Robot adaptation

- Datasets: Google Robot, Evidence gap: the findings do not provide a named benchmark dataset for xvla-base beyond cross-embodiment/cross-domain positioning
- Metrics: Evidence gap: the findings do not provide exact checkpoint-specific numeric benchmark metrics or values for xvla-base or xvla-google-robot
- Compare only when: Treat xvla-base as a cross-embodiment/cross-domain foundation checkpoint based on its exact model card wording.
- Compare only when: Treat xvla-google-robot as the platform-adapted checkpoint for Google Robot platforms.
- Compare only when: Do not compare xvla-base and xvla-google-robot numerically without a shared disclosed evaluation protocol.

### Open X-Embodiment-style multimodal policy inference for Octo Small 1.5

- Datasets: Open X-Embodiment dataset mix
- Metrics: 7-dimensional action prediction 4 steps into the future, History window up to 2 timesteps, Evidence gap: the findings do not provide a benchmark score name/value for the exact octo-small-1.5 checkpoint
- Compare only when: Use Octo Small observation specification exactly as stated: image_primary shape (batch, history_window, 256, 256, 3) and image_wrist shape (batch, history_window, 128, 128, 3).
- Compare only when: Use the stated task-language shapes: attention_mask (batch, 16) and input_ids (batch, 16).
- Compare only when: Keep comparisons to systems with matched observation keys, history window assumptions, and 7-dimensional action interface.
- Compare only when: Do not compare Octo Small benchmark quality against candidates lacking equally specific protocol disclosures.

### GreenVLA-2b-base base-checkpoint selection for multi-embodiment pretraining context

- Datasets: Evidence gap: the findings do not name the exact component datasets for GreenVLA-2b-base, only over 3,000 hours of demonstrations across multiple embodiments
- Metrics: Approximate parameter scale: 2 billion parameters, Evidence gap: the findings do not provide exact checkpoint-specific benchmark metrics or values for GreenVLA-2b-base
- Compare only when: Treat GreenVLA-2b-base as a base pretrained checkpoint rather than an embodiment-specific R1/R2 adapted checkpoint.
- Compare only when: Do not substitute metrics from GreenVLA 4B/5B or R1/R2 variants for the exact 2b-base checkpoint.
- Compare only when: Comparison to other candidates requires matched embodiment and evaluation evidence that the findings do not currently provide.

## Primary sources

- [MolmoAct2-SO100_101 model card](https://huggingface.co/allenai/MolmoAct2-SO100_101) — AllenAI on Hugging Face; supports Exact checkpoint identity for allenai-molmoact2-so100-101, MolmoAct2-SO100_101 is intended for SO-100/101 policy inference, MolmoAct2-SO100_101 is fine-tuned on the SO-100/101 mixture with absolute joint-pose control and annotated language instructions
- [MolmoAct2 official repository](https://github.com/allenai/molmoact2) — Allen Institute for AI; supports MolmoAct2 checkpoint family training-alignment details including SO-100/101 and LIBERO references, MolmoAct2 supports out-of-the-box deployment on named embodiments and has empirical verification on SO-100 and Franka DROID, MolmoAct2 is integrated into LeRobot as a policy implementation
- [MolmoAct2 SO100/101 paper HTML](https://arxiv.org/html/2605.02881v1) — arXiv; supports SO-100/101 corpus scale and provenance, Primary evidence for the MolmoAct2 SO-100/101 dataset context
- [SmolVLA Libero model card](https://huggingface.co/lerobot/smolvla_libero) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-smolvla-libero, The policy was trained and pushed to the Hub using LeRobot
- [SmolVLA Libero Plus model card](https://huggingface.co/lerobot/smolvla_libero_plus) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-smolvla-libero-plus, Model card states SmolVLA framing and LeRobot training/publishing context
- [SmolVLA RoboCasa model card](https://huggingface.co/lerobot/smolvla_robocasa) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-smolvla-robocasa, Model card states SmolVLA framing and LeRobot training/publishing context
- [SmolVLA RobotWin model card](https://huggingface.co/lerobot/smolvla_robotwin) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-smolvla-robotwin, Model card states the policy was trained and pushed with LeRobot
- [SmolVLA VLABench model card](https://huggingface.co/lerobot/smolvla_vlabench) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-smolvla-vlabench
- [LeRobot VLABench documentation](https://huggingface.co/docs/lerobot/en/vlabench) — Hugging Face LeRobot; supports Primary benchmark protocol details for VLABench in LeRobot, Observation keys, action shape, task counts, and recommended episode counts for VLABench, Checkpoint linkage from SmolVLA base to lerobot/smolvla_vlabench fine-tuning context
- [X-VLA Base model card](https://huggingface.co/lerobot/xvla-base) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-xvla-base, XVLA is framed as a cross-embodiment and cross-domain VLA foundation model using soft prompts
- [X-VLA Google Robot model card](https://huggingface.co/lerobot/xvla-google-robot) — LeRobot on Hugging Face; supports Exact checkpoint identity for huggingface-lerobot-xvla-google-robot, Checkpoint is adapted for Google Robot platforms and uses the X-VLA foundation model
- [Octo Small 1.5 model card](https://huggingface.co/rail-berkeley/octo-small-1.5) — RAIL Berkeley on Hugging Face; supports Exact checkpoint identity for rail-berkeley-octo-small-1-5, Observation shapes, language token shapes, history window, action dimensionality, and Open X-Embodiment training mix for the exact checkpoint
- [Octo official repository](https://github.com/octo-models/octo) — Octo authors; supports Primary project documentation for Octo capabilities and fine-tuning modes, Context for Open X-Embodiment pretraining and multimodal conditioning in the Octo project
- [GreenVLA-2b-base model card](https://huggingface.co/SberRoboticsCenter/GreenVLA-2b-base) — SberRoboticsCenter on Hugging Face; supports Exact checkpoint identity for sberroboticscenter-greenvla-2b-base, Approximate parameter scale and multi-embodiment pretraining context for GreenVLA-2b-base

## Evidence gaps

- Evidence gap: The findings do not provide exact prompt templates or instruction formatting for any of the ten exact Forge checkpoints.
- Evidence gap: The findings do not provide a complete camera configuration or camera ordering specification for most checkpoints; only VLABench observation keys and Octo Small observation names/shapes are stated.
- Evidence gap: Robot-state dimensionality and semantics are not specified in the findings for most exact checkpoints, including the SmolVLA fine-tuned variants, X-VLA checkpoints, and GreenVLA-2b-base.
- Evidence gap: Action-space units, coordinate frames, and control rates are mostly unspecified for the exact candidates. Verified exceptions are MolmoAct2-SO100_101 using absolute joint-pose control and VLABench's Box(7,) in [-1,1] benchmark context; these should not be generalized to other checkpoints.
- Evidence gap: The findings do not provide checkpoint-specific benchmark metric values for smolvla_libero, smolvla_libero_plus, smolvla_robocasa, smolvla_robotwin, smolvla_vlabench, xvla-base, xvla-google-robot, or GreenVLA-2b-base.
- Evidence gap: The findings do not provide a primary head-to-head comparison protocol among the ten listed candidates, so cross-family routing should default to task and embodiment alignment rather than claimed numeric superiority.
- Evidence gap: For LIBERO, the findings confirm LIBERO alignment for exact SmolVLA variants and family-level MolmoAct2 LIBERO training context, but do not provide exact checkpoint-specific benchmark numbers for the listed ten candidates.
- Evidence gap: For RoboCasa and RobotWin, the findings confirm checkpoint identity for the exact SmolVLA variants but do not disclose their precise evaluation conditions, image preprocessing, or metric definitions.
- Evidence gap: For X-VLA, the findings support cross-embodiment positioning for xvla-base and platform adaptation for xvla-google-robot, but do not provide exact benchmark datasets, metric values, or protocol controls for direct comparison to other candidates.
- Evidence gap: For GreenVLA-2b-base, the findings provide approximate parameter count and pretraining-hours context but not exact component datasets, observation schema, action schema, or exact benchmark results for the listed checkpoint.
- Evidence gap: The findings do not separate model-weight license versus code license for every candidate beyond the source scope descriptions and some repository facts; deployment decisions requiring precise license decomposition need further checkpoint-specific primary evidence.
- Evidence gap: The findings do not provide verified real-robot deployment constraints, latency, safety gating, privacy handling, or post-action validation procedures for most exact checkpoints.
- Evidence gap: Some potentially relevant materials in the findings are explicitly secondary or unofficial for this audit scope, so related claims were not used for decision evidence even when they mention similar model families.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://arxiv.org/abs/2506.01844 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` decision-rule evidence URL is absent from $.sources: decision-rule evidence URL is absent from $.sources: https://huggingface.co/docs/lerobot/en/vlabench Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
