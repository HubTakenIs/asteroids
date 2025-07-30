import pygame
import sys

from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
def main():
    game = pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2) 
    AsteroidField()


   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.is_colliding(player):
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
