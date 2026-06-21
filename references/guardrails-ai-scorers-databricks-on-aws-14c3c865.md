---
title: Guardrails AI scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/guardrails
ingestedAt: "2026-06-18T08:15:35.520Z"
---

[Guardrails AI](https://www.guardrailsai.com/) is a framework for validating LLM outputs using a community-driven hub of validators for safety, PII detection, content quality, and more. MLflow integrates with Guardrails AI so that you can use Guardrails validators as scorers, offering rule-based evaluation without requiring LLM calls.

## Requirements[​](#requirements "Direct link to Requirements")

Install the `guardrails-ai` package:

Python

    %pip install guardrails-ai

## Quick start[​](#quick-start "Direct link to Quick start")

To call a Guardrails AI scorer directly:

Python

    from mlflow.genai.scorers.guardrails import ToxicLanguagescorer = ToxicLanguage(threshold=0.7)feedback = scorer(    outputs="This is a professional and helpful response.",)print(feedback.value)  # "yes" or "no"

To call Guardrails AI scorers using [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate):

Python

    import mlflowfrom mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPIIeval_dataset = [    {        "inputs": {"query": "What is MLflow?"},        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",    },    {        "inputs": {"query": "How do I contact support?"},        "outputs": "You can reach us at support@example.com or call 555-0123.",    },]results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[        ToxicLanguage(threshold=0.7),        DetectPII(),    ],)

## Available Guardrails AI scorers[​](#available-guardrails-ai-scorers "Direct link to Available Guardrails AI scorers")

### Safety and content quality[​](#safety-and-content-quality "Direct link to Safety and content quality")

These scorers validate LLM outputs for safety, PII, and content quality concerns.

## Create a scorer by name[​](#create-a-scorer-by-name "Direct link to Create a scorer by name")

You can dynamically create a scorer using `get_scorer` by passing the validator name as a string:

Python

    from mlflow.genai.scorers.guardrails import get_scorerscorer = get_scorer(    validator_name="ToxicLanguage",    threshold=0.7,)feedback = scorer(    outputs="This is a professional response.",)

## Configuration[​](#configuration "Direct link to Configuration")

Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor.

Python

    from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII, DetectJailbreak# Toxicity detection with custom thresholdscorer = ToxicLanguage(    threshold=0.7,    validation_method="sentence",)# PII detection with custom entity typespii_scorer = DetectPII(    pii_entities=["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"],)# Jailbreak detection with custom sensitivityjailbreak_scorer = DetectJailbreak(    threshold=0.9,)

For validator-specific parameters and additional validators, see the [Guardrails AI documentation](https://www.guardrailsai.com/) and the [Guardrails Hub](https://guardrailsai.com/hub).
