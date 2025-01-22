import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    white = (255, 255, 255)

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(
            screen,               # Screen object
            self.white,           # Color (white)
            self.triangle(),      # List of points (triangle vertices)
            2                     # Line width
        )

    def update(self, dt):
        # sub-classes must override
        pass