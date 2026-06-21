---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b274a5bdcb0c074994afd0ff5d326faaa9443af8525f3010e5d0129225ee409
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-trace-migration
    - ITM
    - Idempotent Migration
    - Idempotent Operations
    - Idempotent operations
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: Idempotent Trace Migration
description: A migration mechanism that automatically resumes from where it left off if interrupted, skipping already-migrated rows so the same command can be safely rerun.
tags:
  - mlflow
  - migration
  - resilience
timestamp: "2026-06-19T19:33:15.343Z"
---

# Idempotent Trace Migration

**Idempotent Trace Migration** is a property of the trace migration utility that moves [Trace|traces](/concepts/traces.md) from an [MLflow experiments|MLflow experiment](/concepts/mlflow-experiment.md) to [Unity Catalog](/concepts/unity-catalog.md) Delta tables. The operation is designed to be safe to run multiple times without duplicating data or causing side effects, even if the migration is interrupted mid-execution. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Overview

The migration copies traces, spans, assessments, tags, and metadata from the source experiment to a set of four Unity Catalog Delta tables: `_otel_spans`, `_otel_annotations`, `_otel_logs`, and `_otel_metrics` (with a user‑defined table prefix). The source experiment is never modified during the process. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Key Properties

### Idempotency

If the migration is interrupted — for example, because of a cluster timeout — the user can safely rerun the exact same migration command. The operation automatically resumes from where it left off. Already‑migrated rows are skipped, so no duplicate traces are created in the destination tables. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Resumability

The migration internally tracks which rows have already been transferred. On re‑execution, it only processes traces that were not yet migrated, making the operation efficient and reliable for large datasets. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Scope

The migration copies all traces, spans, assessments, tags, and metadata present in the source experiment at the time of migration. Archived or deleted traces, dataset records, labeling sessions, runs, and non‑trace entities are not migrated. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Optional Time Filter

To migrate only traces created after a specific point in time, the `start_time_ms` parameter (epoch milliseconds in UTC) can be passed. The migration then ingests only those traces whose request time is at or after the specified timestamp. Already‑migrated traces are skipped regardless. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

```python
from databricks.migrations.migrate_traces_to_uc import run
import time

one_week_ago_ms = int((time.time() - 7 * 24 * 60 * 60) * 1000)
run(
    source_experiment_id="<source_experiment_id>",
    target_experiment_id="<destination_experiment_id>",
    start_time_ms=one_week_ago_ms,
)
```

## Benefits of Idempotent Migration

- **Fault tolerance**: No data loss or duplication if the job is restarted.
- **No‑risk retries**: Operators can re‑run the migration without needing to manually clean up partial results.
- **Incremental migration**: With the `start_time_ms` parameter, the same command can be used to continuously migrate new traces in a rolling fashion.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where migrated traces are stored.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit containing the source traces.
- [Trace](/concepts/traces.md) – The primary entity being migrated.
- Trace Location – The Unity Catalog path that backs the destination experiment.
- [Idempotent operations](/concepts/idempotent-trace-migration.md) – The general software design principle behind this behavior.

## Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
