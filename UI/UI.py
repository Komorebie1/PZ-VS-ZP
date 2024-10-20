import pygame
import sys
# 初始化pygame
pygame.init()

# 定义窗口大小
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("植物大战僵尸 - 主菜单")

# 定义颜色
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
# 定义字体
font = pygame.font.SysFont("SimHei", 40)
# 定义按钮
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.callback = callback
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        window.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
    def on_click(self):
        if self.is_hovered():
            self.callback()
# 按钮回调函数
def start_adventure_mode():
    print("进入冒险模式...")
    # 这里可以跳转到实际的游戏逻辑
def start_challenge_mode():
    print("进入挑战模式...")
    # 这里可以跳转到实际的游戏逻辑
def quit_game():
    pygame.quit()
    sys.exit()

# 创建按钮
buttons = [
    Button("冒险模式", 300, 200, 200, 60, start_adventure_mode),
    Button("挑战模式", 300, 300, 200, 60, start_challenge_mode),
    Button("退出游戏", 300, 400, 200, 60, quit_game)
]
# 主菜单界面的循环
def menu_loop():
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_hovered():
                        button.on_click()
        # 填充背景颜色
        window.fill(WHITE)
        # 绘制按钮并检测鼠标悬停状态
        for button in buttons:
            if button.is_hovered():
                button.color = DARK_GRAY  # 鼠标悬停时变暗
            else:
                button.color = GRAY  # 默认颜色
            button.draw(window)
        # 更新屏幕显示
        pygame.display.update()
# 启动主菜单
menu_loop()
