import os


def main():
    while True:
        print("\nSocket Programming Tool")
        print("1. Port Scanner")
        print("2. Banner Grabber")
        print("3. TCP Client/Server")
        print("4. UDP Client/Server")
        print("5. Chat Application")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("python port_scanner.py")
        elif choice == "2":
            os.system("python3 banner_scanner.py")
        elif choice == "3":
            os.system("python tcp_server.py & python tcp_client.py")
        elif choice == "4":
            os.system("python udp_server.py & python udp_client.py")
        elif choice == "5":
            os.system("python chat_server.py & python chat_client.py")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
