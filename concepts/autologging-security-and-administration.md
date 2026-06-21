---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 077a782e827c015b068a0267f64ac8a74dde998f64fc21c906446249ef43a075
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-security-and-administration
    - Administration and Autologging Security
    - ASAA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Autologging Security and Administration
description: Security via MLflow Experiment permissions and workspace-level admin controls to enable or disable Databricks Autologging for all interactive notebooks
tags:
  - databricks
  - security
  - administration
  - mlflow
timestamp: "2026-06-19T09:45:59.507Z"
---

```markdown
---
title: Autologging Security and Administration
summary: Security and administrative controls for Databricks Autologging, including MLflow Experiment permissions for access control, workspace-level enable/disable via admin settings, and user-level disable options.
sources:
  - databricks-autologging-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:33:00.634Z"
updatedAt: "2026-06-18T11:33:00.634Z"
tags:
  - mlflow
  - security
  - administration
  - databricks
aliases:
  - autologging-security-and-administration
  - Administration and Autologging Security
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Autologging Security and Administration

**Autologging Security and Administration** covers the security model, data management practices, and administrative controls for [[Databricks Autologging]]. This feature automatically captures model parameters, metrics, files, and lineage information when training models from popular machine learning libraries, recording training sessions as [[MLflow Tracking]] runs.^[databricks-autologging-databricks-on-aws.md]

## Security and Data Management

All model training information tracked with Databricks Autologging is stored in MLflow Tracking and is secured by [[MLflow Experiment Permission Levels for Apps|MLflow Experiment permissions]]. Users can share, modify, or delete model training information using the [[MLflow Tracking]] API or UI.^[databricks-autologging-databricks-on-aws.md]

### Access Control

Autologged runs are subject to the same experiment-level access control as other MLflow runs. Permissions can be managed through Unity Catalog or workspace-level settings. See [[MLflow Experiment Permission Levels for Apps|MLflow Experiment permissions]] for detailed configuration options.^[databricks-autologging-databricks-on-aws.md]

## Administration

Administrators can enable or disable Databricks Autologging for all interactive notebook sessions across their workspace from the **Advanced** tab of the admin settings page. Changes do not take effect until the cluster is restarted.^[databricks-autologging-databricks-on-aws.md]

### Workspace-Level Controls

- **Enable / Disable:** Use the admin settings page to toggle autologging for the entire workspace.^[databricks-autologging-databricks-on-aws.md]
- **Cluster Restart Required:** After changing the admin setting, clusters must be restarted before the change takes effect.^[databricks-autologging-databricks-on-aws.md]

### User-Level Controls

Users can also disable Databricks Autologging in individual notebooks by calling `mlflow.autolog(disable=True)`. This setting applies to the current notebook session only and does not override workspace-level controls.^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(disable=True)
```

## Disabling Autologging

### For Specific Frameworks

Administrators or users can disable autologging for a specific framework integration, such as OpenAI or LangChain, by calling the appropriate autolog function with `disable=True`. For example:^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
import mlflow.openai
mlflow.openai.autolog(disable=True)
```

### For All Frameworks

To disable all autologging in a notebook, call `mlflow.autolog(disable=True)`. Alternatively, use the workspace admin settings for all notebooks.

## Related Concepts

- [[MLflow Tracking]] – The underlying system where autologged data is stored
- [[MLflow Experiment Permission Levels for Apps|MLflow Experiment permissions]] – Access control for autologged experiments
- [[Databricks Autologging]] – The main feature page
- Access Control – Workspace and experiment-level security

## Sources

- databricks-autologging-databricks-on-aws.md
```

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
