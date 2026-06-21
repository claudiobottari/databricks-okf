---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec7b0ef7e1c03ce605be0af3bee5bc33312162a42be7cad43834f9236b589610
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - llm-as-a-judge-evaluation-metrics
    - LEM
    - LLM Evaluation Metrics
    - LLM-based metrics
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: deepeval-scorers-databricks-on-aws.md
title: LLM-as-a-Judge Evaluation Metrics
description: DeepEval provides LLM-based evaluation metrics that require a model parameter to act as the judge for scoring outputs
tags:
  - llm
  - evaluation
  - judge
  - metrics
timestamp: "2026-06-18T15:14:43.448Z"
---

# LLM-as-a-Judge Evaluation Metrics

**LLM-as-a-Judge Evaluation Metrics** refer to a class of evaluation techniques where a large language model (LLM) is used as an automated scorer to assess the quality of outputs from other AI systems, particularly other LLMs and GenAI agents. This approach is central to modern AI evaluation pipelines, enabling automated, scalable assessment of response quality without relying solely on human annotation.

## Overview

LLM-as-a-Judge evaluation uses a separate LLM (the "judge") to score outputs from a target system against defined quality criteria. This contrasts with traditional metrics like BLEU or ROUGE that rely on lexical overlap, and with human evaluation that requires manual annotation. The judge LLM evaluates outputs based on its understanding of natural language instructions, context, and desired behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Core Components

### Judge Configuration

A judge is typically configured with:
- **Name** – A descriptive identifier for the evaluation criterion
- **Instructions** – Natural language description of what to evaluate
- **Feedback value type** – The type of output (boolean, categorical, or numeric)
- **Model specification** – The LLM to use as the judge (e.g., `"databricks:/databricks-gpt-5-mini"`) ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Evaluation Dataset

The evaluation dataset contains input-output pairs that the judge assesses. Each entry includes:
- `inputs` – The conversation history or context provided to the target system
- `outputs` – The response from the system being evaluated
- Optional `expectations` – Reference answers that judges can use for comparison ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Feedback Values

Judges return structured feedback values that categorize the quality of responses: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

| Judge Type | Feedback Values | Purpose |
|------------|-----------------|---------|
| Issue Resolution | `fully_resolved`, `partially_resolved`, `needs_follow_up` | Assesses outcome quality |
| Expected Behaviors | `meets_expectations`, `partially_meets`, `does_not_meet` | Checks specific behaviors |
| Tool Call Correctness | `true`, `false` | Validates tool usage |

## Evaluation Approaches

### Input/Output Judges

These judges evaluate the agent's behavior by analyzing conversation history (inputs) and agent responses (outputs). Common criteria include issue resolution status and adherence to expected behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Trace-Based Judges

Trace-based judges analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. These judges can validate whether appropriate tools were called for a given user request. To create a trace-based judge, include `{{ trace }}` in the judge's instructions. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Integration with Evaluation Frameworks

### MLflow GenAI

MLflow GenAI provides the `mlflow.genai.evaluate()` API for running LLM-as-a-Judge evaluations. This function accepts:
- `data` – The evaluation dataset
- `predict_fn` – The function generating responses from the target system
- `scorers` – A list of judge configurations ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### DeepEval Integration

MLflow integrates with DeepEval, a comprehensive evaluation framework, to use DeepEval metrics as scorers. DeepEval provides specialized metrics for:
- [RAG](/concepts/retrieval-augmented-generation-rag.md) systems – Evaluating retrieval quality and answer generation
- Agents – Assessing task completion and tool usage
- Conversational AI – Evaluating multi-turn dialogue quality
- Safety – Evaluating the safety and responsibility of model outputs ^[deepeval-scorers-databricks-on-aws.md]

## Common Use Cases

### A/B Comparison

LLM-as-a-Judge evaluation enables [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) by running the same evaluation dataset against multiple agent configurations and comparing judge ratings. This approach allows teams to quantify the impact of changes—such as system prompt modifications, tool selection, or model choice—before promoting a configuration to production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Production Monitoring

Deploying the same judges used in offline evaluation to production scoring pipelines enables continuous monitoring of agent quality over time. This allows teams to track quality metrics alongside [MLflow](/concepts/mlflow.md) runs and detect regressions early. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- **Use consistent judges** – Deploying the same judges across both offline evaluation and production scoring ensures that differences in scores reflect changes in agent behavior rather than inconsistencies in the evaluation criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Align with human feedback** – As you gather expert annotations on agent outputs, fine-tune judges to better reflect human quality assessments. See Align judges with human feedback. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Control one variable at a time** – Change only the agent behavior being tested while keeping all other factors constant for valid comparisons. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Use representative datasets** – Test cases should reflect the range of real-world inputs the system will encounter in production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that evaluate agent quality
- make_judge()|Make Judge API – The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for continuous quality monitoring
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis
- DeepEval – Comprehensive evaluation framework for LLM applications
- Human Feedback Alignment – Improving judge accuracy with expert annotations
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Evaluating agent variants with consistent judges

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- deepeval-scorers-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
2. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
