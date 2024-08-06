template: str = '''import random
import os
from typing import Any, Callable, List, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset


def set_seeds(seed: int = 2024):
    """
    Sets random sets for torch operations.

    Args:
        seed (int, optional): Random seed to set. Defaults to 42.
    """
    # Set the seed for general torch operations
    torch.manual_seed(seed)
    # Set the seed for CUDA torch operations (ones that happen on the GPU)
    torch.cuda.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)


def initialise_dirs():
    """
        Initialises all the required directories.
    """
    os.makedirs("tmp", exists_ok=True)
    os.makedirs("tmp/logs", exists_ok=True)


class DatasetGenerator(Dataset):
    def __init__(self, data: List[Any], transform: Callable) -> None:
        self.data = data
        self.transform = transform

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index) -> Tuple[Any]:
        datapoint = self.data[index]
        return self.transform(datapoint)
'''
