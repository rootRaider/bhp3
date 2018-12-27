"""
TCP: The Transmission Control Protocol provides a communication service
     between an application program and the Internet Protocol.
Socket: An internal endpoint for sending or receiving data within a node on a computer network.
"""
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999
max_connections = 5

# AF_INET indicates standard IPv4 or host name. SOCK_STREAM indicates TCP.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket object
server.bind((bind_ip, bind_port))  # pass in IP and PORT we want server to listen on
server.listen(max_connections)  # tell server to start listening with a max backlog of connections
print('[*] Listening on %s:%d' % (bind_ip, bind_port))  # print server success on startup


def handle_client(client_socket):
    """
    this is our client handling thread
    void method that sends a packet back to client socket
    :param client_socket: socket.socket
    :return: None
    """
    request = client_socket.recv(1024)  # buffer size 1024
    print('[*] Received: %s' % request)  # print out what client sends

    client_socket.send(b'ACK!')  # send back a packet
    client_socket.close()  # close connection


# put server in main loop awaiting connections
while True:
    client, address = server.accept()  # client socket, remote connection details
    print('[*] Accepted connection from: %s:%d' % (address[0], address[1]))

    # spin up our client thread to handle incoming data
    # create a thread object pointing to our handle and passing in the client socket object
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()  # start thread
