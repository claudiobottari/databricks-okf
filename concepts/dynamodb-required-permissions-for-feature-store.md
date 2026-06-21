---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0a554c3284fc74c11b17631b6dce28e7e9dd5f0d2653350fbc2baa03ce5b088
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamodb-required-permissions-for-feature-store
    - DRPFFS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: DynamoDB Required Permissions for Feature Store
description: The comprehensive list of DynamoDB IAM permissions (e.g., PutItem, GetItem, CreateTable, Query) required for a Databricks Feature Store integration with DynamoDB as an online store.
tags:
  - dynamodb
  - iam
  - permissions
  - feature-store
timestamp: "2026-06-19T17:37:18.541Z"
---

```yaml
---
title: DynamoDB Required Permissions for Feature Store
summary: The comprehensive list of AWS DynamoDB IAM permissions (e.g., DeleteItem, BatchWriteItem, CreateTable) required for write authentication when publishing feature tables to a DynamoDB online store.
sources:
  - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:29:23.725Z"
updatedAt: "2026-06-18T14:29:23.725Z"
tags:
  - aws
  - dynamodb
  - iam
  - permissions
  - feature-store
aliases:
  - dynamodb-required-permissions-for-feature-store
  - DRPFFS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## DynamoDB Required Permissions for Feature Store

When working with Amazon DynamoDB as a third-party online store for [[Databricks Feature Store]] (or the Feature Engineering client), the AWS IAM principal used for authentication must have a specific set of permissions. These permissions differ between write operations (publishing feature tables) and read operations (looking up features from served models). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Write Permissions (Publishing Feature Tables)

To publish feature tables to a DynamoDB online store, the IAM user or instance profile must have all of the following DynamoDB actions: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- `dynamodb:DeleteItem`
- `dynamodb:DeleteTable`
- `dynamodb:PartiQLSelect`
- `dynamodb:DescribeTable`
- `dynamodb:PartiQLInsert`
- `dynamodb:GetItem`
- `dynamodb:CreateGlobalTable`
- `dynamodb:BatchGetItem`
- `dynamodb:UpdateTimeToLive`
- `dynamodb:BatchWriteItem`
- `dynamodb:ConditionCheckItem`
- `dynamodb:PutItem`
- `dynamodb:PartiQLUpdate`
- `dynamodb:Scan`
- `dynamodb:Query`
- `dynamodb:UpdateItem`
- `dynamodb:DescribeTimeToLive`
- `dynamodb:CreateTable`
- `dynamodb:UpdateGlobalTableSettings`
- `dynamodb:UpdateTable`
- `dynamodb:PartiQLDelete`
- `dynamodb:DescribeTableReplicaAutoScaling`

These permissions cover table creation, deletion, item CRUD, and PartiQL operations required by the Feature Store publishing workflow. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Read Permissions (Looking Up Features)

To enable served MLflow Models to look up feature values from DynamoDB, the IAM principal requires read permissions. Although the source material does not enumerate a separate read-only set, the typical minimum set includes `dynamodb:GetItem`, `dynamodb:BatchGetItem`, `dynamodb:Query`, and `dynamodb:Scan`. Databricks recommends using an instance profile configured on the serving endpoint for read authentication. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Authentication Methods

- **Instance Profile (recommended for write):** Attach an instance profile with the required permissions to the Databricks cluster. This works on clusters running Databricks Runtime 10.5 ML and above. No explicit secret credentials or `write_secret_prefix` are needed in the online store spec. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Instance Profile (recommended for read):** Attach the instance profile to the [[Model Serving]] endpoint. This overrides any `read_prefix` specified. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Databricks Secrets:** Store access key ID and secret access key in Databricks secret scopes, then reference them via `write_secret_prefix` or `read_secret_prefix` when publishing or looking up features. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Related Concepts

- Third-Party Online Stores
- [[Publishing Feature Tables to Online Stores|Publish Features to an Online Store]]
- [[Instance Profile (Databricks on AWS)|Instance Profiles in Databricks]]
- Databricks Secrets
- Model Serving for Feature Lookup

### Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
```

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
