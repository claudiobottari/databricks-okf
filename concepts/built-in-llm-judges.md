---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d7ced040a33697ca67754ecd165bffcc02558961951a902aa8d303765160ccb
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - built-in-llm-judges
    - BLJ
    - Built‑in LLM judges
    - built‑in LLM judges
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
    - file: scorers-and-llm-judges-databricks-on-aws.md
    - file: code-based-scorers-databricks-on-aws.md
title: Built-in LLM Judges
description: Predefined scorers that use Databricks-hosted LLMs to evaluate common quality dimensions of GenAI applications such as relevance, safety, groundedness, and correctness.
tags:
  - llm-evaluation
  - databricks
  - mlflow
  - genai
timestamp: "2026-06-19T17:42:32.299Z"
---

# Built-in LLM Judges

**Built-in LLM judges** are predefined [[scorers]] that use Databricks-hosted large language models (LLMs) to automatically evaluate common quality dimensions of a GenAI application, such as relevance, safety, groundedness, and correctness. They are designed to let you start evaluating quality quickly without writing custom evaluation logic. When more control is needed, you can use [Custom LLM Judges](/concepts/custom-llm-judges.md) or [Code-based Scorers](/concepts/code-based-scorers.md).^[built-in-llm-judges-databricks-on-aws.md]

Built-in judges are research-validated and provide a standardized way to assess GenAI application quality. They are a type of MLflow `Scorer` that uses LLMs for quality assessment, treating the judge as an AI assistant specialized in quality evaluation that can examine inputs, outputs, and entire execution traces to make assessments.^[scorers-and-llm-judges-databricks-on-aws.md]

## Available judges

The following table lists the built-in judges provided by MLflow, their required arguments, whether they require ground truth, and what they evaluate. For full documentation of each judge, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/).^[built-in-llm-judges-databricks-on-aws.md]

| Judge | Arguments | Requires ground truth | What it evaluates |
|---|---|---|---|
| `RelevanceToQuery` | `inputs`, `outputs` | No | Is the response directly relevant to the user's request? |
| `RetrievalRelevance` | `inputs`, `outputs` | No | Is the retrieved context directly relevant to the user's request? |
| `Safety` | `inputs`, `outputs` | No | Is the content free from harmful, offensive, or toxic material? |
| `RetrievalGroundedness` | `inputs`, `outputs` | No | Is the response grounded in the information provided in the context? (Is the agent hallucinating?) |
| `Correctness` | `inputs`, `outputs`, `expectations` | Yes | Is the response correct as compared to the provided ground truth? |
| `RetrievalSufficiency` | `inputs`, `outputs`, `expectations` | Yes | Does the context provide all necessary information to generate a response that includes the ground truth facts? |
| `Guidelines` | `inputs`, `outputs` | No | Does the response meet specified natural language criteria? |
| `ExpectationsGuidelines` | `inputs`, `outputs`, `expectations` | No (but needs guidelines in expectations) | Does the response meet per-example natural language criteria? |
| `ToolCallCorrectness` | `inputs`, `outputs`, `expectations` | Yes | Are the tool calls and arguments correct for the user query? |
| `ToolCallEfficiency` | `inputs`, `outputs` | No | Are the tool calls efficient without redundancy? |

## Multi-turn judges

For conversational AI systems, MLflow also provides built-in judges that evaluate entire conversations rather than individual turns. These multi-turn judges analyze the complete conversation history to assess quality patterns that emerge over multiple interactions.^[built-in-llm-judges-databricks-on-aws.md]

You can use multi-turn judges both for evaluation during development and for monitoring in production. See the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/#multi-turn) for the complete list.^[built-in-llm-judges-databricks-on-aws.md]

## Selecting the judge model

By default, each built-in judge uses a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument in the judge definition, specifying the model in the format `<provider>:/<model-name>`. For example:^[scorers-and-llm-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

Correctness(model="databricks:/databricks-gpt-5-mini")
```

For European Union (EU) workspaces, LLM judges use models hosted in the EU. All other regions use models hosted in the US.^[scorers-and-llm-judges-databricks-on-aws.md]

## Production monitoring support

Built-in LLM judges are supported in production monitoring. When using them in this context, only built-in judges and `@scorer`-decorated functions are supported — class-based `Scorer` subclasses are not supported. If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body.^[code-based-scorers-databricks-on-aws.md]

## Judge accuracy and trust

Databricks continuously improves judge quality through research validation against human expert judgment, metrics tracking including Cohen's Kappa, accuracy, and F1 score, and diverse testing on academic and real-world datasets.^[scorers-and-llm-judges-databricks-on-aws.md]

LLM judges might use third-party services to evaluate your GenAI applications, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI. Disabling Partner-powered AI features prevents the LLM judge from calling partner-powered models, though you can still use LLM judges by providing your own model. LLM judges are intended to help evaluate GenAI applications, and their outputs should not be used to train, improve, or fine-tune an LLM.^[scorers-and-llm-judges-databricks-on-aws.md]

## Next steps

- [Choose the LLM that powers a judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers#select-the-llm-that-powers-the-judge)
- [Build a custom LLM judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) when built-in judges do not fit your use case
- [Align judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) to improve accuracy on your domain

## Related concepts

- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md)
- [Custom LLM Judges](/concepts/custom-llm-judges.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)
- [Production Monitoring](/concepts/production-monitoring.md)

## Sources

- built-in-llm-judges-databricks-on-aws.md
- code-based-scorers-databricks-on-aws.md
- scorers-and-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
2. [scorers-and-llm-judges-databricks-on-aws.md](/references/scorers-and-llm-judges-databricks-on-aws-b2df16f5.md)
3. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
