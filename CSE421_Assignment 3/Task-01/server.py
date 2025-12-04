import socket

port = 5050
format = 'utf-8'
DATA = 16

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server_socket_address = (server_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)
server.listen()
print("Our server is listening...")

while True:
    server_socket, client_add = server.accept()
    print("Connected to ", client_add)
    connected = True
    while connected:
        upcoming_message_length = server_socket.recv(DATA).decode(format)
        print("Upcoming message length is", upcoming_message_length.strip())
        message_length = int(upcoming_message_length.strip())
        message = server_socket.recv(message_length).decode(format)
        if message == 'disconnect':
            print("Disconnected with", client_add)
            connected = False
        print(message)
        server_socket.send("Message received.".encode(format))

    server_socket.close()