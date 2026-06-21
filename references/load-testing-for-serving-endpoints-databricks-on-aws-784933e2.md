---
title: Load testing for serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/what-is-load-test
ingestedAt: "2026-06-18T08:12:55.733Z"
---

This article walks you through the essential process of load testing your Model Serving endpoints to ensure they can handle production workloads effectively. It also provides practical examples, real-world analogies, and step-by-step instructions using the Locust load testing framework, to demonstrate how to measure key performance metrics like requests per second and concurrency limits, so you can size your endpoints correctly and confidently deploy models for your business needs.

tip

Load testing is an essential component of production optimization. For a comprehensive guide to optimization strategies including infrastructure, model, and client-side optimizations, see [Optimize Model Serving endpoints for production](https://docs.databricks.com/aws/en/machine-learning/model-serving/production-optimization).

## What is a load test?[​](#what-is-a-load-test "Direct link to What is a load test?")

A load test is a test which simulates real world usage of Model Serving endpoints ensuring they meet your production requirements, like latency or requests per second. A load test measures your endpoint’s performance under different levels of traffic, helping you size your endpoint correctly so as to not cause delays.

Picture this: It's 8:00 AM on a weekday, and a popular café in the heart of the city is just opening. The aroma of fresh coffee fills the air. The barista is prepped, machines warmed up, and the line of caffeine-deprived customers is already forming.

At first, things run smoothly. A couple of customers step up, place their orders, and the barista begins preparing their drinks. Some drinks take 30 seconds, others take a minute — depending on the complexity. The barista juggles multiple orders with practiced efficiency.

But soon, more people arrive. Five customers turn into ten, then twenty. Each is placing an order, waiting for their drink, and maybe chatting a bit at the counter. The barista is now under pressure. Even with a second barista jumping in, the system starts to strain — the line grows, orders pile up, and customers begin waiting longer.

Now imagine you're trying to measure how many drinks the café can serve per minute before customers start to leave frustrated. That’s **load testing**.

In this analogy:

*   Each customer is a **client** sending a request.
*   The barista(s) represent your **server** that processes model inferences one by one or in parallel.
*   The time to take an order and serve the drink is the **model implementation** time.
*   Delays in talking, paying, or finding the order are your **network overhead**.
*   More customers arriving at once is **client concurrency**.
*   Adding more baristas or more machines is like increasing your **server concurrency**.

As in any good café, there’s a limit to how much the staff can handle at once. If you don’t plan ahead — say, by bringing in more baristas during peak hours — people leave unhappy. The same goes for your systems under load. Load testing helps you identify where the bottlenecks are, how much traffic your system can handle, and what changes you need to make for smoother service.

Before you run a load test on your endpoint, you need to:

*   Understand the components and concepts related to load testing.
*   Decide and define your production requirements.
*   Find a representative payload for the load testing framework to use when benchmarking your endpoint.

### Load testing concepts and definitions[​](#load-testing-concepts-and-definitions "Direct link to Load testing concepts and definitions")

The following table defines load testing related concepts:

### Latency requirements[​](#latency-requirements "Direct link to Latency requirements")

Based upon your business and customer requirements, define the ideal performance of your system. On a model serving endpoint, latency includes the round trip time that a client experiences when sending data for inference. This includes networking latency as well as inference time. It is important to ensure that your requirements are realistic. For example, if your model takes 15ms to perform inference when loaded into memory, you need to allow additional time for networking latency when served on a model serving endpoint.

### How do RPS, latency, and concurrency relate?[​](#how-do-rps-latency-and-concurrency-relate "Direct link to How do RPS, latency, and concurrency relate?")

A business has some defined criteria for the success of their system. For ML systems, business criteria is generally high quality results, low latency, and high throughput. The quality of results is specifically related to the model itself, while end-to-end latency and throughput are traits of the serving system. End-to-end latency consists of the model execution time and the network overhead. Throughput (or requests or queries per second) is inversely related to latency and directly related to concurrency.

*   The more concurrency the higher the throughput.
*   The higher the latency the lower the throughout.

Generally, there is an optimal ratio of client side concurrency to server side concurrency for any given application. As an example, “how many burgers can a line chef work on simultaneously”. Because there may be many shared steps in the cooking process, the line chef might be able to more optimally cook four hamburgers at the same time rather than cooking only one at a time. There is a limit to this parallelization, at some point the act of performing many parallel acts adds too much latency, like if the chef needs to add cheese to 1000 burgers.

One of the central goals of a load test is to determine the optimal ratio for your application. The optimal ratio maximizes RPS, meet your latency requirements, and avoid queuing. This ratio can be used to accurately size your endpoint to meet your most demanding loads.

If the endpoint is unable to process requests fast enough, a line begins to form. This is called a queue. The forming of a queue typically results in much longer end-to-end latency as there is now additional time each request spends waiting before being processed. If requests continue to arrive faster than requests can be processed, the queue grows, which further increases latency. For this reason, it is important to understand what sort of peak demand your endpoint may experience and ensure it is sized correctly with a load test.

## Load test scenario examples[​](#load-test-scenario-examples "Direct link to Load test scenario examples")

In load testing, as well as real-world systems, the relationship between client concurrency, server concurrency, and latency is dynamic and interdependent. Let’s see this relationship with a simple example:

### Scenario 1: Simple setup[​](#scenario-1-simple-setup "Direct link to Scenario 1: Simple setup")

In this setup, a single client sends requests sequentially — it waits for a response before issuing the next request. Since the total time per request is the sum of model execution and overhead latency (40 ms + 10 ms), the measured end to end latency is 50 ms.

*   Number of clients: 1
*   Provisioned concurrency: 1
*   Overhead latency: 10 ms
*   Model execution time 40 ms

As a result, the client completes one request every 50 ms, which equates to 20 requests per second or queries per second.

### Scenario 2: Increase provisioned concurrency[​](#scenario-2-increase-provisioned-concurrency "Direct link to Scenario 2: Increase provisioned concurrency")

In this case, you have double the provisioned concurrency and a single client making requests sequentially. This means that the total latency is still 50 ms (40ms + 10ms), and the system is only seeing 20 requests per second (QPS).

*   Number of clients: 1
*   Provisioned concurrency: **1 -> 2**
*   Overhead latency: 10 ms
*   Model execution time 40 ms

### Scenario 3: Add another client to the system.[​](#scenario-3-add-another-client-to-the-system "Direct link to Scenario 3: Add another client to the system.")

Now you have two clients making requests to an endpoint with two provisioned concurrency. In this case, each client’s request can be independently processed by the endpoint simultaneously (assuming perfect load balancing). So while the total latency is still 50 ms (40ms + 10ms), the system observes 40 requests per seconds, since each client sends 20 qps.

*   Number of clients: **1 -> 2**
*   Provisioned concurrency: 2
*   Overhead latency: 10 ms
*   Model execution time 40 ms

Increasing the provisioned concurrency and the number of clients making requests increases the total QPS observed in your system, without a penalty on latency.

### Scenario 4: Lets reduce the provisioned concurrency[​](#scenario-4-lets-reduce-the-provisioned-concurrency "Direct link to Scenario 4: Lets reduce the provisioned concurrency")

In this last scenario, the number of clients is greater than the provisioned concurrency. This setup introduces another variable, queuing, in the system and its effect on QPS and latency.

*   Number of clients: 2
*   Provisioned concurrency: **2 -> 1**
*   Overhead latency: 10 ms
*   Model execution time: 40 ms

Here, you have two clients making requests simultaneously. The endpoint, however, can only process a single request at a time. This forces the second request to wait before the first request has been processed. The waiting, or more correctly, queuing of the second request can adversely affect the latency of the system. Assuming that the server allows queuing (enabled by default in Databricks Model Serving), the second client sees a latency of 90 ms: 10 ms (network overhead) + 40 ms (queuing wait time) + 40 ms (model execution time). This is significantly worse than the 50 ms seen before.
