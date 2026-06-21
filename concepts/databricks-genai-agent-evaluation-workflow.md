---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 495b249e7d7a02e1eaca8135cea0200066d38770ce85153a6b1989f9f36fb6a3
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-genai-agent-evaluation-workflow
    - DGAEW
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks GenAI Agent Evaluation Workflow
description: End-to-end workflow for evaluating GenAI agents on Databricks, including creating agents, defining judges, building datasets, and running evaluations.
tags:
  - Databricks
  - MLflow
  - GenAI
  - evaluation
timestamp: "2026-06-19T17:55:12.608Z"
---

# Databricks GenAI Agent Evaluation Workflow

The **Databricks GenAI Agent Evaluation Workflow** is a structured process for assessing the quality, correctness, and behavior of generative AI agents. Built on [MLflow GenAI](/concepts/mlflow-3-for-genai.md), the workflow uses [[scorers]] – including LLM-based Custom Judges (make_judge)|custom judge|custom judges – to evaluate agent outputs against defined criteria. It supports iterative comparison of different agent configurations and can be extended to production monitoring. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Prerequisites and Environment Setup

Before running evaluations, the environment must be configured. MLflow must be set to track experiments on Databricks (`mlflow.set_tracking_uri("databricks")`), and a target experiment must be specified. If serverless workloads are used for evaluation (e.g., for synthetic evaluation set generation or agent evaluation), a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) must be assigned to the experiment to avoid a `403 PERMISSION_DENIED` error. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md] ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Step 1: Define the Agent to Evaluate

The agent is typically defined as a Python function or callable that accepts a list of messages (conversation history) and returns an assistant response. [OpenAI autologging](/concepts/mlflow-openai-autolog.md) (`mlflow.openai.autolog()`) can be used to automatically trace LLM calls. Tools (e.g., mock APIs for pricing or return policies) can be annotated with `@mlflow.trace` to capture their execution in the evaluation trace. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

A common pattern is to include a global toggle that changes the agent’s behavior (e.g., whether it attempts to resolve issues), allowing comparison across evaluations. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Step 2: Define Scorers (Custom Judges)

Scorers are the evaluation functions applied to each sample. The primary method for creating a custom LLM-based judge is `make_judge()`, which returns an `mlflow.entities.Feedback` object. A judge is defined by:
- A **name** (e.g., `"issue_resolution"`).
- **Instructions** that describe what the judge should evaluate, often using placeholders `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, and `{{ trace }}`.
- A **feedback_value_type**, which can be a `Literal` of strings, a `bool`, or another type.

If `{{ trace }}` is included in the instructions, the judge becomes **trace-based** and can autonomously explore the execution trace to assess tool usage. A trace-based judge requires a specific model (e.g., `"databricks:/databricks-gpt-5-mini"`). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Multiple judges can be defined to evaluate different criteria, such as issue resolution, expected behaviors, and tool call correctness. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Step 3: Create an Evaluation Dataset

The dataset is a list of dictionaries, each containing:
- `"inputs"`: A dictionary with a `"messages"` key that holds the conversation history (list of role/content dicts).
- Optionally, `"expectations"`: A dictionary of expected behaviors (e.g., `{"should_provide_pricing": True}`). Expectations are used by the judge to compare against the agent’s output.

The dataset is passed as the `data` argument to `mlflow.genai.evaluate()`. The agent function is called once per sample. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Step 4: Run the Evaluation

The evaluation is performed with `mlflow.genai.evaluate()`, which accepts:
- `data`: the evaluation dataset.
- `predict_fn`: the agent function.
- `scorers`: a list of judge objects.

The function executes the agent on each sample, applies the scorers to the inputs, outputs, and traces, and logs results to the current MLflow experiment. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

To compare different agent behaviors, the evaluation can be run multiple times with different configurations (e.g., toggling `RESOLVE_ISSUES`) and the results can be reviewed side by side. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Step 5: Analyze Results

Each judge returns a rating for every sample. For example:
- A judge named `"issue_resolution"` returns `"fully_resolved"`, `"partially_resolved"`, or `"needs_follow_up"`.
- A judge named `"expected_behaviors"` returns `"meets_expectations"`, `"partially_meets"`, or `"does_not_meet"`.
- A trace-based judge named `"tool_call_correctness"` returns a boolean.

By comparing the results across configurations, developers can identify which agent version performs better on each criterion. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Next Steps: Production Monitoring and Judge Alignment

The evaluation workflow can be extended to continuous production monitoring. Custom judges can be deployed as [[scorers]] that run on production inference logs. To improve judge accuracy, Databricks recommends aligning judges with human feedback using the align judges workflow – the base judge is a starting point, and expert feedback on agent outputs can be used to fine-tune the judge’s instructions. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judge](/concepts/custom-judges.md) – LLM-based scorer created with `make_judge()`.
- [Trace](/concepts/traces.md) – Execution history used by trace-based judges.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The broader framework for evaluating generative AI applications.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Required policy assignment to avoid permission errors during evaluation.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Applying evaluation judges to live agent traffic.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
