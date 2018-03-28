#!/usr/bin/env python

import bluetooth

'''nearby_devices = bluetooth.discover_devices(lookup_names=True)'''

services = bluetooth.find_service(address="D0:04:01:87:E2:45")

print ("found services", len(services) )


for service in services:
    print (service["name"])
    if service["name"] == "Headset Gateway":
        headset = service
    elif service["name"] == "Advanced Audio":
        audio = service

print ("end list services ")


socket= bluetooth.BluetoothSocket(bluetooth.L2CAP)

try:
    socket.connect( (audio["host"],audio["port"]) ) 
except bluetooth.btcommon.BluetoothError as e:
    print ("connection failed: ",e)