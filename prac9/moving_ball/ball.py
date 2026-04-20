import pygame

class Ball:
    def __init__(self, x, y, radius=25, color=(255, 182, 193), speed=20, screen_width=800, screen_height=600):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed 
        self.screen_width = screen_width
        self.screen_height = screen_height 

    def draw(self, screen): #drawing ball 
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius) 
        

    def move(self, dx, dy):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed 

        if self.radius <= new_x <= self.screen_width - self.radius: 
            self.x = new_x 
        if self.radius <= new_y <= self.screen_height - self.radius:  
            self.y = new_y 