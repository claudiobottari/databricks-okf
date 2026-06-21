---
title: Scorer lifecycle management API reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring
ingestedAt: "2026-06-18T08:15:05.999Z"
---

The MLflow scorer lifecycle methods (register, start, update, and stop) control scorers that run continuous quality assessment on production traces. This page is the API reference for those methods. For a task-based guide to production monitoring on Databricks, see [Monitor GenAI apps in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring).

## Scorer instance methods[​](#scorer-instance-methods "Direct link to Scorer instance methods")

### `Scorer.register()`[​](#scorerregister "Direct link to scorerregister")

**API Reference:** [`Scorer.register`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.register)

Register a custom scorer function with the server. Used for scorers created with the [`@scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.scorer) decorator.

Python

    @scorerdef custom_scorer(outputs):    return len(str(outputs.get("response", "")))# Register the custom scorermy_scorer = custom_scorer.register(name="response_length")

**Parameters:**

*   `name` (str): Unique name for the scorer within the experiment. Defaults to the existing name of the scorer.

**Returns:** New [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) instance with server registration

### `Scorer.start()`[​](#scorerstart "Direct link to scorerstart")

**API Reference:** [`Scorer.start`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.start)

Begin online evaluation with the specified sampling configuration.

Python

    from mlflow.genai.scorers import ScorerSamplingConfig# Start monitoring with samplingactive_scorer = registered_scorer.start(    sampling_config=ScorerSamplingConfig(        sample_rate=0.5,        filter_string="trace.status = 'OK'"    ),)

**Parameters:**

*   `name` (str): Name of the scorer. If not provided, defaults to the current name of the scorer.
*   `sampling_config` ([`ScorerSamplingConfig`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.ScorerSamplingConfig)): Trace sampling configuration
    *   `sample_rate` (float): Fraction of traces to evaluate (0.0-1.0). Default: 1.0
    *   `filter_string` (str, optional): MLflow-compatible filter for trace selection

**Returns:** New [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) instance in active state

### `Scorer.update()`[​](#-scorerupdate "Direct link to -scorerupdate")

**API Reference:** [`Scorer.update`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.update)

Modify the sampling configuration of an active scorer. This is an immutable operation.

Python

    # Update sampling rate (returns new scorer instance)updated_scorer = active_scorer.update(    sampling_config=ScorerSamplingConfig(        sample_rate=0.8,    ),)# Original scorer remains unchangedprint(f"Original: {active_scorer.sample_rate}")  # 0.5print(f"Updated: {updated_scorer.sample_rate}")   # 0.8

**Parameters:**

*   `name` (str): Name of the scorer. If not provided, defaults to the current name of the scorer.
*   `sampling_config` ([`ScorerSamplingConfig`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.ScorerSamplingConfig)): Trace sampling configuration
    *   `sample_rate` (float): Fraction of traces to evaluate (0.0-1.0). Default: 1.0
    *   `filter_string` (str, optional): MLflow-compatible filter for trace selection

**Returns:** New [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) instance with updated configuration

### `Scorer.stop()`[​](#scorerstop "Direct link to scorerstop")

**API Reference:** [`Scorer.stop`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.stop)

Stop online evaluation by setting sample rate to 0. Keeps the scorer registered.

Python

    # Stop monitoring but keep scorer registeredstopped_scorer = active_scorer.stop()print(f"Sample rate: {stopped_scorer.sample_rate}")  # 0

**Parameters:**

*   `name` (str): Name of the scorer. If not provided, defaults to the current name of the scorer.

**Returns:** New [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) instance with sample\_rate=0

## Scorer registry functions[​](#scorer-registry-functions "Direct link to Scorer registry functions")

### `mlflow.genai.scorers.get_scorer()`[​](#-mlflowgenaiscorersget_scorer "Direct link to -mlflowgenaiscorersget_scorer")

**API Reference:** [`get_scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.get_scorer)

Retrieve a registered scorer by name.

