import socket
import json
import threading

# йогурт галичина

HOST = "127.0.0.1"
PORT = 1848

NICKNAME = input("Введіть ваш нікнейм:")
client_socket = None


def handle_server():
    global client_socket
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    client_socket.send(NICKNAME.encode())

    id_data = client_socket.recv(1024).decode()
    print(f"Отримано з сервера: {id_data}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        try:
            data = json.loads(data)
            if data["type"] == "PLAYER_POS":
                ...
            if data["type"] == "PLAYER_POINTS":
                ...
            if data["type"] == "BALL_POS":
                ...
        except:
            continue


def send_possition(dy):
    global client_socket

    if client_socket == None:
        return

    client_socket.send(json.dumps({"nickname": NICKNAME, "dy": dy}).encode())


threading.Thread(target=handle_server).start()
