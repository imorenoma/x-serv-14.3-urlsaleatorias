#!/usr/bin/python3

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostbyname('localhost'), 1234))

# Queue a maximum of 20 TCP connection requests
mySocket.listen(20)

try:
    while True:
        print("Waiting for connections")
        (recvSocket, address) = mySocket.accept()

        print('Request received:')
        print(recvSocket.recv(2048))  # Buffer size
        print('Answering back...')

        randomnum = random.randrange(1, 10000000000)

        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        '<html><h1>Random numbers server</h1>' +
                              '</body>Hola. ' +
                              '<a href= "http://localhost:1234/' +
                              str(randomnum) +
                              '">Dame otra</a>' +
                              "</body></html>" +
                              '\r\n', 'utf-8'))

        recvSocket.close()

except KeyboardInterrupt:
    print("Closing socket")
    mySocket.close()
