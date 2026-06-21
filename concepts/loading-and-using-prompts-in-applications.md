---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ba3501f6933e68e4063cdbe0cb7e12b0dea3c78e74a0c242e674fe9662782da
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loading-and-using-prompts-in-applications
    - Using Prompts in Applications and Loading
    - LAUPIA
    - Use Prompts in Deployed Applications
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Loading and Using Prompts in Applications
description: The pattern of loading prompt versions from the registry using URI syntax (prompts:/catalog.schema.name/version) and formatting them with runtime variables for use in LLM applications.
tags:
  - mlflow
  - prompt-management
  - application-integration
timestamp: "2026-06-19T14:33:01.184Z"
---

# Loading and Using Prompts in Applications

**Loading and Using Prompts in Applications** refers to the workflow of retrieving a prompt template from the [MLflow Prompt Registry](/concepts/prompt-registry.md), filling in dynamic variables at runtime, and sending the formatted prompt to a language model as part of a GenAI application. This approach centralizes prompt management, enables version control, and maintains full lineage between prompt versions, model calls, and application code. ^[create-and-edit-prompts-databricks-on-aws.md]

## Overview

Prompts registered in the MLflow Prompt Registry are stored as immutable versions in a [Unity Catalog](/concepts/unity-catalog.md) schema. Applications load a specific prompt version by name and version number, format it with runtime data, and then use it with an LLM client (such as OpenAI’s API or Databricks-hosted endpoints). This decouples prompt content from application logic, making it easier to iterate on prompts without redeploying code. ^[create-and-edit-prompts-databricks-on-aws.md]

## Loading a Prompt from the Registry

Use `mlflow.genai.load_prompt()` to retrieve a prompt by its URI or by name and version. The URI format is `prompts:/catalog.schema.prompt_name/version`. Alternatively, pass the fully qualified name and the version keyword. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

# URI syntax
prompt = mlflow.genai.load_prompt(name_or_uri=f"prompts:/main.default.summarization_prompt/1")

# Name + version syntax
prompt = mlflow.genai.load_prompt(
    name_or_uri="main.default.summarization_prompt", version="1"
)
```

The returned prompt object supports variable substitution via its `.format()` method. Variables are defined in the prompt template using double‑brace syntax (`{{variable_name}}`). ^[create-and-edit-prompts-databricks-on-aws.md]

## Using the Prompt in an Application

1. **Set up tracking** – Point MLflow to your Databricks workspace and create or specify an experiment. Enable autologging for the OpenAI client to automatically capture traces. ^[create-and-edit-prompts-databricks-on-aws.md]

   ```python
   mlflow.set_tracking_uri("databricks")
   mlflow.set_experiment("/Shared/docs-demo")
   mlflow.openai.autolog()
   ```

2. **Create a client** – Initialize an OpenAI‑compatible client. For Databricks‑hosted LLMs, use the `DatabricksOpenAI` client from the `databricks_openai` package. For external OpenAI models, use the standard `openai.OpenAI` client. ^[create-and-edit-prompts-databricks-on-aws.md]

3. **Format the prompt** – Call `prompt.format(variable=value)` to substitute placeholders with runtime data. ^[create-and-edit-prompts-databricks-on-aws.md]

4. **Make the LLM call** – Send the formatted prompt as part of a chat or completion request. For chat models, the formatted string is typically placed in the `user` role message. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
@mlflow.trace
def my_app(content: str, num_sentences: int):
    formatted_prompt = prompt.format(content=content, num_sentences=num_sentences)
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": formatted_prompt},
        ],
    )
    return response.choices[0].message.content
```

The `@mlflow.trace` decorator captures the application entry point, creating a complete trace that includes the prompt version used, the model response, and any intermediate steps. This trace is recorded in the MLflow experiment and can be inspected for debugging and performance analysis. ^[create-and-edit-prompts-databricks-on-aws.md]

## Version Management

Prompt versions are immutable after creation. To change a prompt, create a new version using `mlflow.genai.register_prompt()` with the same name. Applications always load a specific version, so upgrading the prompt in production is a matter of updating the version number (or using an alias). This Git‑like versioning preserves full history and enables rollbacks. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
updated_prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template=new_template,
    commit_message="Improved clarity in summary instructions",
)
```

## Searching and Discovering Prompts

Use `mlflow.genai.search_prompts()` to find prompts within a Unity Catalog schema. The filter string supports [Catalog and Schema](/concepts/catalog-and-schema.md) constraints. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
results = mlflow.genai.search_prompts(
    filter_string="catalog = 'main' AND schema = 'default'",
    max_results=50,
)
```

## Best Practices

- **Link the experiment to a prompt registry location** – Set the `mlflow.promptRegistryLocation` experiment tag to the Unity Catalog schema (e.g., `main.default`) so that SDKs and tools can automatically infer where prompts are stored. ^[create-and-edit-prompts-databricks-on-aws.md]
- **Provide descriptive commit messages** – Each version’s commit message helps track why a prompt was changed and what the improvement is. ^[create-and-edit-prompts-databricks-on-aws.md]
- **Use tags for metadata** – Attach tags like `author`, `use_case`, `task`, or `model_compatibility` to prompts for easier discovery and governance. ^[create-and-edit-prompts-databricks-on-aws.md]
- **Prefer explicit version numbers in production** – Loading a pinned version (e.g., version `2`) prevents accidental changes from affecting live traffic. Use aliases (not covered in this source) for rolling updates. ^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) – Central repository for prompt templates with version control.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance layer that stores prompt schemas and controls permissions.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Automatic capture of prompt usage and model calls for observability.
- [Prompt Template Variables](/concepts/prompt-template-variables.md) – The `{{variable}}` syntax for injecting runtime data.
- [Track prompts with app versions](/concepts/prompt-versioning.md) – Linking prompt versions to application releases.
- Use prompts in deployed apps – Deploying prompts to production with aliases.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
