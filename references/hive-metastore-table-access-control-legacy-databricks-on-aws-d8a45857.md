---
title: Hive metastore table access control (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/
ingestedAt: "2026-06-18T08:03:45.946Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Data governance (Unity Catalog)](https://docs.databricks.com/aws/en/data-governance/)
*   [Access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/)
*   Hive metastore table access control (legacy)

Last updated on **Jun 9, 2026**

Each Databricks workspace deploys with a built-in Hive metastore as a managed service. An instance of the metastore deploys to each cluster and securely accesses metadata from a central per-workspace repository.

By default, a cluster allows all users to access all data managed by the workspace's built-in Hive metastore unless table access control is enabled for that cluster. Table access control lets you programmatically grant and revoke access to objects in your workspace's Hive metastore from Python and SQL. When table access control is enabled, users can set permissions for data objects that are accessed using that cluster.

note

Hive metastore table access control is a legacy data governance model. Databricks recommends that you [upgrade the tables managed by the Hive metastore to the Unity Catalog metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate). Unity Catalog simplifies security and governance of your data by providing a central place to administer and audit data access across multiple workspaces in your account.

## Requirements[​](#requirements "Direct link to Requirements")

*   This feature requires the [Premium plan or above](https://databricks.com/product/pricing/platform-addons).
*   This feature requires a Data Science & Engineering cluster with an [appropriate configuration](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl#table-access-control) or a SQL warehouse.

This section covers:

*   [Enable Hive metastore table access control on a cluster (legacy)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl)
*   [Hive metastore privileges and securable objects (legacy)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges)
*   [What is the `ANY FILE` securable?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/any-file)
