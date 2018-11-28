"""
TCP: The Transmission Control Protocol provides a communication service
     between an application program and the Internet Protocol.
Socket: An internal endpoint for sending or receiving data within a node on a computer network.
Assumptions:
* our connection will always succeed
* the server is expecting us to send data first (opposed to servers that send data first and await for responses)
* the server will always send us data back in a timely fashion
"""
import socket

target_host = 'www.google.com'
target_port = 80

# AF_INET indicates standard IPv4 or host name. SOCK_STREAM indicates TCP client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket object
client.connect((target_host, target_port))  # connect the client
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')  # send some data

response = client.recv(4096)  # receive some data (buffer size 4096)
print(response.decode())
