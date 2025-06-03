# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Blacken screen and refresh
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()