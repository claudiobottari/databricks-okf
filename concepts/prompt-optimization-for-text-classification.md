---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cb7b66da2211babaf304aac69f4ad9947f89d90ce7a47667c2455a995823021
  pageDirectory: concepts
  sources:
    - optimize-prompts-tutorial-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-optimization-for-text-classification
    - POFTC
  citations:
    - file: optimize-prompts-tutorial-databricks-on-aws.md
title: Prompt Optimization for Text Classification
description: The pattern of using prompt optimization to align a generic classification prompt to a specific set of label categories and formatting constraints
tags:
  - classification
  - prompt-engineering
  - nlp
timestamp: "2026-06-19T19:52:24.713Z"
---

Here is the wiki page for "Prompt Optimization for Text Classification", written based solely on the provided source material.

---

## Prompt Optimization for Text Classification

**Prompt Optimization for Text Classification** is the process of automatically refining a prompt used with a [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) to improve its performance on classification tasks. This technique is particularly useful when a simple, hand-written prompt ("classify this query") produces outputs that are not aligned with the specific task, output format, or constraints of the use case. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Overview

A bare-bones prompt like "classify this: {{query}}" may yield correct classifications, but the output will not be aligned to any specific task or use case. By providing examples of desired inputs and outputs, prompt optimization guides the model to produce outputs that conform to a predefined schema, such as outputting only a single word from a fixed set of labels without additional explanation. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Workflow

The typical optimization workflow involves:

1.  **Register an initial prompt:** A simple template like `classify this: {{query}}` is registered in a [Prompt Registry](/concepts/prompt-registry.md). ^[optimize-prompts-tutorial-databricks-on-aws.md]
2.  **Define a prediction function:** A function that loads the prompt template and sends it, along with the user query, to an LLM for completion. ^[optimize-prompts-tutorial-databricks-on-aws.md]
3.  **Prepare training data:** A dataset of inputs (the query) and expected outputs (the correct label) is assembled. The data can also include `expectations` that define constraints, such as "Classification label must be 'CONCLUSIONS', 'RESULTS', 'METHODS', 'OBJECTIVE', 'BACKGROUND'". ^[optimize-prompts-tutorial-databricks-on-aws.md]
4.  **Run optimization:** The system uses an optimizer—such as GEPA (an evolutionary prompt optimization algorithm)—to iteratively refine the prompt. The optimizer is guided by a [[Scorers|scorer]], such as the MLflow `Correctness` evaluator, which measures how well the prompt's outputs match the expected labels. ^[optimize-prompts-tutorial-databricks-on-aws.md]
5.  **Review and deploy:** The optimized prompt is saved as a new version in the prompt registry. It can then be loaded and used in the prediction function in place of the original prompt. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Key Components

#### Optimizer (GEPA)

GEPA (Genetic Evolutionary Prompt Adaptation) is an optimizer that reflects on the prompt and training data to generate improved candidates. In the example workflow, it uses `databricks-claude-sonnet-4-5` as a reflection model to analyze and rewrite the prompt. ^[optimize-prompts-tutorial-databricks-on-aws.md]

#### Scorer

The scorer evaluates the quality of the prompt's outputs. The `Correctness` scorer from `mlflow.genai.scorers` is used to compare the LLM's response against the expected label. In the example, it uses `databricks-gpt-5` as an evaluator model. ^[optimize-prompts-tutorial-databricks-on-aws.md]

#### Training Data

Training data consists of a list of dictionaries, each containing:
- `inputs`: The query text to be classified.
- `outputs`: The expected ground-truth label (e.g., `{"response": "METHODS"}`).
- `expectations`: Constraints such as "expected facts" that define the allowed label set and formatting rules. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Example: Abstract Section Classification

A concrete example from the source material classifies sentences from medical research abstracts into one of five sections: `CONCLUSIONS`, `RESULTS`, `METHODS`, `OBJECTIVE`, or `BACKGROUND`. The initial prompt is `classify this: {{query}}`. After optimization with 6 training examples (including queries like "The emergence of HIV as a chronic condition..." labeled `BACKGROUND` and "Participants will access the program..." labeled `METHODS`), the system produces a refined prompt that reliably outputs only the correct label word. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Benefits

- **Alignment:** Automatically aligns model behavior to domain-specific classification schemas and formatting rules. ^[optimize-prompts-tutorial-databricks-on-aws.md]
- **Constraint enforcement:** Can enforce that the model outputs only from a predefined set of labels without any explanatory text. ^[optimize-prompts-tutorial-databricks-on-aws.md]
- **Automation:** Eliminates manual trial-and-error prompt engineering by using data-driven optimization. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Related Concepts

- Prompt Engineering
- [Prompt Registry](/concepts/prompt-registry.md)
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md)
- [GEPA Optimizer](/concepts/gepapromptoptimizer.md)
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)
- [Classification](/concepts/data-classification.md)

### Sources

- optimize-prompts-tutorial-databricks-on-aws.md

# Citations

1. [optimize-prompts-tutorial-databricks-on-aws.md](/references/optimize-prompts-tutorial-databricks-on-aws-b91f2148.md)
