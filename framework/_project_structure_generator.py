import os
from typing import Any, Dict
import argparse

from framework.__generate_files import fileGenerator
from framework.constants.templates import *


def create_project(args: argparse.Namespace) -> None:
    """
    Creates a directory with given project name.
    Generates a deep-learning framework in it.
    """
    project = args.name
    datasets = args.dataset
    models = args.model

    root_dir = os.path.join(os.getcwd(), project)
    print("Generating Project:", project)
    print(root_dir)

    os.makedirs(root_dir)
    if not os.path.isdir(root_dir):
        raise NotADirectoryError(f"Directory: {root_dir} not found")

    datasets_dir = os.path.join(root_dir, "datasets")
    os.makedirs(datasets_dir)
    if not os.path.isdir(datasets_dir):
        raise NotADirectoryError(f"Directory: {datasets_dir} not found")

    models_dir = os.path.join(root_dir, "models")
    os.makedirs(models_dir)
    if not os.path.isdir(models_dir):
        raise NotADirectoryError(f"Directory: {models_dir} not found")
    
    #generate train.py
    fileGenerator("train.py", root_dir, TRAIN_TEMPLATE)

    #generate sample dataset file
    if len(datasets)>0:
        for dataset in datasets:
            fileGenerator(dataset, datasets_dir, DATASET_TEMPLATE)
    
    #generate sample model file
    if len(models)>0:
        for model in models:
            fileGenerator(model, models_dir, MODEL_TEMPLATE)
