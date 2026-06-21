---
title: Manage model serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints
ingestedAt: "2026-06-18T08:12:01.671Z"
---

This article describes how to manage model serving endpoints using the **Serving** UI and REST API. See [Serving endpoints](https://docs.databricks.com/api/workspace/servingendpoints) in the REST API reference.

To create model serving endpoints use one of the following:

*   [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).
*   [Create foundation model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints).

## Get the status of the model endpoint[​](#get-the-status-of-the-model-endpoint "Direct link to get-the-status-of-the-model-endpoint")

You can check the status of an endpoint using the **Serving** UI or programmatically using the REST API, Databricks Workspace Client, or MLflow Deployments SDK.

Endpoint statuses can be `Ready`, `Ready (Update failed)`, `Not ready (Updating)`, `Not ready (Update failed)`, or `Not ready (Stopped)`. Readiness refers to whether or not an endpoint can be queried. Updated failed indicates the latest change to the endpoint was unsuccessful. Stopped means the endpoint was stopped.

*   UI
*   REST API
*   Databricks Workspace Client
*   MLflow Deployments SDK

The **Serving endpoint state** indicator at the top of an endpoint's details page:

![Check endpoint status using the endpoint details Serving UI.](https://docs.databricks.com/aws/en/assets/images/get-endpoint-status-7879065a74ff40b4bb513d19597a6155.png)

![Check endpoint status using the list endpoints Serving UI.](https://docs.databricks.com/aws/en/assets/images/list-endpoints-status-b2f4cd6b68e8ef6b357bbfe5c66c647e.png)

## Stop a model serving endpoint[​](#stop-a-model-serving-endpoint "Direct link to stop-a-model-serving-endpoint")

You can temporarily stop a model serving endpoint and start it later. When an endpoint is stopped:

*   The resources provisioned for it are shut down.
*   The endpoint is not able to serve queries until it is started again.
*   Only endpoints that serve [custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models) and have no in-progress updates can be stopped.
*   Stopped endpoints do not count against the resource quota.
*   Queries sent to a stopped endpoint return a 400 error.

### Stop an endpoint[​](#stop-an-endpoint "Direct link to Stop an endpoint")

*   UI
*   REST API

Click **Stop** in the upper-right corner.

![Stop a model serving endpoint using the Serving UI.](https://docs.databricks.com/aws/en/assets/images/stop-endpoint-adc5f68c27e2ee01221122d4e327991e.png)

### Start an endpoint[​](#start-an-endpoint "Direct link to Start an endpoint")

Starting an endpoint creates a new config version with the same properties as the existing stopped config.

When you are ready to start a stopped model serving endpoint:

*   UI
*   REST API

Click **Start** in the upper-right corner.

![Start a model serving endpoint using the Serving UI.](https://docs.databricks.com/aws/en/assets/images/start-endpoint-70c40831e2320a781a0562e982211f7c.png)

## Delete a model serving endpoint[​](#delete-a-model-serving-endpoint "Direct link to delete-a-model-serving-endpoint")

Deleting an endpoint disables usage and deletes all data associated with the endpoint. You cannot undo deletion.

*   UI
*   REST API
*   MLflow Deployments SDK

Click the kebab menu at the top and select **Delete**.

![Delete a model serving endpoint using the Serving UI.](https://docs.databricks.com/aws/en/assets/images/delete-endpoint-daef728215d85cc27ebf386ebf1ac24a.png)

## Debug a model serving endpoint[​](#debug-a-model-serving-endpoint "Direct link to Debug a model serving endpoint")

Two types of logs are available to help debug issues with endpoints:

*   **Model server container build logs**: Generated during endpoint initialization when the container is being created. These logs capture the setup phase including downloading the model, installing dependencies, and configuring the runtime environment. Use these logs to debug why an endpoint failed to start or is stuck during deployment.
*   **Model server logs**: Generated during runtime when the endpoint is actively serving predictions. These logs capture incoming requests, model inference execution, runtime errors, and application-level logging from your model code. Use these logs to debug issues with predictions or investigate query failures.

Both log types are also accessible from the **Endpoints** UI in the **Logs** tab.

### Get container build logs[​](#get-container-build-logs "Direct link to Get container build logs")

For the **build logs** for a served model you can use the following request. See [Debugging guide for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug) for more information.

Bash

    GET /api/2.0/serving-endpoints/{name}/served-models/{served-model-name}/build-logs{  "config_version": 1  // optional}

### Get model server logs[​](#get-model-server-logs "Direct link to Get model server logs")

For the **model server** logs for a serve model, you can use the following request:

Bash

    GET /api/2.0/serving-endpoints/{name}/served-models/{served-model-name}/logs{  "config_version": 1  // optional}

## Manage permissions on a model serving endpoint[​](#manage-permissions-on-a-model-serving-endpoint "Direct link to manage-permissions-on-a-model-serving-endpoint")

You must have at least the CAN MANAGE permission on a serving endpoint to modify permissions. For more information on the permission levels, see [Serving endpoint ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#serving-endpoints).

note

When you update an endpoint, Databricks re-validates the recorded creator's workspace membership and served entity grants. For details, see [Identity and access](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#permissions).

Get the list of permissions on the serving endpoint.

*   UI
*   Databricks CLI

Click the Permissions button at the top right of the UI.

![Manage permissions of a model serving endpoint using the Serving UI.](https://docs.databricks.com/aws/en/assets/images/edit-permissions-577d4ec487cd16805b71ec63bddeaf5d.png)

You can also modify serving endpoint permissions using the [Permissions API](https://docs.databricks.com/api/workspace/permissions).

## Add a serverless usage policy for a model serving endpoint[​](#add-a-serverless-usage-policy-for-a-model-serving-endpoint "Direct link to add-a-serverless-usage-policy-for-a-model-serving-endpoint")

Serverless usage policies allow your organization to apply custom tags on serverless usage for granular billing attribution. If your workspace uses serverless usage policies to attribute serverless usage, you can add a serverless usage policy to your model serving endpoints. See [Attribute usage with serverless usage policies](https://docs.databricks.com/aws/en/admin/usage/budget-policies).

During model serving endpoint creation, you can select your endpoint's serverless usage policy from the **Usage policy** menu in the Serving UI. If you have a serverless usage policy assigned to you, all endpoints that you create are assigned that serverless usage policy, even if you do not select a policy from the **Usage policy** menu.

![Add serverless usage policy during model serving endpoint creation using the Serving UI.](https://docs.databricks.com/aws/en/assets/images/endpoint-budget-policy-7062c1373eeb2f58fe86dc3036514002.png)

If you have `MANAGE` permissions for an existing endpoint, you can edit and add a serverless usage policy to that endpoint from the **Endpoint details** page in the UI.

![Edit serverless usage policy on an existing model serving endpoint using the Serving UI.](https://docs.databricks.com/aws/en/assets/images/edit-endpoint-budget-policy-f643cbfab236d002f35271001d3c3dc2.png)

note

If you've been assigned a serverless usage policy, your existing endpoints are not automatically tagged with your policy. You must manually update existing endpoints if you want to attach a serverless usage policy to them.

## Get a model serving endpoint schema[​](#get-a-model-serving-endpoint-schema "Direct link to get-a-model-serving-endpoint-schema")

A serving endpoint query schema is a formal description of the serving endpoint using the standard OpenAPI specification in JSON format. It contains information about the endpoint including the endpoint path, details for querying the endpoint like the request and response body format, and data type for each field. This information can be helpful for reproducibility scenarios or when you need information about the endpoint, but you are not the original endpoint creator or owner.

To get the model serving endpoint schema, the served model must have a model signature logged and the endpoint must be in a `READY` state.

The following examples demonstrate how to programmatically get the model serving endpoint schema using the REST API. For feature serving endpoint schemas, see [Feature Serving endpoints](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving).

The schema returned by the API is in the format of a JSON object that follows the OpenAPI specification.

Bash

    ACCESS_TOKEN="<endpoint-token>"ENDPOINT_NAME="<endpoint name>"curl "https://example.databricks.com/api/2.0/serving-endpoints/$ENDPOINT_NAME/openapi" -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"

### Schema response details[​](#schema-response-details "Direct link to Schema response details")

The response is an OpenAPI specification in JSON format, typically including fields like `openapi`, `info`, `servers` and `paths`. Since the schema response is a JSON object, you can parse it using common programming languages, and generate client code from the specification using third-party tools. You can also visualize the OpenAPI specification using third-party tools like Swagger Editor.

The main fields of the response include:

*   The `info.title` field shows the name of the serving endpoint.
*   The `servers` field always contains one object, typically the `url` field which is the base url of the endpoint.
*   The `paths` object in the response contains all supported paths for an endpoint. The keys in the object are the path URL. Each `path` can support multiple formats of inputs. These inputs are listed in the `oneOf` field.

The following is an example endpoint schema response:

JSON

    {  "openapi": "3.1.0",  "info": {    "title": "example-endpoint",    "version": "2"  },  "servers": [{ "url": "https://example.databricks.com/serving-endpoints/example-endpoint" }],  "paths": {    "/served-models/vanilla_simple_model-2/invocations": {      "post": {        "requestBody": {          "content": {            "application/json": {              "schema": {                "oneOf": [                  {                    "type": "object",                    "properties": {                      "dataframe_split": {                        "type": "object",                        "properties": {                          "columns": {                            "description": "required fields: int_col",                            "type": "array",                            "items": {                              "type": "string",                              "enum": ["int_col", "float_col", "string_col"]                            }                          },                          "data": {                            "type": "array",                            "items": {                              "type": "array",                              "prefixItems": [                                {                                  "type": "integer",                                  "format": "int64"                                },                                {                                  "type": "number",                                  "format": "double"                                },                                {                                  "type": "string"                                }                              ]                            }                          }                        }                      },                      "params": {                        "type": "object",                        "properties": {                          "sentiment": {                            "type": "number",                            "format": "double",                            "default": "0.5"                          }                        }                      }                    },                    "examples": [                      {                        "columns": ["int_col", "float_col", "string_col"],                        "data": [                          [3, 10.4, "abc"],                          [2, 20.4, "xyz"]                        ]                      }                    ]                  },                  {                    "type": "object",                    "properties": {                      "dataframe_records": {                        "type": "array",                        "items": {                          "required": ["int_col", "float_col", "string_col"],                          "type": "object",                          "properties": {                            "int_col": {                              "type": "integer",                              "format": "int64"                            },                            "float_col": {                              "type": "number",                              "format": "double"                            },                            "string_col": {                              "type": "string"                            },                            "becx_col": {                              "type": "object",                              "format": "unknown"                            }                          }                        }                      },                      "params": {                        "type": "object",                        "properties": {                          "sentiment": {                            "type": "number",                            "format": "double",                            "default": "0.5"                          }                        }                      }                    }                  }                ]              }            }          }        },        "responses": {          "200": {            "description": "Successful operation",            "content": {              "application/json": {                "schema": {                  "type": "object",                  "properties": {                    "predictions": {                      "type": "array",                      "items": {                        "type": "number",                        "format": "double"                      }                    }                  }                }              }            }          }        }      }    }  }}
