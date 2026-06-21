---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1c62997cd86d3ac8251c692cbba87808c4d06b96801c641a255f02ea6556d1f
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - audit-logging-for-abac-policy-operations
    - ALFAPO
    - Audit logging for policies
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Audit Logging for ABAC Policy Operations
description: Databricks logs governed tag assignment/deletion events and ABAC policy CRUD operations (create, delete, get, list) in the system.access.audit table for monitoring and compliance.
tags:
  - data-governance
  - audit
  - unity-catalog
timestamp: "2026-06-19T09:34:20.634Z"
---

# Audit Logging for ABAC Policy Operations

**Audit Logging for ABAC Policy Operations** refers to the recording of actions related to [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies and [Governed Tags](/concepts/governed-tags.md) in the Databricks [audit log system table](/concepts/audit-log-system-table-requirements.md). This logging enables administrators to track who performed governed tag assignments and ABAC policy CRUD operations, when they occurred, and what the outcome was. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## What Is Logged

Databricks logs all governed tag assignment and deletion events, as well as ABAC policy create, delete, view (describe), and list operations. The audit log captures these events under the `unityCatalog` service name. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Governed Tag Operations

Tag-related actions are logged with the action names `createEntityTagAssignment` and `deleteEntityTagAssignment`. The recorded details include the workspace ID, [Metastore](/concepts/metastore.md) ID, tag assignment data, response status, and source IP address. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### ABAC Policy Operations

Policy-related actions are logged with action names `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies`. The logged fields include the policy name, the securable object type and full name, policy information (such as conditions and function reference), response status, and the acting user’s identity. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Querying Audit Logs

The audit log data resides in the `system.access.audit` table. The following example queries illustrate how to retrieve tag assignment history and policy CRUD operations. For more detailed documentation, see Audit logs.

```sql
-- All tag assignment and deletion events from the audit log
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

-- All ABAC policy CRUD operations
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

^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Use Cases

- **Compliance monitoring**: Verify that only authorized users are modifying tag assignments or policy definitions.
- **Change tracking**: Identify when a policy was created, updated, or deleted, and by whom.
- **Troubleshooting**: Investigate unexpected access changes by reviewing the sequence of policy and tag modifications.

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
