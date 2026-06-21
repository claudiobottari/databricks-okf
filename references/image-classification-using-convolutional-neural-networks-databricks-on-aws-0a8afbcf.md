---
title: Image classification using convolutional neural networks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-cnn-mnist
ingestedAt: "2026-06-18T08:08:44.012Z"
---

This notebook demonstrates how to train a [Convolutional Neural Network (CNN)](https://en.wikipedia.org/wiki/Convolutional_neural_network) for image classification using the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) and [PyTorch](https://pytorch.org/). The MNIST dataset contains 70,000 grayscale images of handwritten digits (0-9), making it ideal for learning image classification techniques.

You'll learn how to:

*   Connect your notebook to serverless GPU compute with an A10G GPU
*   Define a simple convolutional neural network architecture
*   Train the model on a single GPU and log metrics to [MLflow](https://docs.databricks.com/aws/en/mlflow/)
*   Save model checkpoints to a Unity Catalog Volume
*   Load and evaluate the trained model

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

This notebook requires a GPU to train the neural network efficiently. Follow these steps to connect to serverless GPU compute:

1.  Click the **Connect** dropdown at the top of the notebook.
2.  Select **Serverless GPU**.
3.  Open the **Environment** side panel on the right side of the notebook.
4.  Set **Accelerator** to **1xA10** for this demo.
5.  Select **AI v5** from the **Environment** dropdown.
6.  Select **Apply** and click **Confirm** to apply this environment to your notebook.

For more information, see [Serverless GPU compute](https://docs.databricks.com/aws/en/compute/serverless/).

## Configure checkpoint storage location[​](#configure-checkpoint-storage-location "Direct link to Configure checkpoint storage location")

The following cell creates [widget parameters](https://docs.databricks.com/aws/en/notebooks/widgets) to specify where model checkpoints will be saved in Unity Catalog. These parameters define:

*   `uc_catalog`: The Unity Catalog catalog name
*   `uc_schema`: The schema (database) within the catalog
*   `uc_volume`: The volume for storing checkpoint files
*   `uc_model_name`: The subdirectory within the volume for this specific model

These values are used throughout the notebook to construct the checkpoint path: `/Volumes/{uc_catalog}/{uc_schema}/{uc_volume}/{uc_model_name}`

The following cell uses placeholder values as defaults. Update the values using the widgets at the top of the notebook. Or, update the default values directly in the next cell.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_volume", "checkpoints")dbutils.widgets.text("uc_model_name", "cnn_mnist")

## Define the convolutional neural network[​](#define-the-convolutional-neural-network "Direct link to Define the convolutional neural network")

The following cell defines a simple CNN architecture for image classification. The network consists of:

*   Two convolutional layers with max pooling to extract features from images
*   Two fully connected layers to classify the extracted features
*   Dropout layers to prevent overfitting

The code also defines helper classes for checkpointing the model and optimizer state to a Unity Catalog Volume, and functions to set up distributed training (used for multi-GPU scenarios).

This implementation is adapted from the [Horovod PyTorch MNIST Example](https://github.com/horovod/horovod/blob/master/examples/pytorch/pytorch_mnist.py).

Python

    import torchimport torch.nn as nnimport torch.nn.functional as Fimport osimport torch.distributed as distimport torch.distributed.checkpoint as dcpfrom datetime import timedeltafrom torch.distributed.checkpoint.state_dict import get_state_dict, set_state_dictfrom torch.distributed.checkpoint.stateful import Statefulclass Net(nn.Module):    def __init__(self):        super(Net, self).__init__()        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)        self.conv2_drop = nn.Dropout2d()        self.fc1 = nn.Linear(320, 50)        self.fc2 = nn.Linear(50, 10)    def forward(self, x):        x = F.relu(F.max_pool2d(self.conv1(x), 2))        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))        x = x.view(-1, 320)        x = F.relu(self.fc1(x))        x = F.dropout(x, training=self.training)        x = self.fc2(x)        return F.log_softmax(x, dim=1)UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_VOLUME = dbutils.widgets.get("uc_volume")UC_MODEL_NAME = dbutils.widgets.get("uc_model_name")# Ensure that the UC Volume directory exists firstCHECKPOINT_DIR = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/{UC_MODEL_NAME}"class AppState(Stateful):    """This is a useful wrapper for checkpointing the Application State. Since this object is compliant    with the Stateful protocol, DCP will automatically call state_dict/load_stat_dict as needed in the    dcp.save/load APIs.    Note: We take advantage of this wrapper to hande calling distributed state dict methods on the model    and optimizer.    """    def __init__(self, model, optimizer=None):        self.model = model        self.optimizer = optimizer    def state_dict(self):        # this line automatically manages FSDP FQN's, as well as sets the default state dict type to FSDP.SHARDED_STATE_DICT        model_state_dict, optimizer_state_dict = get_state_dict(self.model, self.optimizer)        return {            "model": model_state_dict,            "optim": optimizer_state_dict        }    def load_state_dict(self, state_dict):        # sets our state dicts on the model and optimizer, now that we've loaded        set_state_dict(            self.model,            self.optimizer,            model_state_dict=state_dict["model"],            optim_state_dict=state_dict["optim"]        )def setup():    rank = int(os.environ["RANK"])    world_size = int(os.environ["WORLD_SIZE"])    # Shorter timeouts help surface failures quickly instead of hanging    dist.init_process_group(        backend="nccl",        timeout=timedelta(seconds=120),        init_method="env://",        rank=rank,        world_size=world_size,    )    torch.cuda.set_device(int(os.environ.get("LOCAL_RANK", 0)))    dist.barrier()    if rank == 0:        print("PG up; all ranks reached barrier")def cleanup():    try:        dist.barrier()    finally:        dist.destroy_process_group()

### Configure training parameters[​](#configure-training-parameters "Direct link to Configure training parameters")

The following cell sets the hyperparameters for training:

*   `batch_size`: Number of images processed in each training iteration
*   `num_epochs`: Number of complete passes through the training dataset
*   `momentum`: Momentum factor for the SGD optimizer
*   `log_interval`: Frequency of logging training progress

Python

    # Specify training parametersbatch_size = 100num_epochs = 5momentum = 0.5log_interval = 100

### Define the training loop[​](#define-the-training-loop "Direct link to Define the training loop")

The following cell defines the `train_one_epoch` function, which:

*   Iterates through batches of training data
*   Performs forward and backward propagation
*   Updates model weights using the optimizer
*   Logs training loss to MLflow at regular intervals

Python

    def train_one_epoch(model, device, data_loader, optimizer, epoch):    model.train()    for batch_idx, (data, target) in enumerate(data_loader):        data, target = data.to(device), target.to(device)        optimizer.zero_grad()        output = model(data)        loss = F.nll_loss(output, target)        loss.backward()        optimizer.step()        if batch_idx % log_interval == 0:            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(                epoch, batch_idx * len(data), len(data_loader) * len(data),                100. * batch_idx / len(data_loader), loss.item()))            # Log metrics            mlflow.log_metric('loss', loss.item(), step=epoch * len(data_loader) + batch_idx)

## Train the model on a single GPU[​](#train-the-model-on-a-single-gpu "Direct link to Train the model on a single GPU")

The following cell defines the main training function that:

*   Loads the MNIST training dataset
*   Initializes the model and optimizer
*   Trains the model for the specified number of epochs
*   Saves checkpoints to the Unity Catalog Volume after each epoch
*   Logs metrics to MLflow for experiment tracking

Python

    import mlflowimport torch.optim as optimfrom torchvision import datasets, transformsdef train(learning_rate):  with mlflow.start_run() as run:    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')    train_dataset = datasets.MNIST(      'data',      train=True,      download=True,      transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]))    data_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)    model = Net().to(device)    optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=momentum)    with torch.no_grad():      input_example, _ = next(iter(data_loader))      output_example = model(input_example.to(device))    for epoch in range(1, num_epochs + 1):      train_one_epoch(model, device, data_loader, optimizer, epoch)      state_dict = { "app": AppState(model, optimizer) }      dcp.save(state_dict, checkpoint_id=CHECKPOINT_DIR)      print(f"saved checkpoint to {CHECKPOINT_DIR}")

### Run the training function[​](#run-the-training-function "Direct link to Run the training function")

The following cell executes the `train` function with a learning rate of 0.001. The training process will:

*   Download the MNIST dataset (if not already cached)
*   Train the model for 5 epochs
*   Display training progress and loss values
*   Save model checkpoints to the Unity Catalog Volume
*   Log metrics to MLflow

Training typically takes a few minutes on an A10G GPU.

Python

    train(learning_rate = 0.001)

## Load and evaluate the trained model[​](#load-and-evaluate-the-trained-model "Direct link to Load and evaluate the trained model")

After training, you can load the model from the checkpoint and evaluate its performance on the test dataset.

The following cell defines a `test` function that:

*   Loads the model state from the Unity Catalog Volume checkpoint
*   Downloads the MNIST test dataset
*   Evaluates the model on test data
*   Calculates and displays the average test loss

Python

    def test():  # Load model state from checkpoint using dcp  model = Net()  optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=momentum)  app_state = AppState(model, optimizer)  state_dict = { "app": app_state }  dcp.load(state_dict, checkpoint_id=CHECKPOINT_DIR)  model.eval()  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  model.to(device)  test_dataset = datasets.MNIST(    'data',    train=False,    download=True,    transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]))  data_loader = torch.utils.data.DataLoader(test_dataset)  test_loss = 0  for data, target in data_loader:      data, target = data.to(device), target.to(device)      output = model(data)      test_loss += F.nll_loss(output, target)  test_loss /= len(data_loader.dataset)  print("Average test loss: {}".format(test_loss.item()))

### Run the evaluation[​](#run-the-evaluation "Direct link to Run the evaluation")

The following cell executes the `test` function to evaluate the trained model on the MNIST test dataset. A lower test loss indicates better model performance.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Congratulations! You've successfully trained an image classification model using serverless GPU compute. You learned how to:

*   Configure and connect to serverless GPU compute
*   Define a convolutional neural network architecture
*   Train a model with PyTorch and log metrics to MLflow
*   Save model checkpoints to Unity Catalog Volumes
*   Load and evaluate a trained model

### Disconnect from GPU compute[​](#disconnect-from-gpu-compute "Direct link to Disconnect from GPU compute")

To avoid unnecessary GPU usage, manually disconnect from your GPU:

1.  Select **Connected** at the top of the notebook
2.  Hover over **Serverless**
3.  Select **Terminate** from the dropdown menu
4.  Select **Confirm** to terminate

**Note**: If you don't manually disconnect, your connection auto-terminates after 60 minutes of inactivity.

## Next steps[​](#next-steps "Direct link to Next steps")

Explore these resources to learn more about machine learning on Databricks:

*   [Best practices for serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   [MLflow tracking](https://docs.databricks.com/aws/en/mlflow/tracking)
*   [Train models with PyTorch](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Image classification using convolutional neural networks
