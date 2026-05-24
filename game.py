"""
Main game module for Cookie Fean
"""

import pygame
import random
import math
from entities import Player, Cookie, Chute
from constants import *

class CookieFeanGame:
    def __init__(self):
        """Initialize the game"""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cookie Fean")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        
        # Game state
        self.score = 0
        self.combo = 0
        self.lives = 3
        self.level = 1
        
        # Initialize game objects
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.cookies = []
        self.chutes = self.setup_chutes()
        
        # Timing
        self.spawn_rate = INITIAL_SPAWN_RATE
        self.spawn_timer = 0
        self.difficulty_timer = 0
        
        # Sound system
        self.sound_manager = SoundManager()
        self.sound_manager.play_background_music()
        
    def setup_chutes(self):
        """Create the three cookie chutes at the top"""
        chutes = [
            Chute(SCREEN_WIDTH // 6, 50),
            Chute(SCREEN_WIDTH // 2, 50),
            Chute(5 * SCREEN_WIDTH // 6, 50)
        ]
        return chutes
    
    def handle_events(self):
        """Handle user input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
        
        # Continuous key presses for movement
        if not self.paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move_left()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right()
    
    def spawn_cookies(self):
        """Spawn cookies from random chutes"""
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            chute = random.choice(self.chutes)
            new_cookie = Cookie(chute.x, chute.y)
            self.cookies.append(new_cookie)
            self.spawn_timer = 0
    
    def update(self):
        """Update game logic"""
        if self.paused:
            return
        
        # Spawn new cookies
        self.spawn_cookies()
        
        # Update player
        self.player.update()
        
        # Update cookies
        for cookie in self.cookies[:]:
            cookie.update()
            
            # Check collision with player
            if self.check_collision(cookie, self.player):
                self.cookies.remove(cookie)
                self.score += POINTS_PER_COOKIE
                self.combo += 1
                
                # Bonus for combo
                if self.combo > 1:
                    self.score += COMBO_BONUS * (self.combo - 1)
                
                # Play catch sound
                self.sound_manager.play_catch_sound()
                continue
            
            # Check if cookie fell off screen
            if cookie.y > SCREEN_HEIGHT:
                self.cookies.remove(cookie)
                self.combo = 0  # Reset combo
                self.lives -= 1
        
        # Increase difficulty over time
        self.difficulty_timer += 1
        if self.difficulty_timer >= DIFFICULTY_INCREASE_INTERVAL:
            self.increase_difficulty()
            self.difficulty_timer = 0
        
        # Check game over
        if self.lives <= 0:
            self.game_over()
    
    def check_collision(self, cookie, player):
        """Check collision between cookie and player"""
        cookie_rect = pygame.Rect(cookie.x - COOKIE_SIZE // 2, 
                                   cookie.y - COOKIE_SIZE // 2, 
                                   COOKIE_SIZE, COOKIE_SIZE)
        player_rect = pygame.Rect(player.x - player.width // 2, 
                                   player.y - player.height // 2, 
                                   player.width, player.height)
        
        return cookie_rect.colliderect(player_rect)
    
    def increase_difficulty(self):
        """Increase game difficulty"""
        if self.spawn_rate > MIN_SPAWN_RATE:
            self.spawn_rate = max(self.spawn_rate - 2, MIN_SPAWN_RATE)
        self.level += 1
    
    def draw(self):
        """Render game objects"""
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw chutes
        for chute in self.chutes:
            chute.draw(self.screen)
        
        # Draw cookies
        for cookie in self.cookies:
            cookie.draw(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
        
        # Draw pause screen if paused
        if self.paused:
            self.draw_pause_screen()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw score, lives, and level"""
        font = pygame.font.Font(None, 36)
        
        # Score
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Combo
        if self.combo > 1:
            combo_text = font.render(f"Combo: {self.combo}x", True, YELLOW)
            self.screen.blit(combo_text, (10, 50))
        
        # Lives
        lives_text = font.render(f"Lives: {self.lives}", True, RED)
        self.screen.blit(lives_text, (SCREEN_WIDTH - 200, 10))
        
        # Level
        level_text = font.render(f"Level: {self.level}", True, GREEN)
        self.screen.blit(level_text, (SCREEN_WIDTH - 200, 50))
    
    def draw_pause_screen(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        font = pygame.font.Font(None, 72)
        pause_text = font.render("PAUSED", True, WHITE)
        text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(pause_text, text_rect)
        
        small_font = pygame.font.Font(None, 36)
        continue_text = small_font.render("Press SPACE to continue", True, WHITE)
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        self.screen.blit(continue_text, continue_rect)
    
    def game_over(self):
        """Handle game over"""
        self.sound_manager.play_game_over_sound()
        self.display_game_over_screen()
    
    def display_game_over_screen(self):
        """Display game over screen"""
        self.screen.fill(BACKGROUND_COLOR)
        
        font_large = pygame.font.Font(None, 96)
        font_medium = pygame.font.Font(None, 48)
        font_small = pygame.font.Font(None, 36)
        
        game_over_text = font_large.render("GAME OVER", True, RED)
        score_text = font_medium.render(f"Final Score: {self.score}", True, WHITE)
        level_text = font_medium.render(f"Level Reached: {self.level}", True, WHITE)
        restart_text = font_small.render("Press SPACE to restart or ESC to quit", True, WHITE)
        
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 100))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 250))
        self.screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 350))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 500))
        
        pygame.display.flip()
        
        # Wait for restart or quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__init__()  # Restart game
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        waiting = False
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


class SoundManager:
    """Manages game audio"""
    
    def __init__(self):
        """Initialize sound manager"""
        self.bg_music_enabled = True
        self.sfx_enabled = True
        self.volume = 0.7
    
    def play_background_music(self):
        """Play background music loop"""
        try:
            pygame.mixer.music.load('assets/audio/background_music.mp3')
            pygame.mixer.music.set_volume(self.volume * 0.5)  # Lower volume for bg music
            pygame.mixer.music.play(-1)  # Loop indefinitely
        except:
            print("Background music file not found. Add 'assets/audio/background_music.mp3'")
    
    def play_catch_sound(self):
        """Play sound when cookie is caught"""
        try:
            catch_sound = pygame.mixer.Sound('assets/audio/catch.wav')
            catch_sound.set_volume(self.volume)
            catch_sound.play()
        except:
            print("Catch sound file not found. Add 'assets/audio/catch.wav'")
    
    def play_game_over_sound(self):
        """Play sound when game is over"""
        try:
            pygame.mixer.music.stop()
            game_over_sound = pygame.mixer.Sound('assets/audio/game_over.wav')
            game_over_sound.set_volume(self.volume)
            game_over_sound.play()
        except:
            print("Game over sound file not found. Add 'assets/audio/game_over.wav'")
    
    def toggle_music(self):
        """Toggle background music on/off"""
        if self.bg_music_enabled:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.bg_music_enabled = not self.bg_music_enabled
    
    def set_volume(self, level):
        """Set master volume (0.0 to 1.0)"""
        self.volume = max(0, min(1, level))
        pygame.mixer.music.set_volume(self.volume * 0.5)
