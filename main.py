import os


def main():
    print("Socket Programming Tool")
    print("1. Port Scanner")
    print("2. Chat Server")
    print("3. Chat Client")
    print("4. TCP Server")
    print("5. TCP Client")
    print("6. UDP Server")
    print("7. UDP Client")
    print("8. Banner Scanner")

    choice = input("Enter your choice: ")

    scripts = {
        "1": "port_scanner.py",
        "2": "chat_server.py",
        "3": "chat_client.py",
        "4": "tcp_server.py",
        "5": "tcp_client.py",
        "6": "udp_server.py",
        "7": "udp_client.py",
        "8": "banner_scanner.py"
    }

    if choice in scripts:
        os.system(f"python3 src/{scripts[choice]}")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
