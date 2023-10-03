
"""
Coralogix Python SDK Example
Author: Coralogix Ltd.
Email: support@coralogix.com
"""

import logging

# Set the CORALOGIX_LOG_URL with the proper URL value if it is other than api.coralogix.com.
# from coralogix.constants import Coralogix
# Coralogix.CORALOGIX_LOG_URL = 'https://api.eu2.coralogix.com:443/api/v1/logs'

from coralogix.handlers import CoralogixLogger


PRIVATE_KEY = ""
APP_NAME = "python"
SUB_SYSTEM = "python"

# Get an instance of Python standard logger.
logger = logging.getLogger("Python Logger")
logger.setLevel(logging.DEBUG)

#Check if no handler is already initialized 
if not logger.handlers:        
# Get a new instance of Coralogix logger.
    coralogix_handler = CoralogixLogger(PRIVATE_KEY, APP_NAME, SUB_SYSTEM)
# Add coralogix logger as a handler to the standard Python logger.
    logger.addHandler(coralogix_handler)


# Send message
logger.info("Hello World!")
CoralogixLogger.flush_messages()
