import pygame
import sys

# 初始化pygame
pygame.init()

# 定义窗口大小
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 477
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)  # 允许窗口调整大小
pygame.display.set_caption("植物大战僵尸 - 主菜单")

# 加载背景图片
background_image = pygame.image.load("image/mb-header.jpg")  # 将"background.jpg"替换为你的背景图片路径
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))  # 调整图片大小适应窗口

# 定义颜色
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 128)

# 定义字体
font = pygame.font.SysFont("SimHei", 40)

# 定义按钮
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = LIGHT_BLUE
        self.callback = callback

    def draw(self, window):
        # 绘制阴影效果
        shadow_offset = 5
        shadow_rect = pygame.Rect(self.rect.x + shadow_offset, self.rect.y + shadow_offset, self.rect.width, self.rect.height)
        pygame.draw.rect(window, DARK_GRAY, shadow_rect, border_radius=15)  # 阴影的圆角矩形

        # 绘制按钮
        pygame.draw.rect(window, self.color, self.rect, border_radius=15)  # 圆角矩形

        # 绘制边框
        pygame.draw.rect(window, DARK_BLUE, self.rect, 3, border_radius=15)

        # 绘制文本
        text_surface = font.render(self.text, True, WHITE)
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
    Button("冒险模式", 50, 200, 200, 60, start_adventure_mode),
    Button("挑战模式", 50, 300, 200, 60, start_challenge_mode),
    Button("退出游戏", 50, 400, 200, 60, quit_game)
]

# 主菜单界面的循环
def menu_loop():
    global window, background_image
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
            # 处理窗口大小变化
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                background_image = pygame.transform.scale(background_image, (event.w, event.h))  # 根据新窗口大小调整背景图片尺寸

        # 绘制背景图片
        window.blit(background_image, (0, 0))

        # 绘制按钮并检测鼠标悬停状态
        for button in buttons:
            if button.is_hovered():
                button.color = (135, 206, 250)  # 鼠标悬停时浅蓝色
            else:
                button.color = LIGHT_BLUE  # 默认颜色
            button.draw(window)

        # 更新屏幕显示
        pygame.display.update()

# 启动主菜单
menu_loop()
