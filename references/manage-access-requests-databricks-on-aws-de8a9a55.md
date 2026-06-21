---
title: Manage access requests | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/access-request-destinations
ingestedAt: "2026-06-18T08:04:42.874Z"
---

The Request access feature allows users to request privileges for securable objects in Unity Catalog. This page explains how to configure access request destinations as an administrator. These destinations determine where access requests are sent when users request access to data objects.

## What are access request destinations?[​](#what-are-access-request-destinations "Direct link to What are access request destinations?")

When users request access to an object in Unity Catalog (such as a table or view), the request is sent to one or more configured destinations. Destinations can be any of the following:

*   Email addresses
    
*   Slack channels
    
*   Microsoft Teams channels
    
*   Webhook endpoints
    
*   A redirect URL (to your organization's external access request system)
    
    Only one redirect URL can be configured per object. If a URL is set, no other destinations can be set and users are redirected to that URL instead of seeing the in-product request form.
    

## Request permissions right from where you work in Databricks[​](#request-permissions-right-from-where-you-work-in-databricks "Direct link to request-permissions-right-from-where-you-work-in-databricks")

After destinations are configured, users can request permissions from several in-product surfaces: Catalog Explorer, SQL editor and notebooks, AI/BI dashboards, and Genie Spaces.

### Catalog Explorer[​](#catalog-explorer "Direct link to Catalog Explorer")

Users with the `BROWSE` privilege can navigate the catalog tree, open an object's page, and request additional privileges (such as `SELECT`) from there. Users can also be sent a direct URL to an object's page and request access from the same surface, even without `BROWSE`.

![Catalog Explorer object page with a Request access affordance.](https://docs.databricks.com/aws/en/assets/images/catalog-explorer-rfa-b8e10916ba98d23a8c731dfe8fcba329.png)

When a query or command fails with an `INSUFFICIENT_PERMISSIONS` error, the error message includes a **Request access** option that pre-fills the request with the referenced tables. This works anywhere the error surfaces, including the SQL editor and notebooks.

![SQL query failing with an INSUFFICIENT\_PERMISSIONS error and a Request access affordance.](https://docs.databricks.com/aws/en/assets/images/permission-error-1cae5a0615d0ff21dcff9736408b7b43.png)

### AI/BI dashboards[​](#aibi-dashboards "Direct link to AI/BI dashboards")

When a dashboard runs without embedded credentials and a widget references datasets the viewer can't read, the widget surfaces a **Request access** modal for the missing datasets.

![AI/BI dashboard widget prompting the viewer to request access to missing datasets.](https://docs.databricks.com/aws/en/assets/images/dashboard-rfa-04c7b4e8da2fe6315bfd9f870c975a53.png)

### Genie Spaces[​](#genie-spaces "Direct link to Genie Spaces")

When a Genie Space references tables the user lacks permissions on, the space displays a `PERMISSION_DENIED` banner with a **Request access** modal for the inaccessible tables.

![Genie space with a Request access modal listing inaccessible tables.](https://docs.databricks.com/aws/en/assets/images/geniespace-rfa-b693db986178f3c5ef2746fe03c3fc23.png)

## How access request destinations work[​](#how-access-request-destinations-work "Direct link to How access request destinations work")

Access request destinations can be configured on most objects in Unity Catalog, including metastores, catalogs, schemas, tables, views, volumes, functions, models, storage credentials, service credentials, external locations, and connections.

When submitting a request, users can request access for one or more principals. This includes themselves, service principals, other users, or groups. The request is routed to the configured destinations.

If multiple destinations are configured, the request is sent to all of them. If no destination is configured, users cannot request access to the object. By default, objects do not have a configured destination. However, as a metastore admin and workspace admin, you can [enable default email destinations](#default-destinations) to deliver access requests to the appropriate owner, even when no destination is explicitly configured.

If a redirect URL is configured, users are taken to the URL and do not see the access request form. Workspace admins can configure external destinations by following the instructions in [Manage notification destinations](https://docs.databricks.com/aws/en/admin/workspace-settings/notification-destinations).

### Destination inheritance behavior[​](#destination-inheritance-behavior "Direct link to Destination inheritance behavior")

When you configure a destination at higher levels of the Unity Catalog object hierarchy, it also applies to all child objects that don't already have a destination. For example, if you configure a destination on a catalog, this destination is inherited by all schemas and objects under the catalog, except for those that already have a destination.

![Access request destination inheritance example](https://docs.databricks.com/aws/en/assets/images/rfa-destination-inheritance-17adc9489357e4d5effff29172068e49.png)

## Enable default email destinations[​](#enable-default-email-destinations "Direct link to enable-default-email-destinations")

Databricks recommends enabling default email destinations. This ensures that access requests are delivered even when no destination is manually configured. When enabled, requests for catalog objects are sent to the catalog owner's email address, and requests for objects outside a catalog, such as external locations, are sent to the object owner's email address.

tip

Enabling default email destinations ensures that access requests are delivered even when no destination is manually configured for an object. This is the fastest way to start receiving and responding to requests across your Unity Catalog metastore.

To enable default destinations, you must be both a metastore admin and workspace admin.

1.  In the upper-right corner of your workspace, click your profile photo and select **Settings**.
2.  Click **Notifications**.
3.  Turn on **Enable default email destinations for access requests in UC**.

## Configure access request destinations on an object[​](#configure-access-request-destinations-on-an-object "Direct link to configure-access-request-destinations-on-an-object")

To configure access request destinations on an object, you must either be the object owner, have the `MANAGE` privilege on the object, or be a metastore admin.

You can configure destinations using Catalog Explorer, the REST API, or Terraform.

### Configure destinations for existing objects[​](#configure-destinations-for-existing-objects "Direct link to configure-destinations-for-existing-objects")

*   Catalog Explorer
*   REST API
*   Terraform

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Select a securable object.
    
3.  Click the ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) kebab menu and select **Manage access request destinations**.
    
4.  Select one or more email or external destinations, or configure a redirect URL. If a URL is selected, no other destination types can be added.
    
    ![Configure an access request destination.](https://docs.databricks.com/aws/en/assets/images/access-request-destinations-fcf640aa2a901cc0cee52dc40c93c44a.png)
    
5.  Click **Update**.
    

### Configure destinations when creating a catalog[​](#configure-destinations-when-creating-a-catalog "Direct link to configure-destinations-when-creating-a-catalog")

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Click the ![Plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik03LjI1IDcuMjVWMUg4Ljc1VjcuMjVIMTVWOC43NUg4Ljc1VjE1SDcuMjVWOC43NUgxVjcuMjVINy4yNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) plus icon. Then, click **Create a catalog**.
3.  Enter a name for your catalog, then click **Create catalog**.
4.  In the next modal, click **Configure catalog**.
5.  Under the **Access Requests** section, add, modify, or remove destinations as necessary. The email of the catalog owner is included as a destination by default.

![Configure an access request destination for a new catalog.](https://docs.databricks.com/aws/en/assets/images/rfa-destination-create-catalog-bf3c6600dcfb583f7086213448d6787c.png)

1.  Click **Next**, then click **Save**.

Destinations are inherited in the Unity Catalog object hierarchy. When creating a schema within a catalog that has an access request destination, the **Create a new schema** modal mentions the inherited destinations:

![Access request destinations listed in new schema modal](https://docs.databricks.com/aws/en/assets/images/rfa-destination-create-schema-d739da27014f764fc1810d70a8bf896f.png)

To modify these destinations on the schema, see [Configure destinations for existing objects](#configure-rfa-existing).

## Access request examples[​](#access-request-examples "Direct link to Access request examples")

The following section shows examples for access requests sent to different destinations.

### Email[​](#email "Direct link to Email")

Access request emails are sent from `noreply@databricks.com`.

![Request for access email destination.](https://docs.databricks.com/aws/en/assets/images/email-request-for-access-14417fed9df2a52c712bcb04433ad677.png)

### Slack[​](#slack "Direct link to Slack")

![Request for access Slack destination.](https://docs.databricks.com/aws/en/assets/images/slack-request-for-access-0870cd91e598ee64b81398b543a57596.png)

### Webhook (JSON)[​](#webhook-json "Direct link to Webhook (JSON)")

JSON

    {  "requesterName": "<first-name> <last-name> (<email>)",  "objectName": "<catalog>.<schema>.<table>",  "objectType": "Table",  "privileges": "SELECT",  "principalName": "<group-name>",  "onBehalfOf": "<group-name>",  "onBehalfOfType": "Group",  "comment": "My team needs access to run queries on this table.",  "databricksWorkspaceUrl": "https:/<account>.databricks.com/explore/data/<catalog>/<schema>/<table>?o=<table-id>&activeTab=permissions&showGrantModal=true&requestedPrivileges=SELECT&groupId=<group-id>"}

For information on how to integrate webhooks with common tools, see the following:

*   [Send alerts to Jira](https://support.atlassian.com/security-and-access-policies/docs/send-alerts-to-jira/).
*   [How to Integrate Webhooks Into ServiceNow](https://www.servicenow.com/community/in-other-news/how-to-integrate-webhooks-into-servicenow/ba-p/2271745)

## Built-in permission validation[​](#built-in-permission-validation "Direct link to Built-in permission validation")

*   Prerequisite privileges (`USE CATALOG`, `USE SCHEMA`) are checked automatically when a user requests a privilege like `SELECT`.
*   Missing prerequisites generate additional requests routed to the parent objects' approvers.
*   Validation also applies to requests submitted on behalf of another user or group.

## Approve an access request[​](#approve-an-access-request "Direct link to approve-an-access-request")

To approve an access request, follow the link sent to your access request notification. The link opens a modal dialog in your workspace that displays the requester, object, and requested privileges.

![Review a request for access.](https://docs.databricks.com/aws/en/assets/images/review-access-request-64a4310ff4acbaf02bc9216b400530a6.png)

Next, select one of the following approval methods:

*   **Add principal to group(s)** to add the requester to one or more existing groups that have at least one of the requested privileges.
    
    ![Grant a request for access using a group.](https://docs.databricks.com/aws/en/assets/images/grant-using-group-adfdd71bda25898a4b7b16cd4b5865f8.png)
    
*   **Grant privileges to principal** to give them access to the object directly. You can also select privilege presets, such as **Data Reader** to grant a user a collection of privileges.
    
    ![Grant a request for access using privileges.](https://docs.databricks.com/aws/en/assets/images/grant-using-preset-dd71916f307a3002e13a3af2815af62a.png)
    

For a record of every access request and destination configuration, see [Request for access events](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#request-for-access-events) in the audit log reference.
