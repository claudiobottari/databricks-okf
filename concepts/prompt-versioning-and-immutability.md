---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a043d3f1984bd5bbfd48dec7039ae16c2befdcabf3963ffc9af0ef93435f23e
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-versioning-and-immutability
    - Immutability and Prompt Versioning
    - PVAI
    - App and Prompt Versioning
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Prompt Versioning and Immutability
description: Prompts in MLflow are immutable once created; edits produce new versions with full history preserved, enabling rollbacks and comparison.
tags:
  - mlflow
  - versioning
  - prompt-management
timestamp: "2026-06-19T17:58:19.372Z"
---

# Prompt Versioning and Immutability

**Prompt Versioning and Immutability** is a core design principle of the [MLflow Prompt Registry](/concepts/prompt-registry.md): every saved version of a prompt is immutable after creation. To modify a prompt, you must create a new version, preserving a complete, auditable history of changes. This Git-like approach enables rollbacks, side‑by‑side comparison, and clear traceability across the lifecycle of a prompt. ^[create-and-edit-prompts-databricks-on-aws.md]

## Overview

Prompt versioning in the MLflow Prompt Registry behaves like Git‑based version control. When a prompt is first created, it is assigned version `1`. Subsequent edits produce a new version with an incremented number (e.g., `2`, `3`). Because each version is immutable, previous versions remain unchanged and can be revisited at any time. ^[create-and-edit-prompts-databricks-on-aws.md]

This immutability ensures that every prompt version used in an application, evaluation, or production deployment can be traced back to an exact snapshot of the template. It eliminates the risk of a silent change breaking a dependent workflow.

## Creating a New Version

To edit a prompt, you must create a new version. The old version stays in the registry with its original content, commit message, and timestamp. ^[create-and-edit-prompts-databricks-on-aws.md]

### Using the Databricks MLflow UI

1. Navigate to the **Prompts** tab of your MLflow experiment.
2. Click the **New version** button next to the prompt you want to edit.
3. Modify the prompt content.
4. (Optional) Add a commit message describing the change.
5. Click **Save**.

The new version is created and stored alongside earlier versions. ^[create-and-edit-prompts-databricks-on-aws.md]

### Using the Python SDK

Call `mlflow.genai.register_prompt()` with the same prompt name to register a new version. The SDK automatically increments the version number. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

new_template = """\
You are an expert summarizer. Condense the following content into exactly {{ num_sentences }} sentences.
Content: {{content}}
"""

updated_prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template=new_template,
    commit_message="Added detailed instructions for better output quality",
    tags={"improvement": "Added specific guidelines"}
)
```

## Comparing Prompt Versions

The MLflow UI provides a **Compare** feature that lets you view the differences between two or more versions side by side. This helps you understand what changed between iterations and decide which version to promote to production or to use in evaluations. ^[create-and-edit-prompts-databricks-on-aws.md]

To compare versions:
1. Click on the prompt name in the **Prompts** tab.
2. In the upper left, click **Compare** and select the versions to compare.

## Loading a Specific Version

When you load a prompt in your application, you can specify a particular version using either a URI syntax or a `version` parameter: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
# URI syntax
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/2"
)

# Version parameter
prompt = mlflow.genai.load_prompt(
    name_or_uri=f"{uc_schema}.{prompt_name}",
    version="2"
)
```

## Benefits of Immutable Versioning

- **Complete history**: Every change is recorded as a version with its content, commit message, and timestamp. ^[create-and-edit-prompts-databricks-on-aws.md]
- **Rollback**: If a new version introduces a regression, you can revert to a previous version without losing the history. ^[create-and-edit-prompts-databricks-on-aws.md]
- **Traceability**: Production deployments can be pinned to a specific version, making it clear which prompt template is in use. ^[create-and-edit-prompts-databricks-on-aws.md]
- **Audit readiness**: Immutable versions support compliance requirements by providing an unalterable record of prompt changes. ^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – The central store for managing prompt versions.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework that provides prompt versioning capabilities.
- [Immutable Versioning](/concepts/delta-table-versioning.md) – The general software engineering principle applied here.
- [Evaluating Prompt Versions](/concepts/prompt-versioning.md) – How version comparison supports iterative evaluation.
- [Tracking Prompts with App Versions](/concepts/prompt-versioning.md) – Linking prompt versions to application releases.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
