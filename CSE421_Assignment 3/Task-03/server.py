import socket
import threading

port = 5050
format = 'utf-8'
DATA = 16
DISCONNECT_MSG = "disconnect"

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server_socket_address = (server_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)
server.listen()
print("Our server is listening...")

def client_handle(server_socket, client_add):
    print("Connected to", client_add)
    connected = True

    while connected:
        upcoming_message_length = server_socket.recv(DATA).decode(format)

        if not upcoming_message_length.strip():
            print("Client disconnected abruptly:", client_add)
            break

        print("Upcoming message length is", upcoming_message_length.strip())
        message_length = int(upcoming_message_length.strip())
        message = server_socket.recv(message_length).decode(format)

        if message.lower() == DISCONNECT_MSG:
            server_socket.send("BYE. NICE TO SERVER U".encode(format))
            print("Disconnected with", client_add)
            connected = False

        else:
            vowels = 'aeiouAEIOU'
            count = 0

            for ch in message:
                if ch in vowels:
                    count += 1

            if count == 0:
                server_socket.send("Not enough vowels".encode(format))

            elif count <= 2:
                server_socket.send("Enough vowels I guess".encode(format))

            else:
                server_socket.send("Too many vowels".encode(format)) 

        print("Received:", message)
        
    server_socket.close()

while True:
    server_socket, client_add = server.accept()
    thread = threading.Thread(target = client_handle, args = (server_socket, client_add))
    thread.start()

    