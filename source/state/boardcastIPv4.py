from zeroconf import ServiceInfo, Zeroconf
import socket
import time

zeroconf = Zeroconf()
ip = socket.inet_aton(socket.gethostbyname(socket.gethostname()))
service_info = ServiceInfo(
    "_http._tcp.local.",
    "My Service._http._tcp.local.",
    addresses=[ip],
    port=12345,
    properties={},
    server="my-service.local.",
)

zeroconf.register_service(service_info)
print("Service registered.")
start_time = time.time()
while time.time() - start_time <= 30:
    time.sleep(1)
zeroconf.close()