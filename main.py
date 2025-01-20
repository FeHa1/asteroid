import pygame
from constants import *

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)

    while (True): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #for closing the window
                return
        screen.fill(black)
        pygame.display.flip()

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()