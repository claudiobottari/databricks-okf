---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed3c6aa04eb1a30997cebba9339e693d737daf88fe8d64d954d26ccde2163198
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alter-view-as-alternative-to-drop
    - AVAATD
  citations:
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: ALTER VIEW as Alternative to DROP
description: When a view cannot be deleted because it is shared, Databricks recommends using ALTER VIEW to update it instead of dropping and recreating it.
tags:
  - sql-patterns
  - databricks
  - views
timestamp: "2026-06-18T11:55:32.589Z"
---

# ALTER VIEW as Alternative to DROP

When a view in Unity Catalog is shared through [Delta Sharing](/concepts/delta-sharing.md) (also called OpenSharing) or used in [clean rooms](/concepts/databricks-clean-rooms.md), dropping the view is blocked to preserve the sharing relationships. In such cases, `ALTER VIEW` provides a safe alternative for updating the view's definition without breaking existing sharing configurations.

## Error Scenario

Databricks blocks deletion of a securable object — such as a view — when it is actively shared via OpenSharing or used in clean rooms. The error message includes a hint: *"If you just want to update a shared view, please use `ALTER VIEW` instead."* ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

The error is classified with SQLSTATE 55006 (object not in prerequisite state) and is returned in several subtypes:

- `BY_CLEAN_ROOMS` – When the view is shared in clean rooms managed by a central clean room service.
- `BY_SHARES` – When the view is shared through one or more Delta Shares.
- `NO_HINT` – When the error occurs but no specific sharing detail is provided; the `ALTER VIEW` suggestion still applies.

In all cases, the system prevents `DROP VIEW` to avoid breaking the share or clean room that references the view.

## Using ALTER VIEW as Alternative

Instead of dropping and recreating a shared view (which would break the share), use `ALTER VIEW` to modify its definition. For example:

```sql
ALTER VIEW catalog.schema.shared_view AS
SELECT new_columns FROM updated_table WHERE conditions;
```

This updates the view’s query logic while preserving all Delta Share recipients and clean room associations that reference the view. No permissions need to be re‑granted, and no downtime occurs for consumers of the shared data.

## Best Practices

- **Prefer ALTER VIEW over DROP + CREATE** – When a view is shared, always use `ALTER VIEW` to change its definition. Dropping the view will fail if it is still referenced by a share or clean room.
- **Remove shares before dropping** – If you must delete the view entirely, first remove all shares that reference it (using `ALTER SHARE ... REMOVE` or the corresponding API) and clean up clean room references. Only then will `DROP VIEW` succeed.
- **Maintain backward compatibility** – When altering a shared view, ensure the new definition remains compatible with the schema expected by existing consumers to avoid query failures.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The protocol used to share views and other securable objects across workspaces.
- [Clean Rooms](/concepts/databricks-clean-rooms.md) – Secure collaboration environments that may reference shared views.
- DROP VIEW – The SQL statement that is blocked when the view is shared.
- ALTER VIEW – The recommended SQL statement to modify a view’s definition.
- Share Management – How to add or remove views from a Delta Share.
- [SQLSTATE 55006](/concepts/sqlstate-55006.md) – The error class for “object not in prerequisite state.”

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)
