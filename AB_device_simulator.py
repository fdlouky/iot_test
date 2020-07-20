# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:41:23 2020

@author: Dlouky Federico Manuel

This script simulates a device that generates signals in a
json format with the following fields according to the device_function
configured by AA_device_credentials_generator.py:
    •	device_id
    •	device_name
    •	device_latitude
    •	device_longitude
    •	device_battery_level
    •	signal_date: Timestamp (when the signal was emmited)
"""
import sys
import json

# Suppose the device_id comes from the factory.
# For this exercise it was generated as a random SHA1 hash with the next 2 lines.
# import hashlib, random
# device_id = "%032x" % random.getrandbits(128)
device_id = 'd8e3499d40ae09abcbdafdcc9e8e3723'
   
# Ask for a new credential to AA_device_credentials_generator
# from AA_device_credentials_generator import create_credential
# credential_path = create_credential(device_id)
path = ".\device_credentials"
credential_path = path+"\device_"+device_id+".json"

# Read the generated credential 
try:
    with open(credential_path, "r") as f:
        credential = json.loads(f.read())
except:
    print("ERROR getting credential")
    sys.exit("Fatal error. Credential does not exists!")

# Run the tasks reported in the credential
exec(credential["device_function"])

# Read the credential to publish on IoT HUB
CONNECTION_STR_PUB = credential["CONNECTION_STR_PUB"]
