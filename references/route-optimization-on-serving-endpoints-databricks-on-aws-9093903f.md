---
title: Route optimization on serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization
ingestedAt: "2026-06-18T08:12:42.520Z"
---

This article describes how to enable route optimization on your [model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) or [feature serving](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving) endpoints. Route optimized serving endpoints dramatically lower overhead latency and allow for substantial improvements in the throughput supported by your endpoint.

Route-optimized endpoints are queried differently from non-route-optimized endpoints, including using a different URL and authentication using OAuth tokens. See [Query route-optimized serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization) for details.

## What is route optimization?[​](#what-is-route-optimization "Direct link to What is route optimization?")

When you enable route optimization on an endpoint, Databricks Model Serving improves the network path for inference requests, resulting in faster, more direct communication between your client and the model. This optimized routing unlocks higher queries per second (QPS) compared to non-optimized endpoints and provides more stable and lower latencies for your applications.

## Requirements[​](#requirements "Direct link to Requirements")

*   Route optimization on **model serving endpoints** have the same requirements as [non-route-optimized model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#requirement).
*   Route optimization on **feature serving endpoints** have the same requirements as [non-route-optimized feature serving endpoints](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving#requirement).

## Enable route optimization on a model serving endpoint[​](#enable-route-optimization-on-a-model-serving-endpoint "Direct link to Enable route optimization on a model serving endpoint")

*   Serving UI
*   REST API
*   Python
*   Databricks SDK

You can enable route optimization when you create a model serving endpoint using the **Serving** UI. You can only enable route optimization during endpoint creation, you can not update existing endpoints to be route optimized.

1.  In the sidebar, click **Serving** to display the Serving UI.
2.  Click **Create serving endpoint**.
3.  In the **Route optimization** section, select **Enable route optimization.**
4.  After your endpoint is created, Databricks sends you a notification about what is needed to query a route optimized endpoint.

![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/create-endpoint-eb0a4ce61321f63be092b3e0359f1c07.png)

## Enable route optimization on a feature serving endpoint[​](#enable-route-optimization-on-a-feature-serving-endpoint "Direct link to enable-route-optimization-on-a-feature-serving-endpoint")

To use route optimization for Feature and Function Serving, specify the full name of the feature specification in the `entity_name` field for serving endpoint creation requests. The `entity_version` is not needed for `FeatureSpecs`.

Bash

    POST /api/2.0/serving-endpoints{  "name": "my-endpoint",  "config":  {    "served_entities":    [      {        "entity_name": "catalog_name.schema_name.feature_spec_name",        "workload_type": "CPU",        "workload_size": "Small",        "scale_to_zero_enabled": true      }    ]  },  "route_optimized": true}

## Limitations[​](#limitations "Direct link to Limitations")

*   Route optimization is only available for custom model serving endpoints and feature serving endpoints. Serving endpoints that use [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) or [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/) are not supported.
*   Databricks in-house OAuth tokens are the only supported authentication for route optimization. Personal access tokens are not supported.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query route-optimized serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization)
*   [Optimize Model Serving endpoints for production](https://docs.databricks.com/aws/en/machine-learning/model-serving/production-optimization)
