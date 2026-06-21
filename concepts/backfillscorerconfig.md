---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6ccaea6d46fc942cb9ca66ea27658d1d15ad8f0ab9659373e6b74a3b7ce6a62
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - backfillscorerconfig
    - Backfill Scorer Config
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
title: BackfillScorerConfig
description: Configuration object used to specify custom sample rates for individual scorers during a backfill operation.
tags:
  - api
  - configuration
  - databricks
timestamp: "2026-06-19T22:12:34.027Z"
---

---

title: BackfillScorerConfig
summary: A configuration object that pairs a scorer with a custom sample rate for backfill operations.
sources:
  - backfill-historical-traces-with-scorers-databricks-on-aws.md
  - scorer-lifecycle-management-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:52:14.956Z"
updatedAt: "2026-06-19T17:39:40.140Z"
tags:
  - databricks
  - configuration
  - scoring
aliases:
  - backfillscorerconfig
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# BackfillScorerConfig

**BackfillScorerConfig** is a configuration class from `databricks.agents.scorers` that pairs a [[Scorers|Scorer]] with a custom `sample_rate` for use with the [BackfillScorers](/concepts/backfillscorers.md) function. It allows overriding the scorer’s default sampling rate for a specific backfill job without changing the scorer’s permanent configuration. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md, scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Constructor

```python
BackfillScorerConfig(scorer=..., sample_rate=...)
```

- **`scorer`**: A [[Scorers|Scorer]] instance (registered and started) to evaluate historical traces.
- **`sample_rate`** (`float`): The fraction of traces to evaluate during the backfill (0.0 to 1.0). If not provided, the function falls back to the scorer’s current sample rate. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md, scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Usage

`BackfillScorerConfig` objects are passed as a list to `backfill_scorers`. Each configuration replaces the scorer’s original [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) for that backfill job only. The `backfill_scorers` function also accepts `experiment_id`, `start_time`, and `end_time` parameters. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Example

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime
from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)

response_length = response_length.register(name="response_length")
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Define custom sample rates for backfill
custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
    BackfillScorerConfig(scorer=response_length, sample_rate=0.9),
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30)
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md, scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Related Concepts

- [BackfillScorers](/concepts/backfillscorers.md)
- [[Scorers|Scorer]]
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md)
- Safety
- [Backfill historical traces](/concepts/historical-trace-backfilling.md)
- [Scorer lifecycle management API reference](/concepts/scorer-lifecycle-management.md)

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md
- scorer-lifecycle-management-api-reference-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
2. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
