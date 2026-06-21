---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cdfb383d34ebfd8afbf4a0be422fd39c6ca71e973584b07230a7b5063ab72fda
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-function
    - feature-function-udf
    - FF(
    - Feature functions
    - feature functions
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: Feature Function
description: A user-defined scalar function registered in Unity Catalog that computes feature values on-demand at inference time using both stored and context-provided inputs.
tags:
  - feature-engineering
  - on-demand-features
  - udf
timestamp: "2026-06-19T10:25:06.139Z"
---

Here is the wiki page for "Feature Function".

---

## Feature Function

A **Feature Function** is a [Unity Catalog](/concepts/unity-catalog.md) function used in the [Databricks Feature Engineering](/concepts/databricks-feature-engineering-client.md) pipeline to compute on-demand features at the time of inference. Unlike precomputed features stored in a feature table, a feature function executes server-side logic — such as distance calculations, string transformations, or mathematical operations — in response to an online query. It allows features that depend on dynamic, request-time data to be served with low latency. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

### When to Use a Feature Function

Feature functions are useful when a feature value cannot be precomputed and stored because it depends on input that is only known at inference time. For example:

- **Geospatial computation**: Calculating the distance between a fixed destination (from a feature table) and a user whose current location is provided at query time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Real-time personalization**: Computing a user-specific score, rank, or threshold that changes every session.
- **Data transformations**: Applying on-the-fly normalization, encryption, or formatting that should not be performed in batch.

### How It Works

1. **Define the function in Unity Catalog**: The function is created as a SQL or Python UDF, stored in a [Catalog and Schema](/concepts/catalog-and-schema.md). It can accept any number of parameters, including values that come from the feature table and values provided by the caller at inference time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
2. **Create a [FeatureSpec](/concepts/featurespec.md)**: A `FeatureSpec` combines [FeatureLookups](/concepts/featurelookup.md) (which retrieve precomputed features from an online feature store) with `FeatureFunction` objects. The `FeatureFunction` references the Unity Catalog function and specifies `input_bindings` to map the function's parameters to either columns from a feature lookup or context data supplied at query time. It also declares the `output_name` under which the computed result will be returned. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
3. **Deploy a serving endpoint**: The [FeatureSpec](/concepts/featurespec.md) is deployed to a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md). When a request arrives, the endpoint retrieves the precomputed features from the online store, then executes the feature function with the bound inputs to produce the final feature vector. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

### Example

The following example calculates the distance between a destination (whose location is stored in a feature table) and a user (whose location is provided at query time). ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
# Step 1: Define the function in Unity Catalog
function_name = f"{catalog_name}.{schema_name}.distance"

spark.sql(f"""
CREATE OR REPLACE FUNCTION {function_name}(latitude DOUBLE, longitude DOUBLE,
                                             user_latitude DOUBLE, user_longitude DOUBLE)
RETURNS DOUBLE
LANGUAGE PYTHON
AS
$
import math
lat1 = math.radians(latitude)
lon1 = math.radians(longitude)
lat2 = math.radians(user_latitude)
lon2 = math.radians(user_longitude)
radius = 6371  # Earth's radius in km
dlat = lat2 - lat1
dlon = lon2 - lon1
a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance = radius * c
return distance
$
""")

# Step 2: Create the FeatureSpec with the FeatureFunction
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup, FeatureFunction

fe = FeatureEngineeringClient()

features = [
    FeatureLookup(
        table_name=feature_table_name,
        lookup_key="destination_id"
    ),
    FeatureFunction(
        udf_name=function_name,
        output_name="distance",
        input_bindings={
            "latitude": "latitude",
            "longitude": "longitude",
            "user_latitude": "user_latitude",
            "user_longitude": "user_longitude"
        },
    ),
]

fe.create_feature_spec(name=feature_spec_name, features=features)
```

### Input Bindings

The `input_bindings` dictionary maps each parameter of the Unity Catalog function to its source:^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

- **Lookup columns**: Values from the feature table that are retrieved by the primary key (e.g., `"latitude": "latitude"`).
- **Context columns**: Values that must be supplied by the caller at inference time (e.g., `"user_latitude": "user_latitude"`).

When querying the endpoint, the caller includes both the lookup key(s) and the context values:^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
response = client.predict(
    endpoint=endpoint_name,
    inputs={
        "dataframe_records": [
            {"destination_id": 1, "user_latitude": 37, "user_longitude": -122},
        ]
    },
)
```

### Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The online serving infrastructure that hosts a FeatureSpec.
- [Online Feature Store](/concepts/online-feature-store.md) – Stores precomputed features for low-latency retrieval.
- [FeatureLookup](/concepts/featurelookup.md) – Declares which precomputed features to fetch from an online table.
- [FeatureSpec](/concepts/featurespec.md) – The combined specification of lookups and functions that defines the endpoint's serving logic.

### Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
