---
name: nebius-serverless-jobs
description: Plan, run, verify, and clean up Nebius Serverless jobs for training, batch inference, evaluation, preprocessing, and finite scientific workflows.
---

# Nebius Serverless Jobs

Use this skill for finite training, batch inference, evaluation,
preprocessing, simulation, and scientific workloads.

## Plan

1. Confirm profile, project, region, immutable image, command/arguments,
   platform/preset, timeout, restart/checkpoint policy, preemptible choice,
   secret selectors, and object-storage input/output mounts.
2. Make inputs reproducible and outputs durable. Required results must not
   depend on container-local storage.
3. Explain cost and interruption behavior and obtain confirmation before
   creating the paid job. Prefer preemptible GPUs only for
   restartable/checkpointed work.
4. Check the installed CLI:

   ```bash
   /usr/local/bin/nebius ai job create --help
   ```

## Create and verify

```bash
/usr/local/bin/nebius --profile <PROFILE> ai job create \
  --parent-id '<PROJECT_ID>' \
  --name '<JOB_NAME>' \
  --image '<DIGEST_OR_VERIFIED_SHORT_ALIAS>' \
  --platform '<PLATFORM>' \
  --preset '<PRESET>' \
  --preemptible \
  --container-command '<ENTRYPOINT>' \
  --args '<ARGUMENTS>' \
  --volume 's3://<INPUT_BUCKET>:/workspace/input:ro' \
  --volume 's3://<OUTPUT_BUCKET>:/workspace/output:rw' \
  --timeout '<DURATION>'
```

Omit `--preemptible` when interruption would invalidate the workflow. Add
`--env-secret` and `--registry-secret` selectors when required; never inline
their values.

1. Record job/operation IDs, image digest, project/region, platform/preset,
   GPU type/count, preemptible choice, dataset identity, and command.
2. Monitor `nebius ai get <JOB_ID> --format json` and non-secret
   `nebius ai logs <JOB_ID> --tail 200 --timestamps`.
3. Validate terminal state and exit code, expected output objects,
   sizes/checksums when practical, metrics, and a representative serving or
   inference handoff when applicable.
4. A successful job state alone is not artifact verification. Do not claim
   training readiness without measured metrics and verified output artifacts.
5. Cancel failed or unnecessary jobs; delete task-owned jobs, temporary image
   aliases, and temporary selectors only after durable outputs are secured.

Never put credentials, registry auth, patient/customer data, or private
artifacts in command arguments or logs.
