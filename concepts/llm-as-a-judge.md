---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 406646ee77fa31825616fb1052c2e65c3c747c352453827500daddc8a1148732
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - llm-as-a-judge
    - LLM-as-Judge
    - LLM-as-judge
    - AI Judges
    - Choose the LLM that powers a judge
    - LLM-as-judge|judge
    - Model-as-judge
    - select the LLM that powers a judge
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: LLM-as-a-Judge
description: The pattern of using a large language model to evaluate the quality of outputs from another LLM-based system, serving as an automated evaluator for dimensions like relevance and safety.
tags:
  - llm-evaluation
  - pattern
  - genai
timestamp: "2026-06-19T09:11:31.223Z"
---

# LLM-as-a-Judge

**LLM-as-a-Judge** refers to the practice of using a large language model (LLM) as an automated evaluator to score the quality of outputs from another GenAI application. In [MLflow GenAI](/concepts/mlflow-3-for-genai.md), this is implemented through predefined **built-in LLM judges** — scorers that use Databricks-hosted LLMs to assess common quality dimensions such as relevance, safety, groundedness, and correctness.^[built-in-llm-judges-databricks-on-aws.md]

Built-in judges are designed for rapid evaluation. For scenarios requiring more control over evaluation criteria, users can supplement or replace them with [Custom LLM Judges](/concepts/custom-llm-judges.md) or Python-based [Code-based Scorers](/concepts/code-based-scorers.md).^[built-in-llm-judges-databricks-on-aws.md]

## Available Judges

The following table summarizes the predefined LLM judges provided by MLflow. Each judge evaluates a specific quality dimension of the GenAI application's output.

| Judge | Arguments | Requires Ground Truth? | What It Evaluates |
|-------|-----------|------------------------|-------------------|
| `RelevanceToQuery` | `inputs`, `outputs` | No | Is the response directly relevant to the user's request? |
| `RetrievalRelevance` | `inputs`, `outputs` | No | Is the retrieved context directly relevant to the user's request? |
| `Safety` | `inputs`, `outputs` | No | Is the content free from harmful, offensive, or toxic material? |
| `RetrievalGroundedness` | `inputs`, `outputs` | No | Is the response grounded in the information provided in the context? (i.e., is the agent hallucinating?) |
| `Correctness` | `inputs`, `outputs`, `expectations` | Yes | Is the response correct as compared to the provided ground truth? |
| `RetrievalSufficiency` | `inputs`, `outputs`, `expectations` | Yes | Does the context provide all necessary information to generate a response that includes the ground truth facts? |
| `Guidelines` | `inputs`, `outputs` | No | Does the response meet specified natural language criteria? |
| `ExpectationsGuidelines` | `inputs`, `outputs`, `expectations` | No (but needs guidelines in expectations) | Does the response meet per-example natural language criteria? |
| `ToolCallCorrectness` | `inputs`, `outputs`, `expectations` | Yes | Are the tool calls and arguments correct for the user query? |
| `ToolCallEfficiency` | `inputs`, `outputs` | No | Are the tool calls efficient without redundancy? |

For complete details and usage documentation, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/).^[built-in-llm-judges-databricks-on-aws.md]

## Multi‑Turn Judges

For conversational AI systems, MLflow provides judges that evaluate entire conversations rather than individual turns. These judges analyze the complete conversation history to assess quality patterns that emerge over multiple interactions. They can be used both during evaluation during development and for [Production Monitoring](/concepts/production-monitoring.md).^[built-in-llm-judges-databricks-on-aws.md]

## Next Steps

- [Choose the LLM that powers a judge](/concepts/llm-as-a-judge.md)  
- [Build a custom LLM judge](/concepts/custom-llm-judge.md) when built-in judges do not fit your use case  
- Align judges with human feedback to improve accuracy on your domain  

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
