---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85b136117aaf09f42ab2dadc025bf6da1dfa0a7846dc8003cd715d08706a29f5
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-turn-judge
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Multi-turn Judge
description: A type of LLM judge that evaluates entire conversational histories across multiple interaction turns rather than scoring individual response turns in isolation.
tags:
  - llm-evaluation
  - conversational-ai
  - mlflow
timestamp: "2026-06-19T09:11:26.205Z"
---

# Multi-turn Judge

**Multi-turn Judge** refers to a type of [LLM judge](/concepts/llm-judges.md) designed to evaluate entire conversations rather than individual turns in conversational AI systems. Unlike single-turn judges that assess each user-assistant exchange independently, multi-turn judges analyze the complete conversation history to assess quality patterns that emerge over multiple interactions. ^[built-in-llm-judges-databricks-on-aws.md]

## Overview

Conversational AI systems often exhibit quality characteristics that cannot be evaluated by examining individual turns in isolation. For example, an agent might maintain context across several exchanges, gradually refine its understanding of a user's request, or build upon information provided earlier in the conversation. Multi-turn judges capture these holistic properties by processing the full dialogue history. ^[built-in-llm-judges-databricks-on-aws.md]

## Use Cases

Multi-turn judges are used in two primary contexts:

- **Evaluation during development**: Assess conversational quality as part of the [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) workflow before deploying an agent to production. ^[built-in-llm-judges-databricks-on-aws.md]
- **Production monitoring**: Continuously monitor conversation quality in deployed systems using [production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md). ^[built-in-llm-judges-databricks-on-aws.md]

## Available Multi-turn Judges

For the complete list and detailed documentation of available multi-turn judges, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/#multi-turn). ^[built-in-llm-judges-databricks-on-aws.md]

## Relationship to Other Judge Types

Multi-turn judges are one category within the broader set of [Built-in LLM Judges](/concepts/built-in-llm-judges.md). Other categories include:

- **Single-turn judges**: Evaluate individual user-assistant exchanges on dimensions like relevance, safety, groundedness, and correctness. ^[built-in-llm-judges-databricks-on-aws.md]
- **Tool call judges**: Assess the correctness and efficiency of tool invocations made by the agent. ^[built-in-llm-judges-databricks-on-aws.md]

When built-in multi-turn judges do not fit a specific use case, developers can create [Custom Judges](/concepts/custom-judges.md) using the make_judge()|make_judge API. ^[built-in-llm-judges-databricks-on-aws.md]

## Related Concepts

- [LLM Judge](/concepts/llm-judges.md) — The general concept of LLM-based evaluators
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined scorers for common quality dimensions
- [Custom Judges](/concepts/custom-judges.md) — User-defined evaluators for specialized criteria
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework for GenAI applications
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [Conversational AI Evaluation](/concepts/conversation-evaluation.md) — Broader practices for assessing dialogue systems

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
