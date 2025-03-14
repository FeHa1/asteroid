import pygame

class CircleShape(pygame.sprite.Sprite):

    white = (255, 255, 255)

    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(
            screen,               
            self.white,           
            self.triangle(),      
            2                     
        )

    def update(self, dt):
        # sub-classes must override
        pass


    def check_collision(self, other):
        """
        Check if this circle collides with another CircleShape.
        Returns True if they collide, otherwise False.
        """
        distance = self.position.distance_to(other.position)
        
        return distance <= (self.radius + other.radius)