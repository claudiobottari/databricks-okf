---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f0235a14362f1042326557e585cdbc5cf1796375b5ea372c86d14bd2ff70290
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-features-limitations-and-constraints
    - Constraints and Declarative Features Limitations
    - DFLAC
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Declarative Features Limitations and Constraints
description: Known limitations of the declarative feature APIs including entity column type restrictions, RequestSource scalar-only support, globally unique column names across sources, and limited UDAF function support.
tags:
  - feature-engineering
  - constraints
  - databricks
timestamp: "2026-06-19T09:57:47.621Z"
---

# Declarative Features Limitations and Constraints

The Declarative Feature Engineering APIs impose several limitations and constraints that users must follow when defining, registering, and serving features. These restrictions cover column naming, data types, supported aggregation functions, request-time data sources, and the required compute environment. Adhering to these rules is necessary to avoid runtime errors and ensure correct feature computation, training set creation, and model serving.^[declarative-features-databricks-on-aws.md]

## Compute and Environment Requirements

The Declarative Feature Engineering APIs require a [classic compute](https://docs.databricks.com/aws/en/compute/use-compute) cluster running Databricks Runtime 17.0 ML or above. In addition, the custom Python package `databricks-feature-engineering` version 0.15.0 or higher must be installed in each notebook session using `%pip install databricks-feature-engineering>=0.15.0` followed by `dbutils.library.restartPython()`.^[declarative-features-databricks-on-aws.md]

## Naming and Column Constraints

### Entity and Timeseries Column Name Matching

When using `create_training_set`, the names of the entity columns and timeseries columns in the training (labeled) dataset must exactly match the corresponding column names used in the feature definitions. A mismatch causes an error during training set construction.^[declarative-features-databricks-on-aws.md]

### Label Column Exclusion

The column name used as the `label` in the training dataset must not exist in any source table used to define the features. If a source table contains a column with the same name as the label, the API raises a conflict error.^[declarative-features-databricks-on-aws.md]

### Global Uniqueness of Column Names

Across all sources in a training set or serving endpoint, the following sets of column names must be globally unique:

- Entity column names
- Timeseries column names
- Request feature column names

No two sources may share a column name that appears in any of these categories.^[declarative-features-databricks-on-aws.md]

## Data Type Constraints

### Entity Column Type Restriction

Entity columns cannot be of type `DATE` or `TIMESTAMP`. Entity columns must be a supported scalar type other than these two temporal types.^[declarative-features-databricks-on-aws.md]

### Request Source Data Type Restriction

The `RequestSource` data source supports only scalar data types as defined in `ScalarDataType`: `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, and `SHORT`. Complex types such as arrays, maps, and structs are not supported.^[declarative-features-databricks-on-aws.md]

## Function and Transformation Constraints

### Supported Aggregation Functions

The `create_feature` API supports only a limited list of user-defined aggregate functions (UDAFs). For the complete list, refer to the [Supported functions](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-api-reference#supported-functions) documentation. Using an unsupported function results in an error.^[declarative-features-databricks-on-aws.md]

### Request Source Transformation Constraints

`RequestSource` does not support aggregation functions or time-windowed transformations. Only `ColumnSelection` functions can be used with a `RequestSource`. This means that request-time data cannot be aggregated over time or grouped by entity; it can only be passed through as a raw column value.^[declarative-features-databricks-on-aws.md]

## Materialization Limitations

For materialization-specific limitations (e.g., constraints on offline and online store configurations, trigger types, and supported feature types), see the [Materialize declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/materialized-features) documentation. The materialization APIs have additional restrictions not covered on this page.^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) – Overview of the API workflows
- create_training_set – Creating training sets with declarative features
- [RequestSource](/concepts/requestsource.md) – Request-time data source for online features
- [DeltaTableSource](/concepts/deltatablesource.md) – Primary feature data source
- [ColumnSelection](/concepts/automl-column-selection.md) – The only function supported for request sources
- Supported Functions in Declarative Features – List of allowed aggregation functions

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
