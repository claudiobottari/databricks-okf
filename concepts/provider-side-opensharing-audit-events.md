---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dfd4925da10e59ed14c7577497fb99a5fecbc688e0ee938aae17943baca167b
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-side-opensharing-audit-events
    - POAE
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Provider-side OpenSharing Audit Events
description: Audit events visible to data providers in OpenSharing, including query result details for pre-signed URL shares and STS-token shares, and error messages for failed operations.
tags:
  - audit-logging
  - providers
  - delta-sharing
timestamp: "2026-06-18T14:28:58.345Z"
---

# Provider-side OpenSharing Audit Events

**Provider-side OpenSharing Audit Events** are the set of logged actions and metadata that a data provider can observe when recipients query shared data through [Delta Sharing](/concepts/delta-sharing.md)'s OpenSharing protocol. These events are recorded in the provider's audit log system table and enable monitoring of how, when, and by whom the provider's shared data is accessed.

## Overview

When a data recipient queries shared data through OpenSharing, the provider receives temporary read access to the underlying data via either pre-signed URLs or scoped-down STS tokens. Each of these access methods generates distinct audit log events on the provider side, allowing providers to monitor recipient activity. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Audit Log Events

### Pre-signed URL Shares

For pre-signed URL-based sharing, the provider audit logs record two key events after a recipient's query receives a response: `deltaSharingQueriedTableChanges` and `deltaSharingQueriedTable`. These events contain detailed information about what was shared, including file metadata and recipient identifiers. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### STS-token Shares

For STS-token-based sharing, the provider audit logs record `generateTemporaryTableCredentials` and `generateTemporaryVolumeCredentials` events. These logs include `request_params` fields that document the specific credentials, shares, tables, and recipients involved in the access. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Viewing Event Details

Providers can examine the `response.result` field of pre-signed URL events to see detailed information about shared data, including:

- File paths and sizes
- Table versions
- Number of records returned
- Recipient identifiers (hashed)
- Query metadata such as limit hints and partition filtering

For STS-token events, the `request_params` column provides details about:
- Recipient and share names
- Credential types
- Table metadata
- Storage paths

## Logged Errors

OpenSharing also records error events in the `response.error_message` field when recipient actions fail. Provider-side errors include:

- **Metastore configuration errors**: When OpenSharing is not enabled on the selected [Metastore](/concepts/metastore.md)
- **Resource existence errors**: When catalogs, tables, schemas, shares, or recipients do not exist
- **Permission errors**: When non-admin users attempt privileged operations
- **State errors**: When workspaces are no longer assigned to their [Metastore](/concepts/metastore.md)
- **Duplicate resource errors**: When recipients or shares already exist with the same name
- **Token rotation errors**: When attempting to rotate a recipient with active tokens

## Requirements

To access OpenSharing audit logs, an account admin must enable the audit log system table for the Databricks account. Non-admin users require explicit access to `system.access.audit` to read these logs. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) - The underlying data sharing protocol
- [OpenSharing](/concepts/opensharing.md) - The specific sharing protocol that generates these audit events
- [Recipient-side OpenSharing Audit Events](/concepts/recipient-side-opensharing-audit-events.md) - The corresponding events visible to data recipients
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) - The storage location for these events
- [Pre-signed URL Sharing](/concepts/pre-signed-url-sharing.md) - One of the two access methods for OpenSharing
- [STS Token Sharing](/concepts/sts-token-sharing.md) - The other access method for OpenSharing

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
