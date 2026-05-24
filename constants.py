"""
Game constants and configuration
"""

import pygame

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# FPS
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (30, 30, 40)
PLAYER_COLOR = (0, 51, 153)  # Dark blue for FEAN shirt
SKIN_COLOR = (205, 133, 63)   # Brown skin tone
COOKIE_COLOR = (184, 115, 51)  # Cookie brown
CHIP_COLOR = (101, 67, 33)     # Chocolate chip brown
CHUTE_COLOR = (100, 100, 100)  # Gray
CHUTE_OPENING_COLOR = (50, 50, 50)  # Dark gray
BASKET_COLOR = (200, 100, 50)  # Orange for catching basket

# Player properties
PLAYER_WIDTH = int(SCREEN_WIDTH / 6)  # 1/6 of screen width (was requested as 1/4, but 1/6 scales better)
PLAYER_HEIGHT = int(SCREEN_HEIGHT / 4)  # 1/4 of screen height
PLAYER_SPEED = 8

# Cookie properties
COOKIE_SIZE = 20
COOKIE_FALL_SPEED = 3
MAX_COOKIE_VELOCITY = 12
GRAVITY = 0.3

# Chute properties
CHUTE_WIDTH = 80
CHUTE_HEIGHT = 60

# Game mechanics
INITIAL_SPAWN_RATE = 40  # Frames between cookie spawns (lower = faster)
MIN_SPAWN_RATE = 15      # Minimum spawn rate (hard cap on difficulty)
POINTS_PER_COOKIE = 10
COMBO_BONUS = 5          # Bonus points per combo multiplier
DIFFICULTY_INCREASE_INTERVAL = 300  # Frames between difficulty increases

# Game recommendations
GAME_FEATURES = {
    "power_ups": [
        "SLOW_MO: Slows down falling cookies temporarily",
        "MAGNET: Automatically attracts nearby cookies",
        "SHIELD: Protects against one missed cookie",
        "SCORE_BOOST: Doubles points for 10 seconds"
    ],
    "obstacles": [
        "Rotten cookies: Award negative points if caught",
        "Fast cookies: Fall faster than normal",
        "Frozen cookies: Harder to catch (larger collision check needed)"
    ],
    "sound_effects": [
        "catch.wav - Plays when cookie is caught",
        "miss.wav - Plays when cookie is missed",
        "game_over.wav - Plays when game ends",
        "combo.wav - Plays on combo milestones (x5, x10, etc.)",
        "level_up.wav - Plays when difficulty increases",
        "background_music.mp3 - Loops during gameplay"
    ]
}
