import sys
sys.path.append("./")
import pygame

from vars import variables as vars

def get_font(size) -> pygame.font.Font:
    return pygame.font.Font("fonts/pyfm_font.ttf", size)
