---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8814f2ced52fec86cbd0593667480eae7871457561db85d678cbce0b35ef1664
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-llm-judge-architecture
    - MLJA
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow LLM Judge Architecture
description: The framework of built-in LLM judges in MLflow that use a judge LLM (defaulting to a Databricks-hosted model) to automatically assess GenAI application quality across dimensions like relevance, groundedness, safety, and correctness.
tags:
  - mlflow
  - llm-evaluation
  - architecture
  - genai
timestamp: "2026-06-19T14:01:08.603Z"
---

# MLflow LLM Judge Architecture

**MLflow LLM Judge Architecture** describes the design and operational framework of LLM-as-a-judge evaluators within the MLflow GenAI ecosystem. These judges are LLM-based scorers that assess the quality of generative AI outputs programmatically. The architecture supports both built-in judges for common criteria and a flexible custom judge system for domain‑specific evaluation.^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Core Components

### Built‑in Judges
MLflow provides a set of pre‑configured judges that address standard quality dimensions. Each built‑in judge is implemented as a class that can be instantiated and passed to `mlflow.genai.evaluate()`.

- **`RelevanceToQuery`** – Evaluates whether the application’s response directly addresses the user’s input without deviating into unrelated topics. Requires `inputs` and `outputs` on the Trace’s root span.^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **`RetrievalRelevance`** – Evaluates whether each document returned by a retriever is relevant to the input request. Requires a span with `span_type` set to `RETRIEVER` in the MLflow Trace.^[answer-and-context-relevance-judges-databricks-on-aws.md]

Both judges return a `Feedback` object containing:
- `value`: `"yes"` if the context is relevant, `"no"` otherwise.
- `rationale`: Explanation of the judge’s reasoning.^[answer-and-context-relevance-judges-databricks-on-aws.md]

Built‑in judges default to a Databricks‑hosted LLM; the judge model can be changed via the `model` parameter using the format `<provider>:/<model-name>`.^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Custom Judges
For criteria not covered by built‑in judges, the `make_judge()` API allows the creation of custom LLM‑based scorers. A custom judge is defined by:
- **Name** – A unique identifier.
- **Instructions** – A natural‑language prompt that describes the evaluation task, may include template variables such as `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, or `{{ trace }}`.
- **Feedback value type** – The data type of the score (e.g. `bool`, `str`, `float`).
- **Optional rubric** – A detailed scoring guide.
- **Model specification** – The LLM endpoint used to perform the judgment.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

When `{{ trace }}` is included in the instructions, the judge becomes **trace‑based**: it analyzes the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. Trace‑based judges require an explicit `model` parameter.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How Judges Work

### Evaluation Flow
1. A judge receives the inputs (conversation history or query), outputs (agent response), and optionally expectations (ground‑truth references) or execution trace.
2. The judge constructs a prompt (built‑in or custom) that asks the underlying LLM to score the output according to the defined criteria.
3. The LLM returns a structured judgment – a score and a rationale – which the judge packages into a `Feedback` object.
4. During `mlflow.genai.evaluate()`, each judge is applied to every row of the evaluation dataset. The resulting feedback is aggregated and logged to the MLflow experiment.^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Input/Output vs. Trace‑Based
- **Input/Output judges** evaluate behavior by analyzing only the conversation history (`inputs`) and agent responses (`outputs`). They are suitable for criteria such as issue resolution or adherence to expected behaviors.
- **Trace‑based judges** evaluate the full execution trace, enabling validation of tool usage correctness, reasoning quality, and intermediate steps. They are essential for assessing agent systems that invoke multiple tools.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Integration with Evaluation

Judges are passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`. Multiple judges can be applied simultaneously. The same dataset and judge set can be used to compare different agent configurations in [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md).^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=agent_function,
    scorers=[
        built_in_relevance_judge,
        custom_behavior_judge,
    ]
)
```

## Alignment with Human Feedback

The judge architecture supports a feedback loop: as human experts provide annotations on agent outputs, judges can be refined to better reflect human quality assessments. This process – Align judges with human feedback – improves the correlation between automated scores and human judgment over time.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Selection of the Judge LLM

Both built‑in and custom judges accept a `model` parameter to specify which LLM powers the judgment. The model string follows the format `<provider>:/<model-name>`. Common providers include `databricks` (serving endpoint name) and any LiteLLM‑compatible provider. Changing the judge model can alter the sensitivity or bias of the evaluation.^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Custom Judges](/concepts/custom-judges.md)
- make_judge()|Make Judge API
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md)
- GenAI Agent Evaluation
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- Human Feedback Alignment

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
