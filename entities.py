"""
Game entities: Player, Cookies, and Chutes
"""

import pygame
import math
from constants import *


class Player:
    """The Fean character that catches cookies"""
    
    def __init__(self, x, y):
        """Initialize the player"""
        self.x = x
        self.y = y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.velocity_x = 0
        self.speed = PLAYER_SPEED
    
    def move_left(self):
        """Move player left"""
        self.velocity_x = -self.speed
    
    def move_right(self):
        """Move player right"""
        self.velocity_x = self.speed
    
    def update(self):
        """Update player position"""
        self.x += self.velocity_x
        
        # Boundary checking
        if self.x - self.width // 2 < 0:
            self.x = self.width // 2
        elif self.x + self.width // 2 > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width // 2
        
        # Friction/deceleration
        self.velocity_x *= 0.9
    
    def draw(self, surface):
        """Draw the player"""
        # Draw a simple rectangle for now (will be replaced with sprite)
        player_rect = pygame.Rect(self.x - self.width // 2,
                                   self.y - self.height // 2,
                                   self.width,
                                   self.height)
        
        # Draw player body (blue to match FEAN shirt)
        pygame.draw.rect(surface, PLAYER_COLOR, player_rect, border_radius=10)
        
        # Draw a simple face
        face_center_x = self.x
        face_center_y = self.y - self.height // 3
        pygame.draw.circle(surface, SKIN_COLOR, (face_center_x, face_center_y), self.width // 6)
        
        # Draw eyes
        eye_offset = self.width // 10
        pygame.draw.circle(surface, BLACK, (face_center_x - eye_offset, face_center_y - self.width // 15), 3)
        pygame.draw.circle(surface, BLACK, (face_center_x + eye_offset, face_center_y - self.width // 15), 3)
        
        # Draw a catching basket area (lighter color)
        basket_rect = pygame.Rect(self.x - self.width // 3,
                                   self.y + self.height // 4,
                                   self.width // 1.5,
                                   self.height // 3)
        pygame.draw.rect(surface, BASKET_COLOR, basket_rect, border_radius=5)


class Cookie:
    """A cookie falling from the chutes"""
    
    def __init__(self, x, y):
        """Initialize a cookie"""
        self.x = x
        self.y = y
        self.velocity_y = COOKIE_FALL_SPEED
        self.size = COOKIE_SIZE
        self.rotation = 0
        self.rotation_speed = 5
    
    def update(self):
        """Update cookie position and rotation"""
        self.y += self.velocity_y
        self.velocity_y += GRAVITY  # Accelerate downward
        self.rotation += self.rotation_speed
        
        # Cap maximum velocity
        if self.velocity_y > MAX_COOKIE_VELOCITY:
            self.velocity_y = MAX_COOKIE_VELOCITY
    
    def draw(self, surface):
        """Draw the cookie"""
        # Draw cookie circle
        pygame.draw.circle(surface, COOKIE_COLOR, (int(self.x), int(self.y)), self.size // 2)
        
        # Draw cookie chips (small dots)
        chip_count = 8
        for i in range(chip_count):
            angle = (360 / chip_count) * i + (self.rotation % 360)
            rad = math.radians(angle)
            chip_x = self.x + math.cos(rad) * (self.size // 3)
            chip_y = self.y + math.sin(rad) * (self.size // 3)
            pygame.draw.circle(surface, CHIP_COLOR, (int(chip_x), int(chip_y)), 2)


class Chute:
    """A cookie chute that dispenses cookies"""
    
    def __init__(self, x, y):
        """Initialize a chute"""
        self.x = x
        self.y = y
        self.width = CHUTE_WIDTH
        self.height = CHUTE_HEIGHT
    
    def draw(self, surface):
        """Draw the chute"""
        # Draw chute body
        chute_rect = pygame.Rect(self.x - self.width // 2,
                                  self.y,
                                  self.width,
                                  self.height)
        pygame.draw.rect(surface, CHUTE_COLOR, chute_rect, border_radius=5)
        
        # Draw chute opening (darker)
        opening_rect = pygame.Rect(self.x - self.width // 3,
                                    self.y + self.height - 10,
                                    self.width // 1.5,
                                    10)
        pygame.draw.rect(surface, CHUTE_OPENING_COLOR, opening_rect)
        
        # Draw chute outline
        pygame.draw.rect(surface, BLACK, chute_rect, 2, border_radius=5)


class Particle:
    """A particle effect (for catching cookies, etc.)"""
    
    def __init__(self, x, y, vx, vy, lifetime=30, color=(255, 215, 0)):
        """Initialize a particle"""
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.color = color
        self.size = 5
    
    def update(self):
        """Update particle position"""
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
        self.lifetime -= 1
    
    def draw(self, surface):
        """Draw the particle"""
        # Fade out over time
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        color = tuple(min(255, c) for c in self.color)
        
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size)
    
    def is_alive(self):
        """Check if particle is still alive"""
        return self.lifetime > 0
