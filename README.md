# Coralogix Python SDK Example Project

## Install:
```bash
pip install coralogix-logger
```

## Configuration:

**PRIVATE_KEY** (String): 
> A unique ID that represents your team. The private key can be found under DataFlow->Api Keys->Send Your Logs. 

**APLICATION_NAME** (String): 
>This is a name tag for the data coming from this application, you can later filter by it on Coralogix.

**SUBSYSTEM_NAME** (String): 
>The name of your sub-system, much like the application name but nested under application name.

**CORALOGIX_LOG_URL** (String):
>Coralogix supports multiple geo regions and depending on where you account is located, 
>This part is required only if you are not in the EU region
>The URL can be provide as an Evironment variable.
```bash
export CORALOGIX_LOG_URL = 'https://<Cluster_api_URL>:443/api/v1/logs'
```
Or from the app itself:
```python
from coralogix.constants import Coralogix
Coralogix.CORALOGIX_LOG_URL = 'https://<Cluster_api_URL>:443/api/v1/logs'
```
The options:
```
api.coralogix.us 
api.coralogix.com (default)
api.app.coralogix.in
api.coralogixsg.com
```

If you need to progamatically force the SDK to send all messages that are in the buffer, it can be done as such.
```python
CoralogixLogger.flush_messages()
```

For more information please visit https://coralogix.com/integrations/coralogix-python-integration/
