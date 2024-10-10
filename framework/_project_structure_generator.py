import argparse
import os
from typing import List
import shutil

from framework._generate_files import fileGenerator
import framework.templates as tp
import framework.templates.dataset as ds
import framework.templates.model as md
import framework.templates.utils as ut


def generate_dataset_init(datasets: List[str], dataset_dir: str) -> None:
    template: str = ds.starting_template
    for dataset in datasets:
        template += "\n"
        fileArgs = ds.FileArgs(name=dataset, classname=dataset[0].upper() + dataset[1:])
        template += ds.if_statement.format(**fileArgs.__dict__)

    template += "\n"
    template += ds.end_of_if

    fileGenerator("__init__.py", dataset_dir, template)


def generate_model_init(models: List[str], model_dir: str) -> None:
    template: str = md.starting_template
    for model in models:
        template += "\n"
        fileArgs = md.FileArgs(name=model, classname=model[0].upper() + model[1:])
        template += md.if_statement.format(**fileArgs.__dict__)

    template += "\n"
    template += md.end_of_if

    fileGenerator("__init__.py", model_dir, template)


def generate_dataset(dataset: str, dataset_dir: str) -> None:
    template = ds.template
    fileArgs = ds.FileArgs(name=dataset, classname=dataset[0].upper() + dataset[1:])
    fileGenerator(dataset + ".py", dataset_dir, template, fileArgs.__dict__)


def generate_model(model: str, model_dir: str) -> None:
    template = md.template
    fileArgs = md.FileArgs(name=model, classname=model[0].upper() + model[1:])
    fileGenerator(model + ".py", model_dir, template, fileArgs.__dict__)


def generate_utils(util_dir: str) -> None:
    fileGenerator("__init__.py", util_dir, ut.init.template)
    fileGenerator("logger.py", util_dir, ut.logger.template)
    fileGenerator("common_functions.py", util_dir, ut.common_functions.template)


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

    try:
        os.makedirs(root_dir)
        if not os.path.isdir(root_dir):
            raise NotADirectoryError(f"Directory: {root_dir} not found")

        # generate train.py
        fileGenerator("train.py", root_dir, tp.train.template)
        fileGenerator("pyrightconfig.json", root_dir, tp.pyrightconfig.template)

        # generate datasets
        datasets_dir = os.path.join(root_dir, "cdatasets")
        os.makedirs(datasets_dir)
        if not os.path.isdir(datasets_dir):
            raise NotADirectoryError(f"Directory: {datasets_dir} not found")

        if len(datasets) > 0:
            for dataset in datasets:
                generate_dataset(dataset, datasets_dir)
            generate_dataset_init(datasets, datasets_dir)

        # generate models
        models_dir = os.path.join(root_dir, "models")
        os.makedirs(models_dir)
        if not os.path.isdir(models_dir):
            raise NotADirectoryError(f"Directory: {models_dir} not found")
        if len(models) > 0:
            for model in models:
                generate_model(model, models_dir)
            generate_model_init(models, models_dir)

        # generate utils
        utils_dir = os.path.join(root_dir, "utils")
        os.makedirs(utils_dir)
        if not os.path.isdir(utils_dir):
            raise NotADirectoryError(f"Directory: {utils_dir} not found")
        generate_utils(utils_dir)
    except Exception as e:
        shutil.rmtree(root_dir)
        raise e


def add_action(args: argparse.Namespace) -> None:
    datasets = args.dataset
    models = args.model
    root_dir = os.getcwd()
    print("Adding in:", root_dir)

    if datasets:
        # generate datasets
        datasets_dir = os.path.join(root_dir, "cdatasets")
        os.makedirs(datasets_dir, exist_ok=True)
        if not os.path.isdir(datasets_dir):
            raise NotADirectoryError(f"Directory: {datasets_dir} not found")

        if len(datasets) > 0:
            for dataset in datasets:
                generate_dataset(dataset, datasets_dir)
            datasets = [
                dataset[:-3]
                for dataset in os.listdir(datasets_dir)
                if "_" not in dataset and dataset.endswith(".py")
            ]
            generate_dataset_init(datasets, datasets_dir)

    if models:
        # generate models
        models_dir = os.path.join(root_dir, "models")
        os.makedirs(models_dir, exist_ok=True)
        if not os.path.isdir(models_dir):
            raise NotADirectoryError(f"Directory: {models_dir} not found")
        if len(models) > 0:
            for model in models:
                generate_model(model, models_dir)
            models = [
                model[:-3]
                for model in os.listdir(models_dir)
                if "_" not in model and model.endswith(".py")
            ]
            generate_model_init(models, models_dir)
