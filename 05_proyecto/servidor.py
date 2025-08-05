# Servidor
import socket
from datetime import datetime  # Para obtener la hora actual

HOST = 'localhost'
PORT = 9002  # Cambiamos el puerto para no interferir con otros ejemplos

# Creamos el socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor de hora actual en espera de conexiones...")

while True:
    # Aceptamos conexión entrante
    cliente, direccion = servidor.accept()
    print(f"Conectado desde: {direccion}")

    # Recibimos solicitud del cliente
    datos = cliente.recv(1024)
    if not datos:
        break

    print("Solicitud recibida")

    # Obtenemos la fecha y hora actual
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Enviamos la hora actual al cliente
    cliente.sendall(hora_actual.encode())

    # Cerramos la conexión con el cliente
    cliente.close()
