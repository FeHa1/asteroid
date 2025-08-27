import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    
    clock = pygame.time.Clock()
    dt = 0


    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #for closing the window
                return

        screen.fill(black)
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return  
            
        # Colisión disparo-asteroide
        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid):
                    # Destruir tanto el disparo como el asteroide
                    shot.kill()
                    asteroid.kill()
                    break  # Salir del bucle interno para evitar errores
     
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

