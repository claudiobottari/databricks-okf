---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f893904716bfb825f5f0328725c4a41691dade3ff540e50aa29d66b8ec2a7160
  pageDirectory: concepts
  sources:
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-based-scorers
    - Code-based Scorer
    - Code-based scorer
    - Code‑Based Scorers
    - Code‑based scorers
    - Custom (Code-Based) Scorers
    - Custom Code-Based Scorers
    - Custom Code-based Scorers
    - Custom code-based scorers
    - Custom code‑based scorers
    - Python code-based scorers
    - code-based scorer
    - code‑based scorers
    - custom code-based scorers
    - custom code‑based scorers
    - model-based scorers
    - Code-Based Scorer Examples
    - Code-based scorer examples
    - Python code-based scorer
    - code-based scorer examples
  citations:
    - file: scorers-and-llm-judges-databricks-on-aws.md
title: Code-based Scorers
description: Custom programmatic scorers offering maximum flexibility for defining evaluation metrics through heuristics, advanced logic, or custom LLM integration beyond what custom judges provide.
tags:
  - mlflow
  - custom-scoring
  - programmatic-evaluation
timestamp: "2026-06-19T20:19:57.240Z"
---

# Code-based Scorers

**Code-based scorers** are a type of [Scorer] in the MLflow GenAI evaluation framework that allow users to define evaluation logic through custom Python code. They provide the highest level of flexibility and control for measuring the quality of GenAI applications, models, and agents. ^[scorers-and-llm-judges-databricks-on-aws.md]

## How scorers work

Every scorer — whether built-in, custom LLM judge, or code-based — follows the same fundamental workflow. A scorer receives a [Trace] from either `evaluate()` or the production monitoring service. It then:

1. Parses the trace to extract specific fields and data used to assess quality  
2. Runs the scorer logic to perform the quality assessment  
3. Returns the quality assessment as [`Feedback`](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations) to attach to the trace  

^[scorers-and-llm-judges-databricks-on-aws.md]

Code-based scorers implement this interface using custom Python code rather than relying on predefined prompt templates or built-in heuristics. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Use cases

Code-based scorers are recommended for scenarios where more flexibility and control is needed than custom LLM judges alone can provide. The source documentation lists four primary use cases: ^[scorers-and-llm-judges-databricks-on-aws.md]

| Use case | Description |
|----------|-------------|
| Custom heuristic or code-based evaluation metric | Define deterministic scoring logic (e.g., exact match, regex checks, business rule validation) |
| Custom trace-to-judge data mapping | Override how fields from the application’s trace are passed to built-in LLM judges |
| Use your own LLM | Replace the default Databricks-hosted judge model with a model of your choice (e.g., a fine-tuned model or an external provider) |
| Any other advanced logic | Implement complex evaluation pipelines that cannot be expressed through prompts alone |

These cases cover situations where a user requires the ultimate flexibility in defining precisely how quality is measured. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Relationship to other scorer types

In the MLflow GenAI evaluation framework, scorer types form a spectrum from simplicity to control:

- **[Built-in LLM judges]** — Research-validated judges for common quality dimensions (relevance, safety, etc.). Quick to use but limited to predefined criteria.
- **[Custom LLM judges]** — Judges defined with custom prompts and instructions. Provide more control over grades and scores than built-in judges, but still rely on LLMs for assessment.
- **Code-based scorers** — The most flexible option. Users write arbitrary Python code, which can call any model (including their own LLM), implement deterministic logic, or integrate with external services.

Code-based scorers build on the same underlying mechanism as other scorers but replace the LLM prompt with full programmatic control. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Using code-based scorers

The source directs readers to a separate page for full implementation details: [Code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers). The same scorer can be used for both [evaluation in development](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) and [monitoring in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) to ensure consistency across the application lifecycle. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Related concepts

- [[Scorers|Scorer]] — The parent concept for all evaluation components
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre‑built evaluation judges
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — Prompt‑based custom judges
- Evaluation in development — Using scorers during model development
- [Production Monitoring](/concepts/production-monitoring.md) — Using scorers in production to track quality
- [Trace](/concepts/traces.md) — The data structure that scorers receive for evaluation

## Sources

- scorers-and-llm-judges-databricks-on-aws.md

# Citations

1. [scorers-and-llm-judges-databricks-on-aws.md](/references/scorers-and-llm-judges-databricks-on-aws-b2df16f5.md)
