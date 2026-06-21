---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 828a075a583c03ff01d2a4609571aae00dfadca018ddd83a2683d6699648ba5d
  pageDirectory: concepts
  sources:
    - multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-secrets-for-ml-model-credentials
    - DSFMMC
  citations:
    - file: multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Secrets for ML Model Credentials
description: A pattern for securely injecting Hugging Face access tokens (or other sensitive credentials) into distributed training workloads by storing them as Databricks secrets and referencing them in the workload YAML rather than hard-coding them in scripts.
tags:
  - security
  - mlops
  - databricks
timestamp: "2026-06-19T19:48:51.142Z"
---

# Databricks Secrets for ML Model Credentials

**Databricks Secrets for ML Model Credentials** provides a secure mechanism for storing and accessing sensitive authentication tokens, API keys, and other credentials needed by machine learning workloads — such as model download tokens from Hugging Face or external API keys. By using Databricks Secrets instead of hard-coding credentials in source code or configuration files, ML pipelines can securely access gated models, external services, and private datasets without exposing sensitive information.

## Overview

Machine learning workflows often require credentials to access external resources. Common examples include Hugging Face access tokens for downloading gated models, cloud storage API keys for reading training data, or authentication tokens for external inference endpoints. Databricks Secrets allow users and service principals to store these credentials securely in an encrypted secret scope and reference them from ML code, notebooks, and workload configurations. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Use Cases

### Hugging Face Token for Model Access

Gated models on Hugging Face — such as Llama-3.1-8B — require an access token with read permission to download. Rather than embedding the token in Python code or environment variables, you can store it as a Databricks secret and inject it into the workload at runtime. This pattern is demonstrated in multi-node LLM fine-tuning examples on Databricks. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Credentials for MLflow Serverless Workloads

When MLflow creates serverless workloads (scheduled scorers, synthetic evaluation set generation, agent evaluation) for an experiment, those workloads may need credentials to access external resources. [Serverless budget policies](/concepts/serverless-budget-policy.md) can also be assigned to experiments to control spending, but the underlying credential access still uses the Databricks Secrets framework. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Creating and Managing Secrets

### Create a Secret Scope

Use the Databricks CLI `databricks secrets` command to create a secret scope and store secrets within it:

```bash
databricks secrets create-scope my_scope
databricks secrets put-secret my_scope hf_token
```

Replace `my_scope` with the desired scope name and `hf_token` with the key name for your credential. Scopes can be scoped to a workspace or to a specific user/service principal. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Referencing Secrets in Workload Configurations

In the [AI Runtime CLI](/concepts/ai-runtime-cli.md) [Workload YAML Configuration](/concepts/workload-yaml-configuration.md), secrets are declared under a `secrets:` block. Each secret maps an environment variable name to a reference in the form `scope/key`:

```yaml
secrets:
  HF_TOKEN: 'my_scope/hf_token'
```

At runtime, the AI Runtime automatically resolves the secret and sets the environment variable `HF_TOKEN` to its value. The training script can then use `os.environ.get("HF_TOKEN")` to read the token without ever seeing the raw secret in source files or logs. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

### Referencing Secrets in Notebooks and Python Code

In notebooks or Python scripts running on Databricks, you can retrieve secrets programmatically using the `dbutils.secrets` module:

```python
hf_token = dbutils.secrets.get(scope="my_scope", key="hf_token")
```

This approach keeps secrets out of notebooks stored in version control and allows authorized users to access only the scopes they have permission to read. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Best Practices

- **Use secret scopes**: Always store credentials in Databricks Secrets rather than hard-coding them in YAML files, Python scripts, or notebooks. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **Scope access appropriately**: Create separate secret scopes for different teams or applications, and grant access only to users and service principals that need the credentials. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **Rotate secrets regularly**: Periodically update stored tokens (e.g., regenerate Hugging Face access tokens) and replace the corresponding secret value using the CLI or Databricks UI. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **Avoid secret exposure in logs**: Ensure that logging code does not print environment variables that contain secret values. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets — The core secrets management service on the Databricks platform
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — Command-line tool used to launch workload configurations that reference secrets
- Hugging Face Model Access — Gated models that require authentication tokens stored as secrets
- [Multi-Node LLM Fine-Tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — Distributed training workloads that commonly use secrets for model download
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Experiments with serverless workloads that may need credentials for external services
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Policy control for serverless workloads separate from credential management

## Sources

- multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md](/references/multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws-d26ca320.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
