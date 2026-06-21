---
title: "Phase 6: Design Delta Lake architecture | Databricks on AWS"
source: https://docs.databricks.com/aws/en/lakehouse-architecture/deployment-guide/delta-lake
ingestedAt: "2026-06-18T08:07:57.117Z"
---

In this phase, you design Delta Lake storage architecture and data organization patterns for your lakehouse.

## Design medallion architecture[​](#design-medallion-architecture "Direct link to design-medallion-architecture")

The medallion architecture organizes data into layers to improve data quality as it progresses through the pipeline. This pattern is fundamental to building a well-structured lakehouse.

In its simplest form, the medallion architecture consists of three layers: bronze layer (raw data), silver layer (refined data), and gold layer (business-ready data).

### Bronze layer (raw data)[​](#bronze-layer-raw-data "Direct link to bronze-layer-raw-data")

Ingest source data into the first layer of the lakehouse and persist it there. When all downstream data is created from the bronze layer, you can rebuild the subsequent layers from this layer if needed.

**Bronze layer characteristics**

*   **Source of truth**: Raw data exactly as it arrives from source systems.
*   **Minimal transformation**: Data stored in its original format (or converted to Delta for auditability).
*   **Immutable**: Data is append-only, never updated or deleted.
*   **Schema-on-read**: Flexible schema handling for diverse source systems.
*   **Audit trail**: For some applications (such as GDPR or regulated data), it may be appropriate to convert this layer to Delta format.

**Best practices for bronze layer**

*   Preserve all source data fields for complete auditability.
*   Use Unity Catalog volumes for landing raw files.
*   Implement incremental ingestion to avoid full reprocessing.
*   Partition by ingestion date for efficient data management.
*   Document data sources and ingestion schedules.

### Silver layer (refined data)[​](#silver-layer-refined-data "Direct link to silver-layer-refined-data")

The purpose of the second layer is to hold cleansed, refined, filtered, and aggregated data.

**Silver layer characteristics**

*   **Data quality**: Removes duplicates, handles missing values, enforces schema.
*   **Enrichment**: Joins data from multiple sources to create integrated datasets.
*   **Standardization**: Applies consistent data types, formats, and naming conventions.
*   **Business rules**: Implements validation rules and business logic.
*   **Serves analytics**: Foundation for reporting, dashboards, and machine learning.

**Best practices for silver layer**

*   Implement data quality checks and monitoring.
*   Use Unity Catalog managed tables for silver layer data.
*   Partition by business dimensions (for example, date, region, product).
*   Document transformation logic and business rules.
*   Establish SLAs for data freshness.

### Gold layer (business-ready data)[​](#gold-layer-business-ready-data "Direct link to gold-layer-business-ready-data")

The third layer is created around business or project needs. It provides a different view as data products to other business units or projects, preparing data around security needs (for example, anonymized data) or optimizing for performance (for example, pre-aggregated views).

**Gold layer characteristics**

*   **Business-specific**: Tailored to specific use cases and consumers.
*   **Performance-optimized**: Pre-aggregated, denormalized for fast queries.
*   **Access-controlled**: Implements row-level security and column masking.
*   **Consumer-ready**: Structured for BI tools, applications, and machine learning models.
*   **Data products**: Published as reusable datasets across the organization.

**Best practices for gold layer**

*   Create separate gold tables for different business units or use cases.
*   Use dynamic views for row-level and column-level security.
*   Implement predictive optimization for frequently queried tables.
*   Document data lineage from bronze through gold.
*   Publish data products through Unity Catalog with clear ownership.

### Landing zone consideration[​](#landing-zone-consideration "Direct link to landing-zone-consideration")

Pipelines in larger organizations often have an additional landing zone in the cloud. The landing zone receives raw files from external systems before ingestion into the bronze layer.

**Landing zone patterns**

*   **Cloud object storage**: S3, ADLS Gen2, or GCS buckets for file drops.
*   **Unity Catalog volumes**: Secure POSIX-style file access with Unity Catalog governance.
*   **Third-party access**: External systems can write directly to landing zones.
*   **Notification triggers**: Use event notifications to trigger ingestion pipelines.

