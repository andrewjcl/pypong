import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption('PyPong')
clock = pygame.time.Clock()

bg_surf = pygame.Surface((400, 800))
bg_surf.fill('WHITE')

ball_x = 200
ball_y = 400

ball_x_speed = 2
ball_y_speed = -2

cpu_y1 = 350
cpu_y2 = 450


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
                cpu_y1 -= 10
                cpu_y2 -= 10
        if keys[pygame.K_z]:
                cpu_y1 += 10
                cpu_y2 += 10
    
    # Draw background
    screen.blit(bg_surf, (0, 0))

   # Player 
    mouse_cords = pygame.mouse.get_pos()
    player_y1 = mouse_cords[1] - 50
    player_y2 = mouse_cords[1] + 50
    pygame.draw.line(screen, 'Black', (400, player_y1), (400, player_y2), 20)

    # CPU
    pygame.draw.line(screen, 'Black', (0, cpu_y1), (0, cpu_y2), 20)


    # Ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Collision with top and bottom
    if ball_y <= 0 or ball_y >= 800:
        ball_y_speed *= -1

    # Collision with player
    if ball_x == 390:
        if ball_y >= player_y1 and ball_y <= player_y2:
            ball_x_speed *= -1

    if ball_x == 10:
        if ball_y >= cpu_y1 and ball_y <= cpu_y2:
            ball_x_speed *= -1

    pygame.draw.circle(screen, 'Black', (ball_x, ball_y), 6, 6)
    pygame.display.update()
    clock.tick(60)
