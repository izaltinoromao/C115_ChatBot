import socket

host = 'localhost'
port = 5052

contas = [{"Numero" : "999999999", "Fatura" : "R$ 200,00", "Saldo" : "50 minutos", "Titular" : "Leonardo José", "End cobranca" : "Rua orlindo oliveira, 777"},
          {"Numero" : "888888888", "Fatura" : "R$ 100,00", "Saldo" : "30 minutos", "Titular" : "Izaltino Romão", "End cobranca" : "Rua guedes maia, 666"},
          {"Numero" : "777777777", "Fatura" : "R$ 50,00", "Saldo" : "45 minutos", "Titular" : "Samuel", "End cobranca" : "Av tiradentes, 888"}]

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
    if option == '5':
        break
    elif option == '1':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("Sua fatura é de: " + fatura['Fatura']).encode())
    elif option == '2':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("Seu saldo é de: " + fatura['Saldo']).encode())
    elif option == '3':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("O titular da conta é: " + fatura['Titular']).encode())    
    elif option == '4':
        fatura = next(x for x in contas if x["Numero"] == number)
        connection.send(("O endereco de cobranca é: " + fatura['End cobranca']).encode())    

    print(f"[CLIENT] -> {option}")
    connection.send("Selecione sua opção: ".encode())

connection.close()

