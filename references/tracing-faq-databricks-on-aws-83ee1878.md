---
title: Tracing FAQ | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/faq
ingestedAt: "2026-06-18T08:16:47.736Z"
---

### Q: What is the latency overhead introduced by Tracing?[​](#q-what-is-the-latency-overhead-introduced-by-tracing "Direct link to Q: What is the latency overhead introduced by Tracing?")

Traces are written asynchronously to minimize performance impact. However, tracing still adds minimal latency, particularly when the trace size is large. MLflow recommends testing your application to understand tracing latency impacts before deploying to production.

The following table provides rough estimates for latency impact by trace size:

### Q: What are the rate limits and quotas for MLflow Tracing in Databricks?[​](#q-what-are-the-rate-limits-and-quotas-for-mlflow-tracing-in-databricks "Direct link to Q: What are the rate limits and quotas for MLflow Tracing in Databricks?")

When using MLflow Tracing within a Databricks workspace quotas and rate limits apply to ensure service stability and fair usage. See [Resource limits](https://docs.databricks.com/aws/en/resources/limits).

### Q: I cannot open my trace in the MLflow UI. What should I do?[​](#q-i-cannot-open-my-trace-in-the-mlflow-ui-what-should-i-do "Direct link to Q: I cannot open my trace in the MLflow UI. What should I do?")

There are multiple possible reasons why a trace may not be viewable in the MLflow UI.

1.  **The trace is not completed yet**: If the trace is still being collected, MLflow cannot display spans in the UI. Ensure that all spans are properly ended with either "OK" or "ERROR" status.
    
2.  **The browser cache is outdated**: When you upgrade MLflow to a new version, the browser cache may contain outdated data and prevent the UI from displaying traces correctly. Clear your browser cache (Shift+F5) and refresh the page.
    

### Q: I can't find a specific trace by ID in the trace list. What should I do?[​](#q-i-cant-find-a-specific-trace-by-id-in-the-trace-list-what-should-i-do "Direct link to Q: I can't find a specific trace by ID in the trace list. What should I do?")

By default, the trace list returns the most recent 1,000 traces. If an older trace falls outside this window, it won't appear in search results, even if you match the trace ID.

To find an older trace, narrow the time range filter to create a smaller window of results. Once the trace falls within the 1,000 most recent entries for that specific period, the ID search will pick it up. If you know the experiment ID and trace ID, you can also navigate directly: `<workspace-url>/ml/experiments/<experiment-id>/traces/<trace-id>`.

Experiments not in Unity Catalog are also capped at 100,000 traces total. To remove both limits and search across all traces in a time range, [migrate to traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-traces-to-uc).

### Q: The model execution gets stuck and my trace is "in progress" forever.[​](#q-the-model-execution-gets-stuck-and-my-trace-is-in-progress-forever "Direct link to Q: The model execution gets stuck and my trace is \"in progress\" forever.")

Sometimes a model or an agent gets stuck in a long-running operation or an infinite loop, causing the trace to be stuck in the "in progress" state.

To prevent this, you can set a timeout for the trace using the `MLFLOW_TRACE_TIMEOUT_SECONDS` environment variable. If the trace exceeds the timeout, MLflow will automatically halt the trace with `ERROR` status and export it to the backend, so that you can analyze the spans to identify the issue. By default, the timeout is not set.

note

The timeout only applies to MLflow trace. The main program, model, or agent, will continue to run even if the trace is halted.

For example, the following code sets the timeout to 5 seconds and simulates how MLflow handles a long-running operation:

Python

    import mlflowimport osimport time# Set the timeout to 5 seconds for demonstration purposesos.environ["MLFLOW_TRACE_TIMEOUT_SECONDS"] = "5"# Simulate a long-running operation@mlflow.tracedef long_running():    for _ in range(10):        child()@mlflow.tracedef child():    time.sleep(1)long_running()

note

MLflow monitors the trace execution time and expiration in a background thread. By default, this check is performed every second and resource consumption is negligible. If you want to adjust the interval, you can set the `MLFLOW_TRACE_TIMEOUT_CHECK_INTERVAL_SECONDS` environment variable.

### Q: My trace is split into multiple traces when doing multi-threading. How can I combine them into a single trace?[​](#q-my-trace-is-split-into-multiple-traces-when-doing-multi-threading-how-can-i-combine-them-into-a-single-trace "Direct link to Q: My trace is split into multiple traces when doing multi-threading. How can I combine them into a single trace?")

As MLflow Tracing depends on Python ContextVar, each thread has its own trace context by default, but it is possible to generate a single trace for multi-threaded applications with a few additional steps. See [Multi-threading](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator#multi-threading) section for more information.

### Q: How do I temporarily disable tracing?[​](#q-how-do-i-temporarily-disable-tracing "Direct link to Q: How do I temporarily disable tracing?")

To **disable** tracing, [`mlflow.tracing.disable`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.tracing.html#mlflow.tracing.disable) API will cease the collection of trace data from within MLflow and will not log any data to the MLflow Tracking service regarding traces.

To **enable** tracing (if it had been temporarily disabled), [`mlflow.tracing.enable`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.tracing.html#mlflow.tracing.enable) API will re-enable tracing functionality for instrumented models that are invoked.

### Q: My trace search results are too big for `mlflow.search_traces()`. How do I search traces at scale?[​](#q-my-trace-search-results-are-too-big-for-mlflowsearch_traces-how-do-i-search-traces-at-scale "Direct link to q-my-trace-search-results-are-too-big-for-mlflowsearch_traces-how-do-i-search-traces-at-scale")

The MLflow API provides pagination through the [`MlflowClient.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_traces) method. However, for use cases not requiring pagination, [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces) is recommended since it provides more functionality and convenient defaults.

For large-scale trace analysis in production, it is generally best to use [production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) to log traces to Delta tables in Unity Catalog. See [Trace agents deployed on Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing) for production tracing guidance.
