---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5e3f9a569ab8707037247e7c43918c67d6ff96a039797bd16aa34ba005a9661
  pageDirectory: concepts
  sources:
    - safety-judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - production-safety-monitoring
    - PSM
    - Production Quality Monitoring
    - Production quality monitoring
    - production quality monitoring
  citations:
    - file: safety-judge-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Production Safety Monitoring
description: Continuous monitoring of safety for deployed AI applications, set up using MLflow's production monitoring capabilities to track safety evaluations over time.
tags:
  - monitoring
  - safety
  - mlflow
  - production
timestamp: "2026-06-19T20:18:35.956Z"
---

# Production Safety Monitoring

**Production Safety Monitoring** refers to the continuous evaluation of deployed AI model outputs for harmful, offensive, or inappropriate content in real-time or near-real-time. It is a critical component of responsible AI deployment, ensuring that models operating in production environments do not generate unsafe responses for end users.

## Overview

Production Safety Monitoring uses automated judges—LLM-based evaluation models—to assess the safety of model outputs as they are served in production. These judges analyze text content and provide a pass/fail assessment along with a detailed rationale explaining any safety concerns.^[safety-judge-databricks-on-aws.md]

The primary tool for implementing production safety monitoring is the [Safety judge](/concepts/safety-judge-mlflow.md), a built-in judge that evaluates text content for potentially harmful material. This judge can be invoked directly for single assessments or integrated with MLflow's evaluation framework for batch evaluation.^[safety-judge-databricks-on-aws.md]

## Key Components

### Safety Judge

The `Safety` judge evaluates text content to identify potentially harmful, offensive, or inappropriate material. It returns a pass/fail assessment along with a detailed rationale explaining any safety concerns.^[safety-judge-databricks-on-aws.md]

The judge is invoked using the `Safety` class from `mlflow.genai.scorers`. By default, it uses a Databricks-hosted LLM designed for GenAI quality assessments. The judge model can be customized by specifying a different model using the `model` argument in the format `<provider>:/<model-name>`.^[safety-judge-databricks-on-aws.md]

### Scheduled Scorers

For continuous production monitoring, scheduled scorers are used to automatically evaluate model outputs at regular intervals. These scorers may be affected by [Serverless Budget Policy](/concepts/serverless-budget-policy.md) configurations—if the workspace disables the default serverless budget policy and no fallback policy is assigned, scheduled scorers fail with a 403 PERMISSION_DENIED error.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Implementation

### Prerequisites

To implement production safety monitoring, you need:

1. MLflow and required packages installed (`mlflow[databricks]>=3.4.0`)
2. An MLflow experiment set up following the environment setup quickstart

### Basic Implementation

The Safety judge can be invoked directly for single assessments:^[safety-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety

assessment = Safety(
    outputs="Your model output text to evaluate for safety."
)
```

For batch evaluation, the judge is used with `mlflow.genai.evaluate()` as a scorer.^[safety-judge-databricks-on-aws.md]

### Customizing the Judge Model

You can change the judge model to use a different LLM for safety evaluations:^[safety-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety(
    model="databricks:/databricks-claude-opus-4-5"
)

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[safety_judge]
)
```

## Budget Policy Considerations

Production monitoring workflows that use scheduled scorers require proper configuration of [Serverless Budget Policy](/concepts/serverless-budget-policy.md). If the workspace disables the default serverless budget policy and no alternative policy is assigned to the experiment, scheduled scorers fail with the following error:^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

To resolve this, set a serverless budget policy on the MLflow experiment by either:^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

- Setting the **Budget policy** in the experiment's **Details** panel in the UI, or
- Using the API to set the `mlflow.workload_creation_policy_id` tag on the experiment

## Best Practices

- **Monitor continuously**: Set up scheduled scorers to evaluate safety at regular intervals appropriate for your use case.^[safety-judge-databricks-on-aws.md]
- **Customize guidelines for your domain**: Use the [Guidelines judge](/concepts/guidelines-llm-judge.md) to define specific safety criteria tailored to your application's context.^[safety-judge-databricks-on-aws.md]
- **Select the right judge model**: Choose a judge model that balances evaluation quality with latency and cost requirements for your production workload.^[safety-judge-databricks-on-aws.md]
- **Ensure proper budget policy configuration**: Verify that serverless budget policies are correctly set to avoid scheduled evaluation failures.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Safety judge](/concepts/safety-judge-mlflow.md) — The built-in judge for evaluating text content safety
- [Guidelines judge](/concepts/guidelines-llm-judge.md) — For creating custom safety criteria
- [Production Monitoring](/concepts/production-monitoring.md) — Broader monitoring framework for deployed models
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls spending for serverless workloads including scheduled scorers
- 403 PERMISSION_DENIED Serverless Budget Policy Error — Troubleshooting budget policy failures
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow that may use safety judges
- [MLflow experiments](/concepts/mlflow-experiment.md) — Organizational unit for MLflow runs and evaluations

## Sources

- safety-judge-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [safety-judge-databricks-on-aws.md](/references/safety-judge-databricks-on-aws-d841b2a4.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
