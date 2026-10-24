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

## Native cache prewarming and local models

Use the [versioned NIM Operator cache workflow](https://docs.nvidia.com/nim-operator/3.1.2/cache-non-llm.html#cache-nims-that-use-model-profiles)
appropriate to that model. Profile-based NIMs can use explicit
`source.ngc.model.profiles` and an existing owner PVC; avoid downloading all
profiles unintentionally. CPU-only prewarming is appropriate when the exact
model's download path supports it, not a universal NIM guarantee. Keep native
cache ownership separate from Run:ai inference serving; another serving
controller or custom preparation wrapper is not inherently required.

Check Ready, completion condition, PVC and immutable source against retained
successful execution evidence; for profile-based caches, also verify selected
`status.profiles[].name`. Native-download NIMs can have no profile list. In
[Operator 3.1.2's controller](https://github.com/NVIDIA/k8s-nim-operator/blob/v3.1.2/internal/controller/nimcache_controller.go#L737),
cache Jobs have a 600s TTL and a Ready cache does not recreate an expired Job.
Capture Job/Pod ownership, command, imageID and identity before expiry when
needed; distinguish a retained successful Pod from a complete Job owner chain.
A filename listing does not prove weight integrity or scientific validity.
This release's [validation rejects changed cache specs](https://github.com/NVIDIA/k8s-nim-operator/blob/v3.1.2/internal/webhook/apps/v1alpha1/nimcache_webhook_validation_helper.go#L227),
including a registry URL change that preserves the image digest. Do not force a
refresh or assume an in-place mirror update is supported.

Local-model settings are model/version-specific. For example, the versioned
[Boltz2 NIM 1.10 configuration](https://docs.nvidia.com/nim/bionemo/boltz2/1.10.0/configure.html)
supports `MODEL_PATH` together with
`NIM_DISABLE_MODEL_DOWNLOAD=1`; these are not universal NIM variables. Verify
that the complete pinned assets exist, all later loaders use that directory,
and skipping download does not leave a required workspace unprepared. Preserve
the approved serving entrypoint and validate exact metadata and predictions;
an image tag alone does not establish the reported application version.

## Read-only root and customer-data boundaries

An EROFS startup failure identifies an attempted write path, not GPU
incompatibility. Inventory the exact image's workspace, model/runtime caches,
temporary files, home/XDG state and optional output exports. Prefer documented
local-model/path configuration or supported native mounts over image patches.
Use the installed Run:ai schema for read-only root, UID/GID, PVC mounts and home
creation; inspect the admitted Pod and every container's actual mounts.

Read-only root applies per container and does not make mounted volumes
read-only. Review queue/OAuth sidecars and init containers independently, plus
`emptyDir`, shared memory and host/node storage. Owner-private PVCs deliberately
allow same-owner sharing; they do not establish per-request isolation or crash
erasure. A cache may also receive results through an application's fallback.
Use [storage qualification](storage-durability.md) for ownership and retention.

A supported high log threshold can suppress input-bearing records at lower
levels, but is not payload redaction: direct prints, exception responses and
native libraries can bypass the application logger. Check validation/error
paths, stdout/stderr, access logs, traces and node log retention. Telemetry-off
is a separate control. Successful inference with private scratch does not prove
complete data confinement, snapshot safety or regulated-data suitability.

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

In [3.0.20's autoscaling validator](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/workloads-and-policies/composer/fields_composer.go#L701),
`minReplicas > 0` requires omitting `scaleToZeroRetentionSeconds` entirely;
even an explicit zero is rejected. Validate these cross-field rules as well as
the published request schema when adapting a scale-to-zero fixture.

Verify **effective Pod placement**, not a `nodePools` field echoed by an API.
The [3.0.20 inference composer](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/workloads-and-policies/composer/composer_v2/inference_workloads/compose_helpers.go#L281)
explicitly skips `nodePools` and `priorityClass` in its placement conversion,
while it does compose native required node affinity. Policies and CLI translation
can also affect the result. Inspect supported CLI/schema translation and actual
Revision/Pod affinity before claiming a GPU-pool restriction. This release-local
finding is not a universal limitation or permission to patch the generated Pod.

An unscheduled Pending Pod may not yet have its assignment pool label: the
[KAI binding path](https://github.com/kai-scheduler/KAI-Scheduler/blob/330e0235c963841a53e079f88ce11b65b88a64f3/pkg/scheduler/cache/cache.go#L342)
patches it after creating a BindRequest. Check required affinity before binding
and actual node placement afterward; a missing assignment label alone does not
prove a placement violation. A present conflicting label still needs investigation.

For example, [Boltz2 NIM1.10 configuration](https://docs.nvidia.com/nim/bionemo/boltz2/1.10.0/configure.html)
documents one request per GPU and one HTTP worker. Its optional bounded admission
requires `NIM_ENABLE_QUEUE_METRICS`; setting a concurrency variable alone is not
proof of bounded queuing. Prefer one already-supported control layer and measured
limits rather than adding another proxy/queue. Do not turn this model-specific
example into a universal NIM setting.

## Independent replicas and maintenance

Replica count and scheduler gang size are different controls. In checked
**Run:ai3.0.20 / KAI0.18.3**, the default Knative plugin makes one Revision-owned
PodGroup whose `minMember` comes from `min-scale`. Thus minimum2 replicas form a
two-member gang. Losing one member can make KAI evict the survivor as a stale
gang, including a non-preemptible group. Two replicas alone do not prove
maintenance failover.

The [published RunaiConfig field](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/cluster/sdk/apis/run/v1/pod-grouper/types.go#L56)
defaults to true. Through the existing Run:ai Helm owner, the native option is:

```yaml
clusterConfig:
  pod-grouper:
    args:
      gangScheduleKnative: false
```

[Run:ai converts it into KAI Config](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/cluster/go-operator/internal/run/operands/kai-operator/resources/pod_grouper.go#L19),
which emits `--knative-gang-schedule=false`. The
[KAI Knative plugin](https://github.com/kai-scheduler/KAI-Scheduler/blob/330e0235c963841a53e079f88ce11b65b88a64f3/pkg/podgrouper/podgrouper/plugins/knative/knative.go#L72)
then creates a Pod-owned group with minimum1 for each Pod while native
`autoscaling.minReplicas` can remain2. This changes regional Knative grouping,
not MPI or batch grouping. Do not use the batch-only `kai.scheduler/batch-min-member`
annotation as a Knative override or assume existing groups migrate automatically.
Inspect fresh groups and preserve the workload's required placement and quotas.

This per-Pod path selects PriorityClass `inference` (125). KAI's
[preemptibility fallback](https://github.com/kai-scheduler/KAI-Scheduler/blob/330e0235c963841a53e079f88ce11b65b88a64f3/pkg/common/podgroup/preemptible.go#L14)
uses non-preemptible when the explicit enum is omitted and priority is at least100.
Inspect the actual PodGroup and PriorityClass: the Kubernetes Pod's own
`spec.priority` can be0 and is not proof of KAI's scheduling priority. Review
effects on any custom Knative priority settings and Revision-wide allocation.

Use the provider's documented serialized-maintenance procedure. Non-preemptible
autoscaler annotations are not a workload PodDisruptionBudget (PDB). A PDB limits
voluntary Eviction only when the actor honors it; KAI's stale eviction uses Pod
DELETE. Check actual matching workload PDBs rather than substituting controller
PDBs, and retain normal grace periods without force or eviction bypasses.

Before a controlled disruption, verify both initial replicas. During the selected
target's eviction or loss, pin the known survivor's Pod/node identity, image,
restarts, readiness and real predictions. The target may become NotReady, reboot
or be replaced; qualify every recovered Ready replica's actual placement, GPU,
driver and ownership independently. Preserve interrupted attempts and bound any
separately authorized case without resetting its deadline.

[Nebius managed maintenance](https://docs.nebius.com/kubernetes/maintenance/index)
cordons, waits/drains, stops/starts the VM, then uncordons and clears its condition.
Leave provider-owned maintenance cordons to that controller. For a conflicting
maintenance window, consider an already prepared authorized region after checking
capacity, models, cache, data residency and endpoint grants; this is an operator
procedure, not an automatic regional-failover claim.

The official rolling-update guide budgets both old and new minimum gangs at
once: two old plus two new replicas require four GPUs/quota in that documented
mode. Independent grouping does not establish a different zero-downtime rollout
guarantee. Cloud node minimum0 also does not override an active inference
minimum2. Qualify the chosen availability/cost tradeoff with actual survivor
requests during a bounded disruption and verify owned cleanup afterward.

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
