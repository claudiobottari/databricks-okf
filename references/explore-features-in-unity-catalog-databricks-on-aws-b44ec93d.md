---
title: Explore features in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/ui-uc
ingestedAt: "2026-06-18T08:10:48.064Z"
---

With Feature Engineering in Unity Catalog, all of the benefits of Unity Catalog are available for all feature tables, including the following:

*   Feature discovery. You can browse and search for features by feature table name, feature, comment, or tag.
*   Governance. Feature tables, functions, and models are all governed by Unity Catalog. When you train a model, it inherits permissions from the data it was trained on.
*   Lineage. When you create a feature table in Databricks, the data sources used to create the feature table are saved and accessible. For each feature in a feature table, you can also access the models, notebooks, jobs, and endpoints that use the feature.
*   Cross-workspace access. Feature tables, functions, and models are automatically available in any workspace that has access to the catalog.

You can use any Delta table in Unity Catalog that includes a primary key constraint as a feature table. For information about managing tables in Unity Catalog, including privileges, lineage, and tags, see [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

You can also explore and manage feature tables using the Features UI. To access the Features UI, click ![Feature Store Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAABRElEQVRIDWNUsHT6zzAAgGkA7ARbOWox3UKehRybVkztYzA31Ceo9cnzFwzpZfUM1+7ewVBL0ziWkZRg6K4rxbAUJMBIy+x0/9hesKWKVs5gGpmgqY+RLUJnExXH1IhTdIup6mN8cYpuMVE+jsguQteHlQ+KUy1VFaxy6IJU9TG64fj4WH0sIiDIMLe3lUFPUx2fXoZL128yJBdXM7z58B6vOmySWH1MjKUgw0AOA6klB2D1McynJp7BDG8/fsBqrjC/AMOZ7WsJhgpWzUBBrBbDFOOyFCSPTw6m/+T5izAmBo3XYgzVJArgyw1Y45hE88lSPmAWUzWo8cUperBQ1WJ8cYpuMd6gBmUZXACfHC49yOJYfQwqkUB5GZRPCQGQWnIAVh+DikFiDIQVmeRYTNMWCD4HYfUxPg3Ukhu1mFohSdAcAKHrUqbEeRf4AAAAAElFTkSuQmCC) **Features** in the sidebar. Select a catalog with the catalog selector to view all of the available feature tables in that catalog, along with the following metadata:

*   Who owns the feature table.
*   Online stores where the feature table has been published.
*   The last time a notebook or job wrote to the feature table.
*   Key-value tags added to the feature table.
*   Text comments describing the feature table.

![Feature store page](https://docs.databricks.com/aws/en/assets/images/feature-store-ui-uc-47543a1b45cc58e1c664e0caee10716f.png)

note

Any table managed by Unity Catalog that has a primary key is automatically a feature table and appears on this page. If you don't see a table on this page, see how to [add a primary key constraint on the table](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc#use-existing-uc-table).

## Search and browse for feature tables[​](#search-and-browse-for-feature-tables "Direct link to Search and browse for feature tables")

Use the search box to search for feature tables. To limit the search to a catalog, use the **Catalogs** selector. You can enter all or part of the name of a feature table, a feature, a comment, or a tag of the feature table. Search text is case-insensitive.

![Feature search example](https://docs.databricks.com/aws/en/assets/images/feature-search-example-uc-16dbd302e1a2dbbe8880e4a56cf27f98.png)

You can also use the tag selector to filter feature tables with a specific tag.

## Explore and manage feature tables with Catalog Explorer[​](#explore-and-manage-feature-tables-with-catalog-explorer "Direct link to Explore and manage feature tables with Catalog Explorer")

Click the feature table name to [explore and manage feature table in Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/).

## Find features and feature tables using Genie Code[​](#find-features-and-feature-tables-using-genie-code "Direct link to find-features-and-feature-tables-using-genie-code")

[Genie Code](https://docs.databricks.com/aws/en/genie-code/use-genie-code) can help you find features or feature tables. In your `/findTables` query, mention “features” or “feature tables”. For example, “/findTables features related to movie ratings” or “/findTables feature tables related to movie ratings”.
