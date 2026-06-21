---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa1ff98828df33803a49da71d2cd3b5024f242e03cb6f1e342a182e485281a68
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-and-review-with-genie-code
    - Review with Genie Code and Labeling
    - LARWGC
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Labeling and Review with Genie Code
description: Genie Code capability to view labeling sessions, see who is assigned to review traces, and inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations.
tags:
  - labeling
  - review
  - feedback
  - observability
timestamp: "2026-06-18T12:29:18.213Z"
---

#Labeling and Review with Genie Code

**Labeling and Review with Genie Code** refers to the ability to use the [Genie Code](/concepts/genie-code.md) natural-language interface within [MLflow](/concepts/mlflow.md) to inspect and manage human feedback and human-in-the-loop review of [GenAI](/concepts/mlflow-genai-evaluate-api.md) agent traces. Genie Code can surface labeling sessions, reviewer assignments, and the schemas that define feedback criteria — all through conversational queries instead of navigating multiple UI pages or writing custom queries. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

Genie Code is a conversational assistant that has read access to everything in an MLflow experiment, including traces, datasets, evaluation runs, scorers, and labeling sessions. For labeling and review workflows, Genie Code can answer questions about who is assigned to review which traces, what feedback criteria are being collected (such as ratings, comments, and expectations), and how labeling sessions are structured. This allows teams to track the progress and results of human review without manually opening the labeling UI. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities

- **View labeling sessions** – Ask Genie Code about active or completed labeling sessions in the experiment, including who is assigned to review specific traces. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Inspect labeling schemas** – Request details of the feedback criteria defined in a labeling schema (e.g., ratings, comments, expectations) to understand exactly what evaluators are being asked to assess. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Explore reviewer assignments** – Determine which reviewers are assigned to which traces or sessions, helping to balance workload and track coverage. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Example Questions

Genie Code can answer questions such as:

- "Which sessions have the lowest user feedback scores, and what went wrong in those conversations?"
- "Show me the labeling schema for this experiment — what rating scale and comment fields are being collected?"
- "Who is assigned to review the traces from the last evaluation run?"

^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Requirements

To use Genie Code for labeling and review, your workspace must have:

- Partner-powered AI features enabled for both the account and workspace (see [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md)).
- The workspace in a supported region; Genie Code is a Designated Service that uses Geos for data residency (see Geo availability of Genie Code features).

^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [Genie Code](/concepts/genie-code.md) – The general conversational interface for agent observability and evaluation
- MLflow Labeling – The broader human-in-the-loop labeling framework in MLflow
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) – Mechanisms for collecting ratings, comments, and expectations
- [Trace Analysis and Debugging with Genie Code](/concepts/trace-analysis-and-debugging-with-genie-code.md) – Related capability for investigating trace issues
- [Evaluation with LLM Judges](/concepts/mlflow-genai-evaluation-with-llm-as-judge.md) – Programmatic scoring that complements human labeling

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
