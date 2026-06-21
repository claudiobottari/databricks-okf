---
title: Flag data as certified or deprecated | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/certify-deprecate-data
ingestedAt: "2026-06-18T08:03:56.322Z"
---

This page shows how to apply system tags to objects to mark them as certified or deprecated.

## Certification status system tag[​](#certification-status-system-tag "Direct link to Certification status system tag")

The certified status system tag allows users to label objects, such as catalogs, schemas, tables, dashboards, Genie Spaces, Databricks apps, and notebooks, with indicators of data quality or lifecycle status. It is a system-governed tag with two tag values: certified and deprecated. This helps organizations enforce governance, improve data discoverability, and increase trust in analytics and AI applications. The tag is displayed next to object names in the workspace, and influences how data appears in notebooks and the SQL editor.

The tag key is `system.certification_status` and there are two tag values:

*   `certified`: Indicates that a data asset has met internal standards for accuracy, completeness, and trust. Certified assets display a check mark in the workspace.
    
    ![Certified system tag.](https://docs.databricks.com/aws/en/assets/images/certified-tag-a4a7c7e9541215b1e10de1898bee158c.png)
    
*   `deprecated`: Warns that a data asset is outdated, no longer reliable, or should not be used in new workflows. Deprecated assets display a restricted icon in the workspace.
    
    ![Deprecated system tag.](https://docs.databricks.com/aws/en/assets/images/deprecated-tag-0cb9e54fc18b8af264227001799b3247.png)
    

## Supported object types[​](#supported-object-types "Direct link to Supported object types")

You can apply the certification status tag to the following objects:

*   Catalogs
*   Schemas
*   Tables
*   Views
*   Volumes
*   Functions
*   Registered models
*   Dashboards
*   Genie Spaces
*   Databricks Apps
*   Notebooks

## Permissions required[​](#permissions-required "Direct link to Permissions required")

You must have the ASSIGN permission on the `system.certification_status` governed tag to apply it to objects. See [Manage permissions on governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/manage-permissions).

To add tags to Unity Catalog securable objects, you must own the object or have all of the following privileges:

*   `APPLY TAG` on the object
*   `USE SCHEMA` on the object's parent schema
*   `USE CATALOG` on the object's parent catalog

## Assign certified or deprecated status to objects[​](#assign-certified-or-deprecated-status-to-objects "Direct link to Assign certified or deprecated status to objects")

You can assign certified or deprecated status to objects using either the workspace UI or SQL.

*   Workspace UI
*   SQL

1.  Navigate to a supported object.
    
2.  Click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) and select **Assign certification**.
    
3.  Select **Certified**, **Deprecated**, or **None**.
    
    ![Edit certification and deprecation.](https://docs.databricks.com/aws/en/assets/images/edit-certification-deprecation-bcde29b206c5e43bd859ec6f668b81ef.png)
    
4.  Click **Save**.
    

You can update or remove the status at any time.

## Search by certification status[​](#search-by-certification-status "Direct link to Search by certification status")

You can filter for certified or deprecated assets directly from the search page. In the **Search** field, use the `certificationStatus` keyword to query objects by their certification status.

note

Search using tags is not supported on dashboards, Genie Spaces, or Databricks apps.

For example, the following snippet returns only certified tables:

    type:table certificationStatus:certified

The following snippet returns only deprecated assets across supported object types:

    certificationStatus:deprecated

*   In the search filters, you can also select **Certified** or **Deprecated** from the **Certification status** filter menu.
    
    ![Search by certification status.](https://docs.databricks.com/aws/en/assets/images/search-certification-status-551865cf6048a0433b0084842eb3fcda.png)
    

note

It might take a few minutes for certification or deprecation updates to appear in search results.
