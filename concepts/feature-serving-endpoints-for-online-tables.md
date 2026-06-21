---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7c859668198b5ff80a6ad43133952e25539532a88db3d15eeffbe9260cd4ded
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-endpoints-for-online-tables
    - FSEFOT
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Feature Serving Endpoints for Online Tables
description: A REST API endpoint that serves features from online tables at low latency for models and applications hosted outside Databricks, created via a Feature Spec linked to a Delta table.
tags:
  - databricks
  - feature-serving
  - REST-API
  - mlops
timestamp: "2026-06-19T14:52:22.456Z"
---

# Feature Serving Endpoints for Online Tables

**Feature Serving Endpoints** provide a REST API interface for serving feature data from [Online Tables](/concepts/online-tables.md) to applications hosted outside of Databricks. These endpoints enable low-latency lookups of feature values for model inference and other real-time use cases. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Overview

A Feature Serving endpoint exposes features from online tables through a standard REST API, making features available at low latency for external applications. When you create a feature serving endpoint, it automatically uses the associated online table to perform efficient, low-latency feature lookups. This is particularly useful for [Model Serving](/concepts/model-serving.md) with automatic feature lookup and for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Creating a Feature Serving Endpoint

### Step 1: Create a Feature Spec

First, create a feature spec that specifies the source Delta table. This feature spec can be used in both offline and online scenarios. The source Delta table and the online table must use the same primary key. The feature spec appears in the **Function** tab in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup

fe = FeatureEngineeringClient()

fe.create_feature_spec(
  name="catalog.default.user_preferences_spec",
  features=[
    FeatureLookup(
      table_name="user_preferences",
      lookup_key="user_id"
    )
  ]
)
```

### Step 2: Create the Endpoint

Using the feature spec, create a feature serving endpoint. This step assumes you have already created an online table that synchronizes data from the source Delta table. The endpoint makes data available through a REST API using the associated online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

> **Note:** The user performing this operation must be the owner of both the offline table and the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

workspace = WorkspaceClient()

# Create endpoint
endpoint_name = "fse-location"
workspace.serving_endpoints.create_and_wait(
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

### Step 3: Query the Endpoint

To access the API endpoint, send an HTTP POST request to the endpoint URL. The following example shows how to do this using Python: ^[databricks-online-tables-legacy-databricks-on-aws.md]

```python
import json, requests

url = "https://{workspace_url}/serving-endpoints/user-preferences/invocations"
headers = {'Authorization': f'Bearer {DATABRICKS_TOKEN}', 'Content-Type': 'application/json'}
data = {
  "dataframe_records": [{"user_id": user_id}]
}
data_json = json.dumps(data, allow_nan=True)

response = requests.request(method='POST', headers=headers, url=url, data=data_json)
if response.status_code != 200:
  raise Exception(f'Request failed with status {response.status_code}, {response.text}')

print(response.json()['outputs'][0]['hotel_preference'])
```

## Use Cases

### RAG Applications

Feature serving endpoints are commonly used with RAG Applications. The typical workflow involves: ^[databricks-online-tables-legacy-databricks-on-aws.md]

1. Creating a feature serving endpoint for the online table containing structured data.
2. Creating a tool using LangChain or a similar package that uses the endpoint for data lookups.
3. Using the tool in a LangChain agent or similar agent to retrieve relevant data.
4. Creating a model serving endpoint to host the application.

### Model Serving with Automatic Feature Lookup

When a model is trained using [FeatureLookup](/concepts/featurelookup.md) objects, and an online table is synced to the corresponding feature table, models served through [Model Serving](/concepts/model-serving.md) automatically look up feature values from the online table during inference — no additional configuration is required. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Endpoint Permission Model

A unique service principal is automatically created for each feature serving or model serving endpoint. This service principal has limited permissions required only to query data from online tables. This design ensures that: ^[databricks-online-tables-legacy-databricks-on-aws.md]

- Endpoints can access data independently of the user who created the resource.
- Endpoints continue to function if the creator leaves the workspace.
- The lifetime of the service principal matches the lifetime of the endpoint.

Audit logs may indicate system-generated records for the owner of the Unity Catalog catalog granting necessary privileges to this service principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md).
- A model must be registered in Unity Catalog to access online tables.
- A Databricks admin must accept the Serverless Terms of Service in the account console.
- The user creating the endpoint must be the owner of both the source Delta table and the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Online Tables](/concepts/online-tables.md) — The row-oriented, read-only copies of Delta Tables that serve as the data source for feature serving endpoints.
- Feature Serving — The broader capability of serving feature values for online inference.
- [Model Serving](/concepts/model-serving.md) — Serving machine learning models, which can automatically use feature serving endpoints for lookups.
- [FeatureLookup](/concepts/featurelookup.md) — The API object used to define feature dependencies during model training.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The Databricks UI for managing tables and online tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer required for online tables and feature serving.
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) — An alternative method for querying online tables using Serverless SQL warehouses.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
