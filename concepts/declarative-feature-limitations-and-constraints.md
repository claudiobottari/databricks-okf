---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 856fd7273c7bc47d004fbd82ead77c7905c922b1fbab301d87452ff3ad6bcead
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-feature-limitations-and-constraints
    - Constraints and Declarative Feature Limitations
    - DFLAC
    - Train models with declarative features
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Declarative Feature Limitations and Constraints
description: Key constraints of declarative features including restrictions on entity column types, supported functions, source column uniqueness, and request source capabilities
tags:
  - feature-engineering
  - limitations
  - constraints
timestamp: "2026-06-19T18:18:19.236Z"
---

# Declarative Feature Limitations and Constraints

The **Declarative Feature Limitations and Constraints** document outlines the specific restrictions and unsupported configurations when using the [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) in Databricks. These limitations apply to feature definitions, training sets, serving endpoints, and materialization workflows.

## General Feature Definition Limitations

### Naming and Column Constraints

Entity column names, timeseries column names, and request feature column names must be globally unique across all sources within a single training set or serving endpoint. This means that if you have multiple feature sources, no two columns with the same name are permitted, even if they originate from different source tables. ^[declarative-features-databricks-on-aws.md]

The column name used as the `label` column in the training dataset must not exist in any of the source tables used for defining `Feature` objects. This prevents ambiguity between the label and feature columns during model training. ^[declarative-features-databricks-on-aws.md]

### Data Type Constraints

Entity columns cannot be of type `DATE` or `TIMESTAMP`. This restriction applies to all columns specified in the `entity` parameter when defining features. ^[declarative-features-databricks-on-aws.md]

## `RequestSource` Limitations

[RequestSource](/concepts/requestsource.md) supports only scalar data types defined in `ScalarDataType`. The supported types are: `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, and `SHORT`. Complex types such as arrays, maps, and structs are not supported. ^[declarative-features-databricks-on-aws.md]

`RequestSource` does not support aggregation functions or time windows. Only `ColumnSelection` functions can be used with request-time data sources. This means features defined from request sources can only perform simple column selections without any time-based or aggregation logic. ^[declarative-features-databricks-on-aws.md]

## Training Set Limitations

When using the `create_training_set` API, the names of entity columns and timeseries columns must match exactly between the training (labeled) dataset and the feature definitions. Mismatched column names will cause errors during training set creation. ^[declarative-features-databricks-on-aws.md]

## Function Support Limitations

Only a limited list of functions (UDAFs) is supported in the `create_feature` API. Not all aggregation or transformation functions are available for use with declarative features. Users should consult the supported functions documentation for the complete list of available functions. ^[declarative-features-databricks-on-aws.md]

## Materialization Limitations

For materialization-specific limitations that apply when using `materialize_features` to populate offline or online stores, users should refer to the dedicated materialization limitations documentation. ^[declarative-features-databricks-on-aws.md]

## Best Practices to Avoid Constraint Violations

- Ensure entity and timeseries column names are consistent between training datasets and feature definitions.
- Use unique column names across all sources when combining multiple features in a training set or serving endpoint.
- Avoid using `DATE` or `TIMESTAMP` columns as entity columns.
- For request-time data, restrict feature definitions to `ColumnSelection` functions only.

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) — The core APIs for defining and computing features
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The client used to interact with feature engineering workflows
- [Training Set Creation](/concepts/training-set-feature-store.md) — How training sets are built from features and labeled data
- [Feature Materialization](/concepts/feature-materialization.md) — The process of persisting features for serving
- [RequestSource](/concepts/requestsource.md) — Data source for request-time features

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
