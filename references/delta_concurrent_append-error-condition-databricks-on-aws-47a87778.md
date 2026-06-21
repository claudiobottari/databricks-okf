---
title: DELTA_CONCURRENT_APPEND error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-concurrent-append-error-class
ingestedAt: "2026-06-18T08:07:12.158Z"
---

[SQLSTATE: 2D521](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-2d-invalid-transaction-termination)

Transaction conflict detected. A concurrent `<operation>` added data to table `<tableName>` committed at version `<version>`.

## ALLOTTED\_TIME\_EXCEEDED[​](#allotted_time_exceeded "Direct link to ALLOTTED_TIME_EXCEEDED")

Row-level conflict resolution exceeded the allotted time. Please retry the operation. Refer to `<docLink>` for more information.

## CHANGE\_TYPE\_COLUMN[​](#change_type_column "Direct link to CHANGE_TYPE_COLUMN")

The table contains a column named '\_change\_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column. Refer to `<docLink>` for more information.

The concurrent operation changed the table metadata (for example, schema or partitioning). Please retry the operation. Refer to `<docLink>` for more information.

## PARTITIONED\_TABLE\_WITHOUT\_MERGE\_SOURCE[​](#partitioned_table_without_merge_source "Direct link to PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE")

Row-level conflict detection could not be performed on this partitioned table. Please retry the operation. Refer to `<docLink>` for more information.

## PREDICATES\_NEED\_REWRITE[​](#predicates_need_rewrite "Direct link to PREDICATES_NEED_REWRITE")

The filter predicates used by this transaction could not be applied for row-level conflict detection. Please retry the operation. Refer to `<docLink>` for more information.

## PROTOCOL\_CHANGE[​](#protocol_change "Direct link to PROTOCOL_CHANGE")

The concurrent operation upgraded the table protocol. Please retry the operation. Refer to `<docLink>` for more information.

## ROW\_LEVEL\_CHANGES[​](#row_level_changes "Direct link to ROW_LEVEL_CHANGES")

The concurrent operation modified the same rows that this transaction attempted to modify. Please retry the operation. Refer to `<docLink>` for more information.

## WHOLE\_TABLE\_READ[​](#whole_table_read "Direct link to WHOLE_TABLE_READ")

This transaction attempted to read the entire table, conflicting with the concurrent modification. Consider adding filters to your query to narrow the data scope or retrying the operation. Refer to `<docLink>` for more information.

## WHOLE\_TABLE\_REPLACE[​](#whole_table_replace "Direct link to WHOLE_TABLE_REPLACE")

The concurrent operation replaced all data in the table. Please retry the operation. Refer to `<docLink>` for more information.

## WITHOUT\_HINT[​](#without_hint "Direct link to WITHOUT_HINT")

Please retry the operation. Refer to `<docLink>` for more information.

## WITH\_PARTITION\_HINT[​](#with_partition_hint "Direct link to WITH_PARTITION_HINT")

The concurrent operation modified data in the partition `<partitionValues>` that should have been read by this operation. Please retry the operation. Refer to `<docLink>` for more information.
