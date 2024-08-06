template: str = """import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=f"tmp/logs/{__name__}.log", encoding="utf-8", level=logging.DEBUG
)
"""
