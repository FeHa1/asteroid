import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):

    # use the same as the class Asteroid
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.white, (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt  

