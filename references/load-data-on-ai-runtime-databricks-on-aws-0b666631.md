---
title: Load data on AI Runtime | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading
ingestedAt: "2026-06-18T08:08:22.326Z"
---

Public Preview

AI Runtime for single-node tasks is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The distributed training API for multi-GPU workloads remain in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This section covers information about loading data on AI Runtime specifically for ML and DL applications. Check the [tutorial](https://docs.databricks.com/aws/en/getting-started/dataframes) to learn more about how to load and transform data using the Spark Python API.

note

Unity Catalog is required. All data access on AI Runtime goes through Unity Catalog. Your tables and volumes must be registered in Unity Catalog and accessible to your user or service principal.

## Load tabular data[​](#load-tabular-data "Direct link to Load tabular data")

Use Spark Connect to load tabular machine learning data from [Delta tables](https://docs.databricks.com/aws/en/delta/).

For single-node training, you can convert Apache Spark DataFrames into pandas DataFrames using the [PySpark method](https://docs.databricks.com/aws/en/pyspark/reference/classes/dataframe/toPandas) `toPandas()`, and then optionally convert to NumPy format using the [PySpark method](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_numpy.html) `to_numpy()`.

Spark Connect supports most PySpark APIs, including Spark SQL, Pandas API on Spark, Structured Streaming, and MLlib (DataFrame-based). See the [PySpark API reference documentation](https://spark.apache.org/docs/latest/api/python/reference/index.html) for the latest supported APIs.

For other limitations, see [Serverless compute limitations](https://docs.databricks.com/aws/en/compute/serverless/limitations).

## Load large Delta tables using volumes[​](#load-large-delta-tables-using-volumes "Direct link to Load large Delta tables using volumes")

For large Delta tables that are too big to convert with `toPandas()`, export the data to a Unity Catalog volume and load it directly using PyTorch or Hugging Face:

Python

    # Step 1: Export the Delta table to Parquet files in a UC volumeoutput_path = "/Volumes/catalog/schema/my_volume/training_data"spark.table("catalog.schema.my_table").write.mode("overwrite").parquet(output_path)

Python

    # Step 2: Load the exported data directly using Hugging Face datasetsfrom datasets import load_datasetdataset = load_dataset("parquet", data_files="/Volumes/catalog/schema/my_volume/training_data/*.parquet")

This approach avoids Spark overhead during training and works well for both single-GPU and distributed training workflows.

## Load unstructured data from volumes with `UCVolumeDataset`[​](#load-unstructured-data-from-volumes-with-ucvolumedataset "Direct link to load-unstructured-data-from-volumes-with-ucvolumedataset")

For unstructured data such as images, audio, and text files stored in Unity Catalog volumes, use `UCVolumeDataset` from the `serverless_gpu.data` package. `UCVolumeDataset` is a PyTorch [`IterableDataset`](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets) that copies each file from the volume to a fast local cache on first access and yields the cached local file path. It handles the performance and distribution concerns you would otherwise implement by hand:

*   **Local caching.** Files are copied from the FUSE mount to a local cache directory on first access and served from the cache afterward, so multi-epoch training does not re-read the volume.
*   **Automatic partitioning.** When `torch.distributed` is initialized, files are partitioned across ranks and then further divided across `DataLoader` workers, so each `(rank, worker)` pair receives a non-overlapping slice with no extra setup.

note

`UCVolumeDataset` and `serverless_gpu.data.DataLoader` require [GPU environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu#serverless-gpu-python-api-upgraded-to-0516) or above.

`UCVolumeDataset` yields raw local file paths. To decode those files into tensors, wrap it in a second `IterableDataset` that consumes the path stream and applies your parsing logic. This keeps I/O and parsing concerns separate.

Python

    from serverless_gpu.data import UCVolumeDatasetfrom torch.utils.data import IterableDatasetfrom PIL import Imageimport torchvision.transforms.functional as TFclass ImageDataset(IterableDataset):    """Decodes each cached file path from UCVolumeDataset into a tensor."""    def __init__(self, path_dataset: UCVolumeDataset):        self._path_dataset = path_dataset    def __iter__(self):        for local_path in self._path_dataset:            image = Image.open(local_path).convert("RGB")            yield TF.to_tensor(image)path_dataset = UCVolumeDataset("/Volumes/catalog/schema/my_volume/images")dataset = ImageDataset(path_dataset)

The wrapper receives already-cached local paths, so the parsing step never touches the FUSE mount. You can chain additional wrappers for augmentation, tokenization, or filtering.

For optimal performance, pair `UCVolumeDataset` with `serverless_gpu.data.DataLoader` rather than the stock PyTorch `DataLoader`. It is tuned for serverless GPU I/O and fetches and caches files concurrently while the GPU computes. See [Data loading performance](#data-loading-performance).

## Load data inside the @distributed decorator[​](#load-data-inside-the-distributed-decorator "Direct link to Load data inside the @distributed decorator")

When using the [Serverless GPU API](https://api-docs.databricks.com/python/serverless_gpu/index.html) for distributed training, move data loading code inside the [@distributed](https://api-docs.databricks.com/python/serverless_gpu/api/serverless_gpu.html#serverless_gpu.launcher.distributed) decorator. The dataset size can exceed the maximum size allowed by pickle, so it is recommended to generate the dataset inside the decorator, as shown below:

Python

    from serverless_gpu import distributed# This may cause a pickle error if the dataset is too largedataset = get_dataset(file_path)@distributed(gpus=8, gpu_type='H100')def run_train():    # Load data inside the decorator to avoid pickle serialization issues    dataset = get_dataset(file_path)    ...

When you construct a `UCVolumeDataset` inside the decorator, it reads `torch.distributed` rank information at iteration time and partitions files across ranks automatically, so you do not need a `DistributedSampler` for file-based volume data.

## Data loading performance[​](#data-loading-performance "Direct link to Data loading performance")

`/Workspace` and `/Volumes` directories are hosted on remote Unity Catalog storage. If your dataset is stored in Unity Catalog, the data loading speed is limited by the available network bandwidth. If you are training multiple epochs, the recommended approach is to use `UCVolumeDataset` which does this caching for you: it copies each file to local storage on first access and serves subsequent reads from the local copy. For datasets in volumes, prefer it over a manual `shutil.copytree`, which copies the entire tree up front even if training touches only part of it.

If your dataset is large, the following techniques can improve throughput:

*   **Use `serverless_gpu.data.DataLoader` to parallelize fetching.** This is a drop-in subclass of the [torch `DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) tuned for serverless GPU I/O: `num_workers` defaults to 6 and `prefetch_factor` to 4 (compared to PyTorch's 0 and 2), so files are fetched and cached concurrently while the GPU computes. It also logs per-batch fetch timing to the active MLflow run, which helps you spot data-loading bottlenecks.
    
    Python
    
        from serverless_gpu.data import DataLoaderloader = DataLoader(    dataset,    batch_size=32,    pin_memory=True,    # num_workers=6, by default    # prefetch_factor=4, by default    # raise num_workers to increase parallel reads, or prefetch_factor to deepen each worker's queue.)
    
    All ranks must use the same `num_workers` value, because `UCVolumeDataset` partitions files using a global stride across `world_size × num_workers` slots. Mismatched values cause files to be duplicated or skipped.
    
*   **Increase batch size.** Larger batches amortize per-batch data-loading overhead over more samples and reduce the number of file-fetch operations per step. If GPU memory is the limiting factor, combine a larger batch size with gradient accumulation to preserve the effective batch size.
    

## Streaming datasets[​](#streaming-datasets "Direct link to Streaming datasets")

For very large datasets that do not fit in memory, use streaming approaches:

*   `UCVolumeDataset` from `serverless_gpu.data` for streaming files from Unity Catalog volumes with local caching and automatic distributed partitioning. See [Load unstructured data from volumes with `UCVolumeDataset`](#load-unstructured-data-from-volumes-with-ucvolumedataset).
*   [PyTorch IterableDataset](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets) for custom streaming logic.
*   [Hugging Face datasets](https://huggingface.co/docs/datasets/stream) with streaming for datasets hosted on the Hub or in volumes.
*   [Ray Data](https://docs.ray.io/en/latest/data/data.html) for distributed batch data processing.
