// Main Game Class

class CookieFeanGame {
    constructor() {
        this.canvas = document.getElementById('gameCanvas');
        this.ctx = this.canvas.getContext('2d');
        
        // Game state
        this.score = 0;
        this.combo = 0;
        this.lives = 3;
        this.level = 1;
        this.paused = false;
        this.gameOver = false;
        
        // Game objects
        this.player = new Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100);
        this.cookies = [];
        this.chutes = this.setupChutes();
        this.particles = [];
        
        // Timing
        this.spawnRate = INITIAL_SPAWN_RATE;
        this.spawnTimer = 0;
        this.difficultyTimer = 0;
        this.lastFrameTime = 0;
        
        // Sound manager
        this.soundManager = new SoundManager();
        
        // Input handling
        this.keys = {};
        this.setupInputHandlers();
        
        // Start game loop
        this.startGameLoop();
    }

    setupChutes() {
        const chutes = [];
        CHUTE_POSITIONS.forEach(x => {
            chutes.push(new Chute(x, 50));
        });
        return chutes;
    }

    setupInputHandlers() {
        window.addEventListener('keydown', (e) => {
            this.keys[e.key.toLowerCase()] = true;
            
            if (e.key === ' ') {
                e.preventDefault();
                this.togglePause();
            }
            if (e.key === 'Escape') {
                e.preventDefault();
                if (this.gameOver) {
                    this.reset();
                }
            }
        });

        window.addEventListener('keyup', (e) => {
            this.keys[e.key.toLowerCase()] = false;
        });
    }

    handleInput() {
        if (this.paused || this.gameOver) return;

        if (this.keys['arrowleft'] || this.keys['a']) {
            this.player.moveLeft();
        }
        if (this.keys['arrowright'] || this.keys['d']) {
            this.player.moveRight();
        }
    }

    togglePause() {
        if (this.gameOver) return;
        
        this.paused = !this.paused;
        
        const pauseOverlay = document.getElementById('pauseOverlay');
        if (this.paused) {
            pauseOverlay.classList.add('active');
            this.soundManager.pauseMusic();
        } else {
            pauseOverlay.classList.remove('active');
            this.soundManager.resumeMusic();
        }
    }

    spawnCookies() {
        this.spawnTimer++;
        if (this.spawnTimer >= this.spawnRate) {
            const randomChute = this.chutes[Math.floor(Math.random() * this.chutes.length)];
            const newCookie = new Cookie(randomChute.x, randomChute.y + CHUTE_HEIGHT);
            this.cookies.push(newCookie);
            this.spawnTimer = 0;
        }
    }

    update() {
        if (this.paused || this.gameOver) return;

        this.handleInput();
        
        // Spawn new cookies
        this.spawnCookies();
        
        // Update player
        this.player.update();
        
        // Update cookies
        for (let i = this.cookies.length - 1; i >= 0; i--) {
            const cookie = this.cookies[i];
            cookie.update();
            
            // Check collision with player
            if (this.checkCollision(cookie, this.player)) {
                this.cookies.splice(i, 1);
                this.score += POINTS_PER_COOKIE;
                this.combo++;
                
                // Bonus for combo
                if (this.combo > 1) {
                    this.score += COMBO_BONUS * (this.combo - 1);
                }
                
                // Play catch sound and create particles
                this.soundManager.playCatchSound();
                this.createCatchParticles(cookie.x, cookie.y);
                
                // Update UI
                this.updateUI();
            }
            // Check if cookie fell off screen
            else if (cookie.y > SCREEN_HEIGHT) {
                this.cookies.splice(i, 1);
                this.combo = 0;
                this.lives--;
                
                this.soundManager.playMissSound();
                this.updateUI();
                
                if (this.lives <= 0) {
                    this.endGame();
                }
            }
        }
        
        // Update particles
        for (let i = this.particles.length - 1; i >= 0; i--) {
            this.particles[i].update();
            if (!this.particles[i].isAlive()) {
                this.particles.splice(i, 1);
            }
        }
        
        // Increase difficulty over time
        this.difficultyTimer++;
        if (this.difficultyTimer >= DIFFICULTY_INCREASE_INTERVAL) {
            this.increaseDifficulty();
            this.difficultyTimer = 0;
        }
    }

    checkCollision(cookie, player) {
        const cookieRect = cookie.getCollisionRect();
        const playerRect = player.getCollisionRect();
        return checkCollision(cookieRect, playerRect);
    }

    increaseDifficulty() {
        if (this.spawnRate > MIN_SPAWN_RATE) {
            this.spawnRate = Math.max(this.spawnRate - 2, MIN_SPAWN_RATE);
        }
        this.level++;
        this.soundManager.playLevelUpSound();
        this.updateUI();
    }

    createCatchParticles(x, y) {
        for (let i = 0; i < 8; i++) {
            const angle = (Math.PI * 2 / 8) * i;
            const vx = Math.cos(angle) * 5;
            const vy = Math.sin(angle) * 5;
            
            this.particles.push(
                new Particle(x, y, vx, vy, 30, COLORS.YELLOW)
            );
        }
    }

    updateUI() {
        document.getElementById('score').textContent = this.score;
        document.getElementById('lives').textContent = this.lives;
        document.getElementById('level').textContent = this.level;
        
        const comboDisplay = document.getElementById('comboDisplay');
        if (this.combo > 1) {
            comboDisplay.style.display = 'block';
            document.getElementById('combo').textContent = this.combo;
        } else {
            comboDisplay.style.display = 'none';
        }
    }

    endGame() {
        this.gameOver = true;
        this.soundManager.playGameOverSound();
        
        document.getElementById('finalScore').textContent = this.score;
        document.getElementById('finalLevel').textContent = this.level;
        document.getElementById('gameOverOverlay').classList.add('active');
        
        // Allow restart with space
        window.addEventListener('keydown', (e) => {
            if (e.key === ' ' && this.gameOver) {
                e.preventDefault();
                this.reset();
            }
        });
    }

    reset() {
        // Reset game state
        this.score = 0;
        this.combo = 0;
        this.lives = 3;
        this.level = 1;
        this.paused = false;
        this.gameOver = false;
        this.spawnRate = INITIAL_SPAWN_RATE;
        this.spawnTimer = 0;
        this.difficultyTimer = 0;
        
        // Clear game objects
        this.player = new Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100);
        this.cookies = [];
        this.particles = [];
        
        // Hide overlays
        document.getElementById('pauseOverlay').classList.remove('active');
        document.getElementById('gameOverOverlay').classList.remove('active');
        
        // Resume music
        this.soundManager.playBackgroundMusic();
        
        // Update UI
        this.updateUI();
    }

    draw() {
        // Clear canvas
        this.ctx.fillStyle = COLORS.BACKGROUND;
        this.ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
        
        // Draw chutes
        this.chutes.forEach(chute => chute.draw(this.ctx));
        
        // Draw cookies
        this.cookies.forEach(cookie => cookie.draw(this.ctx));
        
        // Draw particles
        this.particles.forEach(particle => particle.draw(this.ctx));
        
        // Draw player
        this.player.draw(this.ctx);
        
        // Draw grid lines for chutes (optional visual guide)
        this.drawChuteGuides();
    }

    drawChuteGuides() {
        this.ctx.strokeStyle = 'rgba(0, 255, 255, 0.1)';
        this.ctx.lineWidth = 1;
        this.ctx.setLineDash([5, 5]);
        
        this.chutes.forEach(chute => {
            this.ctx.beginPath();
            this.ctx.moveTo(chute.x, chute.y + CHUTE_HEIGHT);
            this.ctx.lineTo(chute.x, SCREEN_HEIGHT);
            this.ctx.stroke();
        });
        
        this.ctx.setLineDash([]);
    }

    startGameLoop() {
        const gameLoop = (timestamp) => {
            if (this.lastFrameTime === 0) this.lastFrameTime = timestamp;
            
            const deltaTime = timestamp - this.lastFrameTime;
            
            if (deltaTime >= FRAME_TIME) {
                this.update();
                this.draw();
                this.lastFrameTime = timestamp - (deltaTime % FRAME_TIME);
            }
            
            requestAnimationFrame(gameLoop);
        };
        
        requestAnimationFrame(gameLoop);
    }
}

