Mockstroids

A simple starter project using Pygame, inspired by classic asteroid-style arcade games. This version sets up a resizable game window and prepares constants for asteroid behavior.

Features

Initializes a Pygame window (1280x720 resolution).

Runs a basic game loop that handles quit events.

Defines constants for asteroid properties:

Minimum radius (20)

Number of asteroid kinds (3)

Spawn rate (0.8)

Maximum radius (calculated from minimum × kinds).

Requirements

Python 3.9+ (recommended)

Pygame

Install Pygame:

pip install pygame

Running the Game

Clone or download the repo, then run:

python main.py


If successful, a black game window titled Mockstroids will appear at 1280x720.

Project Structure
.
├── main.py          # Entry point, contains game loop
├── constants.py     # Game configuration values
└── README.md        # Project documentation

Next Steps

Add asteroid spawning logic using the constants.

Implement ship controls and shooting mechanics.

Expand event handling for player input.