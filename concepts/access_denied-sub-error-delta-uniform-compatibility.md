---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e27159fdb7546a6460479c3f1e17283b7c98b6c135895cf58605a6606c5198f
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access_denied-sub-error-delta-uniform-compatibility
    - AS(UC
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: ACCESS_DENIED sub-error (Delta Uniform Compatibility)
description: A specific reason code under the DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION error class indicating the configured location cannot be accessed due to permissions
tags:
  - error-messages
  - permissions
  - databricks
timestamp: "2026-06-18T11:56:15.466Z"
---

# ACCESS_DENIED sub-error (Delta Uniform Compatibility)

The **ACCESS_DENIED** sub-error occurs when the Delta Lake engine attempts to verify or use the location specified by the `delta.universalFormat.compatibility.location` table property but cannot access that location due to missing permissions, network errors, or other access-related failures. This is one of several sub-errors under the broader error condition `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION`.^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Message

When the ACCESS_DENIED sub-error is raised, the full error message includes a descriptive detail from the underlying storage system:

```
ACCESS_DENIED: Cannot access the location. Error: <error>
```

The `<error>` placeholder is replaced with the actual error message returned by the cloud storage provider (for example, an `AccessDenied` exception from AWS S3 or an `AuthorizationFailure` from Azure Blob Storage).^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Cause

The error is triggered when the Delta table property `delta.universalFormat.compatibility.location` is set to a path that the compute principal (e.g., the cluster’s instance profile or service principal) does not have permission to read or write. Common reasons include:

- The storage location does not exist or the principal lacks `LIST`/`READ` permissions on the bucket or container.
- The path points to a directory that exists but the principal’s credentials are not authorized for that bucket.
- The location uses a scheme or endpoint that the cluster is not configured to access (e.g., a different cloud provider region or a cross-account bucket without proper trust policies).

Because the `delta.universalFormat.compatibility.location` must be an **empty directory** that Delta Lake uses for compatibility output (e.g., Iceberg metadata), the engine checks that the directory is accessible before writing. If access is denied, the engine raises this sub-error.^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Resolution

To resolve the ACCESS_DENIED sub-error:

1. Verify that the compute principal (instance profile, service principal, or access key) has the necessary permissions on the storage location. For AWS S3, ensure the IAM role has `s3:GetBucketLocation`, `s3:ListBucket`, and `s3:PutObject` (if the directory needs to be created). For Azure, ensure the storage account firewall does not block the cluster’s IP and that the managed identity has `Storage Blob Data Contributor` or equivalent role.
2. Confirm that the location path is correct and uses the proper URI format (`s3://` or `wasbs://`).
3. If the location is a cross-account bucket, set up the appropriate bucket policy or trust relationship.
4. Test access by running a simple `ls` command on the location using the cluster’s credentials (e.g., `%fs ls "s3://my-bucket/path/"`).

After correcting the permissions, retry the operation that produced the error.^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION – The parent error condition that includes all sub-errors.
- [Delta Uniform Compatibility](/concepts/delta-uniform-compatibility-format.md) – The feature that requires this location to be set.
- [Delta Iceberg Compatibility](/concepts/delta-iceberg-table-feature-compatibility.md) – The primary use case for the compatibility location.
- Error conditions in Delta Lake – General guidance on Delta error handling.
- [Table property delta.universalFormat.compatibility.location](/concepts/deltauniversalformatcompatibilitylocation.md) – The property that triggers this check.

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
