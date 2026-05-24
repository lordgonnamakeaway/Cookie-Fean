"""
Cookie Fean Game
A fun 2D game where Fean catches falling cookies from three chutes.
"""

import pygame
import random
import sys
from game import CookieFeanGame

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create and run the game
    game = CookieFeanGame()
    game.run()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
