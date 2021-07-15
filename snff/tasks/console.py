import logging


def execute() -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    format = logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(format)

    logger.addHandler(console)
