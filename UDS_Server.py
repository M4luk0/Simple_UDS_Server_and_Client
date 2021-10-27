#!/usr/bin/python3
"""
Simple UDS Server
Copyright: Juan Antonio Gil Chamorro (M4luk0)
"""

# Libraries
import socket
import os

# Checks if the socket exists and deletes it
if os.path.exists("/tmp/socket"):
    os.remove("/tmp/socket")

# Creates the socket and binds it to a file
print("Opening socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind("/tmp/socket")

# We put the socket on standby
print("Listening...")
server.listen()
connection, address = server.accept()
data = connection.recv(4096)

# Wait to receive "hola", send "adios" and close the connection.
if data == b'hola':
    connection.send(b'adios')
    print(data)
    os.remove("/tmp/socket")
    server.close()
