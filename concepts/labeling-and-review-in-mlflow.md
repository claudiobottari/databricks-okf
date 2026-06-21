---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1444eec9b049f8585f9124725af0bc5414472b34b7d7e85c128c20c9693dca51
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-and-review-in-mlflow
    - Review in MLflow and Labeling
    - LARIM
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Labeling and Review in MLflow
description: The capability to view labeling sessions, inspect labeling schemas, and review feedback criteria such as ratings, comments, and expectations for GenAI agent traces.
tags:
  - mlflow
  - labeling
  - feedback
  - review
timestamp: "2026-06-19T10:43:51.867Z"
---

## Labeling and Review in MLflow

**Labeling and Review in MLflow** refers to the set of observability features—available through Genie Code for agent observability and evaluation—that allow developers to inspect human feedback on agent traces. These features enable teams to view labeling sessions, see who is assigned to review traces, and examine the labeling schema that defines the feedback criteria (such as ratings, comments, and expectations). ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Capabilities

Within an MLflow experiment, users can ask Genie Code natural-language questions about labeling and review. Genie Code provides read access to all labeling sessions, reviewer assignments, and schema definitions. For example, a user can ask “Which sessions have the lowest user feedback scores, and what went wrong in those conversations?” to quickly surface problematic interactions. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

The labeling schema specifies the criteria used by human reviewers, including:

- **Ratings** – Numeric or categorical scores.
- **Comments** – Free-text explanations.
- **Expectations** – Desired behavior or correctness benchmarks. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Using Genie Code for Labeling and Review

Genie Code provides a natural language interface to explore observability and evaluation data without writing queries or navigating multiple UI pages. To access labeling and review information, a user clicks the Genie Code icon in the top-right of the MLflow experiment page and asks questions such as: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- “View labeling sessions and who’s assigned to review traces.”
- “Inspect labeling schemas to understand feedback criteria.”

### Requirements

To use Genie Code (including its labeling and review features), the workspace must have partner-powered AI features enabled for both the account and the workspace, and be in a supported region. See Geo availability of Genie Code features for details. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Related Concepts

- Genie Code for agent observability and evaluation
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md)
- Trace Analysis
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)

### Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
