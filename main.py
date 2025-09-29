import pygame
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from constants import *  # noqa: F403


def main():
    # Initialize player score
    player_score = 0

    # Startup message and screen setup
    print(f"Starting Mockstroids — {SCREEN_WIDTH}x{SCREEN_HEIGHT}")  # noqa: F405
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize font system (for score display)
    pygame.font.init()
    font = pygame.font.Font(None, 28)  # default font, size 28

    # Sprite groups for managing game objects
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign static containers so new objects auto-register in groups
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = updatables
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)

    # Create player in center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # noqa: F405

    # Start asteroid spawning system
    AsteroidField()

    # Game clock for frame timing
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear screen to black
        screen.fill("black")

        # Tick clock: ensures 60 FPS, converts ms to seconds
        dt = clock.tick(60) / 1000

        # Update all game objects
        updatables.update(dt)

        # Collision: shots vs asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.isColliding(asteroid):
                    shot.kill()  # remove shot
                    player_score += 1  # increase score
                    asteroid.split()  # break asteroid into pieces
                    break  # stop checking this shot

        # Collision: asteroids vs player
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game Over")
                return

        # Draw all objects
        for drawable in drawables:
            drawable.draw(screen)

        # Draw score at top-right
        score_surf = font.render(f"Score: {player_score}", True, "white")
        score_rect = score_surf.get_rect(topright=(SCREEN_WIDTH - 10, 10))  # noqa: F405
        screen.blit(score_surf, score_rect)

        # Flip display buffer (show frame)
        pygame.display.flip()


# Run the game when script is executed
if __name__ == "__main__":
    main()
