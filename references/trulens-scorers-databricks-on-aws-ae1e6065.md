---
title: TruLens scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/trulens
ingestedAt: "2026-06-18T08:15:41.630Z"
---

[TruLens](https://www.trulens.org/) is an evaluation and observability framework for LLM applications that provides feedback functions for RAG systems and agent trace analysis. MLflow integrates with TruLens so that you can use TruLens feedback functions as scorers, including benchmarked goal-plan-action alignment evaluations for agent traces.

## Requirements[​](#requirements "Direct link to Requirements")

Install the `trulens` and `trulens-providers-litellm` packages:

Python

    %pip install trulens trulens-providers-litellm

## Quick start[​](#quick-start "Direct link to Quick start")

To call a TruLens scorer directly:

Python

    from mlflow.genai.scorers.trulens import Groundednessscorer = Groundedness(model="openai:/gpt-5-mini")feedback = scorer(    inputs="What is MLflow?",    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",    expectations={        "context": "MLflow is an ML platform for experiment tracking and model deployment."    },)print(feedback.value)  # "yes" or "no"print(feedback.metadata["score"])  # 0.85

To call TruLens scorers using [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate):

Python

    import mlflowfrom mlflow.genai.scorers.trulens import Groundedness, AnswerRelevanceeval_dataset = [    {        "inputs": {"query": "What is MLflow?"},        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",        "expectations": {            "context": "MLflow is an ML platform for experiment tracking and model deployment."        },    },    {        "inputs": {"query": "How do I track experiments?"},        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",        "expectations": {            "context": "MLflow provides APIs like mlflow.start_run() for experiment tracking."        },    },]results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[        Groundedness(model="openai:/gpt-5-mini"),        AnswerRelevance(model="openai:/gpt-5-mini"),    ],)

## Available TruLens scorers[​](#available-trulens-scorers "Direct link to Available TruLens scorers")

### RAG metrics[​](#rag-metrics "Direct link to RAG metrics")

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation (RAG) applications.

### Agent trace metrics[​](#agent-trace-metrics "Direct link to Agent trace metrics")

These scorers evaluate AI agent execution traces using goal-plan-action alignment.

Agent trace scorers require a `trace` argument and evaluate the full execution trace:

Python

    import mlflowfrom mlflow.genai.scorers.trulens import LogicalConsistency, ToolSelectiontraces = mlflow.search_traces(experiment_ids=["1"])results = mlflow.genai.evaluate(    data=traces,    scorers=[        LogicalConsistency(model="openai:/gpt-5-mini"),        ToolSelection(model="openai:/gpt-5-mini"),    ],)

## Create a scorer by name[​](#create-a-scorer-by-name "Direct link to Create a scorer by name")

You can dynamically create a scorer using `get_scorer` by passing the metric name as a string:

Python

    from mlflow.genai.scorers.trulens import get_scorerscorer = get_scorer(    metric_name="Groundedness",    model="openai:/gpt-5-mini",)feedback = scorer(    inputs="What is MLflow?",    outputs="MLflow is a platform for ML workflows.",    expectations={"context": "MLflow is an ML platform."},)

## Configuration[​](#configuration "Direct link to Configuration")

TruLens scorers accept common parameters that control evaluation behavior. All scorers require a `model` parameter.

Python

    from mlflow.genai.scorers.trulens import Groundedness, ContextRelevance# Common parametersscorer = Groundedness(    model="openai:/gpt-5-mini",    threshold=0.7,)# Default threshold is 0.5scorer = ContextRelevance(model="openai:/gpt-5-mini")

For metric-specific parameters and advanced usage options, see the [TruLens documentation](https://www.trulens.org/).
