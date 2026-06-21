---
title: RAGAS scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/ragas
ingestedAt: "2026-06-18T08:15:39.521Z"
---

[RAGAS](https://docs.ragas.io/) (Retrieval Augmented Generation Assessment) is an evaluation framework for LLM applications. MLflow integrates with RAGAS so that you can use RAGAS metrics as scorers for evaluating retrieval quality, answer generation, agent behavior, and text similarity.

## Requirements[​](#requirements "Direct link to Requirements")

Install the `ragas` package:

## Quick start[​](#quick-start "Direct link to Quick start")

To call a RAGAS scorer directly:

Python

    from mlflow.genai.scorers.ragas import Faithfulnessscorer = Faithfulness(model="databricks:/databricks-gpt-5-mini")feedback = scorer(trace=trace)print(feedback.value)  # Score between 0.0 and 1.0print(feedback.rationale)  # Explanation of the score

To call RAGAS scorers using [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate):

Python

    import mlflowfrom mlflow.genai.scorers.ragas import Faithfulness, ContextPrecisiontraces = mlflow.search_traces()results = mlflow.genai.evaluate(    data=traces,    scorers=[        Faithfulness(model="databricks:/databricks-gpt-5-mini"),        ContextPrecision(model="databricks:/databricks-gpt-5-mini"),    ],)

## Available RAGAS scorers[​](#available-ragas-scorers "Direct link to Available RAGAS scorers")

### RAG metrics[​](#rag-metrics "Direct link to RAG metrics")

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation (RAG) applications.

### Agent and tool use metrics[​](#agent-and-tool-use-metrics "Direct link to Agent and tool use metrics")

These scorers evaluate AI agent behavior, including tool invocation accuracy and goal achievement.

### Natural language comparison[​](#natural-language-comparison "Direct link to Natural language comparison")

These scorers compare generated text against expected output using both semantic and deterministic methods.

### General purpose[​](#general-purpose "Direct link to General purpose")

These scorers provide flexible, customizable evaluation logic.

### Other tasks[​](#other-tasks "Direct link to Other tasks")

## Create a scorer by name[​](#create-a-scorer-by-name "Direct link to Create a scorer by name")

You can dynamically create a scorer using `get_scorer` by passing the metric name as a string:

Python

    from mlflow.genai.scorers.ragas import get_scorerscorer = get_scorer(    metric_name="Faithfulness",    model="databricks:/databricks-gpt-5-mini",)feedback = scorer(trace=trace)

## Configuration[​](#configuration "Direct link to Configuration")

RAGAS scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter. Non-LLM metrics do not require a model.

Python

    from mlflow.genai.scorers.ragas import Faithfulness, ExactMatch# LLM-based metric with model specificationscorer = Faithfulness(model="databricks:/databricks-gpt-5-mini")# Non-LLM metric (no model required)deterministic_scorer = ExactMatch()

For metric-specific parameters and advanced usage options, see the [RAGAS documentation](https://docs.ragas.io/).
