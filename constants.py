# Screen dimensions (in pixels)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Asteroid settings
ASTEROID_MIN_RADIUS = 20  # Smallest asteroid radius
ASTEROID_KINDS = 3  # Number of asteroid size categories
ASTEROID_SPAWN_RATE = 0.8  # How often asteroids spawn (seconds between spawns)
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Largest asteroid radius

# Shot (bullet) settings
SHOT_RADIUS = 5  # Radius of each shot
PLAYER_SHOOT_SPEED = 500  # Speed of shots (pixels per second)
PLAYER_SHOOT_COOLDOWN = 0.3  # Minimum time between shots (in seconds)

# Player (ship) settings
PLAYER_RADIUS = 20  # Radius of the player’s hitbox
PLAYER_TURN_SPEED = 300  # Rotation speed (degrees per second)
PLAYER_MOVE_SPEED = 200  # Forward movement speed (pixels per second)
