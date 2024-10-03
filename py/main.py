# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()  # Ensure these are sprite groups
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    updatable.add(player1)
    drawable.add(player1)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = [updatable]
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:  # Make sure you are checking for keydown events
                if event.key == pygame.K_SPACE:
                    shot = player1.shoot()
                    if shot:  # Check that shot was created
                        updatable.add(shot)
                        drawable.add(shot)

        dt = clock.tick(60) / 1000


        for i in updatable:
            i.update(dt)

        for asteroid in asteroids:
            if player1.collisions(asteroid):
                print("game over!")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
      
if __name__ == "__main__":
    main()