---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b4535e6d6c06ed250c20e442d07c098da1898e835bf3bf55fc146f07a24e6d2
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nodes-and-edges
    - Edges and Nodes
    - NAE
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Nodes and Edges
description: "Fundamental building blocks of a graph: nodes (vertices) represent entities such as people or cities, and edges (links, relationships, arcs) represent connections or relationships between them."
tags:
  - graph-analysis
  - fundamentals
timestamp: "2026-06-19T19:01:58.048Z"
---

# Nodes and Edges

In [Graph and Network Analysis](/concepts/graph-and-network-analysis.md), a **graph** (or **network**) consists of a set of **nodes** and a set of **edges** that connect the nodes. Nodes represent the things being connected — such as people, cities, or servers — while edges represent the connections or relationships between them, such as people who have worked together, or train stations that have a direct link between them. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Terminology

Nodes are also called *vertices*, *points*, or *entities*. Edges are also called *lines*, *relationships*, *links*, or *arcs*. For example, in a social network, people are nodes and friendships are edges. In a transportation network, cities are nodes and flight routes are edges. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Directed and undirected edges

An edge can represent a one-way relationship (e.g., a fan following a celebrity) or a two-way relationship (e.g., coworkers). If edges can be one-way, the network is called **directed**. If edges do not have an associated direction, the network is called **undirected**. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Weighted edges

Edges can have **weights**. Examples include the carrying capacity of a highway or cable. Weighted edges are used in algorithms such as shortest‑path computation. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Degree of a node

The **degree** of a node is the number of edges that link to it. For directed graphs, *in-degree* is the number of edges coming into the node, and *out-degree* is the number of edges pointing away from the node. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Graph analysis](/concepts/graph-and-network-analysis.md) — Overview of graph processing and use cases.
- [NetworkX](/concepts/networkx.md) — A Python library for small‑scale graph analysis on a single node.
- [GraphFrames](/concepts/graphframes.md) — A distributed graph processing library for large‑scale networks.
- [Degree distribution](/concepts/degree-and-degree-distribution.md) — The number of nodes of each degree in a network.
- Centrality — Measures of node importance, such as degree centrality and betweenness centrality.
- Shortest path — The minimum distance between two nodes, considering direction and weights.

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
