---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 819886963ea63d0d4cf51792e0cebf825b1a4c2e48fb2f96a4cd7b06155334c9
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-templates-with-variable-substitution
    - PTWVS
    - Parameter Substitution
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Prompt Templates with Variable Substitution
description: Prompts support double-brace syntax ({{variable_name}}) for defining template variables that are filled in at runtime using the prompt.format() method.
tags:
  - prompt-engineering
  - templates
  - variables
timestamp: "2026-06-18T14:50:29.981Z"
---

# Prompt Templates with Variable Substitution

**Prompt Templates with Variable Substitution** is a feature of the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) that allows you to define reusable prompt structures with placeholders that are filled in at runtime. This enables dynamic prompt generation while maintaining consistency and traceability across your GenAI applications.

## Overview

A prompt template is a text (or chat) string that contains one or more variables using double-brace `{{variable_name}}` syntax. At application runtime, you supply values for each variable, and the template is formatted with those values. This separates the prompt design (which is versioned in the registry) from the dynamic data that changes per request. ^[create-and-edit-prompts-databricks-on-aws.md]

For example, a summarization prompt can be defined as:
```
Summarize content you are provided with in {{num_sentences}} sentences.

Content: {{content}}
```
At inference time, the application calls `prompt.format(num_sentences=3, content="...")` to produce the final string sent to the model. ^[create-and-edit-prompts-databricks-on-aws.md]

## Creating a Prompt Template

### In the Databricks MLflow UI

1. Navigate to an MLflow experiment and click the **Prompts** tab.
2. Click **New prompt** and choose either **Text** (single text template) or **Chat** (a list of role-based messages).
3. In the **Prompt** field, type your template using `{{variable_name}}` for each placeholder.
4. Optionally add a commit message and click **Create**. The prompt is stored with version 1. ^[create-and-edit-prompts-databricks-on-aws.md]

### Using the Python SDK

First, link your experiment to a Unity Catalog schema by setting the `mlflow.promptRegistryLocation` tag:
```python
mlflow.set_experiment_tags({"mlflow.promptRegistryLocation": "main.default"})
```

Then register a prompt with template variables:
```python
prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template="""\
Summarize content you are provided with in {{num_sentences}} sentences.

Content: {{content}}
""",
    commit_message="Initial version of summarization prompt",
)
```
The template uses the same double-brace syntax for variables. ^[create-and-edit-prompts-databricks-on-aws.md]

## Using a Prompt Template with Variable Substitution

### Load the Prompt

Load a specific version of the prompt from the registry:
```python
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/main.default.summarization_prompt/1"
)
```

### Format with Dynamic Data

Call the `.format()` method on the retrieved `Prompt` object, passing keyword arguments for each variable defined in the template:
```python
formatted_prompt = prompt.format(
    content="This guide shows you how to integrate prompts...",
    num_sentences=1
)
```
The result is a fully resolved string (for text prompts) or a list of message dictionaries (for chat prompts) that can be passed directly to a language model. ^[create-and-edit-prompts-databricks-on-aws.md]

### Use in an Application

The formatted prompt is typically used inside an application function decorated with `@mlflow.trace` for lineage tracking:
```python
@mlflow.trace
def my_app(content: str, num_sentences: int):
    formatted_prompt = prompt.format(
        content=content, num_sentences=num_sentences
    )
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": formatted_prompt},
        ],
    )
    return response.choices[0].message.content
```
This pattern ensures that each inference call is logged with the exact prompt version and substituted values. ^[create-and-edit-prompts-databricks-on-aws.md]

## Version Management

Prompt versions are immutable after creation. To modify a prompt template, you must create a new version. This Git-like versioning maintains a complete history and enables rollbacks. ^[create-and-edit-prompts-databricks-on-aws.md]

### Creating a New Version

Call `mlflow.genai.register_prompt()` with the same name but an updated template:
```python
new_template = """\
You are an expert summarizer. Condense the following content into exactly {{ num_sentences }} clear and informative sentences...

Content: {{content}}
"""
updated_prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template=new_template,
    commit_message="Added detailed instructions for better output quality",
)
```
The registry increments the version number automatically. Applications can then load the new version by specifying `version="2"` or by using an alias. ^[create-and-edit-prompts-databricks-on-aws.md]

## Searching for Prompt Templates

To discover prompts stored in a Unity Catalog schema, use `search_prompts()`:
```python
results = mlflow.genai.search_prompts(
    filter_string="catalog = 'main' AND schema = 'default'",
    max_results=50
)
```
This returns a list of prompt metadata including names, versions, tags, and timestamps. ^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) – Central repository for versioned prompt templates.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The broader framework for building and evaluating generative AI applications.
- [Prompt Version Management](/concepts/prompt-version-management.md) – Creating, comparing, and rolling back prompt versions.
- [Evaluation of Prompt Versions](/concepts/prompt-versioning.md) – Comparing different prompt templates to identify the best performer.
- [Use Prompts in Deployed Applications](/concepts/loading-and-using-prompts-in-applications.md) – Deploying prompts to production using aliases.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
