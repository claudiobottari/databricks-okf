---
title: Track and export serving endpoint health metrics to Prometheus and Datadog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/metrics-export-serving-endpoint
ingestedAt: "2026-06-18T08:12:03.237Z"
---

This article provides an overview of serving endpoint health metrics and shows how to use the metrics export API to export endpoint metrics to [Prometheus](https://prometheus.io/docs/introduction/overview/) and [Datadog](https://docs.datadoghq.com/api/latest/).

Endpoint health metrics measures infrastructure and metrics such as latency, request rate, error rate, CPU usage, memory usage, etc. This tells you how your serving infrastructure is behaving.

## Requirements[​](#requirements "Direct link to Requirements")

*   Read access to the desired endpoint and personal access token (PAT) which can be generated in **Settings** in the Databricks UI to access the endpoint.
    
*   An existing [model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) endpoint. You can validate this by checking the endpoint health with the following:
    
    Bash
    
        curl -n -X GET -H "Authorization: Bearer [PAT]" https://[DATABRICKS_HOST]/api/2.0/serving-endpoints/[ENDPOINT_NAME]
    
*   Validate the export metrics API:
    
    Bash
    
        curl -n -X GET -H "Authorization: Bearer [PAT]" https://[DATABRICKS_HOST]/api/2.0/serving-endpoints/[ENDPOINT_NAME]/metrics
    

## Serving endpoint metrics definitions[​](#serving-endpoint-metrics-definitions "Direct link to Serving endpoint metrics definitions")

## Prometheus integration[​](#prometheus-integration "Direct link to Prometheus integration")

note

Regardless of which type of deployment you have in your production environment, the scraping configuration should be similar.

The guidance in this section follows the Prometheus documentation to start a Prometheus service locally using docker.

1.  Write a `yaml` config file and name it `prometheus.yml`. The following is an example:
    
    YAML
    
        global:  scrape_interval: 1m  scrape_timeout: 10sscrape_configs:  - job_name: 'prometheus'    metrics_path: '/api/2.0/serving-endpoints/[ENDPOINT_NAME]/metrics'    scheme: 'https'    authorization:      type: 'Bearer'      credentials: '[PAT_TOKEN]'    static_configs:      - targets: ['dbc-741cfa95-12d1.dev.databricks.com']
    
2.  Start Prometheus locally with the following command:
    
    Bash
    
           docker run \   -p 9090:9090 \   -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \   prom/prometheus
    
3.  Navigate to `http://localhost:9090` to check if your local Prometheus service is up and running.
    
4.  Check the Prometheus scraper status and debug errors from: `http://localhost:9090/targets?search=`
    
5.  Once the target is fully up and running, you can query the provided metrics, like `cpu_usage_percentage` or `mem_usage_percentage`, in the UI.
    

## Datadog integration[​](#datadog-integration "Direct link to Datadog integration")

[Datadog](https://docs.datadoghq.com/) has a variety of agents that can be deployed in different environments.

For demonstration purposes, the following launches a Mac OS agent locally that scrapes the metrics endpoint in your Databricks host. The configuration for using other agents are in a similar pattern.

note

The preliminary set up for this example is based on the free edition.

Datadog also offers a Databricks integration that connects Datadog to your model serving endpoints to monitor endpoint metrics without code. See the Datadog documentation for how to connect your [model serving configuration](https://docs.datadoghq.com/integrations/databricks/?tab=driveronly#model-serving-configuration) to Datadog.

1.  Register a Datadog account.
    
2.  Install OpenMetrics integration in your [account dashboard](https://app.datadoghq.com/integrations), so Datadog can accept and process OpenMetrics data.
    
3.  Follow the [Datadog documentation](https://app.datadoghq.com/account/settings#agent/mac) to get your Datadog agent up and running. For this example, use the DMG package option to have everything installed including `launchctl` and `datadog-agent`.
    
4.  Locate your OpenMetrics configuration. For this example, the configuration is at `~/.datadog-agent/conf.d/openmetrics.d/conf.yaml.default`. The following is an example configuration `yaml` file.
    
    YAML
    
         instances:  - openmetrics_endpoint: https://[DATABRICKS_HOST]/api/2.0/serving-endpoints/[ENDPOINT_NAME]/metrics   metrics:   - cpu_usage_percentage:       name: cpu_usage_percentage       type: gauge   - mem_usage_percentage:       name: mem_usage_percentage       type: gauge   - provisioned_concurrent_requests_total:       name: provisioned_concurrent_requests_total       type: gauge   - request_4xx_count_total:       name: request_4xx_count_total       type: gauge   - request_5xx_count_total:       name: request_5xx_count_total       type: gauge   - request_count_total:       name: request_count_total       type: gauge   - request_latency_ms:       name: request_latency_ms       type: histogram   tag_by_endpoint: false   send_distribution_buckets: true   headers:     Authorization: Bearer [PAT]     Content-Type: application/openmetrics-text
    
5.  Start datadog agent using `launchctl start com.datadoghq.agent`.
    
6.  Every time you need to make changes to your config, you need to restart the agent to pick up the change.
    
    Bash
    
         launchctl stop com.datadoghq.agent launchctl start com.datadoghq.agent
    
7.  Check the agent health with `datadog-agent health`.
    
8.  Check agent status with `datadog-agent status`. You should be able to see a response like the following. If not, debug with the error message. Potential issues may be due to an expired PAT token, or an incorrect URL.
    
    Bash
    
         openmetrics (2.2.2) -------------------   Instance ID: openmetrics: xxxxxxxxxxxxxxxx [OK]   Configuration Source: file:/opt/datadog-agent/etc/conf.d/openmetrics.d/conf.yaml.default   Total Runs: 1   Metric Samples: Last Run: 2, Total: 2   Events: Last Run: 0, Total: 0   Service Checks: Last Run: 1, Total: 1   Average Execution Time : 274ms   Last Execution Date : 2022-09-21 23:00:41 PDT / 2022-09-22 06:00:41 UTC (xxxxxxxx)   Last Successful Execution Date : 2022-09-21 23:00:41 PDT / 2022-09-22 06:00:41 UTC (xxxxxxx)
    
9.  Agent status can also be seen from the UI at:[http://127.0.0.1:5002/](http://127.0.0.1:5002/).
    
    If your agent is fully up and running, you can navigate back to your Datadog dashboard to query the metrics. You can also create a monitor or alert based on the metric data:[https://app.datadoghq.com/monitors/create/metric](https://app.datadoghq.com/monitors/create/metric).