// Sound Manager Class
class SoundManager {
    constructor() {
        this.backgroundMusic = this.createAudio(AUDIO_PATHS.backgroundMusic);
        this.catchSound = this.createAudio(AUDIO_PATHS.catchSound);
        this.gameOverSound = this.createAudio(AUDIO_PATHS.gameOverSound);
        this.missSound = this.createAudio(AUDIO_PATHS.missSound);
        this.levelUpSound = this.createAudio(AUDIO_PATHS.levelUpSound);
        
        this.enabled = true;
        this.volume = 0.7;
    }

    createAudio(src) {
        const audio = new Audio();
        audio.src = src;
        audio.onerror = () => {
            console.log(`Could not load audio: ${src}`);
        };
        return audio;
    }

    playBackgroundMusic() {
        if (!this.enabled) return;
        try {
            this.backgroundMusic.loop = true;
            this.backgroundMusic.volume = this.volume * 0.5;
            this.backgroundMusic.play().catch(e => {
                console.log('Could not play background music:', e);
            });
        } catch (e) {
            console.log('Error playing background music:', e);
        }
    }

    pauseMusic() {
        try {
            this.backgroundMusic.pause();
        } catch (e) {
            console.log('Error pausing music:', e);
        }
    }

    resumeMusic() {
        try {
            this.backgroundMusic.play().catch(e => {
                console.log('Could not resume music:', e);
            });
        } catch (e) {
            console.log('Error resuming music:', e);
        }
    }

