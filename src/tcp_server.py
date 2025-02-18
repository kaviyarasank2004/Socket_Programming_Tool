import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows reusing the same port

# Bind the socket
server =input("enter the ip: ")
port =input("enter the port: ")

server_address = (server,port)
print(f"Starting up on {server} port {port}")
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
