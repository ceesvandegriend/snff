import logging
import urllib
import json

def execute() -> None:
    logger = logging.getLogger(__name__)
    URL = "https://www.ifconfig.io/all.json"

    response = urllib.urlopen(URL)
    data = json.loads(response.read())
    logger.info(data)