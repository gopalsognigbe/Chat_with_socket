import socket
import time


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


print(f"Connexion au serveur {HOST_IP}, Port {HOST_PORT}...")
while True :
        
    
    try :
        s = socket.socket() 
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : Impossible de se connecter.   Reconnexion.....")
        time.sleep(4)
    else :
        print("connection etabliee")
        break


print("connecte au serveur")
data_recues = s.recv(MAX_DATA_SIZE)
if data_recues:
    print(data_recues.decode())
else:
    print("Aucune donnee")

while True :
    text_client = input ("Vous : ")
    s.sendall(text_client.encode())

    data_recues = s.recv(MAX_DATA_SIZE)
    if data_recues.decode() == "fin" :
        break
    print(data_recues.decode())
 
s.close()