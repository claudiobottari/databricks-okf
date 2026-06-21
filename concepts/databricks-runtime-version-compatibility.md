---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2762891953b2e4eeb63b164b3f372645eb80755436139e0efd0214363ea47ec
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-version-compatibility
    - DRVC
    - Databricks Runtime Versioning
    - Databricks Runtime version supported by Spark NLP
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: Databricks Runtime Version Compatibility
description: Annotations (DBR tags) indicating which Databricks Runtime ML version introduced each parameter, helping users determine feature availability.
tags:
  - Databricks
  - versioning
  - compatibility
timestamp: "2026-06-19T14:07:55.158Z"
---

# Databricks Runtime Version Compatibility

**Databricks Runtime Version Compatibility** — in the context of the AutoML Python API — describes which parameters are available in each [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (DBR ML) version. The AutoML methods `classify()`, `regress()`, and `forecast()` each support a set of parameters that were introduced or deprecated at specific runtime versions. ^[automl-python-api-reference-databricks-on-aws.md]

## General Version Notes

- The `max_trials` parameter is **deprecated** in Databricks Runtime 10.4 ML and is **not supported** in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control run duration instead. ^[automl-python-api-reference-databricks-on-aws.md]  
- Parameters annotated with `# :re[DBR] X.Y ML and above` are only available in Databricks Runtime X.Y ML or a later release. ^[automl-python-api-reference-databricks-on-aws.md]

## Parameter Availability by Runtime Version

The table below lists key parameters and the minimum Databricks Runtime version in which they are supported.

| Parameter | Minimum DBR Version | Affected Methods |
|-----------|---------------------|------------------|
| `exclude_cols` | 10.3 ML | `classify`, `regress` |
| `exclude_frameworks` | 10.3 ML | `classify`, `regress` |
| `experiment_dir` | 10.4 LTS ML | `classify`, `regress` |
| `imputers` | 10.4 LTS ML | `classify`, `regress` |
| `output_database` | 10.5 ML | `forecast` |
| `feature_store_lookups` | 11.3 LTS ML (classify/regress), 12.2 LTS ML (forecast) | `classify`, `regress`, `forecast` |
| `pos_label` | 11.1 ML | `classify` |
| `experiment_name` | 12.1 ML | `classify`, `regress`, `forecast` |
| `country_code` | 12.0 ML | `forecast` |
| `split_col` | 15.3 ML | `classify`, `regress` |
| `sample_weight_col` | 15.4 ML (classify), 15.3 ML (regress), 16.0 ML (forecast) | `classify`, `regress`, `forecast` |

^[automl-python-api-reference-databricks-on-aws.md] (all table entries derived from parameter annotations in the source)

## Impact on Workloads

When writing AutoML code, you must ensure that the [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) version running your cluster supports the parameters you intend to use. Using a parameter that is not available in your runtime will cause a syntax or runtime error. For example, `split_col` cannot be used with Databricks Runtime 15.2 ML or earlier. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML Python API Reference](/concepts/automl-python-api.md) – Full documentation of the `classify`, `regress`, and `forecast` methods.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The versioned ML environment that controls parameter availability.
- [AutoML Summary](/concepts/automlsummary.md) – The object returned by AutoML runs, which includes trial information.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
