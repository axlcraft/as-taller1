import socket
HOST = 'localhost'
PORT = 9000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print("el servidor está a la espera de conexiones ...")

cliente, direccion = servidor.accept()
print("un cliente se conectó desde la dirección  {direccion}")

datos = cliente.recv(1024)
cliente.sendall(b"hola! " + datos)
cliente.close()