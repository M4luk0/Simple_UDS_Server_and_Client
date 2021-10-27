#!/usr/bin/python3
"""
Simple UDS Client
Copyright: Juan Antonio Gil Chamorro (M4luk0)
"""

# Libraries
import socket
import os

# We connect to the socket created in /tmp and send "hola"
print("Connecting...")
if os.path.exists("/tmp/socket"):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect("/tmp/socket")
    print("Connected")
    client.send(b'hola')
    data = client.recv(4096)
    # if you receive "adios" close connection
    if data == b'adios':
        print(data)
        client.close()
else:
    print("Can't connect, open the server!")
