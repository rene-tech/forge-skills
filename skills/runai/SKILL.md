---
name: runai
description: "Plan, install, operate, integrate, and troubleshoot NVIDIA Run:ai platforms and native workloads, including scheduling, GPU sharing, multi-cluster fleets, inference, and APIs. Distinguish the full platform from standalone KAI Scheduler."
---

# Run:ai Expert

Use native Run:ai, Kubernetes, Helm and vendor interfaces. Prefer supported
components and existing immutable images over a new scheduler, proxy, controller
or runtime wrapper. Documentation establishes a contract; readbacks and
representative results establish that an installation works.

## Establish identity and ownership

1. Identify SaaS versus self-hosted, OSS versus support-entitled, control-plane,
   worker and CLI versions, Kubernetes distribution, cloud and regions.
2. Read the relevant versioned docs and installed schema before choosing fields.
   Never turn one release's limitation into a universal rule.
3. Inspect existing releases, projects, identities, workloads, storage and
   monitoring within the authorized environment. Never dump Secrets or tokens.
4. Preserve user workloads and existing configuration owners. Make changes through
   their IaC/GitOps path; do not hand-patch managed objects as a shortcut.
5. Follow existing user authorization. Prepare a concrete diff and validation
   before any required approval; this skill creates no new approval workflow.

## Task routing

Read only the relevant references; do not load the whole manual.

| Task | Reference |
| --- | --- |
| Locate docs, versions, schemas, releases and source | [Source map](references/sources.md) |
| Helm, HA, air gap, backups and upgrades | [Install and upgrade](references/install-upgrade.md) |
| CLI, REST, tokens, RBAC and deletion semantics | [Interfaces and identity](references/cli-api-auth.md) |
| Source-verified CLI commands and REST request bodies | [Command cookbook](references/command-cookbook.md) |
| Native Agents, MCP server/tools and AI Applications | [Agents and applications](references/agents-mcp-applications.md) |
| Training, workspaces, MPI, templates and policies | [Native workloads](references/workloads-templates-policies.md) |
| Quotas, fairness, gang, pools, MIG and fractions | [Scheduling and GPUs](references/scheduling-gpus.md) |
| PVCs, checkpoints, artifacts and recovery | [Storage and durability](references/storage-durability.md) |
| Standard inference, Knative and NIM | [Inference](references/inference-nim.md) |
| Regional fleets, Nebius Applications and Spot | [Multi-cluster](references/multicluster-nebius.md) |
| Metrics, security, incidents and acceptance | [Operations](references/operations-security.md) |
| KAI, GPU Operator and independent add-ons | [Extensions](references/extensions.md) |

## Operational invariants

- Pin charts and image digests; retain effective values, source provenance and
  rollback information in appropriately protected storage.
- Separate API permissions, endpoint authorization, Kubernetes RBAC, cloud IAM,
  registry credentials and model entitlements. Login proves none of the others.
- Verify project namespace ownership and actual namespace readiness before scoped
  storage or credential deployment. External namespaces are prerequisites.
- Distinguish unavailable capacity, quota denial, image-pull failure, CUDA/build
  incompatibility, application error and network failure.
- Record exact GPU SKU, compute capability, driver/runtime, executable and mode.
  Qualify compatible alternatives; do not infer support from a family name.
- Completed Pods cannot normally support `exec`/`cp`. Retrieve durable output via
  a bounded native CPU inspector or supported storage download.
- Separate DELETE acceptance, physical teardown and retained history. GET 200 with
  a deletion timestamp can be normal; never remove finalizers to hide history.
- Keep credentials, private addresses/identifiers, customer data and private
  add-on implementation out of reusable/public artifacts.

## Completion evidence

Lead with outcome, exact scope/version, validation, limitations and owned cleanup.
For serving, check authorized external requests after idle periods. For batch,
validate actual artifacts. Admission, Pod Ready, exit zero or unit tests alone do
not establish scientific validity, durable recovery or production readiness.

Sources checked **2026-10-23**. Recheck version-sensitive facts when used.
