---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7eeb27ce069123de22528fdc06dee3f2cb310d3bd718bea86ae902793e9632a
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - featurespec
    - Feature Spec
    - Feature Specs
    - FeatureSpecs
    - feature spec
    - feature specs
    - features
    - Feature Spec (FeatureSpec)
    - Feature Types
    - Feature objects
    - Look up features
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: feature-serving-endpoints-databricks-on-aws.md
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: FeatureSpec
description: A Unity Catalog entity that bundles FeatureLookups and FeatureFunctions into a reusable logical unit for model training and Feature Serving endpoints.
tags:
  - feature-store
  - unity-catalog
  - serving
timestamp: "2026-06-19T18:12:13.189Z"
---

# FeatureSpec

A **`FeatureSpec`** is a [Unity Catalog](/concepts/unity-catalog.md) entity that defines a reusable set of features and functions for serving. `FeatureSpec`s combine [FeatureLookup](/concepts/featurelookup.md) objects from feature tables and [FeatureFunction](/concepts/featurefunction.md) objects into a single logical unit that can be used for model training or for serving via Feature Serving endpoints. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

`FeatureSpec`s are stored and managed by Unity Catalog, with full lineage tracking to their constituent offline feature tables and functions. This enables governance, discoverability, and reuse across different models and applications. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

A `FeatureSpec` always references the offline feature tables, but those tables must be published to an online store for real-time serving scenarios. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

`FeatureSpec`s appear in Catalog Explorer and are treated as first-class Unity Catalog objects. ^[feature-serving-endpoints-databricks-on-aws.md]

## Composition

A `FeatureSpec` is composed of a list of `FeatureLookup` objects and `FeatureFunction` objects. You define these using the `databricks-feature-engineering` Python package. ^[feature-serving-endpoints-databricks-on-aws.md]

- **`FeatureLookup`**: Specifies a feature table to look up and the lookup key to use. It can also include a list of `feature_names` to select specific columns, and may specify `default_values` for missing keys. ^[feature-serving-endpoints-databricks-on-aws.md]
- **`FeatureFunction`**: References a user-defined function (UDF) in Unity Catalog that computes a feature value on demand. The function can be bound to inputs from other features or from the request payload. ^[feature-serving-endpoints-databricks-on-aws.md]

## Creating a FeatureSpec

Use `FeatureEngineeringClient.create_feature_spec()` to create the `FeatureSpec`. The `name` parameter specifies the fully qualified name in Unity Catalog using the three-level namespace (`catalog.schema.name`). ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.feature_engineering import (
    FeatureFunction,
    FeatureLookup,
    FeatureEngineeringClient,
)

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name="main.default.customer_profile",
        lookup_key="user_id",
        feature_names=["average_yearly_spend", "country"],
    ),
    FeatureFunction(
        udf_name="main.default.difference",
        output_name="spending_gap",
        input_bindings={"num_1": "ytd_spend", "num_2": "average_yearly_spend"},
    ),
]

fe.create_feature_spec(
    name="main.default.customer_features",
    features=features,
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

### Specifying default values

To specify default values for features, use the `default_values` parameter in the `FeatureLookup`. If the feature columns are renamed using the `rename_outputs` parameter, `default_values` must use the renamed feature names. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
FeatureLookup(
    table_name="ml.recommender_system.customer_features",
    feature_names=["membership_tier", "age", "page_views_count_30days"],
    lookup_key="customer_id",
    default_values={
        "age": 18,
        "membership_tier": "bronze",
    },
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

## Using a FeatureSpec

### In model training

You can use a `FeatureSpec` in model training by referencing it in `create_training_set`. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### For serving

You can create a Feature Serving endpoint using the `FeatureSpec` as the entity name. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

workspace = WorkspaceClient()

workspace.serving_endpoints.create(
    name="my-serving-endpoint",
    config=EndpointCoreConfigInput(
        served_entities=[
            ServedEntityInput(
                entity_name="main.default.customer_features",
                scale_to_zero_enabled=True,
                workload_size="Small",
            )
        ]
    ),
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

### Querying

When you query the endpoint, you provide the primary key and any context data that functions require. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")
response = client.predict(
    endpoint="my-serving-endpoint",
    inputs={
        "dataframe_records": [
            {"user_id": 1, "ytd_spend": 598},
            {"user_id": 2, "ytd_spend": 280},
        ]
    },
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for machine learning features
- Feature Serving — Low-latency serving of features from Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that stores and manages FeatureSpecs
- [FeatureLookup](/concepts/featurelookup.md) — Object that specifies feature table lookups
- [FeatureFunction](/concepts/featurefunction.md) — Object that wraps UDFs for on-demand feature computation
- [Online Feature Store](/concepts/online-feature-store.md) — Required for real-time serving of FeatureSpec features
- [Model Serving](/concepts/model-serving.md) — Serving MLflow models that use FeatureSpec features

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- feature-serving-endpoints-databricks-on-aws.md
- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
3. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
