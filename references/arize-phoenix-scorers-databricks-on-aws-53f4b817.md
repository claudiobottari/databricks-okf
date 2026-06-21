---
title: Arize Phoenix scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/phoenix
ingestedAt: "2026-06-18T08:15:37.499Z"
---

    import mlflowfrom mlflow.genai.scorers.phoenix import Hallucination, Relevanceeval_dataset = [    {        "inputs": {"query": "What is MLflow?"},        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",        "expectations": {            "context": "MLflow is an ML platform for experiment tracking and model deployment."        },    },    {        "inputs": {"query": "How do I track experiments?"},        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",        "expectations": {            "context": "MLflow provides APIs like mlflow.start_run() for experiment tracking."        },    },]results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[        Hallucination(model="databricks:/databricks-gpt-5-mini"),        Relevance(model="databricks:/databricks-gpt-5-mini"),    ],)
