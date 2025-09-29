
import pygame
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from constants import * # noqa: F403


def main():
    print(f"Starting Mockstroids — {SCREEN_WIDTH}x{SCREEN_HEIGHT}")  # noqa: F405
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = updatables
    Asteroid.containers = (asteroids,updatables,drawables)
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)  # noqa: F405
    AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60) / 1000

        updatables.update(dt)
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.isColliding(asteroid):
                    shot.kill()
                    asteroid.kill()
                    break
            
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game Over")
                return

        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
