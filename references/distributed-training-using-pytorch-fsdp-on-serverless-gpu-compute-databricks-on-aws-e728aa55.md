---
title: Distributed training using PyTorch FSDP on serverless GPU compute | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-distributed-pytorch-fsdp
ingestedAt: "2026-06-18T08:08:50.499Z"
---

This notebook demonstrates how to train a Transformer model using distributed training with PyTorch's Fully Sharded Data Parallel (FSDP) on Databricks serverless GPU compute. FSDP is a data parallelism technique that shards model parameters, gradients, and optimizer states across multiple GPUs, enabling efficient training of large models that don't fit on a single GPU.

In this example, you'll learn how to:

*   Set up distributed training with the [serverless GPU distributed training API](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor)
*   Define and train a 10M parameter Transformer model using FSDP
*   Save distributed checkpoints during training
*   Track experiments with MLflow
*   Load checkpoints for inference or continued training

This notebook uses synthetic data to keep it self-contained, but you can adapt it to work with your own datasets.

**Key concepts:**

*   **FSDP (Fully Sharded Data Parallel)**: A PyTorch distributed training strategy that shards model parameters across GPUs to reduce memory usage and enable training of larger models.
*   **Serverless GPU compute**: Databricks managed GPU compute that automatically scales and provisions resources for your workloads.

For more information, see [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training).

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook requires serverless GPU compute. To connect:

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**
2.  On the right side, click the environment button
3.  Select **8xH100** as the **Accelerator**
4.  Choose **AI v5** environment from the right panel that contains all the required libraries to run this notebook example
5.  Click **Apply**

## Configure Unity Catalog locations[​](#configure-unity-catalog-locations "Direct link to Configure Unity Catalog locations")

Set up the Unity Catalog locations where the model and checkpoints will be stored. Update these values to match your workspace configuration. You need `USE CATALOG` and `USE SCHEMA` privileges on the specified catalog and schema.

Python

    # You must have `USE CATALOG` privileges on the catalog, and you must have `USE SCHEMA` privileges on the schema.# If necessary, change the catalog and schema name here.dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("model_name", "transformer_fsdp")dbutils.widgets.text("uc_volume", "checkpoints")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_VOLUME = dbutils.widgets.get("uc_volume")MODEL_NAME = dbutils.widgets.get("model_name")UC_MODEL_NAME = f"{UC_CATALOG}.{UC_SCHEMA}.{MODEL_NAME}"print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_VOLUME: {UC_VOLUME}")print(f"UC_MODEL_NAME: {UC_MODEL_NAME}")

## Define helper functions and synthetic dataset[​](#define-helper-functions-and-synthetic-dataset "Direct link to Define helper functions and synthetic dataset")

This section defines utility functions for distributed training setup and a synthetic dataset class for demonstration purposes. In production, you would replace the `SyntheticDataset` with your own data loading logic.

**Key components:**

*   `setup()`: Initializes the distributed training process group and configures GPU devices
*   `cleanup()`: Cleans up the distributed process group after training
*   `AppState`: A wrapper class for checkpointing model and optimizer state that's compatible with PyTorch's distributed checkpoint API
*   `SyntheticDataset`: Generates random data for training demonstration

