---
title: Start a Ray cluster on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/start-ray
ingestedAt: "2026-06-18T08:13:10.350Z"
---

Databricks simplifies the process of starting a Ray cluster by handling cluster and job configuration the same way it does with any Apache Spark job. This is because the Ray cluster is actually started on top of the managed Apache Spark cluster.

## Run Ray on Databricks[​](#run-ray-on-databricks "Direct link to run-ray-on-databricks")

Python

    from ray.util.spark import setup_ray_clusterimport ray# If the cluster has four workers with 8 CPUs each as an examplesetup_ray_cluster(num_worker_nodes=4, num_cpus_per_worker=8)# Pass any custom configuration to ray.initray.init(ignore_reinit_error=True)

This approach works at any cluster scale, from a few to hundreds of nodes. Ray clusters on Databricks also support autoscaling.

After creating the Ray cluster, you can run any Ray application code in a Databricks notebook.

important

Databricks recommends installing any necessary libraries for your application with `%pip install <your-library-dependency>` to ensure they are available to your Ray cluster and application accordingly. Specifying dependencies in the Ray init function call installs the dependencies in a location inaccessible to the Apache Spark worker nodes, which results in version incompatibilities and import errors.

For example, you can run a simple Ray application in a Databricks notebook as follows:

Python

    import rayimport randomimport timefrom fractions import Fractionray.init()@ray.remotedef pi4_sample(sample_count):    """pi4_sample runs sample_count experiments, and returns the    fraction of time it was inside the circle.    """    in_count = 0    for i in range(sample_count):        x = random.random()        y = random.random()        if x*x + y*y <= 1:            in_count += 1    return Fraction(in_count, sample_count)SAMPLE_COUNT = 1000 * 1000start = time.time()future = pi4_sample.remote(sample_count=SAMPLE_COUNT)pi4 = ray.get(future)end = time.time()dur = end - startprint(f'Running {SAMPLE_COUNT} tests took {dur} seconds')pi = pi4 * 4print(float(pi))

## Shut down a Ray cluster[​](#shut-down-a-ray-cluster "Direct link to Shut down a Ray cluster")

Ray clusters automatically shut down under the following circumstances:

*   You detach your interactive notebook from your Databricks cluster.
*   Your Databricks job is completed.
*   Your Databricks cluster is restarted or terminated.
*   There's no activity for the specified idle time.

To shut down a Ray cluster running on Databricks, you can call the `ray.utils.spark.shutdown_ray_cluster` API.

Python

    from ray.utils.spark import shutdown_ray_clusterimport rayshutdown_ray_cluster()ray.shutdown()

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Scale Ray clusters on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/scale-ray)
