import pyfiglet
import sys
import socket

# ascii banner
ascii_banner = pyfiglet.figlet_format("port scanner")
print(ascii_banner)

if len(sys.argv)== 2 :
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument")

print("-" * 50)
print("scanning target"+target)
print("-" * 50)

#checking for open ports
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result ==0:
            print("port->{} is open ".format(port))
        s.close()
#handling the errors
except KeyboardInterrupt:
    print("\n exiting program")
    sys.exit()
except socket.gaierror:
    print("host name cannot br resolved")
except socket.error:
    print("\n server not responding")
