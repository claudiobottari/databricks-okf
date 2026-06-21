---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1598178991001b9d0b03fa3619b77404e48ad936b90de357cc8c2f832c448972
  pageDirectory: concepts
  sources:
    - upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - model-aliases-for-production-rollouts
    - MAFPR
  citations:
    - file: upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
title: Model Aliases for Production Rollouts
description: Using aliases like 'Champion' on registered models to manage production model versions and promote models across environments in Unity Catalog
tags:
  - model-management
  - deployment
  - unity-catalog
  - mlops
timestamp: "2026-06-19T23:19:32.093Z"
---

## [Model Aliases](/concepts/model-aliases.md) for Production Rollouts

**Model aliases** in [Unity Catalog](/concepts/unity-catalog.md) provide a mechanism to manage production rollouts of machine learning models. A model alias is a named pointer (such as `Champion`, `Challenger`, or `Production`) that can be assigned to a specific model version. By using aliases, deployment and inference workflows can reference a logical name rather than a specific version number, enabling safe, gradual rollouts and simple rollback. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Using Aliases for Rollouts

During model deployment, you can assign an alias to a model version to designate it for a particular role. For example, the `Champion` alias might point to the current production version, while a `Challenger` alias points to a candidate for rollout. Inference endpoints and batch jobs can be configured to load the model version behind a given alias, so updating the alias automatically shifts traffic without changing application code. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

Databricks recommends using aliases to manage production model rollouts. This approach is especially useful when combined with traffic splitting for [Model Serving](/concepts/model-serving.md) endpoints: you can route a small fraction of traffic to a model behind a `Challenger` alias while the majority continues to use the `Champion` alias. As confidence grows, you can increase traffic to the challenger until it fully replaces the champion. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Manual Approval and Alias Setting

If your organization requires manual approval before deploying a model to production, you can use job notifications to trigger an external CI/CD system after a training job completes successfully. Once approved, the CI/CD system can set the appropriate alias (for example, `Champion`) on the approved model version, which causes the serving endpoint or batch pipeline to start using that version. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Requirements

Only the owner of a registered model can set an alias on one of its versions. This privilege restriction ensures that production rollouts are controlled by authorized principals. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) — Central repository for managing models and their versions.
- [Model Serving](/concepts/model-serving.md) — Serving endpoints that can consume aliased model versions.
- [Traffic splitting](/concepts/traffic-splitting-between-models.md) — Gradually shifting traffic between model versions during rollouts.
- Champion/Challenger pattern — A common deployment strategy using aliases.
- Job notifications — Automation triggers for manual approval workflows.

### Sources

- upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md](/references/upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws-c3150366.md)
