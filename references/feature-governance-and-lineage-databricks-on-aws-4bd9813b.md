---
title: Feature governance and lineage | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/lineage
ingestedAt: "2026-06-18T08:10:18.823Z"
---

Databricks Feature Store governs access to feature tables and automatically tracks lineage across the feature tables, functions, and models used to build a model.

For information about monitoring the performance of a served model and changes in feature table data, see [Data profiling](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/).

## Control access to feature tables[​](#control-access-to-feature-tables "Direct link to Control access to feature tables")

Access control for feature tables in Unity Catalog is managed by Unity Catalog. See [Unity Catalog privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).

## View feature table, function, and model lineage[​](#view-feature-table-function-and-model-lineage "Direct link to View feature table, function, and model lineage")

When you log a model using `FeatureEngineeringClient.log_model`, the features used in the model are automatically tracked and can be viewed in the **Lineage** tab of Catalog Explorer. In addition to feature tables, Python UDFs that are used to compute on-demand features are also tracked.

## How to capture lineage of a feature table, function, or model[​](#how-to-capture-lineage-of-a-feature-table-function-or-model "Direct link to How to capture lineage of a feature table, function, or model")

Lineage information tracking feature tables and functions used in models is automatically captured when you call `log_model`. See the following example code.

Python

    from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup, FeatureFunctionfe = FeatureEngineeringClient()features = [    FeatureLookup(        table_name = "main.on_demand_demo.restaurant_features",        feature_names = ["latitude", "longitude"],        rename_outputs={"latitude": "restaurant_latitude", "longitude": "restaurant_longitude"},        lookup_key = "restaurant_id",        timestamp_lookup_key = "ts"    ),    FeatureFunction(        udf_name="main.on_demand_demo.extract_user_latitude",        output_name="user_latitude",        input_bindings={"blob": "json_blob"},    ),    FeatureFunction(        udf_name="main.on_demand_demo.extract_user_longitude",        output_name="user_longitude",        input_bindings={"blob": "json_blob"},    ),    FeatureFunction(        udf_name="main.on_demand_demo.haversine_distance",        output_name="distance",        input_bindings={"x1": "restaurant_longitude", "y1": "restaurant_latitude", "x2": "user_longitude", "y2": "user_latitude"},    )]training_set = fe.create_training_set(    label_df, feature_lookups=features, label="label", exclude_columns=["restaurant_id", "json_blob", "restaurant_latitude", "restaurant_longitude", "user_latitude", "user_longitude", "ts"])class IsClose(mlflow.pyfunc.PythonModel):    def predict(self, ctx, inp):        return (inp['distance'] < 2.5).valuesmodel_name = "fe_packaged_model"mlflow.set_registry_uri("databricks-uc")fe.log_model(    IsClose(),    model_name,    flavor=mlflow.pyfunc,    training_set=training_set,    registered_model_name=registered_model_name)

## View the lineage of a feature table, model, or function[​](#view-the-lineage-of-a-feature-table-model-or-function "Direct link to View the lineage of a feature table, model, or function")

To view the lineage of a feature table, model, or function, follow these steps:

1.  Navigate to the table, model version, or function page in Catalog Explorer.
    
2.  Select the **Lineage** tab. The left sidebar shows Unity Catalog components that were logged with this table, model version, or function.
    
    ![Lineage tab on model page in Catalog Explorer](https://docs.databricks.com/aws/en/assets/images/model-page-lineage-tab-bbdc568a7dbbb5f618cd54da17a61f95.png)
    
3.  Click **See lineage graph**. The lineage graph appears. For details about exploring the lineage graph, see [Data lineage in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage).
    
    ![lineage screen](https://docs.databricks.com/aws/en/assets/images/lineage-graph-27b728d947b58f826aaac446e640d143.png)
    
4.  To close the lineage graph, click ![close button for lineage graph](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFqADAAQAAAABAAAAFgAAAAAcITNaAAABlElEQVQ4Ed3Tva4BURAH8P9u9h2UEo0Gsa/gCRRbidBJPI+PfhVapUZFdGhktxCF6BDis8Q1k3s21o5djeLeU1hzzpxfxuzQ7o+FLyz9CyaT/wQ+Ho/o9Xr4pP3n81nMFVsxGo3Q7XbR6XRCcUKbzSbD6/Xa97oMX/Qb5HI5UNWDwQC32w2WZQXSCK3X6zgcDqhWq4jFYr4cEaaMfD7PiYQbhuHFtHm5XBjd7/eMxuNxzn3+eAtT0jOuYkLp5xNaqVQgoZQbCitM0zT0+33u93w+x3a7ZTSRSFCKuLRP/3ntdhvj8ZgRqjSZTIqg2hSnQh2q52azwWw2UyGGwyGu16sXS18iYUIbjQa/sHK5DNM04TgObNsOxUPhVzSTyaBQKCCdTns4jaO03sK73Y4rpXmlSlOpFN/XdR2lUsnDW60Wz/orLsKE1mo1EFosFj1UXX7Gp9MpJFyEJ5MJTqcTo9lsVnm+p8KpPa7rYrVa+c5pNgPr0bf7YrEI7Esbj+m4L5fLwNHHc+wvJzoSWxF9LTrj78E/Ap8lauZ1EcwAAAAASUVORK5CYII=) in the upper-right corner.
