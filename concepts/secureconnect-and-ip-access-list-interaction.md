---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e5fadc2c2c4d9c111c8440fca17bac293e10c8c9af6c4d1133113502e7e7645
  pageDirectory: concepts
  sources:
    - restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-and-ip-access-list-interaction
    - IP Access List Interaction and SecureConnect
    - SAIALI
  citations:
    - file: restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
title: SecureConnect and IP Access List Interaction
description: When SecureConnect is enabled on the provider side, the IP access list also enforces access to shared data storage; without SecureConnect, storage URLs are reachable from any client IP regardless of the IP access list.
tags:
  - delta-sharing
  - security
  - secureconnect
  - networking
timestamp: "2026-06-19T20:14:42.970Z"
---

# SecureConnect and IP Access List Interaction

In [Delta Sharing](/concepts/delta-sharing.md) using the [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md) (OpenSharing), data providers can assign IP access lists to restrict recipient access to shared data. The behavior of these IP access lists depends on whether the provider has [SecureConnect](/concepts/secureconnect.md) enabled. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Effect of SecureConnect on IP Access Lists

When SecureConnect is enabled for the provider, the IP access list enforces access restrictions on **shared data storage** in addition to the control‑plane interfaces. Without SecureConnect, storage URLs are reachable from any client IP, regardless of the IP access list. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

The IP access list always affects the following, regardless of SecureConnect:

- [OpenSharing OSS Protocol](/concepts/opensharing-protocol.md) REST API calls
- OpenSharing activation URL access (Databricks‑to‑Open sharing only)
- OpenSharing credential file download (Databricks‑to‑Open sharing only)

When SecureConnect is enabled, the list also controls access to the actual data storage locations where the shared data resides. This means a recipient whose IP address is not on the allow list cannot read the shared data files even if they possess valid credentials. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Key Properties

- The IP access list is independent of Workspace IP access lists. Only **allow lists** are supported. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]
- Each recipient can have up to 100 IP/CIDR entries. Only IPv4 addresses are supported. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Managing IP Access Lists

IP access lists can be assigned, viewed, and removed using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands. The required permissions are as follows:

- **Assign** when creating a recipient: `CREATE RECIPIENT` privilege.
- **Assign** to an existing recipient: recipient object owner.
- **Remove**: recipient object owner.
- **View**: [Metastore](/concepts/metastore.md) admin, user with `USE RECIPIENT` privilege, or recipient object owner.

For detailed steps, see the source article. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Audit Logging

The following operations generate audit logs related to IP access lists:

- Recipient management operations (create, update)
- Denial of access to OpenSharing OSS Protocol REST API calls
- Denial of access to OpenSharing activation URL (Databricks‑to‑Open sharing only)
- Denial of access to OpenSharing credential file download (Databricks‑to‑Open sharing only)

^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [SecureConnect](/concepts/secureconnect.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [OpenSharing Protocol](/concepts/opensharing-protocol.md)
- IP access lists
- [Recipient management](/concepts/recipient-lifecycle-management.md)
- Data provider

## Sources

- restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md](/references/restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws-665da518.md)
