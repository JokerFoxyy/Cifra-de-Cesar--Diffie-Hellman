from socket import *
serverName = "192.168.56.1"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

G = 15
N = 97
X = 5
R1 = (G ** X) % N

print("G: ", G)
print("N: ", N)
print("X: ", X)
print("R1: ", R1)

message = f"{G},{N},{R1}"

clientSocket.send(bytes(message, "utf-8"))

R2 = int(clientSocket.recv(1024))
print("R2: ", R2)

K = (R2 ** X) % N
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