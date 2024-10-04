import argparse
import os
import sys
from typing import NoReturn

from ._project_structure_generator import create_project, add_action

__all__ = ("main",)


parser = argparse.ArgumentParser()
parser.add_argument("action", type=str)
parser.add_argument(
    "-p",
    "--name",
    type=str,
    default="",
    help="When creating a project, add the project name here.",
    required=False,
)
parser.add_argument("-d", "--dataset", nargs="+", default=[], required=False)
parser.add_argument("-m", "--model", nargs="+", default=[], required=False)


def main(args: argparse.Namespace) -> None:
    print("Running args:", args)
    print(os.curdir, os.getcwd())

    # parse arguments to get dictionary
    if args.action == "create":
        create_project(args)
    elif args.action == "add":
        add_action(args)
    else:
        raise ValueError("Invalid Arguements.")


def entrypoint() -> NoReturn:
    # parse arguments
    args = parser.parse_args()
    # print(args)
    sys.exit(main(args))
