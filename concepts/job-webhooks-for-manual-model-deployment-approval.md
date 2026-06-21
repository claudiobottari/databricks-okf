---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46c8969bf455a666e6cccd5d94cab733d4fb82e3aa38dbdb013e4a85ca498ca1
  pageDirectory: concepts
  sources:
    - upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - job-webhooks-for-manual-model-deployment-approval
    - JWFMMDA
  citations:
    - file: upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
title: Job Webhooks for Manual Model Deployment Approval
description: Using job notifications to call out to external CI/CD systems for manual approval gates before deploying production models, then using aliases to promote the model version
tags:
  - ci-cd
  - deployment
  - governance
  - databricks
timestamp: "2026-06-19T23:19:24.621Z"
---

# Job Webhooks for Manual Model Deployment Approval

**Job Webhooks for Manual Model Deployment Approval** refers to a pattern for integrating human sign-off into machine learning deployment pipelines on Databricks. While automated deployment is preferred, the platform supports using job notifications to trigger an external CI/CD system for manual approval before a model version is promoted to production. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Overview

Databricks recommends that teams **automate model deployment** whenever possible, relying on automated checks and tests during the deployment process. However, when manual approval is required — for example, for regulatory compliance or risk management — job notifications can be used to bridge the gap between training and production. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Workflow

1. A [model training job](/concepts/databricks-model-training.md) completes successfully.
2. The job sends a notification (via job notifications) to an external CI/CD system, requesting manual approval to deploy the model.
3. A human reviewer provides approval through the external system.
4. The CI/CD system then deploys the model version to serve traffic — for example, by setting the **“Champion”** alias on the model version, which [model serving endpoints](/concepts/model-serving-endpoint.md) can route traffic to.

This approach keeps the approval step decoupled from the Databricks environment and allows existing governance workflows to remain in place. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Job notifications – Mechanisms for sending alerts on job completion or failure.
- [Model Aliases](/concepts/model-aliases.md) – Named pointers to model versions (e.g., Champion, Challenger) used for traffic routing.
- [Model serving endpoints](/concepts/model-serving-endpoint.md) – Real-time inference endpoints that can use aliases to select the active model version.
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) – Integrating continuous integration and delivery into ML pipelines.
- [Unity Catalog Model Registry](/concepts/unity-catalog-model-registry.md) – The catalog where registered models and their versions are stored.

## Sources

- upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md](/references/upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws-c3150366.md)
