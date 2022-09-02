import socket

host = 'localhost'
port = 5052

contas = [{"Numero" : "999999999", "Fatura" : "R$ 200,00", "Saldo" : "50 minutos"},
          {"Numero" : "888888888", "Fatura" : "R$ 100,00", "Saldo" : "30 minutos"},
          {"Numero" : "888888888", "Fatura" : "R$ 100,00", "Saldo" : "30 minutos"}]

def valida(number):
    return next((x for x in contas if x["Numero"] == number), None)
          

serverSocket = socket.socket()
serverSocket.bind((host, port))
serverSocket.listen(1)

print("The server is ready")
connection, address = serverSocket.accept()
print(f"Connection stablished with {address}")


number = connection.recv(1024).decode()
validado = valida(number)
validadoStr = str(validado)
print(validadoStr)
connection.send(validadoStr.encode())

while(validadoStr == "None"):
    number = connection.recv(1024).decode()
    validado = valida(number)
    validadoStr = str(validado)
    print(validadoStr)
    connection.send(validadoStr.encode())


while True:

    option = connection.recv(1024).decode()
    if option == '3':
        break

    print(f"[CLIENT] -> {option}")
    connection.send("CHOSE: ".encode())

connection.close()

