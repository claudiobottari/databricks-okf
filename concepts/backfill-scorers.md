---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40fd5c15c9e1603865f9ad2db0dc5d572f96f665a767cf28bd8c8f42c3184eeb
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - backfill-scorers
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Backfill Scorers
description: Technique to retrospectively apply evaluation scorers to historical MLflow experiment traces within a specified date range.
tags:
  - mlflow
  - evaluation
  - databricks
  - monitoring
timestamp: "2026-06-19T22:12:25.900Z"
---

```yaml
---
title: Backfill Scorers
summary: A Databricks technique to retroactively apply MLflow GenAI scorers to historical trace data over a specified time range.
sources:
  - backfill-historical-traces-with-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:07:56.242Z"
updatedAt: "2026-06-19T17:39:43.250Z"
tags:
  - databricks
  - mlflow
  - scoring
  - evaluation
  - monitoring
aliases:
  - backfill-scorers
  - backfill historical traces
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Backfill Scorers

**Backfill Scorers** is a feature in the `databricks.agents.scorers` module that allows you to apply [[scorers]] to historical traces (past agent invocations) within a defined time window. This enables retroactive scoring of previously collected data, for example to populate a monitoring dashboard with historical scores or to compute metrics on past runs without re‑running the agent. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Function and Parameters

The main entry point is the `backfill_scorers` function. It accepts an MLflow experiment ID, a list of `BackfillScorerConfig` objects, a start time, and an end time. Each `BackfillScorerConfig` pairs a registered scorer with a sample rate (a float between 0.0 and 1.0) that applies specifically to this backfill operation, independent of the scoring rate used during ongoing monitoring. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

The function returns a job ID that you can use to track the asynchronous backfill operation.

## Use Case

Once a scorer is registered and started, it begins scoring new traces as they arrive. However, traces generated before the scorer was started remain unscored. Backfill Scorers fills this gap by running one or more scorers on traces that fall between `start_time` and `end_time`. Each scorer can be assigned a custom sample rate during backfill, which may differ from the rate used for ongoing scoring. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Related Concepts

- [[Scorers]] – Components that evaluate MLflow traces for quality, safety, or custom metrics.
- [[MLflow experiment]] – The organizational unit for MLflow runs and traces.
- [[Production monitoring]] – Ongoing scoring workflows that can be supplemented by backfill operations.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md
```

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
