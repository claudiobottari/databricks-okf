---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eaf83477bda4367addcd440857a07a701826f1324400ebe526a6551b1207cd7d
  pageDirectory: concepts
  sources:
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-based-metadata-in-unity-catalog
    - TMIUC
  citations:
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: Tag-based metadata in Unity Catalog
description: Tags for labeling models and model versions in Unity Catalog, supporting search in Catalog Explorer (up to 50 tags per object), replacing stage labels from the Workspace Model Registry.
tags:
  - metadata
  - unity-catalog
  - governance
timestamp: "2026-06-19T19:35:56.647Z"
---

# Tag-based metadata in Unity Catalog

**Tag-based metadata** in Unity Catalog refers to the ability to attach key-value tags to models and model versions stored in Unity Catalog. Tags provide a flexible labeling mechanism that replaces the fixed-stage system of the Workspace Model Registry, enabling users to categorize, search, and manage ML models with custom metadata. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Overview

In Unity Catalog, tags can be created on both the model object and on individual model versions. Unlike the Workspace Model Registry, which used four fixed stages (e.g., `Staging`, `Production`), Unity Catalog replaces stages with custom **aliases** and **tags**. Aliases are reassignable references (up to 10) used for calling a specific model version, while tags are arbitrary key-value labels that can be applied for any purpose — for example, labeling versions as `Production`, `Staging`, or `Archived`. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

Tags work alongside aliases to provide a more flexible model lifecycle management. While aliases are the recommended way to point to a particular version for deployment, tags can be used for broader organizational or operational labeling. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Usage

You can add tags to a model or model version through the Unity Catalog UI (Catalog Explorer) or via the API. The UI provides an **Add tags** button on the model version page. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

When migrating models from the Workspace Model Registry to Unity Catalog, stages can be mapped to tags. For a simple migration, each stage (e.g., `Production`) becomes a tag applied to the corresponding model version. This allows you to preserve your existing stage-based labeling scheme. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Searching by tags

In Catalog Explorer, you can search for models by tag by typing the tag key or value into the search box. However, this search functionality is limited to models only — it does not support searching for model versions by tag. Additionally, the MLflow client does not support searching for models by Unity Catalog tags. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Limitations

- Unity Catalog allows a maximum of **50 tags** per object (model or model version). ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]
- Tags can be used to search for models in Catalog Explorer, but not for model versions. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]
- The MLflow client API does not support searching models by tag. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance and catalog system that supports tag-based metadata.
- [MLflow](/concepts/mlflow.md) — The machine learning lifecycle tool used to manage models; note that its client does not currently support tag-based search.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI tool for browsing Unity Catalog assets, including tag-based search.
- [Aliases](/concepts/model-aliases.md) — A separate, reassignable label mechanism (up to 10 per model) used for calling model versions.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The predecessor system whose stages are replaced by tags and aliases in Unity Catalog.
- Model lifecycle management — The broader process of deploying, tracking, and promoting models, assisted by tags and aliases.

## Sources

- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
