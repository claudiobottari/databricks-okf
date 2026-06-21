---
title: Evaluate GenAI apps during development | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness
ingestedAt: "2026-06-18T08:14:48.062Z"
---

The [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) function provides an evaluation harness for GenAI applications. Instead of manually running your app and checking outputs one by one, MLflow Evaluation provides a structured way to feed in test data, run your app, and automatically score the results. This makes it easier to compare versions, track improvements, and share results across teams.

MLflow Evaluation connects offline testing with production monitoring. That means the same evaluation logic you use in development can also run in production, giving you a consistent view of quality across the entire AI lifecycle.

The [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) function systematically tests GenAI app quality by running it against test data ([evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/concepts/#evaluation-data) and applying [scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers)).

If you are new to evaluation, start with [10-minute demo: Evaluate a GenAI app](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/eval).

## When to use[​](#when-to-use "Direct link to When to use")

*   Nightly or weekly checks of your app against curated evaluation datasets
*   Validating prompt or model changes across app versions
*   Before a release or PR to prevent quality regressions

## Quick reference[​](#quick-reference "Direct link to Quick reference")

The `mlflow.genai.evaluate()` function runs your GenAI app against an evaluation dataset using specified scorers and optionally a prediction function or model ID, returning an `EvaluationResult`.

Python

    def mlflow.genai.evaluate(    data: Union[pd.DataFrame, List[Dict], mlflow.genai.datasets.EvaluationDataset],  # Test data.    scorers: list[mlflow.genai.scorers.Scorer],  # Quality metrics, built-in or custom.    predict_fn: Optional[Callable[..., Any]] = None,  # App wrapper. Used for direct evaluation only.    model_id: Optional[str] = None,  # Optional version tracking.) -> mlflow.models.evaluation.base.EvaluationResult:

*   For API details, see [Parameters for `mlflow.genai.evaluate()`](#parameters) or the [MLflow documentation](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate).
*   For details on `EvaluationDataset`, see [Building MLflow evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset).
*   For details on evaluation runs and logging, see [Evaluation runs in MLflow](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/evaluation-runs).

## Requirements[​](#requirements "Direct link to Requirements")

1.  Install MLflow and required packages.
    
    Bash
    
        pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    

### (Optional) Configure parallelization[​](#optional-configure-parallelization "Direct link to optional-configure-parallelization")

MLflow by default uses background threadpool to speed up the evaluation process. To configure the number of workers, set the environment variable `MLFLOW_GENAI_EVAL_MAX_WORKERS`.

Bash

    export MLFLOW_GENAI_EVAL_MAX_WORKERS=10

## Evaluation modes[​](#evaluation-modes "Direct link to evaluation-modes")

There are two evaluation modes:

*   [Direct evaluation (recommended)](#direct-eval). MLflow calls your app directly to generate traces for evaluation:
    
    1.  Runs your app on test inputs, capturing [traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/).
    2.  Applies [scorers or LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) to assess quality, creating [feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations).
    3.  Stores results in an [Evaluation Run](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/evaluation-runs) in the active MLflow experiment.
*   [Answer sheet evaluation](#answer-sheet). You provide pre-computed outputs or existing traces for evaluation:
    
    1.  Applies [scorers or LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) to assess quality on pre-computed outputs or [traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/), creating [feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations).
    2.  Stores results in an [Evaluation Run](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/evaluation-runs) in the active MLflow experiment.

## Direct evaluation (recommended)[​](#direct-evaluation-recommended "Direct link to direct-evaluation-recommended")

MLflow calls your GenAI app directly to generate and evaluate traces. You can either pass your application's entry point wrapped in a Python function (`predict_fn`) or, if your app is deployed as a Databricks Model Serving endpoint, pass that endpoint wrapped in [`to_predict_fn`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/eval-examples#eval-endpoint).

By calling your app directly, this mode enables you to reuse the scorers defined for offline evaluation in [production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring) since the resulting traces will be identical.

As shown in the diagram, data, your app, and selected scorers are provided as inputs to `mlflow.genai.evaluate()`, which runs the app and scorers in parallel and records output as traces and feedback.

![How evaluate works with tracing](https://docs.databricks.com/aws/en/assets/images/eval-with-tracing-823ef523d9ae152493ff181e77bc7c84.png)

### Data formats for direct evaluation[​](#data-formats-for-direct-evaluation "Direct link to Data formats for direct evaluation")

For schema details, see [Evaluation dataset reference](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets).

### Example using direct evaluation[​](#example-using-direct-evaluation "Direct link to Example using direct evaluation")

The following code shows an example of how to run the evaluation:

Python

    import mlflowfrom mlflow.genai.scorers import RelevanceToQuery, Safety# Your GenAI app with MLflow tracing@mlflow.tracedef my_chatbot_app(question: str) -> dict:    # Your app logic here    if "MLflow" in question:        response = "MLflow is an open-source platform for managing ML and GenAI workflows."    else:        response = "I can help you with MLflow questions."    return {"response": response}# Evaluate your appresults = mlflow.genai.evaluate(    data=[        {"inputs": {"question": "What is MLflow?"}},        {"inputs": {"question": "How do I get started?"}}    ],    predict_fn=my_chatbot_app,    scorers=[RelevanceToQuery(), Safety()])

### Rate limiting model calls[​](#rate-limiting-model-calls "Direct link to Rate limiting model calls")

When evaluating models with rate limits (such as third-party APIs or foundation model endpoints), wrap your predict function with rate-limiting logic. This example uses the library `ratelimit`:

Python

    import mlflowfrom mlflow.genai.scorers import RelevanceToQuery, Safetyfrom ratelimit import limits, sleep_and_retry# You can replace this with your own predict_fnpredict_fn = mlflow.genai.to_predict_fn("endpoints:/databricks-gpt-oss-20b")@sleep_and_retry@limits(calls=10, period=60)  # 10 calls per minutedef rate_limited_predict_fn(*args, **kwargs):  return predict_fn(*args, **kwargs)results = mlflow.genai.evaluate(    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],    predict_fn=predict_fn,    scorers=[RelevanceToQuery(), Safety()])

The above rate limit controls calls to your predict\_fn. You can also control the number of workers used to evaluate your agent by [configuring parallelization](#configure-parallelization).

## Answer sheet evaluation[​](#answer-sheet-evaluation "Direct link to answer-sheet-evaluation")

Use this mode when you can't - or don't want to - run your GenAI app directly during evaluation. For example, you already have outputs (for example, from external systems, historical traces, or batch jobs) and you just want to score them. You provide the inputs and the output, and `evaluate()` runs scorers and logs an evaluation run.

important

If you use an answer sheet with different traces than your production environment, you may need to re-write your scorer functions to use them for [production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring).

As shown in the diagram, you provide evaluation data and selected scorers as inputs to `mlflow.genai.evaluate()`. Evaluation data can consist of existing traces, or of inputs and pre-computed outputs. If inputs and pre-computed outputs are provided, `mlflow.genai.evaluate()` constructs traces from the inputs and outputs. For both input options, `mlflow.genai.evaluate()` runs the scorers on the traces and outputs feedback from the scorers.

![How evaluate works with answer sheet](https://docs.databricks.com/aws/en/assets/images/eval-with-answer-sheet-84f4ae4e7d0d1fda3594ad9995378852.png)

### Data formats for answer sheet evaluation[​](#data-formats-for-answer-sheet-evaluation "Direct link to Data formats for answer sheet evaluation")

For schema details, see [Evaluation dataset reference](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets).

**If inputs and outputs are provided**

**If existing traces are provided**

### Example using inputs and outputs[​](#example-using-inputs-and-outputs "Direct link to Example using inputs and outputs")

The following code shows an example of how to run the evaluation:

Python

    import mlflowfrom mlflow.genai.scorers import Safety, RelevanceToQuery# Pre-computed results from your GenAI appresults_data = [    {        "inputs": {"question": "What is MLflow?"},        "outputs": {"response": "MLflow is an open-source platform for managing machine learning workflows, including tracking experiments, packaging code, and deploying models."},    },    {        "inputs": {"question": "How do I get started?"},        "outputs": {"response": "To get started with MLflow, install it using 'pip install mlflow' and then run 'mlflow ui' to launch the web interface."},    }]# Evaluate pre-computed outputsevaluation = mlflow.genai.evaluate(    data=results_data,    scorers=[Safety(), RelevanceToQuery()])

### Example using existing traces[​](#example-using-existing-traces "Direct link to Example using existing traces")

The following code shows how to run the evaluation using existing traces:

Python

    import mlflow# Retrieve traces from productiontraces = mlflow.search_traces(    filter_string="trace.status = 'OK'",)# Evaluate problematic tracesevaluation = mlflow.genai.evaluate(    data=traces,    scorers=[Safety(), RelevanceToQuery()])

## View results in UI[​](#-view-results-in-ui "Direct link to -view-results-in-ui")

An evaluation run is like a test report that captures everything about how your app performed on a specific dataset. The evaluation run contains a trace for each row in your evaluation dataset annotated with [feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations) from each judge.

Using the evaluation run, you can view aggregate metrics and investigate test cases where your app performed poorly.

### Assessment summary[​](#assessment-summary "Direct link to Assessment summary")

1.  Click **Experiments** in the sidebar to display the Experiments page.
    
2.  Click on the name of your experiment to open it.
    
3.  In the left sidebar, click **Evaluation runs**. The right pane shows a table of traces.
    
    ![Evaluation runs table](https://docs.databricks.com/aws/en/assets/images/eval-runs-table-2c75f5ca715d14ce725027781b63ceab.png)
    
    If you do not see the Assessments with their **Pass** and **Fail** labels, scroll to the right or hover over the pane separator and click the left-pointing arrow.
    
    ![Expand table](https://docs.databricks.com/aws/en/assets/images/expand-pane-fbb56a0c40834f8da51bff95d8690b1e.gif)
    
4.  To see the rationale for the **Pass** or **Fail** label, hover over the label.
    
    ![Hover over label to show rationale](https://docs.databricks.com/aws/en/assets/images/rationale-9cc9a86e3ec21c1e060890d8485741e7.gif)
    

### Details and add feedback[​](#details-and-add-feedback "Direct link to Details and add feedback")

To see more details for each trace:

1.  Click on the request identifier in the **Request** column. A window appears showing the full trace, including inputs and outputs for each step.
    
    ![Request details window](https://docs.databricks.com/aws/en/assets/images/request-details-e0ca5297702b7bdcd95efa9b7c598b15.png)
    
2.  At the right, you can add Feedback or Expectations to apply to the response for this request. If you do not see the Assessments pane, click ![Assessments button](data:image/png;base64,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). To add a new Assessment, scroll down and click ![Add new assessment button](data:image/png;base64,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).
    
3.  You can use the arrows at either side of this window to step through the requests.
    
    ![Step through requests using arrows](https://docs.databricks.com/aws/en/assets/images/step-through-requests-6ba8423d7bfd92825d6e83b0682a79d7.png)
    

## Parameters for `mlflow.genai.evaluate()`[​](#-parameters-for-mlflowgenaievaluate "Direct link to -parameters-for-mlflowgenaievaluate")

This section describes each of the parameters used by `mlflow.genai.evaluate()`.

Python

    def mlflow.genai.evaluate(    data: Union[pd.DataFrame, List[Dict], mlflow.genai.datasets.EvaluationDataset],  # Test data.    scorers: list[mlflow.genai.scorers.Scorer],  # Quality metrics, built-in or custom.    predict_fn: Optional[Callable[..., Any]] = None,  # App wrapper. Used for direct evaluation only.    model_id: Optional[str] = None,  # Optional version tracking.) -> mlflow.models.evaluation.base.EvaluationResult:

### `data`[​](#data "Direct link to data")

The evaluation dataset must be in one of the following formats:

*   `EvaluationDataset` (recommended).
*   List of dictionaries, Pandas DataFrame, or Spark DataFrame.

If the data argument is provided as a DataFrame or list of dictionaries, it must follow the following schema. This is consistent with the schema used by [EvaluationDataset](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset). Databricks recommends using an `EvaluationDataset` as it enforces schema validation, in addition to tracking the lineage of each record.

### `scorers`[​](#scorers "Direct link to scorers")

List of quality metrics to apply. You can provide:

*   [Built-in scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers)
*   [Custom scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers)

See [Scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) for more details.

### `predict_fn`[​](#predict_fn "Direct link to predict_fn")

The GenAI app's entry point. This parameter is only used with [direct evaluation](#direct-eval). `predict_fn` must meet the following requirements:

*   Accept the keys from the `inputs` dictionary in `data` as keyword arguments.
*   Return a JSON-serializable dictionary.
*   Be instrumented with [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/).
*   Emit exactly one trace per call.

### `model_id`[​](#model_id "Direct link to model_id")

Optional model identifier to link results to your app version (for example, `"models:/my-app/1"`).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Evaluate your app](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Step-by-step guide to running your first evaluation.
*   [Build evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Create structured test data from production logs or scratch.
*   [Define custom scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) - Build metrics tailored to your specific use case.
