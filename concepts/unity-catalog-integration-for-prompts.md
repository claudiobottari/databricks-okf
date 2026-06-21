---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b97b1fbddbff8d77e38ec1a680a1a45cfa743282f7ba11724bf1f5f451a57a3
  pageDirectory: concepts
  sources:
    - prompt-registry-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-integration-for-prompts
    - UCIFP
  citations:
    - file: prompt-registry-databricks-on-aws.md
title: Unity Catalog Integration for Prompts
description: Integration between the Prompt Registry and Unity Catalog for governance, access control, audit trails, and prompt-to-experiment lineage tracking.
tags:
  - mlflow
  - unity-catalog
  - governance
  - databricks
timestamp: "2026-06-19T19:58:25.452Z"
---

# Unity Catalog Integration for Prompts

**Unity Catalog Integration for Prompts** refers to the governance and access control capabilities that the MLflow Prompt Registry inherits through its integration with Unity Catalog. This integration enables teams to manage prompt templates with enterprise-grade security, audit trails, and centralized governance.^[prompt-registry-databricks-on-aws.md]

## Overview

The MLflow Prompt Registry stores prompts as named entities within Unity Catalog, meaning they benefit from Unity Catalog's existing access control framework. This allows organizations to apply the same governance policies to prompt templates that they use for other data assets such as tables, models, and notebooks.^[prompt-registry-databricks-on-aws.md]

Key governance features provided by this integration include:

- **Access control**: Unity Catalog permissions determine who can view, create, edit, or manage prompts and their versions.
- **Audit trails**: All changes to prompts are tracked through Unity Catalog's logging capabilities, providing a complete history of modifications.
- **Lineage tracking**: Prompts can be linked to experiments and evaluation results, creating a traceable path from prompt creation through deployment.

^[prompt-registry-databricks-on-aws.md]

## Prerequisites for Unity Catalog Integration

To use prompts with Unity Catalog integration, users must have the following Unity Catalog permissions on a schema:^[prompt-registry-databricks-on-aws.md]

- `CREATE FUNCTION` – Required to create new prompts within the schema.
- `EXECUTE` – Required to load and use prompts.
- `MANAGE` – Required to manage prompts, including setting aliases and updating versions.

Additionally, the environment must have MLflow with Unity Catalog support installed:^[prompt-registry-databricks-on-aws.md]

```bash
pip install --upgrade "mlflow[databricks]>=3.1.0"
```

## Prompt Registry as Unity Catalog Entities

Prompts in the Prompt Registry follow a Git-like model and are stored as named entities within Unity Catalog schemas. Each prompt exists within a three-level namespace: `catalog.schema.prompt_name`. For example, `docs.default.customer_support` refers to the "customer_support" prompt in the "default" schema of the "docs" catalog.^[prompt-registry-databricks-on-aws.md]

The entity structure includes:^[prompt-registry-databricks-on-aws.md]

- **Prompts**: Named entities in Unity Catalog.
- **Versions**: Immutable snapshots with auto-incrementing numbers.
- **Aliases**: Mutable pointers to specific versions (e.g., "production", "staging").
- **Tags**: Version-specific key-value pairs.

## Benefits of Unity Catalog Integration

The integration provides several advantages for prompt management:^[prompt-registry-databricks-on-aws.md]

- **Collaboration without code changes**: Non-engineers can modify prompts through the UI while Unity Catalog enforces appropriate permissions.
- **Safe deployment with aliases**: Teams can use mutable references such as "production" or "staging" for A/B testing and gradual rollouts, all governed by Unity Catalog policies.
- **Centralized governance**: Organizations maintain consistent access control and audit trails across all prompt versions.

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) – The centralized repository for managing prompt templates.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance and access control platform that underpins this integration.
- [Prompt Version Management](/concepts/prompt-version-management.md) – Versioning and lifecycle management for prompts.
- [Prompt Aliases](/concepts/prompt-aliases.md) – Mutable references that point to specific prompt versions.
- [Prompt Templates](/concepts/prompt-templates-with-variables.md) – The template formats supported by the Prompt Registry.

## Sources

- prompt-registry-databricks-on-aws.md

# Citations

1. [prompt-registry-databricks-on-aws.md](/references/prompt-registry-databricks-on-aws-71dbf9b1.md)
