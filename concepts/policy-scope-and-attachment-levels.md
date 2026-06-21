---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e7e518b9fc740707712bc7595484e7955e60e5d97a9cf3dea27c32ac4cf7861
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-scope-and-attachment-levels
    - Attachment Levels and Policy Scope
    - PSAAL
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 17
      end: 18
    - file: 27-31
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 310
      end: 315
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 29
      end: 31
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
      start: 22
      end: 27
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
      start: 58
      end: 66
    - file: 29-31
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 74
      end: 79
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 363
      end: 365
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 373
      end: 375
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
      start: 368
      end: 370
    - file: 58-66
title: Policy Scope and Attachment Levels
description: GRANT policies in Unity Catalog can be attached at the catalog or schema level (not at the individual model level) and apply to all securable objects within that scope that match the condition.
tags:
  - unity-catalog
  - policy-management
  - scoping
timestamp: "2026-06-19T21:55:06.066Z"
---

---
title: Policy Scope and Attachment Levels
summary: The level in the resource hierarchy at which a policy is defined, determining which securable objects fall under its evaluation.
sources:
  - abac-grant-policies-for-models-beta-databricks-on-aws.md
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T17:23:33.953Z"
updatedAt: "2026-06-19T17:23:33.953Z"
tags:
  - data-governance
  - access-control
  - unity-catalog
  - architecture
  - serverless-budget-policy
aliases:
  - policy-scope-and-attachment-levels
  - Attachment Levels and Policy Scope
  - PSAAL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Policy Scope and Attachment Levels

**Policy Scope and Attachment Levels** describes where a policy is defined in a Databricks resource hierarchy and which securable objects it applies to. The attachment level determines the policy's reach: a policy attached at a higher level (e.g., catalog or experiment) applies to all descendants within that scope unless overridden, while a policy attached at a narrower level (e.g., schema) is confined to that specific resource. This concept is fundamental to both [ABAC GRANT Policies](/concepts/abac-grant-policy.md) and [serverless budget policies](/concepts/serverless-budget-policy.md). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Attachment Levels for ABAC GRANT Policies

In Databricks Unity Catalog, ABAC GRANT policies can be attached only at the **catalog** or **schema** level (in Beta). These policies dynamically grant the `EXECUTE` privilege on models whose governed tags match a condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:17-18, 27-31]

- **Catalog-level attachment**: The policy applies to all models in that catalog, subject to the tag-matching condition.
- **Schema-level attachment**: The policy applies only to models within that schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:17-18]

A policy attached at the catalog level is inherited by all schemas within the catalog; this inheritance can be seen using `SHOW EFFECTIVE POLICIES ON SCHEMA ...`. A policy attached at the schema level does not apply to objects in other schemas in the same catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:310-315]

The scope of a GRANT policy is defined by its `ON CATALOG` or `ON SCHEMA` clause together with the condition that matches governed tags. If no condition is specified, the policy applies to all models within that catalog or schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:29-31]

## Attachment Levels for Serverless Budget Policies

Serverless budget policies control spending on serverless workloads such as MLflow scorers and evaluations. These policies can be attached to an **MLflow experiment**. When attached, MLflow uses the specified budget policy for every serverless workload it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md:22-27]

If the workspace default serverless budget policy is disabled and no policy is assigned to the experiment, MLflow returns a `403 PERMISSION_DENIED` error when attempting to create serverless workloads. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md:58-66]

This attachment level (experiment) is distinct from the catalog/schema level used by GRANT policies, but follows the same principle: the policy’s scope is the experiment and all serverless workloads triggered from it. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md:22-27]

## Relationship Between Attachment Level and Effective Scope

The **scope** of a policy is the set of securable objects (models, experiments, etc.) that are evaluated against the policy’s conditions. For ABAC GRANT policies, scope is determined by:

1. The catalog or schema the policy is attached to.
2. The tag-matching condition (`WHEN` clause) that filters which models within that catalog/schema receive the privilege. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:29-31]

When a policy is attached at a higher level (e.g., a catalog), it affects all objects under that catalog that meet the condition. When attached at a lower level (e.g., a schema), the effect is narrower. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:17-18, 29-31]

The effective privileges on a model are the union of direct grants and any applicable GRANT policies from the model's catalog or schema. A principal holds `EXECUTE` if either a direct grant or a matching GRANT policy applies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:74-79]

## Best Practices

- **Attach at the smallest scope that covers the targets**: A broader scope may bring unrelated securables into the policy’s tag-matching and grant unintended access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:363-365]
- **Use direct grants for foundational permissions**: `USE CATALOG` and `USE SCHEMA` must be granted directly; GRANT policies cannot grant them. Use GRANT policies only for `EXECUTE` on models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:373-375]
- **Combine with tag inheritance**: Apply default tag values at the parent catalog or schema so descendants inherit them. Override tags on specific objects as needed. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md:368-370]
- **For serverless budget policies**, explicitly assign a policy to an experiment when the default workspace policy is disabled. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md:22-27, 58-66]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Direct Grants vs. GRANT Policies](/concepts/direct-grant-vs-grant-policy-interaction.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
3. [abac-grant-policies-for-models-beta-databricks-on-aws.md:17-18](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
4. 27-31
5. [abac-grant-policies-for-models-beta-databricks-on-aws.md:310-315](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
6. [abac-grant-policies-for-models-beta-databricks-on-aws.md:29-31](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
7. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md:22-27](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
8. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md:58-66](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
9. 29-31
10. [abac-grant-policies-for-models-beta-databricks-on-aws.md:74-79](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
11. [abac-grant-policies-for-models-beta-databricks-on-aws.md:363-365](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
12. [abac-grant-policies-for-models-beta-databricks-on-aws.md:373-375](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
13. [abac-grant-policies-for-models-beta-databricks-on-aws.md:368-370](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
14. 58-66
