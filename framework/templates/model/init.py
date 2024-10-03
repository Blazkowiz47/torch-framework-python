starting_template: str = """from logging import Logger
from typing import Any, Dict
from torch.nn import Module


def get_model(model: str, config: Dict[str, Any], log: Logger, **kwargs) -> Module:
"""


if_statement: str = """
    if model == "{name}":
        from models.{name} import {classname} 

        return {classname}(config, log, **kwargs)
"""

end_of_if: str = """
    ### Donot remove this line as the build generator uses this as a marker
    ### while adding new model.
    raise NotImplementedError(f"Model: {model} not present")
"""
