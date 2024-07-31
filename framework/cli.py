import os
import sys
from typing import List, NoReturn

from framework._project_structure_generator import create_project


__all__ = ("main",)


def main(args: List[str]) -> None:
    print("Running args:", args)
    print(os.curdir, os.getcwd())
    if args[0] == "create":
        create_project(args[1:])
    elif args[0] == "add-dataset":
        raise NotImplementedError("Not implemented add-dataset yet.")
    else:
        raise ValueError("Invalid Arguements.")


def entrypoint() -> NoReturn:
    sys.exit(main(sys.argv[1:]))
