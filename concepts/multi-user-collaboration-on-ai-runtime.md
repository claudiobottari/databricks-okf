---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d807f304d0266a01bba46f4e567e56d19eb7457db1301db0659f94a4e2fa4a9
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-user-collaboration-on-ai-runtime
    - MCOAR
    - multi-user-collaboration-on-databricks-ai-runtime
    - MCODAR
    - multi-user-collaboration-on-databricks
    - MCOD
    - Notebook collaboration and commenting
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Multi-User Collaboration on AI Runtime
description: Best practices for sharing code, using Git folders, and collaborating on notebooks in Databricks AI Runtime.
tags:
  - collaboration
  - git
  - databricks
  - best-practices
timestamp: "2026-06-18T12:15:47.056Z"
---

Here is the wiki page for "Multi-User Collaboration on AI Runtime".

---

# Multi-User Collaboration on AI Runtime

**Multi-User Collaboration on AI Runtime** refers to the practices and workflows that enable multiple data scientists and engineers to work concurrently on a single [AI Runtime](/concepts/ai-runtime.md) project without interfering with each other's code, data, or experiments. Effective collaboration requires careful management of shared resources—such as code files, environments, and datasets—as well as leveraging [MLflow](/concepts/mlflow.md) for experiment tracking and Git for version control.

## Shared Code Storage

To ensure all collaborators can access shared code, AI Runtime follows a standard Databricks workspace structure where permissions on workspace files determine visibility.

- **Use `/Workspace/Shared` for shared artifacts.** Store helper modules, environment YAML files, configuration files, and common libraries in `/Workspace/Shared` rather than in user-specific folders (e.g., `/Workspace/Users/<your_email>/`). This ensures all team members can read and execute the code without needing to copy or duplicate it. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Avoid storing shared code in user-specific folders.** Code placed in a user-specific folder is private to that user by default, which prevents other collaborators from accessing or executing it unless permissions are explicitly changed. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Version Control with Git

For code under active development, collaborative teams should use Git repositories within Databricks to manage versions, branches, and contributions.

- **Use Git folders in user-specific folders.** Each team member can clone the same remote repository into their own `/Workspace/Users/<your_email>/` space. This allows each person to work on their own branch without affecting others. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Push changes to a remote Git repo.** After making changes on a local branch, contributors push their work to the shared remote repository for review and merging. This provides a complete version history and enables standard Git workflows like pull requests and code review. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Follow best practices for Databricks Git integration.** See Best practices for using Git on Databricks for guidance on branching strategies, CI/CD pipelines, and managing large files. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Notebook Collaboration

Databricks notebooks include built-in collaboration features that AI Runtime users can leverage.

- **Share and comment on notebooks.** Collaborators can share notebooks with each other and add comments directly in the notebook interface. This is useful for code review, providing feedback on analysis, or documenting observations. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Avoid simultaneous edits on the same notebook.** Databricks notebooks do not support real-time collaborative editing like Google Docs. When multiple users need to edit the same notebook, use Git branches to manage changes and merge them via pull requests. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Experiment Tracking and Sharing

[MLflow](/concepts/mlflow.md) is the primary mechanism for sharing and comparing experimental results across users.

- **Use absolute experiment paths.** When setting the `MLFLOW_EXPERIMENT_NAME` environment variable, always use an absolute path (e.g., `/Users/<username>/my-experiment`) to avoid ambiguity when multiple users are running experiments with similar names. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Share experiments.** An MLflow experiment created by one user can be shared with other collaborators by granting them read or edit permissions on the experiment's path in the workspace. This allows the team to view, compare, and analyze all runs from a unified interface. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Customize run names for clarity.** When running experiments, use descriptive `run_name` parameters in `mlflow.start_run(run_name="your-custom-name")` so collaborators can quickly identify the purpose of each run in the experiment list. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Data and Model Checkpointing

Collaboration on data pipelines and model training requires careful management of shared model checkpoints.

- **Use Unity Catalog volumes for shared checkpoints.** Distribute model checkpoints and training data through Unity Catalog volumes, which provide unified governance. All collaborators with appropriate permissions on the volume can read and write checkpoints. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Be aware of data pipeline state in checkpoints.** Model checkpoints capture model and optimizer state, but do not capture the exact position within a training dataset. When resuming training from a checkpoint, account for this by restarting from an epoch boundary or tracking processed samples in your own training state. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Monitoring and Observability

Collaborators can monitor GPU resources on AI Runtime using the **GPU resources** pane. This pane shows utilization, memory, and temperature metrics for each GPU. The pane polls metrics every 10 seconds and retains up to 2 hours of history. When a user is not actively viewing the pane, it pauses after 5 minutes of inactivity; reopening it resumes monitoring. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment for single-node and multi-GPU tasks
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management
- Git on Databricks — Version control integration for collaborative development
- Unity Catalog Volumes — Shared storage for checkpoints and data
- [Notebook collaboration and commenting](/concepts/multi-user-collaboration-on-ai-runtime.md) — Databricks' built-in sharing features for notebooks
- [GPU resources pane](/concepts/gpu-resources-monitoring-pane.md) — Real-time monitoring of GPU metrics

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
