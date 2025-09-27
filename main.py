import pygame
from player import Player
from constants import *  # noqa: F403


def main():
    print(f"Starting Mockstroids — {SCREEN_WIDTH}x{SCREEN_HEIGHT}")  # noqa: F405
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # noqa: F405
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # noqa: F841


if __name__ == "__main__":
    main()
