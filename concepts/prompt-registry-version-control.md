---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a3df356753f60de92aa8992f0c15d2830fa2e374da0668da598249703bc81f5
  pageDirectory: concepts
  sources:
    - mlflow-prompt-optimization-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-version-control
    - PRVC
    - Prompt Registry Versioning
  citations:
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
title: Prompt Registry Version Control
description: MLflow Prompt Registry's automatic registration of optimized prompts, enabling version control and retrieval of prompt versions via URIs like prompts:/{prompt_location}@latest.
tags:
  - mlflow
  - prompt-registry
  - version-control
timestamp: "2026-06-19T19:39:32.018Z"
---

# Prompt Registry Version Control

**Prompt Registry Version Control** refers to the system within [MLflow](/concepts/mlflow.md) that tracks, manages, and stores different versions of prompts used in generative AI applications. The Prompt Registry provides versioning capabilities that enable users to iterate on prompts systematically, compare performance across versions, and deploy specific versions to production environments.

## Overview

The MLflow Prompt Registry stores prompts as versioned entities, allowing users to create, update, and manage prompt iterations over time. Each prompt version is associated with a unique identifier and can be retrieved, compared, and deployed independently. This version control system is essential for maintaining prompt quality and reproducibility in production AI applications. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Automatic Version Registration

When using the `mlflow.genai.optimize_prompts()` API for Prompt Optimization, optimized prompts are automatically registered as new versions in the Prompt Registry. This integration ensures that every optimization run produces a traceable version entry, enabling users to track improvements and revert to previous versions if needed. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Version Retrieval

Prompts can be loaded from the registry using their version identifier. The `mlflow.genai.load_prompt()` function supports loading prompts by URI, including the `@latest` tag to retrieve the most recent version. This mechanism is critical for ensuring that [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) and production scoring workflows use the correct prompt version. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Loading a Prompt Version

```python
# Load the latest version of a prompt
prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}@latest")

# Format the prompt with input data
formatted_prompt = prompt.format(question=question)
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Version Control in Optimization Workflows

During Prompt Optimization, the version control system plays a key role in ensuring that optimization algorithms work with the correct prompt versions. The `predict_fn` used in optimization must call `mlflow.entities.model_registry.PromptVersion.format()` to load prompts from the registry rather than using hardcoded prompt strings. This ensures that optimization results are properly linked to their source prompt versions. ^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

### Correct Usage

```python
# ✅ Correct - loads from registry
def predict_fn(question: str):
    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}@latest")
    return llm_call(prompt.format(question=question))
```

### Incorrect Usage

```python
# ❌ Incorrect - hardcoded prompt
def predict_fn(question: str):
    return llm_call(f"Answer: {question}")
```

^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

## Benefits

- **Traceability**: Every prompt change is recorded as a distinct version with metadata
- **Reproducibility**: Previous prompt versions can be retrieved and used for comparison or rollback
- **Collaboration**: Multiple team members can work on different prompt versions simultaneously
- **Deployment Control**: Specific versions can be promoted to production while others remain in development
- **Audit Trail**: Version history provides a complete record of prompt evolution over time

## Related Concepts

- Prompt Optimization — Automated improvement of prompts using evaluation metrics
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for tracking prompt optimization runs
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow that uses versioned prompts
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduled scoring that relies on specific prompt versions
- [PromptVersion](/concepts/prompt-versioning.md) — The registry entity representing a specific prompt iteration

## Sources

- mlflow-prompt-optimization-beta-databricks-on-aws.md

# Citations

1. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
