---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b5265f4e46252efca32dfa3b9741fba43deed9429bafb6b70ace028241a5bf9
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-request-approval-methods
    - ARAM
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: Access Request Approval Methods
description: "Two methods for approving requests: adding the requester to an existing group with privileges, or directly granting privileges to the principal."
tags:
  - unity-catalog
  - access-control
  - approval
timestamp: "2026-06-19T19:22:46.996Z"
---

# Access Request Approval Methods

**Access Request Approval Methods** are the mechanisms through which approvers can grant requested permissions to Unity Catalog securable objects when a user submits an access request. After an approver follows the notification link to review a request, they can choose from two distinct methods to fulfill the request. ^[manage-access-requests-databricks-on-aws.md]

## Overview

When a user requests access to an object in [Unity Catalog](/concepts/unity-catalog.md), the request is sent to configured [Access Request Destinations](/concepts/access-request-destinations.md). The approver receives a notification containing a link that opens a modal dialog in the Databricks workspace, displaying the requester, the target object, and the requested privileges. From this dialog, the approver can select one of two approval methods to grant access. ^[manage-access-requests-databricks-on-aws.md]

## Approval Methods

### Add Principal to Group(s)

The approver can add the requesting principal to one or more existing groups that already possess at least one of the requested privileges. This method leverages existing group-based permissions to grant access without modifying object-level privileges directly. ^[manage-access-requests-databricks-on-aws.md]

This approach is useful when:
- The organization uses Unity Catalog Groups to manage permissions
- The requested privileges align with an existing group's access profile
- The approver wants to maintain centralized permission management

### Grant Privileges to Principal

The approver can grant the requested privileges directly to the requesting principal on the target object. This method allows the approver to select specific privileges or use privilege presets. ^[manage-access-requests-databricks-on-aws.md]

**Privilege presets** include pre-configured collections of privileges, such as **Data Reader**, which grants a standard set of read-only permissions to a user. These presets simplify the approval process by bundling commonly assigned privileges together. ^[manage-access-requests-databricks-on-aws.md]

## Built-in Permission Validation

When an approver processes a request, the system automatically validates prerequisite privileges. For example, if a user requests `SELECT` on a table, the system checks that the user has `USE CATALOG` and `USE SCHEMA` on the parent [Catalog and Schema](/concepts/catalog-and-schema.md). If prerequisites are missing, the system generates additional requests that are routed to the parent objects' approvers. This validation applies to requests submitted on behalf of another user or group as well. ^[manage-access-requests-databricks-on-aws.md]

## Examples

Both approval methods are presented in the review modal after clicking the notification link:

- **Group-based approval**: The approver sees a list of groups with relevant privileges and can select one or more to add the requester to. The interface shows the group name and a checkbox for selection. ^[manage-access-requests-databricks-on-aws.md]
- **Privilege-based approval**: The approver sees the target object and requested privileges, and can grant them directly to the principal, optionally using privilege presets like **Data Reader**. ^[manage-access-requests-databricks-on-aws.md]

## Audit Trail

All access request approvals and destination configurations are recorded in the Databricks Audit Logs under "Request for access events." This provides a complete record of every access request and how it was resolved. ^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Access Request Destinations](/concepts/access-request-destinations.md) — Where access requests are sent for review
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The permission model for securable objects
- Unity Catalog Groups — Group-based permission management
- Manage Access Requests — Configuring and using the access request feature
- Databricks Audit Logs — Event logging for security and compliance

## Sources

- manage-access-requests-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
