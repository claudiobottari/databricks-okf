---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e5d138652753d1e9ee44df3842ecffa68ee8c7534825a5fde73b6e6b78943d7
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
    - optimize-multiple-prompts-together-databricks-on-aws.md
    - optimize-prompts-tutorial-databricks-on-aws.md
    - prompt-registry-databricks-on-aws.md
    - track-prompt-versions-alongside-application-versions-databricks-on-aws.md
    - use-prompts-in-deployed-applications-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-prompt-registry
    - MPR
    - aliases in the Prompt Registry
  citations:
    - file: prompt-registry-databricks-on-aws.md
    - file: create-and-edit-prompts-databricks-on-aws.md
    - file: use-prompts-in-deployed-applications-databricks-on-aws.md
    - file: track-prompt-versions-alongside-application-versions-databricks-on-aws.md
    - file: mlflow-prompt-optimization-beta-databricks-on-aws.md
    - file: optimize-prompts-tutorial-databricks-on-aws.md
    - file: optimize-prompts-using-custom-scorers-databricks-on-aws.md
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: MLflow Prompt Registry
description: A centralized system within MLflow for storing, versioning, and managing prompt templates used in GenAI applications, backed by Unity Catalog.
tags:
  - mlflow
  - prompt-management
  - llmops
timestamp: "2026-06-19T17:58:28.466Z"
---

# MLflow Prompt Registry

The **MLflow Prompt Registry** is a centralized repository for managing [GenAI](/concepts/mlflow-genai-evaluate-api.md) prompt templates across their lifecycle within [MLflow](/concepts/mlflow.md) and [Unity Catalog](/concepts/unity-catalog.md). It provides Git-like versioning, alias-based deployment, and integration with GenAI frameworks, enabling teams to version, track, deploy, and collaborate on prompts without code changes.^[prompt-registry-databricks-on-aws.md]

## Overview

The Prompt Registry enables teams to:^[prompt-registry-databricks-on-aws.md]
- **Version and track prompts** with Git-like versioning, commit messages, and rollback capabilities
- **Deploy safely with aliases** using mutable references (e.g., `"production"`, `"staging"`) for A/B testing and gradual rollouts
- **Collaborate without code changes** by allowing non-engineers to modify prompts through the UI
- **Integrate with any framework** including LangChain, LlamaIndex, and other GenAI frameworks
- **Maintain governance** through Unity Catalog integration for access control and audit trails
- **Track lineage** by linking prompts to experiments and evaluation results

Prompts are stored in Unity Catalog schemas and follow a Git-like model with named entities (prompts), immutable version snapshots, mutable aliases, and version-specific tags.^[prompt-registry-databricks-on-aws.md]

## Prerequisites

1. Install MLflow with Unity Catalog support:
   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0"
   ```
2. Create an MLflow experiment by following the [set up your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
3. Access a Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions to view or create prompts.^[prompt-registry-databricks-on-aws.md]

## Quick Start

Register a prompt, set a production alias, and load it in an application:^[prompt-registry-databricks-on-aws.md]

```python
import mlflow
from databricks.sdk import WorkspaceClient

model = "databricks-claude-sonnet-4-5"
llm = WorkspaceClient().serving_endpoints.get_open_ai_client()

# Register a prompt template
prompt = mlflow.genai.register_prompt(
    name="docs.default.customer_support",
    template="You are a helpful assistant. Answer this question: {{question}}",
    commit_message="Initial customer support prompt"
)
print(f"Created version {prompt.version}")  # "Created version 1"

# Set a production alias
mlflow.genai.set_prompt_alias(
    name="docs.default.customer_support",
    alias="production",
    version=1
)

