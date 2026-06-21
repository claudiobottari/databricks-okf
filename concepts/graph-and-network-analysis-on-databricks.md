---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2fe03b3038997ac813c4105a2dc0962e15601f18bf9f4750ede5fbf9f560a9b
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - graph-and-network-analysis-on-databricks
    - Network Analysis on Databricks and Graph
    - GANAOD
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Graph and Network Analysis on Databricks
description: Overview of Databricks capabilities for graph processing, combining Databricks Runtime ML with NetworkX, GraphFrames, and external tools
tags:
  - databricks
  - graph-analysis
  - machine-learning
timestamp: "2026-06-19T10:46:10.782Z"
---

## Graph and Network Analysis on Databricks

**Graph and network analysis** on Databricks refers to the platform’s capabilities for processing and analyzing graph-structured data — sets of **vertices (nodes)** connected by **edges (links)**. Graphs model relationships in domains such as social networks, transportation, telecommunications, fraud detection, and product recommendation. Databricks provides tools for both single‑node and distributed graph processing, enabling analysis at any scale and integration with other analytics and machine learning workflows. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Basic Graph Concepts

A **graph** consists of a set of **vertices** (also called nodes, points, or entities) and a set of **edges** (links, relationships, or arcs) that connect them. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

- **Directed vs. undirected networks**: In a directed graph, edges have a direction (e.g., a fan following a celebrity); in an undirected graph, edges represent symmetric relationships (e.g., coworkers). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Weighted edges**: Edges can carry weights, such as the capacity of a highway or cable. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Degree**: The degree of a node is the number of edges incident to it. For directed graphs, **in‑degree** counts incoming edges and **out‑degree** counts outgoing edges. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Network and Node Properties

- **Shortest path**: The minimum distance between two nodes, accounting for direction and optional edge weights. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Centrality**: Measures of node importance. **Degree centrality** is the fraction of nodes directly connected; **betweenness centrality** is the fraction of shortest paths that pass through the node. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Degree distribution**: The count of nodes for each degree value, revealing the network’s structure. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Diameter**: The maximum shortest‑path distance between any two nodes (equivalent to the maximum eccentricity). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Density**: The ratio of actual edges to the total possible edges. For an undirected graph, total possible edges = n(n‑1)/2; for a directed graph, n(n‑1). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Small‑world networks**: Real‑world networks often exhibit closely linked subgroups and short average path lengths, a pattern that can cause data skew in distributed processing. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Tools on Databricks

Databricks Runtime ML includes two primary graph analysis packages:

- **[NetworkX](/concepts/networkx.md)** – For relatively small networks that fit on a single compute node. Provides a rich set of algorithms and is built into Databricks Runtime ML. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **[GraphFrames](/concepts/graphframes.md)** – For large networks requiring distributed processing. Supports GraphX‑inspired APIs and integrates with Apache Spark. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Users can also install additional open‑source packages or connect to external partners for graph processing and visualization. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Example Notebook

The source includes a notebook titled *Basic graph analysis using NetworkX* that demonstrates these concepts on Databricks. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Related Concepts

- Machine Learning on Databricks
- Fraud Detection on Databricks
- Recommendation Systems
- Apache Spark GraphX
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

### Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
