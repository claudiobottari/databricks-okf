---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f732d0ead5c927270ac4a037c4210aeea4b9d21c735772c21afd95cdbb51b74
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - functions-and-registered-models
    - Registered Models and Functions
    - FARM
    - Registered model
    - Registered models
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Functions and Registered Models
description: Functions in Unity Catalog represent reusable executable logic including UDFs, stored procedures, and registered MLflow models, with models having additional privileges for version management and tagging.
tags:
  - unity-catalog
  - functions
  - machine-learning
timestamp: "2026-06-19T23:15:39.176Z"
---

# Functions and Registered Models

**Functions** are securable objects in [Unity Catalog](/concepts/unity-catalog.md) that represent reusable, executable logic. They are stored within a Schema and include user-defined functions (UDFs), stored procedures, and registered models. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Types of Functions

### User-Defined Functions (UDFs)

User-defined functions are custom functions written in SQL or Python that can be called in SQL queries and notebooks. They allow users to extend the built-in capabilities of the query engine with custom logic. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Stored Procedures

Stored procedures are user-defined routines that execute a sequence of SQL statements. Unlike UDFs, stored procedures may include side effects such as inserting or updating data. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Registered Models

Registered models are [MLflow](/concepts/mlflow.md) machine learning models registered in [Unity Catalog](/concepts/unity-catalog.md). In [Unity Catalog](/concepts/unity-catalog.md), registered models are implemented as a type of function object. The model itself serves as a container, while the artifacts and metadata for each training run are stored as **model versions** within it. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Permissions Model

The permissions model for registered models is the same as that of functions. However, the following additional privileges apply specifically to models: ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

- **`APPLY TAG`**: Allows adding and editing tags on a model and its versions. The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema.
- **`CREATE MODEL VERSION`**: Allows a user to register new versions of a model without granting the ability to execute, modify, or add tags to the model. The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema.

Creating a model requires the `CREATE MODEL` privilege on the schema, not `CREATE FUNCTION`. The `CREATE MODEL` privilege can also be granted on a catalog to allow creating models in any schema within that catalog. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Object Hierarchy

Functions (including registered models) exist within the [Three-Level Namespace](/concepts/three-level-namespace.md) of [Unity Catalog](/concepts/unity-catalog.md): `catalog.schema.function`. They are contained within schemas, which are contained within catalogs, which exist under the [Metastore](/concepts/metastore.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform that manages securable objects
- Schema — The container object that holds functions and registered models
- [MLflow](/concepts/mlflow.md) — The framework used to package and register models
- [Metastore](/concepts/metastore.md) — The top-level securable object in [Unity Catalog](/concepts/unity-catalog.md)
- User-Defined Functions (UDFs) — Custom functions written in SQL or Python
- Model Lifecycle Management — Managing model versions and deployment in [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
