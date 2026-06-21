---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea4f35025c9f3b7254ce93153375b1661084071bb6db694e9a15193d33d0adcb
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ai-governance
    - UCFAG
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: Unity Catalog for AI Governance
description: Fine-grained access control, security policies, and governance for all data and AI assets across the Databricks platform.
tags:
  - governance
  - security
  - databricks
timestamp: "2026-06-19T19:06:57.376Z"
---

## Unity Catalog for AI Governance

**Unity Catalog for AI Governance** refers to the use of [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ unified governance solution – to manage and secure artificial intelligence assets alongside traditional data assets. Within the Databricks platform, Unity Catalog enables administrators to apply fine‑grained access control, security policies, and governance across all data and AI resources, including models, features, experiments, and pipelines. This capability is a core part of the platform’s support for MLOps and DevOps for machine learning, ensuring that AI development and deployment adhere to the same governance standards as enterprise data. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Role in AI Governance

The governance of AI assets is critical for maintaining trust, compliance, and reproducibility in machine learning workflows. By integrating Unity Catalog into the CI/CD lifecycle, teams can enforce policies on who can access training data, who can deploy models, and how model artifacts are versioned and tracked. This reduces the risk of data leakage, unauthorized model changes, or regulatory non‑compliance. Unity Catalog provides a single control plane for setting permissions and auditing usage, which is especially important when multiple teams collaborate on shared AI initiatives. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Relationship to DataOps and ModelOps

Unity Catalog sits at the intersection of DataOps and ModelOps. For DataOps, it governs access to input data pipelines and training datasets. For ModelOps, it governs the model registry, serving endpoints, and experiment metadata. This unified governance layer allows organizations to trace lineage from raw data through to production predictions, supporting both security and auditability. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [AI Governance](/concepts/ai-governance.md)
- Data Governance
- Access Control
- MLOps
- DataOps
- ModelOps
- Databricks
- Fine-Grained Permissions
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)

### Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
