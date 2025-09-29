import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # If the class has a "containers" attribute, register this sprite in those groups
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            # Otherwise, just initialize as a plain sprite with no groups
            super().__init__()

        # Center position of the circle (uses floating point for smooth movement)
        self.position = pygame.Vector2(x, y)

        # Velocity vector (how much the object moves each frame)
        self.velocity = pygame.Vector2(0, 0)

        # Radius of the circle (for drawing and collision detection)
        self.radius = radius

    def draw(self, screen):
        # Subclasses should override this to render themselves on the screen
        pass

    def update(self, dt):
        # Subclasses should override this to update their state each frame
        # dt = "delta time" (time in seconds since the last frame)
        pass

    def isColliding(self, other):
        # Two circles collide if the distance between their centers
        # is less than or equal to the sum of their radii
        return self.position.distance_to(other.position) <= (self.radius + other.radius)
