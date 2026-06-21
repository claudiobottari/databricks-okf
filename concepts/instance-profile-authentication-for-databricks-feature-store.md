---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0385aa6f97cb4879398920ffd28042c07948ddf6e30be4b41eeb24a92c6bcf9e
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-authentication-for-databricks-feature-store
    - IPAFDFS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Instance Profile Authentication for Databricks Feature Store
description: Using AWS instance profiles attached to Databricks clusters or serving endpoints to authenticate feature store operations with third-party online stores.
tags:
  - authentication
  - aws
  - instance-profile
  - databricks
timestamp: "2026-06-18T10:50:13.935Z"
---

## Instance Profile Authentication for Databricks Feature Store

**Instance profile authentication** for the [Databricks Feature Store](/concepts/databricks-feature-store.md) (or Feature Engineering) allows you to publish feature tables to, and look up features from, third-party online stores (such as DynamoDB) without managing explicit credentials. Databricks recommends using instance profiles for both write (publishing) and read (lookup) authentication where possible. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Write Authentication for Publishing Feature Tables

To publish feature tables to a third-party online store, the instance profile must have the necessary write permissions for the target store. For DynamoDB online stores, the required permissions include (but are not limited to) `dynamodb:PutItem`, `dynamodb:BatchWriteItem`, `dynamodb:CreateTable`, and `dynamodb:DeleteTable`. A full list of required DynamoDB actions is provided in the source documentation. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

To use instance profile authentication for publishing:

1. Create an IAM [instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) with the required write permissions to the online store.
2. Add the instance profile to Databricks and attach it to a cluster.
3. Use that cluster to run the code that publishes to the online store.

No explicit secret credentials or `write_secret_prefix` are required in the [online store spec](/concepts/onlinestoreconfig.md) when the cluster carries the correct instance profile. This method works on clusters running Databricks Runtime 10.5 ML and above. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Read Authentication for Looking Up Features from Served Models

To allow Databricks-hosted MLflow models served via a Serving Endpoint to look up feature values from a third-party online store, you configure the serving endpoint with an instance profile that has read-only access to the store.

1. Create an IAM instance profile with the necessary read permissions (e.g., `dynamodb:GetItem`, `dynamodb:Query`).
2. Configure the serving endpoint to use that instance profile. See [Add model serving instance profile](/concepts/model-serving-instance-profile.md) for details.

When you publish the feature table to the online store, any `read_prefix` you might have set is overridden by the instance profile. You do not need to specify `read_secret_prefix`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Alternative: Databricks Secrets

If instance profiles are not suitable for your use case, you can provide authentication credentials using Databricks Secrets. This involves creating separate secret scopes and keys for read and write access, and referencing them in the `read_secret_prefix` or `write_secret_prefix` parameters when publishing. The source document details the exact naming conventions for DynamoDB and SQL store secrets. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Related Concepts

- [Feature Store](/concepts/feature-store.md) — Core concept for managing and serving features
- [DynamoDB Online Store](/concepts/amazon-dynamodb-online-store-integration.md) — Example third-party online store
- Databricks Secrets — Alternative credential management approach
- Serving Endpoint — Model serving infrastructure that can use instance profiles
- Instance Profile — AWS IAM role attached to compute resources

### Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
