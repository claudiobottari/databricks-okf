---
title: Correctness judge | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_correct
ingestedAt: "2026-06-18T08:15:00.004Z"
---

The `Correctness` judge assesses whether your GenAI application's response is factually correct by comparing it against provided ground truth information (`expected_facts` or `expected_response`). This built-in LLM judge is designed for evaluating application responses against known correct answers.

For API details, see the [MLflow documentation](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Correctness).

For detailed documentation and additional examples, see the [MLflow Correctness judge documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/response-quality/correctness/).

## Prerequisites for running the examples[​](#prerequisites-for-running-the-examples "Direct link to Prerequisites for running the examples")

1.  Install MLflow and required packages.
    
    Python
    
        %pip install --upgrade "mlflow[databricks]>=3.4.0"dbutils.library.restartPython()
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    

## Usage examples[​](#usage-examples "Direct link to Usage examples")

*   Invoke directly
*   Invoke with evaluate()

Python

    from mlflow.genai.scorers import Correctnesscorrectness_judge = Correctness()# Example 1: Response contains expected factsfeedback = correctness_judge(    inputs={"request": "What is MLflow?"},    outputs={"response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."},    expectations={        "expected_facts": [            "MLflow is open-source",            "MLflow is an AI engineering platform"        ]    })print(feedback.value)  # "yes"print(feedback.rationale)  # Explanation of which facts are supported# Example 2: Response missing or contradicting factsfeedback = correctness_judge(    inputs={"request": "When was MLflow released?"},    outputs={"response": "MLflow was released in 2017."},    expectations={"expected_facts": ["MLflow was released in June 2018"]})# Example 3: Using expected_response instead of expected_factsfeedback = correctness_judge(    inputs={"request": "What is the capital of France?"},    outputs={"response": "The capital of France is Paris."},    expectations={"expected_response": "Paris is the capital of France."})

### Alternative: Using expected\_response[​](#alternative-using-expected_response "Direct link to Alternative: Using expected_response")

You can also use `expected_response` instead of `expected_facts`:

Python

    eval_dataset_with_response = [    {        "inputs": {"query": "What is MLflow?"},        "outputs": {            "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."        },        "expectations": {            "expected_response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize their AI applications."        },    }]# Run evaluation with expected_responseeval_results = mlflow.genai.evaluate(    data=eval_dataset_with_response,    scorers=[Correctness()])

tip

Use `expected_facts` rather than `expected_response` for more flexible evaluation - the response doesn't need to match word-for-word, just contain the key facts.

## Select the LLM that powers the judge[​](#select-the-llm-that-powers-the-judge "Direct link to Select the LLM that powers the judge")

By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument when you create the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name.

You can customize the judge by providing a different judge model:

Python

    from mlflow.genai.scorers import Correctness# Use a different judge modelcorrectness_judge = Correctness(    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model)# Use in evaluationeval_results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[correctness_judge])

## Interpret results[​](#interpret-results "Direct link to Interpret results")

The judge returns a `Feedback` object with:

*   **`value`**: "yes" if response is correct, "no" if incorrect
*   **`rationale`**: Detailed explanation of which facts are supported or missing

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Explore other built-in judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Learn about other built-in quality evaluation judges
*   [Create custom judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) - Build domain-specific evaluation judges
*   [Run evaluations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Use judges in comprehensive application evaluation
