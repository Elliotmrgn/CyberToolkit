import socket, threading
import sys

#TODO: maybe change to update as it finds port (websocket)

# Function ping_check - Ping a device to see if it is active
def ping_check(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False
    

# Function port_check - Test a port to see if it is open
def port_check(host, start_port, stop_port):
    if ping_check:
        open_ports = []
        for port in range(start_port, stop_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(.001)  # Set timeout for socket connection
            result = sock.connect_ex((host, port))
            print(result)
            if result == 0:
                open_ports.append(port)
            sock.close()
        print()
        print(open_ports)
        return open_ports
    
    else: return None
    