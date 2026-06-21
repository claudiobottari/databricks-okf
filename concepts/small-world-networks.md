---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56e8a5fea523b9bfb58754d565fea4438c35cbea940646dedc38b59e94536f0a
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - small-world-networks
    - Small-world phenomenon
    - small-world phenomenon
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Small-world Networks
description: A real-world network pattern characterized by closely linked subgroups and a short average path length between any two nodes; commonly observed in social and other real-world networks and can lead to data skew in distributed graph processing.
tags:
  - graph-analysis
  - network-patterns
timestamp: "2026-06-19T19:02:33.721Z"
---

---
title: Small-World Networks
summary: Real-world network pattern characterized by closely linked subgroups and short average path length between any two nodes
sources:
  - graph-and-network-analysis-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:46:19.414Z"
updatedAt: "2026-06-19T10:46:19.414Z"
tags:
  - graph-analysis
  - network-science
  - complex-networks
aliases:
  - small-world-networks
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Small-World Networks

**Small-World Networks** are a class of network structures commonly observed in real-world systems, particularly those involving people or social interactions. The "small-world phenomenon" describes the observation that many real-world networks simultaneously exhibit closely linked subgroups and a short average path length between any two nodes.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Characteristics

Most real-world networks are not randomly connected—they exhibit patterns and substructures that distinguish them from purely random [graph topologies](/concepts/graph-and-network-analysis.md). Small-world networks are defined by two key properties:^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

1. **Closely linked subgroups**: Nodes tend to form clusters where connections are dense, meaning that the acquaintances of any given node are likely to also know each other.

2. **Short average path length**: Despite local clustering, the average number of steps required to travel between any two randomly chosen nodes remains small—popularly known as "six degrees of separation."^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

These two properties coexisting—high clustering combined with short path lengths—distinguish small-world networks from both regular lattices (high clustering but long path lengths) and random graphs (short path lengths but low clustering).^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Prevalence in Real-World Systems

The small-world phenomenon is very common in practice and appears in many domains:^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

- **Social networks**: The classic example, where any two individuals can be linked through a surprisingly short chain of acquaintances.
- **Communication networks**: Networks of email correspondence, phone calls, or messaging platforms.
- **Collaboration networks**: Co-authorship networks among researchers or professional networks among colleagues.
- **Biological networks**: Neural networks in the brain or protein-protein interaction networks.

## Computational Implications

The pervasiveness of small-world networks has important implications for graph processing at scale. These patterns lead to common issues when processing large graphs, such as natural occurrences of Data Skew|data skew that distributed graph processing frameworks must contend with.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

For example, when processing a social network graph, highly connected hub nodes can create data skew in distributed computations, requiring careful partitioning strategies in tools like [GraphFrames](/concepts/graphframes.md) or custom graph algorithms.

## Related Concepts

- [Node Degree|Degree](/concepts/degree-and-degree-distribution.md) — The number of edges connected to a node; small-world networks often have degree distributions with a long tail of highly connected hub nodes.
- Shortest Path — The minimum distance between two nodes; small-world networks have characteristically short average shortest paths.
- [Graph and Network Analysis](/concepts/graph-and-network-analysis.md) — The broader field of studying graph structures.
- Clustering Coefficient — A measure of how tightly nodes cluster together; small-world networks have high clustering coefficients.
- [GraphFrames](/concepts/graphframes.md) — A distributed graph processing library for large-scale analysis on Databricks.
- [NetworkX](/concepts/networkx.md) — A Python library for analyzing small to medium-sized networks, useful for exploring small-world properties on a single node.
- Centrality — Measures of node importance; hub nodes in small-world networks often have high centrality.

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
