import socket
HOST = 'localhost'
PORT = 9000

cliente = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

cliente.sendall(b"mundo!")
respuesta = cliente.recv(1024)
print(f"respuesta: {respuesta}")


cliente.close()
