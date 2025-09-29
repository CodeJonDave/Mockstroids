import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    # Groups this sprite should be added to (set externally in main.py)
    containers = None

    def __init__(self, x, y):
        # Initialize as a circle at (x, y) with fixed shot radius
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """Render the shot as a small white circle outline."""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Move the shot forward each frame according to velocity and delta time."""
        self.position += self.velocity * dt
