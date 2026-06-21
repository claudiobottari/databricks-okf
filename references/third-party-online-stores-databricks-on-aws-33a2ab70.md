---
title: Third-party online stores | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/third-party-online-stores
ingestedAt: "2026-06-18T08:10:36.821Z"
---

For real-time serving of feature values, Databricks recommends using [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

With third-party online stores, you publish feature tables to a low-latency database and deploy the model or feature spec to a REST endpoint for real-time serving of feature values.

Databricks Feature Store also supports automatic feature lookup. In this case, the input values provided by the client include values that are only available at the time of inference. The model incorporates logic to automatically fetch the feature values it needs from the provided input values.

The diagram illustrates the relationship between MLflow and Feature Store components for real-time serving.

![Feature Store workflow with online lookup](https://docs.databricks.com/aws/en/assets/images/fs-flow-online-lookup-3a850a7f3a04730d5911da59a10619af.png)

Databricks Feature Store supports these online stores:

## Start using online stores[​](#start-using-online-stores "Direct link to Start using online stores")

See the following articles to get started with online stores:

*   [Authentication for working with third-party online stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication)
*   [Publish features to a third-party online store](https://docs.databricks.com/aws/en/machine-learning/feature-store/publish-features)
*   [Model Serving with automatic feature lookup](https://docs.databricks.com/aws/en/machine-learning/feature-store/automatic-feature-lookup) (includes example notebook)
