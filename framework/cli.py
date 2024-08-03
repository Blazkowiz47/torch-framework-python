import os
import sys
from typing import Dict, List, NoReturn, Any

from framework._project_structure_generator import create_project
from framework.argument_parser import parse_args


__all__ = ("main",)
                

def main(args: List[str]) -> None:
    print("Running args:", args)
    print(os.curdir, os.getcwd())

    #parse arguments to get dictionary
    parsedArgs = parse_args(args)

    if args[0] == "create":
        create_project(parsedArgs)
    elif args[0] == "add-dataset":
        raise NotImplementedError("Not implemented add-dataset yet.")
    else:
        raise ValueError("Invalid Arguements.")

def entrypoint() -> NoReturn:
    sys.exit(main(sys.argv[1:]))
