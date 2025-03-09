import socket
import threading

clients = []  # 用来存储所有客户端

# 处理客户端的连接
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"[MESSAGE RECEIVED] {message}")
                # 将接收到的消息发送给其他客户端
                broadcast(message, client_socket)
        except:
            # 如果客户端断开连接，则移除客户端
            clients.remove(client_socket)
            client_socket.close()
            break

# 广播消息给所有客户端，除了发送者
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
                print(f"[MESSAGE SENT] {message}")
            except:
                clients.remove(client)
                client.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen()
    print("[SERVER STARTED] Waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
