---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0945f544a582b6a1c587118abb747b11f0e0fa9dd23496bd4028ab74db75e27
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
    - correctness-judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - llm-as-a-judge-paradigm
    - LLM-as-judge|LLM-based judges
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
    - file: correctness-judge-databricks-on-aws.md
title: LLM-as-a-Judge Paradigm
description: The pattern of using large language models themselves as evaluators to assess quality dimensions of other LLM outputs, as implemented by Databricks-hosted judge models.
tags:
  - llm-evaluation
  - genai
  - mlflow
timestamp: "2026-06-19T14:10:56.750Z"
---

## LLM-as-a-Judge Paradigm

The **LLM-as-a-Judge paradigm** is an evaluation approach in which a large language model (LLM) is used to assess the quality of outputs produced by another LLM or GenAI application. Instead of relying solely on human annotation or traditional metrics, the judge LLM scores responses along predefined quality dimensions such as relevance, safety, groundedness, and correctness. ^[built-in-llm-judges-databricks-on-aws.md]

### How It Works

A judge takes as input the original user query, the application’s response, and optionally a reference answer (ground truth). It then returns a structured verdict (e.g., `"yes"`/`"no"`, a category, or a numeric score) along with a natural language rationale explaining the judgment. The judge can be a general-purpose LLM or a model fine-tuned for evaluation tasks. ^[correctness-judge-databricks-on-aws.md]

### Built-in Judges

Many platforms, including Databricks, provide **built-in LLM judges** — predefined scorers that use Databricks-hosted LLMs to evaluate common quality dimensions. These judges allow teams to start evaluating quickly without designing custom prompts. The following table lists available built-in judges and what they assess: ^[built-in-llm-judges-databricks-on-aws.md]

| Judge | Arguments | Requires Ground Truth | What It Evaluates |
|-------|-----------|------------------------|-------------------|
| `RelevanceToQuery` | `inputs`, `outputs` | No | Is the response directly relevant to the user's request? |
| `RetrievalRelevance` | `inputs`, `outputs` | No | Is the retrieved context directly relevant to the user's request? |
| `Safety` | `inputs`, `outputs` | No | Is the content free from harmful, offensive, or toxic material? |
| `RetrievalGroundedness` | `inputs`, `outputs` | No | Is the response grounded in the provided context (no hallucination)? |
| `Correctness` | `inputs`, `outputs`, `expectations` | Yes | Is the response factually correct compared to ground truth? |
| `RetrievalSufficiency` | `inputs`, `outputs`, `expectations` | Yes | Does the context provide all necessary information to cover the ground truth facts? |
| `Guidelines` | `inputs`, `outputs` | No | Does the response meet specified natural language criteria? |
| `ExpectationsGuidelines` | `inputs`, `outputs`, `expectations` | No (needs guidelines in expectations) | Does the response meet per-example natural language criteria? |
| `ToolCallCorrectness` | `inputs`, `outputs`, `expectations` | Yes | Are the tool calls and arguments correct for the user query? |
| `ToolCallEfficiency` | `inputs`, `outputs` | No | Are the tool calls efficient without redundancy? |

Built-in judges can be used directly or as part of a comprehensive evaluation pipeline via `mlflow.genai.evaluate()`. ^[built-in-llm-judges-databricks-on-aws.md]

#### Example: Correctness Judge

The `Correctness` judge compares an application’s response against `expected_facts` or `expected_response`. For instance, if the query is “What is MLflow?” and the expected facts are `["MLflow is open-source", "MLflow is an AI engineering platform"]`, the judge returns `"yes"` if all facts are present and `"no"` otherwise. Using `expected_facts` allows more flexible evaluation (word-for-word matching is not required).^[correctness-judge-databricks-on-aws.md]

### Multi-turn Judges

For conversational AI, the paradigm extends to **multi-turn judges** that evaluate entire conversations rather than individual turns. These judges analyze the complete conversation history to assess quality patterns that emerge over multiple interactions, such as coherence, helpfulness, or safety across turns.^[built-in-llm-judges-databricks-on-aws.md]

### Customization and Control

When built-in judges do not fit a specific use case, practitioners can build **custom LLM judges** or use **Python code-based scorers**. Custom judges allow full control over the prompt, grading criteria, and the underlying LLM. The judge LLM can be changed by specifying a `model` argument (e.g., `"databricks:/databricks-gpt-5-mini"` or any LiteLLM-compatible provider). ^[built-in-llm-judges-databricks-on-aws.md]

### Advantages and Considerations

- **Scalability**: LLM judges can evaluate thousands of responses without human fatigue.
- **Consistency**: When the same judge is applied across configurations, results are comparable.
- **Interpretability**: Judges provide rationales, helping developers understand why a score was assigned.
- **Limitations**: Judges may inherit biases from their training data and may not perfectly align with human judgment. Periodic Align judges with human feedback is recommended to improve accuracy on domain-specific tasks.

### Related Concepts

- [GenAI application evaluation](/concepts/genai-application-evaluation-lifecycle.md)
- [Custom LLM Judge](/concepts/custom-llm-judge.md)
- [Scorer (MLflow)](/concepts/scorers-mlflow-genai.md)
- [Correctness Judge](/concepts/correctness-judge.md)
- [Safety judge](/concepts/safety-judge-mlflow.md)
- [Multi-turn evaluation](/concepts/multi-turn-conversation-evaluation.md)
- [Human feedback alignment](/concepts/human-feedback-for-llm-judge-alignment.md)
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)

### Sources

- built-in-llm-judges-databricks-on-aws.md
- correctness-judge-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
2. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