    playCatchSound() {
        if (!this.enabled) return;
        try {
            this.catchSound.currentTime = 0;
            this.catchSound.volume = this.volume;
            this.catchSound.play().catch(e => {
                console.log('Could not play catch sound:', e);
            });
        } catch (e) {
            console.log('Error playing catch sound:', e);
        }
    }

    playMissSound() {
        if (!this.enabled) return;
        try {
            this.missSound.currentTime = 0;
            this.missSound.volume = this.volume;
            this.missSound.play().catch(e => {
                // Sound file might not exist
            });
        } catch (e) {
            // Silently fail for optional sounds
        }
    }

    playGameOverSound() {
        if (!this.enabled) return;
        try {
            this.backgroundMusic.pause();
            this.gameOverSound.currentTime = 0;
            this.gameOverSound.volume = this.volume;
            this.gameOverSound.play().catch(e => {
                console.log('Could not play game over sound:', e);
            });
        } catch (e) {
            console.log('Error playing game over sound:', e);
        }
    }

    playLevelUpSound() {
        if (!this.enabled) return;
        try {
            this.levelUpSound.currentTime = 0;
            this.levelUpSound.volume = this.volume * 0.7;
            this.levelUpSound.play().catch(e => {
                // Optional sound, fail silently
            });
        } catch (e) {
            // Silently fail for optional sounds
        }
    }

    setVolume(level) {
        this.volume = Math.max(0, Math.min(1, level));
        if (this.backgroundMusic) {
            this.backgroundMusic.volume = this.volume * 0.5;
        }
    }

    toggleSound() {
        this.enabled = !this.enabled;
    }
}

// Initialize game when page loads
window.addEventListener('DOMContentLoaded', () => {
    const game = new CookieFeanGame();
    game.soundManager.playBackgroundMusic();
    game.updateUI();
});
