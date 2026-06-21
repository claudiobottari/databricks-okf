---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1af7f73f4d56285c8664476588de8baa5cbd9c4098565b509fbac2902f009d31
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-ownership-constraints
    - COC
    - Connection Ownership
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Connection Ownership Constraints
description: Rules governing SAP BDC connection ownership, including requirement for individual user owners and ownership transfer restrictions
tags:
  - security
  - governance
  - databricks
timestamp: "2026-06-18T14:52:56.536Z"
---

# Connection Ownership Constraints

**Connection Ownership Constraints** refer to the rules governing who can own a Databricks connection and how ownership can be transferred. These constraints ensure that connections are always owned by an identifiable individual user, not by a group or automated principal.

## Ownership Transfer Rules

Only the current connection owner or a [Metastore](/concepts/metastore.md) admin can update the owner of a connection. This restriction prevents unauthorized reassignment of connection ownership. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Owner Identity Restriction

The owner of a connection **must be an individual user**. Ownership cannot be transferred to a group or a service principal. This constraint ensures that there is always a specific person accountable for the connection’s lifecycle and permissions. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Connection Ownership](/concepts/connection-ownership-constraints.md) — The general concept of owning a Databricks connection.
- [Metastore Admin](/concepts/metastore-admin-role.md) — The role that can override ownership restrictions.
- Service Principal — A non-user identity that cannot own a connection under this constraint.
- [SAP Business Data Cloud Connector](/concepts/sap-business-data-cloud-bdc-connector.md) — The context in which these constraints are documented.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
