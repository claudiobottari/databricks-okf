---
title: Feature Serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving
ingestedAt: "2026-06-18T08:10:13.153Z"
---

Databricks Feature Serving makes data in the Databricks platform available to models or applications deployed outside of Databricks. Feature Serving endpoints automatically scale to adjust to real-time traffic and provide a high-availability, low-latency service for serving features. This page describes how to set up and use Feature Serving. For a step-by-step tutorial, see [Example: Deploy and query a feature serving endpoint](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-serving-tutorial).

When you use Model Serving to serve a model that was built using features from Databricks, the model automatically looks up and transforms features for inference requests. With Databricks Feature Serving, you can serve structured data for retrieval augmented generation (RAG) applications, as well as features that are required for other applications, such as models served outside of Databricks or any other application that requires features based on data in Unity Catalog.

![when to use feature serving](https://docs.databricks.com/aws/en/assets/images/when-to-use-feature-serving-c3596cc9cd702803b05fedae1389390a.png)

## Feature Serving benefits[​](#feature-serving-benefits "Direct link to Feature Serving benefits")

Databricks Feature Serving provides a single interface that serves pre-materialized and on-demand features. It also includes the following benefits:

*   Simplicity. Databricks handles the infrastructure. With a single API call, Databricks creates a production-ready serving environment.
*   High availability and scalability. Feature Serving endpoints automatically scale up and down to adjust to the volume of serving requests.
*   Security. Endpoints are deployed in a secure network boundary and use dedicated compute that terminates when the endpoint is deleted or scaled to zero.

## Requirements[​](#requirements "Direct link to requirements")

*   Databricks Runtime 14.2 ML or above.
*   To use the Python API, Feature Serving requires `databricks-feature-engineering` version 0.1.2 or above, which is built into Databricks Runtime 14.2 ML. For earlier Databricks Runtime ML versions, manually install the required version using `%pip install databricks-feature-engineering>=0.1.2`. If you are using a Databricks notebook, you must then restart the Python kernel by running this command in a new cell: `dbutils.library.restartPython()`.
*   To use the Databricks SDK, Feature Serving requires `databricks-sdk` version 0.18.0 or above. To manually install the required version, use `%pip install databricks-sdk>=0.18.0`. If you are using a Databricks notebook, you must then restart the Python kernel by running this command in a new cell: `dbutils.library.restartPython()`.

Databricks Feature Serving provides a UI and several programmatic options for creating, updating, querying, and deleting endpoints. This article includes instructions for each of the following options:

*   Databricks UI
*   REST API
*   Python API
*   Databricks SDK

To use the REST API or MLflow Deployments SDK, you must have a Databricks API token.

## Authentication for Feature Serving[​](#authentication-for-feature-serving "Direct link to Authentication for Feature Serving")

For information about authentication, see [Authorize access to Databricks resources](https://docs.databricks.com/aws/en/dev-tools/auth/).

## Create a `FeatureSpec`[​](#create-a-featurespec "Direct link to create-a-featurespec")

A `FeatureSpec` is a user-defined set of features and functions. You can combine features and functions in a `FeatureSpec`. `FeatureSpecs` are stored in and managed by Unity Catalog and appear in Catalog Explorer.

The tables specified in a `FeatureSpec` must be published to an online feature store or a third-party online store. See [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

You must use the `databricks-feature-engineering` package to create a `FeatureSpec`.

First, define the function:

Python

    from unitycatalog.ai.core.databricks import DatabricksFunctionClientclient = DatabricksFunctionClient()CATALOG = "main"SCHEMA = "default"def difference(num_1: float, num_2: float) -> float:  """  A function that accepts two floating point numbers, subtracts the second one  from the first, and returns the result as a float.  Args:      num_1 (float): The first number.      num_2 (float): The second number.  Returns:      float: The resulting difference of the two input numbers.  """  return num_1 - num_2client.create_python_function(  func=difference,  catalog=CATALOG,  schema=SCHEMA,  replace=True)

Then you can use the function in a `FeatureSpec`:

Python

    from databricks.feature_engineering import (  FeatureFunction,  FeatureLookup,  FeatureEngineeringClient,)fe = FeatureEngineeringClient()features = [  # Lookup column `average_yearly_spend` and `country` from a table in UC by the input `user_id`.  FeatureLookup(    table_name="main.default.customer_profile",    lookup_key="user_id",    feature_names=["average_yearly_spend", "country"]  ),  # Calculate a new feature called `spending_gap` - the difference between `ytd_spend` and `average_yearly_spend`.  FeatureFunction(    udf_name="main.default.difference",    output_name="spending_gap",    # Bind the function parameter with input from other features or from request.    # The function calculates num_1 - num_2.    input_bindings={"num_1": "ytd_spend", "num_2": "average_yearly_spend"},  ),]# Create a `FeatureSpec` with the features defined above.# The `FeatureSpec` can be accessed in Unity Catalog as a function.fe.create_feature_spec(  name="main.default.customer_features",  features=features,)

### Specify default values[​](#specify-default-values "Direct link to Specify default values")

To specify default values for features, use the `default_values` parameter in the `FeatureLookup`. See the following example:

Python

    feature_lookups = [    FeatureLookup(        table_name="ml.recommender_system.customer_features",        feature_names=[            "membership_tier",            "age",            "page_views_count_30days",        ],        lookup_key="customer_id",        default_values={          "age": 18,          "membership_tier": "bronze"        },    ),]

If the feature columns are renamed using the `rename_outputs` parameter, `default_values` must use the renamed feature names.

Python

    FeatureLookup(  table_name = 'main.default.table',  feature_names = ['materialized_feature_value'],  lookup_key = 'id',  rename_outputs={"materialized_feature_value": "feature_value"},  default_values={    "feature_value": 0  })

## Create an endpoint[​](#create-an-endpoint "Direct link to Create an endpoint")

The `FeatureSpec` defines the endpoint. For more information, see [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints), [the Python API documentation](https://api-docs.databricks.com/python/feature-engineering/latest/ml_features.endpoint_core_config.html), or the [Databricks SDK documentation](https://github.com/databricks/databricks-sdk-py/blob/e290be90ac0bcf8d01207f8186bc757890c75a09/databricks/sdk/service/serving.py#L159) for details.

note

For workloads that are latency sensitive or require high queries per second, Model Serving offers route optimization on custom model serving endpoints, see [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization).

*   Databricks SDK - Python
*   Python API
*   REST API

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInputworkspace = WorkspaceClient()# Create endpointworkspace.serving_endpoints.create(  name="my-serving-endpoint",  config = EndpointCoreConfigInput(    served_entities=[    ServedEntityInput(        entity_name="main.default.customer_features",        scale_to_zero_enabled=True,        workload_size="Small"      )    ]  ))

To see the endpoint, click **Serving** in the left sidebar of the Databricks UI. When the state is **Ready**, the endpoint is ready to respond to queries. To learn more about Model Serving, see [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

### Save the augmented DataFrame in the inference table[​](#save-the-augmented-dataframe-in-the-inference-table "Direct link to Save the augmented DataFrame in the inference table")

For endpoints created starting February 2025, you can configure the model serving endpoint to log the augmented DataFrame that contains the looked-up feature values and function return values. The DataFrame is saved to the inference table for the served model.

For instructions on setting this configuration, see [Log feature lookup DataFrames to inference tables](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#features).

For information about inference tables, see [Monitor served models using Unity AI Gateway\-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables).

## Get an endpoint[​](#get-an-endpoint "Direct link to Get an endpoint")

You can use the Databricks SDK or the Python API to get the metadata and status of an endpoint.

*   Databricks SDK - Python
*   Python API

Python

    from databricks.sdk import WorkspaceClientworkspace = WorkspaceClient()endpoint = workspace.serving_endpoints.get(name="customer-features")# print(endpoint)

## Get the schema of an endpoint[​](#get-the-schema-of-an-endpoint "Direct link to Get the schema of an endpoint")

You can use the Databricks SDK or the REST API to get the schema of an endpoint. For more information about the endpoint schema, see [Get a model serving endpoint schema](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#get-schema).

*   Databricks SDK - Python
*   REST API

Python

    from databricks.sdk import WorkspaceClientworkspace = WorkspaceClient()# Create endpointendpoint = workspace.serving_endpoints.get_open_api(name="customer-features")

## Query an endpoint[​](#query-an-endpoint "Direct link to Query an endpoint")

You can use the REST API, the MLflow Deployments SDK, or the Serving UI to query an endpoint.

The following code shows how to set up credentials and create the client when using the MLflow Deployments SDK.

      # Set up credentials  export DATABRICKS_HOST=...  export DATABRICKS_TOKEN=...

Python

      # Set up the client  import mlflow.deployments  client = mlflow.deployments.get_deploy_client("databricks")

note

As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use [OAuth tokens](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m).

If you use personal access token authentication, Databricks recommends using personal access tokens belonging to [service principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals#tokens).

### Query an endpoint using APIs[​](#query-an-endpoint-using-apis "Direct link to Query an endpoint using APIs")

This section includes examples of querying an endpoint using the REST API or the MLflow Deployments SDK.

*   MLflow Deployments SDK
*   REST API

Python

    import mlflow.deploymentsclient = mlflow.deployments.get_deploy_client("databricks")response = client.predict(    endpoint="test-feature-endpoint",    inputs={        "dataframe_records": [            {"user_id": 1, "ytd_spend": 598},            {"user_id": 2, "ytd_spend": 280},        ]    },)

### Query an endpoint using the UI[​](#query-an-endpoint-using-the-ui "Direct link to Query an endpoint using the UI")

You can query a serving endpoint directly from the Serving UI. The UI includes generated code examples that you can use to query the endpoint.

1.  In the left sidebar of the Databricks workspace, click **Serving**.
    
2.  Click the endpoint you want to query.
    
3.  In the upper-right of the screen, click **Query endpoint**.
    
    ![query endpoint button](https://docs.databricks.com/aws/en/assets/images/query-endpoint-button-43406a324b7d59064f5be64026243a70.png)
    
4.  In the **Request** box, type the request body in JSON format.
    
5.  Click **Send request**.
    

JSON

    // Example of a request body.{  "dataframe_records": [    { "user_id": 1, "ytd_spend": 598 },    { "user_id": 2, "ytd_spend": 280 }  ]}

The **Query endpoint** dialog includes generated example code in curl, Python, and SQL. Click the tabs to view and copy the example code.

![query endpoint dialog](https://docs.databricks.com/aws/en/assets/images/query-endpoint-dialog-693b693d2c8303a6e87262fa82de380f.png)

To copy the code, click the copy icon in the upper-right of the text box.

![copy button in query endpoint dialog](https://docs.databricks.com/aws/en/assets/images/query-endpoint-dialog-with-code-6316cdbe439df6ce632e8a8dd3665262.png)

## Update an endpoint[​](#update-an-endpoint "Direct link to Update an endpoint")

important

To modify a Feature Serving endpoint's configuration (such as changing the `FeatureSpec` or workload size), always use the update APIs described in this section. Do not delete and recreate the endpoint to apply changes. Deleting a live endpoint causes immediate downtime and interrupts all applications that query it.

You can update an endpoint using the REST API, the Databricks SDK, or the Serving UI.

### Update an endpoint using APIs[​](#update-an-endpoint-using-apis "Direct link to Update an endpoint using APIs")

*   Databricks SDK - Python
*   REST API

Python

    from databricks.sdk import WorkspaceClientworkspace = WorkspaceClient()workspace.serving_endpoints.update_config(  name="my-serving-endpoint",  served_entities=[    ServedEntityInput(      entity_name="main.default.customer_features",      scale_to_zero_enabled=True,      workload_size="Small"    )  ])

### Update an endpoint using the UI[​](#update-an-endpoint-using-the-ui "Direct link to Update an endpoint using the UI")

Follow these steps to use the Serving UI:

1.  In the left sidebar of the Databricks workspace, click **Serving**.
2.  In the table, click the name of the endpoint you want to update. The endpoint screen appears.
3.  In the upper-right of the screen, click **Edit endpoint**.
4.  In the **Edit serving endpoint** dialog, edit the endpoint settings as needed.
5.  Click **Update** to save your changes.

![update an endpoint](https://docs.databricks.com/aws/en/assets/images/update-endpoint-30420b342aac8449c8bab7d181ad0c24.png)

## Delete an endpoint[​](#delete-an-endpoint "Direct link to Delete an endpoint")

warning

This action is irreversible. Deleting a Feature Serving endpoint causes immediate downtime for any applications querying it. If you want to change the endpoint's configuration, use [Update an endpoint](#update-an-endpoint) instead of deleting and recreating the endpoint.

You can delete an endpoint using the REST API, the Databricks SDK, the Python API, or the Serving UI.

### Delete an endpoint using APIs[​](#delete-an-endpoint-using-apis "Direct link to Delete an endpoint using APIs")

*   Databricks SDK - Python
*   Python API
*   REST API

Python

    from databricks.sdk import WorkspaceClientworkspace = WorkspaceClient()workspace.serving_endpoints.delete(name="customer-features")

### Delete an endpoint using the UI[​](#delete-an-endpoint-using-the-ui "Direct link to Delete an endpoint using the UI")

Follow these steps to delete an endpoint using the Serving UI:

1.  In the left sidebar of the Databricks workspace, click **Serving**.
2.  In the table, click the name of the endpoint you want to delete. The endpoint screen appears.
3.  In the upper-right of the screen, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) and select **Delete**.

![delete an endpoint](https://docs.databricks.com/aws/en/assets/images/delete-endpoint-11109d506b8679598b1a8e29cf9563c8.png)

## Monitor the health of an endpoint[​](#monitor-the-health-of-an-endpoint "Direct link to Monitor the health of an endpoint")

For information about the logs and metrics available for Feature Serving endpoints, see [Monitor model quality and endpoint health](https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints).

## Access control[​](#access-control "Direct link to Access control")

For information about permissions on Feature Serving endpoints, see [Manage permissions on a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#permissions).

## Example notebook[​](#example-notebook "Direct link to Example notebook")

This notebook illustrates how to use the Databricks SDK to create a Feature Serving endpoint using Databricks Online Feature Store.

#### Feature Serving example notebook with online store
