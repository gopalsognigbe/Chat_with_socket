import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.bind((HOST_IP,HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, Port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"connexion etablie avec {client_address}")

while True:
    texte_envoye = input("Serveur :")
    connection_socket.sendall(texte_envoye.encode())

    text_recu = connection_socket.recv(MAX_DATA_SIZE)
    print(text_recu.decode())
    if texte_envoye == "fin" :
        break

s.close()
connection_socket.close()