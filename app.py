import logging
from flask import Flask
app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s", level=logging.INFO)

@app.route("/")
def hello():
    logger.debug("This is a sample log statement")
    logger.info("This is a sample log statement")
    logger.warning("This is a sample log statement")
    logger.error("This is a sample log statement")
    logger.critical("This is a sample log statement")
    return "Welcome to Azure App Service !"
