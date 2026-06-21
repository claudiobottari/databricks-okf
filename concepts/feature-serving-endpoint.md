---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9d81a5cdf760a0dea5b664f095b381e357dbe0c3ccc932179ff358e357ca6b8
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feature-serving-endpoint
    - FSE
    - Create serving endpoint
    - Feature Serving Endpoint Schema
    - Feature Serving Endpoints
    - Feature Serving endpoints
    - Feature serving endpoints
    - feature serving endpoints
    - Feature Serving|feature serving endpoints
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 1
      end: 10
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 13
      end: 20
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 26
      end: 30
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 55
      end: 85
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 86
      end: 110
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 30
      end: 50
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 35
      end: 50
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 42
      end: 44
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 110
      end: 130
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 133
      end: 135
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 136
      end: 150
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 134
      end: 135
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
      start: 1
      end: 10
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
      start: 8
      end: 12
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 127
      end: 127
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
      start: 126
      end: 126
title: Feature Serving Endpoint
description: A Databricks endpoint that serves precomputed and on-demand features for real-time inference using a FeatureSpec
tags:
  - feature-store
  - serving
  - inference
timestamp: "2026-06-19T18:44:10.842Z"
---

# Feature Serving Endpoint

A **Feature Serving Endpoint** is a managed REST API service on Databricks that serves feature values from online tables to external applications with low latency. It enables real-time applications such as recommendation engines, fraud detection systems, and RAG agents to perform online feature lookups. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:1-10]

## Overview

Feature Serving Endpoints bridge offline feature engineering and online inference. The endpoint is configured with a [FeatureSpec](/concepts/featurespec.md) that declares which features to serve, their lookup keys, and any [FeatureFunction](/concepts/featurefunction.md) UDFs to apply at serving time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:13-20]

The endpoint relies on an online feature store (an online table) that holds a low-latency, row-oriented copy of the source Delta table. Publishing the source table to the online store is a prerequisite for creating the endpoint. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:26-30]

## Creating a Feature Spec

Before deploying an endpoint, a [FeatureSpec](/concepts/featurespec.md) must be created in Unity Catalog. The spec determines what data the endpoint will serve and how it will be computed. It can include:

- **FeatureLookup** objects that reference a feature table and specify the lookup key column.
- **FeatureFunction** objects that reference a UDF in Unity Catalog, along with input bindings that map feature values and inference-time context to the function's parameters.

The following example creates a feature spec for a travel recommendation scenario: the spec looks up a city’s latitude and longitude from a feature table, and then computes a distance using a user-defined function (UDF) that takes the user’s current location at inference time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:55-85]

```python
from databricks.feature_engineering import FeatureLookup, FeatureFunction, FeatureEngineeringClient

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
        }
    )
]

fe.create_feature_spec(
    name="catalog.schema.travel_spec",
    features=features
)
```

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:86-110]

## Creating the Online Store

An online store must first be created and the source table published to it. The online store is a serverless, low-latency storage layer. Capacity options include `CU_1`, `CU_2`, `CU_4`, and `CU_8`. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:30-50]

```python
fe.create_online_store(
    name=online_store_name,
    capacity="CU_2"
)
published_table = fe.publish_table(
    online_store=online_store,
    source_table_name=feature_table_name,
    online_table_name=online_table_name
)
```

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:35-50]

The source table must have Change Data Feed enabled for continuous or triggered publishing. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:42-44]

## Creating a Feature Serving Endpoint

An endpoint can be created using the Databricks UI, the REST API, or the Databricks SDK. The endpoint is configured with:

- **Entity name** – The fully qualified name of the feature spec.
- **Workload size** – Determines the compute capacity (`Small`, `Medium`, `Large`).
- **Scale‑to‑zero** – Option to automatically shut down the endpoint when idle.

### Using the Databricks SDK

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

workspace = WorkspaceClient()
endpoint_name = "fse-location"

status = workspace.serving_endpoints.create_and_wait(
    name=endpoint_name,
    config=EndpointCoreConfigInput(
        served_entities=[
            ServedEntityInput(
                entity_name=feature_spec_name,
                scale_to_zero_enabled=True,
                workload_size="Small"
            )
        ]
    )
)
```

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:110-130]

## Querying the Endpoint

To query the endpoint, send an HTTP POST request with the primary key values and any context data required by feature functions. The endpoint returns the computed feature values. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:133-135]

### Using the MLflow Deployments Client

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")
response = client.predict(
    endpoint=endpoint_name,
    inputs={
        "dataframe_records": [
            {"destination_id": 1, "user_latitude": 37, "user_longitude": -122},
            {"destination_id": 2, "user_latitude": 37, "user_longitude": -122},
        ]
    }
)
```

^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:136-150]

The user’s latitude and longitude are context features provided at inference time because they are not known during offline precomputation. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:134-135]

## Use Case: Retrieval-Augmented Generation (RAG)

Feature Serving Endpoints are used in structured RAG applications. An online table holds structured data, and the endpoint exposes it to a LangChain tool. The RAG agent uses the tool to look up relevant data during generation. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md:1-10]

The typical workflow is: ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md:8-12]

1. Create a feature serving endpoint.
2. Create a LangChain tool that queries the endpoint.
3. Use the tool in a LangChain agent.
4. Host the LangChain application on a model serving endpoint.

## Best Practices

- **Enable scale‑to‑zero**: Use this option for development and staging environments to minimize costs when the endpoint is idle. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:127]
- **Choose appropriate workload size**: Start with `Small` for testing and scale based on latency and throughput needs. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:126]

## Limitations

- The user creating the endpoint must be the owner of both the offline source table and the online table (implied by the publishing step). ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:30-50]

## Related Concepts

- [Online Tables](/concepts/online-tables.md) — The low-latency storage layer serving feature values.
- [FeatureSpec](/concepts/featurespec.md) — The Unity Catalog object that defines the endpoint’s serving plan.
- [FeatureFunction](/concepts/featurefunction.md) — UDF-based mechanism for computing features at serving time.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — The Python API for creating feature tables, online stores, and feature specs.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — Hosts ML models or LangChain applications that may consume features.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer managing feature specs, UDFs, and tables.
- RAG Applications — Generative AI apps that can use Feature Serving Endpoints for structured lookups.

## Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:1-10](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
2. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:13-20](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
3. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:26-30](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
4. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:55-85](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
5. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:86-110](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
6. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:30-50](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
7. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:35-50](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
8. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:42-44](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
9. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:110-130](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
10. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:133-135](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
11. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:136-150](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
12. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:134-135](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
13. [example-use-features-with-structured-rag-applications-databricks-on-aws.md:1-10](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
14. [example-use-features-with-structured-rag-applications-databricks-on-aws.md:8-12](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
15. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:127-127](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
16. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md:126-126](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
