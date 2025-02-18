import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host =input("enter the host: ")
port = int(input("enter the port: "))
server_address = (host,port)

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
