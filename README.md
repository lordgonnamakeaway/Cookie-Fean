````markdown name=README.md url=https://github.com/lordgonnamakeaway/Cookie-Fean/blob/main/README.md
# Cookie Fean - A 2D Cookie Catching Game

A fun arcade-style game where the Fean character catches randomly falling cookies from three chutes above!

## Game Overview

**Cookie Fean** is a 2D game built with Python and Pygame where you control the Fean character to catch falling cookies. The game gets progressively harder as you advance through levels, with increasing spawn rates and faster-falling cookies.

### Features

- **Player Control**: Move left and right using arrow keys or A/D to position Fean under the falling cookies
- **Three Cookie Chutes**: Cookies fall randomly from three chutes positioned across the top of the screen
- **Combo System**: Build combos by catching consecutive cookies for bonus points
- **Progressive Difficulty**: Game difficulty increases over time with faster cookie spawn rates
- **Score Tracking**: Track your score, combo multiplier, lives remaining, and current level
- **Sound System**: Catch sounds, background music, and game over audio (audio files required)
- **Pause Functionality**: Press SPACE to pause/resume the game
- **Game Over Screen**: Shows final score and level reached with restart option

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/lordgonnamakeaway/Cookie-Fean.git
cd Cookie-Fean
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Create the assets directory structure:
```bash
mkdir -p assets/audio
mkdir -p assets/images
```

## Running the Game

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** or **A/D** | Move left/right |
| **SPACE** | Pause/Resume |
| **ESC** | Quit game |

## Game Mechanics

### Scoring
- **Cookie Catch**: +10 points per cookie
- **Combo Bonus**: +5 points × (combo count - 1)
  - Example: Catching 5 cookies in a row = 10 + 10 + 15 + 20 + 25 = 80 points
- **Missed Cookie**: Lose 1 life and reset combo

### Difficulty Progression
- Cookies spawn faster as you progress
- Game level increases automatically
- Initial spawn rate: Every 40 frames
- Minimum spawn rate: Every 15 frames (hard cap)
- Difficulty increases every 300 frames of gameplay

### Lives System
- Start with 3 lives
- Lose 1 life each time a cookie falls off screen without being caught
- Game over when lives reach 0

## Audio Files (Required)

You'll need to add the following audio files to `assets/audio/`:

1. **background_music.mp3** - Background loop music
2. **catch.wav** - Sound when cookie is caught
3. **game_over.wav** - Sound when game ends
4. **miss.wav** (optional) - Sound when cookie is missed
5. **combo.wav** (optional) - Sound for combo milestones
6. **level_up.wav** (optional) - Sound when difficulty increases

### Audio Recommendations

- **Background Music**: Upbeat, looping track (2-4 minutes recommended)
- **Catch Sound**: Short, satisfying "ding" or "pop" sound (100-300ms)
- **Game Over Sound**: Dramatic or funny sound (1-2 seconds)
- **Combo Sound**: Ascending tone or cheering sound (short)

> **Note**: The game will work without audio files, but will print warnings to console when trying to play missing sounds.

## Customization

### Game Constants

Edit `constants.py` to customize:

- **Screen dimensions**: `SCREEN_WIDTH`, `SCREEN_HEIGHT`
- **Player size**: `PLAYER_WIDTH`, `PLAYER_HEIGHT`
- **Player speed**: `PLAYER_SPEED`
- **Cookie size and fall speed**: `COOKIE_SIZE`, `COOKIE_FALL_SPEED`
- **Difficulty settings**: `INITIAL_SPAWN_RATE`, `MIN_SPAWN_RATE`, `DIFFICULTY_INCREASE_INTERVAL`
- **Points**: `POINTS_PER_COOKIE`, `COMBO_BONUS`
- **Colors**: Modify color tuples for custom theming

### Example Customization

To make the game easier:
```python
INITIAL_SPAWN_RATE = 60  # Slower initial spawn
MIN_SPAWN_RATE = 25      # Higher minimum spawn rate
PLAYER_SPEED = 12        # Faster player movement
```

To make the game harder:
```python
INITIAL_SPAWN_RATE = 30  # Faster spawn
MIN_SPAWN_RATE = 10      # Lower minimum
GRAVITY = 0.5            # Faster acceleration
```

## Recommended Features to Add

### Power-ups
- **SLOW_MO**: Temporarily slows falling cookies
- **MAGNET**: Automatically attracts nearby cookies
- **SHIELD**: Protects against one missed cookie
- **SCORE_BOOST**: Doubles points for 10 seconds

### Obstacles
- **Rotten Cookies**: Award negative points or lose a life if caught
- **Fast Cookies**: Fall faster than normal cookies
- **Frozen Cookies**: Require multiple catches or special handling

### Additional Enhancements
- High score leaderboard/saving
- Visual effects and particles for catching
- Different player skins/characters
- Cookie varieties with different point values
- Boss levels with special patterns
- Tutorial/How to Play screen
- Settings menu (volume control, difficulty presets)
- Mobile touch controls support

## Project Structure

```
Cookie-Fean/
├── main.py          # Entry point for the game
├── game.py          # Main game logic, game loop, sound management
├── entities.py      # Game objects (Player, Cookie, Chute, Particle)
├── constants.py     # Game configuration and constants
├── README.md        # This file
└── assets/
    ├── audio/       # Audio files (to be added)
    │   ├── background_music.mp3
    │   ├── catch.wav
    │   └── game_over.wav
    └── images/      # Image sprites (to be added)
        ├── fean.png
        ├── cookie.png
        └── chute.png
```

## Game Classes

### CookieFeanGame
Main game class that handles:
- Game initialization
- Event handling
- Game loop (update/draw)
- Collision detection
- Difficulty progression
- Game state management

### SoundManager
Handles all audio:
- Background music playback
- Sound effect triggering
- Volume control

### Player
Represents the Fean character:
- Position and movement
- Boundary checking
- Drawing player sprite

### Cookie
Represents falling cookies:
- Physics (velocity, acceleration)
- Rotation animation
- Drawing with chip pattern

### Chute
Represents cookie dispensers:
- Drawing chute graphics
- Spawning location for cookies

### Particle
Optional particle effects for visual polish

## Troubleshooting

### Game won't start
- Ensure Python 3.8+ is installed: `python --version`
- Check pygame is installed: `pip install pygame`

### No sound playing
- Verify audio files exist in `assets/audio/`
- Check file formats match expectations (mp3/wav)
- Ensure system audio is not muted

### Game runs slowly
- Close other applications
- Reduce FPS or window resolution
- Check CPU usage

### Player movement feels sluggish
- Increase `PLAYER_SPEED` in `constants.py`
- Adjust velocity friction in `entities.py` Player.update()

## Future Roadmap

- [ ] Sprite-based graphics replacing placeholder shapes
- [ ] Particle effects for cookie catches
- [ ] Mobile touch controls
- [ ] High score persistence
- [ ] Multiple difficulty levels
- [ ] Special cookie types and power-ups
- [ ] Leaderboard system
- [ ] Settings/Options menu
- [ ] Pause menu with volume control

## License

This project is open source and available under the MIT License.

## Credits

- Game Design & Development: lordgonnamakeaway
- Character: The Fean
- Built with: Python, Pygame

---

**Enjoy playing Cookie Fean! 🍪**
````
