import pygame
from circleshape import CircleShape

class Asteroid(CircleShape): 

    containers = None  

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if self.containers:
            self.add(*self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.white, (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt  

    