---
title: Combine Ray and Spark in the same environment on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/connect-spark-ray
ingestedAt: "2026-06-18T08:13:01.234Z"
---

With Databricks, you can run Ray and Spark operations in the same execution environment to leverage the strengths of both distributed computing engines.

Ray and Spark integration is supported by Delta Lake and Unity Catalog, which provide robust data management, secure access, and lineage tracking.

This article shows you how to connect Ray and Spark operations according to the following use cases:

*   **Write Spark data to Ray data**: Efficiently transfer data in-memory to Ray.
*   **Write Ray data to Spark**: Output data from Ray back to Delta Lake or other storage solutions to ensure compatibility and access.
*   **Connect external Ray applications to Unity Catalog**: Connect Ray applications outside of Databricks to load data from a Databricks Unity Catalog table.

For more information on when to use Ray, Spark, or both, see [When to use Spark vs. Ray](https://docs.databricks.com/aws/en/machine-learning/ray/spark-ray-overview).

## Create a distributed Ray dataset from a Spark DataFrame[​](#create-a-distributed-ray-dataset-from-a-spark-dataframe "Direct link to Create a distributed Ray dataset from a Spark DataFrame")

To create a distributed Ray dataset from a Spark DataFrame, you can use the `ray.data.from_spark()` function to directly read a Spark DataFrame from Ray without needing to write the data to any location.

In-memory Spark to Ray transfers are available on Databricks Runtime ML 15.0 and above.

To enable this feature, you must do the following:

*   Set the Spark cluster config `spark.databricks.pyspark.dataFrameChunk.enabled` to `true` before starting your cluster.

Python

    import ray.datasource_table = "my_db.my_table"# Read a Spark DataFrame from a Delta table in Unity Catalogdf = spark.read.table(source_table)ray_ds = ray.data.from_spark(df)

warning

Autoscaling Spark clusters (including those using spot instances) must set the `use_spark_chunk_api` parameter to `False` to use the `from_spark()` function. Otherwise, the API call will result in cache misses because the cache on a Spark executor is lost when the executor terminates.

Python

    ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)

## Write Ray Data to Spark[​](#write-ray-data-to-spark "Direct link to Write Ray Data to Spark")

To write Ray data to Spark, you must write the dataset to a location that Spark can access.

In Databricks Runtime ML below 15.0, you can write directly to an object store location using the Ray Parquet writer, `ray_dataset.write_parquet()` from the `ray.data` module. Spark can read this Parquet data with native readers.

For Unity Catalog enabled workspaces, use the `ray.data.Dataset.write_databricks_table` function to write to a Unity Catalog table.

This function temporarily stores the Ray dataset in Unity Catalog Volumes, reads from Unity Catalog volumes with Spark, and finally writes to a Unity Catalog table. Before calling `ray.data.Dataset.write_databricks_table` function, ensure that the environment variable `"_RAY_UC_VOLUMES_FUSE_TEMP_DIR"` is set to a valid and accessible Unity Catalog volume path, like `"/Volumes/MyCatalog/MySchema/MyVolume/MyRayData"`.

Python

    ds = ray.datads.write_databricks_table()

For workspaces that do not have Unity Catalog enabled, you can manually store a Ray Data dataset as a temporary file, such as a Parquet file in DBFS, and then read the data file with Spark.

Python

    ds.write_parquet(tmp_path)df = spark.read.parquet(tmp_path)df.write.format("delta").saveAsTable(table_name)

## Write data from Ray core applications to Spark[​](#write-data-from-ray-core-applications-to-spark "Direct link to Write data from Ray core applications to Spark")

Databricks can also integrate Ray Core applications with Spark, allowing you to run Ray Core (the lower-level APIs of Ray) and Spark workloads within the same environment and enabling data exchange between them. This integration offers several patterns to suit different workloads and data management needs, ensuring a simplified experience using both frameworks.

There are three main patterns for writing data from Ray to Spark.

