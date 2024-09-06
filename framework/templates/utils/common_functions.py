template: str = '''import os
import random
from abc import abstractmethod
from typing import Any, Callable, List, Optional, Tuple

import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset

from utils.logger import log


def set_seeds(seed: int = 2024):
    """
    Sets random sets for torch operations.

    Args:
        seed (int, optional): Random seed to set. Defaults to 42.
    """
    log.debug(f"Setting seed to: {seed}")
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
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("tmp/logs", exist_ok=True)


class DatasetGenerator(Dataset):
    def __init__(self, data: List[Any], transform: Callable) -> None:
        self.data = data
        self.transform = transform

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index) -> Tuple[Any]:
        datapoint = self.data[index]
        return self.transform(datapoint)


class Wrapper:
    def __init__(
        self, rdir: str = "", batch_size: int = 1, num_workers: int = 1
    ) -> None:
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.rdir = rdir
        self.name = ""

    @abstractmethod
    def loop_splitset(self, ssplit: str) -> List[Any]:
        """
        Loops through the given directory.
        Practically, one should only change this function and get various splits.
        Returns: List of files to load along with its class label.
        """
        raise NotImplementedError("")

    def get_split(
        self,
        split: str,
        batch_size: Optional[int] = None,
        num_workers: Optional[int] = None,
    ) -> DataLoader:
        """
        Generates the given split.
        """
        log.debug(f"Generating {split} split for {self.name} dataset.")
        batch_size = batch_size or self.batch_size
        data = self.loop_splitset(split)
        log.debug(f"Total files: {len(data)}")
        return DataLoader(
            DatasetGenerator(data, self.transform),
            num_workers=num_workers or self.num_workers,
            batch_size=batch_size or self.batch_size,
        )

    @abstractmethod
    def augment(self, image):
        """
        Augments the given image.
        """
        raise NotImplementedError()

    @abstractmethod
    def transform(self, datapoint: Tuple[str, int]) -> Tuple:
        """
        Transforms the given datapoint.
        """
        raise NotImplementedError()
'''
