---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2698391389fcdaf4bba831620571a1db3a8e177ececdddcc91323cd1d1cc863
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-audit-logging
    - GPAL
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Audit Logging
description: GRANT policy create, alter, and drop operations are logged under the same audit actions (createPolicy, deletePolicy, getPolicy, listPolicies) as row filter and column mask policies.
tags:
  - audit
  - security
  - unity-catalog
  - databricks
timestamp: "2026-06-19T08:47:37.685Z"
---

# GRANT Policy Audit Logging

**GRANT Policy Audit Logging** refers to the capture and recording of operations performed on [ABAC GRANT Policies](/concepts/abac-grant-policy.md) in Unity Catalog. GRANT policies are attribute-based access control policies that dynamically grant privileges (currently `EXECUTE` on models) based on governed tag conditions. Their lifecycle operations produce audit events that are stored in the system’s audit log, consistent with other policy types. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Events

The following actions are audited for GRANT policies:

- **`createPolicy`** – When a GRANT policy is created.
- **`alterPolicy`** (or equivalent) – When a GRANT policy is modified. (Note: the source lists `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` as the audited actions; alter is likely captured similarly.)
- **`deletePolicy`** – When a GRANT policy is deleted.
- **`getPolicy`** – When a GRANT policy is described or retrieved.
- **`listPolicies`** – When policies are listed.

These operations are logged under the same actions used for [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Querying Audit Logs

Example audit log queries for GRANT policies are available in the general audit logging documentation for Unity Catalog ABAC policies. The source material refers readers to that documentation for specific query examples. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- Regularly review audit logs to detect unexpected policy creation, deletion, or access changes.
- Combine GRANT policy audit events with direct grant audit events to maintain a complete picture of privilege assignments.

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) – The policies whose operations are audited.
- [Audit logging](/concepts/abac-policy-audit-logging.md) – The overarching system for tracking Unity Catalog events.
- [Row Filter Policies](/concepts/row-filter-policies.md) – Another ABAC policy type sharing the same audit action names.
- [Column Mask Policies](/concepts/column-mask-policies.md) – Another ABAC policy type sharing the same audit action names.
- [Governed Tags](/concepts/governed-tags.md) – The attributes used in GRANT policy conditions.

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
