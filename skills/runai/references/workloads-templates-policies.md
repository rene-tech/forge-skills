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

In the [3.0.20 Project guide](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/platform-management/aiinitiatives/organization/projects.md#deleting-a-project),
Project deletion retains its namespace while attempting workload/asset deletion;
namespace retention alone is not a leak or a successful complete teardown.
The [pinned Project GC guard](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/cluster/agent/pkg/validator/project_garbage_collector.go)
accepts only the authentic `system:serviceaccount:kube-system:generic-garbage-collector`
username plus the current ServiceAccount UID, on a deleting Project UPDATE that
removes only `orphan` and preserves other fields apart from managedFields.
Managed control planes can use different controller identities: obtain actual
admission/audit `userInfo` before attributing a stuck finalizer. Source conditions
or an absent SA alone do not identify the live caller. Do not strip finalizers,
activate a controller SA's ambient privileges or broaden admission trust without
explicit authorization. These are privileged recovery exceptions, not ordinary
Project deletion or proof that reproducible lifecycle works.

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

### Retry ownership in the checked 3.0.20 path

An omitted native distributed `backoffLimit` becomes `numWorkers × 6`, not zero;
an explicit value is preserved. See the
[native composer](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/workloads-and-policies/composer/composer_v2/distributed_to_kubeflow/distributed_to_kf.go)
(`composeBackoffLimit`). MPI Operator v0.6.0 copies that run policy to the
**launcher Kubernetes Job**; it is not a promise of worker, workload or checkpoint
recovery.

Inspect outer `spec.mpiReplicaSpecs.Worker.restartPolicy`, its inner
`template.spec.restartPolicy`, the launcher Job and actual worker Pods separately.
The native composer writes the supplied restart policy to the inner Pod template;
the [checked MPI API defaults](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/runai-cluster/cluster/workload-controller/pkg/api/mpijob/v2beta1/constants.go)
are Worker `Never` and Launcher `OnFailure` when outer policies are omitted.
[MPI Operator v0.6.0](https://github.com/kubeflow/mpi-operator/blob/v0.6.0/pkg/controller/mpi_job_controller.go)
overrides the Pod policy from the outer replica policy (`ExitCode` maps to Pod
`Never`; other values copy through). An inner `OnFailure` therefore does not
establish effective worker restart behavior. Record owner UIDs and checkpoint
progress to distinguish launcher backoff, worker recreation, Run:ai workload
recreation and genuine application resume. Recheck these mappings on upgrades.

MPI and Project lifecycle source facts refreshed **2026-10-24**; these findings
are version-scoped and contain no deployment qualification claim.
