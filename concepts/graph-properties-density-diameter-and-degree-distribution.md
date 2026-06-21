---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf380a2d55190190f84b03f854b20df2277584d2fbf0c32654558bee3cce9400
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - graph-properties-density-diameter-and-degree-distribution
    - "Degree Distribution and Graph Properties: Density, Diameter,"
    - GPDDADD
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: "Graph Properties: Density, Diameter, and Degree Distribution"
description: Fundamental structural properties of networks including density, diameter, and degree distribution used to characterize graph topology
tags:
  - graph-analysis
  - network-science
  - topology
timestamp: "2026-06-19T10:46:26.882Z"
---

# Graph Properties: Density, Diameter, and Degree Distribution

Graph properties quantify the structural characteristics of a network. The three fundamental properties — **density**, **diameter**, and **degree distribution** — describe how connected a graph is, how far apart its nodes are, and how connectivity is distributed among its vertices. These metrics are essential for understanding the organization and behavior of real-world networks such as social networks, transportation systems, and communication infrastructures. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Density

**Density** measures how many edges are present in a graph relative to the maximum possible number of edges. It indicates how close the graph is to being complete (fully connected). For an undirected graph, the total number of possible edges is \(n(n-1)/2\), where \(n\) is the number of nodes. For a directed graph, each edge has two possible directions, so the total number of possible edges is \(n(n-1)\). The density is then the actual number of edges divided by this total. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

A density value near 1 indicates a very dense graph (many connections), while a value near 0 indicates a sparse graph (few connections).

## Diameter

**Diameter** is the longest of all shortest paths between any two nodes in the network. It represents the maximum distance (in steps or edges) that must be traversed to travel from one node to another. The diameter is equivalent to the maximum eccentricity of nodes in the network, where eccentricity of a node is the greatest distance from that node to any other node. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

A small diameter relative to the number of nodes suggests the network exhibits the [small-world phenomenon](/concepts/small-world-networks.md), where most nodes can be reached from any other node through a short chain of connections.

## Degree Distribution

**Degree distribution** describes the frequency of nodes having a particular degree (where degree is the number of edges connected to a node). For a given graph, the degree distribution lists how many nodes have degree 0, degree 1, degree 2, and so on. This distribution provides insight into the overall structure and organization of the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

In directed graphs, separate degree distributions can be computed for in-degree and out-degree.

## Significance in Graph Analysis

Together, density, diameter, and degree distribution give a high-level summary of a network’s connectivity and scale. They are used to classify networks (e.g., sparse vs. dense), to detect anomalies, and to compare different graphs. These properties are also foundational for more advanced analyses such as community detection and centrality measurement. Many graph processing libraries, including [NetworkX](/concepts/networkx.md) and [GraphFrames](/concepts/graphframes.md), provide built-in functions to compute these metrics for networks of any size. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- Graph theory
- [Network analysis](/concepts/graph-and-network-analysis.md)
- Node degree
- Shortest path
- Centrality
- Directed graph
- Undirected graph
- [Small-world Networks](/concepts/small-world-networks.md)
- Eccentricity

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
