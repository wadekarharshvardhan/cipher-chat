import socket
import threading
import os

HOST = '0.0.0.0'  # Accept connections from any IP
PORT = int(os.environ.get('PORT', 12345))

clients = []

def handle_client(client_socket, addr):
    print(f"[+] {addr} connected.")
    while True:
        try:
            msg = client_socket.recv(1024)
            broadcast(msg, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[LISTENING] Server running on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
