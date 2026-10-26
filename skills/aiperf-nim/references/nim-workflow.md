# Reproducible NIM workflow

Checked 2026-10-26 against AIPerf 0.13.0 and the official NIM benchmarking
guide. Use the installed release's parser/help as the final flag/schema check.
This document does not authorize a new deployment, credential use or load test.

## Endpoint and identity

For an existing NIM LLM, record the origin, actual chat/completions route and
served model ID. `/v1/models` is a useful read-only discovery route when exposed.
NIM commonly exposes `/v1/health/ready`; a managed gateway may expose a different
readiness surface. Do not infer health from an HTTP port alone.

Use the real endpoint's API schema and a small authorized request to check:

- Exact `model` value; tokenizer repository/path, revision and chat template.
- SSE streaming and completion handling, including any proxy buffering.
- Token-limit field (`max_tokens` or `max_completion_tokens`), sampling, stop
  tokens and supported extension fields. Keep request and actual output counts.
- TLS, authentication, tenant scope, timeouts and rate-limit responses.

The sample config expects an origin without `/v1`, then explicitly sets
`/v1/chat/completions`. For a prefixed gateway, put its full route in
`endpoint.path`. Avoid an accidental doubled `/v1` or bypassing the gateway that
users actually call. A direct-backend measurement and a public-route measurement
have different scope; label both when both are requested.

## Credentials and installation

`NGC_API_KEY` authenticates image/model asset access where required. It is not
automatically the HTTP bearer credential for a self-hosted NIM. An NVIDIA hosted
API key or a deployment's gateway key may serve that role. Hugging Face access
for a gated tokenizer is separate. Obtain each from the existing approved secret
source; never print credentials in commands, logs, configs or published exports.

Use an isolated client environment; Python 3.11–3.13 is supported by the checked
AIPerf release:

```bash
uv venv --python 3.12 .venv-aiperf
uv pip install --python .venv-aiperf/bin/python 'aiperf==0.13.0'
.venv-aiperf/bin/aiperf --version
```

Alternatively use an image containing the required AIPerf version, pinned by
digest. Record the actual version inside the image; a Triton SDK image tag does
not by itself prove it contains that version. The client can run on CPU against
a remote NIM. GPU telemetry requires separate access, not permission to allocate
an inference GPU for the client. Do not automatically copy privileged/unconfined
container options from historical benchmark examples.

## Small smoke configuration

Copy the bundled `assets/nim-chat.yaml`. Choose the served model and matching
tokenizer rather than running these placeholder values unchanged:

```bash
export NIM_URL='http://localhost:8000'
export NIM_MODEL='YOUR-SERVED-MODEL-ID'
export NIM_TOKENIZER='YOUR-MATCHING-TOKENIZER-REPOSITORY-OR-PATH'
export NIM_TOKENIZER_REVISION='YOUR-PINNED-REVISION'
export AIPERF_ARTIFACT_DIR='./artifacts/nim-smoke-001'
# Set NIM_API_KEY through your secret mechanism; no literal secret in this file.
.venv-aiperf/bin/aiperf config validate nim-chat.yaml
.venv-aiperf/bin/aiperf config expand nim-chat.yaml
```

Only after the endpoint/load scope is authorized:

```bash
.venv-aiperf/bin/aiperf profile --config nim-chat.yaml
```

Warmup is excluded from measurement. Request/duration phase stop conditions and
per-request timeout have different purposes: a phase duration is not a guarantee
that all outstanding requests and teardown finish by that instant. Choose the
drain/grace policy from actual help and include it in the total budget.

The smoke template requests 512 input/128 output tokens at concurrency one. EOS
may shorten outputs. `apply_chat_template: true` makes local accounting include
the matching HF chat template when available; confirm the template matches NIM
and compare server usage where available. Do not treat requested OSL as observed
OSL or silently enable remote tokenizer code.

## Workloads, sweeps and goodput

Use a representative trace/custom dataset for application claims. Synthetic
prompts isolate shape effects but do not establish real task accuracy or natural
prefix-cache behavior. Preserve dataset hashes, seed, selection and prompt
format. Record any filtering; never silently discard long or failing requests.

For a small concurrency sweep, copy the smoke file, choose sufficient request
counts/runtime for the user's goal, and append a reviewed grid, for example:

```yaml
sweep:
  type: grid
  parameters:
    phases.profiling.concurrency: [1, 2, 4]
```

These values are illustrative. Preview with `aiperf config expand`; verify the
variation count, output paths and aggregate spend before running. Keep cache
state and warmup comparable. Repeated prompts can inflate prefix-cache benefits;
do not flush shared caches to manufacture a cold test.

Concurrency phases immediately replace completed requests. To model independent
arrivals, replace the profiling phase with a bounded arrival-rate phase such as:

```yaml
- name: profiling
  type: poisson
  rate: 2.0
  concurrency: 8
  duration: 120
  gracePeriod: 30
```

This represents a target rate with a concurrency ceiling; report offered and
achieved rates and queue/backpressure effects. Select values from the real
workload and approved budget, not this example.

To measure SLO goodput, add `benchmark.slos` with the user's thresholds. For
example, `time_to_first_token: 500` and `inter_token_latency: 50` are **ms** in
the checked version. Inspect metric definitions/units before supplying other
constraints. Report both good requests/s and attainment/error fraction; high
goodput does not establish that the requested fraction of all requests met SLO.

## Kubernetes and Dynamo

Use the installed official `aiperf-kube-*` skills for lifecycle details. Check
the selected context, namespace, existing operator/CRDs and exact AIPerf image
first. Installing a skill is not permission to install an operator, change RBAC,
delete resources or cancel work. The upstream examples use mutable tags; select
the intended immutable image for a real reproducibility claim.

Keep credentials in supported Secret references, not printed manifests. Record
the actual controller/worker pod count, client resources, target replicas and
network path. A load-generator Job's CPU saturation can distort server results.
Do not colocate it with the server without recording contention.

For Dynamo, use a matching source checkout: the unchanged skills reference its
workload/deployment/recipe files as well as the packaged rules. Freeze the actual
Dynamo backend/disaggregation/profile and worker readiness in the run receipt.
Do not apply Dynamo-only settings to an ordinary monolithic NIM endpoint.

## Failures and other NIM APIs

For 401/403, preserve the exact HTTP response and distinguish endpoint auth from
registry/tokenizer access. For 404 or schema errors, check route/model/field
compatibility before retrying. For 429/503, report admission/load limits. For
timeouts, preserve partial artifacts and establish whether remote work persists.
Do not silently retry all failed requests into a clean-looking result.

Use `.venv-aiperf/bin/aiperf plugins --help` and endpoint-specific upstream docs
before benchmarking embeddings, reranking, vision or audio. Plugin names,
payloads and meaningful metrics differ. Do not report LLM output-token TPS for
non-generative tasks or send a long-running scientific workflow to a chat plugin.

Sources: [NIM quickstart](https://docs.nvidia.com/nim/benchmarking/llm/quickstart),
[NIM parameters](https://docs.nvidia.com/nim/benchmarking/llm/parameters),
[AIPerf configuration](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/tutorials/yaml-config.md),
[load control](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/tutorials/request-rate-concurrency.md),
[goodput](https://github.com/ai-dynamo/aiperf/blob/v0.13.0/docs/tutorials/goodput.md).