# Load and use the prompt in your application
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/docs.default.customer_support@production"
)
formatted_prompt = prompt.format(question="How do I reset my password?")
response = llm.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": formatted_prompt}],
)
print(response.choices[0].message.content)
```

## Creating and Editing Prompts

### Using the UI

Navigate to your MLflow experiment, click the **Prompts** tab, then click **New prompt**. Provide a name, select **Text** or **Chat** type, enter the template (using `{{variable}}` syntax), and optionally add a commit message. Click **Create**.^[create-and-edit-prompts-databricks-on-aws.md]

### Using the SDK

First, link your experiment to a default Prompt Registry location by setting the `mlflow.promptRegistryLocation` tag:^[create-and-edit-prompts-databricks-on-aws.md]

```python
mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

Then register a prompt with `mlflow.genai.register_prompt()`:^[create-and-edit-prompts-databricks-on-aws.md]

```python
prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template="Summarize content in {{num_sentences}} sentences.\nContent: {{content}}",
    commit_message="Initial version",
    tags={"author": "team@company.com", "task": "summarization"}
)
```

Prompt versions are immutable. To edit, create a new version by calling `register_prompt()` with the same name and an updated template.^[create-and-edit-prompts-databricks-on-aws.md]

## Using Prompts in Applications

### Loading

Use `mlflow.genai.load_prompt()` with a URI in the format `prompts:/catalog.schema.prompt_name@alias` or `prompts:/catalog.schema.prompt_name/version`.^[create-and-edit-prompts-databricks-on-aws.md, use-prompts-in-deployed-applications-databricks-on-aws.md]

```python
prompt = mlflow.genai.load_prompt("prompts:/main.default.summarization_prompt@production")
# or by version
prompt = mlflow.genai.load_prompt("prompts:/main.default.summarization_prompt/1")
```

### Formatting

Template variables use double-brace syntax: `{{variable_name}}`.^[create-and-edit-prompts-databricks-on-aws.md]

```python
formatted = prompt.format(content="Some text", num_sentences=2)
```

### Integration with Other Frameworks

For LangChain, LlamaIndex, and other libraries that use single-brace syntax (`{name}`), use `.to_single_brace_format()` to convert the prompt.^[prompt-registry-databricks-on-aws.md]

## Version Management and Aliases

Aliases provide mutable references to specific versions. To promote a prompt, reassign the alias without redeploying application code.^[use-prompts-in-deployed-applications-databricks-on-aws.md]

```python
mlflow.genai.set_prompt_alias(
    name="main.default.summarization_prompt",
    alias="production",
    version=2
)
```

Common alias strategies include environment aliases (`dev`, `staging`, `production`), feature branch aliases, and regional aliases. A rollback-ready pattern saves the current production version before updating.^[use-prompts-in-deployed-applications-databricks-on-aws.md]

## Tracking Prompt Versions with Application Versions

When you use `mlflow.set_active_model()` before loading a prompt from the registry, MLflow automatically creates lineage between the prompt version and the application version via a [LoggedModel](/concepts/loggedmodel.md).^[track-prompt-versions-alongside-application-versions-databricks-on-aws.md]

```python
active_model_info = mlflow.set_active_model(name="customer_support_agent-v2")
prompt = mlflow.genai.load_prompt("prompts:/workspace.default.customer_support_prompt/1")
```

The lineage is visible in the MLflow Experiment UI under the **Versions** tab.^[track-prompt-versions-alongside-application-versions-databricks-on-aws.md]

## Prompt Optimization with GEPA

The `mlflow.genai.optimize_prompts()` API uses the GEPA algorithm to automatically improve prompt templates. You provide a prediction function, training data with expectations, and scorers; the optimizer registers an improved prompt as a new version.^[mlflow-prompt-optimization-beta-databricks-on-aws.md]

```python
from mlflow.genai.optimize import [[gepapromptoptimizer|GepaPromptOptimizer]]
from mlflow.genai.scorers import Correctness

result = mlflow.genai.optimize_prompts(
    predict_fn=predict_fn,
    train_data=dataset,
    prompt_uris=[prompt.uri],
    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),
    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],
)
optimized_prompt = result.optimized_prompts[0]
```

