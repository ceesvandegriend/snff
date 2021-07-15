import logging

import snff.tasks

def execute() -> bool:
    logger = logging.getLogger(__name__)

    try:
        snff.tasks.execute()
        error = False
    except Exception as err:
        logger.error(err, exc_info=True)
        error = True

    return error
