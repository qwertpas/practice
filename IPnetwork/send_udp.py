import socket
import sys

port = 8081

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.sendto(b"UDP contents", ("localhost", port))

