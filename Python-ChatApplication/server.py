import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Use '0.0.0.0' to allow connections from any IP
PORT = 5555

clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                # Remove the client if unable to send message
                remove_client(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                broadcast(message, client)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break

def remove_client(client):
    if client in clients:
        clients.remove(client)

def start_server():
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"Connected with {address}")

        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    start_server()
