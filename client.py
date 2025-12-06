import socket

HOST = "127.0.0.1"
PORT = 22

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect. Is the server running?")
        return
    except PermissionError:
        print("Permission denied. Try running as administrator.")
        return

    print(f"Connected to server on {HOST}:{PORT}")
    print('Type a message. Type "quit" to exit.')

    while True:
        message = input("You: ")
        if not message:
            continue

        client_socket.sendall(message.encode())

        if message.lower() == "quit":
            print("Closing connection...")
            break

        data = client_socket.recv(1024)
        print("Server:", data.decode().strip())

    client_socket.close()
    print("Client closed.")

if __name__ == "__main__":
    main()