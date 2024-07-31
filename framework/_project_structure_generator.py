import os


def create_project(args) -> None:
    """
    Creates a directory with given project name.
    Generates a deep-learning framework in it.
    """
    name, *_ = args
    root_dir = os.path.join(os.getcwd(), name)
    print("Generating Project:", name)
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

    with open(os.path.join(root_dir, "train.py"), "w+") as fp:
        fp.writelines(
            [
                "import torch\n\n\n\n",
                "def train() -> None:\n",
                "\traise NotImplementedError()",
            ]
        )
