---
title: "Example: Deploy and query a feature serving endpoint | Databricks on AWS"
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-serving-tutorial
ingestedAt: "2026-06-18T08:10:15.184Z"
---

Step-by-step example showing how to deploy and query a feature serving endpoint using the Databricks SDK. You can also use the Databricks UI or the REST API to create and query feature serving endpoints. Links to that documentation are included.

In this example, you have a table of cities with their locations (latitude and longitude) and a recommender app that takes into account the user's current distance from those cities. Because the user's location changes constantly, the distance between the user and each city must be calculated at the time of inference. This tutorial illustrates how to perform those calculations with low latency using Databricks Online Feature Store and Databricks Feature Serving. For the full set of example code, see the [example notebook](#example).

## Step 1. Create the source table[​](#step-1-create-the-source-table "Direct link to Step 1. Create the source table")

The source table contains precomputed feature values and can be any Delta table in Unity Catalog with a primary key. In this example, the table contains a list of cities with their latitude and longitude. The primary key is `destination_id`. Sample data is shown below.

## Step 2. Create the online feature store[​](#step-2-create-the-online-feature-store "Direct link to Step 2. Create the online feature store")

For details about Databricks Online Feature Stores, see [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()feature_table_name = f"{catalog_name}.{schema_name}.location_features"function_name = f"{catalog_name}.{schema_name}.distance"# Create the feature tablefe.create_table(  name = feature_table_name,  primary_keys="destination_id",  df = destination_location_df,  description = "Destination location features.")# Enable Change Data Feed to enable CONTINOUS and TRIGGERED publish modesspark.sql(f"ALTER TABLE {feature_table_name} SET TBLPROPERTIES (delta.enableChangeDataFeed = 'true')")# Create an online store with specified capacityonline_store_name = f"{username}-online-store"fe.create_online_store(    name=online_store_name,    capacity="CU_2"  # Valid options: "CU_1", "CU_2", "CU_4", "CU_8")# Wait until the state is AVAILABLEonline_store = fe.get_online_store(name=online_store_name)online_store.state# Publish the tablepublished_table = fe.publish_table(    online_store=online_store,    source_table_name=feature_table_name,    online_table_name=online_table_name)

## Step 3. Create a function in Unity Catalog[​](#step-3-create-a-function-in-unity-catalog "Direct link to step-3-create-a-function-in-unity-catalog")

In this example, the function calculates the distance between the destination (whose location does not change) and the user (whose location changes frequently and is not known until the time of inference).

Python

    # Define the function. This function calculates the distance between two locations.function_name = f"main.on_demand_demo.distance"spark.sql(f"""CREATE OR REPLACE FUNCTION {function_name}(latitude DOUBLE, longitude DOUBLE, user_latitude DOUBLE, user_longitude DOUBLE)RETURNS DOUBLELANGUAGE PYTHON AS$$import mathlat1 = math.radians(latitude)lon1 = math.radians(longitude)lat2 = math.radians(user_latitude)lon2 = math.radians(user_longitude)# Earth's radius in kilometersradius = 6371# Haversine formuladlat = lat2 - lat1dlon = lon2 - lon1a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))distance = radius * creturn distance$$""")

## Step 4. Create a feature spec in Unity Catalog[​](#step-4-create-a-feature-spec-in-unity-catalog "Direct link to step-4-create-a-feature-spec-in-unity-catalog")

The feature spec specifies the features that the endpoint serves and their lookup keys. It also specifies any required functions to apply to the retrieved features with their bindings. For details, see [Create a `FeatureSpec`](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving#create-a-featurespec).

Python

    from databricks.feature_engineering import FeatureLookup, FeatureFunction, FeatureEngineeringClientfe = FeatureEngineeringClient()features=[ FeatureLookup(   table_name=feature_table_name,   lookup_key="destination_id" ), FeatureFunction(   udf_name=function_name,   output_name="distance",   input_bindings={     "latitude": "latitude",     "longitude": "longitude",     "user_latitude": "user_latitude",     "user_longitude": "user_longitude"   }, ),]feature_spec_name = f"main.on_demand_demo.travel_spec"# The following code ignores errors raised if a feature_spec with the specified name already exists.try: fe.create_feature_spec(name=feature_spec_name, features=features, exclude_columns=None)except Exception as e: if "already exists" in str(e):   pass else:   raise e

## Step 5. Create a feature serving endpoint[​](#step-5-create-a-feature-serving-endpoint "Direct link to Step 5. Create a feature serving endpoint")

To create a feature serving endpoint, you can use the UI [Create an endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#create-an-endpoint), the [REST API](https://docs.databricks.com/api/workspace/servingendpoints/create), or the Databricks SDK, shown here.

The feature serving endpoint takes the `feature_spec` that you created in Step 4 as a parameter.

Python

    from databricks.sdk import WorkspaceClientfrom databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput# Create endpointendpoint_name = "fse-location"try: status = workspace.serving_endpoints.create_and_wait(   name=endpoint_name,   config = EndpointCoreConfigInput(     served_entities=[       ServedEntityInput(         entity_name=feature_spec_name,         scale_to_zero_enabled=True,         workload_size="Small"       )     ]   ) ) print(status)# Get the status of the endpointstatus = workspace.serving_endpoints.get(name=endpoint_name)print(status)

## Step 6. Query the feature serving endpoint[​](#step-6-query-the-feature-serving-endpoint "Direct link to Step 6. Query the feature serving endpoint")

When you query the endpoint, you provide the primary key and optionally any context data that the function uses. In this example, the function takes as input the user's current location (latitude and longitude). Because the user's location is constantly changing, it must be provided to the function at inference time as a context feature.

You can also query the endpoint using the UI [Query an endpoint using the UI](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving#query-an-endpoint-using-the-ui) or the [REST API](https://docs.databricks.com/api/workspace/servingendpoints/query).

For simplicity, this example only calculates the distance to two cities. A more realistic scenario might calculate the user's distance from each location in the feature table to determine which cities to recommend.

Python

    import mlflow.deploymentsclient = mlflow.deployments.get_deploy_client("databricks")response = client.predict(   endpoint=endpoint_name,   inputs={       "dataframe_records": [           {"destination_id": 1, "user_latitude": 37, "user_longitude": -122},           {"destination_id": 2, "user_latitude": 37, "user_longitude": -122},       ]   },)pprint(response)

## Example notebook[​](#example-notebook "Direct link to example-notebook")

See this notebook for a complete illustration of the steps:

#### Feature Serving example notebook with online store

## Additional information[​](#additional-information "Direct link to Additional information")

For details about using the feature engineering Python API, see [the reference documentation](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).
