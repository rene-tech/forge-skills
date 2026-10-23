# Standard inference, Knative and NVIDIA NIM

Sources: [Run:ai standard/custom inference](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/workloads-in-nvidia-run-ai/using-inference/custom-inference),
[native NIM guide](https://docs.nvidia.com/run-ai/self-hosted/documentation/workloads-in-nvidia-run-ai/using-inference/nim-inference),
[Knative probing](https://knative.dev/docs/serving/services/configure-probing/),
[request flow](https://knative.dev/docs/serving/request-flow/) and
[concurrency](https://knative.dev/docs/serving/autoscaling/concurrency/).

## Choose a documented serving path

Native standard inference can run an unchanged vendor NIM as a custom server,
using its real entrypoint, environment, port and API. A dedicated NIM UI/API
integration or NIM Operator has different prerequisites, schemas and lifecycle.
Do not substitute one for the other silently. In the checked 3.0.20 source,
`/api/v2/workloads/nim-services` is an operator-specific path; standard inference
uses `/api/v1/workloads/inferences`. Recheck installed feature availability.

Inspect the exact NIM model/version's official support matrix, launch/config,
inference and Helm documentation. Do not apply LLM assumptions to scientific NIMs.
Verify entitlement, runtime NGC API access, registry pull access, model cache,
CPU/RAM/VRAM, shared memory, driver/CUDA and artifact/output paths. A regional
unchanged image mirror does not remove first-start model-download requirements.

Use native secret references in the authorized namespace and supported credential
discovery configuration, without exposing values. Image pull and runtime API
credentials are separate. Keep endpoint OAuth authorization enabled for approved
clients and verify the exact OAuth client ID. `clusterLocalAccessOnly` controls
exposure; it does not replace authorization.

## Readiness, initialization and concurrency

Read the installed API, generated Revision and Pod. The **3.0.20** native `Probes`
schema exposes readiness only, even though generic probe descriptions mention
liveness. Do not inject unsupported startup/liveness fields; this is not a claim
about all later versions or direct Knative authoring.

The documented native initialization timeout and request timeout are distinct.
The checked v3.0 UI guide documents requests from5s to10min. Preserve a suitable
long initialization allowance for node/image/model startup, then choose a normal
readiness failure threshold for runtime traffic removal. A very high readiness
failure threshold also hides prolonged failures after startup. It does not restart
a hung application. Use a supported startup/liveness mechanism only when exposed
by the actual deployment contract; avoid restart loops during model download.

Knative rewrites user readiness through queue-proxy. Check Service, Configuration,
Revision, PodAutoscaler, ServerlessService, Route and networking Ingress conditions,
not only Pod Ready. A min=max1 workload does not intentionally scale to zero,
although VM failure, preemption or eviction can still remove its only replica.
Align native `concurrencyHardLimit` with actual engine capacity; an autoscaling
target is a soft target, not the hard request limit.

Verify **effective Pod placement**, not a `nodePools` field echoed by an API.
The [3.0.20 inference composer](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/workloads-and-policies/composer/composer_v2/inference_workloads/compose_helpers.go#L281)
explicitly skips `nodePools` and `priorityClass` in its placement conversion,
while it does compose native required node affinity. Policies and CLI translation
can also affect the result. Inspect supported CLI/schema translation and actual
Revision/Pod affinity before claiming a GPU-pool restriction. This release-local
finding is not a universal limitation or permission to patch the generated Pod.

For example, [Boltz2 NIM1.10 configuration](https://docs.nvidia.com/nim/bionemo/boltz2/1.10.0/configure.html)
documents one request per GPU and one HTTP worker. Its optional bounded admission
requires `NIM_ENABLE_QUEUE_METRICS`; setting a concurrency variable alone is not
proof of bounded queuing. Prefer one already-supported control layer and measured
limits rather than adding another proxy/queue. Do not turn this model-specific
example into a universal NIM setting.

## Diagnose and qualify

| Observation | Distinction to resolve |
| --- | --- |
| TLS/OAuth fails | Certificate chain, host routing, token and endpoint grant before model code |
| TCP dial timeout to PodIP:8012 | Knative queue-proxy/backend connectivity; correlate Pod lifetime and network before blaming model latency |
| Queue-proxy reachable, local application port fails | Application listener/readiness, CPU/memory/GPU pressure, restart and logs |
| Application503/Retry-After | Vendor admission/capacity, distinct from a connection-stage502 |
| Successful readiness, failed prediction | Health contract versus actual model/input/runtime behavior |

Keep the failed workload long enough to capture exact Pod UID/IP, revision,
endpoint addresses, restart/termination reasons, queue-proxy/activator/ingress
logs and node/cloud events. Compare local app port with backend reachability from
the actual forwarding source. Do not install a diagnostic service unnecessarily.

Qualify cold startup, real authenticated predictions and variants, artifact access,
idle intervals longer than the failure window, warm/cache reuse and resource
stability. External health requests may legitimately queue behind a prediction
when a hard concurrency limit is1; distinguish queuing from failing internal
readiness. Preserve HTTP status/body/latency and exact runtime identity. Health200
or one prediction is not sustained availability or arbitrary-input qualification.
