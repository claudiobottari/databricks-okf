---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 482c77670181fca7316e5936e65df15267afa4b43fe7bec2c7ac9004a0090100
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompat-version-mutual-exclusivity
    - IVME
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: IcebergCompat Version Mutual Exclusivity
description: Only one version of IcebergCompat can be enabled on a Delta table at a time; other versions must be explicitly disabled before enabling a new one.
tags:
  - delta-lake
  - apache-iceberg
  - versioning
timestamp: "2026-06-18T11:54:16.626Z"
---

# IcebergCompat Version Mutual Exclusivity

**IcebergCompat Version Mutual Exclusivity** is a constraint enforced by Databricks that prevents multiple versions of the IcebergCompat table feature from being enabled simultaneously on a single Delta table. At most one IcebergCompat version (e.g., V1, V2) can be active at any time. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Condition

When a user attempts to enable or upgrade to a new IcebergCompat version without first disabling any currently active version, the system raises the following error:

```
DELTA_ICEBERG_COMPAT_VIOLATION.VERSION_MUTUAL_EXCLUSIVE:
Only one IcebergCompat version can be enabled, please explicitly disable all other IcebergCompat versions that are not needed.
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Cause

IcebergCompat versions provide Apache Iceberg compatibility for Delta tables, but the underlying metadata representation and table features are version-specific. Enabling a second version while another remains active creates a conflict in the table's feature set. Databricks enforces mutual exclusivity to maintain a consistent, predictable Iceberg compatibility layer. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve a `VERSION_MUTUAL_EXCLUSIVE` error, you must explicitly disable all other IcebergCompat versions before enabling the desired version.

### Steps

1. Identify which IcebergCompat versions are currently enabled on the table. You can inspect table properties using `DESCRIBE EXTENDED <table_name>` and looking for properties like `delta.enableIcebergCompatV1` or `delta.enableIcebergCompatV2`.
2. Disable any conflicting version by setting the corresponding table property to `false`:
   ```sql
   ALTER TABLE <table_name> SET TBLPROPERTIES (
     'delta.enableIcebergCompatV1' = 'false'
   );
   ```
3. Enable the desired version using `REORG TABLE APPLY (UPGRADE UNIFORM (...))` or by setting the appropriate table property.
4. Verify that no version conflict errors remain. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Related Error: CHANGE_VERSION_NEED_REWRITE

If you are upgrading to a newer IcebergCompat version (e.g., from V1 to V2), you may encounter a different sub-error:
```
CHANGE_VERSION_NEED_REWRITE: Changing to IcebergCompatV<newVersion> requires rewriting the table.
```
In this case, run:
```sql
REORG TABLE <table_name> APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```
This command handles both the data rewrite and the version upgrade, ensuring only the new version remains active. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Best Practices

- **Check current version before upgrading.** Always inspect table properties to determine which IcebergCompat version (if any) is currently active.
- **Use `REORG` for version upgrades.** When moving from one IcebergCompat version to another, use `REORG TABLE APPLY (UPGRADE UNIFORM ...)` rather than manually toggling properties. This ensures data is rewritten to be compatible with the new version.
- **Do not enable multiple versions.** The constraint is enforced server-side, so attempting to bypass it will result in the `VERSION_MUTUAL_EXCLUSIVE` error.
- **Document version migrations.** Keep a record of which version is intended for each table and when upgrades occur to avoid confusion during troubleshooting. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- IcebergCompat — The table feature providing Apache Iceberg compatibility for Delta Lake
- [Uniform](/concepts/delta-uniform.md) — The Databricks feature for Apache Iceberg/Delta Lake interoperability
- [REORG TABLE](/concepts/reorg-table.md) — The command used to rewrite table data and enable/upgrade Uniform
- Delta Lake Table Features — The feature system that governs table capabilities
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION — The broader error class containing this and related sub-errors

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
