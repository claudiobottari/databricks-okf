---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e76a88081be4defbe32ea945945847ac6ba0da6f9de7ab6e9f1bc7e803884e77
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-bricks-knowledge-assistant-incompatibility
    - ABKAI
    - Agent Bricks Knowledge Assistant
    - Knowledge Assistant
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Agent Bricks Knowledge Assistant Incompatibility
description: A known limitation where Knowledge Assistant does not support foundation model Unity Catalog permissions, requiring users to contact their account team before enabling the feature.
tags:
  - databricks
  - limitations
  - knowledge-assistant
timestamp: "2026-06-19T10:39:56.609Z"
---

Here is the wiki page for "Agent Bricks Knowledge Assistant Incompatibility".

---

# Agent Bricks Knowledge Assistant Incompatibility

**Agent Bricks Knowledge Assistant Incompatibility** refers to a specific limitation of the [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) feature: the [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) agent does not support the Unity Catalog permissions-based model access controls that govern pay-per-token, provisioned throughput, and batch inference workloads for other Databricks-hosted foundation models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Overview

When an account admin enacts foundation model Unity Catalog permissions — by removing the default `EXECUTE` privilege on the `system.ai` schema and selectively granting it on approved individual models — the policy is automatically enforced for [pay-per-token](/concepts/pay-per-token-pricing.md) endpoints and [batch inference (AI Functions)](/concepts/ai-functions-and-batch-inference.md) workloads. However, [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) calls are **not** subject to this permission model. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When the Incompatibility Applies

The incompatibility becomes relevant whenever an organization uses foundation model Unity Catalog permissions to restrict which foundation models are accessible. This includes:

- Scenarios where export-controlled, vendor-restricted, region-restricted, or corporate-policy-prohibited model families must be blocked for most users. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]
- Cases where an admin removes `EXECUTE` from the `system.ai` schema to clear all default access, then selectively re-grants permission on approved models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

Under these conditions, Knowledge Assistant continues to serve all models that are otherwise disallowed by the Unity Catalog permission policy, because it does not participate in that policy.

## Practical Effect

- **Pay-per-token endpoints** and **batch inference** workloads automatically stop serving disallowed models immediately after the schema’s `EXECUTE` permission is removed. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]
- **Provisioned throughput** endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]
- **Knowledge Assistant** is unaffected by both the schema-level and the model-level permissions. It can still call any foundation model, regardless of the admin’s Unity Catalog restrictions. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Mitigation

Because the feature is listed as a limitation of foundation model Unity Catalog permissions, the only available mitigation is to contact your Databricks account team before enabling the feature if you actively use Knowledge Assistant. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) — The permission system that Knowledge Assistant does not support.
- [system.ai Schema](/concepts/systemai-schema.md) — The Unity Catalog schema containing model objects.
- [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) — The agent that is incompatible with this permission model.
- [Pay-per-token](/concepts/pay-per-token-serving-mode.md) — One workload type that *does* enforce the permission.
- [Batch inference](/concepts/batch-inference-pipelines.md) — Another workload type that enforces the permission.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — A workload type that requires manual endpoint deletion for enforcement.

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
