---
title: Serve multiple models to a model serving endpoint | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint
ingestedAt: "2026-06-18T08:12:48.966Z"
---

This article describes how to programmatically configure a model serving endpoint to serve multiple models and the traffic split between them.

Serving multiple models from a single endpoint enables you to split traffic between different models to compare their performance and facilitate A/B testing. You can also serve different versions of a model at the same time, which makes experimenting with new versions easier, while keeping the current version in production.

You can serve any of the following model types on a Model Serving endpoint. You can not serve different model types in a single endpoint. For example you can not serve a custom model and an external model in the same endpoint.

*   [Custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models)
*   Generative AI models made available through Foundation Model APIs [provisioned throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)
*   [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/)

## Requirements[​](#requirements "Direct link to Requirements")

See the [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#requirement) for model serving endpoint creation.

To understand access control options for model serving endpoints and best practice guidance for endpoint management, see [Serving endpoint ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#serving-endpoints).

## Create an endpoint and set the initial traffic split[​](#create-an-endpoint-and-set-the-initial-traffic-split "Direct link to Create an endpoint and set the initial traffic split")

When you create model serving endpoints using the Model Serving API or the [Model Serving UI](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#create), you can also set the initial traffic split for the models you want to serve on that endpoint. The following sections provide examples of setting the traffic split for multiple custom models or foundation models served on an endpoint.

### Serve multiple custom models to an endpoint[​](#serve-multiple-custom-models-to-an-endpoint "Direct link to Serve multiple custom models to an endpoint")

The following REST API example creates a single endpoint with two custom models in Unity Catalog and sets the endpoint traffic split between those models. The served entity, `current`, hosts version 1 of `model-A` and gets 90% of the endpoint traffic, while the other served entity, `challenger`, hosts version 1 of `model-B` and gets 10% of the endpoint traffic.

Bash

    POST /api/2.0/serving-endpoints{   "name":"multi-model"   "config":   {      "served_entities":      [         {            "name":"current",            "entity_name":"catalog.schema.model-A",            "entity_version":"1",            "workload_size":"Small",            "scale_to_zero_enabled":true         },         {            "name":"challenger",            "entity_name":"catalog.schema.model-B",            "entity_version":"1",            "workload_size":"Small",            "scale_to_zero_enabled":true         }      ],      "traffic_config":      {         "routes":         [            {               "served_model_name":"current",               "traffic_percentage":"90"            },            {               "served_model_name":"challenger",               "traffic_percentage":"10"            }         ]      }   }}

### Serve multiple models to a provisioned throughput endpoint[​](#serve-multiple-models-to-a-provisioned-throughput-endpoint "Direct link to serve-multiple-models-to-a-provisioned-throughput-endpoint")

The following REST API example creates a single Foundation Model APIs provisioned throughput endpoint with two models and sets the endpoint traffic split between those models. The endpoint named `multi-pt-model`, hosts version 2 of `meta_llama_v3_1_70b_instruct` which gets 60% of the endpoint traffic, and also hosts version 3 of `meta_llama_v3_1_8b_instruct` which gets 40% of the endpoint traffic.

Bash

    POST /api/2.0/serving-endpoints{   "name":"multi-pt-model"   "config":   {      "served_entities":      [         {            "name":"meta_llama_v3_1_70b_instruct",            "entity_name":"system.ai.meta_llama_v3_1_70b_instruct",            "entity_version":"4",            "min_provisioned_throughput":0,            "max_provisioned_throughput":2400         },         {            "name":"meta_llama_v3_1_8b_instruct",            "entity_name":"system.ai.meta_llama_v3_1_8b_instruct",            "entity_version":"4",            "min_provisioned_throughput":0,            "max_provisioned_throughput":1240         }      ],      "traffic_config":      {         "routes":         [            {               "served_model_name":"meta_llama_v3_1_8b_instruct",               "traffic_percentage":"60"            },            {               "served_model_name":"meta_llama_v3_1_70b_instruct",               "traffic_percentage":"40"            }         ]      }   }}

### Serve multiple external models to an endpoint[​](#serve-multiple-external-models-to-an-endpoint "Direct link to serve-multiple-external-models-to-an-endpoint")

You can also configure multiple [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/) in a serving endpoint as long as they all have the same task type and each model has a unique `name`. You cannot have both external models and non-external models in the same serving endpoint.

The following example creates a serving endpoint that routes 50% of the traffic to `gpt-4` provided by OpenAI and the remaining 50% to `claude-3-opus-20240229` provided by Anthropic.

Python

    import mlflow.deploymentsclient = mlflow.deployments.get_deploy_client("databricks")client.create_endpoint(    name="mix-chat-endpoint",    config={        "served_entities": [            {                "name": "served_model_name_1",                "external_model": {                    "name": "gpt-4",                    "provider": "openai",                    "task": "llm/v1/chat",                    "openai_config": {                        "openai_api_key": "{{secrets/my_openai_secret_scope/openai_api_key}}"                    }                }            },            {                "name": "served_model_name_2",                "external_model": {                    "name": "claude-3-opus-20240229",                    "provider": "anthropic",                    "task": "llm/v1/chat",                    "anthropic_config": {                        "anthropic_api_key": "{{secrets/my_anthropic_secret_scope/anthropic_api_key}}"                    }                }            }        ],        "traffic_config": {            "routes": [                {"served_model_name": "served_model_name_1", "traffic_percentage": 50},                {"served_model_name": "served_model_name_2", "traffic_percentage": 50}            ]        },    })

## Update the traffic split between served models[​](#update-the-traffic-split-between-served-models "Direct link to Update the traffic split between served models")

You can also update the traffic split between served models. The following REST API example sets the served model, `current`, to get 50% of the endpoint traffic and the other model, `challenger`, to get the remaining 50% of the traffic.

You can also make this update from the **Serving** tab in the Databricks UI using the **Edit configuration** button.

Bash

    PUT /api/2.0/serving-endpoints/{name}/config{   "served_entities":   [      {         "name":"current",         "entity_name":"catalog.schema.model-A",         "entity_version":"1",         "workload_size":"Small",         "scale_to_zero_enabled":true      },      {         "name":"challenger",         "entity_name":"catalog.schema.model-B",         "entity_version":"1",         "workload_size":"Small",         "scale_to_zero_enabled":true      }   ],   "traffic_config":   {      "routes":      [         {            "served_model_name":"current",            "traffic_percentage":"50"         },         {            "served_model_name":"challenger",            "traffic_percentage":"50"         }      ]   }}

## Query individual models behind an endpoint[​](#query-individual-models-behind-an-endpoint "Direct link to query-individual-models-behind-an-endpoint")

In some scenarios, you might want to query individual models behind the endpoint.

You can do so by using:

Bash

    POST /serving-endpoints/{endpoint-name}/served-models/{served-model-name}/invocations

Here the specific served model is queried. The request format is the same as querying the endpoint. While querying the individual served model, the traffic settings are ignored.

In the context of the `multi-model` endpoint example, if all requests are sent to `/serving-endpoints/multi-model/served-models/challenger/invocations`, then all requests are served by the `challenger` served model.
