import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Creates Player object (instance has to be after groups are created)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create new AsteroidField object
    asteroid_field = AsteroidField()

    # Delta-time
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Refreshes the screen
        pygame.display.flip()

        # limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()