import pygame
import socket
import threading

# 初始化pygame
pygame.init()

# 窗口设置
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client Window")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 物品列表
objects = []

# 接收服务器的更新
def receive_updates(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                x, y = map(int, message.split(','))
                objects.append((x, y))  # 更新物品位置
        except:
            break

# 发送物体位置
def send_position(client_socket, x, y):
    message = f"{x},{y}"
    client_socket.sendall(message.encode())

def main():
    # 创建客户端socket并连接服务器
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))
    # 启动接收线程
    receive_thread = threading.Thread(target=receive_updates, args=(client_socket,))
    receive_thread.start()

    running = True
    while running:
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                client_socket.close()
                pygame.quit()

            # 当鼠标左键按下时，发送物品位置
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                objects.append((x, y))
                send_position(client_socket, x, y)

        # 绘制所有物体
        for obj in objects:
            pygame.draw.rect(win, RED, (obj[0], obj[1], 50, 50))

        pygame.display.update()

if __name__ == "__main__":
    main()
