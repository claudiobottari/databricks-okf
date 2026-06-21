---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e5fec276f602c05c25b5db46a9cfc08c80a16cceac568854433608cc5f6ca61
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-evaluation-quality-dimensions
    - LEQD
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: LLM Evaluation Quality Dimensions
description: Specific quality aspects evaluated by LLM judges including relevance, retrieval relevance, safety, groundedness, correctness, sufficiency, guidelines compliance, tool call correctness, and tool call efficiency.
tags:
  - llm-evaluation
  - quality-metrics
  - genai
timestamp: "2026-06-19T17:42:20.718Z"
---

# LLM Evaluation Quality Dimensions

**LLM Evaluation Quality Dimensions** are the pre-defined criteria used by built-in LLM judges to assess the quality of outputs from generative AI applications. These dimensions cover aspects such as relevance, safety, groundedness, and correctness, and are evaluated by Databricks-hosted models. The dimensions are designed for quick evaluation setup; when more control is needed, custom LLM judges or Python-based scorers can be used instead. ^[built-in-llm-judges-databricks-on-aws.md]

## Available Quality Dimensions

The following table summarizes the quality dimensions, their required arguments, whether they need ground truth, and what they evaluate. Descriptions are taken directly from the built-in judge documentation.

| Dimension | Arguments | Requires Ground Truth | What It Evaluates |
|-----------|-----------|----------------------|-------------------|
| **RelevanceToQuery** | `inputs`, `outputs` | No | Is the response directly relevant to the user's request? |
| **RetrievalRelevance** | `inputs`, `outputs` | No | Is the retrieved context directly relevant to the user's request? |
| **Safety** | `inputs`, `outputs` | No | Is the content free from harmful, offensive, or toxic material? |
| **RetrievalGroundedness** | `inputs`, `outputs` | No | Is the response grounded in the information provided in the context? Is the agent hallucinating? |
| **Correctness** | `inputs`, `outputs`, `expectations` | Yes | Is the response correct as compared to the provided ground truth? |
| **RetrievalSufficiency** | `inputs`, `outputs`, `expectations` | Yes | Does the context provide all necessary information to generate a response that includes the ground truth facts? |
| **Guidelines** | `inputs`, `outputs` | No | Does the response meet specified natural language criteria? |
| **ExpectationsGuidelines** | `inputs`, `outputs`, `expectations` | No (but needs guidelines in expectations) | Does the response meet per-example natural language criteria? |
| **ToolCallCorrectness** | `inputs`, `outputs`, `expectations` | Yes | Are the tool calls and arguments correct for the user query? |
| **ToolCallEfficiency** | `inputs`, `outputs` | No | Are the tool calls efficient without redundancy? |

^[built-in-llm-judges-databricks-on-aws.md]

## Multi-Turn Judges

For conversational AI systems, MLflow provides judges that evaluate entire conversations rather than individual turns. These judges analyze the complete conversation history to assess quality patterns that emerge over multiple interactions. Multi-turn judges can be used both for evaluation during development and for [Production Monitoring](/concepts/production-monitoring.md). ^[built-in-llm-judges-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Custom LLM Judges](/concepts/custom-llm-judges.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- [MLflow predefined scorers documentation](/concepts/mlflow-genai-predefined-scorers.md)
- Align judges with human feedback

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
