# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:41:23 2020

@author: Dlouky Federico Manuel

This script publishes the payload generate by the device 
"AB_device_simulator.py" in IoT Hub.

"""

from AB_device_simulator import device
import json
from azure_mqtt_credentials.azure_dlouky_credentials import CONNECTION_STR_PUB
from azure.iot.device import IoTHubDeviceClient, Message
import time

def iothub_client_telemetry_sample_run():
    try:
        # Create an IoT Hub client
        client = IoTHubDeviceClient.\
            create_from_connection_string(CONNECTION_STR_PUB)
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        
        payload = device()
        while json.loads(payload)["device_battery_level"]>0:
            # Build the message with simulated telemetry values.
            message = Message(payload)
            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent\n" )
            # Reading next payload
            payload = device()
            # Send the message every 1 second.
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )


if __name__ == '__main__':   
    print ( "IoT Hub Stage 2 Dlouky - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()