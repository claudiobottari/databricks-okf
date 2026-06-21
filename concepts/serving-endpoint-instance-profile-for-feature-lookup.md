---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea6e260d1b88cd00128777fa1e66e851c10c7d389723fdb3ccd4eb058fdbf404
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-instance-profile-for-feature-lookup
    - SEIPFFL
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Serving Endpoint Instance Profile for Feature Lookup
description: Configuration of Databricks model serving endpoints with instance profiles to enable MLflow models to authenticate and read features from third-party online stores.
tags:
  - databricks
  - model-serving
  - mlflow
  - instance-profile
timestamp: "2026-06-19T14:05:53.128Z"
---

# Serving Endpoint Instance Profile for Feature Lookup

**Serving Endpoint Instance Profile for Feature Lookup** refers to the authentication mechanism that allows Databricks-hosted MLflow models to read feature values from third-party online stores during inference. This is configured by attaching an instance profile to a Databricks serving endpoint, which provides read-only access to the online store.

## Overview

When a served MLflow model needs to look up features from a third-party online store — such as Amazon DynamoDB — it must authenticate with read permissions. The recommended approach for this is to configure an instance profile on the Databricks serving endpoint. This instance profile must have the necessary read permissions for the target online store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Requirements

The instance profile must have read permissions for the online store. For DynamoDB, these permissions include operations such as:

- `dynamodb:GetItem`
- `dynamodb:BatchGetItem`
- `dynamodb:Query`
- `dynamodb:Scan`
- `dynamodb:PartiQLSelect`
- `dynamodb:DescribeTable`

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Configuration Steps

1. **Create an instance profile** with the required read permissions for the target online store. This is typically done through the cloud provider's IAM (Identity and Access Management) console. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

2. **Configure the Databricks serving endpoint** to use the instance profile. Follow the documentation on [adding an instance profile to a model serving endpoint](/concepts/instance-profile-for-model-serving-endpoints.md) to attach the instance profile to the endpoint. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

3. **Publish the feature table** to the online store. When publishing, you do not need to specify a `read_secret_prefix`. Any `read_secret_prefix` that is specified is overridden by the instance profile configured on the serving endpoint. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Behavior

When an instance profile is configured on the serving endpoint:
- The served model uses the instance profile credentials for read authentication to the online store.
- Any explicit `read_secret_prefix` provided during feature table publishing is ignored in favor of the instance profile.
- No additional secret configuration is needed for read operations. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Alternative: Using Databricks Secrets

As an alternative to instance profiles, you can provide read credentials using [Databricks secrets](/concepts/databricks-secret-scopes.md). This involves creating secret scopes with read-only credentials and specifying a `read_secret_prefix` when publishing the feature table. However, Databricks recommends using instance profiles for lookup authentication. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Authentication for Working with Third-Party Online Stores — Overview of all authentication methods
- Instance Profile Authentication for Publishing — Write authentication for publishing feature tables
- Serving Endpoint Instance Profile for Publishing — Publishing authentication via serving endpoints
- Online Store Credentials Using Databricks Secrets — Alternative credential management
- [Feature Store — Publish Features to Online Store](/concepts/publishing-feature-tables-to-online-stores.md) — Publishing workflow

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
