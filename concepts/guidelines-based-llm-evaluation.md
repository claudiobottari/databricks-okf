---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8b8a9c576c360b9065989a45e6b61bb5efc3f56459e0229037c380471330a23
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-based-llm-evaluation
    - GLE
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Guidelines-based LLM evaluation
description: Evaluation approach using natural language criteria (via Guidelines and ExpectationsGuidelines judges) to assess whether responses meet specified requirements, with or without per-example expectations.
tags:
  - llm-evaluation
  - guidelines
  - mlflow
timestamp: "2026-06-18T10:55:49.787Z"
---

# Guidelines-based LLM evaluation

**Guidelines-based LLM evaluation** uses a predefined [LLM judge](/concepts/llm-judges.md) to assess whether a response from a GenAI application satisfies a set of natural language criteria provided by the evaluator. The judge acts as an automated grader that checks for compliance with rules expressed in plain text — for example, "The response must be in Spanish" or "Do not mention competitor products." ^[built-in-llm-judges-databricks-on-aws.md]

This approach is part of the [MLflow](/concepts/mlflow.md) evaluation framework's suite of built-in scorers. It is useful when you want to quickly verify that outputs adhere to policy, style, or formatting guidelines without requiring custom scoring logic. ^[built-in-llm-judges-databricks-on-aws.md]

## Available judges

MLflow provides two guidelines-based judges, both available in each region's Databricks environment. They differ in how guidelines are supplied.

### Guidelines

The `Guidelines` judge (predefined scorer name in MLflow) evaluates responses against a single set of global natural language criteria that apply to every record in the evaluation dataset. ^[built-in-llm-judges-databricks-on-aws.md]

| Property | Value |
|----------|-------|
| **Arguments** | `inputs`, `outputs` |
| **Requires ground truth** | No |
| **What it evaluates** | Does the response meet specified natural language criteria? |

The judge takes a string of guidelines defined once for the entire evaluation. For example, you might set the guideline to "The response should be no more than three sentences and avoid any technical jargon." Every response is checked against the same rule. ^[built-in-llm-judges-databricks-on-aws.md]

### ExpectationsGuidelines

The `ExpectationsGuidelines` judge (predefined scorer name in MLflow) allows per-example natural language criteria. Each row in the evaluation dataset can carry its own guidelines in the `expectations` column. ^[built-in-llm-judges-databricks-on-aws.md]

| Property | Value |
|----------|-------|
| **Arguments** | `inputs`, `outputs`, `expectations` |
| **Requires ground truth** | No (but needs guidelines in expectations) |
| **What it evaluates** | Does the response meet per-example natural language criteria? |

This judge is useful when different test cases require different rules — for example, one prompt might require a safety warning while another demands a concise answer. The judge evaluates each response against its own specified guideline rather than a single global rule. ^[built-in-llm-judges-databricks-on-aws.md]

## Guidelines definition

Guidelines are expressed as natural language sentences. There is no fixed format; the judge interprets the text and applies it to the response. For reliable results, guidelines should be clear, specific, and actionable. Ambiguous statements such as "be polite" can lead to inconsistent scores, whereas "do not use exclamation marks" or "include a citation" produce more reproducible judgments. ^[built-in-llm-judges-databricks-on-aws.md]

## Usage considerations

- Guidelines-based judges do **not** require ground-truth answers, making them suitable for open-ended tasks where a single correct answer does not exist. ^[built-in-llm-judges-databricks-on-aws.md]
- They are predefined scorers powered by a Databricks-hosted LLM. You can switch the underlying model by following the [scorer model selection](/concepts/explicit-scorer-selection.md) guidance. ^[built-in-llm-judges-databricks-on-aws.md]
- If your evaluation needs fall outside what guidelines can express (e.g., numeric range checks, statistical comparisons), consider using a [Custom LLM Judge](/concepts/custom-llm-judge.md) or a [code-based scorer](/concepts/code-based-scorers.md) instead. ^[built-in-llm-judges-databricks-on-aws.md]

## Related concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — The full set of predefined scorers, including safety, relevance, and correctness judges.
- [LLM Judges](/concepts/llm-judges.md) — General concept of using an LLM as an evaluator.
- [Custom LLM Judge](/concepts/custom-llm-judge.md) — Building your own judge when built-in options are insufficient.
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The broader evaluation and monitoring framework.
- [GenAI evaluation](/concepts/mlflow-genai-evaluation.md) — Overview of evaluating generative AI applications.

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
