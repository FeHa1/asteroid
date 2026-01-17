# Asteroid

Classic arcade space shooter built with Python and Pygame. Features OOP design, collision detection, scoring system, and game over mechanics.

https://github.com/user-attachments/assets/880e1b56-a4cf-481f-ac33-8c91d7cc7aba

## Quick Start

```bash
git clone https://github.com/FeHa1/asteroid.git
cd asteroid
pip install -r requirements.txt
python main.py
```

## Controls

**WASD** - Move | **SPACE** - Shoot

## Technical Highlights

- **OOP Architecture**: Base `CircleShape` class with inheritance for Player, Asteroid, Shot
- **Collision Detection**: Circle-to-circle using Euclidean distance (O(1) per check)
- **Delta-Time Movement**: Frame-rate independent physics
- **Sprite Groups**: Clean separation of rendering, updates, and collision logic
- **Scoring System**: Dynamic points based on asteroid size (10/25/50 pts)

### Key Challenges Solved

**Efficient Collisions**: Implemented circle collision detection to handle multiple moving objects without performance issues.

**Frame Independence**: Delta-time based movement ensures consistent gameplay across different hardware.

**State Management**: Clean game loop with proper sprite cleanup and restart logic.

## Structure

```
main.py           # Game loop, scoring, game over
player.py         # Ship controls and shooting
asteroid.py       # Asteroid entity
shot.py           # Projectile mechanics
asteroidfield.py  # Spawning system
circleshape.py    # Base class for circular objects
constants.py      # Configuration
```
