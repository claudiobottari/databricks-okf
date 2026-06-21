---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33e8cefc18d948e864f672db31775823814dd9e01ce08d03b8eb86bdd0fa55f8
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv-managed-table-requirement
    - IMR
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: IcebergCompatV managed-table requirement
description: The IcebergCompatV feature can only be enabled on managed tables in Databricks, not on external/unmanaged tables.
tags:
  - delta-lake
  - iceberg
  - managed-tables
  - databricks
timestamp: "2026-06-19T18:25:35.591Z"
---

# IcebergCompatV managed-table requirement

The **IcebergCompatV managed-table requirement** is a validation condition enforced by the DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION error class. It states that the feature can be enabled only on [Managed Tables|managed table](/concepts/managed-tables-in-databricks.md) on Databricks. If you attempt to enable IcebergCompatV on an external (unmanaged) table, the operation will fail with the `REQUIRE_MANAGED_TABLE` sub-error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Condition

The error message associated with this requirement is:

> REQUIRE_MANAGED_TABLE  
> The feature can be enabled only on Managed Tables.

This condition is raised when either `ALTER TABLE SET TBLPROPERTIES` or a `REORG TABLE APPLY (UPGRADE UNIFORM ...)` command is executed on a table that is not a managed table. The validation is part of the broader IcebergCompatV compatibility checks that ensure the table meets all prerequisites for Uniform Apache Iceberg integration. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Implications

To use IcebergCompatV, you must first ensure the target table is a managed table. If your table is currently external (unmanaged), you must migrate it to a managed table before enabling the IcebergCompatV table property. The Databricks documentation does not provide an automatic conversion path within the error itself; the user is expected to understand the difference between managed and external tables and manage the migration separately. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Delta tables whose data and metadata are managed by Databricks.
- External Tables – Tables whose data resides in an external location not managed by Databricks.
- [IcebergCompatV](/concepts/icebergcompatv.md) – The table feature that ensures Delta tables are compatible with Apache Iceberg readers.
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The Databricks feature that provides Iceberg read compatibility.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION – The error class that groups all IcebergCompatV validation failures.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
