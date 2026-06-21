---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5554b114fbdf3ee2cf3c037dacf536814c5ad9f8ae79ad67a426e016cd09fbd1
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - empty-dataframe-creation-without-scemptyrdd
    - EDCWS
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: Empty DataFrame Creation Without sc.emptyRDD
description: Creating empty DataFrames by passing an empty ArrayList (Scala) or empty list (Python) to spark.createDataFrame instead of using sc.emptyRDD.
tags:
  - databricks
  - spark
  - scala
  - python
timestamp: "2026-06-19T23:16:54.541Z"
---

<!--  
This page is extracted from the provided source only.  
Do not add information beyond what is in the source.  
-->

# Empty DataFrame Creation Without `sc.emptyRDD`

When upgrading legacy workspaces to [Unity Catalog](/concepts/unity-catalog.md), job notebooks that run on a shared cluster cannot use `sc.emptyRDD()` to create an empty DataFrame because the SparkContext is not directly accessible in the same way. The workaround is to use an empty Java `ArrayList` (Scala) or an empty Python list (Python) with `spark.createDataFrame`. This technique is part of the broader set of job updates required when migrating to [Unity Catalog](/concepts/unity-catalog.md). ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Before Migration (Legacy Code)

In a non-Unity-Catalog environment, you could create an empty DataFrame with a defined schema using `sc.emptyRDD`:

**Scala:**

```scala
val schema = StructType(
  StructField("k", StringType, true) ::
  StructField("v", IntegerType, false) :: Nil
)
spark.createDataFrame(sc.emptyRDD[Row], schema)
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## After Migration ([Unity Catalog](/concepts/unity-catalog.md) Compatible)

On a shared cluster in a [Unity Catalog](/concepts/unity-catalog.md) workspace, use an empty Java `ArrayList` (Scala) or an empty Python list (Python) instead of the `RDD`-based approach.

**Scala:**

```scala
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}

val schema = StructType(
  StructField("k", StringType, true) ::
  StructField("v", IntegerType, false) :: Nil
)
spark.createDataFrame(new java.util.ArrayList[Row](), schema)
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**Python:**

```python
from pyspark.sql.types import StructType, StructField, StringType

schema = StructType([StructField("k", StringType(), True)])
spark.createDataFrame([], schema)
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

Both alternatives produce a DataFrame with zero rows and the specified schema, making them drop‑in replacements for the legacy `sc.emptyRDD` pattern.

## Related Concepts

- [Upgrade legacy workspaces to Unity Catalog](/concepts/migrating-existing-workspaces-to-unity-catalog.md) – The overall migration process that necessitates these code changes.
- [Shared cluster restrictions in Unity Catalog](/concepts/shared-cluster-compatibility-in-unity-catalog.md) – Why certain SparkContext operations are unavailable.
- DataFrame creation in PySpark – General methods for constructing DataFrames.
- Jobs migration to Unity Catalog – Broader guidance for updating job logic.

## Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
