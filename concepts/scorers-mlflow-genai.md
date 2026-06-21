---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5e2d56c6547027c5dd83a2f4907ed4c1fee8c876d0bf53d1a7d661679e710ff
  pageDirectory: concepts
  sources:
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorers-mlflow-genai
    - S(G
    - Scorers in MLflow GenAI
    - Scorer (MLflow)
    - Scorer in MLflow
    - Scorers (MLflow)
    - scorers (MLflow)
  citations:
    - file: scorers-and-llm-judges-databricks-on-aws.md
title: Scorers (MLflow GenAI)
description: A unified interface within MLflow GenAI evaluation framework that defines evaluation criteria for models, agents, and applications, receiving traces and returning quality assessments as feedback.
tags:
  - mlflow
  - evaluation
  - quality-assessment
timestamp: "2026-06-19T20:19:37.229Z"
---

---

title: Scorers (MLflow GenAI)
summary: Functions that evaluate trace quality by parsing traces and running judges or deterministic code, acting as adapters between traces and evaluation logic.
sources:
  - scorers-and-llm-judges-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:41:48.532Z"
updatedAt: "2026-06-18T14:41:48.532Z"
tags:
  - mlflow
  - evaluation
  - quality-monitoring
aliases:
  - scorers-mlflow-genai
  - S(G
confidence: 0.97
provenanceState: merged
inferredParagraphs: 3
---

# Scorers (MLflow GenAI)

**Scorers** are a key component of the MLflow GenAI evaluation framework. They provide a unified interface to define evaluation criteria for your models, agents, and applications. Like their name suggests, scorers score how well your application performed based on the evaluation criteria — this could be a pass/fail, true/false, numerical value, or categorical value. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Overview

Scorers are functions that evaluate a trace's quality. They receive a [Trace (MLflow GenAI)](/concepts/traces-mlflow-genai.md) from either `mlflow.genai.evaluate()` or the production monitoring service, then perform the following steps: ^[scorers-and-llm-judges-databricks-on-aws.md]

1. **Parse** the trace to extract specific fields and data used to assess quality
2. **Run** the scorer to perform the quality assessment based on the extracted fields and data
3. **Return** the quality assessment as Feedback (MLflow GenAI) to attach to the trace

You can use the same scorer for [Evaluation in Development (MLflow GenAI)](/concepts/evaluation-harness-mlflow-genai.md) and [Production Monitoring (MLflow GenAI)](/concepts/production-quality-monitoring-mlflow-genai.md) to keep evaluation consistent throughout the application lifecycle. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Scorers vs. Judges

In MLflow, a *judge* is a callable SDK that evaluates text based on specific criteria. However, judges can't directly process traces — they only understand text inputs. Scorers extract the relevant data from a trace (such as the request, response, and retrieved context) and pass it to the judge for evaluation. Think of scorers as the "adapter" that connects your traces to evaluation logic, whether that's an [LLM Judge](/concepts/llm-judges.md) or custom code. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Types of Scorers

MLflow provides several types of scorers, each building on the previous one with more complexity and control: ^[scorers-and-llm-judges-databricks-on-aws.md]

### Built-in LLM Judges

MLflow provides research-validated built-in judges for common quality dimensions like relevance, safety, groundedness, and correctness. For the complete list and detailed guidance on each judge, see [Built-in LLM Judges](/concepts/built-in-llm-judges.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

### Multi-turn Judges

For conversational AI systems, MLflow also provides built-in judges that evaluate entire conversations rather than individual turns. See [Multi-turn Judges](/concepts/multi-turn-judges.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

### Custom LLM Judges

In addition to built-in judges, you can create your own judges using custom prompts and instructions. Use custom LLM judges when you need to define specialized evaluation tasks, need more control over grades or scores (not just pass/fail), or need to validate that your agent made appropriate decisions and performed operations correctly for your specific use case. Use [Judge Alignment](/concepts/judge-alignment.md) to train custom LLM judges to match human evaluation standards through systematic feedback. See [Custom Judges](/concepts/custom-judges.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

### Code-based Scorers

Custom code-based scorers offer the ultimate flexibility to define precisely how your GenAI application's quality is measured. You can define evaluation metrics tailored to your specific business use case, whether based on simple heuristics, advanced logic, or programmatic evaluations. Use custom scorers for scenarios such as defining a custom heuristic, customizing how trace data maps to built-in LLM judges, using your own LLM for evaluation, or any other case requiring more flexibility than custom LLM judges provide. See [Code-based Scorers](/concepts/code-based-scorers.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

## Selecting the LLM that Powers the Judge

By default, each judge uses a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument in the judge definition. Specify the model in the format `<provider>:/<model-name>`. For example: ^[scorers-and-llm-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness
Correctness(model="databricks:/databricks-gpt-5-mini")
```

### Information about the Models Powering LLM Judges

LLM judges might use third‑party services, including Azure OpenAI operated by Microsoft. Databricks has opted out of Abuse Monitoring for Azure OpenAI, so no prompts or responses are stored with Azure OpenAI. For European Union (EU) workspaces, LLM judges use models hosted in the EU; all other regions use models hosted in the US. Disabling [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) prevents the LLM judge from calling partner‑powered models. You can still use LLM judges by providing your own model. LLM judge outputs should not be used to train, improve, or fine‑tune an LLM. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Judge Accuracy

Databricks continuously improves judge quality through: ^[scorers-and-llm-judges-databricks-on-aws.md]

- **Research validation** against human expert judgment
- **Metrics tracking**: Cohen's Kappa, accuracy, F1 score
- **Diverse testing** on academic and real-world datasets

## Related Concepts

- [Trace (MLflow GenAI)](/concepts/traces-mlflow-genai.md) — The data structure that captures application execution
- Feedback (MLflow GenAI) — Quality measurements attached to traces
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated collections of test cases for systematic testing
- [Evaluation Harness](/concepts/evaluation-harness.md) — The `mlflow.genai.evaluate()` SDK for systematic evaluation
- Production Quality Monitoring — Scheduling scorers for production trace evaluation
- [Judge Alignment](/concepts/judge-alignment.md) — Training custom LLM judges to match human evaluation standards
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre‑defined judges for common quality dimensions
- [Multi-turn Judges](/concepts/multi-turn-judges.md) — Judges for conversational AI systems
- [Custom Judges](/concepts/custom-judges.md) — User‑defined LLM judges with custom prompts
- [Code-based Scorers](/concepts/code-based-scorers.md) — Fully flexible, programmatic evaluation logic

## Sources

- scorers-and-llm-judges-databricks-on-aws.md

# Citations

1. [scorers-and-llm-judges-databricks-on-aws.md](/references/scorers-and-llm-judges-databricks-on-aws-b2df16f5.md)
