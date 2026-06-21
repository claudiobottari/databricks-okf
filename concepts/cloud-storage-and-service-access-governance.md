---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47daedf96780cc8db8a2674d2c99244dd7940a03999dfd6cff6392d91ade2cbb
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cloud-storage-and-service-access-governance
    - Service Access Governance and Cloud Storage
    - CSASAG
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Cloud Storage and Service Access Governance
description: Unity Catalog provides storage credentials (for cloud storage authentication), external locations (storage path + credential pairs), service credentials (for external cloud services), and connections (for external databases and services), governing access to external resources.
tags:
  - unity-catalog
  - governance
  - cloud-storage
  - security
timestamp: "2026-06-19T23:16:39.770Z"
---

# Cloud Storage and Service Access Governance

**Cloud Storage and Service Access Governance** refers to the framework of securable objects, privileges, and access controls within [Unity Catalog](/concepts/unity-catalog.md) that govern authentication and authorization for external cloud storage systems and external cloud services.

## Overview

Within [Unity Catalog](/concepts/unity-catalog.md), the governance of cloud storage and service access is managed through specialized securable objects that store authentication information and control access to external resources. These objects exist directly under the [Metastore](/concepts/metastore.md)](/[Metastore](/concepts/metastore.md)) as part of the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Key Securable Objects

### Storage Credentials

A **[storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md)** is a securable object that stores the authentication information required to access a specific path in cloud storage. The stored authentication method depends on the cloud provider: an IAM role on AWS, a service principal on Azure, or a service account on GCP. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

Storage credentials are most commonly used as a building block for [external locations](#external-location), which pair a storage credential with a specific cloud storage path. A storage credential can also be used directly to create external tables. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

To create a storage credential, a user needs the `CREATE STORAGE CREDENTIAL` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### External Locations

An **[External location](/concepts/external-location.md)** is a securable object that pairs a storage credential with a cloud storage path. It governs access to a specific path in cloud storage. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

To create an [External location](/concepts/external-location.md), a user needs the `CREATE EXTERNAL LOCATION` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). After creating an [External location](/concepts/external-location.md), users need the `READ FILES` privilege to read files directly from the storage path, and the `WRITE FILES` privilege to write files. However, Databricks recommends managing cloud storage access through [volumes](#volume) and the `READ VOLUME` and `WRITE VOLUME` privileges rather than granting `READ FILES` and `WRITE FILES` directly on external locations. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Service Credentials

A **service credential** is a securable object that stores authentication information for accessing external cloud services. This differs from [storage credentials](#storage-credential), which govern access to cloud storage. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

To create a service credential, a user needs the `CREATE SERVICE CREDENTIAL` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). The `ACCESS` privilege allows a user to use the service credential to access an external service. `CREATE CONNECTION` on a service credential (combined with `CREATE CONNECTION` on the [Metastore](/concepts/metastore.md)) allows a user to create a connection to an external database using that credential. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Connections

A **connection** is a securable object that stores the endpoint and credentials needed to access an external system. Connections support the following scenarios: ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

- Query federation
- Catalog federation
- Managed ingestion
- JDBC access
- HTTP services

To create a connection, a user needs the `CREATE CONNECTION` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). If the connection uses a service credential, the user also needs `CREATE CONNECTION` on that service credential. The `USE CONNECTION` privilege allows a user to list and view connection details and use the connection for its supported scenario. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## External Metadata

An **external metadata** object is a securable object used to define custom [Data Lineage](/concepts/data-lineage.md) relationships for systems that operate outside of [Unity Catalog](/concepts/unity-catalog.md)'s native lineage tracking. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

To create an [External Metadata Object](/concepts/external-metadata-object.md), a user needs the `CREATE EXTERNAL METADATA` privilege on the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). To add or modify lineage relationships on the object, the user needs `MODIFY` on the [External Metadata Object](/concepts/external-metadata-object.md), plus the appropriate privileges on any [Unity Catalog](/concepts/unity-catalog.md) objects referenced in the relationship. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Access Control Model

All cloud storage and service access governance objects follow the [Unity Catalog](/concepts/unity-catalog.md) access control model, where privileges are granted to principals (users, service principals, or groups) on securable objects. The hierarchical permission model ensures that access to external resources is governed consistently with other data assets within the [Metastore](/concepts/metastore.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Related Concepts

- [Metastore](/concepts/metastore.md)
- [Storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md)
- Service credential
- [External location](/concepts/external-location.md)
- Connection
- [Unity Catalog](/concepts/unity-catalog.md)
- Data governance
- [External tables](/concepts/unity-catalog-external-table-conversion.md)
- [Volumes](/concepts/ucvolumedataset.md)

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
