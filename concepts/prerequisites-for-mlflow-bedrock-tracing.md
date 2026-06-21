---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c84d95e5ec0b9033b773194867498ac2bc3c73f4b9767250047e44eb0eded8df
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-mlflow-bedrock-tracing
    - PFMBT
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
title: Prerequisites for MLflow Bedrock Tracing
description: Using MLflow tracing with Amazon Bedrock requires installing mlflow[databricks]>=3.1 and boto3, configuring Databricks credentials (DATABRICKS_HOST, DATABRICKS_TOKEN), and configuring AWS credentials for Bedrock access.
tags:
  - mlflow
  - setup
  - bedrock
  - aws
timestamp: "2026-06-19T23:08:59.392Z"
---

# Prerequisites for [MLflow](/concepts/mlflow.md) Bedrock Tracing

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Amazon Bedrock, you must meet several prerequisites covering software installation and environment configuration. The following sections outline the required dependencies and setup steps.

## Software Requirements

You need to install [MLflow](/concepts/mlflow.md) (with Databricks extras) and the **AWS SDK for Python (Boto3)**. For development and experimentation on Databricks, install the full [MLflow](/concepts/mlflow.md) package along with Boto3: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" boto3
```

**MLflow 3** is highly recommended for the best tracing experience with Amazon Bedrock. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Environment Configuration

### Databricks Environment

- **Inside a Databricks notebook**: Credentials (host and token) are automatically set. No manual configuration is needed. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **Outside a Databricks notebook**: You must set the following environment variables: ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

  ```bash
  export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
  export DATABRICKS_TOKEN="your-personal-access-token"
  ```

### AWS Credentials

Your environment must have valid AWS credentials configured so that Boto3 can access the Bedrock API. For production use, consider using IAM roles, [AWS Secrets Manager](/concepts/accessing-secrets-in-scorers.md), or [Databricks secrets](/concepts/databricks-secret-scopes.md) instead of plain environment variables. Common methods include using the AWS CLI (`aws configure`), IAM roles, or environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_DEFAULT_REGION`). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Additional Considerations

- **Explicitly enable autologging**: On [serverless compute clusters](/concepts/serverless-gpu-compute-databricks.md), autologging is **not** automatically enabled. You must explicitly call `mlflow.bedrock.autolog()` to turn on [Automatic Tracing](/concepts/automatic-tracing.md) for Amazon Bedrock calls. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

- **Supported APIs**: Once prerequisites are met, [MLflow](/concepts/mlflow.md) will automatically trace calls to the Bedrock runtime APIs (`converse`, `converse_stream`, `invoke_model`, `invoke_model_with_response_stream`). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Automatic trace capture for LLM invocations.
- Amazon Bedrock – AWS managed service for foundation models.
- Boto3 – AWS SDK for Python.
- Serverless Compute – Databricks compute environment requiring explicit autolog.
- Databricks Secrets – Secure API key management option.

## Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
