---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75449554d32aa343ef3d1591c6c2529390a1e40213b4b6fe395a2844db54d4a8
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-request-destinations
    - ARD
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: Access Request Destinations
description: Configured endpoints (email, Slack, Teams, webhook, redirect URL) that receive privilege requests for Unity Catalog securable objects.
tags:
  - unity-catalog
  - access-control
  - governance
timestamp: "2026-06-19T19:21:29.963Z"
---

# Access Request Destinations

**Access Request Destinations** are configurations on Unity Catalog securable objects that determine where access privilege requests are routed when users request access from surfaces such as Catalog Explorer, the SQL editor, notebooks, AI/BI dashboards, or Genie Spaces. Administrators configure these destinations so that the right approvers receive and can act on requests. ^[manage-access-requests-databricks-on-aws.md]

## Types of Destinations

An access request destination can be any of the following: ^[manage-access-requests-databricks-on-aws.md]

| Destination | Description |
|-------------|-------------|
| Email address | Sends an email from `noreply@databricks.com` to the configured address. |
| Slack channel | Posts a message to a Slack channel. |
| Microsoft Teams channel | Posts a message to a Teams channel. |
| Webhook endpoint | Sends a JSON payload to a webhook URL. |
| Redirect URL | Redirects the user to an external access request system. |

If a redirect URL is configured, no other destination types can be set, and users are taken directly to the URL instead of seeing the in-product request form. ^[manage-access-requests-databricks-on-aws.md]

### Webhook JSON Payload Example

The webhook payload includes the requester, object, requested privileges, principal, and a link to approve the request: ^[manage-access-requests-databricks-on-aws.md]

```json
{
  "requesterName": "<first-name> <last-name> (<email>)",
  "objectName": "<catalog>.<schema>.<table>",
  "objectType": "Table",
  "privileges": "SELECT",
  "principalName": "<group-name>",
  "onBehalfOf": "<group-name>",
  "onBehalfOfType": "Group",
  "comment": "My team needs access to run queries on this table.",
  "databricksWorkspaceUrl": "https://<account>.databricks.com/..."
}
```

For integration with common tools, see [Send alerts to Jira](https://support.atlassian.com/security-and-access-policies/docs/send-alerts-to-jira/) and [How to Integrate Webhooks Into ServiceNow](https://www.servicenow.com/community/in-other-news/how-to-integrate-webhooks-into-servicenow/ba-p/2271745). ^[manage-access-requests-databricks-on-aws.md]

## How Destinations Work

Destinations can be configured on most Unity Catalog securable objects, including metastores, catalogs, schemas, tables, views, volumes, functions, models, storage credentials, service credentials, external locations, and connections. ^[manage-access-requests-databricks-on-aws.md]

Users can request access for one or more principals (themselves, service principals, other users, or groups). The request is sent to all configured destinations. If no destination is configured, users cannot request access to the object. ^[manage-access-requests-databricks-on-aws.md]

By default, objects do not have a configured destination. However, [Metastore](/concepts/metastore.md) and workspace admins can [enable default email destinations](#default-destinations) to deliver requests to the object owner even when no explicit destination is set. ^[manage-access-requests-databricks-on-aws.md]

### Destination Inheritance

Destinations are inherited through the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md). A destination configured at a higher level (e.g., a catalog) applies to all child objects that do not have their own destination. For example, if you configure a destination on a catalog, schemas and tables under that catalog inherit it unless they have an explicit override. ^[manage-access-requests-databricks-on-aws.md]

## Enable Default Email Destinations

Databricks recommends enabling default email destinations so that access requests are always delivered. When enabled: ^[manage-access-requests-databricks-on-aws.md]

- Requests for catalog objects are sent to the catalog owner's email.
- Requests for objects outside a catalog (e.g., external locations) are sent to the object owner's email.

To enable, you must be both a [Metastore](/concepts/metastore.md) admin and workspace admin: ^[manage-access-requests-databricks-on-aws.md]

1. Click your profile photo → **Settings**.
2. Click **Notifications**.
3. Turn on **Enable default email destinations for access requests in UC**.

## Configure Destinations

To configure access request destinations on an object, you must be the object owner, have the `MANAGE` privilege on the object, or be a [Metastore](/concepts/metastore.md) admin. ^[manage-access-requests-databricks-on-aws.md]

### For Existing Objects (Catalog Explorer)

1. Click **Catalog** in the sidebar.
2. Select the securable object.
3. Click the kebab menu → **Manage access request destinations**.
4. Select one or more email or external destinations, or configure a redirect URL.
5. Click **Update**. ^[manage-access-requests-databricks-on-aws.md]

### When Creating a Catalog

1. Click **Catalog** → **Create a catalog**.
2. Enter a name and click **Create catalog**.
3. In the configuration modal, under **Access Requests**, add, modify, or remove destinations. The catalog owner's email is included by default.
4. Click **Next** → **Save**. ^[manage-access-requests-databricks-on-aws.md]

Destinations can also be configured via the REST API or Terraform. ^[manage-access-requests-databricks-on-aws.md]

## Built-In Permission Validation

When a user requests a privilege like `SELECT`, Unity Catalog automatically checks prerequisite privileges (`USE CATALOG`, `USE SCHEMA`). Missing prerequisites generate additional requests routed to the parent objects' approvers. This validation also applies to requests submitted on behalf of another user or group. ^[manage-access-requests-databricks-on-aws.md]

## Approving an Access Request

To approve a request, the approver follows the link sent to the notification destination. The link opens a modal showing the requester, object, and requested privileges. The approver can then: ^[manage-access-requests-databricks-on-aws.md]

- **Add principal to group(s):** Add the requester to existing groups that have the needed privileges.
- **Grant privileges to principal:** Grant access directly, optionally using privilege presets like **Data Reader**.

All access requests and destination configuration changes are recorded in the audit log under [Request for access events](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#request-for-access-events). ^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Permissions Model](/concepts/unity-catalog-permissions-model.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Notification Destinations
- Privileges Reference
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)

## Sources

- manage-access-requests-databricks-on-aws.md
- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
