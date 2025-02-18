import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows reusing the same port

# Bind the socket
server_name = '127.0.0.1'
server_address = (server_name, 10001)
print(f"Starting up on {server_name} port {server_address[1]}")
sock.bind(server_address)
sock.listen(1)

try:
    while True:
        print("Waiting for a connection...")
        connection, client_address = sock.accept()
        print(f"Client connected: {client_address}")

        with connection:
            while True:
                data = connection.recv(1024)
                if not data:
                    print("Client disconnected")
                    break  # Exit the loop when the client disconnects

                print(f"Received: {data.decode()}")
                message = input("Enter the message for the client >> ")
                connection.sendall(message.encode())

except KeyboardInterrupt:
    print("\nServer shutting down...")
finally:
    sock.close()
