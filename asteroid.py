import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    # Static reference to sprite groups this class should be added to
    containers = None

    def __init__(self, x, y, radius):
        # Call parent (CircleShape) constructor to set position, velocity, radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a white circle with an outline thickness of 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move asteroid according to velocity and delta time (dt = seconds since last frame)
        self.position += self.velocity * dt
        
    def split(self):
        # Store current state before destroying the asteroid
        pos = self.position
        vel = self.velocity
        r = self.radius

        # Remove this asteroid from all sprite groups
        self.kill()

        # If asteroid is already at the minimum radius, don’t split further
        if r <= ASTEROID_MIN_RADIUS:
            return

        # Pick a random angle between 20 and 50 degrees for splitting trajectory
        angle = random.uniform(20, 50)

        # Create two smaller asteroids at the same position
        a1 = Asteroid(pos.x, pos.y, r - ASTEROID_MIN_RADIUS)
        a2 = Asteroid(pos.x, pos.y, r - ASTEROID_MIN_RADIUS)

        # Give them new velocities by rotating the old one in opposite directions
        # and slightly increasing speed (×1.2 multiplier)
        a1.velocity = vel.rotate(angle) * 1.2
        a2.velocity = vel.rotate(-angle) * 1.2
