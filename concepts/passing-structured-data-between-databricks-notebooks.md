---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e3652f4d3d22c6682121cf3f45abdc2bbf4adff29af62b51542e2ba8279735c
  pageDirectory: concepts
  sources:
    - orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - passing-structured-data-between-databricks-notebooks
    - PSDBDN
  citations:
    - file: orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md
title: Passing structured data between Databricks notebooks
description: Techniques for sharing non-string data between notebooks using temporary views, DBFS file storage, and JSON serialization.
tags:
  - databricks
  - data-sharing
  - orchestration
timestamp: "2026-06-19T19:53:01.890Z"
---

# Passing structured data between Databricks notebooks

Passing structured data between notebooks is possible using `dbutils.notebook.run()` and `dbutils.notebook.exit()`. Because called notebooks run in the same JVM (for Python and Scala), temporary views can be shared across the call boundary. The `dbutils.notebook.exit()` method can only return a single string, but several patterns allow passing larger or more complex datasets. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Method 1: Return a reference to a temporary view

The callee notebook writes data to a global temporary view and returns the view name via `dbutils.notebook.exit()`. The caller reads the view using `table()` and the global temp database name.

**Callee notebook:**
```python
spark.range(5).toDF("value").createOrReplaceGlobalTempView("my_data")
dbutils.notebook.exit("my_data")
```

**Caller notebook:**
```python
returned_table = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)
global_temp_db = spark.conf.get("spark.sql.globalTempDatabase")
display(table(global_temp_db + "." + returned_table))
```
^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Method 2: Write to DBFS and return the path

For larger datasets, the callee notebook writes the data to DBFS (e.g., Parquet) and returns the path. The caller reads the dataset from that path.

**Callee notebook:**
```python
dbutils.fs.rm("/tmp/results/my_data", recurse=True)
spark.range(5).toDF("value").write.format("parquet").save("dbfs:/tmp/results/my_data")
dbutils.notebook.exit("dbfs:/tmp/results/my_data")
```

**Caller notebook:**
```python
returned_table = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)
display(spark.read.format("parquet").load(returned_table))
```
^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Method 3: Serialise results as JSON

To return multiple values, use the standard `json` library to serialise a dictionary in the callee and deserialise it in the caller.

**Callee notebook:**
```python
import json
dbutils.notebook.exit(json.dumps({
  "status": "OK",
  "table": "my_data"
}))
```

**Caller notebook:**
```python
import json
result = dbutils.notebook.run("LOCATION_OF_CALLEE_NOTEBOOK", 60)
print(json.loads(result))
```
^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Limitations and notes

- `dbutils.notebook.exit()` accepts only a single string. All three methods work around this constraint by passing a reference (view name or path) or a serialised payload. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- The shared JVM is available only when both notebooks run Python or Scala. The techniques work identically in both languages. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]
- The `arguments` parameter of `dbutils.notebook.run()` accepts only Latin ASCII characters; non‑ASCII characters produce an error. ^[orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md]

## Related concepts

- [dbutils.notebook.run()](/concepts/dbutilsnotebookrun.md)
- dbutils.notebook.exit()
- Temporary views
- DBFS
- Widgets|Databricks widgets (for passing parameters to the called notebook)
- Workflow orchestration|Orchestrating Databricks notebooks

## Sources

- orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md

# Citations

1. [orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws.md](/references/orchestrate-databricks-notebooks-and-modularize-code-databricks-on-aws-2198031f.md)
