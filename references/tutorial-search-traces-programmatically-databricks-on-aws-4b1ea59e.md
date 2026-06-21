---
title: "Tutorial: Search traces programmatically | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/search-traces-examples
ingestedAt: "2026-06-18T08:18:02.146Z"
---

This tutorial provides simple examples to get started with [mlflow.search\_traces()](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces). For details on searching traces, see [Search traces programmatically](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk).

## Environment setup[​](#environment-setup "Direct link to Environment setup")

Install required packages:

*   `mlflow[databricks]`: Use the latest version of MLflow to get more features and improvements.
*   `openai`: This app will use the OpenAI API client to call Databricks-hosted models.

Python

    %pip install -qq --upgrade "mlflow[databricks]>=3.1.0" openaidbutils.library.restartPython()

Create an MLflow experiment. If you are using a Databricks notebook, you can skip this step and use the default notebook experiment. Otherwise, follow the [environment setup quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment) to create the experiment and connect to the MLflow Tracking server.

## Generate traces for analysis[​](#generate-traces-for-analysis "Direct link to Generate traces for analysis")

This simple app generates traces to use with `search_traces()`.

Python

    import mlflowfrom databricks_openai import DatabricksOpenAImlflow.openai.autolog()@mlflow.tracedef my_app(message: str) -> str:    # Create an OpenAI client that is connected to Databricks-hosted LLMs    client = DatabricksOpenAI()    response = client.chat.completions.create(        model="databricks-claude-sonnet-4",        messages=[            {                "role": "system",                "content": "You are a helpful assistant. Give brief, 1-2 sentence responses.",            },            {                "role": "user",                "content": message,            },        ]    )    # Add examples of custom metadata and tags    mlflow.update_current_trace(        metadata={            "mlflow.trace.user": 'name@my_company.com',        },        tags={            "environment": "production",        },    )    return response.choices[0].message.content

Python

    my_app("What is MLflow and how does it help with GenAI?")my_app("What is ML vs. AI?")my_app("What is MLflow and how does it help with machine learning?")

## Quick reference[​](#quick-reference "Direct link to Quick reference")

Python

    # Search by statusmlflow.search_traces(filter_string="trace.status = 'OK'")mlflow.search_traces(filter_string="trace.status = 'ERROR'")# Search by timemlflow.search_traces(filter_string="trace.timestamp_ms > 1749006880539")mlflow.search_traces(filter_string="trace.execution_time_ms > 2500")# Search by metadatamlflow.search_traces(filter_string="metadata.`mlflow.trace.user` = 'name@my_company.com'")# Search by tagsmlflow.search_traces(filter_string="tag.environment = 'production'")mlflow.search_traces(filter_string="tag.`mlflow.traceName` = 'my_app'")# Combined filters (AND only)mlflow.search_traces(    filter_string="trace.status = 'OK' AND tag.environment = 'production'")traces = mlflow.search_traces()traces

`mlflow.search_traces()` returns a pandas DataFrame or list of [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects with these fields:

Output

    ['trace_id', 'trace', 'client_request_id', 'state', 'request_time', 'execution_duration', 'request', 'response', 'trace_metadata', 'tags', 'spans', 'assessments']

## Search examples[​](#search-examples "Direct link to Search examples")

When you run this tutorial, the code cells below will show search results.

### Search by status[​](#search-by-status "Direct link to Search by status")

Searching by status lets you find successful, failed, or in-progress traces.

Python

    mlflow.search_traces(filter_string="trace.status = 'OK'")

Python

    mlflow.search_traces(filter_string="trace.status != 'ERROR'")

### Search by timestamp[​](#search-by-timestamp "Direct link to Search by timestamp")

Time must be specified in milliseconds, using Unix timestamps.

Find recent traces from the last 5 minutes:

Python

    import timefrom datetime import datetimecurrent_time_ms = int(time.time() * 1000)five_minutes_ago = current_time_ms - (5 * 60 * 1000)mlflow.search_traces(    filter_string=f"trace.timestamp_ms > {five_minutes_ago}")

Search over a date range:

Python

    start_date = int(datetime(2026, 1, 1).timestamp() * 1000)end_date = int(datetime(2026, 1, 31).timestamp() * 1000)mlflow.search_traces(    filter_string=f"trace.timestamp_ms > {start_date} AND attributes.timestamp_ms < {end_date}")

You can also use the 'timestamp' alias instead of 'timestamp\_ms':

Python

    mlflow.search_traces(filter_string=f"trace.timestamp > {five_minutes_ago}")

### Search by execution time[​](#search-by-execution-time "Direct link to Search by execution time")

Find slow traces:

Python

    mlflow.search_traces(filter_string="trace.execution_time_ms > 2500")

You can also use the 'latency' alias instead of 'execution\_time\_ms':

Python

    mlflow.search_traces(filter_string="trace.latency > 1000")

### Search by metadata[​](#search-by-metadata "Direct link to Search by metadata")

Remember to use backticks for metadata names with dots.

Search custom metadata for a specific user:

Python

    mlflow.search_traces(filter_string="metadata.`mlflow.trace.user` = 'name@my_company.com'")

### Search by tags[​](#search-by-tags "Direct link to Search by tags")

Remember to use backticks for tag names with dots.

Search system tags:

Python

    mlflow.search_traces(    filter_string="tag.`mlflow.traceName` = 'my_app'")

Search custom tags set using [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace):

Python

    mlflow.search_traces(filter_string="tag.environment = 'production'")

### Complex filters[​](#complex-filters "Direct link to Complex filters")

Only AND is supported, not OR.

Find recent successful production traces:

Python

    current_time_ms = int(time.time() * 1000)one_hour_ago = current_time_ms - (60 * 60 * 1000)mlflow.search_traces(    filter_string=f"trace.status = 'OK' AND "                  f"trace.timestamp_ms > {one_hour_ago} AND "                  f"tag.environment = 'production'")

Find fast traces from a specific user:

Python

    mlflow.search_traces(    filter_string="trace.execution_time_ms < 2500 AND "                  "metadata.`mlflow.trace.user` = 'name@my_company.com'")

Find traces from a specific function that exceed a performance threshold:

Python

    mlflow.search_traces(    filter_string="tag.`mlflow.traceName` = 'my_app' AND "                  "trace.execution_time_ms > 1000")

## Next steps[​](#next-steps "Direct link to Next steps")

In general, you will call [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces) to extract a set of traces and then do further analysis or processing of the returned DataFrame or list of `Trace` objects.

For more advanced examples, see:

*   [Tutorial: Trace and analyze users and environments](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces-tutorial) - Run an example of adding context metadata to traces and analyzing the results
*   [Examples: Trace analysis](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces) - See a variety of examples of trace analysis

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Tutorial: Search traces programmatically
