import logging 
from decouple import config

DEBUG = config('DEBUG')

# main logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
if DEBUG == "true":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
logger.info("Logger initilized with level %s", logging.getLevelName(logger.level))
