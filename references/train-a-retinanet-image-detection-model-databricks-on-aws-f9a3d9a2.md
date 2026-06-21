---
title: Train a RetinaNet image detection model | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-retinanet-image-detection-model-training
ingestedAt: "2026-06-18T08:09:05.920Z"
---

This notebook demonstrates how to train a RetinaNet object detection model from scratch using PyTorch and torchvision on Databricks serverless GPU compute. RetinaNet is a single-stage object detection model that uses a Feature Pyramid Network (FPN) and focal loss to handle class imbalance.

The notebook covers:

*   Loading and transforming the COCO dataset for object detection
*   Training a RetinaNet model with ResNet-50 backbone on a single GPU
*   Scaling training across multiple GPUs using Distributed Data Parallel (DDP)
*   Logging training metrics with MLflow

## Connect to serverless GPU compute[​](#connect-to-serverless-gpu-compute "Direct link to Connect to serverless GPU compute")

To run this notebook, connect to serverless GPU compute with **1xA10** for single-GPU training or **8xH100** for the distributed section.

1.  Click the notebook's compute selector in the top right and select **Serverless GPU**.
2.  On the right side, click the environment button.
3.  Select **1xA10** or **8xH100** as the **Accelerator**.
4.  Select **AI v5** as your environment, then click **Apply**.

## Install required packages[​](#install-required-packages "Direct link to Install required packages")

Install pycocotools for COCO dataset utilities and restart the Python environment to load the new package.

Python

    %pip install pycocotoolsdbutils.library.restartPython()

Define widgets to specify the Unity Catalog catalog, schema, and volume where the COCO dataset is stored.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_volume", "coco_data")UC_CATALOG = dbutils.widgets.get("uc_catalog")UC_SCHEMA = dbutils.widgets.get("uc_schema")UC_VOLUME = dbutils.widgets.get("uc_volume")print(f"UC_CATALOG: {UC_CATALOG}")print(f"UC_SCHEMA: {UC_SCHEMA}")print(f"UC_VOLUME: {UC_VOLUME}")

## Import PyTorch libraries[​](#import-pytorch-libraries "Direct link to Import PyTorch libraries")

Import torch and torchvision for building and training the image detection model.

Python

    import torchimport torchvision

## Import model and dataset classes[​](#import-model-and-dataset-classes "Direct link to Import model and dataset classes")

Import the RetinaNet model architecture and COCO dataset utilities from torchvision.

Python

    import osfrom torchvision.models.detection import retinanet_resnet50_fpn_v2# For this example we will be using a default Dataset from torchfrom torchvision.datasets import CocoDetection

## Import distributed training utilities[​](#import-distributed-training-utilities "Direct link to Import distributed training utilities")

Import PyTorch distributed training modules and the serverless GPU distributed decorator for multi-GPU training.

## Define training hyperparameters and data paths[​](#define-training-hyperparameters-and-data-paths "Direct link to Define training hyperparameters and data paths")

Configure the data paths, batch size, number of classes, learning rate, and other training parameters. Adjust `BATCH_SIZE` and `NUM_EPOCHS` based on the GPU type and training requirements.

Python

    import torch.distributed as distfrom serverless_gpu import distributed

Python

    DATA_PATH = f"/Volumes/{UC_CATALOG}/{UC_SCHEMA}/{UC_VOLUME}/"TRAIN_IMG_PATH = os.path.join(DATA_PATH, "val2017")TRAIN_ANN_PATH = os.path.join(DATA_PATH, "annotations", "instances_val2017.json")BATCH_SIZE = 2 # Please use batch size of 8 with H100 for best performanceNUM_CLASSES = 91LEARNING_RATE = 0.005MOMENTUM = 0.9WEIGHT_DECAY = 0.0005NUM_EPOCHS = 1 # Update num_epochs accordingly

## Initialize the RetinaNet model[​](#initialize-the-retinanet-model "Direct link to Initialize the RetinaNet model")

Create a RetinaNet model with ResNet-50 backbone without pre-trained weights, configured for the number of classes in the COCO dataset.

Python

    # Since we are training the model from scratch, we need to initialize weights to Nonemodel = retinanet_resnet50_fpn_v2(weights=None, num_classes=NUM_CLASSES)

## Transform images and annotations into model inputs[​](#transform-images-and-annotations-into-model-inputs "Direct link to Transform images and annotations into model inputs")

The model requires inputs as tensors with shape (C, H, W), float32 data type, and normalized range (0.0 to 1.0). The `get_transform` function converts PIL images and applies data augmentation. The `CocoWrapper` class wraps the COCO dataset to format bounding boxes and labels correctly.

