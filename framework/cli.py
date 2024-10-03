import os
import sys
import argparse
from typing import Dict, List, NoReturn, Any, Union

from ._project_structure_generator import create_project

__all__ = ("main",)


parser = argparse.ArgumentParser()
parser.add_argument("action", type=str)
parser.add_argument("name", type=str, default="")
parser.add_argument("-d", "--dataset", nargs="+", default=["sample"])
parser.add_argument("-m", "--model", nargs="+", default=["sample"])


def main(args: List[str]) -> None:
    print("Running args:", args)
    print(os.curdir, os.getcwd())

    # parse arguments to get dictionary
    if args.action == "create":
        create_project(args)
    elif args.action == "add-datset":
        raise NotImplementedError("Not implemented add-dataset yet.")
    else:
        raise ValueError("Invalid Arguements.")


def entrypoint() -> NoReturn:
    # parse arguments
    args = parser.parse_args()

    # print(args)

    sys.exit(main(args))
