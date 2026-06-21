---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58bfa0695558ce0dee19b66565e78b5f97755594ba815028e6ca49c2c69e44ad
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-user-collaboration-on-databricks
    - MCOD
    - Notebook collaboration and commenting
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Multi-User Collaboration on Databricks
description: Best practices for sharing code and notebooks on Databricks, including using /Workspace/Shared for shared artifacts and Git folders with remote repos for active development.
tags:
  - collaboration
  - git
  - databricks-workspace
timestamp: "2026-06-19T18:45:14.514Z"
---

# Multi-User Collaboration on Databricks

**Multi-User Collaboration on Databricks** refers to the practices and tools that enable multiple team members to work simultaneously on notebooks, code, and experiments in a shared Databricks environment. The platform supports several collaboration patterns that help teams manage access, version control, and communication around their work.

## Overview

When multiple users need to work on the same project, they must coordinate how they share code, track changes, and provide feedback. Databricks offers three primary collaboration mechanisms: a folder-based strategy for shared code, Git-based version control for active development, and built-in notebook commenting and sharing features. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Storing Shared Code

To ensure all team members can access common code — for example, helper modules, environment YAML files, or configuration scripts — it is recommended to store such files in `/Workspace/Shared` rather than in user-specific folders like `/Workspace/Users/<your_email>/`. This location is accessible to every workspace user with the appropriate permissions, eliminating the need to copy or synchronize shared resources across personal directories. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Git-Based Collaboration for Active Development

For code that is under active development and still evolving, using Git folders in user-specific folders (e.g., `/Workspace/Users/<your_email>/`) and pushing changes to a remote Git repository is the recommended approach. This pattern allows each contributor to maintain their own clone and feature branches while still benefiting from a central remote repository for version control, code review, and history tracking. See the Git integration on Databricks best practices for more details. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Notebook Sharing and Commenting

Databricks notebooks support built-in collaboration features: team members can share notebooks with one another and leave comments directly on notebook cells. This enables conversational feedback, code review, and discussion without leaving the notebook interface. For full details, see the documentation on sharing and commenting on notebooks. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- Databricks notebooks – The primary authoring environment for collaborative work.
- Git integration on Databricks – Using repos and remote Git providers for version control.
- Workspace folders – Managing user and shared folders in the Databricks workspace.
- Workspace permissions – Controlling access to notebooks and folders.
- [MLflow experiments](/concepts/mlflow-experiment.md) – Experiment tracking that can be shared and viewed by collaborators.

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
