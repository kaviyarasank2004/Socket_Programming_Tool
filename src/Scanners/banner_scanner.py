import socket

#

def banner(ip,port):
    try:
        #initilizing the socket and connect to the ip and port
        s=socket.socket()
        s.settimeout(10) #set time out
        s.connect((ip,int(port)))
        s.send(b'GET /\n\n')
        _banner=s.recv(1024).decode().strip()  # decode the recived banner
        if banner:
            print(f"banner for {ip}:{port} -> {_banner}")
        else:
            print("no banner found")
    except socket.error as e:
        print(f"error:{e}")
        #ensuring the  socket is closed after the operation
    finally:
        s.close()
def main():
    ip =input("enter the target ip:")
    port =(input("enter the target port:"))
    banner(ip,port)

if __name__ == "__main__":
    main()