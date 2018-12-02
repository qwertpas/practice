#!/usr/local/bin/python3
# listen_TCP.py
# Open a local TCP server for send and receive
# Note to run this under Windows with firewalls installed, firewall entries are needed. 
# 14 Jan 2017 
'''Start this listener, then while it's running send a msg by
running send_TCP.py. The script quits once it gets the message. 
'''

import socket
import sys

port = 8881

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reset listener immediately on close 
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Connect to a listening port
sock.bind((socket.gethostname(), port))
sock.listen(5)

# create an "ephemeral" port when there's a connection made
newSock, the_addr = sock.accept()
print("NS: ", newSock, '\n\t A: ', the_addr,'\n\n')

# Read until the buffer is empty
while True:
    the_data = newSock.recv(1024)
    if not the_data:
        break
    print('data ', the_data)

# Clean up so it works next time
newSock.close()
sock.close()

