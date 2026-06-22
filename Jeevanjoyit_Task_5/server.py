import socket
import threading

HOST = "127.0.0.1"
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                username = usernames[index]

                clients.remove(client)
                usernames.remove(username)
                client.close()

                broadcast(f"🔴 {username} left the chat.".encode())
                print(f"{username} disconnected.")
            break


def receive():
    print("Server is running...")

    while True:
        client, address = server.accept()

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()

        clients.append(client)
        usernames.append(username)

        print(f"{username} connected from {address}")

        broadcast(f"🟢 {username} joined the chat.".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
