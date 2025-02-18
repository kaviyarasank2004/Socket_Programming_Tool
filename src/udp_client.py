import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 10001)

try:
    while True:
        message = input("Enter message for server (or 'exit' to quit) >> ")
        if message.lower() == 'exit':
            print("Closing connection...")
            break

        sock.sendto(message.encode(), server_address)  # Send message to server

        data, _ = sock.recvfrom(1024)  # Receive response from server
        print(f"Received from server: {data.decode()}")

except KeyboardInterrupt:
    print("\nClient shutting down...")

finally:
    sock.close()
