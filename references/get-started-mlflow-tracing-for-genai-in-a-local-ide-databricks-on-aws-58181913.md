---
title: "Get started: MLflow Tracing for GenAI in a local IDE | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-ide
ingestedAt: "2026-06-18T08:15:52.875Z"
---

This quickstart helps you integrate your GenAI app with [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) if you use a local development environment such as an IDE (VS Code, PyCharm, Cursor, or others) or a locally hosted notebook environment, such as Jupyter. If you use a Databricks notebook, see the [Databricks notebook quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-notebook) instead.

This tutorial walks you through:

*   An MLflow experiment for your GenAI app
*   Your local development environment connected to MLflow
*   A simple GenAI application instrumented with MLflow Tracing
*   A trace from that app in your MLflow experiment

![trace](https://assets.docs.databricks.com/_static/images/mlflow3-genai/new-images/trace-ide-quickstart.gif)

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Access to a Databricks workspace.

## Step 1: Install MLflow[​](#step-1-install-mlflow "Direct link to Step 1: Install MLflow")

Install MLflow with Databricks connectivity:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" openai

## Step 2: Create a new MLflow experiment[​](#step-2-create-a-new-mlflow-experiment "Direct link to Step 2: Create a new MLflow experiment")

An MLflow experiment is the container for your GenAI application. For more information, see [Experiments](https://docs.databricks.com/aws/en/mlflow3/genai/concepts/#experiments).

1.  Open your Databricks workspace.
2.  In the left sidebar, under **AI/ML**, click **Experiments**.
3.  At the top of the Experiments page, click **GenAI apps & agents**.
4.  To get the experiment ID and path, click the information icon ![Info icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgMTAuNVY3LjVIOC43NVYxMC41SDcuMjVaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDVDOC40MTQyMSA1IDguNzUgNS4zMzU3OSA4Ljc1IDUuNzVDOC43NSA2LjE2NDIxIDguNDE0MjEgNi41IDggNi41QzcuNTg1NzkgNi41IDcuMjUgNi4xNjQyMSA3LjI1IDUuNzVDNy4yNSA1LjMzNTc5IDcuNTg1NzkgNSA4IDVaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNOCAxNEMxMS4zMTM3IDE0IDE0IDExLjMxMzcgMTQgOEMxNCA0LjY4NjI5IDExLjMxMzcgMiA4IDJDNC42ODYyOSAyIDIgNC42ODYyOSAyIDhDMiAxMS4zMTM3IDQuNjg2MjkgMTQgOCAxNFpNOCAxMi41QzEwLjQ4NTMgMTIuNSAxMi41IDEwLjQ4NTMgMTIuNSA4QzEyLjUgNS41MTQ3MiAxMC40ODUzIDMuNSA4IDMuNUM1LjUxNDcyIDMuNSAzLjUgNS41MTQ3MiAzLjUgOEMzLjUgMTAuNDg1MyA1LjUxNDcyIDEyLjUgOCAxMi41WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) in the upper-left. You use these values in later steps.

![create experiment](https://docs.databricks.com/aws/en/assets/images/genai-apps-agents-tile-2fc67b2799a4b6aa281a90a2dae81c95.png)

## Step 3: Connect your environment to MLflow[​](#step-3-connect-your-environment-to-mlflow "Direct link to Step 3: Connect your environment to MLflow")

The following code snippets show how to set up authentication using a Databricks personal access token (PAT). MLflow also works with the other [Databricks-supported authentication methods](https://docs.databricks.com/aws/en/dev-tools/auth/).

*   Use environment variables
*   Use a .env file

1.  In your MLflow Experiment, click the kebab menu icon ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) > **Log traces locally** > **Generate API Key**.
    
2.  Copy and run the generated code in your terminal.
    
    Bash
    
        export DATABRICKS_TOKEN=<databricks-personal-access-token>export DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.comexport MLFLOW_TRACKING_URI=databricksexport MLFLOW_REGISTRY_URI=databricks-ucexport MLFLOW_EXPERIMENT_ID=<experiment-id>
    

## Step 4: Create and instrument your application[​](#step-4-create-and-instrument-your-application "Direct link to Step 4: Create and instrument your application")

Create your GenAI app with tracing enabled.

1.  Create a Python file named `app.py` in your project directory.
    
2.  Initialize an OpenAI client to connect to either Databricks-hosted LLMs or LLMs hosted by OpenAI.
    
    *   Databricks-hosted LLMs
    *   OpenAI-hosted LLMs
    
    Use `databricks-openai` to get an OpenAI client that connects to Databricks-hosted LLMs. Select a model from the [available foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).
    
    Python
    
        import mlflowfrom databricks_openai import DatabricksOpenAI# Enable MLflow's autologging to instrument your application with Tracingmlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/docs-demo")# Create an OpenAI client that is connected to Databricks-hosted LLMsclient = DatabricksOpenAI()# Select an LLMmodel_name = "databricks-claude-sonnet-4"
    
3.  Define and run your application:
    
    Use the [`@mlflow.trace` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/), which makes it easy to trace any Python function, combined with [OpenAI automatic instrumentation](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/openai) to capture the details of the call to the OpenAI SDK.
    
    Python
    
        # Use the trace decorator to capture the application's entry point@mlflow.tracedef my_app(input: str):    # This call is automatically instrumented by `mlflow.openai.autolog()`    response = client.chat.completions.create(        # Uses a Databricks-hosted LLM by default. To use an AI Gateway, Model Serving endpoint, or your own OpenAI credentials, replace `model_name` with a valid model such as `gpt-4o`.        model=model_name,        messages=[            {                "role": "system",                "content": "You are a helpful assistant.",            },            {                "role": "user",                "content": input,            },        ],    )    return response.choices[0].message.contentresult = my_app(input="What is MLflow?")print(result)
    
4.  Run the application:
    

For details on adding tracing to apps, see [Add traces to applications: automatic and manual tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/) and [MLflow Tracing Integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) (more than 20 library integrations).

## Step 5: View the trace in MLflow[​](#step-5-view-the-trace-in-mlflow "Direct link to Step 5: View the trace in MLflow")

1.  Return to the MLflow experiment UI.
2.  The generated trace appears in the **Traces** tab.
3.  Click the trace to view its details.

![Trace Details](https://assets.docs.databricks.com/_static/images/mlflow3-genai/tracing/getting-started/tracing-ide/trace-details.gif)

### Understanding the trace[​](#understanding-the-trace "Direct link to Understanding the trace")

The new trace shows:

*   **Root span**: Represents the inputs to the `my_app(...)` function
    *   **Child span**: Represents the OpenAI completion request
*   **Attributes**: Contains metadata like model name, token counts, and timing information
*   **Inputs**: The messages sent to the model
*   **Outputs**: The response received from the model

Even this minimal trace surfaces useful information about your application's behavior, including:

*   What was asked
*   What response was generated
*   How long the request took
*   How many tokens were used (affecting cost)

For more complex applications like RAG systems or multi-step agents, MLflow Tracing provides even more value by revealing the inner workings of each component and step.

## Guides and references[​](#guides-and-references "Direct link to Guides and references")

For details on concepts and features in this guide, see:

*   [MLflow Tracing - GenAI observability](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) — Start here for in-depth learning about MLflow Tracing.
*   [MLflow Tracing Integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) — More than 20 libraries with automatic tracing integrations.
*   [Trace concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) — Understand the fundamentals of MLflow Tracing.
