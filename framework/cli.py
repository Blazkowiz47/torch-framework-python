import os
import sys
from typing import Any, List, NoReturn


__all__ = (
    "run",
    "main",
)


def main(args: List[str], **kwargs: Any) -> None:
    return run(*args, **kwargs)


def run(*args: str, **kwargs: Any) -> None:
    print("Running args:", args)
    print(os.curdir)
    return


def entrypoint() -> NoReturn:
    sys.exit(main(sys.argv[1:]))
