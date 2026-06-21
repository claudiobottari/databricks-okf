---
title: OPTIMIZE | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-optimize
ingestedAt: "2026-06-18T08:18:57.344Z"
---

Bin-packing optimization is _idempotent_: if you run it twice on the same data set, the second run has no effect. It produces evenly-balanced data files with respect to their size on disk, but not necessarily the number of tuples per file. The two measures are most often correlated.

Z-Ordering is _not idempotent_, but operates incrementally. The time Z-Ordering takes is not guaranteed to decrease over multiple runs. However, if no new data was added to a partition that was just Z-Ordered, running Z-Ordering again on that partition has no effect. Z-Ordering produces evenly-balanced data files with respect to the number of tuples, but not necessarily data size on disk. The two measures are most often correlated, but skew in optimize task times can occur when they diverge.
