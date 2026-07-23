---
name: nebius-serverless-jobs
description: Plan, run, verify, and clean up Nebius Serverless jobs for training, batch inference, evaluation, preprocessing, and finite scientific workflows.
---

# Nebius Serverless Jobs

1. Confirm project, region, image digest, platform/preset, preemptible choice,
   command, timeout, input/output mounts, secrets, and artifact ownership.
2. Make inputs reproducible and outputs durable; do not rely on container-local
   storage for required results.
3. Monitor state and logs without printing credentials or customer data.
4. Validate exit status, expected artifacts, metrics, and a representative
   serving/inference handoff when applicable.
5. Record job/operation/instance IDs, image/digest, dataset identity, command,
   resources, timings, artifacts, and cleanup.
6. Cancel/delete temporary jobs and selectors and verify absence.
