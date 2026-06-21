---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10485d99a15838fabf0e99949f2b40872501d38ef8759b17c9d514ccc0dad2bf
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-user-collaboration-on-databricks-ai-runtime
    - MCODAR
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Multi-user Collaboration on Databricks AI Runtime
description: Best practices for sharing code via /Workspace/Shared, using Git folders for active development, and collaborating on notebooks for multi-user ML projects.
tags:
  - collaboration
  - workflow
  - databricks
timestamp: "2026-06-19T10:26:27.347Z"
---

# Multi-user Collaboration on Databricks AI Runtime

**Multi-user Collaboration on Databricks AI Runtime** refers to practices and features that enable multiple data scientists and engineers to work together on the same codebase and notebooks when using AI Runtime. Effective collaboration avoids conflicts, ensures shared access to dependencies, and leverages version control.

## Shared Code Storage

To make code available to all users — such as helper modules, environment YAML files, or configuration scripts — store them in `/Workspace/Shared` instead of user-specific folders like `/Workspace/Users/<your_email>/`. This ensures that every team member can access the same files without permission issues. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Version Control with Git

For code that is under active development, use Databricks Repos (Git folders) within user-specific folders (`/Workspace/Users/<your_email>/`). Each user can work on their own clone and branch of the repository, while pushing changes to a remote Git repo. This approach provides per-user isolation during development while maintaining a single source of truth through the remote repository. For further guidance, see the Databricks best practices for using Git on Databricks. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Notebook Collaboration

Collaborators can share and comment on notebooks directly in the Databricks workspace. This enables real-time feedback and discussion without leaving the notebook environment. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- Databricks Repos – Git integration for version-controlled notebook and code development.
- Workspace Shared Folder – The `/Workspace/Shared` location for team-wide artifacts.
- Notebook Collaboration – Sharing, commenting, and co-authoring notebooks on Databricks.
- [Experiment Tracking and Observability](/concepts/ai-runtime-experiment-tracking-and-observability.md) – MLflow integration, logging, and GPU monitoring in AI Runtime.
- Resource Limits – Global limits that affect collaborative workloads.

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
