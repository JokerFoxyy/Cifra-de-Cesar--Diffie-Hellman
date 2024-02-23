from socket import *
serverName = "10.1.70.4"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

G = 150
N = 220
X = 89


key_1 = (G ** X) % N

print("G: ", G)
print("N: ", N)
print("X: ", X)
print("R1: ", key_1)

message = f"{G},{N},{key_1}"

clientSocket.send(bytes(message, "utf-8"))

key_2 = int(clientSocket.recv(1024))
print("R2: ", key_2)

K = (key_2 ** X) % N
print("K: ", K)

sentence = input("Input lowercase sentence: ")
crypted_send_message = bytes([byte + 3 for byte in bytes(sentence, "utf-8")])

clientSocket.send(crypted_send_message)
print(f'Enviado criptografado: {crypted_send_message.decode()}')

modifiedSentence = clientSocket.recv(1024)
text = str(modifiedSentence,"utf-8")

print ("Recebido criptografado:", text)
decrypted = bytes([byte - 3 for byte in bytes(text, "utf-8")])
print(f'Decriptografado: {decrypted.decode()}')
clientSocket.close()