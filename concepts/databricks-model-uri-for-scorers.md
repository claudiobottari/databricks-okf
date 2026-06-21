---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 113b55cfb577a787a79d08e72bcfdefd53a7dd31a09820daffe2be03bad610db
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-model-uri-for-scorers
    - DMUFS
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Model URI for Scorers
description: The use of databricks:/ model URIs (e.g., databricks:/databricks-gpt-5-mini) to specify LLM judge models for Phoenix scorers within Databricks-managed MLflow environments.
tags:
  - databricks
  - model-uri
  - mlflow
timestamp: "2026-06-19T14:03:59.930Z"
---

# Databricks Model URI for Scorers

**Databricks Model URI for Scorers** refers to the uniform resource identifier pattern used to specify a Databricks-hosted foundation model when configuring scoring components in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). Scorers such as built-in quality judges, custom judges created with `make_judge()`, and third-party scorers like Arize Phoenix accept a `model` parameter that points to a model served via Databricks Model Serving.

## Format

The URI follows the pattern `databricks:/<model-name>`, where `<model-name>` is the serving endpoint name of a foundation model deployed in the Databricks workspace. The prefix `databricks:/` signals to MLflow that the model should be resolved through Databricks’ internal model registry and serving infrastructure. ^[arize-phoenix-scorers-databricks-on-aws.md] (via example), ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md] (via example)

For example, the URI `databricks:/databricks-gpt-5-mini` refers to the Databricks-hosted GPT-5 Mini model, which is commonly used as a judge model for evaluating agent outputs.

## Usage

Scorers that require an LLM to evaluate outputs accept a `model` argument that is set to a Databricks Model URI. This URI tells the scorer which model endpoint to call for each evaluation request.

### Built-in Scorers (Arize Phoenix)

When using Phoenix scorers like `Hallucination` or `Relevance`, the model URI is passed directly in the scorer constructor: ^[arize-phoenix-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.phoenix import Hallucination, Relevance

scorer = Hallucination(model="databricks:/databricks-gpt-5-mini")
```

### Custom Judges (`make_judge`)

The same URI pattern is used with the `make_judge()` function to create a [custom judge](/concepts/custom-judges.md). The model is provided as a keyword argument; the judge then calls that model for every evaluation request. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
from mlflow.genai import make_judge

judge = make_judge(
    name="tool_call_correctness",
    instructions=...,
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

Trace-based judges also require a model specification using the same URI format because they need an LLM to interpret the execution trace. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Model Requirements

The model identified by the URI must be deployed and accessible in the workspace. Users and service principals calling the scorer must have appropriate permissions to query the model endpoint. The model should be capable of following the scoring instructions — typically a powerful instruction-tuned LLM that can assess outputs reliably.

## Relationship to Serverless Budget Policies

When a scorer runs a serverless workload (e.g., when evaluating batches of data), MLflow may need a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) assigned to the experiment to function. The 403 PERMISSION_DENIED error can occur if the workspace has disabled the default budget policy and no fallback is available. See 403 PERMISSION_DENIED Serverless Budget Policy Error for details and resolution steps. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Inference

The Databricks Model URI for scorers is analogous to the model URIs used elsewhere in MLflow (e.g., for model registry references), but uses the `databricks:/` scheme specifically to route through Databricks Model Serving. This allows scorers to use models that are not loaded directly into the notebook environment, reducing resource consumption and centralizing model access.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework in which scorers are used.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based evaluators defined with `make_judge()`.
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) — Pre-built scoring components for hallucination, relevance, and other metrics.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — The infrastructure that hosts the models referenced by the URI.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls spending for serverless workloads triggered by scorers.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md (code examples)
- create-a-custom-judge-using-make_judge-databricks-on-aws.md (code examples, trace-based judge model requirement)
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md (budget policy context)

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
