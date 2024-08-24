template: str = """import logging

log: logging.Logger = None


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(
        f"tmp/logs/{name}.log", mode="a", encoding="utf-8"
    )
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    console_handler.setLevel("DEBUG")
    file_handler.setLevel("INFO")

    return logger
"""
