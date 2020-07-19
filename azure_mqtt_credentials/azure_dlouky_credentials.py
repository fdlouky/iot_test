# =============================================================================
# Connection to my Azure
# =============================================================================

"""
#------------------------PUBLISHER------------------------------------------------------------
# If you have access to the Event Hub-compatible connection string from the Azure portal, then
# you can skip the Azure CLI commands above, and assign the connection string directly here.
CONNECTION_STR_PUB = "HostName=dlouky-hub.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=iCDgrPx8cStBiMofiT/ShyITMXeFu8xqk32eIt4LE5A="

#------------------------SUSCRIBER------------------------------------------------------------
# Event Hub-compatible endpoint
# az iot hub show --query properties.eventHubEndpoints.events.endpoint --name dlouky-hub
EVENTHUB_COMPATIBLE_ENDPOINT = "sb://iothub-ns-dlouky-hub-3859124-23d06ab863.servicebus.windows.net/"

# Event Hub-compatible name
# az iot hub show --query properties.eventHubEndpoints.events.path --name dlouky-hub
EVENTHUB_COMPATIBLE_PATH = "dlouky-hub"

# Primary key for the "service" policy to read messages
# az iot hub policy show --name service --query primaryKey --hub-name dlouky-hub
IOTHUB_SAS_KEY = "xKoQ30wdDedqcS3l8owZVs+8bZkF+EZ+/mRrtr+6BKI="

#CONNECTION_STR_SUB = f'Endpoint={EVENTHUB_COMPATIBLE_ENDPOINT}/;SharedAccessKeyName=service;SharedAccessKey={IOTHUB_SAS_KEY};EntityPath={EVENTHUB_COMPATIBLE_PATH}'
CONNECTION_STR_SUB = "Endpoint=sb://iothub-ns-dlouky-hub-3859124-23d06ab863.servicebus.windows.net//;SharedAccessKeyName=service;SharedAccessKey=xKoQ30wdDedqcS3l8owZVs+8bZkF+EZ+/mRrtr+6BKI=;EntityPath=dlouky-hub"
"""


# =============================================================================
# Connection to Supplied IoT HUB
# =============================================================================

#------------------------PUBLISHER------------------------------------------------------------
CONNECTION_STR_PUB = "HostName=ioteStage2Hub.azure-devices.net;DeviceId=ioteStage2Device;SharedAccessKey=Dj26/8uTaukyrSqLvndzKJK8spfYK72wYS8g9t+BUdU="

#------------------------SUSCRIBER------------------------------------------------------------
CONNECTION_STR_SUB = "Endpoint=sb://iothub-ns-iotestage2-3732702-1e3b4c5763.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=l5lK9dLcA7Z9dC9v9JgYjPKj4vTBvkk9y1KayhMwFFg=;EntityPath=iotestage2hub"