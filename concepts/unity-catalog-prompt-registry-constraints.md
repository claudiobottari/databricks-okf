---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2f056726c677d2220ba2ec668dedb5eabc803dfffa71dbd7e5f464133fe5fa9
  pageDirectory: concepts
  sources:
    - prompt-registry-examples-databricks-on-aws.md
  confidence: 0.92
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-prompt-registry-constraints
    - UCPRC
  citations:
    - file: prompt-registry-examples-databricks-on-aws.md
title: Unity Catalog Prompt Registry Constraints
description: "Unity Catalog imposes specific constraints on prompt operations: catalog+schema required in searches, no pattern/tag filtering, and strict version-deletion ordering for prompt removal."
tags:
  - mlflow
  - prompt-management
  - unity-catalog
  - governance
timestamp: "2026-06-19T19:58:49.950Z"
---

# Unity Catalog Prompt Registry Constraints

**Unity Catalog Prompt Registry Constraints** are specific limitations and requirements that apply when using the [MLflow Prompt Registry](/concepts/prompt-registry.md) with a [Unity Catalog](/concepts/unity-catalog.md)-backed registry. Unlike Workspace-level registries, Unity Catalog registries enforce a mandatory three-part naming structure, restrict search filters, and require explicit version deletion before a prompt can be removed.

## Naming Requirements

All prompts in a Unity Catalog registry must be registered using a fully qualified three-part name: `catalog.schema.prompt_name`. ^[prompt-registry-examples-databricks-on-aws.md]

The `mlflow.genai.register_prompt()` API expects the name to include both [Catalog and Schema](/concepts/catalog-and-schema.md):

```python
prompt = mlflow.genai.register_prompt(
    name="mycatalog.myschema.summarization",
    template="...",
    ...
)
```

Similarly, when loading a prompt with `load_prompt()`, the URI format `prompts:/catalog.schema.prompt_name/version` is used. The name parameter can also be supplied as `catalog.schema.prompt_name` without the URI prefix. ^[prompt-registry-examples-databricks-on-aws.md]

## Search Constraints

The `mlflow.genai.search_prompts()` function for Unity Catalog registries has strict filtering limitations:

- The **only** supported filter format is `catalog = '<catalog_name>' AND schema = '<schema_name>'`. ^[prompt-registry-examples-databricks-on-aws.md]
- The following filter types are **not supported** in Unity Catalog:
  - Name patterns (`name LIKE '%pattern%'`)
  - Tag filtering (`tags.field = 'value'`)
  - Exact name matching (`name = 'specific.name'`)
  - Any combined filters beyond the `catalog + schema` condition

To locate specific prompts after fetching, you must filter the returned list programmatically in Python:

```python
# Get all prompts in a schema
all_prompts = mlflow.genai.search_prompts("catalog = 'mycatalog' AND schema = 'myschema'")
# Filter by name substring
customer_prompts = [p for p in all_prompts if 'customer' in p.name.lower()]
# Filter by tag
tagged_prompts = [p for p in all_prompts if p.tags.get('team') == 'support']
```

This approach allows you to emulate the unsupported filters. ^[prompt-registry-examples-databricks-on-aws.md]

## Deletion Constraints

When deleting a prompt in a Unity Catalog registry, you must delete **all existing versions** before the prompt itself can be removed. Calling `MlflowClient.delete_prompt()` on a prompt that still has versions will fail. ^[prompt-registry-examples-databricks-on-aws.md]

The recommended workflow is:

```python
from mlflow import MlflowClient
client = MlflowClient()

# Delete each version individually
client.delete_prompt_version("mycatalog.myschema.chat_assistant", "1")
client.delete_prompt_version("mycatalog.myschema.chat_assistant", "2")
# ... repeat for all versions

# Then delete the prompt itself
client.delete_prompt("mycatalog.myschema.chat_assistant")
```

A convenient pattern is to iterate over all versions returned by `client.search_prompt_versions()`:

```python
search_response = client.search_prompt_versions("mycatalog.myschema.chat_assistant")
for version in search_response.prompt_versions:
    client.delete_prompt_version("mycatalog.myschema.chat_assistant", str(version.version))
client.delete_prompt("mycatalog.myschema.chat_assistant")
```

This version-first requirement applies only to Unity Catalog registries; other registry types do not enforce it. ^[prompt-registry-examples-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that enforces these constraints.
- [Prompt Registry](/concepts/prompt-registry.md) – The overall MLflow feature for managing prompt versions.
- [MLflow](/concepts/mlflow.md) – The platform hosting the Prompt Registry APIs.
- [Workspace Prompt Registry](/concepts/prompt-registry.md) – The alternative registry type without Unity Catalog constraints.

## Sources

- prompt-registry-examples-databricks-on-aws.md

# Citations

1. [prompt-registry-examples-databricks-on-aws.md](/references/prompt-registry-examples-databricks-on-aws-c1a1a7e0.md)
