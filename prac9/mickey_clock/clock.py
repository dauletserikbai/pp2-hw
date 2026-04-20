import pygame
import sys 
from datetime import datetime 

class Clock:
    def __init__(self):
        pygame.init() 
        
        self.WIDTH = 500
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) #setting screen
        pygame.display.set_caption("Mickey Clock")

        self.bg = pygame.image.load(r"C:\Users\user\Desktop\pp2-hw\prac9\mickey_clock\images\background.png")
        self.minute_hand = pygame.image.load(r"C:\Users\user\Desktop\pp2-hw\prac9\mickey_clock\images\minute.png")
        self.second_hand = pygame.image.load(r"C:\Users\user\Desktop\pp2-hw\prac9\mickey_clock\images\hour.png")

        self.center = (self.WIDTH // 2, self.HEIGHT // 2) 

        self.clock = pygame.time.Clock() 

    def rotate(self, image, angle): 
        rotated_image = pygame.transform.rotozoom(image, -angle, 1) 
        rect = rotated_image.get_rect(center=self.center) 
        return rotated_image, rect

    def get_time_angles(self):
        now = datetime.now() 

        minute = now.minute
        second = now.second + now.microsecond / 1_000_000 
        

        minute_angle = (minute + second / 60) * 6 
        
        second_angle = second * 6
        

        return minute_angle, second_angle

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 

            self.screen.fill((0, 0, 0)) 
            self.screen.blit(self.bg, (0, 0)) 

            minute_angle, second_angle = self.get_time_angles() 

            min_img, min_rect = self.rotate(self.minute_hand, minute_angle) 
            sec_img, sec_rect = self.rotate(self.second_hand, second_angle) 
            

            self.screen.blit(min_img, min_rect)
            self.screen.blit(sec_img, sec_rect) 
            
            pygame.display.flip() 
            self.clock.tick(60) 