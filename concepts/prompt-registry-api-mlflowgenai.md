---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90ca4934a7162621af3bc1f5f222fca56eb08c584e4bcbfbe07b0d5b724f8ade
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-api-mlflowgenai
    - PRA(
    - Prompt Registry (MLflow GenAI)
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Prompt Registry API (mlflow.genai)
description: Python SDK functions including register_prompt(), load_prompt(), and search_prompts() for programmatic prompt lifecycle management.
tags:
  - mlflow
  - python-sdk
  - api
timestamp: "2026-06-19T17:58:38.255Z"
---

Here is a wiki page for "Prompt Registry API (mlflow.genai)", based solely on the provided source material.

---

## Prompt Registry API (`mlflow.genai`)

The **Prompt Registry API** (`mlflow.genai`) is a set of functions in the MLflow Python SDK for managing prompts and their versions within the MLflow Prompt Registry. The registry is integrated with Unity Catalog, providing a Git-like versioning system for prompt templates. ^[create-and-edit-prompts-databricks-on-aws.md]

### Core Functions

#### `mlflow.genai.register_prompt()`

This function creates a new prompt or registers a new version of an existing prompt. Prompt names can contain only letters, numbers, hyphens, underscores, and dots. Prompts use double-brace syntax (`{{variable}}`) for template variables. ^[create-and-edit-prompts-databricks-on-aws.md]

When creating a new prompt, a `name` and `template` are required. Optional parameters include a `commit_message` and `tags`. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Create a new prompt
prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template="Summarize content in {{num_sentences}} sentences.\nContent: {{content}}",
    commit_message="Initial version",
    tags={"author": "data-science-team@company.com"}
)

# Create a new version of an existing prompt
new_template = """Detailed instructions for {{content}}"""
updated_prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template=new_template,
    commit_message="Added detailed instructions"
)
```

`register_prompt()` returns an object with `.name` and `.version` attributes. ^[create-and-edit-prompts-databricks-on-aws.md]

#### `mlflow.genai.load_prompt()`

This function loads a prompt from the registry. It accepts a URI syntax (`prompts:/catalog.schema.prompt_name/version`) or separate `name_or_uri` and `version` parameters. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Using URI syntax
prompt = mlflow.genai.load_prompt(name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1")

# Using explicit version parameter
prompt = mlflow.genai.load_prompt(name_or_uri=f"{uc_schema}.{prompt_name}", version="1")
```

After loading, you format the prompt with dynamic data using the `.format()` method. ^[create-and-edit-prompts-databricks-on-aws.md]

#### `mlflow.genai.search_prompts()`

This function searches for prompts within a Unity Catalog schema. It requires a filter string in the format `"catalog = '<catalog_name>' AND schema = '<schema_name>'"`. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
results = mlflow.genai.search_prompts(
    filter_string="catalog = 'main' AND schema = 'default'",
    max_results=50
)
```

### Experiment Tag Configuration

To link an MLflow experiment to a default Prompt Registry location, set the `mlflow.promptRegistryLocation` tag on the experiment. This allows SDKs and tools to infer the Unity Catalog schema automatically. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

### Versioning and Immutability

Prompt versions are immutable after creation. To edit a prompt, you must create a new version using `mlflow.genai.register_prompt()` with the same prompt name. Each version maintains complete history with a commit message, enabling rollbacks. ^[create-and-edit-prompts-databricks-on-aws.md]

### Prerequisites

1. Install MLflow: `pip install --upgrade "mlflow[databricks]>=3.1.0" openai` ^[create-and-edit-prompts-databricks-on-aws.md]
2. Create an MLflow experiment. ^[create-and-edit-prompts-databricks-on-aws.md]
3. Create or identify a Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges. ^[create-and-edit-prompts-databricks-on-aws.md]

### Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — The underlying system for storing and managing prompts.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Catalog and Schema](/concepts/catalog-and-schema.md) system where prompts are stored.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit linked to a Prompt Registry schema.
- [Prompt Templates](/concepts/prompt-templates-with-variables.md) — The definition of prompt content with variable substitution.
- [Prompt Versioning](/concepts/prompt-versioning.md) — The Git-like version management system for prompts.

### Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
