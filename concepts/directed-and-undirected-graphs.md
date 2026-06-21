---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5daaa71aeae55896735da195b85d63bcf9a1f5b2030b15e0ec6616ac2da68ef1
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - directed-and-undirected-graphs
    - Undirected Graphs and Directed
    - DAUG
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Directed and Undirected Graphs
description: Classification of graphs based on whether edges represent one-way or two-way relationships between nodes
tags:
  - graph-analysis
  - graph-theory
  - fundamentals
timestamp: "2026-06-19T10:46:33.336Z"
---

# Directed and Undirected Graphs

**Directed and undirected graphs** are two fundamental categories of networks that differ in whether edges have an associated direction. In network analysis, a graph consists of nodes (vertices) connected by edges (links). The directionality of edges determines how relationships are modeled and how properties like degree are computed. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Directed Graphs

A **directed graph** (or digraph) is one in which edges have a direction, representing a one-way relationship. For example, the relationship of a fan following a celebrity on a social network is one-way: the fan follows the celebrity, but the celebrity may not follow the fan back. Each edge points from one node to another. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

In a directed graph, the degree of a node is split into two measures:
- **In-degree**: the number of edges coming into the node.
- **Out-degree**: the number of edges pointing away from the node. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Undirected Graphs

An **undirected graph** is one in which edges do not have an associated direction, representing a two-way or symmetric relationship. For example, the relationship between coworkers is mutual: if person A works with person B, then person B works with person A. The edge simply indicates a connection without orientation. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

In an undirected graph, the degree of a node is the total number of edges that link to it. There is no distinction between in-degree and out-degree. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Graph and Network Analysis on Databricks](/concepts/graph-and-network-analysis-on-databricks.md) – Overview of graph processing capabilities and tooling.
- [Nodes and Edges](/concepts/nodes-and-edges.md) – The basic building blocks of any graph.
- [Weighted Edges](/concepts/weighted-edges.md) – Edges that carry additional numeric information.
- Degree (graph theory) – The measure of how many edges connect to a node.
- Centrality – Importance measures for nodes in a network.
- Shortest path – The minimum distance between two nodes.
- In-degree – Incoming edges for a node in a directed graph.
- Out-degree – Outgoing edges for a node in a directed graph.
- [GraphFrames](/concepts/graphframes.md) – Distributed graph processing on Apache Spark.
- [NetworkX](/concepts/networkx.md) – Python library for single-node graph analysis.

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
