---
title: Databricks Feature Store | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/
ingestedAt: "2026-06-18T08:10:03.236Z"
---

Databricks Feature Store is a central registry for the features used in your AI and ML models. When you register feature tables and models in Unity Catalog, you get built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing and discovery.

With Databricks, the entire model training workflow takes place on a single platform, including:

*   Data pipelines that ingest raw data, create feature tables, train models, and perform batch inference.
*   Model and feature serving endpoints that are available with a single click and that provide milliseconds of latency.
*   Data and model monitoring.

When you use features from Databricks Feature Store to train models, the model automatically tracks lineage to the features that were used in training. At inference time, the model automatically looks up the latest feature values. Databricks Feature Store also provides on-demand computation of features for real-time applications, handling all feature computation tasks. This eliminates training/serving skew, ensuring that the feature computations used at inference are the same as those used during model training. It also significantly simplifies the client-side code, as all feature lookups and computation are handled by Databricks Feature Store.

note

This page describes Databricks Feature Store for workspaces that are enabled for Unity Catalog. If your workspace is not enabled for Unity Catalog, see [Workspace Feature Store (deprecated)](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/).

## Conceptual overview[​](#conceptual-overview "Direct link to Conceptual overview")

For an overview of how Databricks Feature Store works and a glossary of terms, see [Databricks Feature Store overview and glossary](https://docs.databricks.com/aws/en/machine-learning/feature-store/concepts).

## Develop features[​](#develop-features "Direct link to Develop features")

## Use features in training workflows[​](#use-features-in-training-workflows "Direct link to Use features in training workflows")

## Serve features[​](#serve-features "Direct link to Serve features")

## Feature governance and lineage[​](#feature-governance-and-lineage "Direct link to Feature governance and lineage")

## Tutorials[​](#tutorials "Direct link to Tutorials")

## Requirements[​](#requirements "Direct link to Requirements")

To use Databricks Feature Store, your workspace must be enabled for Unity Catalog. If your workspace is not enabled for Unity Catalog, see [Workspace Feature Store (deprecated)](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/).

## Supported data types[​](#supported-data-types "Direct link to supported-data-types")

Databricks Feature Store and legacy Workspace Feature Store support the following [PySpark data types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html):

*   `IntegerType`
*   `FloatType`
*   `BooleanType`
*   `StringType`
*   `DoubleType`
*   `LongType`
*   `TimestampType`
*   `DateType`
*   `ShortType`
*   `ArrayType`
*   `BinaryType` \[1\]
*   `DecimalType` \[1\]
*   `MapType` \[1\]
*   `StructType` \[2\]

\[1\] `BinaryType`, `DecimalType`, and `MapType` are supported in all versions of Feature Engineering in Unity Catalog and in Workspace Feature Store v0.3.5 or above. \[2\] `StructType` is supported in Feature Engineering v0.6.0 or above.

The data types listed above support feature types that are common in machine learning applications. For example:

*   You can store dense vectors, tensors, and embeddings as `ArrayType`.
*   You can store sparse vectors, tensors, and embeddings as `MapType`.
*   You can store text as `StringType`.

When published to online stores, `ArrayType` and `MapType` features are stored in JSON format.

The Feature Store UI displays metadata on feature data types:

![Complex data types example](https://docs.databricks.com/aws/en/assets/images/complex-data-type-example-18d4e615f2c7e61dffcce1f6358f23c0.png)

## More information[​](#more-information "Direct link to More information")

For more information on best practices, download [The Comprehensive Guide to Feature Stores](https://www.databricks.com/p/ebook/the-comprehensive-guide-to-feature-stores).