*   **Persist output in a temporary location**: Temporarily store Ray task outputs in DBFS or Unity Catalog volumes before consolidating them into a Spark DataFrame.
*   **Connect with Spark Connect**: Directly connect Ray tasks to a Spark cluster, enabling Ray to interact with Spark DataFrames and tables.
*   **Use third-party libraries**: Use external libraries, such as `deltalake` or `deltaray`, to write data from Ray Core tasks to Delta Lake or Spark tables.

### Pattern 1: Persist output in a temporary location[​](#pattern-1-persist-output-in-a-temporary-location "Direct link to Pattern 1: Persist output in a temporary location")

The most common pattern for writing data from Ray to Spark is to store the output data in a temporary location, such as Unity Catalog volumes or DBFS. After storing the data, the Ray driver thread reads each part of the files on the worker nodes and consolidates them into a final DataFrame for further processing. Typically, the temporary files are in a standard format like CSV. This approach works best when the output data is in tabular form, such as a Pandas DataFrame generated by a Ray Core task.

Use this method when the output from Ray tasks is too large to fit in the memory of the driver node or the shared object-store. If you need to handle large datasets without persisting data to storage, consider increasing the memory allocated to the driver node in your Databricks cluster to improve performance.

Python

    import osimport uuidimport numpy as npimport pandas as pd@ray.remotedef write_example(task_id, path_prefix):  num_rows = 100  df = pd.DataFrame({      'foo': np.random.rand(num_rows),      'bar': np.random.rand(num_rows)  })  # Write the DataFrame to a CSV file  df.to_csv(os.path.join(path_prefix, f"result_part_{task_id}.csv"))n_tasks = 10# Put a unique DBFS prefix for the temporary file pathdbfs_prefix = f"/dbfs/<USERNAME>"# Create a unique path for the temporary filespath_prefix = os.path.join(dbfs_prefix, f"/ray_tmp/write_task_{uuid.uuid4()}")tasks = ray.get([write_example.remote(i, path_prefix) for i in range(n_tasks)])# Read all CSV files in the directory into a single DataFramedf = spark.read.csv(path_prefix.replace("/dbfs", "dbfs:"), header=True, inferSchema=True)

### Pattern 2: Connect using Spark Connect[​](#pattern-2-connect-using-spark-connect "Direct link to Pattern 2: Connect using Spark Connect")

Another way for Ray Core tasks to interact with Spark within the remote task is to use Spark Connect. This allows you to set up the Spark context on the Ray worker to point to the Spark cluster running from the driver node.

To set this up, you must configure Ray cluster resources to allocate space for Spark. For example, if a worker node has 8 CPUs, set num\_cpus\_worker\_node to 7, leaving 1 CPU for Spark. For larger Spark tasks, it's recommended to allocate a larger share of resources.

Python

    from databricks.connect import DatabricksSessionimport ray@ray.remoteclass SparkHandler(object):   def __init__(self, access_token=None, cluster_id=None, host_url=None):       self.spark = (DatabricksSession                     .builder                     .remote(host=host_url,                             token=access_token,                             cluster_id=cluster_id)                     .getOrCreate()                     )   def test(self):       df = self.spark.sql("select * from samples.nyctaxi.trips")       df.write.format("delta").mode("overwrite").saveAsTable("catalog.schema.taxi_trips")       return df.count()access_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()cluster_id = dbutils.notebook.entry_point.getDbutils().notebook().getContext().clusterId().get()host_url = f"https://{dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get('browserHostName').get()}"sh = SparkHandler.remote(access_token=access_token,                        cluster_id=cluster_id,                        host_url=host_url)print(ray.get(sh.test.remote()))

This example uses the notebook-generated token. However, Databricks recommends that production use cases use an access token stored in Databricks secrets.

Since this process calls a single Spark driver, it creates a _threading lock_ which causes all tasks to wait for the preceding Spark tasks to complete. Therefore, it is recommended to use this when there are not many concurrent tasks since they all will have sequential behavior as the Spark tasks complete. For these situations, it is better to persist the output and then combine into a single Spark dataframe at the end and then write out to an output table.

### Pattern 3: Third-party libraries[​](#pattern-3-third-party-libraries "Direct link to Pattern 3: Third-party libraries")

