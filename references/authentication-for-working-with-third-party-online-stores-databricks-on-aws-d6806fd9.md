---
title: Authentication for working with third-party online stores | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication
ingestedAt: "2026-06-18T08:10:17.121Z"
---

Publishing feature tables to a third-party online store requires write authentication, and looking up features requires read authentication. Configure both using an instance profile or Databricks secrets, as described in the following sections.

The table shows the authentication methods supported for each action:

## Authentication for publishing feature tables to third-party online stores[​](#authentication-for-publishing-feature-tables-to-third-party-online-stores "Direct link to Authentication for publishing feature tables to third-party online stores")

To publish feature tables to an third-party online store, you must provide write authentication.

Databricks recommends that you provide write authentication through [an instance profile attached to a Databricks cluster](#auth-instance-profile). Alternatively, you can [store credentials in Databricks secrets](#provide-online-store-credentials-using-databricks-secrets), and then refer to them in a `write_secret_prefix` when publishing.

The instance profile or IAM user should have all of the following permissions:

*   `dynamodb:DeleteItem`
*   `dynamodb:DeleteTable`
*   `dynamodb:PartiQLSelect`
*   `dynamodb:DescribeTable`
*   `dynamodb:PartiQLInsert`
*   `dynamodb:GetItem`
*   `dynamodb:CreateGlobalTable`
*   `dynamodb:BatchGetItem`
*   `dynamodb:UpdateTimeToLive`
*   `dynamodb:BatchWriteItem`
*   `dynamodb:ConditionCheckItem`
*   `dynamodb:PutItem`
*   `dynamodb:PartiQLUpdate`
*   `dynamodb:Scan`
*   `dynamodb:Query`
*   `dynamodb:UpdateItem`
*   `dynamodb:DescribeTimeToLive`
*   `dynamodb:CreateTable`
*   `dynamodb:UpdateGlobalTableSettings`
*   `dynamodb:UpdateTable`
*   `dynamodb:PartiQLDelete`
*   `dynamodb:DescribeTableReplicaAutoScaling`

### Provide write authentication through an instance profile attached to a Databricks cluster[​](#provide-write-authentication-through-an-instance-profile-attached-to-a-databricks-cluster "Direct link to provide-write-authentication-through-an-instance-profile-attached-to-a-databricks-cluster")

On clusters running Databricks Runtime 10.5 ML and above, you can use the instance profile attached to the cluster for write authentication when publishing to DynamoDB online stores.

note

Use these steps only for write authentication when publishing to DynamoDB online stores.

1.  Create an [instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) that has write permission to the online store.
2.  Attach the instance profile to a Databricks cluster by following these two steps:
    1.  [Add the instance profile to Databricks](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile#add-instance-profile).
    2.  [Launch a cluster with the instance profile](https://docs.databricks.com/aws/en/compute/configure#instance-profiles).
3.  Select the cluster with the attached instance profile to run the code to publish to the online store. You do not need to provide explicit secret credentials or `write_secret_prefix` to the [online store spec](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

### Provide write credentials using Databricks secrets[​](#provide-write-credentials-using-databricks-secrets "Direct link to Provide write credentials using Databricks secrets")

Follow the instructions in [Use Databricks secrets](#provide-online-store-credentials-using-databricks-secrets).

## Authentication for looking up features from third-party online stores with served MLflow models[​](#authentication-for-looking-up-features-from-third-party-online-stores-with-served-mlflow-models "Direct link to Authentication for looking up features from third-party online stores with served MLflow models")

To enable Databricks-hosted MLflow models to connect to third-party online stores and look up feature values, you must provide read authentication.

Databricks recommends that you provide lookup authentication through [an instance profile attached to a Databricks served model](#auth-instance-profile-lookup). Alternatively, you can [store credentials in Databricks secrets](#provide-online-store-credentials-using-databricks-secrets), and then refer to them in a `read_secret_prefix` when publishing.

### Provide lookup authentication through an instance profile configured to a served model[​](#provide-lookup-authentication-through-an-instance-profile-configured-to-a-served-model "Direct link to provide-lookup-authentication-through-an-instance-profile-configured-to-a-served-model")

1.  Create an [instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) that has write permission to the online store.
    
2.  Configure your [Databricks serving endpoint to use instance profile](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile).
    
    note
    
    When publishing your table, you do not have to specify a `read_prefix`, and any `read_prefix` specified is overridden with the instance profile.
    

### Provide read credentials using Databricks secrets[​](#provide-read-credentials-using-databricks-secrets "Direct link to Provide read credentials using Databricks secrets")

Follow the instructions in [Use Databricks secrets](#provide-online-store-credentials-using-databricks-secrets).

## Use Databricks secrets for read and write authentication.[​](#use-databricks-secrets-for-read-and-write-authentication "Direct link to use-databricks-secrets-for-read-and-write-authentication")

This section shows the steps to follow to set up authentication with Databricks secrets. For code examples illustrating how to use these secrets, see [Publish features to a third-party online store](https://docs.databricks.com/aws/en/machine-learning/feature-store/publish-features).

1.  [Create two secret scopes](https://docs.databricks.com/aws/en/security/secrets/#secrets) that contain credentials for the online store: one for read-only access (shown here as `<read-scope>`) and one for read-write access (shown here as `<write-scope>`). Alternatively, you can reuse existing secret scopes.
    
    If you intend to use an instance profile for write authentication (configured at Databricks cluster level), you do not need to include the `<write-scope>`. If you intend to use an instance profile for read authentication (configured at Databricks Serving endpoint level), you do not need to include the `<read-scope>`.
    
2.  Pick a unique name for the target online store, shown here as `<prefix>`.
    
    For DynamoDB (works with any version of Feature Engineering client, and Feature Store client v0.3.8 and above), create the following secrets:
    
    *   Access key ID for the IAM user with read-only access to the target online store: `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
    *   Secret access key for the IAM user with read-only access to the target online store: `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`
    *   Access key ID for the IAM user with read-write access to the target online store: `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
    *   Secret access key for the IAM user with read-write access to the target online store: `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`
    
    For SQL stores, create the following secrets:
    
    *   User with read-only access to the target online store: `databricks secrets put-secret <read-scope> <prefix>-user`
    *   Password for user with read-only access to the target online store: `databricks secrets put-secret <read-scope> <prefix>-password`
    *   User with read-write access to the target online store: `databricks secrets put-secret <write-scope> <prefix>-user`
    *   Password for user with read-write access to the target online store: `databricks secrets put-secret <write-scope> <prefix>-password`

note

There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can [define and share](https://docs.databricks.com/aws/en/security/secrets/#scopes) a single secret scope for accessing all online stores.
