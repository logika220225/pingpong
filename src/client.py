import socket
import json
import threading

# йогурт галичина

HOST = "127.0.0.1"
PORT = 1848

NICKNAME = input("Введіть ваш нікнейм:")

def handle_server():
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    client_socket.send(NICKNAME.encode())

    id_data = client_socket.recv(1024).decode()
    print(f"Отримано з сервера: {id_data}")
    
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Отримано з сервера: {data}")

handle_server()