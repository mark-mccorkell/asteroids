import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Limit game speed
    clock = pygame.time.Clock()
    dt = 0

    # Create groups to hold game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)


    # Create a Player object in the centre of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update pall updatable objects
        updatable.update(dt)
        #player.update(dt)

        # Blacken screen
        screen.fill("black")

        # Redraw all redrawable objects
        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)
        

        # Refresh the screen
        pygame.display.flip()

        # Limit to 60fps and update delta time
        dt  = clock.tick(60) / 1000


if __name__ == "__main__":
    main()