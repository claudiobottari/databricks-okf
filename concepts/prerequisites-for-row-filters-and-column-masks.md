---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 824cbd24e4039efe4f8c2abfdd0b7d306abf1ba99071b442f4403f7f965d496f
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-row-filters-and-column-masks
    - Column Masks and Prerequisites for Row Filters
    - PFRFACM
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
title: Prerequisites for Row Filters and Column Masks
description: The required privileges (EXECUTE, USE SCHEMA, USE CATALOG), compute resource constraints (SQL warehouse, shared/dedicated access mode versions), and UDF registration requirements for applying row filters and column masks.
tags:
  - unity-catalog
  - prerequisites
  - compute-requirements
timestamp: "2026-06-19T19:30:41.444Z"
---

# Prerequisites for Row Filters and Column Masks

Before you can apply [row filters](/concepts/row-filter-policies.md) or [column masks](/concepts/delta-lake-column-masks.md) to tables in Unity Catalog, you must meet several prerequisites related to the workspace, function definitions, user privileges, compute resources, and data type compatibility. These requirements ensure that the filters and masks are correctly registered and enforced when queries are executed.

## Workspace and Catalog Requirements

Your workspace must be enabled for [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). Additionally, the filter or mask function must be registered as a SQL user-defined function (UDF) in Unity Catalog. If you need to use Python or Scala logic, you must first create a Python or Scala UDF, then create a SQL UDF that calls it. The SQL UDF is what you apply as the row filter or column mask. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Required Privileges

To assign a function that adds a row filter or column mask to a table, you must have the following privileges:

- **`EXECUTE`** on the function.
- **`USE SCHEMA`** on the schema containing the function.
- **`USE CATALOG`** on the parent catalog.

If you are adding filters or masks when **creating a new table**, you must also have the **`CREATE TABLE`** privilege on the schema. If you are adding them to an **existing table**, you must be the table owner or have the **`MANAGE`** privilege on the table. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Compute Requirements

To access a table that has row filters or column masks, your compute resource must meet one of the following conditions:

- A **SQL warehouse**.
- **Standard access mode** (formerly shared access mode) on Databricks Runtime 12.2 LTS or above.
- **Dedicated access mode** (formerly single user access mode) on Databricks Runtime 15.4 LTS or above.

You **cannot** read row filters or column masks using dedicated compute on Databricks Runtime 15.3 or below. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

If you use dedicated access mode on Databricks Runtime 15.4 LTS and above, your workspace must be enabled for serverless compute—the data filtering functionality that supports row filters and column masks runs on serverless compute. You may be charged for serverless compute resources when reading tables that use these policies. Write operations to such tables are supported only on Databricks Runtime 16.3 and above, and must use supported patterns such as `MERGE INTO`. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Data Type Compatibility

UDF parameter types must match the data types of the table columns passed to them. If a column type differs from the UDF parameter type (for example, passing a `STRING` column to an `INT` parameter), the column value is implicitly cast. With ANSI mode disabled, values that cannot be cast are silently converted to `NULL`, which can cause the filter or mask to produce incorrect results without raising an error. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Table Replacement Behavior

When you run `REPLACE TABLE`, any existing row filter is retained regardless of schema changes. Column masks are also retained if the new table includes columns with the same names as those that had masks in the original table. In both cases, the policies are preserved even if they are not explicitly redefined. However, if a retained policy references a column that was removed or changed, subsequent queries might fail. To resolve this, update or drop the policy using `ALTER TABLE`. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Mapping Tables (Alternative Approach)

As an alternative to UDF-based row filters, you can define a mapping table (access‑control list) that encodes which data rows are accessible to certain users or groups. This approach integrates with fact tables through direct joins and is useful for complex security models. However, mapping tables do not replace the core prerequisites above—you still need a Unity Catalog workspace and appropriate privileges to create and query them. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [Row Filters](/concepts/row-filter-policies.md)
- Column Masks
- [Unity Catalog](/concepts/unity-catalog.md)
- User-Defined Functions (UDFs)
- Fine-Grained Access Control

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
