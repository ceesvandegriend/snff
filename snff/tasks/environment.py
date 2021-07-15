import logging
import os

def execute() -> None:
    logger = logging.getLogger(__name__)

    for var in os.environ:
        logger.info(f"{var}: {os.environ[var]}")
