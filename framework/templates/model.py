template: str = """from typing import Any, Dict 
from torch.nn import Conv2d, Module, Sequential

class {classname}(Module):

    def __init__(self, config: Dict[str, Any]):
        super({classname}, self).__init__()
        self.name = "{name}"
        self.config = config

    def forward(self, x):
        raise NotImplementedError()
"""

