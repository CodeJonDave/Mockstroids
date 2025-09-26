import pygame
from constants import *  # noqa: F403


def main():
    print(f"Starting Asteroids — {SCREEN_WIDTH}x{SCREEN_HEIGHT}")  # noqa: F405

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
