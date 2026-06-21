---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6dda4d58630e98453db69c6a451f5ecfca7dfe5ace4b1920d4f59dc5bddbd663
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - langfuse-to-databricks-trace-export
    - LTE
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Langfuse-to-Databricks Trace Export
description: A configuration pattern that redirects Langfuse-instrumented OpenTelemetry spans to Databricks MLflow's OTLP endpoint instead of Langfuse's own servers, enabling trace storage in Unity Catalog tables.
tags:
  - observability
  - llm-tracing
  - databricks
timestamp: "2026-06-19T10:27:33.966Z"
---

---
title: Langfuse-to-Databricks Trace Export
summary: Workflow for routing Langfuse-instrumented OpenTelemetry traces to Databricks MLflow via the OTLP endpoint instead of Langfuse's own servers.
sources:
  - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:16:25.382Z"
updatedAt: "2026-06-18T12:16:25.382Z"
tags:
  - mlflow
  - langfuse
  - tracing
  - databricks
aliases:
  - langfuse-to-databricks-trace-export
  - LTE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Langfuse-to-Databricks Trace Export

**Langfuse-to-Databricks Trace Export** is the process of configuring the Langfuse observability SDK to send OpenTelemetry-based trace spans to the Databricks [MLflow](/concepts/mlflow.md) OTLP endpoint, where they are stored in [Unity Catalog](/concepts/unity-catalog.md) tables alongside other MLflow traces. This consolidation enables querying and comparing Langfuse-instrumented calls with traces from other frameworks in a single location, using Databricks SQL for analysis and applying Unity Catalog governance such as access controls and [lineage](/concepts/data-lineage.md). ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Requirements

Before setting up the export, the following are required:

- A Databricks workspace with the “OpenTelemetry on Databricks” preview enabled. See Manage Databricks previews.
- A new or existing [MLflow Experiment](/concepts/mlflow-experiment.md) to receive the traces.

## Setup Overview

The export is configured in a Databricks notebook using Python. The high‑level steps are:

1. Install required packages.
2. Disable Langfuse’s own trace collection by setting dummy environment variables.
3. Configure the Databricks connection using the workspace host and API token.
4. Link an MLflow experiment to a Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md).
5. Add a Databricks OTLP exporter to the OpenTelemetry `TracerProvider` that Langfuse initializes.
6. Run traced functions (decorated with `@observe()`) to produce spans.
7. View traces in the MLflow experiment UI under the **Traces** tab.

## Step‑by‑Step Instructions

### Step 1: Install packages

Install `langfuse`, `mlflow[databricks]`, and the OpenTelemetry exporter packages in the notebook:

```python
%pip install "langfuse>=3.14.5" "mlflow[databricks]>=3.10.0" opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
%restart_python
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Step 2: Disable Langfuse trace collection

To prevent traces from being sent to a Langfuse server, set `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, and `LANGFUSE_SECRET_KEY` to dummy values. Only the OTLP exporter configured later will receive the spans.

```python
import os
os.environ["LANGFUSE_HOST"] = "localhost"
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""
```

An alternative is to set `LANGFUSE_TRACING_ENABLED=False`. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Step 3: Configure Databricks connection

Retrieve the workspace host URL and API token. Inside a Databricks notebook, use the notebook context; outside a notebook, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` manually.

```python
context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
DATABRICKS_HOST = context.apiUrl().get().rstrip("/")
DATABRICKS_TOKEN = context.apiToken().get()
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Step 4: Link an experiment to Unity Catalog

Define the Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md), then link them to an MLflow experiment using `set_experiment_trace_location`. This tells Databricks where to store incoming traces.

```python
import mlflow
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location

CATALOG_NAME = "<UC_CATALOG_NAME>"
SCHEMA_NAME = "<UC_SCHEMA_NAME>"
EXPERIMENT_ID = "<EXPERIMENT_ID>"

trace_location = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name=CATALOG_NAME, schema_name=SCHEMA_NAME),
    experiment_id=EXPERIMENT_ID,
)
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Step 5: Add the Databricks OTLP exporter

Get the `TracerProvider` that Langfuse registered, then attach a `BatchSpanProcessor` with an `OTLPSpanExporter` pointing to the Databricks OTLP endpoint. The `X-Databricks-UC-Table-Name` header routes spans to the correct Unity Catalog table.

```python
from langfuse import get_client
from opentelemetry import trace as otel_trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

langfuse = get_client()
provider = otel_trace.get_tracer_provider()

databricks_exporter = OTLPSpanExporter(
    endpoint=f"{DATABRICKS_HOST}/api/2.0/otel/v1/traces",
    headers={
        "content-type": "application/x-protobuf",
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "X-Databricks-UC-Table-Name": trace_location.full_otel_spans_table_name,
    },
)

provider.add_span_processor(BatchSpanProcessor(databricks_exporter))
```

Because the Langfuse environment variables are set to dummy values, this processor is the only active exporter, and all spans are sent exclusively to Databricks. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Step 6: Run a traced function

Use Langfuse’s `@observe()` decorator to instrument functions. The decorator creates OpenTelemetry spans that the exporter forwards to Databricks.

```python
from langfuse import observe

@observe()
def my_llm_call(prompt: str) -> str:
    return f"Response to: {prompt}"

@observe()
def my_pipeline(user_input: str) -> str:
    result = my_llm_call(user_input)
    return result

my_pipeline("Hello, world!")
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Viewing Traces

After running the traced code, open the MLflow experiment in your Databricks workspace and click the **Traces** tab. The trace from the `my_pipeline` call appears there. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Benefits of Consolidating Traces on Databricks

- Query and compare Langfuse‑instrumented calls together with traces from other frameworks in a single place.
- Use Databricks SQL to analyze trace data at scale.
- Apply [Unity Catalog](/concepts/unity-catalog.md) governance such as access controls and [lineage](/concepts/data-lineage.md) to all traces.

## Next Steps

- [Store OpenTelemetry traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md) – Learn more about managing traces in Unity Catalog tables.
- View traces in the Databricks MLflow UI – Search and filter traces.
- Query OpenTelemetry traces stored in Unity Catalog – Use Databricks SQL to query trace data.
- [Search for traces by OTel span attributes](/concepts/span-attributes-and-search.md) – Find ingested Langfuse traces by OpenTelemetry span attributes.

## Related Concepts

- OpenTelemetry
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Langfuse
- OTLP Exporter
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Databricks SQL
- [Trace Storage in Unity Catalog](/concepts/mlflow-trace-storage-in-unity-catalog.md)

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
