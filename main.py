import pygame

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置人物的位置和大小
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height

# 设置人物的移动速度
player_speed = 5

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 处理键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # 绘制人物和背景
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
    pygame.display.update()

# 退出 Pygame
pygame.quit()
