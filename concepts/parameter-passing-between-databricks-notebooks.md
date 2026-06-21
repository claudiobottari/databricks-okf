---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8909a4a52be507a0519f7bedeb01bc504d8d870447ffc47404c745d2fe9340c5
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parameter-passing-between-databricks-notebooks
    - PPBDN
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: Parameter passing between Databricks notebooks
description: Techniques for passing string parameters and structured data (via temporary views, DBFS, or JSON) between notebooks using dbutils.notebook.run() and widgets.
tags:
  - databricks
  - notebook-orchestration
  - data-pipeline
timestamp: "2026-06-19T19:53:31.960Z"
---

# Parameter Passing Between Databricks Notebooks

**Parameter passing between Databricks notebooks** refers to the mechanisms for passing arguments into and receiving return values from Databricks notebooks when they are called programmatically. The primary API for this functionality is `dbutils.notebook.run()`, which enables complex workflow orchestration with dependencies, conditional logic, and data sharing between notebooks.

## Overview

Databricks provides two main methods for notebook orchestration: `%run` and `dbutils.notebook.run()`. While `%run` executes a notebook inline and makes its functions and variables available in the calling notebook, `dbutils.notebook.run()` starts a new ephemeral job and supports parameter passing and return values. This makes `dbutils.notebook.run()` the appropriate choice for building workflows that require passing data between notebooks. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

`dbutils.notebook.run()` is available only in Python and Scala, but it can invoke notebooks written in any language supported by Databricks, including R. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## The `dbutils.notebook.run()` API

The `dbutils.notebook.run()` method accepts three parameters: the path to the target notebook, a timeout in seconds, and a map of arguments. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

```python
dbutils.notebook.run("notebook-name", 60, {"argument": "data", "argument2": "data2"})
```

### Parameter Rules

- Both the arguments passed to `run()` and the return value from `dbutils.notebook.exit()` must be strings. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- The `arguments` parameter accepts only Latin characters (ASCII character set); non-ASCII characters return an error. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- Jobs created using the `dbutils.notebook` API must complete within 30 days or less. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Widget Integration

The `arguments` parameter sets widget values in the target notebook. If the target notebook has a widget named `A` and you pass `("A": "B")` as an argument, retrieving the value of widget `A` will return `"B"`. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Returning Data from Notebooks

The `dbutils.notebook.exit()` method is used to return a string value from a called notebook back to the calling notebook. Since only a single string can be returned, there are several strategies for returning structured data: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

### Returning a Reference to a Temporary View

The called notebook stores data in a global temporary view and returns the view name. The calling notebook then accesses the data through that view: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

```python
# In callee notebook
spark.range(5).toDF("value").createOrReplaceGlobalTempView("my_data")
dbutils.notebook.exit("my_data")

# In caller notebook
returned_table = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)
global_temp_db = spark.conf.get("spark.sql.globalTempDatabase")
display(table(global_temp_db + "." + returned_table))
```

### Returning a DBFS Path

For larger datasets, the called notebook writes results to DBFS and returns the path: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

```python
# In callee notebook
dbutils.fs.rm("/tmp/results/my_data", recurse=True)
spark.range(5).toDF("value").write.format("parquet").save("dbfs:/tmp/results/my_data")
dbutils.notebook.exit("dbfs:/tmp/results/my_data")

# In caller notebook
returned_table = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)
display(spark.read.format("parquet").load(returned_table))
```

### Returning JSON Data

To return multiple values, use standard JSON libraries to serialize and deserialize: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

```python
# In callee notebook
import json
dbutils.notebook.exit(json.dumps({
  "status": "OK",
  "table": "my_data"
}))

# In caller notebook
import json
result = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)
print(json.loads(result))
```

## Timeout and Error Handling

The `timeout_seconds` parameter controls how long the calling notebook waits for the called notebook to complete. A value of 0 means no timeout. The call throws an exception if the notebook does not finish within the specified time. If Databricks is down for more than 10 minutes, the notebook run fails regardless of `timeout_seconds`. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

Errors throw a `WorkflowException`, which can be caught and handled with retry logic: ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

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

## Comparison with `%run`

The `%run` command executes the called notebook inline within the same JVM, making its functions and variables available in the calling notebook. However, `%run` does not support parameter passing or return values. Use `%run` when you want to share code and functions between notebooks, and use `dbutils.notebook.run()` when you need parameter passing, return values, or workflow orchestration with dependencies. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

When you use `%run` with a notebook containing widgets, the called notebook runs with the widget's default values unless you explicitly pass values. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Running Multiple Notebooks Concurrently

Standard Scala and Python concurrency constructs, such as Threads and Futures, can be used to run multiple notebooks concurrently using `dbutils.notebook.run()`. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Related Concepts

- Databricks Notebooks — The core execution environment for parameter passing
- [dbutils Utilities](/concepts/databricks-utilities-for-scala-library.md) — The broader utility API that includes `notebook.run()` and `notebook.exit()`
- Databricks Widgets — Controls used to receive parameters in notebooks
- %run — The alternative method for including notebooks inline
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Scheduled orchestration for notebook workflows
- Workflow Orchestration — Broader patterns for coordinating multi-step pipelines

## Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
