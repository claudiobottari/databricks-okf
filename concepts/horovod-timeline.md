---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85485868b797c732c565ebeed340e430965693aeca16be075f6e94327dc394f1
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-timeline
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Timeline
description: A performance tracing tool for Horovod that records activity timelines, accessible via Chrome tracing, but with significant performance overhead (~40% throughput reduction).
tags:
  - profiling
  - debugging
  - performance
timestamp: "2026-06-19T19:05:34.485Z"
---

# Horovod Timeline

**Horovod Timeline** is a built-in profiling feature of the Horovod framework that records a detailed timeline of internal activity during distributed training. It captures events such as allreduce operations, tensor fusion, and communication overhead, which can be visualized to diagnose performance bottlenecks in distributed deep learning workloads.^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Performance Impact

Horovod Timeline has a **significant performance impact**. For example, the throughput of an Inception3 training job can decrease by approximately 40% when the timeline is enabled. To maximize training speed, Databricks recommends disabling Horovod Timeline for production HorovodRunner jobs.^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

The timeline file cannot be viewed while training is in progress; it is only available for inspection after the training job completes.^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Recording a Horovod Timeline

To record a timeline, set the `HOROVOD_TIMELINE` environment variable to the path where the timeline JSON file should be saved. Databricks recommends using a location on shared storage (such as DBFS) so that the file can be easily retrieved. The following example creates a unique directory in `/dbfs/`, sets the environment variable, and launches a HorovodRunner job:^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

```python
timeline_dir = "/dbfs/ml/horovod-timeline/%s" % uuid.uuid4()
os.makedirs(timeline_dir)
os.environ['HOROVOD_TIMELINE'] = timeline_dir + "/horovod_timeline.json"

hr = HorovodRunner(np=4)
hr.run(run_training_horovod, params=params)
```

The training function itself must include any timeline-specific code at the beginning and end, as shown in the companion Horovod timeline example notebook (linked in the original documentation).^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Viewing the Timeline

After training completes, download the timeline JSON file using the Databricks CLI. The file can then be opened in the Chrome browser at `chrome://tracing` for interactive visual analysis. The resulting trace displays the sequence and overlap of communication and computation across workers.^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

![Horovod timeline](https://docs.databricks.com/aws/en/assets/images/mnist-timeline-2f43586369684bc8573ceae09687437a.png)

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The deprecated API for launching Horovod training on Databricks.
- Distributed training with Horovod – General approach for migrating single-node code to distributed training.
- DBFS – Databricks File System, used to store timeline output.
- Databricks CLI – Tool for downloading files from the workspace.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

> **Note:** Horovod and HorovodRunner are deprecated as of Databricks Runtime 15.4 LTS ML. The timeline feature is documented here for reference only; for new distributed training workloads, use [TorchDistributor](/concepts/torchdistributor.md) (for PyTorch) or the `tf.distribute.Strategy` API (for TensorFlow).^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
