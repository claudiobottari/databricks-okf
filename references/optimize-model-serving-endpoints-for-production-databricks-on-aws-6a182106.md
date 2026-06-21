---
title: Optimize Model Serving endpoints for production | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/production-optimization
ingestedAt: "2026-06-18T08:12:23.040Z"
---

Learn how to optimize Model Serving endpoints for production workloads that require high throughput, low latency, and reliable performance.

Optimization strategies fall into three categories:

*   [**Endpoint optimizations**](#infrastructure): Configure endpoint infrastructure for better performance
*   [**Model optimizations**](#model): Improve model efficiency and throughput
*   [**Client optimizations**](#client): Optimize how clients interact with serving endpoints

## When to optimize your endpoint[​](#when-to-optimize-your-endpoint "Direct link to When to optimize your endpoint")

Consider optimizing your Model Serving endpoint when you encounter any of the following scenarios:

*   **High query volume**: Your application sends more than 50k queries per second (QPS) to a single endpoint
*   **Latency requirements**: Your application requires sub-100ms response times
*   **Scaling bottlenecks**: Endpoints experience queuing or return HTTP 429 errors during traffic spikes
*   **Cost optimization**: You want to reduce serving costs while maintaining performance targets
*   **Production preparation**: You're preparing to move from development to production workloads

## Infrastructure optimizations[​](#-infrastructure-optimizations "Direct link to -infrastructure-optimizations")

Infrastructure optimizations improve network routing, scaling behavior, and compute capacity.

### Route optimization[​](#route-optimization "Direct link to Route optimization")

[Route optimization](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization) provides the most significant infrastructure improvement for high-throughput workloads. When you enable route optimization on an endpoint, Databricks Model Serving improves the network path for inference requests, resulting in faster, more direct communication between clients and models.

**Performance benefits:**

**When to use route optimization:**

*   Workloads requiring more than 200 QPS
*   Applications with strict latency requirements (sub-50ms overhead)
*   Production deployments serving multiple concurrent users

important

Route optimization is only available for custom model serving endpoints. Foundation Model APIs and external models do not support route optimization. OAuth tokens are required for authentication; personal access tokens are not supported.

See [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization) for setup instructions and [Query route-optimized serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization) for querying details.

### Provisioned concurrency[​](#provisioned-concurrency "Direct link to Provisioned concurrency")

Provisioned concurrency controls how many simultaneous requests your endpoint can process. Configure provisioned concurrency based on your expected QPS and latency requirements.

**Configuration guidelines:**

*   **Minimum concurrency**: Set high enough to handle baseline traffic without queuing
*   **Maximum concurrency**: Set high enough to accommodate traffic spikes while controlling costs
*   **Autoscaling**: Enable autoscaling to dynamically adjust capacity based on demand

**Calculate required concurrency:**

    Required Concurrency = Target QPS × Average Latency (seconds)

For example, if your target is 100 QPS with 200ms average latency:

    Required Concurrency = 100 × 0.2 = 20

Use [load testing](https://docs.databricks.com/aws/en/machine-learning/model-serving/what-is-load-test) to measure actual latency and determine optimal concurrency settings.

### Instance types[​](#instance-types "Direct link to Instance types")

Choose instance types based on your model's compute requirements:

tip

Start with CPU instances for development and testing. Switch to GPU instances only if you observe high inference latency or your model requires specialized compute (such as deep learning operations).

## Model optimizations[​](#model-optimizations "Direct link to model-optimizations")

Model optimizations improve inference speed and resource efficiency.

### Model size and complexity[​](#model-size-and-complexity "Direct link to Model size and complexity")

Model Size and Complexity: Smaller, less complex models generally lead to faster inference times and higher QPS. Consider techniques like model quantization or pruning if your model is large.

### Batching[​](#batching "Direct link to Batching")

If your application can send multiple requests in a single call, enable batching at the client side. This can significantly reduce the overhead per prediction.

### Pre-processing and post-processing optimization[​](#pre-processing-and-post-processing-optimization "Direct link to Pre-processing and post-processing optimization")

Offload complex pre-processing and post-processing from serving endpoints to reduce load on inference infrastructure.

## Client-side optimizations[​](#client-side-optimizations "Direct link to client-side-optimizations")

Client-side optimizations improve how applications interact with serving endpoints.

### Connection pooling[​](#connection-pooling "Direct link to Connection pooling")

Connection pooling reuses existing connections instead of creating new connections for each request, significantly reducing overhead.

*   Use the Databricks SDK, which automatically implements connection pooling best practices
*   If using custom clients, implement connection pooling yourself.

### Error handling and retry strategies[​](#error-handling-and-retry-strategies "Direct link to Error handling and retry strategies")

Implement robust error handling to gracefully handle temporary failures, especially during autoscaling events or network disruptions.

### Payload size optimization[​](#payload-size-optimization "Direct link to Payload size optimization")

Minimize request and response payload sizes to reduce network transfer time and improve throughput.

## Measure and improve performance[​](#measure-and-improve-performance "Direct link to Measure and improve performance")

### Performance monitoring[​](#performance-monitoring "Direct link to Performance monitoring")

Monitor endpoint performance using the tools provided by Model Serving:

See [Monitor model quality and endpoint health](https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints) for detailed monitoring guidance and [Track and export serving endpoint health metrics to Prometheus and Datadog](https://docs.databricks.com/aws/en/machine-learning/model-serving/metrics-export-serving-endpoint) for exporting metrics to observability tools.

### Load testing[​](#load-testing "Direct link to Load testing")

Load testing measures endpoint performance under realistic traffic conditions and helps you:

*   Determine optimal provisioned concurrency settings
*   Identify performance bottlenecks
*   Validate latency and throughput requirements
*   Understand the relationship between client concurrency and server concurrency

See [Load testing for serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/what-is-load-test).

## Troubleshoot common performance issues[​](#troubleshoot-common-performance-issues "Direct link to Troubleshoot common performance issues")

### Queuing[​](#queuing "Direct link to Queuing")

Model Serving supports autoscaling to adjust capacity based on traffic patterns. However, sudden traffic surges can cause queuing because autoscaling requires time to detect increased load and provision additional capacity. During this period, incoming requests may temporarily exceed available capacity, causing requests to queue.

Queuing occurs when the request rate or concurrency surpasses the endpoint's current processing capacity. This typically happens during sharp traffic spikes, workload bursts, or when the endpoint has insufficient provisioned concurrency. Model Serving endpoints allow temporary queuing to handle bursts, but beyond a defined threshold, the endpoint returns HTTP 429 (Too Many Requests) errors to protect system stability.

Queuing increases latency because queued requests wait before being processed. To minimize queuing:

*   Set minimum provisioned concurrency high enough to handle baseline traffic plus typical bursts
*   Enable route optimization for higher capacity limits
*   Implement retry logic with exponential backoff in your client applications

### External API bottlenecks[​](#external-api-bottlenecks "Direct link to External API bottlenecks")

Models often call external APIs for data enrichment, feature retrieval, or other tasks during inference. These external dependencies can become performance bottlenecks:

*   **Latency**: Measure the response time of each external API call. High latency in these calls directly increases overall serving latency and reduces throughput.
*   **Throughput limits**: External APIs may impose rate limits or capacity constraints. Exceeding these limits can cause throttling, errors, and performance degradation.
*   **Error rates**: Frequent errors from external APIs can trigger retries and increase load on your serving endpoint.
*   **Caching**: Implement caching for frequently accessed data from external APIs to reduce the number of calls and improve response times.

Monitor these factors to identify bottlenecks and implement targeted optimizations for high-throughput workloads.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization)
*   [Load testing for serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/what-is-load-test)
