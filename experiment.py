import argparse
import os
import contextlib
import numpy as np
import torch
from dataclasses import asdict, dataclass
import yaml
from torch.utils.data import DataLoader
from tqdm import tqdm

# ==========================================
# 1. CONFIGURATION
# ==========================================


@dataclass
class TrainConfig:
    pass


@dataclass
class TestConfig:
    pass


def load_config(config_path: str, config_class):
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)
    return config_class(**data)

# ==========================================
# 2. DATA PREPARATION
# ==========================================


def prepare_train_dataloaders(config: TrainConfig, dataset_path: str):
    pass


def prepare_test_dataloaders(config: TestConfig, dataset_path: str):
    pass

# ==========================================
# 3. CORE EXECUTION LOGIC
# ==========================================


def execute_training(config: TrainConfig, dls: dict, ds_train, ds_val, ckpt_path: str):
    pass


def execute_testing(config: TestConfig, dl_test, ckpt_path: str, predictions_out: str):
    pass


# ==========================================
# ENTRYPOINT
# ==========================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["train", "test"])
    parser.add_argument("--config", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--experiment_name", required=False,
                        default="Default_Experiment")
    parser.add_argument("--ckpt_path", required=False,
                        help="Override model save path", default="models/model.pt")
    parser.add_argument("--predictions_out", required=False,
                        help="Override predictions save path", default="predictions/predictions.npz")
    parser.add_argument("--artifact_id", required=False)

    args = parser.parse_args()

    if args.mode == "train":
        config = load_config(args.config, TrainConfig)
        execute_training(config, dls, ds_train, ds_val, args.ckpt_path)
    elif args.mode == "test":
        config = load_config(args.config, TestConfig)
        execute_testing(config, dl_test, args.ckpt_path, args.predictions_out)
