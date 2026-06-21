---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b706a5242127a2b30cdf4796b7dc75494ee73f502299aa4a8cbb4e6afd535bf
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - accessing-secrets-in-scorers
    - ASIS
    - AWS Secrets Manager
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Accessing secrets in scorers
description: How to securely use Databricks secrets within custom scorers by importing dbutils from databricks.sdk.runtime.
tags:
  - mlflow
  - security
  - secrets
timestamp: "2026-06-18T14:37:01.174Z"
---

# Accessing secrets in scorers

**Accessing secrets in scorers** describes how [custom code-based scorers](/concepts/code-based-scorers.md) can securely retrieve Databricks Secrets — such as API keys and credentials — to integrate external services during evaluation or monitoring of GenAI agents. This mechanism supports both development evaluation and [Production Monitoring](/concepts/production-monitoring.md) workflows. ^[code-based-scorer-reference-databricks-on-aws.md]

## Why access secrets in scorers

Scorers often need to call external LLM endpoints (e.g., Azure OpenAI, AWS Bedrock) or authenticated APIs to evaluate response quality. Hardcoding credentials is insecure and impractical. By retrieving secrets from Databricks Secrets at runtime, scorers can authenticate without exposing sensitive values in source code or configuration files. ^[code-based-scorer-reference-databricks-on-aws.md]

## How to access secrets

By default, `dbutils` is **not available** in the scorer runtime environment. To access Databricks Secrets inside a scorer, explicitly import `dbutils` from `databricks.sdk.runtime` within the scorer function body. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import scorer, ScorerSamplingConfig
from mlflow.entities import Trace, Feedback

@scorer
def custom_llm_scorer(trace: Trace) -> Feedback:
    # Explicitly import dbutils to access secrets
    from databricks.sdk.runtime import dbutils

    # Retrieve your API key from Databricks secrets
    api_key = dbutils.secrets.get(scope='my-scope', key='api-key')

    # Use the API key to call your custom LLM endpoint
    # ... your custom evaluation logic here ...

    return Feedback(
        value="yes",
        rationale="Evaluation completed using custom endpoint"
    )

# Register and start the scorer
custom_llm_scorer.register()
custom_llm_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=1))
```

The same approach works whether the scorer is used with [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) during development or as a registered scorer for production monitoring. ^[code-based-scorer-reference-databricks-on-aws.md]

## Best practices

- Import `dbutils` **inside** the scorer function (not at module level) to avoid import-order issues in the managed environment. ^[code-based-scorer-reference-databricks-on-aws.md]
- Store API keys in Databricks Secrets scopes with appropriate access controls, and reference them by scope name and key. ^[code-based-scorer-reference-databricks-on-aws.md]
- For production monitoring, ensure that the service principal or user running the scorer has `READ` permission on the secret scope. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related Concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md)
- Databricks Secrets
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- [@scorer decorator](/concepts/scorer-decorator.md)
- [Scorer class](/concepts/scorer-class.md)
- [Error handling in scorers](/concepts/error-handling-in-scorers.md)

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
