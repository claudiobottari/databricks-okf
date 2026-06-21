---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 228152f9aa3ac4447f7e2a9a27843a92a97c797d912232bfa4dc3d5ef385793f
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - accessing-databricks-secrets-in-scorers
    - ADSIS
    - Use Databricks secrets|Use Databricks secrets
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Accessing Databricks secrets in scorers
description: Custom scorers can securely use Databricks secrets by importing dbutils from databricks.sdk.runtime inside the scorer function.
tags:
  - mlflow
  - scoring
  - secrets
  - security
timestamp: "2026-06-19T17:44:31.693Z"
---

# Accessing Databricks secrets in scorers

**Accessing Databricks secrets in scorers** refers to the mechanism by which custom [Code-based Scorers](/concepts/code-based-scorers.md) can securely retrieve API keys, credentials, and other sensitive values stored in the Databricks secret store. This allows scorers to integrate with external services—such as custom LLM endpoints like Azure OpenAI or AWS Bedrock—without hard‑coding secrets in source code. ^[code-based-scorer-reference-databricks-on-aws.md]

## How to access secrets

By default, `dbutils` is not available in the scorer runtime environment. To access secrets, you must explicitly import the runtime module from inside the scorer function: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from databricks.sdk.runtime import dbutils
```

Once imported, you can retrieve a secret using the standard Databricks secrets API: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
api_key = dbutils.secrets.get(scope='my-scope', key='api-key')
```

The secret can then be used in your custom evaluation logic—for example, to authenticate when calling an external LLM judge endpoint. ^[code-based-scorer-reference-databricks-on-aws.md]

## Example

The following complete example shows a custom scorer that retrieves an API key from Databricks secrets and uses it to evaluate a trace: ^[code-based-scorer-reference-databricks-on-aws.md]

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
custom_llm_scorer.start(sampling_config = ScorerSamplingConfig(sample_rate=1))
```

This approach works for both MLflow evaluation|development evaluation (using `mlflow.genai.evaluate()`) and [Production Monitoring](/concepts/production-monitoring.md) with registered scorers. ^[code-based-scorer-reference-databricks-on-aws.md]

## Usage scenarios

Accessing secrets is particularly useful when your scorer calls an external evaluation endpoint that requires authentication. Common use cases include:

- Scoring responses using a third‑party LLM API (e.g., Anthropic, OpenAI, Bedrock).
- Querying an internal model serving endpoint that is secured with an API token.
- Fetching credentials for a vector database or other information retrieval system used during evaluation.

Because the secret access pattern is identical for both evaluation and monitoring, you can develop and test scorers locally and then deploy them to production without changing the secret retrieval code. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Databricks secrets](/concepts/databricks-secret-scopes.md) — The secure storage service for sensitive data
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions for MLflow GenAI
- Feedback (MLflow) — The structured output object for scorer results
- [Scorer class](/concepts/scorer-class.md) — Alternative method for defining scorers (not recommended for production monitoring)
- [Production Monitoring](/concepts/production-monitoring.md) — Using registered scorers in the inference table pipeline
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
