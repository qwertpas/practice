import socket
import sys

port = 8081

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", port))
print("socket: ", sock)

running = True
while running:
    the_data, the_addr = sock.recvfrom(1024)
    print("R: ", the_data, '\t\t A: ', the_addr)

