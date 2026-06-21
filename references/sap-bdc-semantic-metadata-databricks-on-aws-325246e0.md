---
title: SAP BDC semantic metadata | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/semantic-metadata
ingestedAt: "2026-06-18T08:05:42.827Z"
---

This page describes the semantic metadata that automatically syncs from SAP Business Data Cloud (BDC) into Unity Catalog for mounted SAP BDC shares.

SAP table and column names can be difficult to read. For all mounted SAP BDC shares, semantic metadata is automatically ingested into Unity Catalog at the table level when a table is accessed, making the data more understandable and discoverable. Any changes made in SAP BDC are reflected in Unity Catalog.

SAP BDC is the source of truth for semantic metadata. Metadata synced from SAP BDC is read-only in Databricks. OpenSharing recipients of SAP BDC shares cannot directly access or query the semantic metadata.

note

If you don't see the latest metadata in Catalog Explorer, click **Refresh Table** to trigger ingestion.

## SAP semantic types ingested[​](#sap-semantic-types-ingested "Direct link to sap-semantic-types-ingested")

The following semantics from SAP BDC are ingested into Unity Catalog:

SAP BDC syncs governance tags in the `sap.PersonalData` namespace as [system governed tags](https://docs.databricks.com/aws/en/database-objects/tags#system-tags) on tables in Unity Catalog. These tags classify whether SAP BDC data contains personal or sensitive information.

important

Do not manually assign, modify, or delete tags in the `sap.*` namespace. These are system-reserved values that are automatically assigned by the Databricks system when SAP BDC shares are mounted. If you assign them manually, Databricks might clear or remove them later.

To govern access based on these tags, create attribute-based access control (ABAC) policies that reference them.

The following tags are synced. For more information about SAP personal data annotations, see the [SAP CSN Interop specification](https://sap.github.io/csn-interop-specification/spec-v1/extensions/personal-data#schema-definitions).

After you mount an SAP BDC share to a catalog, synced metadata is available across Databricks. Because SAP table and column names are often difficult to interpret, the synced comments, key constraints, and tags help you understand and work with SAP data more effectively.

*   **Catalog Explorer**: View comments, key constraints, and tags in the table and column details. You can filter columns by searching for the contents of their comments, making it easier to find relevant columns.
*   **SQL**: Use `DESCRIBE TABLE EXTENDED` to view table and column comments and key constraints. Query `INFORMATION_SCHEMA.TABLE_TAGS` to view SAP governance tags.
*   **Genie Spaces**: In a [Genie Space](https://docs.databricks.com/aws/en/genie/set-up) that includes SAP BDC tables, users can ask questions in natural language without needing to understand SAP naming conventions.
*   **Governance**: Use synced SAP [governance tags](https://docs.databricks.com/aws/en/admin/governed-tags/) in [ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) to control access to sensitive data.
*   **Audit logs**: Metadata sync events, including tag assignments, comment updates, and constraint changes, are recorded in [audit logs](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs). Use audit logs to track when SAP BDC metadata was ingested or updated in your catalog.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Create and manage the SAP Business Data Cloud (BDC) connector](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/create-connection)
*   [Apply tags to Unity Catalog securable objects](https://docs.databricks.com/aws/en/database-objects/tags)
*   [Attribute-based access control in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/)
*   [Audit and monitor data sharing](https://docs.databricks.com/aws/en/delta-sharing/audit-logs)
