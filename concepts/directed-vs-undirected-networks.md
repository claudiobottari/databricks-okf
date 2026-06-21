---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6fca15248edf30b6dc701d4895b876bb4da9b833e93c68e945cd3c6703367ba0
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - directed-vs-undirected-networks
    - DVUN
    - Directed and Undirected Networks
    - Directed and undirected networks
    - Directed and Undirected Networks|directed graphs
    - directed networks
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Directed vs Undirected Networks
description: "Classification of graphs based on edge directionality: directed graphs represent one-way relationships (e.g., follower/followee), while undirected graphs represent two-way relationships (e.g., coworkers)."
tags:
  - graph-analysis
  - fundamentals
timestamp: "2026-06-19T19:01:56.513Z"
---

# Directed vs Undirected Networks

In graph and network analysis, every edge (or link) can be classified by whether it has an associated direction. This property defines two fundamental types of networks: **directed** and **undirected**. The choice between the two depends on the nature of the relationship being modelled.

## Directed Networks

A network is **directed** when its edges represent a one‑way relationship. Each edge has a source node and a target node, and the connection applies only in that direction. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Common examples include:
- A fan following a celebrity on a social network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- Hyperlinks between web pages.
- Airline routes where flights operate in one direction.

In directed graphs, the **degree** of a node is split into two measures:
- **In‑degree**: the number of edges coming *into* the node.
- **Out‑degree**: the number of edges pointing *away from* the node.

^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

The total number of possible edges in a directed graph with \(n\) nodes is \(n(n-1)\), because each unordered pair of nodes can have edges in both directions. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Undirected Networks

A network is **undirected** when its edges represent a two‑way (or symmetric) relationship. An edge between two nodes implies a connection that can be traversed in either direction. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Common examples include:
- Coworkers in a professional network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- Roads connecting cities.
- Friendship links on some social platforms (where the link is mutual).

In undirected graphs, the **degree** of a node is simply the total number of edges incident to it; there is no distinction between in‑degree and out‑degree. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

The total number of possible edges in an undirected graph with \(n\) nodes is \(n(n-1)/2\), because each unordered pair of nodes can have at most one edge. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Practical Considerations

When performing graph analysis, the directed or undirected nature of the network affects:
- **Shortest path calculations** – direction matters in directed networks; a path may exist one way but not the other.
- **Centrality measures** – for example, degree centrality can be split into in‑degree and out‑degree in directed networks.
- **Data storage and querying** – packages like [NetworkX](/concepts/networkx.md) (for single‑node graphs) and [GraphFrames](/concepts/graphframes.md) (for distributed graphs) both support directed and undirected representations.

## Related Concepts

- [Graph and Network Analysis on Databricks](/concepts/graph-and-network-analysis-on-databricks.md)
- Node (graph theory)
- Edge (graph theory)
- Degree (graph theory)
- [GraphFrames](/concepts/graphframes.md)
- [NetworkX](/concepts/networkx.md)

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
