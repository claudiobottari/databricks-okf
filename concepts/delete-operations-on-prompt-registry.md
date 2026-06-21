---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38c8b72ab2e146cb4c5a1f882848c97877b95b3745962fb27f6a8c6efb268738
  pageDirectory: concepts
  sources:
    - prompt-registry-examples-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delete-operations-on-prompt-registry
    - DOOPR
  citations:
    - file: prompt-registry-examples-databricks-on-aws.md
title: Delete Operations on Prompt Registry
description: Deleting prompts requires deleting all versions first for Unity Catalog registries; other registry types allow direct prompt deletion without version cleanup.
tags:
  - mlflow
  - prompt-management
  - unity-catalog
timestamp: "2026-06-19T19:58:41.419Z"
---

# Delete Operations on Prompt Registry

**Delete Operations on Prompt Registry** refer to the process of removing prompt versions and entire prompts from the [Prompt Registry](/concepts/prompt-registry.md) using the `MlflowClient` API. These operations differ depending on whether the prompt resides in a [Unity Catalog](/concepts/unity-catalog.md) registry or another type of registry. ^[prompt-registry-examples-databricks-on-aws.md]

## delete_prompt_version()

The `MlflowClient.delete_prompt_version()` method removes a specific version of a prompt given its full name and version identifier. The version must be passed as a string. For example:

```python
from mlflow import MlflowClient

client = MlflowClient()
client.delete_prompt_version("mycatalog.myschema.chat_assistant", "1")
```

^[prompt-registry-examples-databricks-on-aws.md]

## delete_prompt()

The `MlflowClient.delete_prompt()` method removes an entire prompt record. It can be called after all versions of the prompt have been deleted, or, for non-Unity-Catalog registries, directly. Example:

```python
client.delete_prompt("mycatalog.myschema.chat_assistant")
```

^[prompt-registry-examples-databricks-on-aws.md]

## Important Considerations

- **Unity Catalog registries**: Deleting a prompt fails if any versions still exist. All versions must be deleted first using `delete_prompt_version()`. This is enforced by the registry. ^[prompt-registry-examples-databricks-on-aws.md]
- **Other registry types**: `delete_prompt()` works normally without requiring version deletion beforehand. ^[prompt-registry-examples-databricks-on-aws.md]

For convenience, you can search all versions of a prompt and delete them in a loop before deleting the prompt itself:

```python
search_response = client.search_prompt_versions("mycatalog.myschema.chat_assistant")
for version in search_response.prompt_versions:
    client.delete_prompt_version("mycatalog.myschema.chat_assistant", str(version.version))
client.delete_prompt("mycatalog.myschema.chat_assistant")
```

^[prompt-registry-examples-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- MlflowClient
- [MLflow](/concepts/mlflow.md)
- Prompt Registry register_prompt|register_prompt
- load_prompt

## Sources

- prompt-registry-examples-databricks-on-aws.md

# Citations

1. [prompt-registry-examples-databricks-on-aws.md](/references/prompt-registry-examples-databricks-on-aws-c1a1a7e0.md)
