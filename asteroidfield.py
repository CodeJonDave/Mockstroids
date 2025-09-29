import pygame
import random
from asteroid import Asteroid
from constants import *  # noqa: F403


class AsteroidField(pygame.sprite.Sprite):
    # Possible spawn edges: each entry is [direction_vector, position_function]
    # - direction_vector: base movement direction for asteroids
    # - position_function: returns a spawn position along that edge
    edges = [
        # Spawn on the left edge, moving right
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),  # noqa: F405
        ],
        # Spawn on the right edge, moving left
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS,  # noqa: F405
                y * SCREEN_HEIGHT,  # noqa: F405
            ),
        ],
        # Spawn on the top edge, moving down
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),  # noqa: F405
        ],
        # Spawn on the bottom edge, moving up
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH,  # noqa: F405
                SCREEN_HEIGHT + ASTEROID_MAX_RADIUS,  # noqa: F405
            ),
        ],
    ]

    # Groups to which this sprite belongs (set externally in main.py)
    containers = None

    def __init__(self):
        # Register this object in the provided sprite groups
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Tracks elapsed time until the next spawn
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """Create a new asteroid with given radius, position, and velocity."""
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """Update the spawn timer and spawn new asteroids when ready."""
        self.spawn_timer += dt

        # If enough time has passed, spawn a new asteroid
        if self.spawn_timer > ASTEROID_SPAWN_RATE:  # noqa: F405
            self.spawn_timer = 0

            # Choose a random edge (direction + spawn position)
            edge = random.choice(self.edges)

            # Base speed between 40 and 100 px/s
            speed = random.randint(40, 100)

            # Velocity: base direction, rotated by up to ±30 degrees
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))

            # Position: use the edge’s position function (x or y between 0–1)
            position = edge[1](random.uniform(0, 1))

            # Kind determines asteroid size (1 = small, 2 = medium, 3 = large)
            kind = random.randint(1, ASTEROID_KINDS)  # noqa: F405

            # Spawn asteroid with radius based on kind
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)  # noqa: F405