For comprehensive medallion architecture guidance, see [What is the medallion lakehouse architecture?](https://docs.databricks.com/aws/en/lakehouse/medallion).

## Design data ingestion strategy[​](#design-data-ingestion-strategy "Direct link to design-data-ingestion-strategy")

Ingesting data into the bronze layer is the first step in the medallion architecture. Design your ingestion strategy based on data sources, volumes, and latency requirements.

### Ingestion methods[​](#ingestion-methods "Direct link to ingestion-methods")

**Lakeflow Connect**

Lakeflow Connect is a managed data ingestion service provided by Databricks that can regularly sync data from external sources into Databricks without writing a single line of code.

**Partner ingestion tools**

Tools such as Fivetran can also ingest data from sources not supported by Lakeflow Connect. Any such raw and unstructured data should be stored in Unity Catalog volumes (rather than external locations).

**Custom ingestion pipelines**

For complex transformation requirements or unsupported sources, build custom ingestion pipelines using Lakeflow Spark Declarative Pipelines or notebooks.

### Ingestion patterns[​](#ingestion-patterns "Direct link to ingestion-patterns")

**Batch ingestion**

*   Schedule regular data loads (for example, hourly, daily, weekly).
*   Best for large volumes of historical data.
*   Lower cost compared to streaming.
*   Acceptable latency for analytical workloads.

**Streaming ingestion**

*   Continuous data ingestion with low latency.
*   Use Lakeflow Spark Declarative Pipelines with Auto Loader for streaming file ingestion.
*   Best for real-time analytics and operational use cases.
*   Higher compute costs but fresh data.

**Change data capture (CDC)**

*   Capture and apply incremental changes from source systems.
*   Efficient for large tables with frequent updates.
*   Preserves data lineage and audit trail.
*   Supported by Lakeflow Connect and Lakeflow Spark Declarative Pipelines.

**Best practices for data ingestion**

*   Use Unity Catalog volumes for landing raw data before bronze ingestion.
*   Implement idempotent ingestion to handle retries safely.
*   Use Auto Loader for efficient file ingestion from cloud storage.
*   Configure retention policies for landing zone data.
*   Monitor ingestion pipelines for failures and data quality issues.

## Design table management strategy[​](#design-table-management-strategy "Direct link to design-table-management-strategy")

Tables and volumes can be created as managed or external. Understanding the trade-offs helps you design the right table strategy.

### Managed vs external tables[​](#managed-vs-external-tables "Direct link to managed-vs-external-tables")

**Managed tables and volumes**

Unity Catalog manages access to external tables and volumes from Databricks, but doesn't control underlying files or fully manage the storage location of those files. Managed tables and volumes, on the other hand, are fully managed by Unity Catalog and stored in a managed storage location associated with the containing schema.

Databricks recommends managed volumes and managed tables for most workloads because they simplify configuration, optimization, and governance. New features, such as predictive optimization and managed DR, are available only for managed tables.

**External tables and volumes**

The biggest difference with external is that managed tables do not offer the simple folder structure of `schema_name/table_name`, instead using an internal GUID-style folders. These folders should only be accessed via Unity Catalog.

**When to use external tables**

*   Data must remain in specific cloud storage paths for regulatory or compliance reasons.
*   External systems require direct file access to the data.
*   Sharing data with systems that cannot use OpenSharing.
*   Existing data that cannot be migrated to managed storage.

**Best practices for table management**

*   Use managed tables for all new lakehouse data (bronze, silver, gold).
*   Use managed volumes for landing zone and raw unstructured data.
*   Reserve external tables only for data that must remain in specific paths.
*   Document ownership and lifecycle policies for all tables.
*   Enable predictive optimization for frequently queried managed tables.

## Hub-and-spoke medallion design[​](#hub-and-spoke-medallion-design "Direct link to hub-and-spoke-medallion-design")

The hub-and-spoke design pattern can be combined with medallion architecture for enterprise deployments. This pattern centralizes shared data assets while allowing domain-specific data processing.

**Hub-and-spoke medallion characteristics**

*   **Data hub**: Ingests, curates, and manages organization-wide assets (for example, SAP data or general assets such as weather or financials). These can be considered source-linked data products.
*   **Data domains**: Each domain reads some of the hub-curated data products and also ingests and curates its own domain-specific raw data. Domains then produce domain-specific data products.
*   **Publishing models**
    *   **Centralized publishing**: Domains publish data products back to the hub for organization-wide consumption.
    *   **Distributed publishing**: Domains publish data products within their own catalogs for domain-specific use.

**Example hub-and-spoke medallion**

    Data Hub (Central)├── Bronze: Organization-wide raw data (SAP, financials, weather)├── Silver: Curated shared datasets└── Gold: Enterprise-wide data productsSales Domain├── Bronze: Sales-specific raw data + shared hub data├── Silver: Sales analytics datasets└── Gold: Sales data products (published to hub or domain)Engineering Domain├── Bronze: Engineering telemetry + shared hub data├── Silver: Engineering metrics└── Gold: Engineering dashboards (published within domain)

**Best practices for hub-and-spoke medallion**

*   Use the hub for organization-wide shared data that multiple domains consume.
*   Allow domains to ingest and curate their own domain-specific data.
*   Establish clear data product publishing policies (centralized vs distributed).
*   Use Unity Catalog catalogs to separate hub and domain data.
*   Use Databricks\-managed OpenSharing to share data products between hub and domains.

## Design data governance strategy[​](#design-data-governance-strategy "Direct link to design-data-governance-strategy")

Data governance ensures data quality, discoverability, and compliance across the lakehouse. Design governance strategies appropriate for your organization's maturity and requirements.

### Data quality strategy[​](#data-quality-strategy "Direct link to data-quality-strategy")

Regardless of the medallion architecture variant, data quality must improve as data progresses through the layers. Consequently, trust in the data will subsequently increase from a business perspective.

**Data quality tools**

*   **Constraints**: Ensure that the quality and integrity of data added to a table are automatically verified.
*   **Primary and foreign keys**: Encode relationships between fields in tables (informational, not enforced).
*   **Expectations**: Prevent data quality issues from trickling downstream (currently with Lakeflow Spark Declarative Pipelines, soon with all Unity Catalog tables).
*   **Lakehouse Monitoring**: Monitor the statistical properties and quality of the data in all tables in your account.

**Data quality best practices**

*   Implement data quality checks at bronze ingestion (for example, schema validation, null checks).
*   Enforce stricter quality rules as data moves to silver and gold.
*   Monitor data quality metrics and trends over time.
*   Define data quality SLAs for critical datasets.
*   Automate alerting for data quality violations.

### Avoid data silos[​](#avoid-data-silos "Direct link to avoid-data-silos")

Data movement, copy, and duplication take time and may decrease the quality of the data in the lakehouse, especially when it leads to data silos. To make the distinction clear between data copy vs. data silo, a standalone or throwaway copy of data is not harmful on its own. It is sometimes necessary to boost agility, experimentation, and innovation. When these copies become operational with downstream business data products dependent on them, they become data silos. These silos soon become out of sync, ultimately leading to a less trustworthy data lake.

**Best practices to avoid data silos**

*   Use Unity Catalog views and OpenSharing instead of copying data.
*   Establish a single source of truth for each dataset.
*   Discourage department-level data copies and duplicates.
*   Use Unity Catalog lineage to track data dependencies.
*   Retire redundant datasets regularly.

### Data catalog and discovery[​](#data-catalog-and-discovery "Direct link to data-catalog-and-discovery")

Unity Catalog provides data discovery and lineage for usability and data governance.

**Data discovery**

Users of all business areas, especially in a self-service model, need to be able to discover relevant data. Therefore, a lakehouse needs a data catalog that covers all business-relevant data. The primary goals of a data catalog are to:

*   Enable users to search for and discover datasets.
*   Provide metadata, descriptions, and documentation for datasets.
*   Show data lineage from source to consumption.
*   Display data quality metrics and freshness information.

**Data lineage**

Track the data lineage precisely so that users can explain how data arrived at their current shape and form. Unity Catalog automatically captures lineage for:

*   Table-to-table dependencies.
*   Notebook and job executions that read or write data.
*   Upstream source systems.
*   Downstream consumers and data products.

**Best practices for data catalog**

*   Add descriptions and tags to all catalogs, schemas, and tables.
*   Document data owners and subject matter experts.
*   Use Unity Catalog search to enable data discovery.
*   Review and update metadata regularly.
*   Use lineage to understand data dependencies before making changes.

## Delta Lake architecture recommendations[​](#delta-lake-architecture-recommendations "Direct link to delta-lake-architecture-recommendations")

**Recommended**

*   Use the medallion architecture to structure the data lake (bronze, silver, gold).
*   Use Unity Catalog managed tables for all lakehouse data (bronze through gold).
*   Use Unity Catalog volumes for landing zones and raw unstructured data.
*   Implement data quality checks at each layer (bronze, silver, gold).
*   Use Unity Catalog to enable data discovery and lineage tracking.
*   Enable predictive optimization for frequently queried managed tables.
*   Establish clear data product publishing policies for hub-and-spoke architectures.

**Avoid**

*   Don't create data silos by duplicating operational data across domains.
*   Don't use external tables unless data must remain in specific storage paths.
*   Don't skip bronze layer (always preserve raw data as source of truth).
*   Don't bypass data quality checks to meet delivery deadlines.
*   Don't allow unmanaged data sprawl without Unity Catalog governance.

## Phase 6 outcomes[​](#phase-6-outcomes "Direct link to Phase 6 outcomes")

After completing Phase 6, you should have:

*   Medallion architecture designed (bronze, silver, gold layers with clear purposes).
*   Data ingestion strategy defined (batch, streaming, or CDC based on requirements).
*   Table management strategy designed (managed vs external tables).
*   Hub-and-spoke medallion architecture evaluated (for multi-domain organizations).
*   Data quality strategy defined with appropriate checks at each layer.
*   Data governance policies established (for example, catalog, lineage, discovery).
*   Landing zone architecture designed (if required for external systems).
*   Data product publishing model defined (centralized, distributed, or hybrid).

**Next phase**: [Phase 7: Plan Infrastructure as Code approach](https://docs.databricks.com/aws/en/lakehouse-architecture/deployment-guide/iac)

**Implementation guidance**: For step-by-step instructions to implement your Delta Lake design, see [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/).
