import socket

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

while True:
    server_socket, client_add = server.accept()
    print("Connected to ", client_add)
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
            if message.isdigit():
                hrs = int(message)

                if hrs <= 40:
                    salary = 200 * hrs 
                
                else:
                    salary = 8000 + 300 * (hrs - 40)
                
                server_socket.send(f"Salary: Tk {salary}".encode(format))
            
            else:
                server_socket.send(f"Invalid.".encode(format))
                
        print("Received:", message)
        
    server_socket.close()

    