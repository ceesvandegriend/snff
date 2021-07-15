import logging
from urllib import request
import json

def execute() -> None:
    logger = logging.getLogger(__name__)
    URL = "https://www.ifconfig.io/all.json"

    response = request.urlopen(URL)
    data = json.loads(response.read())
    logger.info(data)