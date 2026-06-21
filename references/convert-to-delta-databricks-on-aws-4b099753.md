---
title: CONVERT TO DELTA | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-convert-to-delta
ingestedAt: "2026-06-18T08:18:42.252Z"
---

**Applies to:** ![check marked yes](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAcCAYAAABlL09dAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFqADAAQAAAABAAAAHAAAAAClq0b4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACyGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8dGlmZjpZUmVzb2x1dGlvbj43MjwvdGlmZjpZUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6UmVzb2x1dGlvblVuaXQ+MjwvdGlmZjpSZXNvbHV0aW9uVW5pdD4KICAgICAgICAgPHRpZmY6WFJlc29sdXRpb24+NzI8L3RpZmY6WFJlc29sdXRpb24+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4zNjwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOkNvbG9yU3BhY2U+MTwvZXhpZjpDb2xvclNwYWNlPgogICAgICAgICA8ZXhpZjpQaXhlbFlEaW1lbnNpb24+NDc8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KgoXBqAAABIFJREFUSA3VlctrXFUcx8/r3hvTNGpISiOULIRKjCAaFQtdzExCk8xkIq1k3LiqqRQEEbcuOv0HBMGFxkdWWbQhSeNMGhJmknEVBFtBFKULH4hUoR2wIZnM3PPw+7uZm0QHrOiqF+7cc885v8/9vc53GHvQLv6vHHaMs8u46brE6M3dz+6fwHzy6qQgwFxuzhwGYV425y2e9/3Ivm1sGE+cns08mppP99FN43ienn/fG6+1eJzYSKhKsqJPvXvqofbHu3LOsZekL07CrS4ygkHVNOwtztnSTr16dTO3WYttYmhz38Fr3uVFnudtcnF0iEv5nvTlAEVqG5Y5sxcxl5wJDxkSnNm6/pqF/K3yy8sbsW1M2/d40k3KOT5nhgvjF5hg05Q5vas1h2sYC7i6t9dFOcWv094jQcBs9OHzpWxxJmYQPCoO5YmgqfnRs/Bo2tSNw01QhT0KSNpHYMILonoPB4Hd1aumbr/CBz5Nzo9OECPOOTUObXaJQrZbMXfTWXfCaktdEFUez79cjjw96itr3Hp5pu1MarJ2XLS7dWA6d3bCgc3capWYYnB6kLxiQpuLIpAnTGhCvBK0pY0I6gPqtF37beaHsfzAgFvPFX8Nt/SUd8Q73uari8RKVBKoBA1mEm3yWMfn3LEXKAWYIjCtUZ9G6QI09Dt9D9FcL6WLE5iPentoIX2SefyaUKLfGfvF9q1qcvPtzVpkpH31GKrej+pb4BRXXHMp6si3gN828rQz8ExoC4BmaQ5gllwafQLQNS54v6kZA+snZV9XL61FYN+T3TA/SrlWRzxqrSnXsCNIvgVaUE5dwyyWM8WJfD5PsbjhYqZfcFlGgft0TYcoqCCGb3Q3gaP8GsmdREbhobTb4asb51ZmaTFxZWREdXgr+NBiabyYi3v1TDHzFNp6Db3ca3ZNCLjHHaco9loSg8hjs6vvcsnuMfSsE6KfoGPXx4LKK6sl03Av6h+3ztNcdHgK408b68pg9No6Cs2ZhyXnqCUF32pIdYf27oF/377NpPieGkG1q3eSS+n3V9Ir9cEvX/c2zi7f6OnpqdHmVCH7LHeuBAeORVAWQcnMSZ8zKfl35ufq7Qg8+OGgR1VETgsykCy819jx2r03ktfSH9x4bjpEw/ukbkOfZZ9nzpYQazeKrJueEoO4RviKQUMKxCLtQOzYgt9EIYED0nHT4oCgULs4TW2mpj8pTyxPJRZGTwspl5GpThsC2qxNk2qgHegf/osLvWfK5xbvEpM0wNExrGQrd1zdvAklQxfzIPyjUUcErw0tZRYE51dg2gqFnMBekiiRLUGjIw3mfhVj6TssQihqXQQqsCHOggOEDg7iBgxyB2VqU4o0ylp+YT1b+DhmUCRR8WhAGkztBJX6yDT0MLTgW9XhB4gJbYjABI4NXBe+ECiwwpqCrnxjjRkiKNkSg1h07Xu898pY/NUWoXdNoedNobcQ+p8g9M1iHYbGrJZnLH3xQvTXNJvqS+H+z39NMQzP//Vn2pKKQ+CDIZXrcjNtl6LitUjqweYHdfQnxCZNMo0VXxYAAAAASUVORK5CYII=) Databricks SQL ![check marked yes](data:image/png;base64,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) Databricks Runtime

Converts an existing Apache Parquet table to a Delta table in-place. This command lists all the files in the directory, creates a Delta Lake transaction log that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process collects statistics to improve query performance on the converted Delta table. If you provide a table name, the metastore is also updated to reflect that the table is now a Delta table.

This command supports converting Apache Iceberg tables whose underlying file format is Parquet. In this case, the converter generates the Delta Lake transaction log based on Iceberg table's native file manifest, schema and partitioning information.

## Syntax[​](#syntax "Direct link to Syntax")

    CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]

