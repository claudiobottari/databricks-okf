---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b35add2dcbe42032b0f5034075f0700126576e8aeef2bb61634723227ab546a
  pageDirectory: concepts
  sources:
    - model-deployment-patterns-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hybrid-deploy-code-approach
    - HDCA
    - Deploy Code Approach
  citations:
    - file: model-deployment-patterns-databricks-on-aws.md
title: Hybrid Deploy Code Approach
description: A variation of the deploy code pattern where code is deployed to staging, the model is trained on full production data in staging, and then the trained model artifact is deployed to production, saving training costs in production.
tags:
  - mlops
  - deployment
  - cost-optimization
timestamp: "2026-06-19T19:42:33.851Z"
---

# Hybrid Deploy Code Approach

The **Hybrid Deploy Code Approach** is a model deployment pattern that combines elements of both the [Deploy Code Approach](/concepts/hybrid-deploy-code-approach.md) and the [Deploy Models Approach](/concepts/deploy-models-pattern.md). In this pattern, training code is deployed to the staging environment, where the model is trained on the full production dataset. The resulting model artifact is then deployed to the production environment for serving. ^[model-deployment-patterns-databricks-on-aws.md]

## Overview

The Hybrid Deploy Code Approach is described by Databricks as a variation of the standard deploy code pattern for situations where training the model in the production environment is not ideal. Instead of training in production, the model is trained in staging over the full production dataset, and then the trained model artifact is promoted to production. ^[model-deployment-patterns-databricks-on-aws.md]

## Advantages

This approach offers several benefits:

- **Reduced training costs in production:** By training the model in the staging environment rather than production, you avoid the computational expense of running training jobs in the production environment. ^[model-deployment-patterns-databricks-on-aws.md]
- **Access to production data:** The model can be trained on the full production dataset, which may not be accessible from the development environment for security or compliance reasons. ^[model-deployment-patterns-databricks-on-aws.md]

## Disadvantages

- **Added operational cost in staging:** Training on the full production dataset in staging introduces an extra operational expense that would not exist in the standard deploy code pattern. ^[model-deployment-patterns-databricks-on-aws.md]

## When to Use

Consider the Hybrid Deploy Code Approach when your situation requires that the model be trained on the full production dataset, but you want to avoid running training workloads in the production environment. This can be relevant in organizations where:

- Access to production compute resources is limited or expensive.
- Production environment security policies restrict training workloads.
- You want to maintain separation between training infrastructure and serving infrastructure.

## Relationship to Standard Patterns

The Hybrid Deploy Code Approach is closely related to the two primary deployment patterns:

- **[Deploy Code Approach](/concepts/hybrid-deploy-code-approach.md):** The standard recommended pattern where code is promoted through environments and training happens in each environment. The hybrid approach modifies this by moving the final training step from production to staging.
- **[Deploy Models Approach](/concepts/deploy-models-pattern.md):** In this alternative pattern, the model artifact is trained entirely in development and deployed through staging to production. The hybrid approach differs by still using code promotion for staging but using artifact promotion for production.

## Environment Mapping

In the Hybrid Deploy Code Approach, the typical mapping of activities to environments is:

| Environment | Training | Testing | Serving |
|-------------|----------|---------|---------|
| Development | Training on sample data | Unit tests | — |
| Staging | Training on full production data | Integration tests | — |
| Production | — | — | Model serving |

## Related Concepts

- MLOps Workflow — The overall MLOps pipeline that these deployment patterns fit into.
- Model Promotion — The process of moving model artifacts between environments.
- [Model Serving](/concepts/model-serving.md) — Running trained models in production to serve predictions.
- [Unity Catalog](/concepts/unity-catalog.md) — Typically used to organize environments as separate catalogs.

## Sources

- model-deployment-patterns-databricks-on-aws.md

# Citations

1. [model-deployment-patterns-databricks-on-aws.md](/references/model-deployment-patterns-databricks-on-aws-231ed92b.md)
