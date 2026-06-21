---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c07e8da58a645bd4d0faff800267efeb157ef124b5042ff9ffe6be3979aedeb7
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - permissions-for-custom-classifiers
    - PFCC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Permissions for Custom Classifiers
description: "Role and privilege requirements for managing custom classifiers: metastore admin role, ASSIGN on the governed tag, and SELECT on example table columns."
tags:
  - data-governance
  - unity-catalog
  - security
  - permissions
timestamp: "2026-06-19T14:39:31.533Z"
---

# Permissions for Custom Classifiers

**Permissions for Custom Classifiers** refers to the specific access privileges required to create, edit, delete, and interact with custom classifiers in Databricks Data Classification within Unity Catalog. Custom classifiers extend the built-in classification system to detect organization-specific sensitive data types. ^[custom-classifiers-databricks-on-aws.md]

## Required Privileges by Operation

### [Metastore](/concepts/metastore.md) Admin Role

To create, edit, or delete a custom classifier, you must be a **metastore admin**. This is the highest-level permission required for managing custom classifiers. ^[custom-classifiers-databricks-on-aws.md]

### Governed Tag ASSIGN Privilege

To create or edit a custom classifier, you must have `ASSIGN` privileges on the [governed tag](/concepts/governed-tags.md) that the classifier uses. This privilege controls which users can associate a governed tag with data classification rules. ^[custom-classifiers-databricks-on-aws.md]

### Table SELECT Privilege

To select a column as an example for a custom classifier, you must have `SELECT` permission on the table that contains that column. If you lack this permission, you must request it from the table owner or choose a different example column. ^[custom-classifiers-databricks-on-aws.md]

## Permission Errors and Troubleshooting

### Permission Denied When Creating or Listing

If you encounter a permission denied error when creating or listing custom classifiers, verify that:

- You are a [Metastore](/concepts/metastore.md) admin.
- You have `ASSIGN` privileges on the governed tag you intend to use (for creation or editing).

^[custom-classifiers-databricks-on-aws.md]

### Cannot Select an Example Column

If you cannot select an example column during classifier creation or editing, you likely lack `SELECT` permission on the table. Resolve this by:

- Asking the table owner to grant `SELECT` on the table.
- Choosing a different example column from a table where you have the required access.

^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The tagging system used by custom classifiers to label detected data
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that hosts Data Classification
- [Metastore Admin](/concepts/metastore-admin-role.md) — The role required to manage custom classifiers
- [Data Classification](/concepts/data-classification.md) — The system that custom classifiers extend
- Table Permissions in Unity Catalog — Broader access control model for tables

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
