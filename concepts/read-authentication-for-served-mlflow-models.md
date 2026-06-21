---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 771c7c7be23ee875c1b39bdf916ffa31ebdff9032024f20cfbd1bc59c87ad511
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-authentication-for-served-mlflow-models
    - RAFSMM
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Read Authentication for Served MLflow Models
description: Required read credentials (via instance profile on serving endpoints or secrets with read_secret_prefix) for Databricks-hosted MLflow models to look up feature values from third-party online stores.
tags:
  - mlflow
  - model-serving
  - authentication
  - feature-store
timestamp: "2026-06-19T17:38:05.115Z"
---

# Read Authentication for Served MLflow Models

**Read Authentication for Served MLflow Models** refers to the mechanisms used to grant Databricks-hosted MLflow models permission to look up feature values from third-party online stores during serving. When a model is deployed to a serving endpoint and needs to retrieve features for inference, the system must authenticate with the external online store to read the data. Two primary methods are supported: instance profiles and Databricks secrets.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Overview

Databricks-hosted MLflow models that serve predictions must connect to third-party online stores—such as Amazon DynamoDB—to look up feature values. To enable this connection, you must configure **read authentication** for the served model. The authentication method you choose depends on your infrastructure and security requirements.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

Databricks supports two approaches for providing read authentication to served MLflow models:

### Instance Profile (Recommended)

Databricks recommends using an instance profile attached to the serving endpoint for lookup authentication. This approach avoids managing secrets directly and integrates with AWS IAM roles.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

To configure this:

1. **Create an instance profile** that has read permission to the online store.
2. **Configure your Databricks serving endpoint** to use the instance profile. See the documentation on [configuring an instance profile for model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile).
3. When publishing your feature table, you do not need to specify a `read_prefix`; any `read_prefix` you specify is overridden by the instance profile.

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Databricks Secrets

As an alternative, you can store credentials in Databricks Secrets and refer to them using a `read_secret_prefix` when publishing the feature table. This method provides more granular control over credential management.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

To configure secrets for read authentication:

1. **Create a secret scope** for read-only access (shown here as `<read-scope>`).
2. **Store the appropriate secrets** for the target online store type:

**For DynamoDB (or other key-value stores):**
- `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
- `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`

**For SQL stores:**
- `databricks secrets put-secret <read-scope> <prefix>-user`
- `databricks secrets put-secret <read-scope> <prefix>-password`

If you are using an instance profile for read authentication (configured at the Databricks Serving endpoint level), you do not need to create a `<read-scope>`.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Comparison with Write Authentication

Read authentication is separate from write authentication. While write authentication uses the same two methods (instance profile or secrets), the configuration points differ:
- **Write authentication** is configured at the **cluster** level (when publishing feature tables).
- **Read authentication** is configured at the **serving endpoint** level (for served models).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- Use an **instance profile** for read authentication when possible, as it simplifies credential management and integrates with AWS IAM.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- If you use secrets, consider Secret Scope Sharing to avoid hitting the workspace limit on the number of secret scopes. A single secret scope can be shared for accessing all online stores.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- Ensure your IAM user or instance profile has read permissions appropriate for the online store. For DynamoDB, this typically includes actions like `dynamodb:GetItem`, `dynamodb:BatchGetItem`, and `dynamodb:Query`.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Deploying and hosting MLflow models for inference.
- Feature Store Authentication — Broader context for both read and write authentication.
- Publishing Features to Third-Party Online Stores — The write-side counterpart to read authentication.
- Databricks Secrets — Secure credential storage for Databricks workloads.
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) — AWS IAM roles attached to compute resources.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
