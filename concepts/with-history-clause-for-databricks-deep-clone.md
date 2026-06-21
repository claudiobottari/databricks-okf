---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df3728b812cc045b95a449da4ff1422a38612f6739f2207dc5699bb2002827e5
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - with-history-clause-for-databricks-deep-clone
    - WHCFDDC
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: WITH HISTORY clause for Databricks deep clone
description: When deep cloning a streaming table in Databricks, the WITH HISTORY clause is required; a DEEP CLONE without it will fail with REQUIRES_WITH_HISTORY.
tags:
  - delta-lake
  - sql-syntax
  - databricks
timestamp: "2026-06-18T11:52:58.999Z"
---

# WITH HISTORY clause for Databricks deep clone

The **WITH HISTORY** clause is a required parameter when performing a [Deep Clone](/concepts/deep-clone.md) of a Delta Streaming Table on Databricks. Without this clause, the deep clone operation fails with the `REQUIRES_WITH_HISTORY` error condition.

## Error Condition

When attempting to deep clone a streaming table without the `WITH HISTORY` clause, Databricks returns the SQL state `0A000` with the error message:

```
WITH HISTORY is required. Use CREATE TABLE ... DEEP CLONE ... WITH HISTORY.
```

This is one of several failure modes specific to streaming table deep clones. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Syntax

The correct syntax for deep cloning a streaming table is:

```sql
CREATE TABLE <target_table> DEEP CLONE <source_table> WITH HISTORY
```

The `WITH HISTORY` clause tells Databricks to include the change data feed (CDC) records when creating the clone. This is required because streaming tables rely on the transaction log to track changes and maintain materialized state. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Why WITH HISTORY is Required

Streaming tables use [Delta Lake](/concepts/delta-lake.md) change data feed to track incremental updates. When you deep clone a streaming table, Databricks must:

- Capture the complete change history from the source table
- Store the transaction metadata needed for downstream streaming consumers
- Preserve the [partitioning](/concepts/delta-table-partitioning-mismatch.md) and data layout optimization history

Without `WITH HISTORY`, the cloned table would lose the metadata needed to support streaming reads and incremental processing. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Limitations

The `WITH HISTORY` clause is required only for streaming tables that use the default publishing mode (`OLD_ARCHITECTURE_NOT_SUPPORTED`). Other restrictions that may apply when deep cloning streaming tables include:

- **LOCATION_NOT_SUPPORTED**: Specifying a custom `LOCATION` is not supported. The cloned streaming table uses [managed storage](/concepts/managed-storage-location.md).
- **SCHEDULED_TABLE_NOT_SUPPORTED**: Scheduled streaming tables cannot be deep cloned.
- **TIME_TRAVEL_NOT_SUPPORTED**: [Time travel](/concepts/delta-lake-time-travel.md) queries are not supported for streaming table deep clones. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Best Practices

When deep cloning streaming tables, always include `WITH HISTORY` to ensure:

1. Complete metadata preservation for downstream consumers
2. Full transaction history for debugging and auditing
3. Consistent state for incremental processing workloads

## Sources

- [DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error condition - Databricks on AWS](https://docs.databricks.com/aws/en/error-messages/delta-deep-clone-streaming-table-error-error-class)

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
