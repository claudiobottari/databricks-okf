---
title: Serve declarative features | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/serve-declarative-features
ingestedAt: "2026-06-18T08:10:34.973Z"
---

important

Feature Serving endpoints are not supported for Declarative Feature Engineering. To serve features online, deploy a model serving endpoint using a model logged through Unity Catalog.

Models that are trained using features from Databricks automatically track lineage to the features they were trained on. When deployed as model serving endpoints, these models use Unity Catalog to look up features from online stores.

## Deploy a model serving endpoint[​](#deploy-a-model-serving-endpoint "Direct link to Deploy a model serving endpoint")

Use an existing model serving endpoint, or use the Databricks SDK to create a new one. The model must be registered in Unity Catalog.

The following code shows how to create a new model serving endpoint. For more information, see [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInputw = WorkspaceClient()endpoint_name = "fraud-detection-endpoint"model_name = "main.ecommerce.fraud_model"w.serving_endpoints.create(    name=endpoint_name,    config=EndpointCoreConfigInput(        name=endpoint_name,        served_entities=[            ServedEntityInput(                entity_name=model_name,                entity_version=1,                max_provisioned_concurrency=4,                min_provisioned_concurrency=0,            )        ],    ),)

## Query the endpoint[​](#query-the-endpoint "Direct link to Query the endpoint")

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()response = w.serving_endpoints.query(    name="fraud-detection-endpoint",    dataframe_records=[        {"user_id": "user_123", "transaction_time": "2026-03-01T12:00:00"},    ],)

## Query the endpoint with RequestSource features[​](#query-the-endpoint-with-requestsource-features "Direct link to Query the endpoint with RequestSource features")

If the model was trained with `RequestSource` features, the request payload must also include all `RequestSource` columns. These columns were added to the MLflow model signature during `log_model`, so the endpoint's API schema reflects the required request fields.

Python

    response = w.serving_endpoints.query(    name="fraud-detection-endpoint",    dataframe_records=[        {            "user_id": "user_123",            "transaction_time": "2026-03-01T12:00:00",            "transaction_amount": 275.30,  # RequestSource column            "vendor_id": "v_42",           # RequestSource column (also used as entity key)        },    ],)

Entity keys are used for looking up table-backed features from the online store. `RequestSource` columns are passed through directly to the model.

You can also use `curl`:

Bash

    curl -X POST "https://<workspace>.cloud.databricks.com/serving-endpoints/<endpoint>/invocations" \  -H "Authorization: Bearer $DATABRICKS_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "dataframe_records": [      {        "user_id": "user_123",        "transaction_time": "2026-03-01T12:00:00",        "transaction_amount": 275.30,        "vendor_id": "v_42"      }    ]  }'
