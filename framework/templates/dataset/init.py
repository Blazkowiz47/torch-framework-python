starting_template: str = """
from typing import Any, Dict
from utils import Wrapper


def get_dataset(dataset: str, config: Dict[str, Any]) -> Wrapper:
"""


if_statement: str = """
    if dataset == "{name}":
        from cdatasets.{name} import {classname}Wrapper

        return {classname}Wrapper(config)
"""

end_of_if: str = """
    ### Donot remove this line as the build generator uses this as a marker
    ### while adding new dataset.
    raise NotImplementedError(f"Dataset: {dataset} not present")
"""
