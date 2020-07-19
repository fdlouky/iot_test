# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:41:23 2020

@author: Dlouky Federico Manuel

This script publish the payload generate by the device 
"AB_device_simulator.py" in a MQTT broker.

"""

from AB_device_simulator import device
import paho.mqtt.client as mqtt
import time
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client_, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_publish(client, userdata, mid):
    print("Published: " + str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.will_set("stage2/disconnections", "dead battery!")  
client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
client.loop_start()

payload = device()
while json.loads(payload)["device_battery_level"]>0:
    client.publish("stage2/payloads", payload, qos=2, retain=False)
    # Reading next payload
    payload = device()
    # Send the message every 1 seconds
    time.sleep(1)

client.disconnect()