Python

    from torchvision.transforms import v2from torchvision import tv_tensorsdef get_transform(train):  transforms = []  transforms.append(v2.ToImage())  transforms.append(v2.ToDtype(torch.float32, scale=True))  if train:    transforms.append(v2.RandomHorizontalFlip())  return v2.Compose(transforms)class CocoWrapper(CocoDetection):  def __init__(self, root, annFile, transforms=None):    super().__init__(root, annFile)    self._transforms = transforms  def __getitem__(self, idx):    img, target = super().__getitem__(idx)    image_id = self.ids[idx]    boxes = []    labels = []    for obj in target:      x, y, w, h = obj["bbox"]      boxes.append([x, y, x + w, y + h])      labels.append(obj["category_id"])    if len(boxes) == 0:      boxes = torch.zeros((0, 4), dtype=torch.float32)      labels = torch.zeros((0,), dtype=torch.int64)    else:      boxes = torch.as_tensor(boxes, dtype=torch.float32)      labels = torch.as_tensor(labels, dtype=torch.int64)    w, h = img.size    boxes = torchvision.tv_tensors.BoundingBoxes(      data=boxes,      format=torchvision.tv_tensors.BoundingBoxFormat.XYXY,      canvas_size=(h, w)    )    final_target = {      "boxes": boxes,      "labels": labels,      "image_id": torch.tensor([image_id])    }    if self._transforms is not None:      img, final_target = self._transforms(img, final_target)    return img, final_targetdataset = CocoWrapper(  root = TRAIN_IMG_PATH,  annFile=TRAIN_ANN_PATH,  transforms=get_transform(train=True))# Sanity Checkimg, target = dataset[0]print("Image type:", type(img))print("Image shape:", img.shape)        # should be [3, H, W]print("Image dtype:", img.dtype)print("\nTarget keys:", target.keys())print("Boxes shape:", target["boxes"].shape)print("Labels shape:", target["labels"].shape)print("Image ID:", target["image_id"])

## Create the data loader[​](#create-the-data-loader "Direct link to Create the data loader")

Define a DataLoader with custom collation to batch images and targets for training.

Python

    from torch.utils.data import DataLoaderdef collate_fn(batch):    images, targets = list(zip(*batch))    return list(images), list(targets)train_loader = DataLoader(    dataset,    batch_size=BATCH_SIZE,    shuffle=True,    num_workers=16,    collate_fn=collate_fn,    pin_memory=True,    prefetch_factor=2 # Please use a prefetch_factor of 4 with H100 for best performance)

## Configure the optimizer[​](#configure-the-optimizer "Direct link to Configure the optimizer")

Set up the SGD optimizer with learning rate, momentum, and weight decay parameters.

Python

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')model.to(device)params = [p for p in model.parameters() if p.requires_grad]optimizer = torch.optim.SGD(    params,    lr=LEARNING_RATE,    momentum=MOMENTUM,    weight_decay=WEIGHT_DECAY)

## Train the model on a single GPU[​](#train-the-model-on-a-single-gpu "Direct link to Train the model on a single GPU")

Run the training loop for the specified number of epochs, logging loss metrics to MLflow.

Python

    import timeimport mlflowmodel.train()lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)with mlflow.start_run():    for epoch in range(NUM_EPOCHS):        start_time = time.time()        epoch_loss = 0        for i, (images, targets) in enumerate(train_loader):            images = list(image.to(device) for image in images)            targets = [{k: v.to(device) for k, v in t.items()} for t in targets]            loss_dict = model(images, targets)            losses = sum(loss for loss in loss_dict.values())            optimizer.zero_grad()            losses.backward()            optimizer.step()            epoch_loss += losses.item()            mlflow.log_metric("loss", losses.item(), step=epoch * len(train_loader) + i)            if i % 50 == 0:                print(f"Epoch {epoch+1} | Step {i}/{len(train_loader)} | Loss: {losses.item():.4f}")        lr_scheduler.step()        end_time = time.time()        avg_loss = epoch_loss / len(train_loader)        mlflow.log_metric("epoch_avg_loss", avg_loss, step=epoch)        print(f"Epoch {epoch+1} Finished! Avg Loss: {avg_loss:.4f} | Time: {(end_time - start_time)/60:.2f} min")print("Training Complete.")

## Train with distributed data parallel (DDP)[​](#train-with-distributed-data-parallel-ddp "Direct link to Train with distributed data parallel (DDP)")

Scale training across multiple GPUs using the `@distributed` decorator. This approach copies data to local storage on each worker and uses DistributedSampler to partition the dataset across GPUs. All imports, transforms, the dataset, and the DataLoader are redefined inside the training function, as required by the distributed execution model.

