---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc6c15e510c2a01448a47fe618d4b34c7506883128e276cd70ba1db463332f32
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sqlstate-0akdc
    - DS0
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: Databricks SQLSTATE 0AKDC
description: A SQLSTATE code in Databricks indicating a 'feature not supported' condition, associated with the DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class.
tags:
  - databricks
  - error-messages
  - sqlstate
timestamp: "2026-06-18T11:50:45.978Z"
---

---
title: Databricks SQLSTATE 0AKDC
summary: A SQLSTATE code indicating a feature not supported error in Databricks, specifically for `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` when the source table is not Delta or has been time-traveled by timestamp.
sources:
  - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - error
  - sqlstate
  - delta-lake
aliases:
  - sqlstate-0akdc
  - 0AKDC
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks SQLSTATE 0AKDC

**SQLSTATE 0AKDC** is a feature-not-supported error code in Databricks. It is raised by the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class when an attempt is made to clone a [Delta table](/concepts/delta-lake-table.md) with its history from a source that cannot provide the required change data. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

SQLSTATE 0A belongs to the **class 0A – Feature Not Supported** category. Within that class, `0AKDC` is a vendor-specific condition code defined by Databricks.

## Error Condition: `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`

The full error class is `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`. It can be triggered in two sub-conditions: ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### `NON_DELTA`

The source table is in a format other than Delta (for example, Parquet, CSV, or JSON). Only a [Delta Lake](/concepts/delta-lake.md) source table can be cloned with history, because history requires the Delta transaction log. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

> **Error message:** `Source table of <format> format is not supported.`

### `TIME_TRAVELLED_BY_TIMESTAMP`

The source table was accessed using a timestamp-based time travel query (e.g., `TIMESTAMP AS OF`). Cloning with history from a timestamp-based snapshot is not supported. To clone with history, use a [Delta Lake version](/concepts/delta-table-versioning.md) number instead. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

> **Error message:** `Source table time travelled by timestamp is not supported.`

## Resolution

To avoid this error, ensure that:

- The source table is a Delta table (not an external format).
- If using time travel, specify the version number (with `VERSION AS OF`) rather than a timestamp.

## Related Concepts

- SQLSTATE classes in Databricks — Overview of all SQLSTATE error classifications
- [Delta Clone](/concepts/delta-clone.md) — The `CLONE` operation that creates a copy of a Delta table
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) — Accessing historical data by version or timestamp
- [Delta Clone with History](/concepts/delta-clone-with-history.md) — The specific operation that requires a Delta source

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
