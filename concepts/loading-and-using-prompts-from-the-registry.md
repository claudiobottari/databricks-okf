---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fb3050dbe0d58ba5c88338917dd987b84f87b1572a1e30efbdbb82445b0a0d3
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-and-using-prompts-from-the-registry
    - Using Prompts from the Registry and Loading
    - LAUPFTR
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Loading and Using Prompts from the Registry
description: Prompts can be loaded by name and version using URI syntax (prompts:/catalog.schema.name/version) or explicitly, then formatted with variables and used in LLM applications.
tags:
  - api
  - prompt-management
  - mlflow-sdk
timestamp: "2026-06-19T09:33:00.320Z"
---

# Loading and Using Prompts from the Registry

**Loading and Using Prompts from the Registry** refers to the process of retrieving [MLflow Prompt Registry](/concepts/prompt-registry.md) entries programmatically and integrating them into GenAI applications. This workflow enables teams to decouple prompt content from application code, manage prompt versions centrally, and maintain full lineage between prompts and the MLflow Models that use them. ^[create-and-edit-prompts-databricks-on-aws.md]

## Overview

Once prompts are registered in the Prompt Registry, they can be loaded at runtime using the MLflow Python SDK. Prompts are retrieved by their name and optionally a specific version, supporting both URI-based and parameter-based loading syntax. The loaded prompt object can then be formatted with dynamic variables and passed to an LLM. ^[create-and-edit-prompts-databricks-on-aws.md]

## Loading a Prompt

### Load by Version

Use [`mlflow.genai.load_prompt()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.load_prompt) to load a specific version of a prompt. The `name_or_uri` parameter accepts either a standard URI or a simple catalog and schema-qualified name. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Load a specific version using URI syntax
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1"
)

# Alternative syntax without URI
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"{uc_schema}.{prompt_name}",
    version="1"
)
```

### Load Latest Version

To load the most recent version, omit the `version` parameter. The latest version is automatically selected. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"{uc_schema}.{prompt_name}"
)
```

## Using the Prompt in an Application

After loading a prompt object, applications can format it with runtime variables using the `format()` method. Template variables defined with `{{variable}}` syntax in the prompt are replaced with actual values. ^[create-and-edit-prompts-databricks-on-aws.md]

### With Databricks-Hosted LLMs

The following example demonstrates loading a prompt, formatting it, and using it with a [Databricks-hosted foundation model](/concepts/databricks-hosted-foundation-models.md) via the `DatabricksOpenAI` client: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow
from databricks_openai import DatabricksOpenAI

# Enable MLflow's autologging to instrument your application with Tracing
mlflow.openai.autolog()

# Set up MLflow tracking to Databricks
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/docs-demo")

# Create an OpenAI client connected to Databricks-hosted LLMs
client = DatabricksOpenAI()

# Select an LLM
model_name = "databricks-claude-sonnet-4"

# Load the prompt from the registry
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1"
)

# Use the trace decorator to capture the application's entry point
@mlflow.trace
def my_app(content: str, num_sentences: int):
    # Format with variables
    formatted_prompt = prompt.format(
        content=content,
        num_sentences=num_sentences
    )
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": formatted_prompt,
            },
        ],
    )
    return response.choices[0].message.content

result = my_app(
    content="This guide shows you how to integrate prompts from the MLflow Prompt Registry into your GenAI applications.",
    num_sentences=1
)
```

### With OpenAI-Hosted LLMs

The same pattern works with OpenAI-hosted models by using the standard `openai` client. Only the client initialization changes — the prompt loading and formatting workflow remains identical. ^[create-and-edit-prompts-databricks-on-aws.md]

## Lineage and Tracking

When [MLflow Autologging](/concepts/mlflow-autologging.md) is enabled, the application code is automatically instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md). This captures the full execution trace, including which prompt version was loaded and which model was called, ensuring complete lineage for reproducibility. ^[create-and-edit-prompts-databricks-on-aws.md]

## Best Practices

- **Use version pinning in production.** Always specify a version (or use an alias) to ensure consistent behavior across deployments.
- **Enable autologging.** Use `mlflow.openai.autolog()` to automatically capture prompt-to-model lineage.
- **Validate formatted prompts.** After formatting, inspect the result to ensure template variables were correctly substituted before sending to the LLM.
- **Place prompts and models in the same catalog.** Keep related prompts and models within the same [Unity Catalog](/concepts/unity-catalog.md) schema for easier discovery and governance.

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) — The centralized store for prompt templates
- Create and Edit Prompts — Registering new prompts
- [Prompt Versioning](/concepts/prompt-versioning.md) — Managing prompt history with immutable versions
- [Track Prompts with App Versions](/concepts/prompt-versioning.md) — Linking prompts to application releases
- Use Prompts in Deployed Apps — Deploying prompts to production environments
- [Evaluate Prompts](/concepts/evaluation-dataset-for-prompts.md) — Comparing prompt versions against quality criteria
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for GenAI application development

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
