# python-sdk-example

## Install:
```
pip install coralogix-logger
```

## Configuration:

**PRIVATE_KEY** (String): 
> A unique ID that represents your team. The private key can be found > > under DataFlow->Api Keys->Send Your Logs. 

**APLICATION_NAME** (String): 
>The name of your main application. For example, a company named Startup which develops app_1 and app_2 can use “Startup app_1” and “Startup app_2” for this parameter; or if they want to debug their test environment they might insert the “Startup app_1 – Test” or “Startup app_1 – Staging”.

**SUBSYSTEM_NAME** (String): 
>The name of your sub-system. Your application probably has multiple subsystems, e.g. “Backend servers”, “Middleware”, “Frontend servers”, “Database servers” etc. In order to help you examine only the data you need, inserting the subsystem parameter is vital.


## Coralogix Cluster Config:

**CORALOGIX_LOG_URL** (String):
>Is an environment variable that defines to which Coralogix Cluster will the logs be sent to. You can Check your cluster region by looking into you teams URL ending (.com, .us, .in)
```
api.coralogix.us 
api.coralogix.com (default)
api.app.coralogix.in
api.coralogixsg.com

```

Can be added as a Environment Variable or with the following piece of code

```
from coralogix.constants import Coralogix
Coralogix.CORALOGIX_LOG_URL = 'https://api.coralogix.us:443/api/v1/logs'
```

If you need to progamatically force the SDK to send all messages that are in the buffer, flush_messages() can be used.

flush_messages() : Flush all messages in buffer and send them immediately on the current thread
```
CoralogixLogger.flush_messages()
```

For more information please visit https://coralogix.com/integrations/coralogix-python-integration/
