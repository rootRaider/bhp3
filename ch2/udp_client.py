"""
UDP: User Datagram Protocol is a core member of the Internet protocol suite
     and uses a connectionless communication model with a minimum of protocol mechanism.
"""
import socket

target_host = '127.0.0.1'
target_port = 80

# SOCK_DGRAM indicates UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket object

# NOTE: book does not do this but otherwise request hangs
client.bind((target_host, target_port))

# Since UDP is connectionless protocol there is no call to connect
client.sendto(b'AAABBBCCC', (target_host, target_port))  # send some data

data, address = client.recvfrom(4096)  # receive some data (buffer size 4096)
print(data.decode())
print(address)
