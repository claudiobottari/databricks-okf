---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ae2c38742632c6b3a59d4294f9a6a455e7da1078547384273ab092d3ae7fcf6
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-vs-built-in-scorers
    - CVBS
    - Built-in Scorers
    - built-in scorers
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Custom vs Built-in Scorers
description: The distinction between predefined LLM judges provided by Databricks/MLflow and custom alternatives (custom LLM judges or Python code-based scorers) for more controlled evaluation.
tags:
  - llm-evaluation
  - mlflow
  - databricks
timestamp: "2026-06-18T14:34:56.991Z"
---

# Custom vs Built-in Scorers

**Custom vs Built-in Scorers** describes the two primary approaches to evaluating GenAI applications in [MLflow GenAI](/concepts/mlflow-3-for-genai.md): using pre-defined, Databricks-hosted LLM judges (built-in scorers) or creating your own evaluation logic via either an LLM-based custom judge or a Python code-based scorer. The choice depends on how quickly you need to start evaluating versus how much control you require over the evaluation criteria.

## Overview

Built-in LLM judges are [[scorers]] that use Databricks-hosted LLMs to evaluate common quality dimensions such as relevance, safety, groundedness, and correctness. They are designed for rapid adoption—you can start evaluating quality immediately without writing any judge logic. For situations that demand more control, you can build a [Custom LLM Judge](/concepts/custom-llm-judge.md) or use a [Python code-based scorer](/concepts/code-based-scorers.md).^[built-in-llm-judges-databricks-on-aws.md]

## Built-in Scorers

Databricks provides a library of predefined LLM judges that cover the most frequent evaluation needs. All built-in judges are powered by Databricks-hosted LLMs, so no additional model setup is required. Available judges include:

- `RelevanceToQuery`, `RetrievalRelevance` – assess how well the response or retrieved context matches the user’s request.
- `Safety` – checks for harmful, offensive, or toxic content.
- `RetrievalGroundedness` – detects hallucination by verifying responses against provided context.
- `Correctness` – requires ground truth (`expectations`) and compares the response to it.
- `RetrievalSufficiency` – also requires ground truth; determines whether the context contains all necessary information.
- `Guidelines` – evaluates whether the response adheres to user-defined natural language criteria.
- `ExpectationsGuidelines` – evaluates per-example natural language criteria embedded in the `expectations` field.
- `ToolCallCorrectness`, `ToolCallEfficiency` – evaluate tool call correctness and efficiency (these also appear in the MLflow predefined scorer documentation).

MLflow also provides [Multi-turn Judges](/concepts/multi-turn-judges.md) for conversational AI systems that analyze entire conversation histories rather than individual turns.^[built-in-llm-judges-databricks-on-aws.md]

Built-in scorers are ideal when you want to **start evaluating quality quickly** and the standard quality dimensions (relevance, safety, groundedness, correctness) cover your use case.^[built-in-llm-judges-databricks-on-aws.md]

## Custom Scorers

When built-in judges do not fit your unique requirements—for example, you need a domain-specific rubric, a different LLM provider, or logic that cannot be expressed in natural language instructions—you can create a **custom scorer**. There are two routes:

- **Custom LLM judge** – You define the instructions, grading criteria, and optionally the underlying model. This is built using make_judge()|Make Judge API (`make_judge()`) or by extending the [MLflow judge class](/concepts/mlflow-llm-judges.md).
- **Python code-based scorer** – You write arbitrary Python logic to compute a score, giving you full flexibility without relying on an LLM. This is useful for deterministic checks, numeric calculations, or integrating with external services.

Custom scorers provide **more control over your judges** at the cost of additional setup and maintenance effort.^[built-in-llm-judges-databricks-on-aws.md]

## Choosing Between Built-in and Custom Scorers

| Factor | Built-in Scorers | Custom Scorers |
|--------|------------------|----------------|
| Setup effort | Immediate – no configuration required | Requires implementation (LLM instructions or Python code) |
| Evaluation criteria | Predefined quality dimensions (relevance, safety, groundedness, correctness, etc.) | Any criteria you define |
| Model | Databricks-hosted LLM only | Your choice of LLM (for custom LLM judges) or no LLM (for code-based scorers) |
| Ground truth | Required by some built-in judges (`Correctness`, `RetrievalSufficiency`) | Optional, depending on your implementation |
| Flexibility | Limited to built-in dimensions | Unlimited |
| Best for | Rapid prototyping, common quality checks, production monitoring with standard metrics | Domain-specific evaluation, nuanced behavior, complex scoring logic |

Use **built-in scorers** when the predefined dimensions align with your goals and you want to start evaluating immediately. Use **custom scorers** when you need evaluation that goes beyond the built-in options—such as [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) with unique criteria, or when you want to Align judges with human feedback to improve accuracy on your domain.^[built-in-llm-judges-databricks-on-aws.md]

## Next Steps

- [Choose the LLM that powers a judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers#select-the-llm-that-powers-the-judge)
- [Build a custom LLM judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) when built-in judges don't fit your use case
- [Align judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) to improve accuracy on your domain

## Related Concepts

- [[Scorers]] – The general concept of evaluation functions in MLflow GenAI.
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – Creating your own LLM-based scorer via `make_judge()`.
- Python code-based scorers – Deterministic or computational scorers.
- [Multi-turn Judges](/concepts/multi-turn-judges.md) – Built-in judges for conversational AI.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – A use case that often benefits from custom judges.

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
