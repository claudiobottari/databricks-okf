---
title: DeepEval scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/deep-eval
ingestedAt: "2026-06-18T08:15:33.969Z"
---

[DeepEval](https://docs.confident-ai.com/) is a comprehensive evaluation framework for LLM applications that provides metrics for RAG systems, agents, conversational AI, and safety evaluation. MLflow integrates with DeepEval so that you can use DeepEval metrics as scorers.

## Requirements[​](#requirements "Direct link to Requirements")

Install the `deepeval` package:

## Quick start[​](#quick-start "Direct link to Quick start")

To call a DeepEval scorer directly:

Python

    from mlflow.genai.scorers.deepeval import AnswerRelevancyscorer = AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini")feedback = scorer(    inputs="What is MLflow?",    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",)print(feedback.value)  # "yes" or "no"print(feedback.metadata["score"])  # 0.85

To call DeepEval scorers using [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate):

Python

    import mlflowfrom mlflow.genai.scorers.deepeval import AnswerRelevancy, Faithfulnesseval_dataset = [    {        "inputs": {"query": "What is MLflow?"},        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",    },    {        "inputs": {"query": "How do I track experiments?"},        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",    },]results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[        AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini"),        Faithfulness(threshold=0.8, model="databricks:/databricks-gpt-5-mini"),    ],)

## Available DeepEval scorers[​](#available-deepeval-scorers "Direct link to Available DeepEval scorers")

### RAG metrics[​](#rag-metrics "Direct link to RAG metrics")

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation (RAG) applications.

### Agentic metrics[​](#agentic-metrics "Direct link to Agentic metrics")

These scorers evaluate AI agent behavior, including task completion and tool usage.

### Conversational metrics[​](#conversational-metrics "Direct link to Conversational metrics")

These scorers evaluate multi-turn conversational AI quality.

### Safety metrics[​](#safety-metrics "Direct link to Safety metrics")

These scorers evaluate the safety and responsibility of model outputs.

### Other metrics[​](#other-metrics "Direct link to Other metrics")

### Non-LLM metrics[​](#non-llm-metrics "Direct link to Non-LLM metrics")

## Create a scorer by name[​](#create-a-scorer-by-name "Direct link to Create a scorer by name")

You can dynamically create a scorer using `get_scorer` by passing the metric name as a string:

Python

    from mlflow.genai.scorers.deepeval import get_scorerscorer = get_scorer(    metric_name="AnswerRelevancy",    threshold=0.7,    model="databricks:/databricks-gpt-5-mini",)feedback = scorer(    inputs="What is MLflow?",    outputs="MLflow is a platform for ML workflows.",)

## Configuration[​](#configuration "Direct link to Configuration")

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter.

Python

    from mlflow.genai.scorers.deepeval import AnswerRelevancy, TurnRelevancy# LLM-based metric with common parametersscorer = AnswerRelevancy(    model="databricks:/databricks-gpt-5-mini",    threshold=0.7,    include_reason=True,)# Metric-specific parametersconversational_scorer = TurnRelevancy(    model="openai:/gpt-4o",    threshold=0.8,    window_size=3,    strict_mode=True,)

For metric-specific parameters and advanced usage options, see the [DeepEval documentation](https://docs.confident-ai.com/).
