# Native workloads, templates and policies

Find versioned guides through [the source map](sources.md): workspaces, standard
training, distributed training, standard/distributed inference, supported external
workload types, workload assets and templates. Choose the intended lifecycle:
interactive session, finite job, serving endpoint or a distributed gang.

## Author and qualify a native workload

1. Select the existing project, cluster and allowed node pools. Read effective
   quotas and policies, not only the template's defaults.
2. Pin a supported image/platform. Inspect its ENTRYPOINT, CMD, user, executable,
   dependencies and image pull policy. A Kubernetes/Run:ai `command` overrides an
   image entrypoint; `args` are not a shell unless a shell is explicitly invoked.
3. Declare CPU/RAM, GPU count or supported sharing unit, storage, UID/GID,
   tolerations, placement and finite duration. Keep ordinary parameters arbitrary;
   integrity hashes are not a workload eligibility or tuning allowlist.
4. Submit through the native CLI/API and capture accepted workload identity,
   effective spec and resulting Kubernetes owners. Bound startup separately from
   execution and output retrieval. Validate output, status, usage and cleanup.

For **3.0.20** the checked REST paths include
`POST /api/v1/workloads/trainings`, `POST /api/v1/workloads/inferences`, and
`POST /api/v1/workload-templates/trainings` or `/inferences`. Verify the installed
OpenAPI schema for complete request bodies and template-binding field names;
do not invent a generic job envelope or reuse a template UUID from another scope.
Use the source `control-plane/workloads/swagger/source/` to resolve exact fields.

## Templates and admission policies

Templates are reusable authoring defaults; policies constrain or default actual
workloads at the assigned scope. Read parent/project policy inheritance and
locked fields. A template matching a policy on paper is insufficient: submit and
read back a representative workload, including a deliberate forbidden change.
Keep the installed/UI default aligned with qualification; a passing one-off
override does not repair a broken catalog template.

For policy JSON/YAML, use the matching policy reference and native assets. Do not
silently unlock fields or broaden authorized users when an inference request is
rejected. An allowed-image rule must include the immutable image actually used;
a tag-to-digest conversion can change what admission compares. Record the native
error and inspect the rule before changing it.

## Projects and namespaces

Project identity, tenant identity, project name and Kubernetes namespace need not
match. Determine whether the platform creates a namespace or adopts an external
one. In the checked 3.0.20 project schema, `requestedNamespace` selects external
namespace integration; omitting it permits native namespace ownership. Inspect
the installed contract before relying on this behavior. Wait for an Active native
namespace, then provision project-scoped PVCs and runtime credentials there.
Do not manually create a namespace merely to conceal failed reconciliation.

## MPI/distributed jobs

Use native distributed-training/MPI support or a supported training operator.
Declare launcher/worker roles, replicas, per-replica resources, gang size, quota,
placement and rendezvous according to that release's examples. Confirm actual
GPU allocation on every rank and the executable's MPI/CUDA support. TCP, Ethernet,
RDMA and NVLink are different paths; a completed multi-node job does not prove
RDMA or a scaling benefit. Validate host communication, UCX/OpenMPI integration,
network policy, shared storage and finite scientific outputs before throughput.

Preserve actual user options and protocol. Separate faster execution defaults
from scientific parameter changes, retries and result validation. Reuse the
existing engine and native controller; a custom MPI coordinator is not the first
response to missing capacity or a misconfigured launcher.
