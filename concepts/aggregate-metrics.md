---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6aa401ffcbe9ef494c6794aa925a91fce987926271ab44c367bffb41b3d67cda
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
    - use-custom-metrics-with-data-profiling-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - aggregate-metrics
    - aggregate
    - aggregate-metrics-in-mlflow-evaluation
    - AMIME
    - aggregate-metrics-mlflow-evaluation
    - AM(E
  citations:
    - file: use-custom-metrics-with-data-profiling-databricks-on-aws.md
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Aggregate Metrics
description: Summary statistics computed across all evaluated examples in an evaluation run, such as mean correctness or safety pass rate.
tags:
  - mlflow
  - metrics
  - statistics
timestamp: "2026-06-19T18:43:41.978Z"
---

# Aggregate Metrics

**Aggregate metrics** are summary statistics computed over a dataset that capture overall behavior, quality, or performance. In data profiling, they are calculated directly from the columns of the primary table and stored in the [Profile Metrics Table](/concepts/profile-metrics-table.md). In [MLflow](/concepts/mlflow.md) evaluation runs, they summarize quality assessments across all evaluated examples and are stored as part of the evaluation run structure. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md] ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Aggregate Metrics in Data Profiling

In the context of [Data Profiling](/concepts/data-profiling.md), aggregate metrics are one of three types of custom metrics you can define (alongside derived metrics and drift metrics). They are computed from columns in the primary table using a SQL expression defined as a Jinja template. The resulting value is stored as a new column in the profile metrics table and appears in the analysis rows for the columns to which it applies. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

### Characteristics

- Computation accesses the primary table data directly.
- The `definition` must be a single SQL expression (no joins or subqueries).
- The `input_columns` parameter specifies which columns the metric uses; use `[":table"]` when the metric depends on multiple columns.
- The `output_data_type` defines the schema of the result (e.g., `DoubleType()`).

### Examples

| Metric Name | Definition | Input Columns |
|-------------|-----------|---------------|
| `squared_avg` | `avg(\`{{input_column}}\` * \`{{input_column}}\`)` | `["f1", "f2"]` |
| `avg_diff_f1_f2` | `avg(f1 - f2)` | `[":table"]` |
| `weighted_error` | `avg(CASE WHEN {{prediction_col}} = {{label_col}} THEN 0 WHEN {{prediction_col}} != {{label_col}} AND critical=TRUE THEN 2 ELSE 1 END)` | `[":table"]` |

The `weighted_error` example uses a weighted penalty when the `critical` column is `True`, demonstrating how aggregate metrics can capture business logic or custom model quality scores. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

## Aggregate Metrics in MLflow Evaluation Runs

An [Evaluation Run](/concepts/evaluation-run.md) in MLflow automatically computes aggregate metrics that summarize the quality scores from [scorers (MLflow)|scorers](/concepts/mlflow-scorers.md) across all traces in the run. These metrics appear under **Aggregate Metrics** in the evaluation run structure. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

### Examples

Common aggregate metrics generated during an evaluation run include:

- `correctness_mean`: average correctness score across all inputs
- `relevance_mean`: average relevance score
- `safety_pass_rate`: fraction of inputs that passed a safety scorer

Each aggregate metric is computed from the per-trace feedback values produced by the scorers. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Relationship to Other Metric Types

Aggregate metrics serve as the foundational computation that enables more advanced metric types:

- Derived Metrics – Calculated from previously computed aggregate metrics without accessing the primary table again. For example, `root_mean_square` can be derived from the `squared_avg` aggregate metric. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]
- [Drift Metrics](/concepts/drift-metrics.md) – Compare aggregate or derived metrics between two time windows (current vs. baseline or previous window) to track distribution changes over time. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

Using derived and drift metrics instead of recomputing against the full primary table reduces computational overhead. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

## Storage

- In data profiling, aggregate metrics are stored in the **Profile Metrics Table**, alongside automatic analysis statistics. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]
- In MLflow, aggregate metrics are stored as part of the evaluation run’s metrics, accessible via the run’s MLflow tracking API. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Related Concepts

- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- [Custom Metrics (Data Profiling)](/concepts/custom-metrics-in-data-profiling.md)
- Derived Metrics
- [Drift Metrics](/concepts/drift-metrics.md)
- [Evaluation Run](/concepts/evaluation-run.md)
- [Scorers (MLflow)](/concepts/scorers-mlflow-genai.md)
- [Data Profiling](/concepts/data-profiling.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)

## Sources

- use-custom-metrics-with-data-profiling-databricks-on-aws.md
- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [use-custom-metrics-with-data-profiling-databricks-on-aws.md](/references/use-custom-metrics-with-data-profiling-databricks-on-aws-8de965f1.md)
2. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
