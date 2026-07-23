---
name: use-nebius
description: Route Nebius operations to the smallest relevant project, registry/secret, Serverless endpoint, or Serverless job skill. Use after an exact Forge model skill has been selected or for direct Nebius resource work.
---

# Use Nebius

1. Resolve the explicit profile, tenant/project, region, network, registry, and
   existing resource state with `$nebius-project-discovery`.
2. Load `$nebius-registry-and-secrets` only when private images or runtime
   secrets are required.
3. Use `$nebius-serverless-endpoints` for interactive inference services.
4. Use `$nebius-serverless-jobs` for training, batch evaluation, preprocessing,
   or finite scientific workloads.
5. Record resource IDs, operations, platform/preset, preemptible choice, image
   digest, representative request, outputs/metrics, and cleanup.

Stop on authentication or authorization failure. Never switch credentials,
profiles, projects, or regions to bypass access controls.
