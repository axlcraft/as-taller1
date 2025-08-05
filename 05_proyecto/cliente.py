# Cliente
import socket

HOST = 'localhost'
PORT = 9002  # Mismo puerto que el servidor

# Conectamos al servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Enviamos un mensaje cualquiera (el contenido no importa en este caso)
cliente.sendall(b"hora")

# Recibimos y mostramos la hora actual del servidor
respuesta = cliente.recv(1024)
print(f"La hora actual en el servidor es: {respuesta.decode()}")

# Cerramos la conexión
cliente.close()
