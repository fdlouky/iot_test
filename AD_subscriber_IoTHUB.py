# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:41:23 2020

@author: Dlouky Federico Manuel

This script suscribe to dlouky-hun and read the payload generate by the device 
"AB_device_simulator.py" .

"""

from azure.eventhub import EventHubConsumerClient
from azure_mqtt_credentials.azure_dlouky_credentials import CONNECTION_STR_SUB
from pymongo import MongoClient 
import json

# Connect to MongoDB database
client = MongoClient('localhost', port=27017)
# Use or create a MongoDB database
db = client['db_elastacloud']
# Create a new MongoDB collection
col = db['collection_elastacloud']
# List MongoDB databases
# print(client.list_database_names())

# Define callbacks to process events
def on_event_batch(partition_context, events):
    for event in events:
        # print("Received event from partition: {}.".format(partition_context.partition_id))
        message = event.body_as_str()
        print("Telemetry received: ", message)
        # Insert the message as a document to the MongoDB collection
        col.insert_one(json.loads(message))
        # print("Properties (set by device): ", event.properties)
        # print("System properties (set by IoT Hub): ", event.system_properties)
        print()
    partition_context.update_checkpoint()

def on_error(partition_context, error):
    # Put your code here. partition_context can be None in the on_error callback.
    if partition_context:
        print("An exception: {} occurred during receiving from Partition: {}.".format(
            partition_context.partition_id,
            error
        ))
    else:
        print("An exception: {} occurred during the load balance process.".format(error))


def main():
    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR_SUB,
        consumer_group="$default",
    )
    try:
        with client:
            client.receive_batch(
                on_event_batch=on_event_batch,
                on_error=on_error
            )
    except KeyboardInterrupt:
        print("Receiving has stopped.")

if __name__ == '__main__':
    main()
