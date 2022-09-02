import socket

host = 'localhost'
port = 5052

clientSocket = socket.socket()
clientSocket.connect((host, port))

number = input("Numero: ")
clientSocket.send(number.encode())

while clientSocket.recv(1024).decode() == "None":
    number = input("Numero de novo: ")
    clientSocket.send(number.encode())

option = input("CHOSE: ")

while option != '3':
    clientSocket.send(option.encode())

    option = input(clientSocket.recv(1024).decode())

clientSocket.close()