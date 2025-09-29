# Mockstroids

A simple starter project using **Pygame**, inspired by the classic Asteroids arcade game.  
This version includes a controllable player ship, asteroid spawning and splitting, shots, collision handling, and a basic scoring system.

---

## 🎮 Features

- **Game Window**
  - Resizable Pygame window at **1280x720** resolution.
  - Main loop runs at **60 FPS**, handling input, updates, collisions, and rendering.

- **Player Ship**
  - Drawn as a triangle but uses a circular hitbox.
  - Controls:
    - `A` / `D` → Rotate left/right
    - `W` / `S` → Move forward/backward
    - `SPACE` → Fire a shot
  - Shooting has a cooldown to prevent spamming.
  - Colliding with an asteroid ends the game.

- **Asteroids**
  - Spawn randomly from the edges of the screen at set intervals.
  - Travel in straight lines with slight random trajectory variation.
  - When destroyed, they **split into two smaller asteroids** (until reaching minimum size).
  - Colliding with the player ends the game.

- **Shots**
  - Fired from the tip of the ship in the direction it faces.
  - Small circles that move at high speed until they hit an asteroid.

- **Scoring**
  - Destroying an asteroid increases the player’s score.
  - Score is displayed in the **top-right corner** of the screen.

---

## 🛠 Requirements

- Python **3.9+** (recommended)
- **Pygame** library

Install Pygame:

```bash
pip install pygame
```

---

## ▶️ Running the Game

Clone or download the repository, then run:

```bash
python main.py
```

If successful, a window titled **Mockstroids** will open at `1280x720`.  
Control your ship, shoot asteroids, and try to survive as long as possible.

---

## 📂 Project Structure

```
.
├── main.py          # Entry point, main game loop
├── constants.py     # Global game settings and values
├── circleshape.py   # Base class for circular game objects
├── asteroid.py      # Asteroid class (movement, splitting, collisions)
├── asteroidfield.py # Handles asteroid spawning from screen edges
├── player.py        # Player ship class (movement, rotation, shooting)
├── shot.py          # Shot (bullet) class
└── README.md        # Project documentation
```

---

## 🚀 Next Steps

Planned improvements and expansions:

- Add **restart/game over screen**.
- Add **lives system** (instead of instant death).
- Add **sound effects** for shooting, explosions, and collisions.
- Implement **background stars or parallax effect**.
- Increase difficulty over time (faster spawn rate, more asteroids).
- Add **high score tracking**.

---

## 📸 Screenshots (Coming Soon)

> Placeholder for gameplay screenshots or GIFs once visuals are finalized.

---

## 📜 License

This project is free to use and modify for learning purposes.  
Feel free to extend it into your own version of Asteroids!
