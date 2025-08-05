# Servidor
import socket

HOST = 'localhost' 
PORT = 9000 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

while True:
    
    print("El servidor 'Echo' esta esperando conexiones...")

    cliente, direccion = servidor.accept() 
    print(f"Un cliente se conecto desde la direccion {direccion}")

    datos = cliente.recv(1024)

    
    if not datos:
        break
    
   
    print("Datos recibidos: ", datos)
    
   
    cliente.sendall(datos)

    
    cliente.close()

