import socket

HOST = '192.168.4.10' 
PORT = 12345           

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
while True:
    data = conn.recv(1024)  
    if not data:
        break
    print(f"Received data: {data.decode()} on {HOST}:{PORT}")

conn.close()
server_socket.close()
