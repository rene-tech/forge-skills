# Extension boundaries and composition

Use extensions only when the intended workload needs them. An available operator
is not a reason to install another control plane or wrap a vendor runtime.

## KAI Scheduler and resource management

[KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler) is independently
usable. Its docs/examples cover hierarchical queues, fairness, gang scheduling,
preemption, placement and GPU sharing. The full platform integrates scheduling
with projects, policies, workload authoring, identity and monitoring. Do not
install a second scheduler/queue authority over an existing managed Run:ai setup.
Inspect the integrated KAI version and the actual workload-to-PodGroup mapping.

New modular platform releases can expose resource-management and GPU-fractioning
operators separately. Discover their release-specific ownership and contracts
from the [full platform source](https://github.com/dsx-ai-factory/run-ai) and
published component map; do not assume standalone and integrated configurations
are interchangeable or separately needed.

## GPU Operator, DRA and network stack

[GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)
owns supported GPU software provisioning, not application correctness. Identify
whether cloud node images already supply drivers/toolkit and whether Operator,
device plugin, CDI/NRI or DRA manages allocation. One owner must configure each.
Follow exact fraction/MIG/driver compatibility; two successful operator Pods do
not establish enforced isolation or kernel support.

For MPI, RDMA, GPUDirect or multi-node NVLink, use supported networking/operator
and DRA integration for the actual hardware. Verify end-to-end transport and
rank behavior. Do not infer RDMA from a GPU type, installed package or fast TCP.

## Training, pipelines and NIM

Supported training operators, Ray, Argo and external workload integrations can
participate through native grouping/admission. Confirm the documented integration
and selected scheduler; keep that operator as workload owner rather than writing
a duplicate launcher. Match retry, cleanup and gang semantics across layers.

NIM Operator and standard Run:ai inference are separate deployment paths. Install
the Operator only for an authorized use case that needs its CRDs/lifecycle.
An unchanged NIM container can use standard inference without a custom wrapper
when the documented image/API/prerequisites fit. See [inference](inference-nim.md).

## Dynamo/Grove pool binding

For a `DynamoGraphDeployment` v1beta1 graph that must stay in one native pool,
set required node affinity in every component's `podTemplate.spec`, including
the frontend, using that pool's configured node-label key/value. The
[Run:ai3.0.20 DGD parser](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/cluster/external-workload-integrator/pkg/handlers/dynamo_graph_deployment_handler.go#L192)
reads component affinity for native requested pools; a node selector or
`nvidia.com/kai-scheduler-queue` annotation alone does not bind that list. The
[pool converter](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/common/node-pool-utils/converter/converter.go#L27)
maps required affinity `In` expressions to native pools before falling back to
object labels and project defaults.

The [shared parser](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/cluster/external-workload-integrator/pkg/handlers/commonparsers/common_handler.go#L38)
keeps an already populated `ExternalWorkload.spec.requestedNodePools`; the first
component can establish it. Correct a missing binding through a fresh graph UID
and normal owner lifecycle. Before qualification HTTP, match the external
workload's `spec.originalWorkloadUID` to that graph and require its requested
list to contain only the intended pool. Recheck after readiness alongside the
actual PodGroup queue and physical Pod placement. An initially correct queue
alone is insufficient; verify this release-specific behavior before generalizing.

## Optional process-snapshot acceleration

Private process-snapshot add-ons are independent of stock Run:ai/KAI/NIM and
are not required for a clean foundation. Discover the selected add-on's owner
and approved documentation privately when relevant; this public skill contains
no private product, repository, endpoint, profile, credential or integration code.

A process snapshot's validity depends on exact runtime/model state, GPU/driver
compatibility, storage and restore semantics. Keep normal vendor loading as a
supported fallback and scheduling/auth/durability with their existing owners.
Measure actual restored startup and results before advertising acceleration.
Do not substitute snapshots for application checkpoints or call an image cache
hit a successful process restore. No private extension is installed or configured
merely by invoking this skill.
