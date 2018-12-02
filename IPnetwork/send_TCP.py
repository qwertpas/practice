#!/usr/local/bin/python3
# send_TCP.py
# Send bytes to a local TCP server
# Note to run this under Windows with firewalls installed, firewall entries are needed. 
# 14 Jan 2017 
'''Once listen_TCP.py is started, this will send a message to the listener,
 while it's running. Both scripts quit once the listener gets the message. 
'''
import socket
import sys

port = 8881

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the IP address and port where the server is listening
server_address = ((socket.gethostname(), port))
sock.connect(server_address)
print('connecting to %s port %s\n' % server_address, file=sys.stderr, flush=True)
## send bytes
sock.send(b'HereIam')
sock.close()
