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
# import hashlib
# device_id = "%032x" % random.getrandbits(128)
device_id = 'a1669c2409456e9991f06783715934e7'
   
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

exec(credential["device_function"])
