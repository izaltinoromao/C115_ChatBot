import socket

host = 'localhost'
port = 5052

clientSocket = socket.socket()
clientSocket.connect((host, port))

number = input("Informe o numero: ")
clientSocket.send(number.encode())

while clientSocket.recv(1024).decode() == "None":
    print("Numero nao cadastrado em nossa base !!!")
    number = input("Digite novamente: ")
    clientSocket.send(number.encode())

option = input("CHOSE: ")

while option != '4':
    clientSocket.send(option.encode())

    print(clientSocket.recv(1024).decode())

    option = input(clientSocket.recv(1024).decode())
    if option == '4':
        print("Finalizando sessão")

clientSocket.close()