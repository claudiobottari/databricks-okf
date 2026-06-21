---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26a72e5e3972dbcc6be8ffa2f5b4ad303cf63816ed6eac43498f861d899f4919
  pageDirectory: concepts
  sources:
    - optimize-multiple-prompts-together-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-model-strategy-in-agent-systems
    - MSIAS
    - multi-agent systems
  citations:
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: Multi-Model Strategy in Agent Systems
description: The practice of using different LLMs for different stages of a multi-prompt pipeline, such as a stronger model for planning and a more cost-efficient model for execution.
tags:
  - architecture
  - cost-optimization
  - agent-systems
  - llm
timestamp: "2026-06-19T19:52:08.411Z"
---

## Multi-Model Strategy in Agent Systems

A **Multi-Model Strategy in Agent Systems** is an architectural pattern where different language models are used for different subtasks within a single agent workflow. Rather than relying on a single monolithic model, the agent delegates specific roles — such as planning, reasoning, or generation — to models best suited for each role, often balancing capability and cost.

### Motivation

Complex agent systems frequently chain multiple prompts together, each requiring different levels of reasoning or domain knowledge. Using a single, expensive, high‑capability model for every step is cost‑inefficient and can be slower. A multi‑model strategy addresses this by assigning the most demanding subtasks (e.g., planning or decomposition) to a strong model, and simpler, high‑volume subtasks (e.g., classification or answer generation) to a smaller, cost‑efficient model. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

### Prompt Optimization Across Models

When multiple models are used, each has its own prompt template. These prompts are interdependent: the output of one model becomes the input context for another. Optimizing them in isolation can lead to sub‑optimal overall performance. Tools like the GEPA (Gradient‑based Evolutionary Prompt Adaptation) prompt optimizer allow practitioners to **optimize all prompts together** as a joint optimization problem. The optimizer considers the entire chain and adjusts each prompt to improve the final outcome. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

### Example: Plan-and-Answer Agent

A canonical example from the Databricks/MLflow ecosystem is a two‑step classification agent:

1. **Planning step** – a strong model (e.g., `databricks-gpt-5`) receives a plan prompt and produces a reasoning plan based on the query.
2. **Answer step** – a cost‑efficient model (e.g., `databricks-gpt-5-nano`) receives the answer prompt, which includes both the original query and the plan, and outputs the final classification label.

Both prompts (`plan_prompt` and `answer_prompt`) are registered and then jointly optimized using `mlflow.genai.optimize_prompts()` with the `GepaPromptOptimizer`. The optimizer evaluates the chain end‑to‑end using a scorer (e.g., `Correctness` with a judge model) and evolves the wording of both prompts to maximize accuracy. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

### Benefits

- **Cost efficiency** – Expensive model invocations are confined to the reasoning step; the answer step uses a cheaper model.
- **Improved accuracy** – Joint optimization ensures that the plan produced by the strong model is in the right format for the weaker model to consume.
- **Modularity** – Each prompt can be versioned, tested, and rolled back independently.

### Related Concepts

- Agent Systems
- Prompt Optimization
- [GEPA Prompt Optimizer](/concepts/gepapromptoptimizer.md)
- [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md)
- Model Chaining
- Cost-Aware Model Selection
- [MLflow](/concepts/mlflow.md)

### Sources

- optimize-multiple-prompts-together-databricks-on-aws.md

# Citations

1. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
