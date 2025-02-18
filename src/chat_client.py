import socket
import threading

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
nickname = input("Choose your nickname: ")
host = input("enter the host: ")
port=input("enter the port: ")

client.connect((host,int(port)))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

#start the thread

receiving_thread = threading.Thread(target=receive)
receiving_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
