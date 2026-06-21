---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bcd10825095cc2a397bc77bdf4adf2a2843009723bcb3bdf47d761e62497d42
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-audit-logging
    - APAL
    - Audit Logging
    - Audit logging
    - audit logging
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Policy Audit Logging
description: Databricks logs all governed tag and ABAC policy operations (create, delete, list, get) in the system.access.audit table for compliance and monitoring.
tags:
  - auditing
  - unity-catalog
  - security
  - compliance
timestamp: "2026-06-19T17:59:37.026Z"
---

# ABAC Policy Audit Logging

**ABAC Policy Audit Logging** refers to the recording and tracking of operations related to [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in [Unity Catalog](/concepts/unity-catalog.md), including governed tag assignments and policy CRUD (create, read, update, delete) actions. Databricks logs these events in the `system.access.audit` system table, enabling administrators to monitor policy changes and investigate access-related issues. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Logged Events

### ABAC Policy CRUD Operations

The following actions are logged for ABAC policies in Unity Catalog: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

| Action Name | Description |
|-------------|-------------|
| `createPolicy` | A new policy is created |
| `deletePolicy` | An existing policy is deleted |
| `getPolicy` | Policy details are retrieved |
| `listPolicies` | Policies are listed for a securable object |

These actions apply to all ABAC policy types, including [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Tag Operations

Changes to governed tags are also logged, as tags determine which policies apply to which data assets. The following tag-related actions are recorded: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

| Action Name | Description |
|-------------|-------------|
| `createEntityTagAssignment` | A tag is assigned to a securable object |
| `deleteEntityTagAssignment` | A tag is removed from a securable object |

## Querying the Audit Log

Audit log entries for ABAC policy and tag operations are stored in the `system.access.audit` system table. The `service_name` for all Unity Catalog operations is `'unityCatalog'`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Example: Query Tag Operations

The following SQL query retrieves all tag assignment and deletion events: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SELECT
  event_time,
  action_name,
  user_identity.email AS actor,
  request_params.workspace_id,
  request_params.metastore_id,
  request_params.tag_assignment,
  response.status_code,
  source_ip_address
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN (
    'createEntityTagAssignment',
    'deleteEntityTagAssignment'
  )
ORDER BY event_time DESC;
```

### Example: Query Policy CRUD Operations

The following SQL query retrieves all ABAC policy create, delete, get, and list operations: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SELECT
  event_time,
  action_name,
  user_identity.email AS actor,
  request_params.name AS policy_name,
  request_params.on_securable_type,
  request_params.on_securable_fullname,
  request_params.policy_info,
  response.status_code
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN ('createPolicy', 'deletePolicy', 'getPolicy', 'listPolicies')
ORDER BY event_time DESC;
```

## Related Concepts

- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — The `system.access.audit` table that stores audit events
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model governing policy operations
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing ABAC capabilities
- [Governed Tags](/concepts/governed-tags.md) — Tags that drive ABAC policy evaluation
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
