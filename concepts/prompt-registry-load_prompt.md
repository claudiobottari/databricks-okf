---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62e1e66b6f3775ba3ed85c2986c50b5793b6ada7bbb6d6a7cdf1f616323a2c0d
  pageDirectory: concepts
  sources:
    - prompt-registry-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-load_prompt
    - PRL
    - Prompt Registry load_prompt
  citations:
    - file: prompt-registry-examples-databricks-on-aws.md
title: Prompt Registry load_prompt
description: Loading specific prompt versions by URI ('prompts:/...') or by name and version number, with optional missing parameter handling.
tags:
  - mlflow
  - prompt-management
  - prompt-registry
timestamp: "2026-06-19T19:58:39.263Z"
---

## Prompt Registry `load_prompt`

The **`load_prompt`** function is an API in the [Prompt Registry](/concepts/prompt-registry.md) that retrieves a specific version of a registered prompt for use in applications. It is part of the `mlflow.genai` module and enables LLM-powered workflows to dynamically load prompt templates, format them with runtime data, and pass them to a model endpoint. ^[prompt-registry-examples-databricks-on-aws.md]

### API Reference

The function is documented in the MLflow Python API reference under [`mlflow.genai.load_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.load_prompt). ^[prompt-registry-examples-databricks-on-aws.md]

### Usage and Parameters

`load_prompt` accepts a prompt identifier in two forms:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `name_or_uri` | Either a prompt URI (e.g., `"prompts:/catalog.schema.name/version"`) or a prompt name alone (e.g., `"catalog.schema.name"`). | `"prompts:/docs.default.customer_support/1"` |
| `version` (optional) | An integer specifying the prompt version. Required when using a name alone (without a URI). | `version=3` |
| `allow_missing` (optional) | A boolean (`True`/`False`) that controls whether missing optional template parameters are allowed when constructing the prompt. When set to `True`, the prompt can be formatted even if some variables are not provided. | `allow_missing=True` |

^[prompt-registry-examples-databricks-on-aws.md]

When a URI is provided, the version is embedded in the URI path and the `version` parameter should be omitted. When only a name (catalog.schema.name) is given, the version must be supplied separately via the `version` parameter. ^[prompt-registry-examples-databricks-on-aws.md]

### Example

The following code demonstrates loading a prompt, formatting it with a user question, and sending the result to a chat completion endpoint:

```python
import mlflow
from databricks.sdk import WorkspaceClient

model = "databricks-claude-sonnet-4-5"
llm = WorkspaceClient().serving_endpoints.get_open_ai_client()

# Load a specific prompt version using the URI format
prompt = mlflow.genai.load_prompt(name_or_uri="prompts:/docs.default.customer_support/1")

# Format the prompt with runtime data
formatted_prompt = prompt.format(question="How do I reset my password?")

# Use the formatted prompt in an LLM call
response = llm.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": formatted_prompt}],
)

print(f"\nResponse using version {prompt.version}:")
print(response.choices[0].message.content)
```

^[prompt-registry-examples-databricks-on-aws.md]

The loaded prompt object (returned by `load_prompt`) exposes a `.version` attribute indicating which version was loaded, and a `.format()` method to substitute template variables. ^[prompt-registry-examples-databricks-on-aws.md]

### Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – The system for managing prompt versions and aliases.
- mlflow.genai.register_prompt – How to create and register a new prompt.
- mlflow.genai.search_prompts – How to discover prompts in the registry.
- mlflow.genai.set_prompt_alias – How to assign aliases (e.g., "production") to prompt versions.

### Sources

- prompt-registry-examples-databricks-on-aws.md

# Citations

1. [prompt-registry-examples-databricks-on-aws.md](/references/prompt-registry-examples-databricks-on-aws-c1a1a7e0.md)
