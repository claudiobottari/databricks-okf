---
title: Distributed training of two tower recommendation model using Lightning | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-recommender-system-lightning
ingestedAt: "2026-06-18T08:09:03.358Z"
---

This notebook demonstrates how to create a two tower recommendation model using the PyTorch Lightning `Trainer` API with distributed training across 8 H100 GPUs on a single node.

Reminders:

*   For this demo, attach to **GPU 8xH100** to leverage distributed training across multiple GPUs.
*   The `@distributed` decorator from the `serverless_gpu` Python library will distribute the PyTorch Lightning training function across 8 H100 GPUs.

To get started, configure your notebook to use serverless GPU:

1.  Click the **Connect** dropdown at the top to open the compute selector.
2.  Select **Serverless GPU**.
3.  Open the **Environment** panel on the right side.
4.  Select **8xH100** as your accelerator.
5.  Select **AI v5** as your environment. Click **Apply**, then **Confirm**.

Your notebook is now connected to serverless GPU compute. The `@distributed` decorator will handle launching your training across all 8 GPUs.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before running through this demo, configure the widget variables at the top of this notebook:

*   `uc_catalog`: The Unity Catalog catalog where the trained model is registered.
*   `uc_schema`: The Unity Catalog schema from the above catalog where the trained model is registered.

The dataset is downloaded automatically during the notebook run. The model is saved in `<uc_catalog>.<uc_schema>.<model_name_in_registry>`.

## Two tower recommendation model[​](#two-tower-recommendation-model "Direct link to Two tower recommendation model")

For more insight into the two tower recommendation model, view the following resources:

*   [Hopsworks definition](https://www.hopsworks.ai/dictionary/two-tower-embedding-model)
*   [TorchRec's training implementation](https://github.com/pytorch/torchrec/blob/main/examples/retrieval/two_tower_train.py#L75)

### Instructions:[​](#instructions "Direct link to Instructions:")

Below, the code walks you through how to:

1.  Install packages
2.  Download and prepare dataset
3.  Required training configurations
4.  Two tower recommendation model definition
5.  Creating the main training function
6.  Training the two tower model
7.  Perform inference
8.  Register your model to MLflow for serving

## 1) Install packages[​](#1-install-packages "Direct link to 1) Install packages")

The Databricks AI v5 environment includes most of the libraries required for this example. Run the following cell to install the additional packages that are not yet part of the environment.

Python

    %pip install --no-cache-dir --force-reinstall --no-deps --index-url https://download.pytorch.org/whl/cu129 torchaudio==2.9.0 fbgemm-gpu==1.4.0%pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cu129 torchrec==1.4.0dbutils.library.restartPython()

The following cell consolidates all the imports used throughout this example.

Python

    # General Importsimport osimport urllib.requestimport zipfilefrom dataclasses import dataclass, fieldfrom typing import Any, Dict, List, Optional, Tuple# Data Processing Importsimport pandas as pdimport numpy as npfrom sklearn.preprocessing import LabelEncoderfrom sklearn.model_selection import train_test_split# Databricks Specific Importsimport mlflowfrom mlflow.models.signature import infer_signaturefrom mlflow.pyfunc import PythonModel# Torch Specific Importsimport torchfrom torch import nnfrom torch.utils.data import DataLoader, Datasetfrom torchmetrics.classification import AUROC# PyTorch Lightningimport pytorch_lightning as plfrom pytorch_lightning import Trainerfrom pytorch_lightning.callbacks import LearningRateMonitor, ModelCheckpoint, DeviceStatsMonitorfrom pytorch_lightning.loggers import MLFlowLogger# TorchRec Specific Importsfrom torchrec.datasets.utils import Batchfrom torchrec.modules.embedding_configs import EmbeddingBagConfigfrom torchrec.modules.embedding_modules import EmbeddingBagCollectionfrom torchrec.modules.mlp import MLPfrom torchrec.optim.keyed import KeyedOptimizerWrapperfrom torchrec.sparse.jagged_tensor import KeyedJaggedTensor

## 2) Download and prepare dataset[​](#2-download-and-prepare-dataset "Direct link to 2) Download and prepare dataset")

Download the [Learning from Sets](https://files.grouplens.org/datasets/learning-from-sets-2019/) dataset, preprocess it, and split into train/validation/test sets.

Python

    dbutils.widgets.text("uc_catalog", "main")dbutils.widgets.text("uc_schema", "default")dbutils.widgets.text("uc_volume", "recsys")uc_catalog = dbutils.widgets.get("uc_catalog")uc_schema = dbutils.widgets.get("uc_schema")uc_volume = dbutils.widgets.get("uc_volume")

Python

    DATASET_URL = "https://files.grouplens.org/datasets/learning-from-sets-2019/learning-from-sets-2019.zip"DATASET_PATH = f"/Volumes/{uc_catalog}/{uc_schema}/{uc_volume}/dataset"ZIP_PATH = f"{DATASET_PATH}/learning-from-sets-2019.zip"CSV_PATH = f"{DATASET_PATH}/learning-from-sets-2019/item_ratings.csv"# Download and extractif not os.path.exists(CSV_PATH):    os.makedirs(DATASET_PATH, exist_ok=True)    print("Downloading dataset...")    urllib.request.urlretrieve(DATASET_URL, ZIP_PATH)    with zipfile.ZipFile(ZIP_PATH, "r") as zf:        zf.extractall(DATASET_PATH)    print("Download complete.")# Load and preprocessdf = pd.read_csv(CSV_PATH)df = df.sort_values(["userId", "movieId"]).head(100_000)# Encode userId to contiguous integersuser_encoder = LabelEncoder()df["userId"] = user_encoder.fit_transform(df["userId"])# Binarize ratings: 1 if >= mean, else 0mean_rating = df["rating"].mean()df["label"] = (df["rating"] >= mean_rating).astype(np.int64)df = df[["userId", "movieId", "label"]]# Compute embedding table sizes from datanum_users = int(df["userId"].nunique())num_movies = int(df["movieId"].nunique())print(f"Dataset: {len(df)} rows, {num_users} users, {num_movies} movies")# Split: 70% train, 21% validation, 9% testtrain_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)val_df, test_df = train_test_split(temp_df, test_size=0.33, random_state=42)print(f"Train: {len(train_df)}, Validation: {len(val_df)}, Test: {len(test_df)}")

Python

    class RecDataset(Dataset):    """Wraps a DataFrame with columns [userId, movieId, label] as a PyTorch Dataset."""    def __init__(self, dataframe: pd.DataFrame):        self.users = dataframe["userId"].values.astype(np.int64)        self.movies = dataframe["movieId"].values.astype(np.int64)        self.labels = dataframe["label"].values.astype(np.int64)    def __len__(self) -> int:        return len(self.labels)    def __getitem__(self, idx: int) -> dict:        return {"userId": self.users[idx], "movieId": self.movies[idx], "label": self.labels[idx]}def get_dataloader(dataframe: pd.DataFrame, batch_size: int = 1024, shuffle: bool = True) -> DataLoader:    return DataLoader(RecDataset(dataframe), batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)

## 3) Required training configurations[​](#3-required-training-configurations "Direct link to 3) Required training configurations")

All the arguments and information required for this training example are consolidated into the following cell. All of these can be modified to suit your use case.

Python

    @dataclassclass Args:    epochs: int = 3    embedding_dim: int = 128    layer_sizes: List[int] = field(default_factory=lambda: [128, 64])    learning_rate: float = 0.01    batch_size: int = 1024cat_cols = ["userId", "movieId"]emb_counts = [num_users, num_movies]  # computed from data in section 2

## 4) Two tower recommendation model definition[​](#4-two-tower-recommendation-model-definition "Direct link to 4) Two tower recommendation model definition")

This section defines the model using PyTorch Lightning. For more information, see the documentation:

*   [Hopsworks definition](https://www.hopsworks.ai/dictionary/two-tower-embedding-model)
*   [TorchRec's training implementation](https://github.com/pytorch/torchrec/blob/main/examples/retrieval/two_tower_train.py#L75)
*   [PyTorch Lightning trainer](https://lightning.ai/docs/pytorch/stable/common/trainer.html)

Python

    class TwoTowerModel(nn.Module):    def __init__(        self,        embedding_bag_collection: EmbeddingBagCollection,        layer_sizes: List[int],        device: Optional[torch.device] = None    ) -> None:        super().__init__()        assert len(embedding_bag_collection.embedding_bag_configs()) == 2, "Expected two EmbeddingBags in the two tower model"        assert embedding_bag_collection.embedding_bag_configs()[0].embedding_dim == embedding_bag_collection.embedding_bag_configs()[1].embedding_dim, "Both EmbeddingBagConfigs must have the same dimension"        embedding_dim = embedding_bag_collection.embedding_bag_configs()[0].embedding_dim        self._feature_names_query: List[str] = embedding_bag_collection.embedding_bag_configs()[0].feature_names        self._candidate_feature_names: List[str] = embedding_bag_collection.embedding_bag_configs()[1].feature_names        self.ebc = embedding_bag_collection        self.query_proj = MLP(in_size=embedding_dim, layer_sizes=layer_sizes, device=device)        self.candidate_proj = MLP(in_size=embedding_dim, layer_sizes=layer_sizes, device=device)    def forward(self, kjt: KeyedJaggedTensor) -> Tuple[torch.Tensor, torch.Tensor]:        pooled_embeddings = self.ebc(kjt)        query_embedding: torch.Tensor = self.query_proj(            torch.cat(                [pooled_embeddings[feature] for feature in self._feature_names_query],                dim=1,            )        )        candidate_embedding: torch.Tensor = self.candidate_proj(            torch.cat(                [pooled_embeddings[feature] for feature in self._candidate_feature_names],                dim=1,            )        )        return query_embedding, candidate_embeddingclass LitTwoTower(pl.LightningModule):    """    PyTorch Lightning module wrapping a TwoTowerModel.    Uses torchmetrics AUROC for train/val metrics.    """    def __init__(        self,        two_tower: nn.Module,        device: torch.device,        emb_counts: Optional[List[int]],        cat_cols: List[str],        lr: float = 1e-3,    ) -> None:        super().__init__()        self.two_tower = two_tower        self.loss_fn = nn.BCEWithLogitsLoss()        self.train_auroc = AUROC(task="binary")        self.val_auroc = AUROC(task="binary")        self.lr = lr        # Store metadata used in batch transform        self.emb_counts = emb_counts        self.cat_cols = cat_cols        self.save_hyperparameters(ignore=["two_tower", "device"])    def forward(self, batch: Dict[str, Any]) -> torch.Tensor:        kjt_batch = self._transform_to_torchrec_batch(batch, self.emb_counts)        query_embedding, candidate_embedding = self.two_tower(kjt_batch.sparse_features)        logits = (query_embedding * candidate_embedding).sum(dim=1).squeeze()        return logits    def _loss(self, outputs: torch.Tensor, batch: Dict[str, Any]) -> torch.Tensor:        labels = self._get_batch_labels(batch)        return self.loss_fn(outputs, labels)    def _update_metric(self, batch: Dict[str, Any], outputs: Optional[torch.Tensor], metric: AUROC) -> None:        if outputs is None:            outputs = self.forward(batch)        preds = torch.sigmoid(outputs)        labels = self._get_batch_labels(batch)        metric.update(preds, labels)    def training_step(self, batch: Dict[str, Any], batch_idx: int):        logits = self.forward(batch)        loss = self._loss(logits, batch)        # Metric update        self._update_metric(batch, logits, self.train_auroc)        # Log both step and epoch loss series; enable sync_dist for multi-GPU/DDP        self.log("train_loss", loss, on_step=True, on_epoch=True, prog_bar=True, logger=True, sync_dist=True)        self.log("train_auroc", self.train_auroc, on_step=False, on_epoch=True, prog_bar=True,             logger=True, sync_dist=True)        return loss    def validation_step(self, batch: Dict[str, Any], batch_idx: int):        logits = self.forward(batch)        loss = self._loss(logits, batch)        self._update_metric(batch, logits, self.val_auroc)        # Typically only epoch-level val metrics are needed for monitoring        self.log("val_loss", loss, on_step=False, on_epoch=True, prog_bar=True, logger=True, sync_dist=True)        self.log("val_auroc", self.val_auroc, on_step=False, on_epoch=True, prog_bar=True,             logger=True, sync_dist=True)    def configure_optimizers(self):        optimizer = KeyedOptimizerWrapper(            dict(self.two_tower.named_parameters()),            lambda params: torch.optim.Adam(params, lr=self.lr),        )        return optimizer    def _get_batch_labels(self, batch: Dict[str, Any]) -> torch.Tensor:        return batch["label"].to(dtype=torch.float32, device=self.device)    def _transform_to_torchrec_batch(        self,        batch: Dict[str, Any],        num_embeddings_per_feature: Optional[List[int]],    ) -> Batch:        kjt_values_list = []        kjt_lengths_list = []        for col_idx, col_name in enumerate(self.cat_cols):            values = batch[col_name]            num_emb = num_embeddings_per_feature[col_idx]            kjt_values_list.append(values % num_emb)            kjt_lengths_list.append(torch.ones(len(values), dtype=torch.int64))        values_t = torch.cat(kjt_values_list).to(dtype=torch.int64, device=self.device)        lengths_t = torch.cat(kjt_lengths_list).to(device=self.device)        sparse_features = KeyedJaggedTensor.from_lengths_sync(            self.cat_cols,            values_t,            lengths_t,        )        labels = batch["label"].to(dtype=torch.int64, device=self.device)        return Batch(            dense_features=torch.zeros(1, device=self.device),            sparse_features=sparse_features,            labels=labels,        )def create_two_tower_model(args, device, cat_cols, emb_counts) -> LitTwoTower:    eb_configs = [        EmbeddingBagConfig(            name=f"t_{feature_name}",            embedding_dim=args.embedding_dim,            num_embeddings=emb_counts[feature_idx],            feature_names=[feature_name],        )        for feature_idx, feature_name in enumerate(cat_cols)    ]    ebc = EmbeddingBagCollection(tables=eb_configs, device=device)    base = TwoTowerModel(        embedding_bag_collection=ebc, layer_sizes=args.layer_sizes, device=device    )    lit = LitTwoTower(        base, cat_cols=cat_cols, emb_counts=emb_counts, device=device, lr=args.learning_rate    )    return lit

## 5) Create the main training function[​](#5-create-the-main-training-function "Direct link to 5) Create the main training function")

Next, use the `@distributed` decorator from `serverless_gpu` library together with the helper functions and the `Trainer` API by PyTorch Lightning to launch training on multiple GPUs.

Python

    # setup mlflow experimentusername = spark.sql("SELECT current_user()").first()['current_user()']experiment_path = f'/Users/{username}/sgc-torchrec-example'experiment = mlflow.set_experiment(experiment_path)os.environ["MLFLOW_EXPERIMENT_NAME"] = experiment_path

Python

    from serverless_gpu import distributed# setup arguments for training functionargs = Args(epochs=1)device = torch.device("cuda" if torch.cuda.is_available() else "cpu")CHECKPOINT_PATH = f"/Volumes/{uc_catalog}/{uc_schema}/{uc_volume}/checkpoints"@distributed(gpus=8, gpu_type="H100")def training_function(args=args, cat_cols=cat_cols, emb_counts=emb_counts, device=device,                      train_data=train_df, val_data=val_df, checkpoint_path=CHECKPOINT_PATH):    mlflow.pytorch.autolog()    model = create_two_tower_model(args, device=device, cat_cols=cat_cols, emb_counts=emb_counts)    train_dataloader = get_dataloader(train_data, batch_size=args.batch_size, shuffle=True)    eval_dataloader = get_dataloader(val_data, batch_size=args.batch_size, shuffle=False)    mlflow_logger = MLFlowLogger(        experiment_name=experiment_path,        log_model="all",    )    ckpt_cb = ModelCheckpoint(        dirpath=checkpoint_path,        monitor="val_auroc",        mode="max",        save_top_k=1,        save_last=True,                        # enables last_model_path        filename="{epoch}-{val_auroc:.4f}",    )    callbacks = [        LearningRateMonitor(logging_interval="step"),        DeviceStatsMonitor(),        ckpt_cb,    ]    trainer = Trainer(        max_epochs=args.epochs,        accelerator="gpu",        strategy="ddp",        devices=8,        log_every_n_steps=20,        logger=mlflow_logger,        callbacks=callbacks,    )    trainer.fit(        model,        train_dataloaders=train_dataloader,        val_dataloaders=eval_dataloader    )    # Return run_id and best checkpoint path    result = {        "run_id": trainer.logger.run_id,                   # MLflow run id        "best_model_checkpoint": ckpt_cb.best_model_path,  # best checkpoint path        "last_model_checkpoint": ckpt_cb.last_model_path   # last checkpoint path    }    return result

## 6) Train the two tower model using the serverless GPU distributed training API[​](#6-train-the-two-tower-model-using-the-serverless-gpu-distributed-training-api "Direct link to 6) Train the two tower model using the serverless GPU distributed training API")

Python

    result = training_function.distributed()

## 7) Test the best model checkpoint[​](#7-test-the-best-model-checkpoint "Direct link to 7) Test the best model checkpoint")

Retrieve the best model checkpoint and run test to verify results

Python

    print(f"Experiment Name: {experiment.name}")print(f"Experiment ID: {experiment.experiment_id}")print(f"Artifact Location: {experiment.artifact_location}")print(f"Lifecycle_stage: {experiment.lifecycle_stage}")ranked_checkpoints = mlflow.search_logged_models(  experiment_ids=[experiment.experiment_id],  output_format="list",  order_by=[{"field_name": "metrics.accuracy", "ascending": False}])best_checkpoint: mlflow.entities.LoggedModel = ranked_checkpoints[0]print(best_checkpoint.metrics[0])

Python

    run_id = best_checkpoint.source_run_idartifact_path = best_checkpoint.artifact_locationmodel_uri = f"runs:/{run_id}/{artifact_path}"two_tower_model = mlflow.pytorch.load_model(model_uri)num_batches = 5 # Number of batches to print out at a timebatch_size = 1 # Print out each individual rowtest_dataloader = iter(get_dataloader(test_df, batch_size=batch_size, shuffle=False))device = torch.device("cuda:0")two_tower_model.to(device)two_tower_model.eval()for _ in range(num_batches):    next_batch = next(test_dataloader)    expected_result = next_batch["label"][0]    actual_result = two_tower_model(next_batch)    actual_result = torch.sigmoid(actual_result)    print(f"Expected Result: {expected_result}; Actual Result: {actual_result.round().item()}")

## 8) Register your model to MLflow for serving[​](#8-register-your-model-to-mlflow-for-serving "Direct link to 8) Register your model to MLflow for serving")

When the model in the previous step looks correct, use the corresponding `run_id` from the latest run to register the model. To make this easy to serve, create a PyFunc that wraps the two tower model to take in a simpler input: `(Dict[str, List] -> List[float])`.

Python

    class TwoTowerWrapper(PythonModel):    """    MLflow PythonModel wrapper for TwoTower model that handles dictionary input and returns list outputs    """    def __init__(self, two_tower_model):        self.two_tower_model = two_tower_model    def predict(self, model_input: Dict[str, List]) -> List[float]:        batch = {key: torch.tensor(value) for key, value in model_input.items()}        if "label" not in batch:            batch["label"] = torch.zeros(len(next(iter(batch.values()))))        with torch.no_grad():            output = self.two_tower_model(batch).cpu()        output = torch.sigmoid(output)        return output.tolist()

Python

    def preprocess_data(batch):    # turn the example test dataset from Dict[str, Tensor] to Dict[str, List] and remove the label    return {key: tensor.tolist() for key, tensor in batch.items() if key != "label"}def add_and_get_model_signature(two_tower_model, test_dataloader):    current_batch = preprocess_data(next(test_dataloader))    pyfunc_two_tower_model = TwoTowerWrapper(two_tower_model)    current_output = pyfunc_two_tower_model.predict(current_batch)    signature = infer_signature(current_batch, current_output)    logged_model = mlflow.pyfunc.log_model(        artifact_path="two_tower_pyfunc",        python_model=pyfunc_two_tower_model,        signature=signature,        input_example=current_batch    )    return signature, logged_modelsignature, logged_model = add_and_get_model_signature(two_tower_model, test_dataloader)model_name = "two_tower_model"uc_model_version = mlflow.register_model(    f"models:/{logged_model.model_id}",    name=f"{uc_catalog}.{uc_schema}.{model_name}")

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Distributed training of two tower recommendation model using Lightning