Python

    import torchimport torch.nn as nnimport torch.optim as optimimport torch.distributed as distimport torch.distributed.checkpoint as dcpfrom torch.distributed.checkpoint.stateful import Statefulfrom torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dictfrom torch.distributed.checkpoint import FileSystemWriter as StorageWriterfrom torch.distributed.fsdp import fully_shardfrom torch.utils.data import Dataset, DataLoader, DistributedSamplerimport numpy as npimport osimport time# Below is an example of distributed checkpoint based on# https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.htmlclass AppState(Stateful):    """This is a useful wrapper for checkpointing the Application State. Since this object is compliant    with the Stateful protocol, DCP will automatically call state_dict/load_stat_dict as needed in the    dcp.save/load APIs.    Note: We take advantage of this wrapper to hande calling distributed state dict methods on the model    and optimizer.    """    def __init__(self, model, optimizer=None):        self.model = model        self.optimizer = optimizer    def state_dict(self):        # this line automatically manages FSDP FQN's, as well as sets the default state dict type to FSDP.SHARDED_STATE_DICT        model_state_dict, optimizer_state_dict = get_state_dict(self.model, self.optimizer)        return {            "model": model_state_dict,            "optim": optimizer_state_dict        }    def load_state_dict(self, state_dict):        # sets our state dicts on the model and optimizer, now that we've loaded        set_state_dict(            self.model,            self.optimizer,            model_state_dict=state_dict["model"],            optim_state_dict=state_dict["optim"]        )def setup():    """Initialize the distributed training process group"""    # Check if we're in a distributed environment    if 'RANK' in os.environ and 'WORLD_SIZE' in os.environ:        rank = int(os.environ['RANK'])        world_size = int(os.environ['WORLD_SIZE'])        local_rank = int(os.environ.get('LOCAL_RANK', 0))    else:        # Fallback for single GPU        rank = 0        world_size = 1        local_rank = 0    # Initialize process group    if world_size > 1:        if not dist.is_initialized():            dist.init_process_group(backend='nccl', rank=rank, world_size=world_size)    # Set device    if torch.cuda.is_available():        device = torch.device(f'cuda:{local_rank}')        torch.cuda.set_device(device)    else:        device = torch.device('cpu')    return rank, world_size, devicedef cleanup():    """Clean up the distributed training process group"""    if dist.is_initialized():        dist.destroy_process_group()class SyntheticDataset(Dataset):    """Simple synthetic dataset for demo purposes"""    def __init__(self, size=10000, input_dim=512, num_classes=10):        self.size = size        self.input_dim = input_dim        self.num_classes = num_classes        # Generate synthetic data        np.random.seed(42)  # For reproducible results        self.data = torch.randn(size, input_dim)        # Create labels with some pattern        self.labels = torch.randint(0, num_classes, (size,))    def __len__(self):        return self.size    def __getitem__(self, idx):        return self.data[idx], self.labels[idx]

## Define the Transformer model with FSDP[​](#define-the-transformer-model-with-fsdp "Direct link to Define the Transformer model with FSDP")

This section defines a simple Transformer model for classification and the logic to apply FSDP sharding. While FSDP is typically used for large language models with 7B+ parameters, this example demonstrates the technique with a smaller 10M parameter model sharded across multiple H100 GPUs.

**Model architecture:**

*   `TransformerBlock`: A single transformer layer with multi-head attention and MLP
*   `SimpleTransformer`: A stack of transformer blocks with input projection and classification head
*   `apply_fsdp()`: Wraps model layers with FSDP for distributed training

FSDP shards the model parameters, gradients, and optimizer states across GPUs, reducing per-GPU memory requirements and enabling training of larger models.

Python

    class TransformerBlock(nn.Module):    """Simple transformer block for testing FSDP"""    def __init__(self, dim=512, num_heads=8, mlp_ratio=4):        super().__init__()        self.attention = nn.MultiheadAttention(dim, num_heads, batch_first=True)        self.norm1 = nn.LayerNorm(dim)        self.norm2 = nn.LayerNorm(dim)        mlp_dim = int(dim * mlp_ratio)        self.mlp = nn.Sequential(            nn.Linear(dim, mlp_dim),            nn.GELU(),            nn.Linear(mlp_dim, dim),        )    def forward(self, x):        # Self-attention        attn_out, _ = self.attention(x, x, x)        x = self.norm1(x + attn_out)        # MLP        mlp_out = self.mlp(x)        x = self.norm2(x + mlp_out)        return xclass SimpleTransformer(nn.Module):    """Simple transformer model for classification with FSDP"""    def __init__(self, input_dim=512, num_layers=64, num_classes=10):        super().__init__()        self.input_projection = nn.Linear(input_dim, input_dim)        self.layers = nn.ModuleList([            TransformerBlock(dim=input_dim) for _ in range(num_layers)        ])        self.norm = nn.LayerNorm(input_dim)        self.classifier = nn.Linear(input_dim, num_classes)    def forward(self, x):        # Add sequence dimension for transformer        x = x.unsqueeze(1)  # [batch, 1, input_dim]        x = self.input_projection(x)        for layer in self.layers:            x = layer(x)        x = self.norm(x)        # Global average pooling        x = x.mean(dim=1)  # [batch, input_dim]        return self.classifier(x)def apply_fsdp(model, world_size):    """Apply FSDP to the model"""    if world_size > 1:        print("Applying FSDP to model layers...")        # Apply fsdp to each transformer layer        for i, layer in enumerate(model.layers):            fully_shard(layer)            print(f"Applied FSDP to layer {i}")        # Apply FSDP to the entire model        fully_shard(model)        print("Applied FSDP to entire model")    else:        print("Single GPU detected, skipping FSDP setup")    return model

