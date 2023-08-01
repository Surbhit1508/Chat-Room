import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Use the server IP address
PORT = 5555

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection to server lost.")
            client.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    # Start a separate thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input()
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
