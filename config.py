"""
Game configuration file for easy customization
This file allows you to tweak game settings without modifying constants.py
"""

# DIFFICULTY SETTINGS
DIFFICULTY_PRESET = "normal"  # Options: "easy", "normal", "hard", "custom"

# If using "custom", define your own settings below:
CUSTOM_DIFFICULTY = {
    "initial_spawn_rate": 40,      # Frames between cookie spawns (lower = harder)
    "min_spawn_rate": 15,          # Minimum spawn rate (hard difficulty cap)
    "difficulty_increase_interval": 300,  # Frames before difficulty increases
    "gravity": 0.3,                # Gravity acceleration
    "max_cookie_velocity": 12,     # Terminal velocity for cookies
}

# DIFFICULTY PRESETS
DIFFICULTY_PRESETS = {
    "easy": {
        "initial_spawn_rate": 60,
        "min_spawn_rate": 25,
        "difficulty_increase_interval": 500,
        "gravity": 0.2,
        "max_cookie_velocity": 8,
        "player_speed": 10,
    },
    "normal": {
        "initial_spawn_rate": 40,
        "min_spawn_rate": 15,
        "difficulty_increase_interval": 300,
        "gravity": 0.3,
        "max_cookie_velocity": 12,
        "player_speed": 8,
    },
    "hard": {
        "initial_spawn_rate": 25,
        "min_spawn_rate": 8,
        "difficulty_increase_interval": 200,
        "gravity": 0.5,
        "max_cookie_velocity": 15,
        "player_speed": 6,
    },
}

# PLAYER SETTINGS
PLAYER_SETTINGS = {
    "width_ratio": 0.167,  # 1/6 of screen width
    "height_ratio": 0.25,  # 1/4 of screen height
    "speed": 8,
}

# SCORING SETTINGS
SCORING = {
    "points_per_cookie": 10,
    "combo_bonus_multiplier": 5,  # Bonus per combo level
    "combo_threshold": 5,          # Combo count for milestone sounds
}

# DISPLAY SETTINGS
DISPLAY = {
    "width": 1200,
    "height": 800,
    "fps": 60,
    "fullscreen": False,
    "vsync": True,
}

# AUDIO SETTINGS
AUDIO = {
    "master_volume": 0.7,
    "music_volume": 0.35,      # Background music volume (relative to master)
    "sfx_volume": 1.0,         # Sound effects volume (relative to master)
    "enable_music": True,
    "enable_sfx": True,
}

# COLOR SCHEME (RGB tuples)
COLORS = {
    "background": (30, 30, 40),
    "player": (0, 51, 153),      # Dark blue for FEAN
    "player_skin": (205, 133, 63),
    "cookie": (184, 115, 51),
    "chip": (101, 67, 33),
    "chute": (100, 100, 100),
    "chute_opening": (50, 50, 50),
    "basket": (200, 100, 50),
}

# GAME RULES
GAME_RULES = {
    "starting_lives": 3,
    "max_combo_display": True,
    "reset_combo_on_miss": True,
    "pause_enabled": True,
}

# ASSET PATHS
ASSET_PATHS = {
    "audio": {
        "background_music": "assets/audio/background_music.mp3",
        "catch_sound": "assets/audio/catch.wav",
        "game_over_sound": "assets/audio/game_over.wav",
        "miss_sound": "assets/audio/miss.wav",
        "combo_sound": "assets/audio/combo.wav",
        "level_up_sound": "assets/audio/level_up.wav",
    },
    "images": {
        "player": "assets/images/fean.png",
        "cookie": "assets/images/cookie.png",
        "chute": "assets/images/chute.png",
    }
}

# FEATURE FLAGS (Enable/disable experimental features)
FEATURES = {
    "particle_effects": False,     # Enable particle effects on catch
    "visual_feedback": True,       # Screen shake, color effects
    "power_ups": False,            # Special items to collect
    "obstacles": False,            # Bad cookies, fast cookies, etc.
    "high_scores": False,          # Save/load high scores
    "touch_controls": False,       # Mobile touch support
}

# POWER-UP SETTINGS (if enabled)
POWERUPS = {
    "slow_motion": {
        "duration": 300,           # Frames
        "speed_multiplier": 0.5,   # 50% of normal speed
        "spawn_rate": 0.02,        # 2% chance per spawn
    },
    "magnet": {
        "duration": 200,
        "attraction_radius": 150,
        "spawn_rate": 0.015,
    },
    "shield": {
        "duration": 400,
        "spawn_rate": 0.01,
    },
    "score_boost": {
        "duration": 300,
        "multiplier": 2.0,         # 2x points
        "spawn_rate": 0.015,
    },
}

# DEBUG SETTINGS
DEBUG = {
    "show_fps": False,
    "show_collision_boxes": False,
    "show_spawn_points": False,
    "infinite_lives": False,
    "auto_catch": False,           # Automatically catch all cookies
}


def get_difficulty_settings(preset=None):
    """
    Get difficulty settings based on preset or custom config
    
    Args:
        preset: Difficulty preset name (overrides DIFFICULTY_PRESET)
    
    Returns:
        Dictionary of difficulty settings
    """
    if preset is None:
        preset = DIFFICULTY_PRESET
    
    if preset == "custom":
        return CUSTOM_DIFFICULTY
    elif preset in DIFFICULTY_PRESETS:
        return DIFFICULTY_PRESETS[preset]
    else:
        print(f"Unknown difficulty preset: {preset}. Using 'normal'")
        return DIFFICULTY_PRESETS["normal"]


def get_game_config():
    """
    Get complete game configuration
    
    Returns:
        Dictionary with all game settings merged
    """
    difficulty = get_difficulty_settings()
    
    config = {
        "difficulty": difficulty,
        "player": PLAYER_SETTINGS,
        "scoring": SCORING,
        "display": DISPLAY,
        "audio": AUDIO,
        "colors": COLORS,
        "rules": GAME_RULES,
        "assets": ASSET_PATHS,
        "features": FEATURES,
        "debug": DEBUG,
    }
    
    return config
