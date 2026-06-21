---
title: Troubleshoot common sharing issues in OpenSharing | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/troubleshooting
ingestedAt: "2026-06-18T08:06:04.014Z"
---

The following sections describe common errors that might occur when you try to access data in a share.

## Resource limit exceeded errors[​](#resource-limit-exceeded-errors "Direct link to resource-limit-exceeded-errors")

**Issue**: Your query on a shared table returns the error `RESOURCE_LIMIT_EXCEEDED`.

*   `"RESOURCE_LIMIT_EXCEEDED","message":"The table metadata size exceeded limits"`
*   `"RESOURCE_LIMIT_EXCEEDED","message":"The number of files in the table to return exceeded limits, consider contact your provider to optimize the table"`

**Possible causes**: There are limits on the number of files in metadata allowed for a shared table:

*   **Active files**: A shared table supports a maximum of 400,000 active files (AddFile actions). If the number of active files exceeds this limit, queries return the "number of files exceeded" error.
*   **Remove file actions**: A shared table supports a maximum of 100,000 RemoveFile actions in the Delta log. If the number of RemoveFile actions exceeds this limit, queries return the "metadata size exceeded" error.

You can request a limit increase for the active files limit. See [Resource limits](https://docs.databricks.com/aws/en/resources/limits).

**Recommended fix**: Contact your data provider and ask them to optimize the shared table by running `OPTIMIZE` and `VACUUM` to compact small files and remove stale RemoveFile entries from the Delta log. For additional guidance, see [RESOURCE\_LIMIT\_EXCEEDED error when querying a Delta Sharing table](https://kb.databricks.com/resource_limit_exceeded-error-when-querying-a-delta-sharing-table) in the Databricks Knowledge Base.

## AWS S3 bucket name issue[​](#aws-s3-bucket-name-issue "Direct link to AWS S3 bucket name issue")

**Issue**: You see an error message that throws a file not found or certificate exception.

Spark error example:

    FileReadException: Error while reading file delta-sharing:/%252Ftmp%252Fexample.share%2523example.tpc_ds.example/XXXXXXXXXXXXX/XXXXXXXX.Caused by: SSLPeerUnverifiedException: Certificate for - <[workspace name].cloud.databricks.com.s3.us-east-1.amazonaws.com> doesn't match any of the subject alternative names [s3.amazonaws.com, *.s3.amazonaws.com…]:

Pandas error example:

    FileNotFoundError(path)FileNotFoundError: https://xxxx.xxxxxx.s3.xx-xxxx-1.amazonaws.com/xxxxxx/part-00000-xxxxx-Amz-Algorithm=Axxxxxx-Amz-Date=xxxxxxxx&X-Amz-SignedHeaders=host&X-Amz-Expires=xxx&X-Amz-Credential=xxxxxxx_request&X-Amz-Signature=xxxxx

Power BI error example:

    DataSource.Error: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel.Details:    https://xxxx.xxxxxxxxx.s3.xx-xxxx-1.amazonaws.com/xxxxxxxx/part-00000-xxxxxxx.snappy.parquet

**Possible cause**: Typically you see this error because your bucket name uses dot or period notation (for example, `incorrect.bucket.name.notation`). This is an AWS limitation. See the [AWS bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).

You might get this error even if your bucket name is formatted correctly. For example, you might encounter an SSL error (`SSLCertVerificationError`) when you execute code on PyCharm.

**Recommended fix**: If your bucket name uses invalid AWS bucket naming notation, use a different bucket for Unity Catalog and OpenSharing.

If your bucket uses valid naming conventions and you still face a `FileNotFoundError` in Python, enable debug logging to help isolate the issue:

Python

    import logginglogging.basicConfig(level=logging.DEBUG)

## Vacuumed data file issue[​](#vacuumed-data-file-issue "Direct link to Vacuumed data file issue")

**Issue**: You see an error message that throws a “404 The specified \[path|key\] does not exist” exception.

Spark error examples:

    java.lang.Throwable: HTTP request failed with status: HTTP/1.1 404 The specified path does not exist.

or

    HTTP request failed with status: HTTP/1.1 404 Not Found <?xml version="1.0" encoding="UTF-8"?><Error><Code>NoSuchKey</Code><Message>The specified key does not exist.</Message>

**Possible cause**: Typically you see this error because the data file corresponding to the pre-signed URL is vacuumed in the shared table and the data file belongs to a historical table version.

**Workaround**: Query the latest snapshot.

## Schema mismatch error with Open Source Spark[​](#schema-mismatch-error-with-open-source-spark "Direct link to schema-mismatch-error-with-open-source-spark")

**Issue**: When using Open Source Spark (OSS), you see a schema mismatch error when reading OpenSharing tables.

Error example:

    py4j.protocol.Py4JJavaError: An error occurred while calling o85.count.: org.apache.spark.SparkException: The schema or partition columns of your Delta table has changed since your DataFrame was created. Please redefine your DataFrame

**Possible cause**: The schema or partition columns of the Delta table changed after the DataFrame was created.

**Recommended fix**: Set the Spark configuration flag `spark.delta.sharing.client.useStructuralSchemaMatch` to `true`.

note

The `spark.delta.sharing.client.useStructuralSchemaMatch` configuration is only available in `delta-sharing-client` 1.2.3 or above, which requires Apache Spark 4.0.0 or above.

Python

    spark.conf.set("spark.delta.sharing.client.useStructuralSchemaMatch", "true")

**Issue**: Your query on a shared view, materialized view, or streaming table returns the error `DS_MATERIALIZATION_QUERY_FAILED`.

    "DS_MATERIALIZATION_QUERY_FAILED": "The shared asset could not be materialized due to the asset not being accessible in the materialization workspace. Please ask data provider to contact :re[DB] support to override the materialization workspace."

**Possible causes**: The provider does not have read-write access to the asset they are trying to share.

**Recommended fix**: Contact your data provider to ensure they have read-write access to the shared data asset.

## Network access error during data materialization[​](#network-access-error-during-data-materialization "Direct link to network-access-error-during-data-materialization")

**Issue**: Your query on a shared data asset returns an error about accessing the data provider's cloud storage.

    There was an issue accessing the data provider's cloud storage. Shared view materialization uses the Serverless compute of data provider's region to perform the materialization. Please contact the data provider to allowlist Serverless compute IPs of their corresponding region to access the view's dependent tables storage location.

**Possible causes**: The storage location for the materialized data has network restrictions (such as a firewall or private link) that prevent Databricks serverless compute from accessing it. When sharing views, materialized views, or streaming tables, the data is temporarily materialized on the provider's side. The materialization storage location is the asset's parent schema or catalog storage location.

**Recommended fix**: The data provider needs to allowlist serverless compute IPs of their corresponding region to access the view's dependent tables storage location. To configure your firewall, see [Serverless compute firewall configuration](https://docs.databricks.com/aws/en/security/network/serverless-network-security/serverless-firewall-config).

## Data asset "does not exist" error[​](#data-asset-does-not-exist-error "Direct link to data-asset-does-not-exist-error")

If you click on a shared asset and encounter an object "does not exist" error, the share owner on the provider side might not have sufficient permissions on the asset. Contact your data provider and ask them to verify that the share owner has the required permissions on all shared assets. For more information about permissions required for a share owner to share a data asset, see [Requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) and [Grant recipient access to share](https://docs.databricks.com/aws/en/delta-sharing/grant-access#grant-recipient-access).
