#!/bin/python3

import sys
import socket
from datetime import datetime

# define target to scan
if len(sys.argv) == 2:
    # puts hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguments.")
    print("Syntax: python3 netw-scanner.py <ip>")
    
# make output look pretty
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

# get what ports want to be scanned
start_port = input("From what port would you like to start testing at?")
print("-" * 50)
end_port = input("What port would you like to stop at?")
print("-" * 50)

nospace_sp = start_port.replace(" ", "")
nospace_ep = end_port.replace(" ", "")

if nospace_sp.isnumeric() == True and nospace_ep.isnumeric() == True:
    
    # check whether start_port and end_port are ints
    if int(nospace_sp) < 65535 and int(nospace_sp) > 0:
        if int(nospace_ep) < 65535 and int(nospace_ep) > 0:

            # iterate over various ports and try to find open ones
            try:
                for port in range(int(nospace_sp), int(nospace_ep)):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((target, port))
                    if result == 0:
                        print(f"Port {port} is open.")
                    s.close()

            except keyboard_interrupt:
                print("/nExciting program. //")
                sys.exit()
                
            except socket.gaierror:
                print("Hostname could not be resolved. //")
                sys.exit()
                
            except socket.error:
                print("Could not connect to a server. //")
                sys.exit()  
else:
    print("Input is not a valid port number. //")
    sys.exit()
    

    
    
    
    
    

