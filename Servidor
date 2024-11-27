import socket

Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 8080)
print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

Enlazar el socket con la dirección y el puerto
server_socket.bind(server_address)

Escuchar conexiones entrantes
server_socket.listen(1)
print("Esperando conexiones...")

while True:
    # Aceptar una conexión entrante
    connection, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address[0]}:{client_address[1]}")

    # Recibir datos del cliente
    data = connection.recv(1024)
    print(f"Recibido: {data.decode()}")

    # Enviar respuesta al cliente
    response = "Hola, cliente!"
    connection.sendall(response.encode())

    # Cerrar la conexión
    connection.close()
    print("Conexión cerrada")
```

