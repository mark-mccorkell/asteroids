# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Limit game speed
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Blacken screen and refresh
        screen.fill("black")
        pygame.display.flip()

        # Limit to 60fps and update delta time
        dt  = clock.tick(60) / 1000


if __name__ == "__main__":
    main()