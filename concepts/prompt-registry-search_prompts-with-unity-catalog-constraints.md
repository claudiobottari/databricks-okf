---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 06c23c92a08824700e7cba3c0fc2cfe86e4ee99d9b72929584919ce302983031
  pageDirectory: concepts
  sources:
    - prompt-registry-examples-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-search_prompts-with-unity-catalog-constraints
    - PRSWUCC
  citations:
    - file: prompt-registry-examples-databricks-on-aws.md
title: Prompt Registry search_prompts with Unity Catalog constraints
description: Searching prompts in Unity Catalog registries is restricted to catalog.schema filter pairs; name patterns, tag filters, and combined filters are unsupported, requiring programmatic post-filtering.
tags:
  - mlflow
  - prompt-management
  - unity-catalog
timestamp: "2026-06-19T19:58:35.114Z"
---

```markdown
# Prompt Registry `search_prompts` with Unity Catalog Constraints

The `search_prompts` function from the [[Prompt Registry API (mlflow.genai)|Prompt Registry (MLflow GenAI)]] API (`mlflow.genai.search_prompts`) enables retrieving prompt definitions stored in the registry. When using a **Unity Catalog-backed prompt registry**, the function imposes specific constraints on the query filter string. ^[prompt-registry-examples-databricks-on-aws.md]

## Unity Catalog Requirements

For Unity Catalog prompt registries, the filter string **must** include both `catalog` and `schema`. The only supported filter format is:

```
catalog = '<catalog_name>' AND schema = '<schema_name>'
```

The API does **not** accept any other filter keys or operators. Attempting to use a different format will result in an error. ^[prompt-registry-examples-databricks-on-aws.md]

**Example:**

```python
results = mlflow.genai.search_prompts("catalog = 'mycatalog' AND schema = 'myschema'")
```

This returns all prompts defined within the specified Unity Catalog [[catalog-and-schema|Catalog and Schema]]. ^[prompt-registry-examples-databricks-on-aws.md]

## Limitations

The following filter expressions are **not supported** in Unity Catalog prompt registries:

- **Name patterns** – e.g., `name LIKE '%pattern%'`
- **Tag filtering** – e.g., `tags.field = 'value'`
- **Exact name matching** – e.g., `name = 'specific.name'`
- **Combined filters** – any filter beyond the required `catalog + schema` pair

These limitations mean you cannot narrow down the search results within the API call itself. ^[prompt-registry-examples-databricks-on-aws.md]

## Recommended Workflow: Post-Process Results Programmatically

Because the filter is limited to [[catalog-and-schema|Catalog and Schema]], the recommended approach is to retrieve all prompts in the schema and then filter the returned list in Python. This allows you to find prompts by name or tags programmatically.

```python
# Get all prompts in the schema
all_prompts = mlflow.genai.search_prompts(
    "catalog = 'mycatalog' AND schema = 'myschema'"
)

# Filter by name substring
customer_prompts = [p for p in all_prompts if 'customer' in p.name.lower()]

# Filter by tag value
tagged_prompts = [p for p in all_prompts if p.tags.get('team') == 'support']
```

^[prompt-registry-examples-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog]] – The [[metastore|Metastore]] that backs the prompt registry and requires the catalog/schema filter.
- [[MLflow Prompt Registry]] – The overall system for storing and versioning prompts.
- mlflow.genai.search_prompts – The API reference for the function.
- mlflow.genai.register_prompt – The companion function for creating prompts.
- mlflow.genai.load_prompt – Loading a specific prompt version.

## Sources

- prompt-registry-examples-databricks-on-aws.md
```

# Citations

1. [prompt-registry-examples-databricks-on-aws.md](/references/prompt-registry-examples-databricks-on-aws-c1a1a7e0.md)
