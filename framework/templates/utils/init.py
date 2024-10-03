template: str = """from utils.logger import get_logger, log
from utils.common_functions import (
    set_seeds,
    initialise_dirs,
    DatasetGenerator,
    Wrapper,
    get_run_name,
    image_extensions,
    video_extensions,
)

__all__ = [
    "get_logger",
    "log",
    "set_seeds",
    "initialise_dirs",
    "get_run_name",
    "DatasetGenerator",
    "Wrapper",
    "image_extensions",
    "video_extensions"
]
"""
