---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b6875398978037086e3f64e64f45edb37074a4d76e30a5a5247f6c416b4523e
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-python-sdk-for-prompt-management
    - MGPSFPM
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: MLflow genai Python SDK for Prompt Management
description: Python SDK functions (register_prompt, load_prompt, search_prompts) for programmatic management of prompts in the Prompt Registry.
tags:
  - mlflow
  - python-sdk
  - api
timestamp: "2026-06-18T11:19:31.729Z"
---

# MLflow genai Python SDK for Prompt Management

The **MLflow genai Python SDK for Prompt Management** provides programmatic interfaces for creating, versioning, loading, and discovering prompts in the MLflow Prompt Registry. The SDK is part of the `mlflow.genai` module and works with Unity Catalog schemas to store and manage prompt templates with Git-like versioning.

## Overview

Prompt Management in MLflow genai allows developers to treat prompts as version-controlled assets, similar to code or models. Prompts are stored in Unity Catalog schemas, support template variables, and maintain immutable version history. The SDK provides functions for registering new prompts, loading specific versions, and searching across the catalog.^[create-and-edit-prompts-databricks-on-aws.md]

## Prerequisites

To use the Prompt Management SDK, you must:

1. Install MLflow and required packages:
   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0" openai
   ```
2. Create an MLflow experiment by following the environment setup quickstart.
3. Identify a Unity Catalog schema where you have `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges.^[create-and-edit-prompts-databricks-on-aws.md]

## Linking an Experiment to a Prompt Registry Location

Before creating prompts, link your MLflow experiment to a default Prompt Registry location using an experiment tag. This allows SDKs and tools to infer your Unity Catalog prompt schema automatically.

```python
import mlflow

mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

Use the `mlflow.promptRegistryLocation` tag with the value `catalog.schema`.^[create-and-edit-prompts-databricks-on-aws.md]

## Creating Prompts

### `mlflow.genai.register_prompt()`

Creates a new prompt or a new version of an existing prompt. Prompts use double-brace syntax (`{{variable}}`) for template variables.

```python
prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template="""Summarize content you are provided with in {{num_sentences}} sentences.
Content: {{content}}""",
    commit_message="Initial version of summarization prompt",
    tags={
        "author": "data-science-team@company.com",
        "use_case": "document_summarization",
    }
)
print(f"Created prompt '{prompt.name}' (version {prompt.version})")
```

Parameters:
- `name`: The prompt name, including the Unity Catalog schema prefix (`catalog.schema.prompt_name`).
- `template`: The prompt template content with `{{variable}}` placeholders.
- `commit_message` (optional): A description of this version for change tracking.
- `tags` (optional): Metadata labels for discovery and categorization.

When called with an existing prompt name, `register_prompt()` creates a new immutable version rather than overwriting the existing one.^[create-and-edit-prompts-databricks-on-aws.md]

## Loading Prompts

### `mlflow.genai.load_prompt()`

Loads a prompt version from the registry for use in applications.

```python
# Load a specific version using URI syntax
prompt = mlflow.genai.load_prompt(name_or_uri="prompts:/main.default.summarization_prompt/1")

# Alternative syntax without URI
prompt = mlflow.genai.load_prompt(
    name_or_uri="main.default.summarization_prompt",
    version="1"
)
```

The URI format is `prompts:/catalog.schema.prompt_name/version`. Once loaded, you can format the prompt with values:

```python
formatted_prompt = prompt.format(
    content="Your text here...",
    num_sentences=2
)
```

^[create-and-edit-prompts-databricks-on-aws.md]

## Searching and Discovering Prompts

### `mlflow.genai.search_prompts()`

Finds prompts in a Unity Catalog schema using filter strings.

```python
# Search by [[catalog-and-schema|Catalog and Schema]]
results = mlflow.genai.search_prompts(
    filter_string="catalog = 'main' AND schema = 'default'"
)

# With result limit
results = mlflow.genai.search_prompts(
    filter_string="catalog = 'main' AND schema = 'default'",
    max_results=50
)
```

The filter string requires the format `catalog = '<name>' AND schema = '<name>'`.^[create-and-edit-prompts-databricks-on-aws.md]

## Versioning Model

Prompt versions are immutable after creation. This Git-like versioning maintains complete history and enables rollbacks. To edit a prompt, you create a new version using `register_prompt()` with the same prompt name but updated template or metadata. Each version gets an incrementing version number.^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Create a new version of an existing prompt
updated_prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template="""You are an expert summarizer. Condense the following content 
into exactly {{ num_sentences }} clear and informative sentences.
Content: {{content}}""",
    commit_message="Added detailed instructions for better output quality",
    tags={
        "author": "data-science-team@company.com",
        "improvement": "Added specific guidelines for summary quality"
    }
)
print(f"Created version {updated_prompt.version}")
```

## Prompt Types

The SDK supports two prompt types:

- **Text**: A single text template for completion-style prompts.
- **Chat**: A list of role-based messages (system, user, assistant) for conversational models.

The prompt type is set during creation in the Databricks MLflow UI; the Python SDK infers the type from the template structure.^[create-and-edit-prompts-databricks-on-aws.md]

## Integration with Applications

After loading a prompt and formatting it with variables, you can use it with any LLM client:

```python
from databricks_openai import DatabricksOpenAI
import mlflow

mlflow.openai.autolog()
client = DatabricksOpenAI()

@mlflow.trace
def my_app(content: str, num_sentences: int):
    formatted_prompt = prompt.format(
        content=content,
        num_sentences=num_sentences
    )
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": formatted_prompt},
        ],
    )
    return response.choices[0].message.content
```

The `@mlflow.trace` decorator captures the application's execution for observability.^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) — The centralized storage for versioned prompts
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores prompt schemas
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Comparing prompt versions with evaluation
- [Prompt Version Aliases](/concepts/prompt-version-aliases.md) — Deploying prompts to production with aliases
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Instrumenting applications that use prompts

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
