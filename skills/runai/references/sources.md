# Authoritative source map

Checked 2026-10-23. Select the deployed edition/version before following commands.

| Surface | Verified primary entry point | Boundary |
| --- | --- | --- |
| Self-hosted | [NVIDIA v3.0 documentation](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/home) | OSS and support-entitled releases; check the chosen release's support matrix. |
| SaaS | [Hosted documentation](https://run-ai-docs.nvidia.com/saas) | Provider-managed control plane; do not apply self-hosted control-plane charts to it. |
| Full OSS platform | [Run:ai source](https://github.com/dsx-ai-factory/run-ai) | UI, CLI, API, identity, charts and worker orchestration; inspect a matching tag/commit. |
| Scheduler only | [KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler) | Scheduler, queues and PodGroups; not the full platform/API/auth service. |
| Serving substrate | [Knative Serving](https://knative.dev/docs/serving/) | Revision lifecycle, routing, probes, concurrency, autoscaling and volumes. |
| GPU infrastructure | [GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) | Drivers, runtime integration, device discovery, MIG and DCGM; select the installed release. |
| Cloud package | [Nebius Applications](https://docs.nebius.com/applications) | Discover exact package version, inputs, update path and managed boundaries. |
| Nebius OSS availability | [Official October 13 launch](https://nebius.com/blog/posts/nvidia-run-ai-open-source-nebius-applications) | Confirms availability; does not specify the actual package version or multi-cluster controls. |

Rendered NVIDIA docs advertise `/llms.txt`, page `.md`, and page-level `/llms.txt`.
Use them when accessible. A 403/404 is a retrieval limit, not proof a feature is
absent; use site navigation or matching public source. SaaS and self-hosted need
not have release/feature parity. A license for a model or support service is
separate from the full platform's OSS license.

## Find every technical area without copying manuals

The following paths were checked in the public **3.0.20** snapshot
`74280199d8665d14e12c88f4cd13dd6a408300ca`.
Use [the exact source tree](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca)
as a stable navigation fallback, not as a recommendation to deploy that release.

Versioned primary manual sections (3.0.20 source snapshot):

| Task | Direct section |
| --- | --- |
| Architecture/support/install/configure | [Installation and configuration manual](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/installation-and-configuration) |
| Connected, air-gapped, same-/multi-cluster | [Guided installation](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/installation-and-configuration/installation/guided-installation) |
| HA, node maintenance, restore and observability | [Operations](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/installation-and-configuration/operations) |
| Backup, upgrades and migrations | [Upgrade manual](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/installation-and-configuration/upgrade) |
| Users, service accounts, roles and access rules | [Authentication and authorization](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/platform-management/authentication) |
| Projects, departments, node pools and MIG profiles | [Manage AI initiatives](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/platform-management/aiinitiatives) |
| Scheduling, fairness, over-quota and fractions | [Scheduler and resource optimization](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/platform-management/runai-scheduler) |
| Admission constraints and field definitions | [Policies](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/platform-management/policies) |
| Metrics, profiling and reports | [Performance monitoring](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/platform-management/monitor-performance) |
| Workspaces, training, distributed jobs, inference, assets and templates | [Workload manual](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/workloads-in-nvidia-run-ai) |
| REST methods, models and required fields | [Assembled OpenAPI specifications](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/infra/openapi/specs) |
| CLI syntax and operational examples | [Versioned CLI reference](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/reference/cli), [practical cookbook](command-cookbook.md) |
| Agent skills, MCP deployment, connection and tools | [Agents manual](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/agents), [task guide](agents-mcp-applications.md) |
| Helm-based multi-resource AI workloads | [AI Applications manual](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/ai-applications), [task guide](agents-mcp-applications.md) |

These source sections are versioned and checked; they are not claims that every
rendered web-page slug or every API field is unchanged in the latest release.

| Need | Repository navigation/search terms |
| --- | --- |
| Architecture, deployment and compatibility | `docs/installation-and-configuration/system-requirements/`, `support-matrix.md`: deployment model, infrastructure, networking, third-party services |
| Recommended installation | `docs/installation-and-configuration/installation/guided-installation/`: connected/air-gapped, same-/multi-cluster, configuration/command references |
| Helm installation | `.../installation/install-using-helm/`: preparations, prerequisites/features, control plane, cluster and uninstall |
| HA and maintenance | `.../operations/`: high availability, scaling, VPA, node maintenance, cluster restore, observability |
| Upgrade | `.../upgrade/`: planning, backup, upgrade, fractions and legacy-workload migrations |
| Authentication/authorization | `docs/platform-management/authentication/`: users, service accounts, roles, permissions and access rules |
| Projects, departments, node pools and MIG | `docs/platform-management/aiinitiatives/`: organization and resources |
| Quota, fairness, preemption and GPU sharing | `docs/platform-management/runai-scheduler/`: scheduling, over-quota, resource optimization and quick starts |
| Policies | `docs/platform-management/policies/`: native workload policies and policy YAML reference |
| Workload authoring | `docs/workloads-in-nvidia-run-ai/`: training, distributed training, workspaces, inference, templates and workload assets |
| Logs, metrics and reports | `docs/installation-and-configuration/operations/observability/`, `docs/platform-management/monitor-performance/` |
| API schemas | `control-plane/infra/openapi/specs/`; each service's `swagger/source/`; installed public API reference |
| Permissions and scope enforcement | `x-authorize` annotations plus handlers; `control-plane/authorization/pkg/database/dao/static-permission-sets/` and `static-roles/` |
| Kubernetes conversion and native fields | `runai-cluster/cluster/sdk/apis/workload_fields/`, `workload-common/builders/`; matching service handler |
| Helm/CRDs/hooks/operands | `runai-cluster/cluster/runai-chart/` and published release chart metadata |

Start with `rg --files`, then search the operation ID, field or observed error.
Generated clients can obscure authoritative schemas: trace validation, handler,
conversion and resulting Kubernetes objects. Keep a source receipt with version,
retrieval date and any difference from the installed contract.

Useful verified pages: [CLI setup](https://docs.nvidia.com/run-ai/self-hosted/v3.0/reference/cli/install-and-configure-cli),
[API authentication](https://docs.nvidia.com/run-ai/self-hosted/v3.0/reference/rest-api/getting-started/how-to-authenticate-to-the-api),
[roles](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/platform-management/authentication/roles),
[upgrade planning](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/installation-and-configuration/upgrade/plan-the-upgrade),
[custom inference](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/workloads-in-nvidia-run-ai/using-inference/custom-inference).
