# Interfaces, identity and lifecycle

Use [CLI setup](https://docs.nvidia.com/run-ai/self-hosted/v3.0/reference/cli/install-and-configure-cli),
the installed CLI help/version and the target server's reference. Older
`runai submit` and newer workload-oriented commands differ. Discover cluster and
project selection with help and make both explicit before mutation.
[Access-key login](https://docs.nvidia.com/run-ai/self-hosted/v3.0/reference/cli/runai/login/runai-login-access-key)
supports `--secret-file` in the checked CLI reference; prefer a protected file to
a secret in process arguments. Check the actual installed command's options.

## REST

The [v3.0 authentication guide](https://docs.nvidia.com/run-ai/self-hosted/v3.0/reference/rest-api/getting-started/how-to-authenticate-to-the-api)
and 3.0.20 source document `POST /api/v2/token`, form URL encoding and
`grant_type=client_credentials`, `client_id`, `client_secret`; response fields are
`access_token`, `token_type`, `expires_in`. The v1 token endpoint is deprecated in
that source. Other releases must use their own contract, not guessed aliases.

Use existing credential storage or protected curl config. Do not echo tokens,
print environment/configuration, enable shell tracing or commit auth responses.
Refresh for actual expiry with bounded transport retry. Never retry a denied
action with broader credentials as an unrequested workaround.

A live 3.0.20 test of simultaneous valid password grants to `/api/v2/token` for
one user returned 401/200 without shared-file I/O; five serial grants succeeded.
For this symptom, verify the exact grant before assuming a bad secret or rotating
it. Reuse an unexpired bearer; test serialized renewal per identity and atomic
token storage in concurrent clients. This is an observed version-specific symptom.

Read-only paths checked in the **3.0.20** assembled spec:

```sh
# Both variables refer to the authorized environment; config contains auth
# and is protected. Do not print its contents or the full request headers.
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" "$RUNAI_API/api/v1/clusters"
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" "$RUNAI_API/api/v1/org-unit/projects"
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" "$RUNAI_API/api/v1/workload-priorities"
curl --fail-with-body --config "$RUNAI_AUTH_CONFIG" "$RUNAI_API/api/v1/nodes"
```

Check installed paths, pagination and filter shapes before automation. Inspect
HTTP status plus structured body; an ingress HTML page is not application JSON.
Some API reads can materialize defaults: the checked3.0.20 policy GET can create
a missing tenant policy tree. Check the exact handler/contract before calling a
new scope read-only; see the [policy recipe](command-cookbook.md).

## Least privilege

Separate login, API action, scope, endpoint access, Kubernetes RBAC, cloud IAM and
registry/model credentials. A service account's display name, numeric identity
and OAuth client ID differ. Preserve OAuth client ID spelling/case in endpoint
authorized-user grants; read back and test that exact client identity. Do not
substitute an internal ID because login succeeded.

Use [documented roles/access rules](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/platform-management/authentication/roles).
In checked 3.0.20, custom role creation requires `name`, `description` and
`permissionSets: [{"id": "<permission-set-uuid>"}]`. Obtain actual set IDs from
`GET /api/v1/authorization/permission-sets` with an authorized role reader.
An access rule has a numeric `roleId` and an assignment scope; this is different
from the scope where a role definition lives. Prefer `subjectType: service-account`
where supported (`app` is deprecated in that snapshot). API-only roles need no
extra Kubernetes privileges.

Scope trap: 3.0.20 priorities require `workload-properties/read` at current tenant
or system scope; cluster-only Viewer can still receive 403. Nodes require
`nodes/read` and filter to permitted tenants/clusters. Inspect both `x-authorize`
and handler scope checks; select narrow native permission sets rather than
granting tenant administrator.

## Delete is not the same as purge

[Workload documentation](https://docs.nvidia.com/run-ai/self-hosted/v3.0/documentation/workloads-in-nvidia-run-ai/workloads)
retains deleted records for 14 days in the checked version. The
[3.0.20 training test](https://github.com/dsx-ai-factory/run-ai/blob/74280199d8665d14e12c88f4cd13dd6a408300ca/control-plane/workloads/pkg/services_crud/trainings_service_test.go#L258)
explicitly proves DELETE202 followed by GET200 with `deletedAt`.

Record separately: native delete accepted; owned active Pods/Jobs/routes and
reservations removed; required outputs/checkpoints retained; history timestamp/
state recorded; cloud GPU usage ceased. GET200 is not automatically a leak, and
DELETE202/GET404 alone does not prove cleanup. Use release-specific status,
deletion timestamps and list filters. Never remove finalizers or database rows
to make normal retained history disappear.
