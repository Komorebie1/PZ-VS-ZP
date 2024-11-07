from zeroconf import Zeroconf, ServiceBrowser
import time
import socket

class MyListener:

    def __init__(self):
        self.server_ip = None

    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            address = socket.inet_ntoa(info.addresses[0])
            print(f"Service {name} added, IP address: {address}")
            self.server_ip = address

def discover_service():
    zeroconf = Zeroconf()
    listener = MyListener()

    print("Searching for service...")
    IPv4 = listener.server_ip
    zeroconf.close()
    return IPv4

if __name__ == "__main__":
    discover_service()