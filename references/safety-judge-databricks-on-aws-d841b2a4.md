---
title: Safety judge | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_safe
ingestedAt: "2026-06-18T08:15:03.941Z"
---

The `Safety` judge evaluates text content to identify potentially harmful, offensive, or inappropriate material. It returns a pass/fail assessment along with a detailed rationale explaining any safety concerns.

For API details, see the [MLflow documentation](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Safety).

For detailed documentation and additional examples, see the [MLflow Safety judge documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/response-quality/safety/).

## Prerequisites for running the examples[​](#prerequisites-for-running-the-examples "Direct link to Prerequisites for running the examples")

1.  Install MLflow and required packages.
    
    Python
    
        %pip install --upgrade "mlflow[databricks]>=3.4.0"dbutils.library.restartPython()
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    

## Usage examples[​](#usage-examples "Direct link to Usage examples")

The `Safety` judge can be invoked directly for single assessment or used with MLflow's evaluation framework for batch evaluation.

*   Invoke directly
*   Invoke with evaluate()

Python

    from mlflow.genai.scorers import Safety# Assess the safety of a single outputassessment = Safety(    outputs="MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.")print(assessment)

## Select the LLM that powers the judge[​](#select-the-llm-that-powers-the-judge "Direct link to Select the LLM that powers the judge")

By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument when you create the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name.

You can customize the Safety judge by specifying a different model:

Python

    from mlflow.genai.scorers import Safety# Use a different model for safety evaluationsafety_judge = Safety(    model="databricks:/databricks-claude-opus-4-5"  # Use a different model)# Run evaluation with Safety judgeeval_results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[safety_judge])

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Explore other built-in judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Learn about relevance, groundedness, and correctness judges
*   [Monitor safety in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Set up continuous safety monitoring for deployed applications
*   [Create custom safety guidelines with Guidelines judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/guidelines) - Define specific safety criteria for your use case
