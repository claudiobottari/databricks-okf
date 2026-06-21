---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa5e693ea66501960c23624e25c74baeab4e7bcfd9ebb3694b1e282aaedd259d
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - on-demand-features-limitations
    - OFL
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 97
      end: 97
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 98
      end: 102
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 7
      end: 9
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 14
      end: 16
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 62
      end: 74
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 88
      end: 94
    - file: on-demand-feature-computation-databricks-on-aws.md
      start: 21
      end: 23
title: On-demand features limitations
description: "Constraints on on-demand features: MapType and ArrayType output types are unsupported, and older library versions require extra Unity Catalog permissions."
tags:
  - limitations
  - feature-store
  - databricks
timestamp: "2026-06-19T19:49:46.824Z"
---

# On-demand features limitations

On-demand features in Databricks allow computing feature values at inference time using Python user-defined functions (UDFs) governed by Unity Catalog. While they provide flexibility for request-time computations, several limitations apply regarding data types, dependencies, permissions, and runtime requirements.

## Supported data types

On-demand features can output all data types supported by Feature Store **except** `MapType` and `ArrayType`. This restriction affects the shape of feature values that a UDF can return. ^[on-demand-feature-computation-databricks-on-aws.md#L97]

## Unity Catalog permissions (older SDK versions)

For the `databricks-feature-engineering` library versions **below 0.14.0**, additional Unity Catalog privileges are required to use a UDF when creating a training set or a Feature Serving endpoint:

- `USE CATALOG` privilege on the `system` catalog.
- `USE SCHEMA` privilege on the `system.information_schema` schema.

These permissions are not needed in newer versions of the library. ^[on-demand-feature-computation-databricks-on-aws.md#L98-L102]

## Runtime and workspace prerequisites

To use on-demand features at all, the workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) and must run **Databricks Runtime 13.3 LTS ML or above**. Older runtimes or workspaces without Unity Catalog cannot use on-demand features. ^[on-demand-feature-computation-databricks-on-aws.md#L7-L9]

## UDF registration and three-level namespace

A Python UDF used as an on-demand feature must be registered in Unity Catalog, meaning it is identified by a three-level namespace (`catalog.schema.function_name`). It cannot be a local or ad-hoc function. ^[on-demand-feature-computation-databricks-on-aws.md#L14-L16]

## Handling missing feature values

When a Python UDF depends on the result of a [FeatureLookup](/concepts/featurelookup.md) and the lookup key is not found, the value returned differs by serving method:

- **Batch scoring** (`score_batch`): returns `None`.
- **Online serving** (Model Serving): returns `float("nan")`.

This inconsistency must be handled explicitly in the UDF logic, as shown in the source material’s example using `np.isnan`. ^[on-demand-feature-computation-databricks-on-aws.md#L62-L74]

## Packaging of UDF dependencies

When logging a model that uses an on-demand feature, any Python packages imported by the UDF must be declared via the `extra_pip_requirements` argument of `fe.log_model`. If not specified, the serving environment may lack required packages, causing inference failures. ^[on-demand-feature-computation-databricks-on-aws.md#L88-L94]

## Model serving requirement

Models that use on-demand features must be logged using the Feature Store method `fe.log_model` (now part of `databricks-feature-engineering`). This ensures that the model automatically evaluates the on-demand UDF during inference. Using `mlflow.log_model` directly will not include the feature metadata required for automatic on-demand computation. ^[on-demand-feature-computation-databricks-on-aws.md#L21-L23]

## Related concepts

- On-demand feature computation
- Feature Store supported data types
- [FeatureFunction](/concepts/featurefunction.md)
- [FeatureLookup](/concepts/featurelookup.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [databricks-feature-engineering](/concepts/databricks-feature-engineering-client.md)

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md:97-97](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
2. [on-demand-feature-computation-databricks-on-aws.md:98-102](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
3. [on-demand-feature-computation-databricks-on-aws.md:7-9](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
4. [on-demand-feature-computation-databricks-on-aws.md:14-16](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
5. [on-demand-feature-computation-databricks-on-aws.md:62-74](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
6. [on-demand-feature-computation-databricks-on-aws.md:88-94](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
7. [on-demand-feature-computation-databricks-on-aws.md:21-23](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