Python

    from datetime import timedeltaBATCH_SIZE_PER_GPU = 8  # for better performance with H100@distributed(gpus=8, gpu_type='H100')def train_distributed():    import os    import torch    import torch.distributed as dist    import time    import shutil    import torchvision    import mlflow    from torch.utils.data import DataLoader    from torchvision.models.detection import retinanet_resnet50_fpn_v2    from torchvision.transforms import v2    from torchvision import tv_tensors    from torchvision.datasets import CocoDetection    def get_transform(train):        transforms = []        transforms.append(v2.ToImage())        transforms.append(v2.ToDtype(torch.float32, scale=True))        if train:            transforms.append(v2.RandomHorizontalFlip())        return v2.Compose(transforms)    def collate_fn(batch):        images, targets = list(zip(*batch))        return list(images), list(targets)    class CocoWrapper(CocoDetection):        def __init__(self, root, annFile, transforms=None):            super().__init__(root, annFile)            self._transforms = transforms        def __getitem__(self, idx):            img, target = super().__getitem__(idx)            image_id = self.ids[idx]            boxes = []            labels = []            for obj in target:                x, y, w, h = obj["bbox"]                boxes.append([x, y, x + w, y + h])                labels.append(obj["category_id"])            if len(boxes) == 0:                boxes = torch.zeros((0, 4), dtype=torch.float32)                labels = torch.zeros((0,), dtype=torch.int64)            else:                boxes = torch.as_tensor(boxes, dtype=torch.float32)                labels = torch.as_tensor(labels, dtype=torch.int64)            w, h = img.size            boxes = torchvision.tv_tensors.BoundingBoxes(                data=boxes,                format=torchvision.tv_tensors.BoundingBoxFormat.XYXY,                canvas_size=(h, w)            )            final_target = {                "boxes": boxes,                "labels": labels,                "image_id": torch.tensor([image_id])            }            if self._transforms is not None:                img, final_target = self._transforms(img, final_target)            return img, final_target    dist.init_process_group(backend="nccl", timeout=timedelta(minutes=30))    rank = int(os.environ["RANK"])    local_rank = int(os.environ["LOCAL_RANK"])    world_size = int(os.environ["WORLD_SIZE"])    torch.cuda.set_device(local_rank)    device = torch.device(f"cuda:{local_rank}")    uc_source_path = DATA_PATH    local_dest_path = "/tmp/coco_data"    if local_rank == 0:        if not os.path.exists(local_dest_path):            print(f"Rank {rank}: Copying data from {uc_source_path} to {local_dest_path}...")            shutil.copytree(uc_source_path, local_dest_path, dirs_exist_ok=True)            print(f"Rank {rank}: Data copy finished!")        else:            print(f"Rank {rank}: Data already exists in local temp.")    dist.barrier()    local_train_img_path = os.path.join(local_dest_path, "val2017")    local_train_ann_path = os.path.join(local_dest_path, "annotations", "instances_val2017.json")    dataset = CocoWrapper(        root=local_train_img_path,        annFile=local_train_ann_path,        transforms=get_transform(train=True)    )    train_sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank, shuffle=True)    train_loader = DataLoader(        dataset,        batch_size=BATCH_SIZE_PER_GPU,        shuffle=False,        num_workers=8, # 8 workers * 8 GPUs = 64 total CPU threads        collate_fn=collate_fn,        pin_memory=True,        prefetch_factor=4,        sampler=train_sampler    )    model = retinanet_resnet50_fpn_v2(weights=None, num_classes=NUM_CLASSES)    model.to(device)    model = DDP(model, device_ids=[local_rank])    params = [p for p in model.parameters() if p.requires_grad]    optimizer = torch.optim.SGD(params, lr=0.04, momentum=0.9, weight_decay=0.0005)    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)    model.train()    if rank == 0:        print(f"Training on {world_size} GPUs. Global Batch Size: {BATCH_SIZE_PER_GPU * world_size}")    with mlflow.start_run():        for epoch in range(NUM_EPOCHS):            train_sampler.set_epoch(epoch)            start_time = time.time()            epoch_loss = 0            for i, (images, targets) in enumerate(train_loader):                images = [image.to(device) for image in images]                targets = [{k: v.to(device) for k, v in t.items()} for t in targets]                loss_dict = model(images, targets)                losses = sum(loss for loss in loss_dict.values())                optimizer.zero_grad()                losses.backward()                optimizer.step()                epoch_loss += losses.item()                if rank == 0:                    mlflow.log_metric("loss", losses.item(), step=epoch * len(train_loader) + i)                if rank == 0 and i % 50 == 0:                    print(f"Rank 0 | Step {i}/{len(train_loader)} | Loss: {losses.item():.4f}")            lr_scheduler.step()            if rank == 0:                avg_loss = epoch_loss / len(train_loader)                mlflow.log_metric("epoch_avg_loss", avg_loss, step=epoch)                print(f"Epoch {epoch+1} Finished! Avg Loss: {avg_loss:.4f} | Time: {(time.time() - start_time)/60:.2f} min")    dist.destroy_process_group()train_distributed.distributed()

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Best practices for serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability)
*   [Troubleshoot issues on serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides)
*   [Multi-GPU and multi-node distributed training](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training)
*   [Train models with PyTorch](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch)
*   [Log models with MLflow](https://docs.databricks.com/aws/en/mlflow/models)

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Train a RetinaNet image detection model
