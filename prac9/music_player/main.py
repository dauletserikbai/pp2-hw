import pygame
import sys 
from player import MusicPlayer 

pygame.init() 

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player") 
font = pygame.font.SysFont(None, 25) 
clock = pygame.time.Clock() 
player = MusicPlayer("music") 

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_p: 
                player.play()
            elif event.key == pygame.K_s: 
                player.stop()
            elif event.key == pygame.K_n: 
                player.next_track()
            elif event.key == pygame.K_b: 
                player.prev_track()
            elif event.key == pygame.K_q: 
                running = False

    track_text = font.render(f"Track: {player.get_current_track_name()}", True, (173, 216, 230))
    screen.blit(track_text, (20, 40)) 

    status_text = font.render(f"Status: {player.status}", True, (173, 216, 230))
    screen.blit(status_text, (20, 80)) 

    progress = player.get_progress() 
    pygame.draw.rect(screen, (173, 216, 230), (20, 140, 560, 20)) 
    pygame.draw.rect(screen, (0, 200, 0), (20, 140, int(560 * progress), 20)) 

    instructions = [
        "P=Play <3  S=Stop <3  N=Next <3  B=Back <3  Q=Quit <3"
    ]

    for i, line in enumerate(instructions):
        txt = font.render(line, True, (180, 180, 180))
        screen.blit(txt, (20, 200 + i * 25)) 

    pygame.display.flip() 
    clock.tick(30)

pygame.quit()
sys.exit()