Another option is using third-party libraries that interact with Delta Lake and Spark. Databricks does not officially support these third-party libraries. An example of this is the `deltalake` library from the `delta-rs` project. This approach currently only works with Hive metastore tables, not Unity Catalog tables.

Python

    from deltalake import DeltaTable, write_deltalakeimport pandas as pdimport numpy as npimport ray@ray.remotedef write_test(table_name):   random_df_id_vals = [int(np.random.randint(1000)), int(np.random.randint(1000))]   pdf = pd.DataFrame({"id": random_df_id_vals, "value": ["foo", "bar"]})   write_deltalake(table_name, pdf, mode="append")def main():   table_name = "database.mytable"   ray.get([write_test.remote(table_name) for _ in range(100)])

Another third party library available is the deltaray library available through the Delta Incubator project [https://github.com/delta-incubator/deltaray](https://github.com/delta-incubator/deltaray))

Python

    # Standard Librariesimport pathlib# External Librariesimport deltarayimport deltalake as dlimport pandas as pd# Creating a Delta Tablecwd = pathlib.Path().resolve()table_uri = f'{cwd}/tmp/delta-table'df = pd.DataFrame({'id': [0, 1, 2, 3, 4, ], })dl.write_deltalake(table_uri, df)# Reading our Delta Tableds = deltaray.read_delta(table_uri)ds.show()

## Connect external Ray applications to Databricks[​](#connect-external-ray-applications-to-databricks "Direct link to Connect external Ray applications to Databricks")

### Create Ray dataset from Databricks warehouse query[​](#create-ray-dataset-from-databricks-warehouse-query "Direct link to Create Ray dataset from Databricks warehouse query")

For Ray 2.8.0 and above, to connect Ray applications outside of Databricks to tables inside Databricks, you can call the `ray.data.read_databricks_tables` API to load data from a Unity Catalog table.

First, set the `DATABRICKS_TOKEN` environment variable to your SQL warehouse access token. If you're not running your program on Databricks Runtime, also set the `DATABRICKS_HOST` environment variable to the Databricks workspace URL, as shown in the following:

Python

    export DATABRICKS_HOST=adb-<workspace-id>.<random-number>.azuredatabricks.net

Then, call `ray.data.read_databricks_tables()` to read from the SQL warehouse.

Python

    import rayray_dataset = ray.data.read_databricks_tables(    warehouse_id='...',  # Databricks SQL warehouse ID    catalog='catalog_1',  # Unity Catalog name    schema='db_1',  # Schema name    query="SELECT title, score FROM movie WHERE year >= 1980",)

warning

Databricks warehouses can only cache query results for approximately 2 hours. For long-running workloads, call the `ray.data.Dataset.materialize` method to materialize the Ray dataset to Ray distributed object store.

### Create Ray dataset from Databricks OpenSharing table[​](#create-ray-dataset-from-databricks-opensharing-table "Direct link to Create Ray dataset from Databricks OpenSharing table")

You can also read data from Databricks [OpenSharing tables](https://docs.databricks.com/aws/en/delta-sharing/). Reading from OpenSharing tables is more reliable than reading from a Databricks warehouse cache.

The `ray.data.read_delta_sharing_tables` API is available on Ray 2.33 and above.

Python

    import rayds = ray.data.read_delta_sharing_tables(    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",    limit=100000,    version=1,)

## Best Practices[​](#best-practices "Direct link to Best Practices")

*   Always use the techniques described in the Ray cluster best practice guide to ensure the cluster is fully utilized.
*   Consider using Unity Catalog volumes to store output data in a non-tabular format and provide governance.
*   Ensure that the `num_cpus_worker_node` configuration is set so that the number of CPU cores matches that of the Spark worker node. Similarly, set `num_gpus_worker_node` to the number of GPUs per Spark worker node. In this configuration, each Spark worker node launches one Ray worker node that fully utilizes the resources of the Spark worker node.

## Limitations[​](#limitations "Direct link to Limitations")

Unity Catalog currently does not share credentials for writing to tables from non-Spark writers. Therefore, all data being written to a Unity Catalog table from a Ray Core task will require that the data be persisted and then read with Spark, or Databricks Connect must be set up within the Ray task.
