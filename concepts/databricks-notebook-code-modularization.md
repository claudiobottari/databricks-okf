---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3edc376c03f93933c1b1e82254e423af759dc20aad1e5abe3743ca1c18c36cfc
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-notebook-code-modularization
    - DNCM
    - Notebook Modularization
    - code modularization
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: Databricks notebook code modularization
description: The practice of organizing reusable code across notebooks using %run and workspace files to encapsulate functions and logic.
tags:
  - databricks
  - code-modularization
  - best-practices
timestamp: "2026-06-19T19:52:45.822Z"
---

# Databricks Notebook Code Modularization

**Databricks notebook code modularization** refers to the set of techniques and tools available on the Databricks platform for organizing, reusing, and orchestrating code across multiple notebooks. Proper modularization improves code maintainability, enables complex workflow construction, and supports parameterized pipeline execution. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Overview

Databricks provides several methods for modularizing notebook code, each suited to different use cases. The primary approaches are `%run`, `dbutils.notebook.run()`, workspace files, and [Lakeflow Jobs](/concepts/lakeflow-jobs.md). The choice of method depends on requirements for scheduling, parameter passing, version control, and whether the called code should execute inline or as a separate job. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## `%run` Command

The `%run` command allows you to include another notebook within a notebook. When you use `%run`, the called notebook is immediately executed inline, and the functions and variables defined in it become available in the calling notebook. This makes `%run` suitable for modularizing code by placing supporting functions in a separate notebook or concatenating notebooks that implement sequential analysis steps. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Usage

`%run` must be placed in a cell by itself, as it runs the entire notebook inline. Paths can be relative or absolute:

- Relative path: `%run ./shared-code-notebook`
- Subdirectory: `%run ./dir/notebook`
- Absolute path: `%run /Users/username@organization.com/directory/notebook`

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Limitations

- `%run` cannot be used to run a Python file and import entities defined in that file into a notebook. To import from a Python file, use workspace files or package the file into a Python library and install it on the cluster. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- When using `%run` to run a notebook containing widgets, the notebook runs with the widget's default values unless you explicitly pass values. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## `dbutils.notebook.run()` API

The `dbutils.notebook` API complements `%run` by allowing parameter passing and return value retrieval. Unlike `%run`, `dbutils.notebook.run()` starts a new ephemeral job to run the notebook, enabling complex workflows with dependencies, conditional logic, and concurrent execution. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Method Signature

```python
dbutils.notebook.run(path: String, timeout_seconds: int, arguments: Map): String
```

- `path`: The path to the notebook to run.
- `timeout_seconds`: Controls the timeout of the run (0 means no timeout). The call throws an exception if it doesn't finish within the specified time. If Databricks is down for more than 10 minutes, the notebook run fails regardless of `timeout_seconds`. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- `arguments`: A map of key-value pairs that set widget values in the target notebook. For example, if the target notebook has a widget named `A`, passing `("A": "B")` makes retrieving widget `A` return `"B"`. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Limitations

- The `arguments` parameter accepts only Latin characters (ASCII character set). Using non-ASCII characters returns an error. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Jobs created using the `dbutils.notebook` API must complete in 30 days or less. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Both parameters and return values must be strings. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Passing Structured Data Between Notebooks

Since `dbutils.notebook.exit()` can only return a single string, structured data must be passed through alternative mechanisms:

- **Temporary views**: The callee notebook can create a global temporary view and return its name. The caller can then query the view. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- **DBFS**: For larger datasets, the callee can write results to DBFS and return the path. The caller reads from that path. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- **JSON serialization**: To return multiple values, use standard JSON libraries to serialize and deserialize results. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Error Handling

Errors from `dbutils.notebook.run()` throw a `WorkflowException`. You can implement retry logic to handle transient failures: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

```python
def run_with_retry(notebook, timeout, args = {}, max_retries = 3):
  num_retries = 0
  while True:
    try:
      return dbutils.notebook.run(notebook, timeout, args)
    except Exception as e:
      if num_retries > max_retries:
        raise e
      else:
        print("Retrying error", e)
        num_retries += 1
```

### Running Multiple Notebooks Concurrently

You can run multiple notebooks simultaneously using standard Python or Scala concurrency constructs such as threads or futures. This enables parallel execution of independent pipeline steps. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Comparison: `%run` vs. `dbutils.notebook.run()`

| Feature | `%run` | `dbutils.notebook.run()` |
|---|---|---|
| Execution model | Inline, same JVM | Separate ephemeral job |
| Parameter passing | Via widget defaults | Via `arguments` map |
| Return values | Not supported | Supported via `dbutils.notebook.exit()` |
| Concurrent execution | Not supported | Supported via threads/futures |
| Conditional workflows | Not supported | Supported via return values |
| Language support | All notebook languages | Python and Scala (can invoke R notebooks) |

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Related Concepts

- Databricks widgets — Used for parameterizing notebooks and passing values with `%run` and `dbutils.notebook.run()`
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Orchestration tool for scheduling and managing notebook workflows
- Workspace files — Alternative for modularizing code using Python files and Git integration
- Databricks libraries — Packaging code into reusable libraries for cluster installation
- dbutils utilities — The broader set of Databricks utility APIs

## Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
