---
title: Data quality monitoring | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/
ingestedAt: "2026-06-18T08:04:06.735Z"
---

Data quality monitoring helps you ensure the quality of all of your data assets in Unity Catalog. Data quality monitoring includes the following capabilities:

*   **Anomaly detection**. Anomaly detection enables scalable data quality monitoring with one click. It monitors all tables in a schema using intelligent scanning that prioritizes important tables and skips low-impact ones. Databricks automatically assesses data quality by analyzing historical data patterns to evaluate each table’s freshness and completeness. See [Anomaly detection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/).
*   **Data profiling**. Data profiling provides summary statistics of the data in a table. You can also use it to track the performance of GenAI apps, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. See [Data profiling](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/).

Data profiling was formerly known as Lakehouse Monitoring.

### Why use anomaly detection?[​](#why-use-anomaly-detection "Direct link to Why use anomaly detection?")

To draw useful insights from your data, you must have confidence in the quality of your data. Anomaly detection monitors enabled tables for _freshness_ and _completeness_.

**Freshness** refers to how recently a table has been updated. Anomaly detection analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale.

**Completeness** refers to the number of rows expected to be written to the table in the last 24 hours. Anomaly detection analyzes the historical row count, and based on this data, predicts a range of expected number of rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, a table is marked as incomplete.

### Why use data profiling?[​](#why-use-data-profiling "Direct link to Why use data profiling?")

Data profiling provides quantitative measures that help you track and confirm the quality and consistency of your data over time. Data profiling captures historical metrics of a table's data distribution or corresponding model's performance, which can be used for quick summary statistics. You can use these metrics to monitor a table and send alerts for changes.

Data profiling helps you answer questions like the following:

*   What does data integrity look like, and how does it change over time? For example, what is the fraction of null or zero values in the current data, and has it increased?
*   What does the statistical distribution of the data look like, and how does it change over time? For example, what is the 90th percentile of a numerical column? Or, what is the distribution of values in a categorical column, and how does it differ from yesterday?
*   Is there drift between the current data and a known baseline, or between successive time windows of the data?
*   What does the statistical distribution or drift of a subset or slice of the data look like?
*   How are ML model inputs and predictions shifting over time?
*   How is model performance trending over time? Is model version A performing better than version B?

In addition, data profiling lets you control the time granularity of observations and set up custom metrics.

Data quality monitoring **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables.
