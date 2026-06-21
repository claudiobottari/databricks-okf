---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0813a708c339594a4e8d265ffce4d41011be3cb4eaed20a780876e2fe3ce03b8
  pageDirectory: concepts
  sources:
    - hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-views-for-columnrow-level-permissions
    - DVFCP
  citations:
    - file: hive-metastore-privileges-and-privileges-and-securable-objects-legacy-databricks-on-aws.md
    - file: hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md
title: Dynamic Views for Column/Row-Level Permissions
description: Using dynamic view functions (current_user() and is_member()) to implement column-level permissions, row-level permissions, and data masking in Hive metastore-managed views.
tags:
  - databricks
  - authorization
  - dynamic-views
  - data-masking
timestamp: "2026-06-19T10:47:41.510Z"
---

# Dynamic Views for Column/Row-Level Permissions

**Dynamic Views for Column/Row-Level Permissions** refer to a technique in Databricks’s legacy Hive [Metastore](/concepts/metastore.md) that uses SQL view definitions with built-in user functions — `current_user()` and `is_member()` — to enforce fine-grained access control at the column or row level. This approach allows administrators to restrict which data a user can see based on their identity or group membership without maintaining separate tables or complex ETL pipelines. ^[hive-metastore-privileges-and-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Overview

The Hive [Metastore](/concepts/metastore.md) supports a privilege model where permissions are inherited hierarchically from catalog to schema to table. However, this model alone does not allow granular control over individual columns or rows within a table. Dynamic views overcome this limitation by embedding access logic directly into the view’s SQL definition. At query time, Spark evaluates the user’s identity and group membership, and conditionally returns or redacts data. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

Dynamic views are managed entirely through standard SQL DDL commands (e.g., `CREATE VIEW`) and are enforced whenever the view is queried. They rely on two key functions provided by Databricks: `current_user()` and `is_member()`. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Dynamic View Functions

Databricks includes two user functions designed for dynamic view logic in the Hive [Metastore](/concepts/metastore.md): ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

- **`current_user()`**: Returns the current user’s name. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]
- **`is_member()`**: Returns `true` if the current user is a member of a specified workspace-level Databricks group. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

These functions can be used together in a `CASE` expression or `WHERE` clause to tailor the output of a view based on the querying user’s group membership.

## Column-Level Permissions

Column-level permissions restrict which columns a user or group can see. For example, a view can redact sensitive columns such as email addresses for users who are not members of the `auditors` group: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
-- Column-level redaction: only auditors see full emails
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  CASE WHEN is_group_member('auditors') THEN email ELSE 'REDACTED' END AS email,
  country,
  product,
  total
FROM sales_raw;
```

In this example, Spark replaces the `CASE` statement with either the literal `'REDACTED'` or the actual column value at analysis time, preserving query performance. The alias `END AS email` prevents the permission logic from appearing as the column name in results. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Row-Level Permissions

Row-level permissions restrict which rows a user can access. For instance, only members of the `managers` group may see transactions with amounts over $1,000,000: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
-- Row-level filter: managers see all rows; others see only rows with total <= 1,000,000
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  country,
  product,
  total
FROM sales_raw
WHERE
  CASE WHEN is_group_member('managers') THEN TRUE ELSE total <= 1000000 END;
```

This technique prevents non‑manager users from even knowing that high‑value transactions exist, because the rows are omitted entirely from the result set. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Data Masking

Beyond simple redaction or filtering, dynamic views can perform advanced data masking using arbitrary SQL expressions. For example, instead of showing the full email address, analysts who are not in the `auditors` group can still see the domain portion for aggregation: ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

```sql
-- Domain-level masking: auditors see full email; others see only the domain
CREATE VIEW sales_redacted AS
SELECT
  user_id,
  region,
  CASE
    WHEN is_group_member('auditors') THEN email
    ELSE regexp_extract(email, '^.*@(.*), 1)
  END
FROM sales_raw;
```

This leverages Spark SQL’s full expression power, enabling use cases such as partial‑string masking, hashing, or conditional aggregation while still protecting sensitive data. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Requirements

To use dynamic views, the workspace must have [table access control](/concepts/table-access-control-tacl.md) enabled, and the cluster or SQL warehouse must be configured to enforce those controls. Without table access control, the permission logic inside the view will not be applied. ^[hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy data catalog that stores these views.
- [Table access control](/concepts/table-access-control-tacl.md) — The overarching permission framework that enforces dynamic views.
- GRANT, REVOKE, DENY — SQL commands for managing Hive [Metastore](/concepts/metastore.md) privileges.
- current_user — The function returning the current user name.
- is_member — The function checking group membership.
- Data masking — Broader concept of obfuscating sensitive data.
- [Unity Catalog](/concepts/unity-catalog.md) — Unity Catalog’s equivalent privilege model with its own dynamic view capabilities.

## Sources

- hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md

# Citations

1. hive-metastore-privileges-and-privileges-and-securable-objects-legacy-databricks-on-aws.md
2. [hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws.md](/references/hive-metastore-privileges-and-securable-objects-legacy-databricks-on-aws-f9aea977.md)