## Define the distributed training function[​](#define-the-distributed-training-function "Direct link to Define the distributed training function")

The training function is wrapped with the `@distributed` decorator from the serverless GPU API. This decorator handles:

*   Provisioning the specified number of GPUs (8 H100 GPUs in this example)
*   Setting up the distributed training environment
*   Managing the lifecycle of remote compute resources

The training function includes:

*   Model initialization and FSDP wrapping
*   Data loading with `DistributedSampler` for parallel data processing
*   Training loop with gradient updates
*   Periodic checkpoint saving using PyTorch's distributed checkpoint API
*   MLflow logging for experiment tracking

Checkpoints are saved to a Unity Catalog volume and logged as MLflow artifacts for versioning and reproducibility.

Python

    from serverless_gpu import distributedfrom serverless_gpu.compute import GPUTypeNUM_WORKERS = 8CHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{MODEL_NAME}"@distributed(gpus=NUM_WORKERS, gpu_type=GPUType.H100)def run_fsdp_training(num_workers=NUM_WORKERS):    """    Self-contained FSDP training demo using PyTorch 2.0+    Trains a simple neural network on synthetic data using FSDP    """    import mlflow    mlflow.start_run(run_name='fsdp_example')    def main_training():        """Main training function"""        print("Starting FSDP Training Demo...")        # Setup distributed training        rank, world_size, device = setup()        print(f"Rank: {rank}, World Size: {world_size}, Device: {device}")        print(f"PyTorch version: {torch.__version__}")        print(f"CUDA available: {torch.cuda.is_available()}")        if torch.cuda.is_available():            print(f"CUDA device count: {torch.cuda.device_count()}")            print(f"Current CUDA device: {torch.cuda.current_device()}")        # Create dataset and data loader        dataset = SyntheticDataset(size=10000, input_dim=512, num_classes=10)        # Use DistributedSampler if we have multiple processes        if world_size > 1:            sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank)            shuffle = False        else:            sampler = None            shuffle = True        dataloader = DataLoader(            dataset,            batch_size=32,            shuffle=shuffle,            sampler=sampler,            num_workers=num_workers,            pin_memory=True        )        # Create model        model = SimpleTransformer(input_dim=512, num_layers=4, num_classes=10).to(device)        # Apply FSDP        model = apply_fsdp(model, world_size)        print(f"Model created and moved to device: {device}")        if rank == 0:            print(f"Model parameters: {sum(p.numel() for p in model.parameters()):,}")        # Loss function and optimizer        criterion = nn.CrossEntropyLoss()        optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)        # Training loop        num_epochs = 5        loss_history = []        print(f"Training for {num_epochs} epochs...")        writer = StorageWriter(cache_staged_state_dict=False, path=CHECKPOINT_DIR)        for epoch in range(num_epochs):            if sampler:                sampler.set_epoch(epoch)            model.train()            total_loss = 0.0            num_batches = 0            epoch_start_time = time.time()            for batch_idx, (data, target) in enumerate(dataloader):                data, target = data.to(device), target.to(device)                # Zero gradients                optimizer.zero_grad()                # Forward pass                output = model(data)                loss = criterion(output, target)                # Backward pass                loss.backward()                mlflow.log_metric(                    key='loss',                    value=loss.item(),                    step=batch_idx,                )                # Update weights                optimizer.step()                total_loss += loss.item()                num_batches += 1                if batch_idx % 10 == 0:                    print(f'Saving checkpoint to {CHECKPOINT_DIR}/step{batch_idx}')                    state_dict = { 'app': AppState(model, optimizer) }                    ckpt_start_time = time.time()                    dcp.save(state_dict, storage_writer=writer, checkpoint_id=f"{CHECKPOINT_DIR}/step{batch_idx}")                    ckpt_time = time.time() - ckpt_start_time                    print(f'Checkpointing took {ckpt_time:.2f}s')                    mlflow.log_artifacts(f'{CHECKPOINT_DIR}/step{batch_idx}', artifact_path=f'checkpoints/step{batch_idx}')                    if rank == 0:                        print(f'Epoch {epoch+1}/{num_epochs}, Batch {batch_idx}, Loss: {loss.item():.6f}')            # Calculate average loss for this epoch            avg_loss = total_loss / num_batches            mlflow.log_metric(key='avg_loss', value=avg_loss)            loss_history.append(avg_loss)            epoch_time = time.time() - epoch_start_time            if rank == 0:                print(f'Epoch {epoch+1}/{num_epochs} with {num_batches} completed in {epoch_time:.2f}s. Average Loss: {avg_loss:.6f}')        # Verify loss is decreasing        if rank == 0:            print("\n=== FSDP Training Results ===")            print("Loss history:")            for i, loss in enumerate(loss_history):                print(f"Epoch {i+1}: {loss:.6f}")            # Check if loss is generally decreasing            initial_loss = loss_history[0]            final_loss = loss_history[-1]            loss_reduction = ((initial_loss - final_loss) / initial_loss) * 100            print(f"\nInitial Loss: {initial_loss:.6f}")            print(f"Final Loss: {final_loss:.6f}")            print(f"Loss Reduction: {loss_reduction:.2f}%")            if final_loss < initial_loss:                print("✅ SUCCESS: FSDP training is working! Loss is decreasing.")            else:                print("❌ WARNING: Loss did not decrease. Check training configuration.")            print(f"\nFSDP training completed successfully on {world_size} GPU(s)")        # Cleanup        cleanup()        mlflow.end_run()        return {            'initial_loss': loss_history[0] if loss_history else None,            'final_loss': loss_history[-1] if loss_history else None,            'loss_history': loss_history,            'world_size': world_size,            'device': str(device),            'fsdp_enabled': world_size > 1        }    # Run the training    return main_training()

## Run the distributed training[​](#run-the-distributed-training "Direct link to Run the distributed training")

Execute the training function to start distributed training across 8 H100 GPUs. The `.distributed()` method triggers remote execution on serverless GPU compute. Training progress, loss metrics, and checkpoints will be logged to MLflow.

This cell may take several minutes to complete as it provisions GPU resources, trains the model for 5 epochs, and saves checkpoints.

Python

    print("Starting FSDP Demo on Databricks Serverless GPU...")result = run_fsdp_training.distributed()print("FSDP Demo completed!")print(f"Training Results: {result}")

## Load a model checkpoint[​](#load-a-model-checkpoint "Direct link to Load a model checkpoint")

This section demonstrates how to load a saved checkpoint for inference or continued training. The checkpoint contains the model weights and optimizer state saved during training.

Note that when loading checkpoints outside of a distributed training context (no process group initialized), PyTorch's distributed checkpoint API automatically disables collective operations and loads the checkpoint on a single device.

Python

    def run_checkpoint_load_example():    # create the non FSDP-wrapped toy model    model = SimpleTransformer(input_dim=512, num_layers=4, num_classes=10)    optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)    state_dict = { 'app': AppState(model, optimizer)}    # print(state_dict)    # since no progress group is initialized, DCP will disable any collectives.    dcp.load(        state_dict=state_dict,        checkpoint_id=f'{CHECKPOINT_DIR}/step0',    )    model.load_state_dict(state_dict['app'].state_dict()['model'])run_checkpoint_load_example()

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you've learned how to use PyTorch FSDP for distributed training on serverless GPU compute, explore these resources to learn more:

*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training) - Learn about different distributed training strategies
*   [Best practices for serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability) - Optimize your GPU workloads
*   [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides) - Common issues and solutions
*   [PyTorch FSDP documentation](https://pytorch.org/docs/stable/fsdp.html) - Deep dive into FSDP features and configuration

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Distributed training using PyTorch FSDP on serverless GPU compute
