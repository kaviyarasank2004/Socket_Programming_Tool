import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to an address and port
server_address = ('127.0.0.1', 10001)
sock.bind(server_address)

print(f"UDP Server listening on {server_address}")

try:
    while True:
        data, client_address = sock.recvfrom(1024)  # Receive data from client
        print(f"Received from {client_address}: {data.decode()}")

        # Reply to client
        message = input("Enter message for client >> ")
        sock.sendto(message.encode(), client_address)

except KeyboardInterrupt:
    print("\nServer shutting down...")

finally:
    sock.close()