For custom scorers, use `make_judge` and an aggregation function to map feedback to numerical scores.^[optimize-prompts-tutorial-databricks-on-aws.md, optimize-prompts-using-custom-scorers-databricks-on-aws.md]

When your agent uses multiple chained prompts, you can optimize all of them together by passing multiple URIs to `prompt_uris`. GEPA considers and optimizes each prompt in the chain.^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Template Formats

Prompts can be stored as simple text strings or conversation-style lists of role-based messages. Both use double-brace syntax for variables.^[prompt-registry-databricks-on-aws.md]

```python
# Simple prompt
simple = mlflow.genai.register_prompt(
    name="mycatalog.myschema.greeting",
    template="Hello {{name}}, how can I help you today?"
)
# Chat-style
chat = mlflow.genai.register_prompt(
    name="mycatalog.myschema.analysis",
    template=[
        {"role": "system", "content": "You are a {{style}} assistant."},
        {"role": "user", "content": "{{question}}"},
    ]
)
```

## SDK Functions

| Function | Description |
|----------|-------------|
| `mlflow.genai.register_prompt()` | Create or create a new version of a prompt |
| `mlflow.genai.load_prompt()` | Load a prompt by URI or name/version |
| `mlflow.genai.set_prompt_alias()` | Assign an alias to a version |
| `mlflow.genai.search_prompts()` | Find prompts in a Unity Catalog schema |
| `mlflow.genai.optimize_prompts()` | Automatically optimize prompt templates |
| `mlflow.genai.delete_prompt()` | Delete a prompt (use with caution) |

^[prompt-registry-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The core ML lifecycle framework
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores prompts
- [GenAI](/concepts/mlflow-genai-evaluate-api.md) – MLflow’s suite of tools for generative AI evaluation and deployment
- [Prompt Versioning](/concepts/prompt-versioning.md) – Git-like versioning of prompts
- [Aliases](/concepts/model-aliases.md) – Mutable references to prompt versions
- [LoggedModel](/concepts/loggedmodel.md) – Metadata hub for application version tracking
- [GEPA](/concepts/gepa-gradient-free-evolutionary-prompt-algorithm.md) – GenAI Prompt Optimization
- LangChain Integration – Using prompts with LangChain

## Sources

- create-and-edit-prompts-databricks-on-aws.md
- mlflow-prompt-optimization-beta-databricks-on-aws.md
- optimize-prompts-tutorial-databricks-on-aws.md
- optimize-prompts-using-custom-scorers-databricks-on-aws.md
- optimize-multiple-prompts-together-databricks-on-aws.md
- prompt-registry-databricks-on-aws.md
- track-prompt-versions-alongside-application-versions-databricks-on-aws.md
- use-prompts-in-deployed-applications-databricks-on-aws.md

# Citations

1. [prompt-registry-databricks-on-aws.md](/references/prompt-registry-databricks-on-aws-71dbf9b1.md)
2. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
3. [use-prompts-in-deployed-applications-databricks-on-aws.md](/references/use-prompts-in-deployed-applications-databricks-on-aws-4f504a27.md)
4. [track-prompt-versions-alongside-application-versions-databricks-on-aws.md](/references/track-prompt-versions-alongside-application-versions-databricks-on-aws-08e423d1.md)
5. [mlflow-prompt-optimization-beta-databricks-on-aws.md](/references/mlflow-prompt-optimization-beta-databricks-on-aws-9e2888f4.md)
6. [optimize-prompts-tutorial-databricks-on-aws.md](/references/optimize-prompts-tutorial-databricks-on-aws-b91f2148.md)
7. [optimize-prompts-using-custom-scorers-databricks-on-aws.md](/references/optimize-prompts-using-custom-scorers-databricks-on-aws-428b4fc5.md)
8. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
