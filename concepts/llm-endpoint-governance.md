---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bb241399b048eb456af0b5c837a20d5cf6606f7c0d6a241e3e8281e1e564ea6
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-endpoint-governance
    - LEG
  citations:
    - file: ai-governance-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: LLM endpoint governance
description: Controlling access to hosted and external LLM endpoints, enforcing rate limits, and tracking usage and costs across providers via Unity AI Gateway.
tags:
  - llm
  - ai-gateway
  - rate-limiting
  - cost-tracking
timestamp: "2026-06-18T10:42:07.059Z"
---

# LLM endpoint governance

**LLM endpoint governance** is the practice of controlling, monitoring, and managing access to large language model (LLM) endpoints across an organization. In the Databricks platform, this capability is provided by [Unity AI Gateway](/concepts/unity-ai-gateway.md), which serves as the enterprise control plane for governing AI traffic.^[ai-governance-databricks-on-aws.md]

## Key capabilities

Unify AI Gateway enables organizations to manage and monitor LLM endpoints from a central location. The core governance capabilities for LLM endpoints include:^[ai-governance-databricks-on-aws.md]

- **Access control**: Control which users, service principals, or groups can invoke specific hosted or external LLM endpoints.
- **Rate limiting**: Enforce usage limits to prevent abuse, manage costs, and ensure fair resource allocation across teams.
- **Usage tracking and cost monitoring**: Track how many requests each endpoint receives, by whom, and across which providers, enabling chargeback and capacity planning.

LLM endpoint governance is part of the broader [AI Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) framework, which applies the same access control, lineage, and audit model used for data assets to AI resources and AI traffic.^[ai-governance-databricks-on-aws.md]

## How LLM endpoint governance works

LLM endpoint governance is built on two layers:

1. **AI asset governance** — The underlying models served by the endpoints are managed as Unity Catalog securable objects. Access to MLflow Models and [Foundation Model APIs](/concepts/foundation-model-apis.md) is granted through standard Unity Catalog privileges. [ABAC GRANT Policies](/concepts/abac-grant-policy.md) can dynamically grant `EXECUTE` on models based on tag conditions, providing fine-grained access control to the models behind endpoints.^[abac-grant-policies-for-models-beta-databricks-on-aws.md, ai-governance-databricks-on-aws.md]

2. **AI traffic governance** — Unity AI Gateway acts as a proxy between users and LLM endpoints. It intercepts calls to both hosted foundation models (e.g., Databricks-hosted models in `system.ai`) and external provider endpoints. At this layer, administrators enforce rate limits, audit usage, and control who can reach each endpoint.^[ai-governance-databricks-on-aws.md]

Access control for endpoints is enforced at the model level (using Unity Catalog privileges) and supplemented by gateway-level policies such as rate limits. Because managed and external endpoints are registered as Unity Catalog securable objects, governance teams can apply consistent policies across all AI traffic.^[ai-governance-databricks-on-aws.md]

## Implementation

LLM endpoint governance is configured through Unity AI Gateway. Account admins can enable or disable the feature from the account console **Previews** page (the feature is currently in Beta). After activation, administrators can:^[ai-governance-databricks-on-aws.md]

- Register hosted and external LLM endpoints for management.
- Assign who can access each endpoint or endpoint category.
- Set rate limits per principal or per endpoint.
- View usage dashboards and audit logs.

For models served through Unity Catalog, administrators can also use [ABAC GRANT Policy](/concepts/abac-grant-policy.md) to grant `EXECUTE` based on tags, ensuring that only users with appropriate attributes can invoke the models exposed by the endpoint.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best practices

- **Use groups for endpoint access** to simplify permissions management and avoid maintaining individual user grants.
- **Combine Unity Catalog privileges and gateway policies** — secure the model with Unity Catalog ABAC policies and use the gateway to enforce operational controls such as rate limits and cost tracking.
- **Monitor usage regularly** to detect unexpected traffic patterns and adjust rate limits or access rules accordingly.
- **Audit endpoint access changes** using Unity Catalog audit logs to maintain a record of who was granted or revoked access.

## Related concepts

- [Unity AI Gateway](/concepts/unity-ai-gateway.md) — The control plane for managing LLM endpoints and MCP servers
- [AI Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) — The overall governance framework for AI assets and traffic
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Dynamic, tag-based privilege grants for models
- MLflow Models — Models that can be served through LLM endpoints
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation model endpoints
- [Account Admin (Unity Catalog)](/concepts/account-admin-unity-catalog.md) — Role responsible for enabling Unity AI Gateway and managing account-level governance

## Sources

- ai-governance-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
