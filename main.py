# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Limit game speed
    clock = pygame.time.Clock()
    dt = 0

    # Create a Player object in the centre of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update player position/angle
        player.update(dt)
        
        # Blacken screen
        screen.fill("black")

        # Redraw the player
        player.draw(screen)
        

        # Refresh the screen
        pygame.display.flip()

        # Limit to 60fps and update delta time
        dt  = clock.tick(60) / 1000


if __name__ == "__main__":
    main()