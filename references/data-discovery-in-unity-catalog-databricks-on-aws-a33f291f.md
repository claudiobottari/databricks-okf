---
title: Data discovery in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-discovery
ingestedAt: "2026-06-18T08:04:03.862Z"
---

Data discovery is the ability for users across your organization to find, understand, and trust data assets in the catalog. As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply, making it easier for users to locate the right data and assess its quality before using it.

note

This page covers admin-side data discovery features. For the user-facing experience of browsing and searching the catalog, see [Discover data](https://docs.databricks.com/aws/en/discover/).

The quality of admin-side metadata directly determines how useful the discovery experience is for users. When you establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence.

## Manage data discoverability[​](#manage-data-discoverability "Direct link to Manage data discoverability")

*   *   [Flag certified and deprecated data](https://docs.databricks.com/aws/en/data-governance/unity-catalog/certify-deprecate-data)
    *   Apply system tags to mark data assets as certified (trusted, meeting quality standards) or deprecated (outdated, unsuitable for new use). These signals appear inline in the workspace and influence how data surfaces in search.
*   *   [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/)
    *   Create controlled tag vocabularies that users can apply to catalog objects to organize and categorize data by topic, team, or domain. Governed tags make data browseable and filterable across the catalog.
