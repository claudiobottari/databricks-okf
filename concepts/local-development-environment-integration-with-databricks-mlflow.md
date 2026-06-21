---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a71d86502351af13890cfdc2c592c622c101cf5a73417c92eb5f46adf966c4cf
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - local-development-environment-integration-with-databricks-mlflow
    - LDEIWDM
  citations:
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
title: Local Development Environment Integration with Databricks MLflow
description: The workflow for connecting a local IDE (VS Code, PyCharm, Cursor, Jupyter) to a Databricks workspace for MLflow experiment tracking, using environment variables and authentication tokens.
tags:
  - ide
  - databricks
  - mlflow
  - development-environment
timestamp: "2026-06-19T10:44:54.782Z"
---

# Local Development Environment Integration with Databricks MLflow

**Local Development Environment Integration with Databricks MLflow** refers to the process of connecting a local development environment—such as an IDE (VS Code, PyCharm, Cursor, or others) or a locally hosted notebook environment like Jupyter—to Databricks MLflow for tracing and monitoring GenAI applications. This integration enables developers to instrument applications with [MLflow Tracing](/concepts/mlflow-tracing.md) from their local environment and view the resulting traces in the Databricks MLflow experiment UI.

## Overview

This integration allows developers to work in their preferred local development environment while leveraging Databricks MLflow's tracing capabilities for GenAI applications. The setup involves connecting the local environment to a Databricks workspace, creating an MLflow experiment, instrumenting the application with tracing, and viewing the traces in the MLflow experiment UI. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Prerequisites

- Access to a Databricks workspace. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Installation

Install MLflow with Databricks connectivity using pip:

```bash
pip install --upgrade "mlflow[databricks]>=3.1" openai
```

^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Creating an MLflow Experiment

An MLflow experiment serves as the container for your GenAI application. To create one:

1. Open your Databricks workspace.
2. In the left sidebar, under **AI/ML**, click **Experiments**.
3. At the top of the Experiments page, click **GenAI apps & agents**.
4. To get the experiment ID and path, click the information icon in the upper-left. You use these values in later steps. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Connecting Your Environment to MLflow

Set up authentication using a Databricks personal access token (PAT) by running the generated code in your terminal: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

```bash
export DATABRICKS_TOKEN=<databricks-personal-access-token>
export DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
export MLFLOW_TRACKING_URI=databricks
export MLFLOW_REGISTRY_URI=databricks-uc
export MLFLOW_EXPERIMENT_ID=<experiment-id>
```

MLflow also works with other Databricks-supported authentication methods. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Instrumenting Your Application

Create a Python file named `app.py` in your project directory and instrument your application with tracing: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

```python
import mlflow
from databricks_openai import DatabricksOpenAI

# Enable MLflow's autologging
mlflow.openai.autolog()

# Set up tracking
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/docs-demo")

# Create an OpenAI client connected to Databricks-hosted LLMs
client = DatabricksOpenAI()
model_name = "databricks-claude-sonnet-4"

# Use the @mlflow.trace decorator to instrument the application
@mlflow.trace
def my_app(input: str):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input},
        ],
    )
    return response.choices[0].message.content

result = my_app(input="What is MLflow?")
print(result)
```

The `@mlflow.trace` decorator makes it easy to trace any Python function, combined with OpenAI automatic instrumentation to capture the details of the call to the OpenAI SDK. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

For details on adding tracing to apps, see [Add traces to applications: automatic and manual tracing](/concepts/combined-automatic-and-manual-tracing.md) and [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) (more than 20 library integrations). ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Viewing Traces in MLflow

1. Return to the MLflow experiment UI.
2. The generated trace appears in the **Traces** tab.
3. Click the trace to view its details. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

### Understanding the Trace

The trace shows:

- **Root span**: Represents the inputs to the `my_app(...)` function
  - **Child span**: Represents the OpenAI completion request
- **Attributes**: Contains metadata like model name, token counts, and timing information
- **Inputs**: The messages sent to the model
- **Outputs**: The response received from the model

Even this minimal trace surfaces useful information about your application's behavior, including what was asked, what response was generated, how long the request took, and how many tokens were used (affecting cost). For more complex applications like RAG systems or multi-step agents, [MLflow Tracing](/concepts/mlflow-tracing.md) provides even more value by revealing the inner workings of each component and step. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) - GenAI observability
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md)
- [Trace concepts](/concepts/traces.md)
- [Automatic and manual tracing](/concepts/combined-automatic-and-manual-tracing.md)
- OpenAI automatic instrumentation
- Databricks-supported authentication methods

## Sources

- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