## Parameters[​](#parameters "Direct link to Parameters")

*   [table\_name](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name)
    
    Either an optionally qualified [table identifier](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-identifiers) or a path to a `parquet` or `iceberg` file directory. The name must not include a [temporal specification or options specification](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#table-name). For Iceberg tables, you can only use paths, as converting managed iceberg tables is not supported.
    
*   **NO STATISTICS**
    
    Bypass statistics collection during the conversion process and finish conversion faster. After the table is converted to Delta Lake, Databricks recommends that you use liquid clustering to reorganize the data layout and generate statistics. See [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering).
    
*   **[PARTITIONED BY](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-partition#partitioned-by)**
    
    Partition the created table by the specified columns. When `table_name` is a path, the `PARTITIONED BY` is required for partitioned data. When the `table_name` is a qualified table identifier, `PARTITIONED BY` clause is optional and the partition specification are loaded from the metastore. In either approach, the conversion process aborts and throw an exception if the directory structure does not conform to the provided or loaded `PARTITIONED BY` specification.
    
    note
    
    In Databricks Runtime 11.1 and below, `PARTITIONED BY` is a required argument for all partitioned data.
    

## Examples[​](#examples "Direct link to Examples")

note

You do not need to provide partitioning information for Iceberg tables or tables registered to the metastore.

SQL

    CONVERT TO DELTA database_name.table_name; -- only for Parquet tablesCONVERT TO DELTA parquet.`s3://my-bucket/path/to/table`  PARTITIONED BY (date DATE); -- if the table is partitionedCONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`; -- uses Iceberg manifest for metadata

## Caveats[​](#caveats "Direct link to Caveats")

Any file not tracked by Delta Lake is invisible and can be deleted when you run `VACUUM`. You should avoid updating or appending data files during the conversion process. After the table is converted, make sure all writes go through Delta Lake.

It is possible that multiple external tables share the same underlying Parquet directory. In this case, if you run `CONVERT` on one of the external tables, then you will not be able to access the other external tables because their underlying directory has been converted from Parquet to Delta Lake. To query or write to these external tables again, you must run `CONVERT` on them as well.

`CONVERT` populates the catalog information, such as schema and table properties, to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata is different from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown.

While using Databricks Runtime, if you want `CONVERT` to overwrite the existing metadata in the Delta Lake transaction log, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to false.

## Related articles[​](#related-articles "Direct link to Related articles")

*   [PARTITIONED BY](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-partition#partitioned-by)
*   [VACUUM](https://docs.databricks.com/aws/en/sql/language-manual/delta-vacuum)
