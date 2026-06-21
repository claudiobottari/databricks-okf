---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7135f042cd40b3d2cce8033b4e6edbb5073df07fc9c5fa4a45285f8856064929
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - concurrent-notebook-execution-in-databricks
    - CNEID
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: Concurrent notebook execution in Databricks
description: Running multiple notebooks in parallel using Python or Scala threading/futures constructs alongside dbutils.notebook.run().
tags:
  - databricks
  - concurrency
  - orchestration
timestamp: "2026-06-19T19:53:17.405Z"
---

# Concurrent Notebook Execution in Databricks

**Concurrent notebook execution in Databricks** refers to the ability to run multiple notebooks simultaneously within a single workflow or pipeline. This technique enables parallel processing of independent tasks, reducing overall execution time and improving resource utilization.

## Overview

Databricks supports concurrent notebook execution through standard programming language constructs for parallelism. By running multiple notebooks in parallel, you can build more efficient workflows where independent tasks execute simultaneously rather than sequentially. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Implementation with Threads and Futures

Concurrent notebook execution is achieved using standard Scala and Python concurrency mechanisms:

- **Scala**: Threads or Futures
- **Python**: Threading or Multiprocessing

These constructs allow you to launch multiple `dbutils.notebook.run()` calls in parallel, each executing a separate notebook as an independent job. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## `dbutils.notebook.run()` for Parallel Execution

The `dbutils.notebook.run()` method is the primary tool for concurrent execution. Unlike `%run`, which executes inline and blocks until completion, `dbutils.notebook.run()` starts a new job for each call. This design enables parallel execution when multiple calls are launched concurrently. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Key Characteristics

- Each call to `dbutils.notebook.run()` creates an ephemeral job that runs immediately ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Parameters are passed as key-value pairs with string values ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Returns a string exit value from the called notebook ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- The `timeout_seconds` parameter controls the maximum execution time (0 means no timeout) ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Example Workflow

A typical concurrent execution pattern involves:

1. Downloading multiple notebook files into a single workspace folder
2. Using a **Run concurrently** notebook as the orchestrator
3. The orchestrator notebook launches parallel executions using threading or futures
4. Each parallel execution runs a target notebook independently
5. Results are collected after all parallel executions complete

Detailed example notebooks are available from Databricks demonstrate this pattern using Scala constructs. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Error Handling

When running notebooks concurrently, you should implement error handling to manage failures in individual notebook executions. Errors throw a `WorkflowException`, which can be caught and handled with retry logic. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

```python
def run_with_retry(notebook, timeout, args={}, max_retries=3):
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

## Best Practices

- Use concurrent execution for **independent tasks** that do not share state or dependencies
- Consider resource limits when launching many parallel jobs
- Implement proper error handling and retry logic for each parallel execution
- Use temporary views or DBFS to pass structured data back from parallel notebooks ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Limitations

- Jobs created using `dbutils.notebook.run()` must complete within **30 days** or less ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- If Databricks is down for more than 10 minutes, notebook runs fail regardless of timeout settings ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Parameters accept only Latin characters (ASCII character set) ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- The `dbutils.notebook` API is available only in Python and Scala (but can invoke R notebooks) ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Comparison with `%run`

| Feature | `%run` | `dbutils.notebook.run()` |
|---------|--------|--------------------------|
| Execution mode | Inline, blocking | New job, non-blocking |
| Parameter passing | Widget values only | Key-value map |
| Return values | None | String exit value |
| Concurrent execution | No | Yes (with threading) |

^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Related Concepts

- Notebook orchestration — Coordinating multi-step notebook workflows
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — Scheduled and triggered notebook execution
- dbutils.notebook — API for programmatic notebook execution
- Parallel computing in Databricks — Broader parallel execution strategies
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Managed workflow orchestration service

## Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
