---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 798baa33015ffdc94bf6ca3a095099c44119513b39546d35f5af727d07c7c0e4
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filters-in-unity-catalog
    - RFIUC
    - Row filters in Delta
    - row filtering
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 100
      end: 107
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 89
      end: 95
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 166
      end: 185
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 199
      end: 210
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 64
      end: 66
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 59
      end: 63
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
      start: 50
      end: 52
title: Row Filters in Unity Catalog
description: A row-level security feature in Databricks Unity Catalog that uses SQL UDFs to filter rows returned from a table based on user attributes or group membership.
tags:
  - data-governance
  - unity-catalog
  - row-security
timestamp: "2026-06-19T19:30:05.722Z"
---

```markdown
---
title: Row Filters in Unity Catalog
summary: A row filter is a SQL user-defined function (UDF) applied to a table to restrict which rows users or groups can see, based on a condition evaluated at query time.
sources:
  - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
kind: concept
createdAt: "2026-07-20T10:00:00.000Z"
updatedAt: "2026-07-20T10:00:00.000Z"
tags:
  - unity-catalog
  - row-level-security
  - row-filters
aliases:
  - Row filters in Unity Catalog
  - Row-level filters
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Row Filters in Unity Catalog

**Row filters** are a Unity Catalog feature that enable row-level security on tables. A row filter is a User-Defined Function (UDF) — written in SQL or as a SQL wrapper around Python/Scala logic — that is applied to a table to control which rows are returned in query results based on the identity or attributes of the invoking user. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Overview

Row filters operate by evaluating a condition for each row of a table. The filter function accepts zero or more input parameters, each bound to a column of the table. When a user queries the table, the filter runs with definer’s rights (except for functions that check user context, such as `SESSION_USER()` or `IS_ACCOUNT_GROUP_MEMBER()`, which run as the invoker). ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

Each table can have only one row filter. Row filters are persisted across `REPLACE TABLE` operations to prevent accidental loss of access policies. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Prerequisites

- The workspace must be enabled for Unity Catalog.
- The row filter must be a SQL UDF registered in Unity Catalog. If Python or Scala logic is required, you must create a Python or Scala UDF and then wrap it in a SQL UDF; the SQL UDF is what gets applied as the filter.
- To assign a filter to a table, you need the `EXECUTE` privilege on the function, `USE SCHEMA` on the schema, and `USE CATALOG` on the catalog. For new tables, you need `CREATE TABLE`; for existing tables, you must be the table owner or have the `MANAGE` privilege.
- Compute must be a SQL warehouse, shared access mode (Databricks Runtime ≥ 12.2 LTS), or dedicated access mode (≥ 15.4 LTS).

^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Applying a Row Filter

You can apply a row filter using Catalog Explorer or SQL commands.

### Via Catalog Explorer

1. In the workspace, open **Catalog** and browse to the table.
2. On the **Overview** tab, under **Row filter**, click **Add filter**.
3. Select the catalog, schema, and filter function.
4. Map the function parameters to the table columns.
5. Click **Add**.

^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

### Via SQL

The following commands create a filter function and apply it:

```sql
CREATE FUNCTION us_filter(region STRING)
  RETURN IF(IS_ACCOUNT_GROUP_MEMBER('admin'), true, region='US');

CREATE TABLE sales (region STRING, id INT);
ALTER TABLE sales SET ROW FILTER us_filter ON (region);
```

To remove a row filter:

```sql
ALTER TABLE sales DROP ROW FILTER;
```

A filter can also be applied during table creation:

```sql
CREATE TABLE sales (region STRING, id INT)
  WITH ROW FILTER us_filter ON (region);
```

^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:100-107]

## Row Filter Examples

### Simple group-based filter

The `us_filter` example above restricts non‑admin users to rows where `region = 'US'`. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:89-95]

### Mapping table (access-control list)

Mapping tables enable complex hierarchical or user‑specific rules. The filter checks membership against a separate table:

```sql
-- Create a mapping table of valid users
CREATE TABLE valid_users (username string);
INSERT INTO valid_users VALUES ('fred@databricks.com'), ('barney@databricks.com');

-- Create a filter that checks the current user
CREATE FUNCTION row_filter()
  RETURN EXISTS(
    SELECT 1 FROM valid_users v
    WHERE v.username = SESSION_USER()
  );

-- Apply the filter (with no column binding)
ALTER TABLE data_table SET ROW FILTER row_filter ON ();
```

In this example, only users listed in `valid_users` can see any rows. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:166-185]

### Combined condition with mapping table

A filter can combine column conditions with group membership:

```sql
CREATE FUNCTION row_filter_small_values (x INT, y INT, z INT)
  RETURN (x < 5 AND y < 5 AND z < 5)
    OR EXISTS(
      SELECT 1 FROM valid_accounts v
      WHERE IS_ACCOUNT_GROUP_MEMBER(v.account)
    );

ALTER TABLE data_table SET ROW FILTER row_filter_small_values ON (x, y, z);
```

This allows members of groups listed in `valid_accounts` to see all rows, while others see only rows where all three columns are less than 5. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:199-210]

## Important Considerations

- **Parameter types must match column types.** If a column type differs from the UDF parameter type, implicit casting occurs. With ANSI mode disabled, failed casts silently convert to `NULL`, potentially causing incorrect filter results. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:64-66]
- **Row filters are retained on `REPLACE TABLE`.** If the new table no longer has the referenced columns, queries may fail. Update or drop the filter using `ALTER TABLE`. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:59-63]
- On Databricks Runtime 15.4 LTS and above, reading tables with row filters may incur serverless compute charges even when using dedicated access mode. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md:50-52]

## Related Concepts

- [[Column Masks in Unity Catalog]] — Complementary column-level security feature in Unity Catalog.
- [[Unity Catalog]] — The underlying governance platform.
- User-Defined Function (UDF) — Functions used to implement row filter logic.
- [[Attribute-Based Access Control (ABAC)]] — A centralized tag-based alternative for filtering and masking.
- [[Mapping Tables for Access Control|Mapping Tables]] — Auxiliary tables that encode row-level access rules.
- IS_ACCOUNT_GROUP_MEMBER — Function used to check group membership in filter policies.
- [[Lakeflow Spark Declarative Pipelines]] — A tool that supports row filters in streaming and materialized views.

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md
```

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
2. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:100-107](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
3. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:89-95](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
4. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:166-185](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
5. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:199-210](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
6. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:64-66](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
7. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:59-63](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
8. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md:50-52](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
