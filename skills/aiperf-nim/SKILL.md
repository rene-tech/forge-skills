---
name: aiperf-nim
description: Benchmark NVIDIA NIM endpoints with NVIDIA AIPerf. Use for NIM or OpenAI-compatible inference latency, throughput, TTFT, inter-token latency, SLO goodput, concurrency/request-rate sweeps, reproducible performance comparisons, and result interpretation. Covers endpoint authentication, tokenizer and NIM profile matching, streaming, synthetic versus real workloads, and Kubernetes/Dynamo handoffs. Distinguish performance benchmarking from model accuracy and MLPerf compliance.
---

# AIPerf for NVIDIA NIM

Community-authored operating skill based on NVIDIA documentation. The bundled
configuration is validated with AIPerf **0.13.0**; check the installed version and
its help before adapting commands. NVIDIA's separately installed Dynamo and
Kubernetes skills remain unchanged upstream copies.

## Establish the experiment

1. Identify the existing endpoint, owner, served model ID, workload, measurement
   goal, allowed load and runtime budget. Use the current authorization; do not
   create a NIM deployment or run a load sweep merely to prepare a benchmark.
2. Read the endpoint's actual model/API contract. For a compatible NIM LLM,
   discover the served ID through `/v1/models`; use the matching tokenizer and
   revision, not a guessed model alias. Check readiness through the supported
   NIM route or the serving owner's health signal.
3. Record NIM image digest, backend and selected profile, model/checkpoint,
   GPU/count/MIG, precision, TP/PP, replicas, scheduler/cache settings and client
   location. Missing fields remain unknown. Preserve explicit customer settings.
4. Define prompt/output distributions, real or synthetic data, streaming,
   sampling/stopping, prefix reuse, warmup, SLOs and termination conditions before
   comparing runs. Report the actual token lengths and failures afterward.

Read [references/nim-workflow.md](references/nim-workflow.md) for setup,
authentication, bounded commands, sweeps and deployment-specific checks.

## Prepare and validate without submitting inference

- Isolate the client dependency: `uv venv --python 3.12 .venv-aiperf`, then
  `uv pip install --python .venv-aiperf/bin/python 'aiperf==0.13.0'`.
- Copy [assets/nim-chat.yaml](assets/nim-chat.yaml) into the run directory.
  Supply the served model, tokenizer/revision and endpoint through its documented
  environment variables. The included numbers describe a small smoke example,
  not a capacity claim or a required customer limit.
- Run `.venv-aiperf/bin/aiperf --version` and
  `.venv-aiperf/bin/aiperf config validate nim-chat.yaml`.
- Inspect `.venv-aiperf/bin/aiperf config expand nim-chat.yaml` before a sweep;
  verify run count, requested load, budget and distinct output directories.
  Validation does not prove endpoint access, model compatibility or capacity.

Keep bearer credentials in an environment/secret mechanism. The NGC pull key,
endpoint authentication key and gated-tokenizer credential are different roles;
do not substitute one for another. Never commit secrets or echo them in reports.

## Execute within the requested scope

- Start with one bounded, authorized smoke run:
  `.venv-aiperf/bin/aiperf profile --config nim-chat.yaml`.
  Confirm the selected model, successful responses and streaming before scaling
  load. Preserve the first failure and its HTTP/runtime evidence.
- Use streaming for token-arrival measurements. Check the actual endpoint's
  `max_tokens` versus `max_completion_tokens` support. Do not silently add
  `ignore_eos`, `min_tokens`, truncation or unsupported request fields.
- Change one comparison variable at a time. Concurrency is closed-loop load;
  arrival-rate tests answer a different question. Bound outstanding work and
  use the user's SLOs, capacity and budget to select the sweep.
- Measure the client as well as the server. Client CPU, networking, tokenizer
  work or exports can limit achieved load. Low GPU utilization alone is not a
  diagnosis. A remote HTTP load generator does not require a GPU allocation.
- Collect artifacts before stopping or deleting task resources. Client exit or
  disconnect does not prove remote work stopped; verify actual resource state.

## Interpret and hand off

Read [references/measurements.md](references/measurements.md). Report request
counts/errors, observed ISL/OSL, latency percentiles and units, aggregate output
tokens/s, requests/s, SLO goodput and measurement conditions. Separate startup,
warmup and steady state. Preserve raw exports and the exact redacted config.

For Dynamo's repository-specific benchmark lifecycle, use
`configure-aiperf-benchmark`, `run-aiperf-benchmark`, then
`analyze-aiperf-results` in a matching Dynamo checkout. For Kubernetes, use
`aiperf-kube-setup`, `aiperf-kube-run`, `aiperf-kube-sweep` and
`aiperf-kube-triage`; check their pinned source/version before cluster actions.

A successful smoke run is not sustained multi-user capacity, model accuracy,
or an MLPerf result. Non-LLM NIM endpoints need their own supported AIPerf
plugin and task-specific metrics; asynchronous scientific jobs are not chat
completion benchmarks.

## Primary sources

- [NVIDIA NIM benchmark overview](https://docs.nvidia.com/nim/benchmarking/llm/overview)
  and [NIM quickstart](https://docs.nvidia.com/nim/benchmarking/llm/quickstart).
- [AIPerf v0.13.0](https://github.com/ai-dynamo/aiperf/tree/v0.13.0),
  [configuration](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/tutorials/yaml-config.md)
  and [CLI reference](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/cli-options.md).
