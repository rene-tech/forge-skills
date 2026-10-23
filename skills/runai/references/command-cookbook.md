# Versioned command cookbook

Checked 2026-10-23 against public **Run:ai3.0.20**, commit
`74280199d8665d14e12c88f4cd13dd6a408300ca`: generated CLIv2 docs under
[`docs/reference/cli/runai`](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/docs/reference/cli/runai)
and [assembled OpenAPI](https://github.com/dsx-ai-factory/run-ai/tree/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/infra/openapi/specs).
These are recipes, not executed acceptance tests. Check installed help/schema and
existing authorization before a mutation. Variables and angle-bracket fields are
generic operator-supplied placeholders; no example identifies a real deployment.

## Identity and context

```sh
runai version
runai config set --cp-url "$RUNAI_API"
runai login access-key --client-id "$RUNAI_CLIENT_ID" \
  --secret-file "$RUNAI_SECRET_FILE" --interactive=disabled
runai cluster list
runai cluster set "$CLUSTER_NAME"
runai project list
runai project set "$PROJECT"
runai training standard submit --help
runai inference standard submit --help
runai training mpi submit --help
runai training pytorch submit --help
runai inference distributed submit --help
```

Protect CLI configuration/token files and the secret file; avoid `--save`, debug
traces or full config dumps unless required and protected. `config set` changes
the local CLI context. Readbacks establish which cluster/project a later command
will use; a display name is not an API UUID.

Source: `runai_config_set.md`, `runai_login_access-key.md`, `runai_cluster_set.md`,
`runai_project_set.md`, and corresponding submit pages in the directory above.
The explicit `standard` command group avoids relying on release-specific aliases.

## Finite standard training

Use an approved immutable CPU image containing `/bin/sleep`; this example consumes
no GPU and tests execution/lifecycle, not scientific correctness.

```sh
runai training standard submit "$JOB" -p "$PROJECT" -i "$CPU_IMAGE" \
  --cpu-core-request 1 --cpu-memory-request 512Mi \
  --gpu-devices-request 0 --backoff-limit 0 \
  --command -- /bin/sleep 60
runai training standard describe "$JOB" -p "$PROJECT" -o json
runai training standard logs "$JOB" -p "$PROJECT" --tail=100 --timestamps
```

For a scientific job, prefer the reviewed existing template:
`runai training standard submit "$JOB" -p "$PROJECT" --template "$TRAINING_TEMPLATE"`.
The image, command and parameters must match that template's intended workload.
Logs may contain sensitive content; retain selected output privately.

## Standard inference

Use a reviewed inference template with its vendor image, resource envelope,
credential references and readiness handler. The explicit serving override below
uses the approved OAuth client identity, not a numeric account ID.

```sh
runai inference standard submit "$ENDPOINT" -p "$PROJECT" \
  --template "$INFERENCE_TEMPLATE" \
  --serving-port="container=$HTTP_PORT,protocol=http,authorization-type=authorizedUsersOrGroups,authorized-users=$CALLER_CLIENT_ID" \
  --min-replicas 1 --max-replicas 1 --concurrency-hard-limit 1 \
  --initialization-timeout-seconds 1800 --request-timeout-seconds 600
runai inference standard describe "$ENDPOINT" -p "$PROJECT" -o json
runai inference standard logs "$ENDPOINT" -p "$PROJECT" --tail=100 --timestamps
```

This one-replica/concurrency1 configuration is an illustrative bounded recipe,
not a universal model setting. A locked policy may reject overrides; inspect it
instead of weakening authorization. Use the returned serving URL for real API
requests. CLI success does not qualify prediction results or sustained health.

## Distributed training/MPI

Use an existing MPI template that defines a valid launcher, worker image and
resources. Do not replace its launcher with a generic shell.

```sh
runai training mpi submit "$MPI_JOB" -p "$PROJECT" --template "$MPI_TEMPLATE" \
  --workers 2 --slots-per-worker 1
runai training mpi describe "$MPI_JOB" -p "$PROJECT" -o json
runai training mpi logs "$MPI_JOB" -p "$PROJECT" --tail=100 --timestamps
```

For PyTorch, inspect `runai training pytorch submit --help`; the checked command
supports `--workers`, per-worker resource flags, `--master-command`/`--master-args`
and worker arguments after `--`. Match the documented image/entrypoint rather
than translating an MPI recipe mechanically. Distributed inference has its own
`runai inference distributed` group and schema. Confirm gang quota and every
rank's actual GPU/transport; one successful rank is not a distributed pass.

## Cleanup after validation

For finite training, confirm native completion and retrieve/validate required
outputs and checkpoints first. For serving, verify the authorized external
endpoint and representative requests, including the required idle/recovery
checks. A successful submit or `describe` alone does not finish these gates.

When cleanup is within the task's authorization, choose the matching command for
the exact temporary workload. Do not delete a retained user service or paste all
three commands as a submit-and-immediate-delete script.

```sh
runai training standard delete "$JOB" -p "$PROJECT"
runai inference standard delete "$ENDPOINT" -p "$PROJECT"
runai training mpi delete "$MPI_JOB" -p "$PROJECT"
```

## REST transport and method map

`RUNAI_AUTH_CONFIG` is an existing protected curl config containing authentication;
never print it. JSON bodies live in reviewed files, not shell-interpolated text.
Current v3.0 token authentication is `POST /api/v2/token` with URL-encoded form
fields; see [identity guidance](cli-api-auth.md). Do not paste tokens into examples.

```sh
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" \
  --json @training.json "$RUNAI_API/api/v1/workloads/trainings"
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" \
  "$RUNAI_API/api/v1/workloads/trainings/$WORKLOAD_ID"
```

The following are independent lifecycle operations, not the next steps of a
submission script. Suspend only when it matches the task and checkpoint contract;
resume the intended workload; delete only after the validation/retention gate.

```sh
# Native suspend/resume manage lifecycle; application checkpoint compatibility
# must be qualified separately. These POSTs do not have invented JSON bodies.
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" --request POST \
  "$RUNAI_API/api/v1/workloads/trainings/$WORKLOAD_ID/suspend"
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" --request POST \
  "$RUNAI_API/api/v1/workloads/trainings/$WORKLOAD_ID/resume"
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" --request DELETE \
  "$RUNAI_API/api/v1/workloads/trainings/$WORKLOAD_ID"
```

| Purpose | Checked method/path and scope |
| --- | --- |
| Standard training | POST `/api/v1/workloads/trainings`; GET/DELETE same path plus `/{workloadId}`; project/cluster in create body |
| Standard inference | POST `/api/v1/workloads/inferences`; GET/DELETE plus `/{workloadId}`; project/cluster in create body |
| Distributed training | POST `/api/v1/workloads/distributed`; GET/DELETE plus `/{workloadId}`; distributed schema, not standard training body |
| Templates | GET/POST `/api/v1/workload-templates/trainings` and `/inferences`; GET/DELETE plus `/{templateId}`; native meta `scopeType`/`scopeId` |
| Training/inference policy | GET/PATCH `/api/v2/policy/trainings` or `/inferences`; GET requires `scope` plus matching project/department/cluster identifiers |
| Policy validation | PATCH previous path with `?validateOnly=true`; validates without applying that policy; not a universal dry-run query |
| Role definitions | GET/POST `/api/v2/authorization/roles`; `roles/read` or `roles/create`; role definition tenant/system scope differs from assignment scope |
| Access-rule assignments | GET/POST `/api/v1/authorization/access-rules`; `access_rules/read` or `access_rules/create`; subject, numeric roleId and actual assignment scope |
| Permission-set catalog | GET `/api/v1/authorization/permission-sets`; `roles/read`; use returned UUIDs when defining roles |

There is no guessed `/api/v1/authorization/roles` example: the checked role path
is v2. For scoping, read the response/schema and effective privileges, not only an
endpoint name. DELETE202 followed by GET200/`deletedAt` is normal retained history
in this version; verify physical cleanup independently.

### Training body: `TrainingCreationRequest`

```json
{
  "name": "example-training",
  "projectId": "<project-id>",
  "clusterId": "<cluster-uuid>",
  "spec": {
    "image": "<approved-cpu-image-ref>",
    "command": "/bin/sleep",
    "args": "60",
    "backoffLimit": 0,
    "compute": {"gpuDevicesRequest": 0, "cpuCoreRequest": 1, "cpuMemoryRequest": "512Mi"}
  }
}
```

### Inference body: `InferenceCreationRequest`

Use an approved HTTP image whose unchanged entrypoint serves port8000. Substitute
its real resource and health contract; the example is a CPU interface probe.

```json
{
  "name": "example-inference",
  "projectId": "<project-id>",
  "clusterId": "<cluster-uuid>",
  "spec": {
    "image": "<approved-http-image-ref>",
    "compute": {"gpuDevicesRequest": 0, "cpuCoreRequest": 1, "cpuMemoryRequest": "512Mi"},
    "autoscaling": {"minReplicas": 1, "maxReplicas": 1, "concurrencyHardLimit": 1},
    "servingConfiguration": {"initializationTimeoutSeconds": 1800, "requestTimeoutSeconds": 600},
    "servingPort": {"container": 8000, "protocol": "http", "clusterLocalAccessOnly": false,
      "authorizationType": "authorizedUsers", "authorizedUsers": ["<caller-oauth-client-id>"]}
  }
}
```

Use **`spec.servingConfiguration.initializationTimeoutSeconds`**; a same-named
autoscaling-era field is deprecated. Add readiness only through the installed
native schema. Do not infer startup/liveness support from Kubernetes examples.

### Training template body: `TrainingTemplateCreationRequest`

POST this reviewed body to `/api/v1/workload-templates/trainings`; later use the
actual returned template ID/name, with matching project scope.

```json
{
  "meta": {"name": "example-cpu-training", "scopeType": "project", "scopeId": "<project-id>"},
  "spec": {
    "image": "<approved-cpu-image-ref>", "command": "/bin/sleep", "args": "60",
    "compute": {"gpuDevicesRequest": 0, "cpuCoreRequest": 1, "cpuMemoryRequest": "512Mi"}
  }
}
```

### Training policy body: `TrainingPolicyChangeRequestV2`

First read the existing project policy using GET with `scope=project` and
`projectId`, after checking its installed read semantics. In3.0.20 the
[policy reader](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/policy-service/pkg/services/get.go#L58)
can initialize a missing tenant policy tree during GET. It is not guaranteed to
be side-effect free on a new scope; do not blindly add an internal query flag to
avoid that behavior. Inspect existing initialized state or the supported read
contract before a strictly read-only audit.

PATCH this candidate with `validateOnly=true` first. Actual application
changes admission for that scope; preserve unrelated existing defaults/rules.

```json
{
  "meta": {"name": "example-training-policy", "scope": "project", "projectId": "<numeric-project-id>"},
  "policy": {"defaults": {"priorityClass": "medium"}, "rules": {"priorityClass": {"canEdit": false}}}
}
```

The quoted numeric placeholder is a template marker: render it as a JSON integer
before sending. Unlike workload creation's string `projectId`, this policy schema
uses an integer. Do not send the literal marker or coerce every API identifier to
the same type.

### Role body: `RoleCreationFieldsInternal`

POST to `/api/v2/authorization/roles` only with the appropriate administrator
authorization; use the actual permission-set UUID from the catalog.

```json
{
  "name": "example-workload-properties-reader",
  "description": "Read tenant workload properties through the native API",
  "permissionSets": [{"id": "<permission-set-uuid>"}]
}
```

Creation alone assigns no user privilege. A separate native access-rule request
must use `subjectType: service-account`, the appropriate subject identity, the
returned numeric role ID, and the smallest required `scopeType`/`scopeId`.
Do not confuse display names, OAuth client IDs and internal subject IDs.

### Validation provenance and limits

All five JSON examples were parsed and checked against their named OpenAPI
request schema from the pinned 3.0.20 snapshot, with synthetic UUID and typed
numeric placeholder substitution and UUID-format checking. Method/path and CLI flag names
were checked against that source. No API mutation, credential lookup or workload
execution was performed. Schema validity cannot prove permission-set identity,
image availability, policy acceptance, actual namespace mapping or application
correctness; validate the installed server and user intent before use.
