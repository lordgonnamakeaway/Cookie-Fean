// Game Constants and Configuration

const SCREEN_WIDTH = 1200;
const SCREEN_HEIGHT = 800;
const FPS = 60;
const FRAME_TIME = 1000 / FPS;

// Colors (RGB)
const COLORS = {
    BACKGROUND: '#1e1e28',
    PLAYER: '#003399',
    SKIN: '#cd853f',
    COOKIE: '#b87333',
    CHIP: '#654321',
    CHUTE: '#646464',
    CHUTE_OPENING: '#323232',
    BASKET: '#c86432',
    WHITE: '#ffffff',
    BLACK: '#000000',
    YELLOW: '#ffff00',
    RED: '#ff0000',
    GREEN: '#00ff00',
    CYAN: '#00ffff'
};

// Player properties
const PLAYER_WIDTH = SCREEN_WIDTH / 6;
const PLAYER_HEIGHT = SCREEN_HEIGHT / 4;
const PLAYER_SPEED = 8;

// Cookie properties
const COOKIE_SIZE = 20;
const COOKIE_FALL_SPEED = 3;
const MAX_COOKIE_VELOCITY = 12;
const GRAVITY = 0.3;

// Chute properties
const CHUTE_WIDTH = 80;
const CHUTE_HEIGHT = 60;
const CHUTE_POSITIONS = [
    SCREEN_WIDTH / 6,
    SCREEN_WIDTH / 2,
    (5 * SCREEN_WIDTH) / 6
];

// Game mechanics
const INITIAL_SPAWN_RATE = 40;
const MIN_SPAWN_RATE = 15;
const POINTS_PER_COOKIE = 10;
const COMBO_BONUS = 5;
const DIFFICULTY_INCREASE_INTERVAL = 300;

// Audio file paths
const AUDIO_PATHS = {
    backgroundMusic: 'assets/audio/background_music.mp3',
    catchSound: 'assets/audio/catch.wav',
    missSound: 'assets/audio/miss.wav',
    gameOverSound: 'assets/audio/game_over.wav',
    levelUpSound: 'assets/audio/level_up.wav'
};

// Difficulty presets
const DIFFICULTY_PRESETS = {
    easy: {
        initialSpawnRate: 60,
        minSpawnRate: 25,
        gravity: 0.2,
        maxVelocity: 8
    },
    normal: {
        initialSpawnRate: 40,
        minSpawnRate: 15,
        gravity: 0.3,
        maxVelocity: 12
    },
    hard: {
        initialSpawnRate: 25,
        minSpawnRate: 8,
        gravity: 0.5,
        maxVelocity: 15
    }
};