Python

    from mlflow.genai.scorers import get_scorer# Get existing scorer by nameexisting_scorer = get_scorer(name="safety_monitor")print(f"Current sample rate: {existing_scorer.sample_rate}")

**Parameters:**

*   `name` (str): Name of the registered scorer

**Returns:** [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) instance

### `mlflow.genai.scorers.list_scorers()`[​](#mlflowgenaiscorerslist_scorers "Direct link to mlflowgenaiscorerslist_scorers")

**API Reference:** [`list_scorers`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.list_scorers)

List all registered scorers for the current experiment.

Python

    from mlflow.genai.scorers import list_scorers# List all registered scorersall_scorers = list_scorers()for scorer in all_scorers:    print(f"Name: {scorer._server_name}")    print(f"Sample rate: {scorer.sample_rate}")    print(f"Filter: {scorer.filter_string}")

**Returns:** List of [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) instances

### `mlflow.genai.scorers.delete_scorer()`[​](#-mlflowgenaiscorersdelete_scorer "Direct link to -mlflowgenaiscorersdelete_scorer")

**API Reference:** [`delete_scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.delete_scorer)

Delete a registered scorer by name.

Python

    from mlflow.genai.scorers import delete_scorer# Delete existing scorer by namedelete_scorer(name="safety_monitor")

**Parameters:**

*   `name` (str): Name of the registered scorer

**Returns:** None

## Scorer properties[​](#scorer-properties "Direct link to Scorer properties")

### `Scorer.sample_rate`[​](#scorersample_rate "Direct link to scorersample_rate")

Current sampling rate (0.0-1.0). Returns 0 for stopped scorers.

Python

    print(f"Sampling {scorer.sample_rate * 100}% of traces")

### `Scorer.filter_string`[​](#scorerfilter_string "Direct link to scorerfilter_string")

Current trace filter string for MLflow trace selection.

Python

    print(f"Filter: {scorer.filter_string}")

## Configuration classes[​](#configuration-classes "Direct link to Configuration classes")

### `ScorerSamplingConfig`[​](#scorersamplingconfig "Direct link to scorersamplingconfig")

**API Reference:** [`ScorerSamplingConfig`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.ScorerSamplingConfig)

Data class that holds sampling configuration for a scorer.

Python

    from mlflow.genai import ScorerSamplingConfigconfig = ScorerSamplingConfig(    sample_rate=0.5,    filter_string="trace.status = 'OK'")

**Attributes:**

*   `sample_rate` (float, optional): Sampling rate between 0.0 and 1.0
*   `filter_string` (str, optional): MLflow trace filter

## Metric backfill[​](#-metric-backfill "Direct link to -metric-backfill")

### `backfill_scorers()`[​](#backfill_scorers "Direct link to backfill_scorers")

Python

    from databricks.agents.scorers import backfill_scorers, BackfillScorerConfigjob_id = backfill_scorers(    experiment_id="your-experiment-id",    scorers=[        BackfillScorerConfig(scorer=safety_scorer, sample_rate=0.8),        BackfillScorerConfig(scorer=response_length, sample_rate=0.9)    ],    start_time=datetime(2024, 1, 1),    end_time=datetime(2024, 1, 31))

**Parameters:**

All parameters are keyword-only.

*   **`experiment_id`** _(str, optional)_: The ID of the experiment to backfill. If not provided, uses the current experiment context
*   **`scorers`** _(Union\[List\[BackfillScorerConfig\], List\[str\]\], required)_: List of `BackfillScorerConfig` objects with custom sample rates (if sample\_rate is not provided in BackfillScorerConfig, defaults to the registered scorer's sample rate), OR list of scorer names (strings) to use current sample rates from the experiment's scheduled scorers. Cannot be empty.
*   **`start_time`** _(datetime, optional)_: Start time for backfill evaluation. If not provided, no start time constraint is applied
*   **`end_time`** _(datetime, optional)_: End time for backfill evaluation. If not provided, no end time constraint is applied

**Returns:** Job ID of the created backfill job for status tracking (str)
