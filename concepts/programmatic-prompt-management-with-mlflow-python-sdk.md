---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c45afda16d72689ba22d213e974bce83dad15e04e3b48d527fcb9229933d19c
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - programmatic-prompt-management-with-mlflow-python-sdk
    - PPMWMPS
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Programmatic Prompt Management with MLflow Python SDK
description: The MLflow Python SDK provides functions like mlflow.genai.register_prompt(), mlflow.genai.load_prompt(), and mlflow.genai.search_prompts() for programmatic prompt lifecycle management.
tags:
  - python-sdk
  - mlflow
  - api
  - programmatic
timestamp: "2026-06-18T14:51:01.711Z"
---

# Programmatic Prompt Management with MLflow Python SDK

**Programmatic Prompt Management** with the [MLflow](/concepts/mlflow.md) Python SDK refers to the workflow of creating, versioning, loading, and searching prompts entirely through code, using `mlflow.genai` API functions. This approach enables developers to manage prompt lifecycles, edit prompts, and integrate them into applications without leaving the Python environment. Programmatic management is a core component of the Prompt Engineering workflow within the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) ecosystem.^[create-and-edit-prompts-databricks-on-aws.md]

## Overview

Programmatic prompt management allows you to perform all the actions available in the Databricks MLflow UI through the Python SDK. This includes creating new prompts, registering new versions of existing prompts, and loading prompts for use in applications. This approach is essential for automated workflows, CI/CD pipelines, and reproducible AI research.^[create-and-edit-prompts-databricks-on-aws.md]

## Prerequisites

Before using the SDK programmatically, you must set up your environment:

1. Install MLflow with the required packages:
    ```bash
    pip install --upgrade "mlflow[databricks]>=3.1.0" openai
    ```
2. Create an [MLflow Experiment](/concepts/mlflow-experiment.md) by following the setup environment quickstart.
3. Identify a [Unity Catalog](/concepts/unity-catalog.md) schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges for storing prompts.
4. Link your experiment to a default prompt registry location using the `mlflow.promptRegistryLocation` tag.^[create-and-edit-prompts-databricks-on-aws.md]

## Step 1. Create a new prompt

To create a prompt programmatically, use `mlflow.genai.register_prompt()`. The function requires a prompt name (using the `catalog.schema.prompt_name` syntax) and a template string. Template variables use the double-brace `{{variable}}` syntax.^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

# Link the current MLflow experiment to a UC schema for prompts
mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})

uc_schema = "main.default"
prompt_name = "summarization_prompt"

initial_template = """\
Summarize content you are provided with in {{ num_sentences }} sentences.
Content: {{ content }}
"""

prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template=initial_template,
    commit_message="Initial version of summarization prompt",
    tags={
        "author": "data-science-team@company.com",
        "use_case": "document_summarization"
    }
)
print(f"Created prompt '{prompt.name}' (version {prompt.version})")
```

## Step 2. Use the prompt in an application

After registration, you can load a specific version of a prompt using `mlflow.genai.load_prompt()` with either a URI syntax (`prompts:/catalog.schema.prompt_name/version`) or by specifying the version number. You then format the prompt with dynamic inputs at runtime.^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Load a specific version using URI syntax
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1"
)

# Or load by version number
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"{uc_schema}.{prompt_name}",
    version="1"
)
```

To use the prompt in an application, initialize an OpenAI client (either [Databricks-hosted LLMs](/concepts/databricks-hosted-llms.md) or OpenAI-hosted models), then format and submit the prompt:^[create-and-edit-prompts-databricks-on-aws.md]

```python
from databricks_openai import DatabricksOpenAI

client = DatabricksOpenAI()
model_name = "databricks-claude-sonnet-4"

@mlflow.traced
def my_app(content: str, num_sentences: int):
    # Format with variables
    formatted_prompt = prompt.format(
        content=content,
        num_sentences=num_sentences
    )
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": formatted_prompt}
        ],
    )
    return response.choices[0].message.content
```

## Step 3. Edit the prompt

Prompt versions are **immutable** after creation. To edit a prompt, you must create a new version by calling `mlflow.genai.register_prompt()` with an existing prompt name. This Git-like versioning maintains complete history and enables rollbacks.^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Define the improved template
new_template = """\
You are an expert summarizer. Condense the following content into exactly {{ num_sentences }} clear and informative sentences that capture the key points.
Content: {{ content }}
"""

# Register a new version
updated_prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template=new_template,
    commit_message="Added detailed instructions for better output quality",
    tags={
        "author": "data-science-team@company.com",
        "improvement": "Added specific guidelines for summary quality"
    }
)
print(f"Created version {updated_prompt.version} of '{updated_prompt.name}'")
```

## Step 4. Use the new version

You can load any specific version of a prompt by its version number:^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Load a specific version
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/2"
)

# Or load from specific version
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"{uc_schema}.{prompt_name}",
    version="2"
)
```

## Step 5. Search and discover prompts

To find prompts in your Unity Catalog schema, use `mlflow.genai.search_prompts()` with a filter string that specifies [Catalog and Schema](/concepts/catalog-and-schema.md):^[create-and-edit-prompts-databricks-on-aws.md]

```python
# REQUIRED format for Unity Catalog - specify [[catalog-and-schema|Catalog and Schema]]
results = mlflow.genai.search_prompts(
    "catalog = 'main' AND schema = 'default'"
)

# Using variables for your schema
catalog_name = uc_schema.split('.')[0]  # 'main'
schema_name = uc_schema.split('.')[1]   # 'default'
results = mlflow.genai.search_prompts(
    f"catalog = '{catalog_name}' AND schema = '{schema_name}'"
)

# Limit results
results = mlflow.genai.search_prompts(
    filter_string=f"catalog = '{catalog_name}' AND schema = '{schema_name}'",
    max_results=50
)
```

## Key Characteristics of Programmatic Prompt Management

| Feature | Description |
|---------|-------------|
| **Immutable versions** | Each version is immutable; edits create new versions |
| **Git-like versioning** | Maintains complete history and enables rollbacks |
| **Double-brace syntax** | Uses `{{variable}}` for template variables |
| **Version tracking** | Track changes across versions via commit messages |
| **URI-based loading** | Load specific versions via `prompts:/catalog.schema.prompt_name/version` |
| **Search integration** | Discover prompts by [Catalog and Schema](/concepts/catalog-and-schema.md) with filter strings |

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — The centralized repository for storing and managing prompts
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for prompt storage
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- Prompt Engineering — The broader discipline of designing effective prompts
- [Databricks-hosted LLMs](/concepts/databricks-hosted-llms.md) — Foundation models available for prompt interaction
- Version Control — Managing prompt versions as code artifacts
- CI/CD for Prompts — Integrating prompt management into automated pipelines

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
