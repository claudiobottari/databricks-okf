---
title: "Get started: MLflow Tracing for GenAI (Databricks Notebook) | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-notebook
ingestedAt: "2026-06-18T08:15:54.415Z"
---

This quickstart helps you integrate your GenAI app with [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) if you use a Databricks notebook as your development environment. If you use a local IDE, please use the [IDE quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-ide) instead.

By the end of this tutorial, you will have:

*   A Databricks notebook with a linked MLflow experiment for your GenAI app
*   A simple GenAI application instrumented with MLflow Tracing
*   A trace from that app in your MLflow experiment

![Tracing UI for quickstart tutorial](https://assets.docs.databricks.com/_static/images/mlflow3-genai/new-images/trace-ide-quickstart.gif)

## Environment setup[​](#environment-setup "Direct link to Environment setup")

1.  [Create a new notebook](https://docs.databricks.com/aws/en/notebooks/notebooks-manage#create-a-notebook) in your Databricks workspace. The notebook will have a default MLflow experiment that is the container for your GenAI application. Learn more about MLflow experiments in the [MLflow concepts section](https://docs.databricks.com/aws/en/mlflow3/genai/concepts/#experiments).
    
2.  Install required packages:
    
    *   `mlflow[databricks]`: Use the latest version of MLflow to get more features and improvements.
    *   `openai`: This tutorial will use the OpenAI API client to call Databricks-hosted models.

Python

    %pip install -qq --upgrade "mlflow[databricks]>=3.1.0" openaidbutils.library.restartPython()

## Step 1: Instrument your application with tracing[​](#step-1-instrument-your-application-with-tracing "Direct link to Step 1: Instrument your application with tracing")

The code snippets below define a simple GenAI app that completes sentence templates using an LLM.

First, create an OpenAI client to connect to [Databricks-hosted foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models):

Python

    from databricks_openai import DatabricksOpenAI# Create an OpenAI client that is connected to Databricks-hosted LLMsclient = DatabricksOpenAI()model_name = "databricks-claude-sonnet-4"

Alternatively, you could use the OpenAI SDK to connect to OpenAI-hosted models:

Python

    import openai# Ensure your OPENAI_API_KEY is set in your environment# os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>" # Uncomment and set if not globally configuredclient = openai.OpenAI()model_name = "gpt-4o-mini"

Second, define and run your application. Instrumenting the app with tracing simply uses:

*   [`mlflow.openai.autolog()`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/openai): Automatic instrumentation to capture the details of the call to the OpenAI SDK
*   [`@mlflow.trace`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/): Decorator that makes it easy to trace any Python function

Python

    import mlflowimport os# Enable auto-tracing for OpenAImlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/tracing-quickstart")# Use the trace decorator to capture the application's entry point@mlflow.tracedef my_app(input: str):  # This call is automatically instrumented by `mlflow.openai.autolog()`  response = client.chat.completions.create(    model=model_name,    temperature=0.1,    max_tokens=200,    messages=[      {        "role": "system",        "content": "You are a helpful assistant.",      },      {        "role": "user",        "content": input,      },    ]  )  return response.choices[0].message.contentresult = my_app(input="What is MLflow?")print(result)

For details on adding tracing to apps, see the [tracing instrumentation guide](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/) and the [20+ library integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/).

## Step 2: View the trace in MLflow[​](#step-2-view-the-trace-in-mlflow "Direct link to Step 2: View the trace in MLflow")

The trace will appear below the notebook cell.

![Notebook tracing UI](https://docs.databricks.com/aws/en/assets/images/quickstart-trace-e64c43f4f4e52d4d4dc36dfca3b824c3.png)

Optionally, you can go to the MLflow experiment UI to see the trace:

1.  Click the experiments icon ![Experiments icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik01Ljc1MDA0IDFDNS4zMzU4MyAxIDUuMDAwMDQgMS4zMzU3OSA1LjAwMDA0IDEuNzVWNy44Mzg3MkM1LjAwMDA0IDguMjE4NDUgNC44Mjc0MyA4LjU3NzU5IDQuNTMwOTEgOC44MTQ4MUwxLjg1MTggMTAuOTU4MUMxLjMxMzQxIDExLjM4ODggMSAxMi4wNDA5IDEgMTIuNzMwNEMxIDEzLjk4MzkgMi4wMTYxNSAxNSAzLjI2OTYzIDE1SDEyLjczMDRDMTMuOTgzOSAxNSAxNSAxMy45ODM5IDE1IDEyLjczMDRDMTUgMTIuMDQwOSAxNC42ODY2IDExLjM4ODggMTQuMTQ4MiAxMC45NTgxTDExLjQ2OTIgOC44MTQ4N0MxMS4xNzI3IDguNTc3NjUgMTEgOC4yMTg1MSAxMSA3LjgzODc4VjEuNzVDMTEgMS4zMzU3OSAxMC42NjQzIDEgMTAuMjUgMUg1Ljc1MDA0Wk02LjUwMDA0IDcuODM4NzJWMi41SDkuNTAwMDRWNy44Mzg3OEM5LjUwMDA0IDguNDQ0NyA5LjY5OTgxIDkuMDI2OCAxMC4wNTg1IDkuNUg1Ljk0MTU2QzYuMzAwMjUgOS4wMjY3OSA2LjUwMDA0IDguNDQ0NjcgNi41MDAwNCA3LjgzODcyWk00LjIwMDU5IDExTDIuNzg4ODUgMTIuMTI5NEMyLjYwNjI4IDEyLjI3NTQgMi41IDEyLjQ5NjYgMi41IDEyLjczMDRDMi41IDEzLjE1NTQgMi44NDQ1NyAxMy41IDMuMjY5NjMgMTMuNUgxMi43MzA0QzEzLjE1NTQgMTMuNSAxMy41IDEzLjE1NTQgMTMuNSAxMi43MzA0QzEzLjUgMTIuNDk2NiAxMy4zOTM3IDEyLjI3NTQgMTMuMjExMiAxMi4xMjk0TDExLjc5OTQgMTFINC4yMDA1OVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) on the right sidebar.
2.  Click the new window icon ![New window icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEwIDFIMTVWNkgxMy41VjMuNTYwNjZMOC41MzAzMyA4LjUzMDMzTDcuNDY5NjcgNy40Njk2N0wxMi40MzkzIDIuNUgxMFYxWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNMSAyLjc1QzEgMi4zMzU3OSAxLjMzNTc5IDIgMS43NSAySDhWMy41SDIuNVYxMy41SDEyLjVWOEgxNFYxNC4yNUMxNCAxNC42NjQyIDEzLjY2NDIgMTUgMTMuMjUgMTVIMS43NUMxLjMzNTc5IDE1IDEgMTQuNjY0MiAxIDE0LjI1VjIuNzVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) next to experiment runs.
3.  The generated trace appears in the **Traces** tab.
4.  Click the trace to view its details.

### Understand the trace[​](#understand-the-trace "Direct link to Understand the trace")

The trace you just created shows:

*   **Root span**: Represents the inputs to the `my_app(...)` function
    *   **Child span**: Represents the OpenAI completion request
*   **Attributes**: Contains metadata like model name, token counts, and timing information
*   **Inputs**: The messages sent to the model
*   **Outputs**: The response received from the model

This simple trace already provides valuable insights into your application's behavior, such as:

*   What was asked
*   What response was generated
*   How long the request took
*   How many tokens were used (affecting cost)

For more complex applications like RAG systems or multi-step agents, MLflow Tracing provides even more value by revealing the inner workings of each component and step.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [MLflow Tracing guide](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) - Start here for more in-depth learning about MLflow Tracing
*   [MLflow Tracing integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) - 20+ libraries with automatic tracing integrations
*   [Tracing concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) - Understand the fundamentals of MLflow Tracing

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Get started: MLflow Tracing for GenAI (Databricks Notebook)
