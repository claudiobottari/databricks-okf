---
title: Monitor GenAI apps in production | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring
ingestedAt: "2026-06-18T08:15:28.561Z"
---

Production monitoring lets you automatically run MLflow 3 scorers on traces from your GenAI apps to continuously assess quality. You schedule scorers against an MLflow experiment, and the monitoring service evaluates a configurable sample of incoming traces. Results are attached as feedback to each evaluated trace.

Production monitoring includes the following:

*   Automated quality assessment using built-in or custom scorers, including [multi-turn judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations) for evaluating entire conversations.
*   Configurable sampling rates so you can control the tradeoff between coverage and computational cost.
*   Use the same scorers in development and production to ensure consistent evaluation.
*   Continuous quality assessment with monitoring running in the background.

note

MLflow 3 production monitoring is compatible with traces logged from MLflow 2.

## Prerequisites[​](#prerequisites "Direct link to prerequisites")

Before setting up production monitoring, ensure you have:

*   **MLflow experiment**: An MLflow experiment where traces are being logged. If no experiment is specified, the active experiment is used.
*   **Instrumented production application**: Your GenAI app must log traces using MLflow Tracing. See the [Production Tracing guide](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing).
*   **Defined scorers**: Tested [scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) that work with your application's trace format. If you used your production app as the `predict_fn` in `mlflow.genai.evaluate()` during development, your scorers are likely already compatible.
*   **Serverless budget policy**: If your workspace does not allow the default serverless budget policy, set a policy on the MLflow experiment before registering scorers. See [Configure a serverless budget policy for an MLflow experiment](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/serverless-budget-policy).

