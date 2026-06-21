---
title: Share feature tables across workspaces (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/feature-store/multiple-workspaces
ingestedAt: "2026-06-18T08:02:47.566Z"
---

important

*   This documentation has been retired and might not be updated.
*   Databricks recommends using [Feature Engineering in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc) to share feature tables across workspaces. The approach in this article is deprecated.

Databricks supports sharing feature tables across multiple workspaces. For example, from your own workspace, you can create, write to, or read from a feature table in a centralized feature store. This is useful when multiple teams share access to feature tables or when your organization has multiple workspaces to handle different stages of development.

For a centralized feature store, Databricks recommends that you designate a single workspace to store all feature store metadata, and create accounts for each user who needs access to the feature store.

If your teams are also [sharing models across workspaces](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/multiple-workspaces), you may choose to dedicate the same centralized workspace for both feature tables and models, or you could specify different centralized workspaces for each.

![Multiple feature store workspaces](https://docs.databricks.com/aws/en/assets/images/multiworkspace-0841a1291637a9c09c68eb1952364323.png)

Access to the centralized feature store is controlled by tokens. Each user or script that needs access [creates a personal access token](https://docs.databricks.com/api/workspace/tokenmanagement) in the centralized feature store and copies that token into the secret manager of their local workspace. Each API request sent to the centralized feature store workspace must include the access token; the Feature Store client provides a simple mechanism to specify the secrets to be used when performing cross-workspace operations.

note

As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use [OAuth tokens](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m).

If you use personal access token authentication, Databricks recommends using personal access tokens belonging to [service principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals#tokens).

## Requirements[​](#requirements "Direct link to Requirements")

Using a feature store across workspaces requires:

*   Feature Store client v0.3.6 and above.
*   Both workspaces must have access to the raw feature data. They must share the same [external Hive metastore](https://docs.databricks.com/aws/en/archive/external-metastores/external-hive-metastore) and have access to the same [DBFS storage](https://docs.databricks.com/aws/en/dbfs/).
*   If [IP access lists](https://docs.databricks.com/aws/en/security/network/front-end/ip-access-list-workspace) are enabled, workspace IP addresses must be on access lists.

## Set up the API token for a remote registry[​](#set-up-the-api-token-for-a-remote-registry "Direct link to Set up the API token for a remote registry")

In this section, “Workspace B” refers to the centralized or remote feature store workspace.

1.  In Workspace B, [create an access token](https://docs.databricks.com/api/workspace/tokenmanagement).
2.  In your local workspace, [create secrets](https://docs.databricks.com/aws/en/dev-tools/cli/commands) to store the access token and information about Workspace B:
    1.  Create a secret scope: `databricks secrets create-scope --scope <scope>`.
    2.  Pick a unique identifier for Workspace B, shown here as `<prefix>`. Then [create](https://docs.databricks.com/aws/en/dev-tools/cli/commands) three secrets with the specified key names:
        *   `databricks secrets put --scope <scope> --key <prefix>-host` : Enter the hostname of Workspace B. Use the following Python commands to get the hostname of a workspace:
            
            Python
            
                import mlflowhost_url = mlflow.utils.databricks_utils.get_webapp_url()host_url
            
        *   `databricks secrets put --scope <scope> --key <prefix>-token` : Enter the access token from Workspace B.
            
        *   `databricks secrets put --scope <scope> --key <prefix>-workspace-id` : Enter the workspace ID for Workspace B which can be [found in the URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-instance-names-urls-and-ids) of any page.
            

## Specify a remote feature store[​](#specify-a-remote-feature-store "Direct link to Specify a remote feature store")

Based on the secret scope and name prefix you created for the remote feature store workspace, you can construct a feature store URI of the form:

Python

    feature_store_uri = f'databricks://<scope>:<prefix>'

Then, specify the URI explicitly when you instantiate a `FeatureStoreClient`:

Python

    fs = FeatureStoreClient(feature_store_uri=feature_store_uri)

Before you create feature tables in the remote feature store, you must create a database to store them. The database must exist in the shared DBFS location.

For example, to create a database `recommender` in the shared location `/mnt/shared`, use the following command:

    %sql CREATE DATABASE IF NOT EXISTS recommender LOCATION '/mnt/shared'

## Create a feature table in the remote feature store[​](#create-a-feature-table-in-the-remote-feature-store "Direct link to Create a feature table in the remote feature store")

The API to create a feature table in a remote feature store depends on the Databricks runtime version you are using.

*   V0.3.6 and above
*   V0.3.5 and below

Use the `FeatureStoreClient.create_table` API:

Python

    fs = FeatureStoreClient(feature_store_uri=f'databricks://<scope>:<prefix>')fs.create_table(  name='recommender.customer_features',  primary_keys='customer_id',  schema=customer_features_df.schema,  description='Customer-keyed features')

For examples of other Feature Store methods, see [Notebook example: Share feature tables across workspaces](#example).

## Use a feature table from the remote feature store[​](#use-a-feature-table-from-the-remote-feature-store "Direct link to Use a feature table from the remote feature store")

You can read a feature table in the remote feature store with the `FeatureStoreClient.read_table` method by first setting the `feature_store_uri`:

Python

    fs = FeatureStoreClient(feature_store_uri=f'databricks://<scope>:<prefix>')customer_features_df = fs.read_table(  name='recommender.customer_features',)

Other helper methods for accessing the feature table are also supported:

Python

    fs.read_table()fs.get_feature_table() # in v0.3.5 and belowfs.get_table() # in v0.3.6 and abovefs.write_table()fs.publish_table()fs.create_training_set()

## Use a remote model registry[​](#use-a-remote-model-registry "Direct link to Use a remote model registry")

In addition to specifying a remote feature store URI, you may also specify a remote model registry URI to [share models across workspaces](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/multiple-workspaces).

To specify a remote model registry for model logging or scoring, you can use a model registry URI to instantiate a FeatureStoreClient.

Python

    fs = FeatureStoreClient(model_registry_uri=f'databricks://<scope>:<prefix>')customer_features_df = fs.log_model(    model,    "recommendation_model",    flavor=mlflow.sklearn,    training_set=training_set,    registered_model_name="recommendation_model")

Using `feature_store_uri` and `model_registry_uri`, you can train a model using any local or remote feature table, and then register the model in any local or remote model registry.

Python

    fs = FeatureStoreClient(    feature_store_uri=f'databricks://<scope>:<prefix>',    model_registry_uri=f'databricks://<scope>:<prefix>')

The following notebook shows how to work with a centralized feature store.

#### Centralized Feature Store example notebook
