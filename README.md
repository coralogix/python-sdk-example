# python-sdk-example
Install:

pip install coralogix-logger

Configuration:

private_key (String): A unique ID that represents your company. The private key can be found under ‘settings’->’ send your logs’. It is located in the upper left corner.

application Name(String): The name of your main application. For example, a company named Startup which develops app_1 and app_2 can use “Startup app_1” and “Startup app_2” for this parameter; or if they want to debug their test environment they might insert the “Startup app_1 – Test” or “Startup app_1 – Staging”.

subsystem Name(String): The name of your sub-system. Your application probably has multiple subsystems, e.g. “Backend servers”, “Middleware”, “Frontend servers”, “Database servers” etc. In order to help you examine only the data you need, inserting the subsystem parameter is vital.


Coralogix Cluster Config:

CORALOGIX_LOG_URL Defines to which Coralogix Cluster will be sent the logs to:
api.coralogix.us 
api.coralogix.com (default)
api.app.coralogix.in

Can be added as a Environment Variable or with the following piece of code


from coralogix.constants import Coralogix
Coralogix.CORALOGIX_LOG_URL = 'https://api.coralogix.us:443/api/v1/logs'

