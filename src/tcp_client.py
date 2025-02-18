import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = '127.0.0.1'
port = 10001
sock.connect((server_address, port))
print(f"Connected to {server_address} port {port}")

try:
    while True:
        message = input("Enter message for server (or type 'exit' to quit) >> ")
        if message.lower() == 'exit':
            print("Closing connection...")
            break  # Exit loop and close socket

        sock.sendall(message.encode())  # Send data

        data = sock.recv(1024)  # Receive response
        if not data:
            print("Server disconnected.")
            break  # Exit loop if server closes the connection

        print(f"Received from server: {data.decode()}")

except KeyboardInterrupt:
    print("\nClient shutting down...")

finally:
    sock.close()
