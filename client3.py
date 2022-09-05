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

print("----------------------------------------------")
print("| 1 -> Fatura || 2 -> Saldo || 3 -> Titular  |")
print("| 4 -> Endereco de cobranca || 5 -> Finalizar|")
print("----------------------------------------------")
option = input("Selecione sua opção: ")

while option != '5':
    clientSocket.send(option.encode())
    print("______________________________________")
    print(clientSocket.recv(1024).decode())
    print("______________________________________")
    print("----------------------------------------------")
    print("| 1 -> Fatura || 2 -> Saldo || 3 -> Titular  |")
    print("| 4 -> Endereco de cobranca || 5 -> Finalizar|")
    print("----------------------------------------------")
    option = input(clientSocket.recv(1024).decode())
    if option == '5':
        print("Finalizando sessão")

clientSocket.close()