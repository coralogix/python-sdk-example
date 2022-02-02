
"""
Coralogix Python SDK Example
Author: Coralogix Ltd.
Email: juan@coralogix.com
"""
from coralogix.constants import Coralogix
Coralogix.CORALOGIX_LOG_URL = 'https://api.coralogix.us:443/api/v1/logs'

""" 

CORALOGIX_LOG_URL Defines to which Coralogix Cluster will be sent the logs to:
api.coralogix.us 
api.coralogix.com (default)
api.app.coralogix.in

"""

import logging
from coralogix.handlers import CoralogixLogger


PRIVATE_KEY = "03f2f7a3-0e6a-77e9-9072-XXXXXXXXXXXXX"
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