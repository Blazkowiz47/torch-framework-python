import argparse
import os
from typing import List
import shutil

from ._generate_files import fileGenerator
from .constants import templates as tp


def generate_dataset_init(datasets: List[str], dataset_dir: str) -> None:
    template: str = tp.dataset.starting_template
    for dataset in datasets:
        template += "\n"
        fileArgs = tp.dataset.FileArgs(
            name=dataset, classname=dataset[0].upper() + dataset[1:]
        )
        template += tp.dataset.if_statement.format(**fileArgs.__dict__)

    template += "\n"
    template += tp.dataset.end_of_if

    fileGenerator("__init__.py", dataset_dir, template)


def generate_model_init(models: List[str], model_dir: str) -> None:
    template: str = tp.model.starting_template
    for model in models:
        template += "\n"
        fileArgs = tp.model.FileArgs(name=model, classname=model[0].upper() + model[1:])
        template += tp.model.if_statement.format(**fileArgs.__dict__)

    template += "\n"
    template += tp.model.end_of_if

    fileGenerator("__init__.py", model_dir, template)


def generate_dataset(dataset: str, dataset_dir: str) -> None:
    template = tp.dataset.template
    fileArgs = tp.dataset.FileArgs(
        name=dataset, classname=dataset[0].upper() + dataset[1:]
    )
    fileGenerator(dataset + ".py", dataset_dir, template, fileArgs.__dict__)


def generate_model(model: str, model_dir: str) -> None:
    template = tp.model.template
    fileArgs = tp.model.FileArgs(name=model, classname=model[0].upper() + model[1:])
    fileGenerator(model + ".py", model_dir, template, fileArgs.__dict__)


def generate_utils(util_dir: str) -> None:
    fileGenerator("__init__.py", util_dir, tp.utils.init.template)
    fileGenerator("logger.py", util_dir, tp.utils.logger.template)
    fileGenerator("common_functions.py", util_dir, tp.utils.common_functions.template)


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
