import json
import socket
import threading

HOST = "0.0.0.0"
PORT = 1848
SPEED = 10

players = {}


def handle_client(conn: socket.socket, addr):
    players[addr] = {"y": 0, "points": 0, "socket": conn}
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        try:
            msg = json.loads(msg)
        except:
            continue
        dy = msg.get("dy", 0)
        players[addr]["y"] += dy * SPEED


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()
while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    if len(players) >= 2:
        break

# thread = threading.Thread(target=process_game)
# thread.start()
