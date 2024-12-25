import socket
import time
SERVER_IP = '192.168.5.7' 
PORT = 56789              

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
i=0
while True:
	message = f"Hello {i}, from pitwo!"
	client_socket.sendall(message.encode())
	print(f"Sent message: {message} through {SERVER_IP}:{PORT}")
	i+=1
	time.sleep(1)

client_socket.close()
