---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c60da489dfd3cce6772180a460be9c18ec8925130bdc8bd41a0fdbf91d7b2e1
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judge-model-infrastructure-and-privacy
    - Privacy and LLM Judge Model Infrastructure
    - LJMIAP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: LLM Judge Model Infrastructure and Privacy
description: LLM judges for guidelines evaluation use specially-tuned models hosted by region (EU or US), support custom model selection via LiteLLM-compatible providers, and have privacy controls including opt-out of Abuse Monitoring and partner-powered AI feature disabling.
tags:
  - llm-evaluation
  - privacy
  - infrastructure
  - databricks
timestamp: "2026-06-19T14:29:57.819Z"
---

# LLM Judge Model Infrastructure and Privacy

**LLM Judge Model Infrastructure and Privacy** covers the architecture, hosting regions, third‑party dependencies, and data‑handling practices behind the [LLM judge](/concepts/llm-judges.md) models used by MLflow Guidelines judges and other built‑in evaluators. Understanding these details helps teams evaluate GenAI applications while meeting compliance and privacy requirements.

## Model Hosting and Third‑Party Services

LLM judges may use third‑party services to evaluate GenAI applications, including Azure OpenAI operated by Microsoft. Databricks has opted out of Abuse Monitoring for Azure OpenAI, so no prompts or responses are stored with Azure OpenAI. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

For workspaces in the European Union (EU), LLM judges use models hosted in the EU. All other regions use models hosted in the United States. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Controlling Model Access

If you disable [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md), the LLM judge is prevented from calling partner‑powered models. You can still use LLM judges by providing your own model. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Choosing a Custom Judge Model

When creating a custom judge (either via `Guidelines()` or `make_judge()`), you can change the model that powers the judge using the `model` argument. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM‑compatible model provider. If you use `databricks` as the provider, the model name is the same as the serving endpoint name. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Data Usage and Training Prohibition

LLM judges are intended to help customers evaluate their GenAI agents and applications. **LLM judge outputs must not be used to train, improve, or fine‑tune an LLM.** ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Judge Model Characteristics

The judge models underlying guidelines judges are specially‑tuned LLMs that receive a context dictionary (containing `request`, `response`, and optional custom keys) and natural‑language rules, then return a binary pass/fail score with a detailed rationale. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- MLflow Guidelines Judges – The `Guidelines()` and `ExpectationsGuidelines()` scorers
- [Custom LLM Judge](/concepts/custom-llm-judge.md) – Building judges with `make_judge()`
- [GenAI Evaluation on Databricks](/concepts/genai-app-evaluation-workflow-on-databricks.md) – Overview of offline evaluation and production monitoring
- [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) – Toggle that controls third‑party model access
- Azure OpenAI – Third‑party LLM provider used by judges

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
