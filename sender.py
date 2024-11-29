import socket

SERVER_IP = '192.168.4.50' 
PORT = 12345              

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

message = "Hello, from Server!"
client_socket.sendall(message.encode())
print(f"Sent message: {message} through {SERVER_IP}:{PORT}")

client_socket.close()
