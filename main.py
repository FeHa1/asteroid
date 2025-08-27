import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def get_asteroid_points(radius):
    if radius >= ASTEROID_MIN_RADIUS * 3:
        return 10
    elif radius >= ASTEROID_MIN_RADIUS * 2:
        return 25
    else:  
        return 50
    

def show_game_over(screen, score):
    # Show the Game Over screen and wait for space to be pressed
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    
    game_over_text = font.render("GAME OVER!", True, (255, 255, 255))
    score_text = small_font.render(f"Final Score: {score}", True, (255, 255, 255))
    continue_text = small_font.render("Press SPACE to continue", True, (255, 255, 255))
    
   
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  
        
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(continue_text, continue_rect)
        pygame.display.flip()
        clock.tick(60)

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    black = (0, 0, 0)

    while True: 
        score = 0  
        font = pygame.font.Font(None, 36)  

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        Player.containers = (updatable, drawable) 
        Asteroid.containers = (updatable, drawable, asteroids)
        AsteroidField.containers = (updatable,)
        Shot.containers = (updatable, drawable, shots)

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()

        clock = pygame.time.Clock()
        dt = 0

        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill(black)
            updatable.update(dt)

            for asteroid in asteroids:
                if player.check_collision(asteroid):
                    game_running = False
                    break

            for shot in shots:
                for asteroid in asteroids:
                    if shot.check_collision(asteroid):
                        
                        score += get_asteroid_points(asteroid.radius)
                        shot.kill()
                        asteroid.kill()
                        break
         
            for sprite in drawable:
                sprite.draw(screen)
            
            # Show score
            score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            dt = clock.tick(60) / 1000
        
        
        if not show_game_over(screen, score):
            break 
        
        pygame.event.clear()
        pygame.key.get_pressed()


if __name__ == "__main__":
    main()

