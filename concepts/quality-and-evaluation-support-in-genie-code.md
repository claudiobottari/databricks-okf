---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 941e8fa02539283b472439d62e530adf39b4c52aee26692ae1ccca72c020201b
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - quality-and-evaluation-support-in-genie-code
    - Evaluation Support in Genie Code and Quality
    - QAESIGC
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Quality and Evaluation Support in Genie Code
description: Genie Code capability to review assessment scores from human feedback, LLM judges, and programmatic checks, inspect evaluation datasets and registered scorers, and get help setting up mlflow.genai.evaluate().
tags:
  - evaluation
  - quality
  - genai
  - mlflow
timestamp: "2026-06-18T12:29:06.806Z"
---

# Quality and Evaluation Support in Genie Code

**Quality and Evaluation Support** describes how [Genie Code](/concepts/genie-code.md) helps developers understand, debug, and improve the quality of GenAI agent outputs through a natural language interface within [MLflow](/concepts/mlflow.md). Genie Code provides read access to everything in an experiment, including evaluation runs, scorers, labeling sessions, and datasets — enabling conversational exploration of quality metrics and evaluation workflows without writing queries or navigating multiple UI pages. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities

Genie Code offers several capabilities specifically related to quality and evaluation: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Review assessment scores** from human feedback, [LLM Judges](/concepts/llm-judges.md), and programmatic checks.
- **Inspect evaluation datasets** used in evaluation runs.
- **Check registered scorers** and their configurations.
- **Get help setting up `mlflow.genai.evaluate()`** with the right scorers for your agent.
- **View labeling sessions** and who is assigned to review traces, and inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations.

These capabilities allow you to assess agent quality without writing code or switching between tools. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Example Questions

You can ask Genie Code questions like the following to drive quality and evaluation tasks: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- “Which sessions have the lowest user feedback scores, and what went wrong in those conversations?”
- “What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?”
- “Help me set up evaluation for my RAG agent with the right scorers.”

These examples show how Genie Code helps you identify quality issues and take action to improve your agent. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [Genie Code](/concepts/genie-code.md) — The natural language interface for agent observability and evaluation
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [LLM Judges](/concepts/llm-judges.md) — Scorers used in evaluation to assess agent outputs
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Labeling and review workflows for quality assessment
- Trace Analysis — Root cause analysis of agent behavior
- [Agent Observability](/concepts/genai-agent-observability.md) — The broader practice of monitoring and debugging GenAI agents

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
