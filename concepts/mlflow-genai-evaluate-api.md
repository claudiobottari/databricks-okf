---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0de61f6227c2e59423aec23b73ad50807ee261c971e225a27797c649d212cd89
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluate-api
    - MGEA
    - MLflow Evaluate API
    - GenAI
    - MLflow Evaluate
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: arize-phoenix-scorers-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow GenAI Evaluate API
description: The mlflow.genai.evaluate() API for running evaluation datasets through multiple scorers including third-party integrations like Phoenix
tags:
  - mlflow
  - evaluation
  - llm
timestamp: "2026-06-19T17:35:34.211Z"
---

---
title: MLflow GenAI Evaluate API
summary: The `mlflow.genai.evaluate()` function that orchestrates evaluation of LLM outputs using configurable scorers on a dataset with inputs, outputs, and expectations.
sources:
  - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  - arize-phoenix-scorers-databricks-on-aws.md
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:03:42.616Z"
updatedAt: "2026-06-19T14:03:42.616Z"
tags:
  - mlflow
  - genai
  - evaluation
aliases:
  - mlflow-genai-evaluate-api
  - MGEA
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

## MLflow GenAI Evaluate API

The **MLflow GenAI Evaluate API** — exposed as `mlflow.genai.evaluate()` — is the primary interface for offline evaluation of GenAI agent responses. It runs a set of [judges](/concepts/llm-judges.md) (LLM-based scorers) against a provided evaluation dataset, optionally calling a user-defined prediction function (`predict_fn`) to generate outputs on the fly. The API supports both input/output judges and [trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md), and works with built-in, custom, or third-party scorers such as [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, arize-phoenix-scorers-databricks-on-aws.md]

### Parameters

The API accepts the following key parameters:

| Parameter | Description |
|-----------|-------------|
| `data` | An evaluation dataset. Each record typically contains `inputs` (the conversation history or prompt), optional `outputs` (if pre‑generated), and optional `expectations` that judges can reference. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, arize-phoenix-scorers-databricks-on-aws.md] |
| `predict_fn` | A callable that takes an input record and returns the agent’s response. When provided, `outputs` do not need to be pre‑computed; the function is invoked per record. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md] |
| `scorers` | A list of judge objects (e.g., created via make_judge() or from third‑party libraries like Arize Phoenix). Each judge scores the output against defined quality criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, arize-phoenix-scorers-databricks-on-aws.md] |

### Usage Patterns

#### Offline Evaluation with Pre‑computed Outputs

When `outputs` are already available in the dataset, call `evaluate()` without a `predict_fn`. This is common when replaying logged production traces:

```python
eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform...",
        "expectations": {"context": "MLflow is an ML platform..."}
    }
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ]
)
```

^[arize-phoenix-scorers-databricks-on-aws.md]

#### Evaluation with a Prediction Function

When the agent logic is available as a callable, pass it as `predict_fn`. The API invokes the function for each row and then runs the scorers on the outputs:

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[issue_resolution_judge, expected_behaviors_judge]
)
```

#### A/B Comparison

By calling `evaluate()` multiple times with the same dataset and scorers but different `predict_fn` (or different agent configurations), developers can compare quality scores across variants. See [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

#### Custom Judges

Judges created with make_judge() can include `{{ trace }}` to enable trace‑based evaluation, which inspects tool calls and intermediate reasoning. The `{{ expectations }}` placeholder allows judges to reference ground‑truth data supplied in the dataset. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Serverless Workloads

When `mlflow.genai.evaluate()` triggers a serverless workload (e.g., for synthetic evaluation set generation or agent evaluation), the experiment must have a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) assigned. If the workspace’s default policy is disabled and no policy is set on the experiment, the API may return a `403 PERMISSION_DENIED` error. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Related Concepts

- make_judge() — API for creating custom LLM‑based judges.
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) — Pre‑built judges for hallucination and relevance.
- [Trace‑Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost control for evaluation workloads.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing variants with `evaluate()`.

### Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- arize-phoenix-scorers-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
2. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
