import os
from typing import Dict, Optional


def fileGenerator(
    fileName: str, directory: str, template: str, fileArgs: Optional[Dict] = None
):
    with open(os.path.join(directory, fileName), "w+") as fp:
        if fileArgs:
            fp.writelines(template.format(**fileArgs))
        else:
            fp.writelines(template)
