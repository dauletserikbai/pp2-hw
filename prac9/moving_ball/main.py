import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock() 

ball = Ball(WIDTH // 2, HEIGHT // 2, screen_width=WIDTH, screen_height=HEIGHT) 

running = True
while running:
    clock.tick(20) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]: 
        ball.move(-1, 0)
    if keys[pygame.K_RIGHT]: 
        ball.move(1, 0)
    if keys[pygame.K_UP]: 
        ball.move(0, -1)
    if keys[pygame.K_DOWN]: 
        ball.move(0, 1)

    screen.fill((255, 255, 255)) 
    ball.draw(screen) 

    pygame.display.flip()

pygame.quit()
