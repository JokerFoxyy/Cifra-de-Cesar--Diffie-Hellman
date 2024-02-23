from socket import *
serverPort = 1200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")

connectionSocket, addr = serverSocket.accept()

print ("Server esperando chave\n")
received_message = connectionSocket.recv(1024)
G, N, key_1 = map(int, received_message.decode("utf-8").split(","))
Y = 1024
key_2 = (G ** Y) % N
K = (key_1 ** Y) % N

print("Y: ", Y)

print("R2: ", key_2)

print("K: ", K)

connectionSocket.send(bytes(str(key_2), "utf-8"))

sentence = connectionSocket.recv(65000)

print(f'Recebido Criptografado: {str(sentence, "utf-8")}')

decrypted = bytes([byte - 3 for byte in sentence])

received = str(decrypted, "utf-8")

print ("Decriptografado:", received)

capitalizedSentence = received.upper()

print(f'Enviado antes de criptografar: {capitalizedSentence}')

sent = bytes([byte + 3 for byte in bytes(capitalizedSentence, "utf-8")])

connectionSocket.send(sent)
print (f"Enviado criptografado: {sent.decode()}")

connectionSocket.close()
