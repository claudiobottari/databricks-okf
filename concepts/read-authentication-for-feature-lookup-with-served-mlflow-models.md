---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 248af811e841676e62468c45c2c951038a8034acb011b06e512ef12a341eb644
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-authentication-for-feature-lookup-with-served-mlflow-models
    - RAFFLWSMM
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Read Authentication for Feature Lookup with Served MLflow Models
description: Methods and requirements for authenticating read operations when Databricks-hosted MLflow models look up features from third-party online stores.
tags:
  - authentication
  - feature-store
  - mlflow
  - model-serving
timestamp: "2026-06-18T10:49:50.070Z"
---

# Read Authentication for Feature Lookup with Served MLflow Models

When a Databricks-hosted MLflow model is served and needs to look up feature values from a third-party online store (such as Amazon DynamoDB or a SQL-based store), read authentication must be provided so the model endpoint can connect to that store. This page describes the two supported authentication methods: an instance profile attached to the serving endpoint, or Databricks secrets.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Prerequisite: Understanding the Targeting

The read authentication configuration is required only when the served model performs feature lookup. The lookup details are defined during the publishing of the feature table to the third-party online store. When using an instance profile for read authentication, any `read_secret_prefix` you may have specified during publishing is **overridden** by the instance profile setting.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Method 1: Instance Profile Configured to the Served Model

Databricks recommends providing read authentication through an instance profile attached to the [Model Serving](/concepts/model-serving.md) endpoint.

1. Create an [AWS instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) that grants read-only permissions to the target online store. For DynamoDB, the required read permissions include actions such as `dynamodb:GetItem`, `dynamodb:BatchGetItem`, `dynamodb:Query`, `dynamodb:Scan`, and `dynamodb:PartiQLSelect` (a full list of DynamoDB actions needed for read operations is in the write authentication section of the source, but only read actions are relevant here).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

2. Configure your [Databricks serving endpoint to use this instance profile](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile). Once the endpoint is configured, you do not need to specify any `read_secret_prefix` when publishing the feature table; any such prefix is automatically overridden with the instance profile credentials.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Method 2: Databricks Secrets

Alternatively, you can store read credentials in Databricks Secrets and refer to them at publish time via a `read_secret_prefix`. This method is useful when you cannot attach an instance profile to the serving endpoint.

### Setup Steps

1. Create a secret scope for read-only access (e.g., `<read-scope>`). You may reuse an existing scope, but be aware of workspace limits on the number of secret scopes. To avoid hitting that limit, you can define a single scope for all online stores.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

2. Choose a unique prefix for the target online store, shown here as `<prefix>`.

   **For DynamoDB** (supports Feature Engineering client and Feature Store client v0.3.8 and above), create the following secrets:
   - Access key ID: `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
   - Secret access key: `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`

   **For SQL stores**, create the following secrets:
   - Read-only user: `databricks secrets put-secret <read-scope> <prefix>-user`
   - Read-only password: `databricks secrets put-secret <read-scope> <prefix>-password`

   These secrets correspond to the IAM user (DynamoDB) or database user (SQL store) that has read-only access to the online store.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

3. When publishing the feature table to the online store, provide the `read_secret_prefix` parameter that points to the scope and prefix, e.g., `<read-scope>.<prefix>`. The model serving endpoint will then use those credentials for feature lookup.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

> **Note**: If you are using an instance profile for write authentication (at the cluster level) and also want to use secrets for read authentication, you only need to create the read secrets scope. The write scope is optional in that case.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- **Use an instance profile when possible**. It simplifies credential management by eliminating the need to store and rotate secrets manually.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **If using secrets, store read-only credentials in a separate scope** from write credentials to follow the principle of least privilege.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Test the connection** after configuring the endpoint to ensure that feature lookup succeeds at inference time.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Managing and serving feature tables
- [Model Serving](/concepts/model-serving.md) — Deploying MLflow models as endpoints
- Databricks Secrets — Secure credential storage
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) — AWS IAM roles for Databricks compute
- [Write Authentication for Publishing Feature Tables](/concepts/write-authentication-for-publishing-feature-tables.md) — Corresponding authentication for writing features (for context)

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
