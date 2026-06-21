---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 790e986a3cbc842540ac607193569127aa0f41e90e24264148fa064b02f25cf0
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-templates-with-variables
    - PTWV
    - Prompt Templates
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Prompt Templates with Variables
description: Prompts use double-brace syntax ({{variable_name}}) to define template variables that are filled in at runtime with dynamic data.
tags:
  - templates
  - prompt-engineering
  - mlflow
timestamp: "2026-06-19T09:31:59.003Z"
---

# Prompt Templates with Variables

**Prompt Templates with Variables** refers to the practice of defining reusable prompt structures that contain placeholders for dynamic content, which are filled in at runtime. This approach enables the same base prompt to be used across multiple invocations with different inputs, making prompts modular, maintainable, and suitable for production applications.^[create-and-edit-prompts-databricks-on-aws.md]

## Overview

Prompt templates use a double-brace syntax (`{{variable_name}}`) to define variables within the prompt text. When the prompt is used in an application, these variables are replaced with actual values provided at runtime. This pattern is commonly employed in both text (completion-style) and chat (role-based message) prompt types.^[create-and-edit-prompts-databricks-on-aws.md]

## Creating Prompts with Variables

### Using the Databricks MLflow UI

1. Navigate to your MLflow experiment and click the **Prompts** tab.
2. Click the **New Prompt** button to open the creation dialog.
3. Select a **Target schema** if one hasn't been chosen.
4. Provide a **Name** for the prompt (only letters, numbers, hyphens, underscores, and dots are allowed).
5. Choose a **Prompt type**:
   - **Text**: A single text template for completion-style prompts.
   - **Chat**: A list of role-based messages (e.g., `system` and `user`) for conversational models.
6. In the **Prompt** field, write your prompt content using `{{variable_name}}` syntax to define variables.
7. Click **Create**.

^[create-and-edit-prompts-databricks-on-aws.md]

### Using the Python SDK

First, link your MLflow experiment to a Unity Catalog schema by setting the `mlflow.promptRegistryLocation` tag:^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

Then, create a prompt with variables using `mlflow.genai.register_prompt()`:^[create-and-edit-prompts-databricks-on-aws.md]

```python
uc_schema = "main.default"
prompt_name = "summarization_prompt"

initial_template = """\
Summarize content you are provided with in {{num_sentences}} sentences.

Content: {{content}}"""

prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template=initial_template,
    commit_message="Initial version of summarization prompt",
    tags={
        "author": "data-science-team@company.com",
        "use_case": "document_summarization",
        "task": "summarization",
        "language": "en",
        "model_compatibility": "gpt-4"
    }
)
```

## Variable Syntax

Variables are defined using `{{ variable_name }}` syntax within the prompt template. The variable name can be any valid identifier, and multiple variables can be used within a single template.^[create-and-edit-prompts-databricks-on-aws.md]

For example, a template might contain:

```
Summarize content you are provided with in {{num_sentences}} sentences.

Content: {{content}}
```

## Using Templates with Variables in Applications

### Loading a Prompt

Load a specific version of a prompt from the registry:^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Load a specific version using URI syntax
prompt = mlflow.genai.load_prompt(name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1")

# Alternative syntax without URI
prompt = mlflow.genai.load_prompt(name_or_uri=f"{uc_schema}.{prompt_name}", version="1")
```

### Formatting with Runtime Values

Once loaded, call the `format()` method on the prompt object, passing keyword arguments that match the variable names defined in the template:^[create-and-edit-prompts-databricks-on-aws.md]

```python
formatted_prompt = prompt.format(
    content="This guide shows you how to integrate prompts...",
    num_sentences=2
)
```

The resulting string replaces each `{{variable}}` placeholder with the corresponding value provided.^[create-and-edit-prompts-databricks-on-aws.md]

## Editing Prompts (Versioning)

Prompt versions are immutable after creation. To update a template, create a new version of the prompt. This Git-like versioning maintains complete history and enables rollbacks.^[create-and-edit-prompts-databricks-on-aws.md]

### Creating a New Version (Python SDK)

Call `mlflow.genai.register_prompt()` with an existing prompt name to create a new version:^[create-and-edit-prompts-databricks-on-aws.md]

```python
new_template = """\
You are an expert summarizer. Condense the following content into exactly {{ num_sentences }} clear and informative sentences.

Content: {{content}}

Your summary should:
- Contain exactly {{num_sentences}} sentences
- Include only the most important information
- Be written in a neutral, objective tone
- Maintain the same level of formality as the original text"""

updated_prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template=new_template,
    commit_message="Added detailed instructions for better output quality"
)
```

## Searching for Prompts

Search for prompts in a Unity Catalog schema using `mlflow.genai.search_prompts()`:^[create-and-edit-prompts-databricks-on-aws.md]

```python
catalog_name = uc_schema.split('.')[0]  # 'main'
schema_name = uc_schema.split('.')[1]   # 'default'

results = mlflow.genai.search_prompts(
    filter_string=f"catalog = '{catalog_name}' AND schema = '{schema_name}'",
    max_results=50
)
```

## Permissions

To create or view prompts in a Unity Catalog schema, you must have the following permissions on that schema:
- `CREATE FUNCTION`
- `EXECUTE`
- `MANAGE`

^[create-and-edit-prompts-databricks-on-aws.md]

## Best Practices

- **Use descriptive variable names** that clearly indicate what data should be provided at runtime.
- **Include a commit message** when creating new versions to document changes.
- **Tag prompts** with metadata such as author, use case, and model compatibility for discoverability.
- **Version your prompts** to track changes and enable rollbacks to previous templates.

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) – Central repository for managing prompt versions.
- [Prompt Versioning](/concepts/prompt-versioning.md) – Managing changes to prompt templates over time.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – Framework for building and evaluating generative AI applications.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for managing data and AI assets.
- [Prompt Evaluation](/concepts/prompt-version-evaluation.md) – Comparing different prompt versions to identify the best performer.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
