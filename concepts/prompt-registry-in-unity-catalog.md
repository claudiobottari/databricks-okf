---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c34e70c971eb6e5afd46d5f122ccdbc4b526c5f67c08fe1fecbb61afbc679baa
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-in-unity-catalog
    - PRIUC
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Prompt Registry in Unity Catalog
description: A centralized prompt management system for browsing, versioning, and aliasing GenAI prompts stored in Unity Catalog
tags:
  - prompt-management
  - unity-catalog
  - genai
  - mlflow
timestamp: "2026-06-19T18:58:57.338Z"
---

# Prompt Registry in Unity Catalog

The **Prompt Registry** in [Unity Catalog](/concepts/unity-catalog.md) is a system for storing, organizing, versioning, and loading prompt templates used by GenAI agents and [MLflow GenAI](/concepts/mlflow-3-for-genai.md) applications. Prompt versions are stored as securable objects within a Unity Catalog schema and can be managed, evaluated, and deployed using the MLflow GenAI API. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

The Prompt Registry allows you to register prompt templates into a [Catalog and Schema](/concepts/catalog-and-schema.md) of your choice. Each registered prompt is a named object with associated metadata such as its template string, a version number (incremented automatically with each registration), and an optional commit message. You create a prompt using `mlflow.genai.register_prompt()` and later load it by name and version using `mlflow.genai.load_prompt()` with a URI of the form `prompts:/<catalog>.<schema>.<name>/<version>`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The registry enables systematic evaluation of different prompt versions to identify the most effective ones for your agents and GenAI applications. By comparing performance across versions against consistent evaluation datasets, teams can make data-driven decisions about which prompts to promote to production. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Prerequisites

To use the Prompt Registry, you need:

- **MLflow 3.1.0 or higher**.
- **Access to an OpenAI API endpoint or [Databricks Model Serving](/concepts/databricks-model-serving.md)**.
- **A [Unity Catalog](/concepts/unity-catalog.md) schema** on which you hold `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges. `CREATE FUNCTION` is required because prompt evaluation often relies on user-defined functions stored in Unity Catalog. `EXECUTE` allows the evaluation runtime to invoke models, and `MANAGE` is required to register or modify prompt objects. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

If you are using a Databricks trial account, the required permissions on the Unity Catalog schema `workspace.default` are already granted. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Creating Prompt Versions

To register a new prompt version, call `mlflow.genai.register_prompt()` and pass a `name` (fully qualified with [Catalog and Schema](/concepts/catalog-and-schema.md)), a `template` string, and a `commit_message`. The function returns an object with a `version` field reflecting the new version number. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
prompt_v1 = mlflow.genai.register_prompt(
    name="main.default.summary_prompt",
    template="Summarize this text: {{content}}",
    commit_message="v1: Basic summarization prompt"
)
print(f"Created prompt version {prompt_v1.version}")
```

Each call with the same `name` creates a new immutable version. If you call `register_prompt` again with a different template, it registers the next version in the sequence. This enables iterative improvement — you can start simple, evaluate, then refine your prompt and register the improved version as v2. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Loading Prompt Versions

To load a specific version, use `mlflow.genai.load_prompt()` with a URI of the form `prompts:/catalog.schema.prompt_name/version`. The loaded prompt object can then be used to format its template with the provided arguments: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/main.default.summary_prompt/1"
)
formatted_prompt = prompt.format(content="Hello world")
```

After identifying the best performing prompt version through evaluation, you can deploy it using aliases for production deployment without changing your application code. For more details, see Use prompts in deployed apps. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

1. **Start simple.** Begin with basic prompts and iteratively improve based on evaluation results. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
2. **Use consistent evaluation datasets.** Evaluate all versions against the same data to ensure fair comparison. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
3. **Track everything.** Log prompt versions, evaluation results, and deployment decisions. Use `mlflow.start_run()` to tie evaluations to an [MLflow Run](/concepts/mlflow-run.md) for later comparison. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
4. **Test edge cases.** Include challenging examples that stress the prompt's ability to follow constraints (e.g., sentence limits, fact coverage). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
5. **Monitor in production.** After deployment, continue to evaluate prompts against new data to detect degradation. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
6. **Document changes.** Use meaningful commit messages, as they serve as the primary record of why a change was made. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Evaluation Workflow

The typical evaluation workflow in the Prompt Registry follows these steps: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

1. **Register prompt versions** — create at least two versions representing different approaches to the task (e.g., a basic prompt and an improved version with comprehensive guidelines). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

2. **Create an evaluation dataset** — use `mlflow.genai.datasets.create_dataset()` to build a table of input-output pairs. Include `expectations` (such as expected facts) for judge-based scoring. The dataset is stored in a Unity Catalog table. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

3. **Define evaluation functions** — wrap the call that loads a prompt version and sends it to an LLM in a function decorated with `@mlflow.trace`. The trace ensures MLflow captures the full execution path for observability. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

4. **Create custom judges** — use `make_judge()` from `mlflow.genai` to build LLM-based scorers that evaluate specific criteria (e.g., sentence count compliance, fact coverage). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

5. **Run comparative evaluation** — use `mlflow.genai.evaluate()` to score each prompt version against the same dataset and the same set of scorers. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

6. **Select the best version** — compare composite scores (e.g., a weighted combination of correctness and compliance) to choose a winner. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Relation to ABAC GRANT Policies

Prompt Registry objects are securable entities in Unity Catalog. Access to them can be controlled by [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — for example, a policy that grants `EXECUTE` on all prompts in a schema that carry a governed tag such as `lifecycle = 'production'`. This allows fine-grained access control without needing to grant permissions on each prompt individually. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Browsing with Genie Code

The Prompt Registry can also be browsed conversationally using [Genie Code](/concepts/genie-code.md), which provides a natural language interface for understanding, debugging, and improving GenAI applications within MLflow. Genie Code can browse prompts in Unity Catalog, view templates, versions, and aliases — all through conversational queries instead of navigating multiple UI pages. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that hosts the Prompt Registry.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The toolkit used to register, load, and evaluate prompts.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used during evaluation (created via `make_judge()`).
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — A dataset stored in Unity Catalog for consistent evaluation across prompt versions.
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Attribute-based policies that can control access to prompts.
- [Prompt Versioning](/concepts/prompt-versioning.md) — The mechanism for tracking iterations of a single prompt name.
- Deployment Aliases — Used to point production systems to a specific version without code changes.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for tracking evaluation runs.
- [Genie Code](/concepts/genie-code.md) — Natural language interface for exploring prompts and evaluation data.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Observability framework that captures execution paths during prompt evaluation.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md
- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
3. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
