---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c99962bb91fcd0e838e75d10de12baba00f3ede238ffb9feb9ad72536b85d76c
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_missing_partition_specs
    - ICEBERG_MISSING_PARTITION_SPECS
    - ICEBERG_MISSING_PARTITION_SPECS error
    - Partition Specs
    - iceberg_missing_partition_specs-delta-clone-sub-error
    - I(CS
    - iceberg_missing_partition_specs-error-condition
    - IEC
    - iceberg_missing_partition_specs-sub-error
    - ICEBERG_MISSING_PARTITION_SPECS sub-error
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_MISSING_PARTITION_SPECS
description: A subclass of DELTA_CLONE_INCOMPATIBLE_SOURCE error indicating the source Apache Iceberg table lacks partition specifications, making it incompatible for cloning.
tags:
  - databricks
  - iceberg
  - partitioning
  - error-handling
timestamp: "2026-06-19T18:22:21.805Z"
---

# ICEBERG_MISSING_PARTITION_SPECS

**ICEBERG_MISSING_PARTITION_SPECS** is a sub‑condition of the DELTA_CLONE_INCOMPATIBLE_SOURCE error class. It occurs when an attempt is made to clone an Apache Iceberg table that has no partition specs into Delta Lake. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Condition

The full error message reads:

```
Source Apache Iceberg table has no partition specs in table.
```

This condition is raised by the Delta clone command when the source Iceberg table does not define any partition specifications (partition specs). Delta requires a valid partition spec on the source table to support the clone operation. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class for this condition.
- [Delta Clone](/concepts/delta-clone.md) — The operation that triggers this error.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source table format.
- ICEBERG_MISSING_PARTITION_SPECS|Partition Specs — Partition definitions required by Delta for cloning.
- HAS_INDEXES — Another sub‑condition of the same error class, triggered when the source table has indexes.

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
