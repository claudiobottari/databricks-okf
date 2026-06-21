---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 227c18f17a7b8aae527719c8b64c0c888b4ad1bb7af2f1d78fb069496deab081
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-pyfunc-wrapping-for-model-serving
    - MPWFMS
  citations:
    - file: filename.md
    - file: source-a.md
    - file: source-b.md
    - file: filename.md:START-END
    - file: filename.md#LSTART-LEND
title: MLflow PyFunc Wrapping for Model Serving
description: Wrapping a PyTorch recommendation model in an MLflow PythonModel to simplify the inference interface from tensor-based batches to dictionary-based list inputs for serving.
tags:
  - mlflow
  - model-serving
  - mlops
timestamp: "2026-06-19T18:34:52.898Z"
---

You are a wiki author. Write a clear, well-structured markdown page about “MLflow PyFunc Wrapping for Model Serving”.
Draw facts only from the provided source material.
Include a ## Sources section at the end listing the source document.
Suggest wikilinks to related concepts where appropriate.
Write in a neutral, informative tone. Be concise but thorough.

Source attribution: at the end of each prose paragraph, append a citation
marker showing which source file(s) the paragraph drew from.
^[filename.md] for single-source, ^[source-a.md, source-b.md] for multi-source.
When a single sentence makes a specific factual claim and you can identify the
exact line range it came from, you may use the claim-level form
^[filename.md:START-END] (or ^[filename.md#LSTART-LEND]) at the end of that
sentence — START and END are 1-indexed line numbers in the source file.
Paragraph-level citations remain the default; only switch to claim-level form
when it materially improves verifiability and the line range is unambiguous.
Place citations only at the end of prose paragraphs or sentences — not on
headings, list items, or code blocks.
Source filenames are visible as `--- SOURCE: filename.md ---` headers in the content below.

If a paragraph is your inference rather than a direct extraction, leave it
uncited — downstream lint rules will count uncited paragraphs as 'inferred'
to compute the page's provenance metadata.

--- SOURCE MATERIAL ---


--- SOURCE: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md ---

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

    DATASET_URL = "https://files.grouplens.org/datasets/learning-from-sets-2019/learning-from-sets-2019.zip"DATASET_PATH = f"/Volumes/{uc_catalog}/{uc_schema}/{uc_volume}/dataset"ZIP_PATH = f"{DATASET_PATH}/learning-from-sets-2019.zip"CSV_PATH = f"{DATASET_PATH}/learning-from-sets-2019/item_ratings.csv"# Download and extractif not os.path.exists(CSV_PATH):    os.makedirs(DATASET_PATH, exist_ok=True)    print("Downloading dataset...")    urllib.request.urlretrieve(DATASET_URL, ZIP_PATH)    with zipfile.ZipFile(ZIP_PATH, "r") as zf:        zf.extractall(DATASET_PATH)    print("Download complete.")# Load and preprocessdf = pd.read_csv(CSV_PATH)df = df.sort_values(["userId", "movieId"]).head(100_000)# Encode userId to contiguous integersuser_encoder = LabelEncoder()df["userId"] = user_encoder.fit_transform(df["userId"])# Binarize ratings: 1 if >= mean, else 0mean_rating = df["rating"].mean()df["label"] = (df["rating"] >= mean_rating).astype(np.int64)df = df"userId", "movieId", "label"# Compute embedding table sizes from datanum_users = int(df["userId"].nunique())num_movies = int(df["movieId"].nunique())print(f"Dataset: {len(df)} rows, {num_users} users, {num_movies} movies")# Split: 70% train, 21% validation, 9% testtrain_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)val_df, test_df = train_test_split(temp_df, test_size=0.33, random_state=42)print(f"Train: {len(train_df)}, Validation: {len(val_df)}, Test: {len(test_df)}")

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

    class TwoTowerModel(nn.Module):    def __init__(        self,        embedding_bag_collection: EmbeddingBagCollection,        layer_sizes: List[int],        device: Optional[torch.device] = None    ) -> None:        super().__init__()        assert len(embedding_bag_collection.embedding_bag_configs()) == 2, "Expected two EmbeddingBags in the two tower model"        assert embedding_bag_collection.embedding_bag_configs()[0].embedding_dim == embedding_bag_collection.embedding_bag_configs()[1].embedding_dim, "Both EmbeddingBagConfigs must have the same dimension"        embedding_dim = embedding_bag_collection.embedding_bag_configs()[0].embedding_dim        self._feature_names_query: List[str] = embedding_bag_collection.embedding_bag_configs()[0].feature_names        self._candidate_feature_names: List[str] = embedding_bag_collection.embedding_bag_configs()[1].feature_names        self.ebc = embedding_bag_collection        self.query_proj = MLP(in_size=embedding_dim, layer_sizes=layer_sizes, device=device)        self.candidate_proj = MLP(in_size=embedding_dim, layer_sizes=layer_sizes, device=device)    def forward(self, kjt: KeyedJaggedTensor) -> Tuple[torch.Tensor, torch.Tensor]:        pooled_embeddings = self.ebc(kjt)        query_embedding: torch.Tensor = self.query_proj(            torch.cat(                [pooled_embeddings[feature] for feature in self._feature_names_query],                dim=1,            )        )        candidate_embedding: torch.Tensor = self.candidate_proj(            torch.cat(                [pooled_embeddings[feature] for feature in self._candidate_feature_names],                dim=1,            )        )        return query_embedding, candidate_embeddingclass LitTwoTower(pl.LightningModule):    """    PyTorch Lightning module wrapping a TwoTowerModel.    Uses torchmetrics AUROC for train/val metrics.    """    def __init__(        self,        two_tower: nn.Module,        device: torch.device,        emb_counts: Optional[List[int]],        cat_cols: List[str],        lr: float = 1e-3,    ) -> None:        super().__init__()        self.two_tower = two_tower        self.loss_fn = nn.BCEWithLogitsLoss()        self.train_auroc = AUROC(task="binary")        self.val_auroc = AUROC(task="binary")        self.lr = lr        # Store metadata used in batch transform        self.emb_counts = emb_counts        self.cat_cols = cat_cols        self.save_hyperparameters(ignore=["two_tower", "device"])    def forward(self, batch: Dict[str, Any]) -> torch.Tensor:        kjt_batch = self._transform_to_torchrec_batch(batch, self.emb_counts)        query_embedding, candidate_embedding = self.two_tower(kjt_batch.sparse_features)        logits = (query_embedding * candidate_embedding).sum(dim=1).squeeze()        return logits    def _loss(self, outputs: torch.Tensor, batch: Dict[str, Any]) -> torch.Tensor:        labels = self._get_batch_labels(batch)        return self.loss_fn(outputs, labels)    def _update_metric(self, batch: Dict[str, Any], outputs: Optional[torch.Tensor], metric: AUROC) -> None:        if outputs is None:            outputs = self.forward(batch)        preds = torch.sigmoid(outputs)        labels = self._get_batch_labels(batch)        metric.update(preds, labels)    def training_step(self, batch: Dict[str, Any], batch_idx: int):        logits = self.forward(batch)        loss = self._loss(logits, batch)        # Metric update        self._update_metric(batch, logits, self.train_auroc)        # Log both step and epoch loss series; enable sync_dist for multi-GPU/DDP        self.log("train_loss", loss, on_step=True, on_epoch=True, prog_bar=True, logger=True, sync_dist=True)        self.log("train_auroc", self.train_auroc, on_step=False, on_epoch=True, prog_bar=True,             logger=True, sync_dist=True)        return loss    def validation_step(self, batch: Dict[str, Any], batch_idx: int):        logits = self.forward(batch)        loss = self._loss(logits, batch)        self._update_metric(batch, logits, self.val_auroc)        # Typically only epoch-level val metrics are needed for monitoring        self.log("val_loss", loss, on_step=False, on_epoch=True, prog_bar=True, logger=True, sync_dist=True)        self.log("val_auroc", self.val_auroc, on_step=False, on_epoch=True, prog_bar=True,             logger=True, sync_dist=True)    def configure_optimizers(self):        optimizer = KeyedOptimizerWrapper(            dict(self.two_tower.named_parameters()),            lambda params: torch.optim.Adam(params, lr=self.lr),        )        return optimizer    def _get_batch_labels(self, batch: Dict[str, Any]) -> torch.Tensor:        return batch["label"].to(dtype=torch.float32, device=self.device)    def _transform_to_torchrec_batch(        self,        batch: Dict[str, Any],        num_embeddings_per_feature: Optional[List[int]],    ) -> Batch:        kjt_values_list = []        kjt_lengths_list = []        for col_idx, col_name in enumerate(self.cat_cols):            values = batch[col_name]            num_emb = num_embeddings_per_feature[col_idx]            kjt_values_list.append(values % num_emb)            kjt_lengths_list.append(torch.ones(len(values), dtype=torch.int64))        values_t = torch.cat(kjt_values_list).to(dtype=torch.int64, device=self.device)        lengths_t = torch.cat(kjt_lengths_list).to(device=self.device)        sparse_features = KeyedJaggedTensor.from_lengths_sync(            self.cat_cols,            values_t,            lengths_t,        )        labels = batch["label"].to(dtype=torch.int64, device=self.device)        return Batch(            dense_features=torch.zeros(1, device=self.device),            sparse_features=sparse_features,            labels=labels,        )def create_two_tower_model(args, device, cat_cols, emb_counts) -> LitTwoTower:    eb_configs = [        EmbeddingBagConfig(            name=f"t_{feature_name}",            embedding_dim=args.embedding_dim,            num_embeddings=emb_counts[feature_idx],            feature_names

# Citations

1. filename.md
2. source-a.md
3. source-b.md
4. filename.md:START-END
5. filename.md#LSTART-LEND
