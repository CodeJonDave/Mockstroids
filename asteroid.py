
import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        pos = self.position
        vel = self.velocity
        r = self.radius
        self.kill()
        if r <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        a1 = Asteroid(pos.x,pos.y,r - ASTEROID_MIN_RADIUS)
        a2 = Asteroid(pos.x,pos.y,r - ASTEROID_MIN_RADIUS)
        a1.velocity = vel.rotate(angle) * 1.2
        a2.velocity = vel.rotate(-angle) * 1.2
        
