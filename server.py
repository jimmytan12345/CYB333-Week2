import socket

HOST = "127.0.0.1"
PORT = 22 


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
    except PermissionError:
        print("Permission denied. Try running server as Administrator or using sudo.")
        return

    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    client_socket, client_addr = server_socket.accept()
    print(f"Client connected: {client_addr}")

    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected")
                break

            message = data.decode().strip()
            print("Client says:", message)

            if message.lower() == "quit":
                print("Client requested to close connection.")
                break

            client_socket.sendall(f"Server got: {message}".encode())

    server_socket.close()
    print("Server shut down.")

if __name__ == "__main__":
    main()