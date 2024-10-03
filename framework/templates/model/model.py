from dataclasses import dataclass

template: str = """from logging import Logger
from typing import Any, Dict 
from torch.nn import Conv2d, Module, Sequential


class {classname}(Module):

    def __init__(self, config: Dict[str, Any], log: Logger, **kwargs):
        super({classname}, self).__init__()
        self.name = "{name}"
        self.config = config
        self.log = log
        self.kwargs = kwargs
        self.log.debug(f"Initialised {self.name} model.")

    def forward(self, x):
        raise NotImplementedError()
"""


@dataclass
class FileArgs(dict):
    """
    Defines the dictionary for named format arguements.
    """

    classname: str
    name: str
