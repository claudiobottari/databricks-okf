---
title: Audit and monitor data sharing | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/audit-logs
ingestedAt: "2026-06-18T08:05:15.492Z"
---

This article describes how data providers and recipients can use audit logs to monitor OpenSharing events. Provider audit logs record actions taken by the provider and actions taken by recipients on the provider's shared data. Recipient audit logs record events related to the accessing of shares and the management of provider objects.

## Requirements[​](#requirements "Direct link to Requirements")

To access audit logs, an account admin must enable the audit log system table for your Databricks account. See [Enable system tables](https://docs.databricks.com/aws/en/admin/system-tables/#enable). For information on the audit log system table, see [Audit log system table reference](https://docs.databricks.com/aws/en/admin/system-tables/audit-logs).

If you are not an account admin or metastore admin, you must be given access to `system.access.audit` to read audit logs.

## View OpenSharing events in the audit log[​](#view-opensharing-events-in-the-audit-log "Direct link to view-opensharing-events-in-the-audit-log")

If your account has system tables enabled, audit logs are stored in `system.access.audit`. If, alternatively, your account has an [audit log delivery setup](https://docs.databricks.com/aws/en/admin/account-settings/audit-log-delivery), you need to know the bucket and path where the logs are delivered.

## Logged events[​](#logged-events "Direct link to Logged events")

To view the list of OpenSharing audit log events, see [OpenSharing events](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#ds).

## View details of a recipient's query result[​](#view-details-of-a-recipients-query-result "Direct link to view-details-of-a-recipients-query-result")

OpenSharing supports sharing asset types such as tables, views, materialized views, streaming ables, and volumes. OpenSharing provides temporary read access to the underlying data from either pre-signed URLs or from scoped-down STS tokens. The following table outlines how the sharing type corresponds to the logged audit log events:

### View details about pre-signed URL shares[​](#view-details-about-pre-signed-url-shares "Direct link to View details about pre-signed URL shares")

In the provider logs, the events `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable` are logged after a data recipient's query gets a response for pre-signed URL-based sharing. Providers can view the `response.result` field of these logs to see more details about what was shared with the recipient. The field can include the following values. This list is not exhaustive.

JSON

    "checkpointBytes": "0","earlyTermination": "false","maxRemoveFiles": "0","path": "file: example/s3/path/golden/snapshot-data0/_delta_log","deltaSharingPartitionFilteringAccessed": "false","deltaSharingRecipientId": "<redacted>","deltaSharingRecipientIdHash": "<recipient-hash-id>","jsonLogFileNum": "1","scannedJsonLogActionNum": "5","numRecords": "3","deltaSharingRecipientMetastoreId": "<redacted>","userAgent": "Delta-Sharing-Unity-Catalog-Databricks-Auth/1.0 Linux/4.15.0-2068-azure-fips OpenJDK_64-Bit_Server_VM/11.0.7+10-jvmci-20.1-b02 java/11.0.7 scala/2.12.15 java_vendor/GraalVM_Community","jsonLogFileBytes": "2846","checkpointFileNum": "0","metastoreId": "<redacted>","limitHint": "Some(1)","tableName": "cookie_ingredients","tableId": "1234567c-6d8b-45fd-9565-32e9fc23f8f3","activeAddFiles": "2", // number of AddFiles returned in the query"numAddFiles": "2", // number of AddFiles returned in the query"numAddCDCFiles": "2", // number of AddFiles returned in the CDF query"numRemoveFiles": "2", // number of RemoveFiles returned in the query"numSeenAddFiles": "3","scannedAddFileSize": "1300", // file size in bytes for the AddFile returned in the query"scannedAddCDCFileSize": "1300", // file size in bytes for the AddCDCFile returned in the CDF query"scannedRemoveFileSize": "1300", // file size in bytes for the RemoveFile returned in the query"scannedCheckpointActionNum": "0","tableVersion": "0"

### View details about STS-token shares[​](#view-details-about-sts-token-shares "Direct link to View details about STS-token shares")

In the provider logs, the events `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` are logged after a data recipient's query gets a response for STS-token-based sharing. Providers can view the `request_params` column of these logs to see more details about what was shared with the recipient. The field can include the following values. This list is not exhaustive.

JSON

    "recipient_name": "someRecipientName""share_id": "ea7a4555-43d9-4cbd-a5df-f4f5193f297e""credential_type": "StorageCredential""is_permissions_enforcing_client": "true""table_full_name": "someTableName""operation": "READ""share_name": "someShareName""table_id": "someTableId""share_owner": "someShareOwner""recipient_id": "someRecipientId""table_url": "s3://somePath""metastore_id": "someMetastoreId"

## Logged errors[​](#logged-errors "Direct link to Logged errors")

If an attempted OpenSharing action fails, the action is logged with the error message in the `response.error_message` field of the log. Items between `<` and `>` characters represent placeholder text.

### Error messages in provider logs[​](#error-messages-in-provider-logs "Direct link to Error messages in provider logs")

OpenSharing logs the following errors for data providers:

*   OpenSharing is not enabled on the selected metastore.
    
        DatabricksServiceException: FEATURE_DISABLED:Delta Sharing is not enabled
    
*   An operation was attempted on a catalog that does not exist.
    
        DatabricksServiceException: CATALOG_DOES_NOT_EXIST:Catalog '<catalog>' does not exist.
    
*   A user who is not an account admin or metastore admin attempted to perform a privileged operation.
    
        DatabricksServiceException: PERMISSION_DENIED:Only administrators can <operation-name> <operation-target>
    
*   An operation was attempted on a metastore from a workspace to which the metastore is not assigned.
    
        DatabricksServiceException: INVALID_STATE:Workspace <workspace-name> is no longer assigned to this metastore
    
*   A request was missing the recipient name or share name.
    
        DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare Missing required field: <recipient-name>/<share-name>
    
*   A request included an invalid recipient name or share name.
    
        DatabricksServiceException: INVALID_PARAMETER_VALUE: CreateRecipient/CreateShare <recipient-name>/<share-name> is not a valid name
    
*   A user attempted to share a table that is not in a Unity Catalog metastore.
    
        DatabricksServiceException: INVALID_PARAMETER_VALUE: Only managed or external table on Unity Catalog can be added to a share
    
*   A user attempted to rotate a recipient that was already in a rotated state and whose previous token had not yet expired.
    
        DatabricksServiceException: INVALID_PARAMETER_VALUE: There are already two active tokens for recipient <recipient-name>
    
*   A user attempted to create a new recipient or share with the same name as an existing one.
    
        DatabricksServiceException: RECIPIENT_ALREADY_EXISTS/SHARE_ALREADY_EXISTS: Recipient/Share <name> already exists`
    
*   A user attempted to perform an operation on a recipient or share that does not exist.
    
        DatabricksServiceException: RECIPIENT_DOES_NOT_EXIST/SHARE_DOES_NOT_EXIST: Recipient/Share '<name>' does not exist
    
*   A user attempted to add a table to a share, but the table had already been added.
    
        DatabricksServiceException: RESOURCE_ALREADY_EXISTS: Shared Table '<name>' already exists
    
*   A user attempted to perform an operation that referenced a table that does not exist.
    
        DatabricksServiceException: TABLE_DOES_NOT_EXIST: Table '<name>' does not exist
    
*   A user attempted to perform an operation that referenced a schema that did not exist.
    
        DatabricksServiceException: SCHEMA_DOES_NOT_EXIST: Schema '<name>' does not exist
    
*   A user attempted to access a share that does not exist.
    
        DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.
    

### Error messages in recipient logs[​](#error-messages-in-recipient-logs "Direct link to Error messages in recipient logs")

OpenSharing logs the following errors for data recipients:

*   The user attempted to access a share they do not have permission to access.
    
        DatabricksServiceException: PERMISSION_DENIED:User does not have SELECT on Share <share-name>
    
*   The user attempted to access a share that does not exist.
    
        DatabricksServiceException: SHARE_DOES_NOT_EXIST: Share <share-name> does not exist.
    
*   The user attempted to access a table that does not exist in the share.
    
        DatabricksServiceException: TABLE_DOES_NOT_EXIST: <table-name> does not exist.
