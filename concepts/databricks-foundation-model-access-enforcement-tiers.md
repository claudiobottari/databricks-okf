---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eda63cb49af7a5f96afc707e001d6fb725da47b63a81fae6274949ad8175ab24
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-access-enforcement-tiers
    - DFMAET
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Databricks Foundation Model Access Enforcement Tiers
description: The three tiers of model access in Databricks — pay-per-token, batch inference (AI Functions), and provisioned throughput — each with different permission enforcement behaviors.
tags:
  - databricks
  - foundation-models
  - inference
timestamp: "2026-06-19T10:40:00.534Z"
---

---

title: Databricks Foundation Model Access Enforcement Tiers
summary: The 3-tier enforcement system for Databricks-hosted foundation models, ranging from unrestricted access to strict allow-list control, enforced via Unity Catalog permissions.
sources:
  - foundation-model-unity-catalog-permissions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:45:00.000Z"
updatedAt: "2026-06-19T09:45:00.000Z"
tags:
  - databricks
  - foundation-models
  - access-control
  - unity-catalog
aliases:
  - databricks-foundation-model-access-enforcement-tiers
  - foundation-model-access-tiers
  - fm-enforcement-tiers
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Databricks Foundation Model Access Enforcement Tiers

**Databricks Foundation Model Access Enforcement Tiers** describe the levels of access restriction that organizations can apply to Databricks-hosted foundation models using [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). The enforcement model ranges from fully open access to strict per-model allow-list control, with an intermediate tier that restricts access without requiring per-model grants.

## Overview

The enforcement tiers are implemented by granting or revoking the `EXECUTE` permission on the `system.ai` schema and individual model objects within Unity Catalog. By default, all users have `EXECUTE` on the schema, which opens all Databricks-hosted foundation models. Changes to permissions are enforced consistently across pay-per-token endpoints, batch inference (AI Functions), and provisioned throughput endpoints.

The choice of tier depends on the organization's legal, regulatory, and security requirements. Most organizations use the standard tier for daily operations, reserving the strict tier only when required by export control laws, vendor restrictions, or corporate policies. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Tier 1: Full Access (Default)

In the default state, all users have `EXECUTE` permission on the `system.ai` schema. This means every Databricks-hosted foundation model is accessible to every user, subject only to billing controls and other governance mechanisms such as [AI Gateway](/concepts/ai-gateway.md) rate limits. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

**Use when:** No legal or policy restrictions require blocking specific models. Day-to-day governance is handled through `system.billing` for cost attribution, AI Gateway for rate limits, and network controls for security. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Tier 2: Schema-Denied Access

At this tier, an admin revokes the default `EXECUTE` permission from the `system.ai` schema. This blocks all users from invoking any foundation model. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

**Use when:** An organization needs to temporarily halt all foundation model usage — for example, during an audit, while compliance requirements are being assessed, or while transitioning to a new policy.

**Effect:** All pay-per-token and batch inference (AI Functions) calls stop immediately. Provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Tier 3: Allow-List Access

After revoking schema-level `EXECUTE`, admins selectively grant `EXECUTE` permission on approved individual model objects within the `system.ai` schema. This creates an explicit allow-list of permitted models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

**Use when:** Legally required to restrict which specific models are open, such as:
- Export-controlled model families
- Vendor-restricted or region-restricted models
- Corporate policies prohibiting specific foundation models ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

**Implementation steps:**
1. Remove `EXECUTE` from the `system.ai` schema for all users/groups.
2. For each approved model, navigate to `system.ai.models.<model-name>` and grant `EXECUTE` to the desired principals.
3. Manually delete any provisioned throughput endpoints that serve disallowed models (these are not automatically enforced). ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Enforcement Across Workload Types

The tier system enforces access control differently depending on the workload type: ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

| Workload Type | Enforcement Behavior |
|---------------|---------------------|
| Pay-per-token endpoints | Automatic — permissions enforced on each API call |
| Batch inference (AI Functions) | Automatic — enforced at invocation time |
| Provisioned throughput endpoints | Manual — admins must delete disallowed endpoints |

## When to Use Each Tier

The source material states that foundation model Unity Catalog permissions should be used **only when legally required** to restrict specific models. For day-to-day governance, use other mechanisms: ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

- `system.billing` for cost tracking and attribution
- AI Gateway for rate limits and request-level usage tracking
- Private Link or private networking for secure connectivity
- Egress and network controls for restricting outbound traffic

## Limitations

- **Agent Bricks Knowledge Assistant** does not support foundation model Unity Catalog permissions. Organizations using Knowledge Assistant should contact their Databricks account team before enabling the feature. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md) — The feature enabling tiered access control
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — The API surface for model invocation
- [AI Gateway](/concepts/ai-gateway.md) — Rate limiting and usage tracking for models
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Dedicated compute for model serving
- [Batch Inference AI Functions](/concepts/ai-functions.md) — Batch inference workloads

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
