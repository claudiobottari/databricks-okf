---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36d12808db375cb34f77b00a327fb28d1341d13d5a43a9a1a1070ed4d97aabd3
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - guidelines-and-tool-call-judges
    - Tool Call Judges and Guidelines
    - GATCJ
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Guidelines and Tool Call Judges
description: A category of built-in LLM judges that evaluate responses against natural language criteria (Guidelines, ExpectationsGuidelines) or assess tool call quality (ToolCallCorrectness, ToolCallEfficiency).
tags:
  - llm-evaluation
  - databricks
  - tool-calling
timestamp: "2026-06-19T14:11:00.584Z"
---

## Guidelines and Tool Call Judges

**Guidelines and Tool Call Judges** are a subset of [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that evaluate whether a GenAI application’s responses comply with specified natural-language criteria and whether its tool calls are correct and efficient. They are predefined scorers that use Databricks-hosted LLMs, requiring no custom model deployment. ^[built-in-llm-judges-databricks-on-aws.md]

### Guidelines Judges

Guidelines judges assess whether a response adheres to a set of user-defined natural-language requirements. Two variants are available:

- **`Guidelines`** – Evaluates responses against a fixed set of criteria specified at evaluation time. It takes `inputs` and `outputs` as arguments and does not require ground truth. The underlying question is: *Does the response meet specified natural language criteria?* ^[built-in-llm-judges-databricks-on-aws.md]

- **`ExpectationsGuidelines`** – Evaluates responses against criteria that can vary per example, provided via the `expectations` column of the evaluation dataset. It takes `inputs`, `outputs`, and `expectations` as arguments. Although it does not require a separate ground‑truth column, the guidelines themselves are embedded in the expectations. The question evaluated is: *Does the response meet per-example natural language criteria?* ^[built-in-llm-judges-databricks-on-aws.md]

Use the `Guidelines` judge when the same set of rules applies to every example (e.g., “do not mention competitors”). Use `ExpectationsGuidelines` when each example needs its own unique instruction (e.g., “the response should include product X for this query”). Both judges check for compliance with natural-language criteria rather than numeric or categorical constraints. ^[built-in-llm-judges-databricks-on-aws.md]

### Tool Call Judges

Tool Call judges evaluate the correctness and efficiency of tool calls made by an agent during execution. Two judges are available:

- **`ToolCallCorrectness`** – Validates whether the tool calls and their arguments are correct for the given user query. It requires ground truth (provided in the `expectations` column) to compare the agent’s tool calls against the expected set. It takes `inputs`, `outputs`, and `expectations` as arguments. ^[built-in-llm-judges-databricks-on-aws.md]

- **`ToolCallEfficiency`** – Assesses whether the tool calls were made efficiently, without redundancy or unnecessary invocations. It does not require ground truth; instead, it analyzes the sequence of tool calls in the agent’s output for the given input. It takes `inputs` and `outputs` as arguments. ^[built-in-llm-judges-databricks-on-aws.md]

These judges are particularly useful for evaluating GenAI agent systems that interact with external tools or APIs, such as retrieval‑augmented generation pipelines or multi‑step reasoning agents. ^[built-in-llm-judges-databricks-on-aws.md]

### Usage Notes

- All four judges are available as predefined scorers in [MLflow evaluation](/concepts/mlflow-evaluation-ui.md). For the complete API and argument details, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/). ^[built-in-llm-judges-databricks-on-aws.md]
- When the built-in judges do not fit your use case, you can build [Custom LLM Judges](/concepts/custom-llm-judges.md) or Python‑based [Code-based Scorers](/concepts/code-based-scorers.md). ^[built-in-llm-judges-databricks-on-aws.md]
- To improve judge accuracy for your specific domain, see Align judges with human feedback. ^[built-in-llm-judges-databricks-on-aws.md]

### Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Custom LLM Judges](/concepts/custom-llm-judges.md)
- [[Scorers]]
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md)
- GenAI agent
- Guidelines (as a scorer concept)

### Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
