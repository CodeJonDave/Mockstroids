import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_MOVE_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    # Static reference to sprite groups this class belongs to
    containers = None
    # Timer to enforce shooting cooldown
    shot_timer = 0

    def __init__(self, x, y):
        # Initialize CircleShape with position and hitbox radius
        super().__init__(x, y, PLAYER_RADIUS)
        # Player’s facing direction (in degrees)
        self.rotation = 0

    def triangle(self):
        """Return the 3 points of the player ship’s triangle shape."""
        forward = pygame.Vector2(0, -1).rotate(
            self.rotation
        )  # direction the ship is facing
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )  # sideways vector

        # Three corners of the triangle ship
        a = self.position + forward * self.radius  # tip of the ship
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player ship as a triangle outline."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """Rotate the ship by turn speed scaled with delta time."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Move the ship forward/backward relative to its rotation."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def update(self, dt):
        """Handle movement, rotation, shooting, and cooldowns each frame."""
        # Countdown shooting cooldown
        if self.shot_timer > 0:
            self.shot_timer -= dt

        # Keyboard input
        keys = pygame.key.get_pressed()

        # Rotate left (A) or right (D)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)

        # Move forward (W) or backward (S)
        if keys[pygame.K_w]:
            self.move(-dt)
        elif keys[pygame.K_s]:
            self.move(dt)

        # Fire shot if SPACE is pressed
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        """Create a new shot at the ship’s tip if cooldown allows."""
        if self.shot_timer > 0:
            return  # still cooling down

        # Direction of shot
        forward = pygame.Vector2(0, -1).rotate(self.rotation)

        # Tip of the ship (where the bullet spawns)
        tip = self.position + forward * self.radius

        # Create shot sprite
        shot = Shot(tip.x, tip.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

        # Reset cooldown timer
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