*   **SQL warehouse ID (for Unity Catalog traces)**: If your traces are stored in Unity Catalog, you must configure a SQL warehouse ID for monitoring to work. See [Enable production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog#enable-production-monitoring).

## Get started[​](#get-started "Direct link to Get started")

To set up production monitoring, you register a scorer with your MLflow experiment and then start it with a sampling configuration. This two-step pattern (`.register()` then `.start()`) applies to all scorer types.

note

At any given time, at most 20 scorers can be associated with an experiment for continuous quality monitoring.

For more information about scorers, see the following:

*   [Scorers and LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers)
*   [Custom judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/)
*   [Code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers)

The following sections describe how to use the different types of judges and how to combine them. Expand a section to learn more.

Create and schedule LLM judges using the UI

### Create and schedule LLM judges using the UI[​](#create-and-schedule-llm-judges-using-the-ui "Direct link to Create and schedule LLM judges using the UI")

You can use the MLflow experiment UI to create and test scorers based on LLM judges.

To create a new LLM judge:

1.  Navigate to the **Judges** tab in the MLflow Experiment UI.
    
    ![Judges tab of MLflow experiment.](https://docs.databricks.com/aws/en/assets/images/judges-tab-97111d007773446fb04b3b3c9498807d.png)
    
2.  Click **New LLM judge**.
    
    ![Create LLM judge form.](https://docs.databricks.com/aws/en/assets/images/create-judge-form-542d97d94426cdb816197a0a788acba7.png)
    
3.  Specify what the scorer will evaluate by selecting **Traces** or **Sessions**.
    
4.  Enter a name for the judge.
    
5.  Click the arrow as shown to display the **Evaluation criteria** section.
    
    ![Evaluation criteria.](https://docs.databricks.com/aws/en/assets/images/eval-criteria-9429e66ac4dbf189f7ab2f1959f6dc42.png)
    
6.  From the drop-down menu, select the type of judge. Some judge types allow you to enter custom instructions including variables.
    
7.  Click the arrow as shown to display the **Automatic evaluation** section.
    
    ![Automatic evaluation settings.](https://docs.databricks.com/aws/en/assets/images/automatic-eval-208e33a51e88bf560ce39f1fadc9cf98.png)
    
8.  Set the **Run on all future traces** toggle as desired.
    
9.  (Optional) Under **Advanced settings**, adjust the **Sample rate** and **Filter string** to control which traces are evaluated.
    
10.  (Optional) To test the new judge on a set of existing traces:
     
     1.  Click **Select traces** in the left pane. A pop-up appears.
     2.  Select the traces to run and click **Select (n)**.
     3.  Click **Run judge**. The traces are evaluated and the results are displayed.
     4.  Review the results. Use the **Next** and **Previous** buttons to step through the results for each selected trace.
     5.  If necessary, edit the judge and iterate until you are happy with the judge's performance.
11.  To create the judge, click **Create judge**.
     

You cannot create a custom code judge using the UI. To see template code that you can copy to your notebook and edit as needed, do the following:

1.  Click the dropdown arrow next to the **New LLM judge** button, and select **Custom code judge**.
    
    ![LLM judge drop-down menu.](https://docs.databricks.com/aws/en/assets/images/custom-code-menu-item-d6f772247da28804ef6baf035dfdd8ce.png)
    
2.  A pop-up appears with instructions and template code showing how to define and run the custom code judge.
    

Use built-in LLM judges

### Use built-in LLM judges[​](#use-built-in-llm-judges "Direct link to Use built-in LLM judges")

MLflow provides several [built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) that you can use out-of-the-box.

Python

    from mlflow.genai.scorers import Safety, ScorerSamplingConfig# Register the scorer with a name and start monitoringsafety_judge = Safety().register(name="my_safety_judge")  # name must be unique to experimentsafety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.7))

By default, each judge uses a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model to instead use a Databricks model serving endpoint by using the `model` argument in the scorer definition. The model must be specified in the format `databricks:/<databricks-serving-endpoint-name>`.

Python

    safety_judge = Safety(model="databricks:/databricks-gpt-oss-20b").register(name="my_custom_safety_judge")

Use Guidelines LLM Judges

### Use Guidelines LLM Judges[​](#use-guidelines-llm-judges "Direct link to Use Guidelines LLM Judges")

[Guidelines LLM Judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/guidelines) evaluate inputs and outputs using pass/fail natural language criteria.

Python

    from mlflow.genai.scorers import Guidelines# Create and register the guidelines scorerenglish_judge = Guidelines(  name="english",  guidelines=["The response must be in English"]).register(name="is_english")  # name must be unique to experiment# Start monitoring with the specified sample rateenglish_judge = english_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.7))

Like built-in judges, you can change the judge model to instead use a Databricks model serving endpoint.

Python

    english_judge = Guidelines(  name="english",  guidelines=["The response must be in English"],  model="databricks:/databricks-gpt-oss-20b",).register(name="custom_is_english")

Use LLM Judges with custom prompts

### Use LLM Judges with custom prompts[​](#use-llm-judges-with-custom-prompts "Direct link to Use LLM Judges with custom prompts")

For more flexibility than Guidelines judges, use [LLM Judges with custom prompts](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) which allow for multi-level quality assessment with customizable choice categories.

Python

    from typing import Literalfrom mlflow.genai import make_judgefrom mlflow.genai.scorers import ScorerSamplingConfig# Create a custom judge using make_judgeformality_judge = make_judge(    name="formality",    instructions="""You will look at the response and determine the formality of the response.Request: {{ inputs }}Response: {{ outputs }}Evaluate whether the response is formal, somewhat formal, or not formal.A response is somewhat formal if it mentions friendship, etc.""",    feedback_value_type=Literal["formal", "semi_formal", "not_formal"],    model="databricks:/databricks-gpt-oss-20b",  # optional)# Register the custom judge and start monitoringregistered_judge = formality_judge.register(name="my_formality_judge")  # name must be unique to experimentregistered_judge = registered_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.1))

Use custom scorer functions

### Use custom scorer functions[​](#use-custom-scorer-functions "Direct link to Use custom scorer functions")

For maximum flexibility, define and use a [custom scorer function](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers).

Custom scorer requirements for production monitoring

*   **Only `@scorer` decorator-based scorers are supported.** Class-based `Scorer` subclasses cannot be registered for production monitoring. If you need a class-based scorer, refactor it to use the `@scorer` decorator instead.
*   **Scorers must be defined and registered from a Databricks notebook.** The monitoring service serializes the scorer function code for remote execution, and this serialization requires the notebook environment. Scorers defined in standalone Python files or local IDE environments cannot be serialized for production monitoring.
*   **Scorers must be self-contained.** Because scorer functions are serialized as code for remote execution, all imports must be done inline within the function body. The function cannot reference variables, objects, or modules defined outside of it.

When defining custom scorers, do not use type hints that need to be imported in the function signature. If the scorer function body uses packages that need to be imported, import these packages inline within the function to ensure proper serialization.

Some packages are available by default without the need for an inline import. These include `databricks-agents`, `mlflow-skinny`, `openai`, and all packages included in [Serverless environment version 2](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/two).

Python

    from mlflow.genai.scorers import scorer, ScorerSamplingConfig# Custom metric: Check if response mentions Databricks@scorerdef mentions_databricks(outputs):    """Check if the response mentions Databricks"""    return "databricks" in str(outputs.get("response", "")).lower()# Register and start monitoringdatabricks_scorer = mentions_databricks.register(name="databricks_mentions")databricks_scorer = databricks_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))

For more custom scorer examples, see [Code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers).

Use multi-turn judges

### Use multi-turn judges[​](#use-multi-turn-judges "Direct link to Use multi-turn judges")

Production monitoring supports [multi-turn judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers#multi-turn-judges) that evaluate entire conversations rather than individual traces. These judges assess quality patterns across multiple interactions, such as user frustration and conversation completeness. Multi-turn judges are registered and started the same way as single-turn judges.

The monitoring job automatically groups traces into conversations based on the `mlflow.trace.session` tag. Multi-turn judges run after a conversation is considered complete — by default, a conversation is complete when no new traces with that session ID are ingested for **5 minutes**. To configure this buffer, set the [`MLFLOW_ONLINE_SCORING_DEFAULT_SESSION_COMPLETION_BUFFER_SECONDS`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.environment_variables.html#mlflow.environment_variables.MLFLOW_ONLINE_SCORING_DEFAULT_SESSION_COMPLETION_BUFFER_SECONDS) environment variable on the monitoring job.

For the complete list of available multi-turn judges, see [Multi-turn judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers#multi-turn-judges). For details on conversation evaluation, see [Evaluate conversations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations).

Python

    from mlflow.genai.scorers import (    ConversationCompleteness,    UserFrustration,    ScorerSamplingConfig,)# Register and start multi-turn judges just like single-turn judgescompleteness_scorer = ConversationCompleteness().register(name="conversation_completeness")completeness_scorer = completeness_scorer.start(    sampling_config=ScorerSamplingConfig(sample_rate=1.0),)frustration_scorer = UserFrustration().register(name="user_frustration")frustration_scorer = frustration_scorer.start(    sampling_config=ScorerSamplingConfig(sample_rate=1.0),)

Combine judges

### Combine judges[​](#combine-judges "Direct link to Combine judges")

You can combine single-turn judges and multi-turn judges in the same experiment. Register and start each scorer individually.

Python

    from mlflow.genai.scorers import Safety, Guidelines, UserFrustration, ScorerSamplingConfig# Single-turn judgessafety_judge = Safety().register(name="safety")safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=1.0))english_judge = Guidelines(    name="english",    guidelines=["The response must be in English"]).register(name="is_english")english_judge = english_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))# Multi-turn judgefrustration_judge = UserFrustration().register(name="frustration")frustration_judge = frustration_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.3))

## View results[​](#view-results "Direct link to View results")

After scheduling scorers, allow 15-20 minutes for initial processing. Then:

1.  Navigate to your MLflow experiment.
2.  Open the **Traces** tab to see assessments attached to traces.
3.  Use the monitoring dashboards to track quality trends.

For multi-turn judges, assessments are attached to the first trace in each session. See [How assessments are stored](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations#how-assessments-are-stored) for details.

## Best practices[​](#best-practices "Direct link to Best practices")

### Sampling strategy[​](#sampling-strategy "Direct link to Sampling strategy")

*   For critical scorers such as safety and security checks, use `sample_rate=1.0`.
    
*   For expensive scorers, such as complex LLM judges, use lower sample rates (0.05-0.2).
    
*   For iterative improvement during development, use moderate rates (0.3-0.5).
    
*   Balance coverage with cost, as shown in the following examples:
    
    Python
    
        # High-priority scorers: higher samplingsafety_judge = Safety().register(name="safety")safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=1.0))  # 100% coverage for critical safety# Expensive scorers: lower samplingcomplex_scorer = ComplexCustomScorer().register(name="complex_analysis")complex_scorer = complex_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=0.05))  # 5% for expensive operations
    

### Filter traces[​](#filter-traces "Direct link to Filter traces")

Use the `filter_string` parameter in `ScorerSamplingConfig` to control which traces a scorer evaluates. This uses the same filter syntax as `mlflow.search_traces()`.

Python

    from mlflow.genai.scorers import Safety, ScorerSamplingConfig# Only evaluate traces that completed successfullysafety_judge = Safety().register(name="safety")safety_judge = safety_judge.start(    sampling_config=ScorerSamplingConfig(        sample_rate=1.0,        filter_string="attributes.status = 'OK'"    ),)

You can combine multiple conditions:

Python

    import time# Evaluate successful traces from the last 24 hoursone_day_ago = int((time.time() - 86400) * 1000)safety_judge = safety_judge.start(    sampling_config=ScorerSamplingConfig(        sample_rate=0.5,        filter_string=f"attributes.status = 'OK' AND attributes.timestamp_ms > {one_day_ago}"    ),)

### Custom scorer design[​](#custom-scorer-design "Direct link to Custom scorer design")

Keep custom scorers self-contained, as shown in the following example:

Python

    @scorerdef well_designed_scorer(inputs, outputs):    # All imports inside the function    import re    import json    # Handle missing data gracefully    response = outputs.get("response", "")    if not response:        return 0.0    # Return consistent types    return float(len(response) > 100)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Scorers not running[​](#scorers-not-running "Direct link to Scorers not running")

If scorers aren't executing, check the following:

1.  **Check experiment**: Ensure that traces are logged to the experiment, not to individual runs.
2.  **Sampling rate**: With low sample rates, it might take time to see results.
3.  **Verify filter string**: Ensure your `filter_string` matches actual traces.

### Serialization issues[​](#serialization-issues "Direct link to Serialization issues")

Custom scorers for production monitoring are serialized so they can be executed remotely by the monitoring service. This imposes several constraints:

*   **Notebook requirement**: Custom `@scorer` functions must be defined and registered from a Databricks notebook. The serialization mechanism relies on the notebook environment.
*   **Self-contained functions**: All imports must be inline within the function body. References to external variables, modules, or objects defined outside the function are not captured during serialization.
*   **No class-based scorers**: Only `@scorer` decorator-based scorers can be registered. Class-based `Scorer` subclasses cannot be serialized for remote execution.
*   **No type hints requiring imports**: Type hints in the function signature that require import statements (for example, `List` from `typing`) cause serialization failures.

When you create a custom scorer, include imports in the function definition.

Python

    # Avoid external dependenciesimport external_library  # Outside function@scorerdef bad_scorer(outputs):    return external_library.process(outputs)# Include imports in the function definition@scorerdef good_scorer(outputs):    import json  # Inside function    return len(json.dumps(outputs))# Avoid using type hints in scorer function signature that requires importsfrom typing import List@scorerdef scorer_with_bad_types(outputs: List[str]):    return False# Class-based scorers are not supported for production monitoringclass MyScorer(Scorer):    name: str = "my_scorer"    def __call__(self, outputs):        return len(outputs) > 10

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Manage production scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/manage-production-scorers) - Manage the lifecycle of your production scorers.
*   [Backfill historical traces with scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/backfill-scorers) - Retroactively apply scorers to historical traces.
*   [Archive traces to a Delta table](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/archive-traces) - Save traces and assessments to a Delta table.
*   [Code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) - Build scorers tailored to your needs.
*   [Evaluate conversations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations) - Learn about multi-turn conversation evaluation and multi-turn judges.
*   [Building MLflow evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Use monitoring results to improve quality.

## Reference guides[​](#reference-guides "Direct link to Reference guides")

*   [Scorer lifecycle management API reference](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring) - API reference for scorer lifecycle management.
*   [Scorers and LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Understand the metrics that power monitoring.
*   [Evaluate GenAI apps during development](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) - How offline evaluation relates to production.
