---
title: Delta Lake table streaming reads and writes | Databricks on AWS
source: https://docs.databricks.com/aws/en/structured-streaming/delta-lake
ingestedAt: "2026-06-18T08:19:05.830Z"
---

This page describes how to use Delta Lake tables as sources and sinks for [Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) with `readStream` and `writeStream`. Delta Lake solves common performance and reliability problems for streaming systems and files. The benefits include:

*   Coalesce small files produced by low-latency ingest and improve performance.
*   Maintain "exactly-once" processing with more than one stream (or concurrent batch jobs).
*   Efficiently discover new files when using files as a stream source.

To learn how to load data using streaming tables in Databricks SQL, see [Use standalone streaming tables](https://docs.databricks.com/aws/en/ldp/dbsql/streaming).

For stream-static joins with Delta Lake, see [Stream-static joins](https://docs.databricks.com/aws/en/transform/join#stream-static).

For a complete list of `DataStreamReader` and `DataStreamWriter` options for Delta Lake, see [`DataStreamReader` Delta Lake options](https://docs.databricks.com/aws/en/spark/api-options#stream-reader-delta) and [`DataStreamWriter` Delta Lake options](https://docs.databricks.com/aws/en/spark/api-options#stream-writer-delta).

warning

If you use a Delta Lake table as a streaming source, the streaming query must run at least one time within the source table's retention window. The default retention windows are 7 days for `VACUUM`\-removed data files and 30 days for the transaction log (`logRetentionDuration`). If a query falls behind these windows, it fails with `DELTA_FILE_NOT_FOUND_DETAILED` and must be reset with a full refresh.

Do _not_ set `spark.sql.files.ignoreMissingFiles` to `true` as a workaround because this configuration silently produces incorrect results. If a stream's schedule can't keep up with the default retention windows, increase the source table's retention instead.

## Use Delta Lake tables as a sink[​](#use-delta-lake-tables-as-a-sink "Direct link to use-delta-lake-tables-as-a-sink")

You can write data into a Delta Lake table using Structured Streaming. The Delta Lake transaction log guarantees exactly-once processing, even when there are other streams or batch queries running concurrently against the table.

When you write to a Delta Lake table using a Structured Streaming sink, you might see empty commits with `epochId = -1`. These are expected and typically occur:

*   On the first batch of each run of the streaming query (this happens every batch for `Trigger.AvailableNow`).
*   When a schema is changed (such as adding a column).

These empty commits are intentional and do not indicate an error. They do not affect the correctness or performance of the query in any significant way.

note

The Delta Lake `VACUUM` function removes all files not managed by Delta Lake but skips any directories that begin with `_`. You can safely store checkpoints alongside other data and metadata for a Delta Lake table using a directory structure such as `<table-name>/_checkpoints`.

### Monitor backlog with metrics[​](#monitor-backlog-with-metrics "Direct link to monitor-backlog-with-metrics")

Use the following metrics to monitor the backlog of a [streaming query process](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#reading-metrics-interactively):

*   `numBytesOutstanding`: Number of bytes yet to be processed in the backlog.
*   `numFilesOutstanding`: Number of files yet to be processed in the backlog.
*   `numNewListedFiles`: Number of Delta Lake files listed to calculate the backlog for this batch.
*   `backlogEndOffset`: The Delta Lake table version used to calculate the backlog.

In a notebook, view these metrics under the **Raw Data** tab in the streaming query progress dashboard:

JSON

    {  "sources": [    {      "description": "DeltaSource[file:/path/to/source]",      "metrics": {        "numBytesOutstanding": "3456",        "numFilesOutstanding": "8"      }    }  ]}

### Append mode[​](#append-mode "Direct link to append-mode")

By default, streams run in append mode and only add new records to the table.

Use the `toTable` method when streaming to tables:

*   Python
*   Scala

Python

    (events.writeStream   .outputMode("append")   .option("checkpointLocation", "/tmp/delta/events/_checkpoints/")   .toTable("events"))

### Complete mode[​](#complete-mode "Direct link to Complete mode")

Use Structured Streaming with complete mode to replace the entire table after every batch. For example, you can continuously update an aggregated summary table of events by customer:

*   Python
*   Scala

Python

    (spark.readStream  .table("events")  .groupBy("customerId")  .count()  .writeStream  .outputMode("complete")  .option("checkpointLocation", "/tmp/delta/eventsByCustomer/_checkpoints/")  .toTable("events_by_customer"))

For applications without strict latency requirements, you can save computing resources and costs with one-time triggers such as `AvailableNow`. For example, use this trigger to update summary aggregation tables on a given schedule, processing only new data that has arrived since the last update. See [`AvailableNow`: Incremental batch processing](https://docs.databricks.com/aws/en/structured-streaming/triggers#available-now).

## Handle changes to source Delta Lake tables[​](#handle-changes-to-source-delta-lake-tables "Direct link to handle-changes-to-source-delta-lake-tables")

Structured Streaming incrementally reads Delta Lake tables. When a streaming query reads from a Delta Lake table, new records are processed idempotently as new table versions commit to the source table. Structured Streaming only accepts append inputs and throws an exception if any modifications occur on the source Delta Lake table. For example, if an `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` operation modifies a source Delta Lake table that is read by a streaming query, the stream fails with an error.

There are four typical approaches for handling upstream changes to source Delta Lake tables, depending on your use case. A reference table and details on each are provided below:

### Skip upstream change commits with `skipChangeCommits`[​](#skip-upstream-change-commits-with-skipchangecommits "Direct link to skip-upstream-change-commits-with-skipchangecommits")

Set `skipChangeCommits` to ignore transactions that delete or modify existing records, and to process only appends. This is useful when changes to existing data do not need to be propagated through the stream, or when you prefer separate logic to handle those changes. You can turn on and turn off `skipChangeCommits` if you need to temporarily ignore one-time changes.

Databricks recommends using `skipChangeCommits` for most workloads that do not use change data feeds.

*   Python
*   Scala

Python

    (spark.readStream  .option("skipChangeCommits", "true")  .table("source_table"))

important

If the schema for a Delta Lake table changes after a streaming read begins against the table, the query fails. For most schema changes, you can restart the stream to resolve schema mismatch and continue processing.

In Databricks Runtime 12.2 LTS and below, you cannot stream from a Delta Lake table with column mapping enabled that has undergone non-additive schema evolution such as renaming or dropping columns. For details, see [Column mapping and streaming](https://docs.databricks.com/aws/en/tables/features/column-mapping#schema-tracking).

note

In Databricks Runtime 12.2 LTS and above, `skipChangeCommits` replaces `ignoreChanges`. In Databricks Runtime 11.3 LTS and lower, `ignoreChanges` is the only supported option. See [Legacy option: `ignoreChanges`](#legacy-ignore-changes) for details.

#### Legacy option: `ignoreDeletes`[​](#legacy-option-ignoredeletes "Direct link to legacy-option-ignoredeletes")

`ignoreDeletes` is a legacy option that only handles transactions that delete data at partition boundaries (that is, full partition drops). If you need to handle non-partition deletes, updates, or other modifications, use `skipChangeCommits` instead.

*   Python
*   Scala

Python

    (spark.readStream  .option("ignoreDeletes", "true")  .table("user_events"))

#### Legacy option: `ignoreChanges`[​](#legacy-option-ignorechanges "Direct link to legacy-option-ignorechanges")

`ignoreChanges` is available in Databricks Runtime 11.3 LTS and lower. In Databricks Runtime 12.2 LTS and above, it is replaced by `skipChangeCommits`.

With `ignoreChanges` enabled, rewritten data files in the source table are re-emitted after a data modification operation such as `UPDATE`, `MERGE INTO`, `DELETE` (within partitions), or `OVERWRITE`. Unchanged rows are often emitted alongside new rows, so downstream consumers must be able to handle duplicates. Deletes are not propagated downstream. `ignoreChanges` takes precedence over `ignoreDeletes`.

In contrast, `skipChangeCommits` disregards file-changing operations entirely. Rewritten data files in the source table due to data modification operations such as `UPDATE`, `MERGE INTO`, `DELETE`, and `OVERWRITE` are ignored entirely. To reflect changes in stream source tables, you must implement separate logic to propagate these changes.

Databricks recommends using `skipChangeCommits` for all new workloads. To migrate a workload from `ignoreChanges` to `skipChangeCommits`, refactor your streaming logic.

### Full refresh of downstream tables[​](#full-refresh-of-downstream-tables "Direct link to Full refresh of downstream tables")

If upstream changes are rare and the data is small enough to reprocess, you can delete the streaming checkpoint and output table, then restart the stream from the beginning. This causes the stream to reprocess all data from the source table. Be aware that this approach also requires reprocessing all downstream tables that depend on the output of this stream.

This approach is best suited for smaller datasets or workloads where upstream changes are infrequent and the cost of a full refresh is acceptable.

### Use change data feed[​](#use-change-data-feed "Direct link to Use change data feed")

For workloads that process all types of changes (inserts, updates, and deletes), use the Delta Lake change data feed. The change data feed records row-level changes to a Delta Lake table, allowing you to stream those changes and write logic to handle each change type in downstream tables. This is the most robust approach because your code explicitly handles every type of change event. See [Use change data feed on Databricks](https://docs.databricks.com/aws/en/tables/features/change-data-feed).

If you are using Lakeflow Spark Declarative Pipelines, see [The AUTO CDC APIs: Simplify change data capture with pipelines](https://docs.databricks.com/aws/en/ldp/cdc).

important

In Databricks Runtime 12.2 LTS and below, you can't stream from the change data feed for a Delta Lake table with column mapping enabled that has undergone non-additive schema evolution, such as renaming or dropping columns. See [Column mapping and streaming](https://docs.databricks.com/aws/en/tables/features/column-mapping#schema-tracking).

### Use materialized views[​](#use-materialized-views "Direct link to Use materialized views")

Materialized views automatically handle upstream changes by recomputing results when source data changes. If you do not need the lowest possible latency and want to avoid managing streaming complexity, a materialized view can simplify your architecture. Materialized views are available in Lakeflow Spark Declarative Pipelines and standalone pipelines. See [Materialized views](https://docs.databricks.com/aws/en/ldp/concepts/materialized-views).

### Example[​](#example "Direct link to Example")

For example, suppose you have a table `user_events` with `date`, `user_email`, and `action` columns that is partitioned by `date`. You stream out of the `user_events` table and you need to delete data from it due to GDPR.

`skipChangeCommits` allows you to delete data in multiple partitions (in this example, filtering on `user_email`). Use the following syntax:

Scala

    spark.readStream  .option("skipChangeCommits", "true")  .table("user_events")

If you update a `user_email` with the `UPDATE` statement, the file containing the `user_email` in question is rewritten. Use `skipChangeCommits` to ignore the changed data files.

Databricks recommends using `skipChangeCommits` instead of `ignoreDeletes` unless you are certain that deletes are always full partition drops.

## Use `foreachBatch` for idempotent table writes[​](#use-foreachbatch-for-idempotent-table-writes "Direct link to use-foreachbatch-for-idempotent-table-writes")

note

Databricks recommends configuring a separate streaming write for each sink you want to update instead of using `foreachBatch`. Writes to multiple sinks in `foreachBatch` reduces parallelization and increases overall latency because writes to multiple tables are serialized in `foreachBatch`.

Delta Lake tables support the following `DataFrameWriter` options to make writes to multiple tables within `foreachBatch` idempotent:

*   `txnAppId`: A unique string that you can pass on each DataFrame write. For example, you can use the StreamingQuery ID as `txnAppId`. `txnAppId` can be any user-generated unique string and does not have to be related to the stream ID.
*   `txnVersion`: A monotonically increasing number that acts as transaction version.

Delta Lake uses `txnAppId` and `txnVersion` to identify and ignore duplicate writes. For example, after a failure interrupts a batch write, you can re-run the batch with the same `txnAppId` and `txnVersion` to correctly identify and ignore duplicates. See [Use foreachBatch to write to arbitrary data sinks](https://docs.databricks.com/aws/en/structured-streaming/foreach).

warning

If you delete the streaming checkpoint and restart the query with a new checkpoint, you must provide a different `txnAppId`. New checkpoints start with a batch ID of `0`. Delta Lake uses the batch ID and `txnAppId` as a unique key, and skips batches with already seen values.

The following code example demonstrates this pattern:

*   Python
*   Scala

Python

    app_id = ... # A unique string that is used as an application ID.def writeToDeltaLakeTableIdempotent(batch_df, batch_id):  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 1  batch_df.write.format(...).option("txnVersion", batch_id).option("txnAppId", app_id).save(...) # location 2streamingDF.writeStream.foreachBatch(writeToDeltaLakeTableIdempotent).start()

## Upsert from streaming queries using `foreachBatch`[​](#upsert-from-streaming-queries-using-foreachbatch "Direct link to upsert-from-streaming-queries-using-foreachbatch")

You can use `merge` and `foreachBatch` to write complex upserts from a streaming query into a Delta Lake table. See [Use foreachBatch to write to arbitrary data sinks](https://docs.databricks.com/aws/en/structured-streaming/foreach).

This approach has many applications:

*   Improve write performance with `update` output mode, whereas `complete` output mode requires rewriting the entire result table for each microbatch.
*   Continuously apply a stream of changes to a Delta Lake table by using a merge query to write change data in `foreachBatch`. See [Slowly changing data (SCD) and change data capture (CDC) with Delta Lake](https://docs.databricks.com/aws/en/delta/merge#merge-in-cdc).
*   Handle deduplication during stream processing. You can use an insert-only merge query in `foreachBatch` to continuously write data to a Delta Lake table with automatic deduplication. See [Data deduplication when writing into Delta Lake tables](https://docs.databricks.com/aws/en/delta/merge#dedupe).

note

*   Verify that your `merge` statement inside `foreachBatch` is idempotent. Otherwise, restarts of the streaming query can apply the operation on the same batch of data multiple times. See [Use `foreachBatch` for idempotent table writes](#idempot-write).
    
*   When `merge` is used in `foreachBatch`, the input data rate metric might return a multiple of the actual rate that data is generated at the source. `merge` reads input data multiple times, which multiplies the metrics. To prevent metric multiplication, cache the batch DataFrame before `merge` and then uncache it after `merge`.
    
    Input data rate is available through `StreamingQueryProgress` and in the notebook streaming rate graph. See [Monitoring Structured Streaming queries on Databricks](https://docs.databricks.com/aws/en/structured-streaming/stream-monitoring).
    

For example, you can use `MERGE` SQL statements within `foreachBatch`:

*   Scala
*   Python

Scala

    // Function to upsert microBatchOutputDF into Delta Lake table using mergedef upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long) {  // Set the dataframe to view name  microBatchOutputDF.createOrReplaceTempView("updates")  // Use the view name to apply MERGE  // NOTE: You have to use the SparkSession that has been used to define the `updates` dataframe  microBatchOutputDF.sparkSession.sql(s"""    MERGE INTO aggregates t    USING updates s    ON s.key = t.key    WHEN MATCHED THEN UPDATE SET *    WHEN NOT MATCHED THEN INSERT *  """)}// Write the output of a streaming aggregation query into Delta Lake tablestreamingAggregatesDF.writeStream  .foreachBatch(upsertToDelta _)  .outputMode("update")  .start()

You can also use the Delta Lake APIs for streaming upserts:

*   Scala
*   Python

Scala

    import io.delta.tables.*val deltaTable = DeltaTable.forName(spark, "table_name")// Function to upsert microBatchOutputDF into Delta Lake table using mergedef upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long) {  deltaTable.as("t")    .merge(      microBatchOutputDF.as("s"),      "s.key = t.key")    .whenMatched().updateAll()    .whenNotMatched().insertAll()    .execute()}// Write the output of a streaming aggregation query into Delta Lake tablestreamingAggregatesDF.writeStream  .foreachBatch(upsertToDelta _)  .outputMode("update")  .start()

## Set initial table version to process changes[​](#set-initial-table-version-to-process-changes "Direct link to set-initial-table-version-to-process-changes")

By default, streams begin with the latest available Delta Lake table version. This includes a complete snapshot of the table at that moment and all future changes. Databricks recommends that you use the default initial table version for most workloads.

Optionally, you can use the following options to specify the starting point of the Delta Lake streaming source without processing the entire table.

*   `startingVersion`: The Delta Lake table version to start reading from. All table changes committed at or after the specified version are read by the stream. If the specified version is not available, the stream fails to start.
    
    To find available commit versions, run `DESCRIBE HISTORY` and check the `version`. To return only the latest changes, specify `latest`. For information on Delta Lake table versions, see [Work with table history](https://docs.databricks.com/aws/en/tables/history).
    
*   `startingTimestamp`: The timestamp to start reading from. All table changes committed at or after the specified timestamp are read by the stream. If the provided timestamp precedes all table commits, the streaming read begins with the earliest available timestamp. Set either:
    
    *   A timestamp string. For example, `"2019-01-01T00:00:00.000Z"`.
    *   A date string. For example, `"2019-01-01"`.

You cannot set both `startingVersion` and `startingTimestamp` at the same time. These settings apply to new streaming queries only. If a streaming query has started and the progress has been recorded in its checkpoint, these settings are ignored.

important

Although you can start the streaming source from a specified version or timestamp, the schema of the streaming source is always the latest schema of the Delta Lake table. You must ensure there is no incompatible schema change to the Delta Lake table after the specified version or timestamp. Otherwise, the streaming source might return incorrect results when reading the data with an incorrect schema.

### Example[​](#example-1 "Direct link to Example")

For example, suppose you have a table `user_events`. If you want to read changes since version 5, use:

Scala

    spark.readStream  .option("startingVersion", "5")  .table("user_events")

If you want to read changes since 2018-10-18, use:

Scala

    spark.readStream  .option("startingTimestamp", "2018-10-18")  .table("user_events")

## Process initial snapshot without dropping data[​](#process-initial-snapshot-without-dropping-data "Direct link to process-initial-snapshot-without-dropping-data")

This feature is available on Databricks Runtime 11.3 LTS and above.

In a stateful streaming query with a defined watermark, processing files by modification time can process records in the wrong order. This can cause the watermark to incorrectly mark records as late events and drop them. This can only occur when the initial Delta snapshot is processed in the default order.

For streams with a Delta source table, the query first processes all of the data present in the table and creates a version called the _initial snapshot_. By default, the Delta Lake table's data files are processed based on which file was last modified. However, the last modification time does not necessarily represent the record event time order.

To avoid data drops during initial snapshot processing, enable the `withEventTimeOrder` option. `withEventTimeOrder` divides the event time range of initial snapshot data into time buckets. Each micro-batch processes a bucket by filtering data within the time range. The `maxFilesPerTrigger` and `maxBytesPerTrigger` options are still applicable to control the micro-batch size, but only approximately due to the processing approach.

The following diagram shows this process:

![Initial Snapshot](https://docs.databricks.com/aws/en/assets/images/delta-initial-snapshot-data-drop-22bccd2312254a9f9e853389e49f13eb.png)

### Constraints[​](#constraints "Direct link to Constraints")

*   You cannot change `withEventTimeOrder` if the stream query has started and the initial snapshot is actively processing. To restart with `withEventTimeOrder` changed, you must delete the checkpoint.
*   If `withEventTimeOrder` is enabled, you cannot downgrade a stream to a Databricks Runtime version that does not support this feature until the initial snapshot processing completes. To downgrade, wait for the initial snapshot to finish, or delete the checkpoint and restart the query.
*   This feature is not supported in the following scenarios:
    *   The event time column is a generated column and there are non-projection transformations between the Delta source and watermark.
    *   There is a watermark that has more than one Delta source in the stream query.

### Performance[​](#performance "Direct link to Performance")

If `withEventTimeOrder` is enabled, initial snapshot processing performance might be slower. Each micro-batch scans the initial snapshot to filter data within the corresponding event time range. To improve filtering performance:

*   Use a Delta source column as the event time so that data skipping can be applied. See [Data skipping](https://docs.databricks.com/aws/en/tables/data-skipping).
*   Partition the table along the event time column.

Use the Spark UI to see how many Delta files are scanned for a specific micro-batch.

### Example[​](#example-2 "Direct link to Example")

Suppose you have a table `user_events` with an `event_time` column. Your streaming query is an aggregation query. If you want to ensure no data drop during the initial snapshot processing, you can use:

Scala

    spark.readStream  .option("withEventTimeOrder", "true")  .table("user_events")  .withWatermark("event_time", "10 seconds")

You can set `withEventTimeOrder` with a Spark configuration on the cluster to apply it to all streaming queries: `spark.databricks.delta.withEventTimeOrder.enabled true`.

## Limit input rate to improve processing performance[​](#limit-input-rate-to-improve-processing-performance "Direct link to limit-input-rate-to-improve-processing-performance")

By default, Structured Streaming processes as many files as possible in each micro-batch. To limit the amount of data processed per batch and manage memory usage, stabilize latency, or reduce cloud storage costs, use the following options:

*   `maxFilesPerTrigger`: The number of new files to be considered in every micro-batch. The default is 1000.
*   `maxBytesPerTrigger`: The amount of data that gets processed in each micro-batch. This option sets a "soft max", meaning that a batch processes approximately this amount of data and might process more than the limit in order to make the streaming query move forward in cases when the smallest input unit is larger than this limit. This is not set by default.

If you use both `maxBytesPerTrigger` and `maxFilesPerTrigger`, the micro-batch processes data until either the `maxFilesPerTrigger` or `maxBytesPerTrigger` limit is reached.

note

By default, if `logRetentionDuration` cleans up transactions in the source table and the streaming query tries to process those versions, the query fails to prevent data loss. You can set the option `failOnDataLoss` to `false` to ignore lost data and continue processing. See [Configure data retention for time travel queries](https://docs.databricks.com/aws/en/tables/history#data-retention).

## Control cloud storage cost[​](#control-cloud-storage-cost "Direct link to control-cloud-storage-cost")

Streaming queries have several trigger modes available that allow you to balance cost and latency, including `processingTime`, `availableNow`, and `realTime`. See [Control cloud storage cost](https://docs.databricks.com/aws/en/structured-streaming/triggers#control-cloud-storage-cost).
