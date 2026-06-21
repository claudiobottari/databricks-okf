---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a803f0dc0a03ab173dd929db5eaf9b0422bb01a96c0d0c257bfa13a2ac44d1b6
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-judge-evaluation
    - MJE
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Multiple Judge Evaluation
description: Using multiple custom judges together to evaluate different aspects of a GenAI agent simultaneously within a single evaluation run.
tags:
  - MLflow
  - GenAI
  - evaluation
timestamp: "2026-06-19T17:54:44.631Z"
---

# Multiple Judge Evaluation

**Multiple Judge Evaluation** is a technique in [GenAI evaluation](/concepts/mlflow-genai-evaluation.md) where several [LLM-as-judge|LLM-based judges](/concepts/llm-as-a-judge-paradigm.md) are combined in a single evaluation run to assess different quality criteria of a generative AI application simultaneously. Each judge is a custom scorer created with make_judge() that returns an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How It Works

Multiple judges are passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`. During evaluation, each judge independently analyzes the same input-output pairs (or execution [traces](/concepts/mlflow-tracing.md)) and produces a rating or classification according to its own instructions. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

For example, a single evaluation can include:
- An **issue resolution judge** that rates conversations as `fully_resolved`, `partially_resolved`, or `needs_follow_up`.
- An **expected behaviors judge** that checks whether responses meet predefined expectations (`meets_expectations`, `partially_meets`, `does_not_meet`).
- A **trace-based judge** that validates tool usage by analyzing the execution trace (returns `true` or `false`).

All judges run in the same evaluation call, and the results panel shows how each judge rates the agent for every test case. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Benefits

Using multiple judges together provides a more comprehensive assessment of agent quality than a single judge alone. It enables comparing performance across different criteria (e.g., resolution quality, behavioral correctness, tool call accuracy) within one experiment, making it easier to identify tradeoffs and areas for improvement. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- make_judge() – The API used to define custom judges.
- [Trace-based judge](/concepts/trace-based-judges.md) – A judge that includes `{{ trace }}` in its instructions to analyze execution traces.
- Align judges with human feedback – A process to improve judge accuracy after initial evaluation.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying custom judges for continuous quality monitoring.
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) – The broader framework that supports multiple judge evaluation.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
