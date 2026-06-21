---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80b4c6aee8eed080f9fe1d5823d8b8ef1c622bbc14ab73235861e712dacec646
  pageDirectory: concepts
  sources:
    - restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-ip-access-list-lifecycle
    - RIALL
  citations:
    - file: restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient IP Access List Lifecycle
description: "The complete set of operations for managing IP access lists on recipients: assigning IPs/CIDRs at creation or to existing recipients, viewing the list, and removing entries, each with specific required permissions."
tags:
  - delta-sharing
  - administration
  - lifecycle
timestamp: "2026-06-19T20:14:40.913Z"
---

# Recipient IP Access List Lifecycle

The **Recipient IP Access List Lifecycle** describes the creation, modification, removal, and monitoring of IP address restrictions applied to recipients of data shared via the [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md). Data providers assign allow‑only IP access lists to control which client IP addresses can access shared data through [OpenSharing](/concepts/opensharing.md). These lists are independent of workspace-level IP Access Lists and apply only to OpenSharing endpoints. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Scope of Enforcement

The IP access list restricts access to the following:

- OpenSharing OSS Protocol REST API calls
- OpenSharing activation URL (Databricks‑to‑Open sharing only)
- OpenSharing credential file download

When the provider has [SecureConnect](/concepts/secureconnect.md) enabled, the IP access list also enforces access to shared data storage. Without SecureConnect, storage URLs are reachable from any client IP, regardless of the list. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Limits

Each recipient supports a maximum of 100 IP or CIDR values. A single CIDR range counts as one value. Only IPv4 addresses are supported. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Lifecycle Stages

### Assignment

A data provider can assign an IP access list to a recipient either at creation time or later in the recipient’s lifecycle.

- **Permissions required**:
  - When assigning during recipient creation: the `CREATE RECIPIENT` privilege.
  - When assigning to an existing recipient: ownership of the recipient object.

The assignment is performed via [Catalog Explorer](/concepts/catalog-explorer.md) or the Databricks Unity Catalog CLI. The provider adds individual IP addresses (e.g., `8.8.8.8`) or CIDR ranges (e.g., `8.8.8.4/10`). ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

### Removal

Recipients can have specific IP entries removed, or the entire list can be cleared. If all IP addresses are removed, the recipient can access shared data from any IP address.

- **Permissions required**: Ownership of the recipient object.

Removal is performed via Catalog Explorer or the CLI by deleting individual IP address entries. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

### Viewing

The current IP access list for a recipient can be viewed through Catalog Explorer, the CLI, or the `DESCRIBE RECIPIENT` SQL command.

- **Permissions required**: [Metastore](/concepts/metastore.md) admin, user with the `USE RECIPIENT` privilege, or ownership of the recipient object. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Audit Logging

The following operations generate audit log events related to recipient IP access lists:

- Recipient creation and update (including assignment or modification of the IP access list)
- Denial of access to:
  - Any OpenSharing OSS Protocol REST API call
  - The OpenSharing activation URL (Databricks‑to‑Open sharing only)
  - The OpenSharing credential file download

For instructions on enabling and reading these logs, see Audit and monitor data sharing. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [SecureConnect](/concepts/secureconnect.md)
- [Workspace IP Access Lists](/concepts/opensharing-ip-access-list.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Unity Catalog CLI
- Recipient Management
- [Audit Logging](/concepts/abac-policy-audit-logging.md)

## Sources

- restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md](/references/restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws-665da518.md)
