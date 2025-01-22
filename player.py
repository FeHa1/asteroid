import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape, PLAYER_RADIUS):
    def __init__(self, x, y):
        pass


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]