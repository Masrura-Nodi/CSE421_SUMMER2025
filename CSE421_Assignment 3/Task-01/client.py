import socket

port = 5050
format = 'utf-8'
data = 16

device_name = socket.gethostname()
client_ip = socket.gethostbyname(device_name)

socket_address = (client_ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(socket_address)

def sending_message(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length_str = str(msg_length).encode(format)
    msg_length_str += b' ' * (data - len(msg_length_str))

    client.send(msg_length_str)
    client.send(message)

    sent_from_server = client.recv(128).decode(format)
    print("Sent from server:", sent_from_server)

sending_message(f"Client's device name is {device_name} and the ip address is {client_ip}")
sending_message("disconnect")