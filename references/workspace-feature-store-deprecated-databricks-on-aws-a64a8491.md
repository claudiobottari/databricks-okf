---
title: Workspace Feature Store (deprecated) | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/
ingestedAt: "2026-06-18T08:10:52.148Z"
---

note

This documentation covers the Workspace Feature Store. Workspace Feature Store is available only for workspaces created before August 19, 2024, 4:00:00 PM (UTC).

Workspace Feature Store is deprecated. Databricks recommends using [Feature Engineering in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc).

Workspace Feature Store is fully integrated with other components of Databricks and provides the following benefits:

*   Discoverability. The Feature Store UI, accessible from the Databricks workspace, lets you browse and search for existing features.
*   Lineage. When you create a feature table in Databricks, the data sources used to create the feature table are saved and accessible. For each feature in a feature table, you can also access the models, notebooks, jobs, and endpoints that use the feature.
*   Integration with model scoring and serving. When you use features from Feature Store to train a model, the model is packaged with feature metadata. When you use the model for batch scoring or online inference, it automatically retrieves features from Feature Store. The caller does not need to know about them or include logic to look up or join features to score new data. This makes model deployment and updates much easier.
*   Point-in-time lookups. Feature Store supports time series and event-based use cases that require point-in-time correctness.

The typical machine learning workflow using Feature Store follows this path:

1.  Write code to convert raw data into features and create a Spark DataFrame containing the desired features.
2.  [Write the DataFrame as a feature table in the Workspace Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/feature-tables#create-feature-table).
3.  Train a model using features from the feature store. When you do this, the model stores the specifications of features used for training. When the model is used for inference, it automatically joins features from the appropriate feature tables.
4.  Register model in [Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry).

You can now use the model to make predictions on new data. For batch use cases, the model automatically retrieves the features it needs from Feature Store.

![Feature Store workflow for batch machine learning use cases.](https://docs.databricks.com/aws/en/assets/images/feature-store-flow-gcp-57e35cf7f77239ddad447ba2b7beb5f1.png)

For real-time serving use cases, publish the features to an online store. See [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

At inference time, the model reads pre-computed features from the online store and joins them with the data provided in the client request to the model serving endpoint.

![Feature Store flow for machine learning models that are served.](https://docs.databricks.com/aws/en/assets/images/feature-store-flow-with-online-store-031283c533262f17af5ccaa15b57d6ea.png)

## Start using Workspace Feature Store[​](#start-using-workspace-feature-store "Direct link to Start using Workspace Feature Store")

To get started, try these example notebooks. The basic notebook steps you through how to create a feature table, use it to train a model, and then perform batch scoring using automatic feature lookup. It also introduces you to the Feature Engineering UI and shows how you can use it to search for features and understand how features are created and used.

#### Basic Workspace Feature Store example notebook

The taxi example notebook illustrates the process of creating features, updating them, and using them for model training and batch inference.

#### Workspace Feature Store taxi example notebook

## Supported data types[​](#supported-data-types "Direct link to Supported data types")

For supported data types, see [Supported data types](https://docs.databricks.com/aws/en/machine-learning/feature-store/#supported-data-types).
