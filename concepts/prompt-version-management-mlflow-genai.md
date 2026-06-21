---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15a40de12e3185d0afa8fc6734c124ea4efe1815d54dd09919ee94e8b594fd40
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-version-management-mlflow-genai
    - PVM(G
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Prompt Version Management (MLflow GenAI)
description: Version-controlled templates for LLM prompts with Git-like history, variables, aliases, and links to evaluation runs for quality tracking.
tags:
  - mlflow
  - prompts
  - version-management
timestamp: "2026-06-18T14:41:48.286Z"
---



# Prompt Version Management (MLflow GenAI)

**Prompt Version Management** within MLflow GenAI is a system for version-controlling LLM prompt templates, treating them as first-class artifacts with Git-like version history, aliases, and quality tracking. It is part of [MLflow for GenAI](/concepts/mlflow-3-for-genai.md)'s broader data model for generative AI applications.

## Overview

Prompts in MLflow are version-controlled templates for LLM prompt sequences. They are tracked with a Git-like version history that records changes over time. Prompts use `{{variable}}` syntax for dynamic content generation, allowing the same template to produce different outputs based on input parameters. ^[concepts-data-model-databricks-on-aws.md]

Prompts are linked to evaluation runs to track their quality over time, and support aliases such as "production" for deployment management. This allows teams to maintain multiple prompt variants, compare their performance, and promote the best-performing version to production. ^[concepts-data-model-databricks-on-aws.md]

## How Prompt Versioning Works

### Version History

Each prompt template has a version history that records every change. When you modify a prompt, MLflow creates a new version, preserving the previous one. This allows you to:

- Review what changed and when
- Revert to a previous version if needed
- Compare prompt variants side-by-side

### Aliases

Prompts support aliases for deployment management. Common aliases include:

- `production` — the currently deployed prompt
- `staging` — the prompt being tested before promotion
- `development` — the prompt for active development

Aliases let you point to different versions without changing your application code. You update the alias, and your application uses the new prompt.

### Variable Substitution

Prompts use `{{variable}}` syntax for dynamic content. For example:

```
You are a {{role}} assistant. Answer the user's question: {{question}}
```

When the prompt is used, `{{role}}` and `{{question}}` are replaced with actual values from the application context. This allows the same prompt template to serve different use cases — such as a customer support agent or a coding assistant — by changing the variable values.

## Quality Tracking

Prompts are linked to evaluation runs, which trace the quality of outputs back to the specific prompt version that generated them. This provides:

- **Quality history** — See how prompt changes affect output quality over time
- **Regression detection** — Identify when a prompt change decreases quality
- **Version comparison** — Compare two prompt versions against the same evaluation dataset

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The container that organizes all prompt, trace, and evaluation data
- [Evaluation Runs](/concepts/evaluation-runs.md) — Test results linked to specific prompt versions
- [Traces](/concepts/traces.md) — Execution logs that capture which prompt version was used
- [Logged Models](/concepts/logged-models.md) — Snapshots that link application versions to specific prompt versions
- [Prompts](/concepts/prompt-versioning.md) — The broader prompt registry concept in MLflow GenAI
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing prompt variants using custom judges

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
