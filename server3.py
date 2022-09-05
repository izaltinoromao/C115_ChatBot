import socket

host = 'localhost'
port = 5052

contas = [{"Numero" : "999999999", "Fatura" : "R$ 200,00", "Saldo" : "50 minutos", "Operadora" : "Vivo"},
          {"Numero" : "888888888", "Fatura" : "R$ 100,00", "Saldo" : "30 minutos", "Operadora" : "Claro"},
          {"Numero" : "777777777", "Fatura" : "R$ 50,00", "Saldo" : "45 minutos", "Operadora" : "Tim"}]

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
connection.send(validadoStr.encode())

while(validadoStr == "None"):
    number = connection.recv(1024).decode()
    validado = valida(number)
    validadoStr = str(validado)
    connection.send(validadoStr.encode())


while True:

    option = connection.recv(1024).decode()
    if option == '4':
        break
    elif option == '1':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("Sua fatura é de: " + fatura['Fatura']).encode())
    elif option == '2':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("Seu saldo é de: " + fatura['Saldo']).encode())
    elif option == '3':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("Sua Operadora é: " + fatura['Operadora']).encode())        

    print(f"[CLIENT] -> {option}")
    connection.send("CHOSE: ".encode())

connection.close()

