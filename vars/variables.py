import pygame, pygame_gui
from configparser import ConfigParser as ConPar

    # SCREEN
WIDTH = 1280    
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
ICON = pygame.image.load("gfx/icon.png")

    # MOUSE AND KEYBORD
MOUSE_POS = pygame.mouse.get_pos()

    # SETTINGS
settings = "settings.ini" 
encoding = "utf-8"

    # BOOLS
Has_changed_setting = False

    # SETUP BOOLS
NO_SETTINGS_SAVED = False

    # SETTINGS
LANG = ""
# Resolution Is In Screen
IS_FULLSCREEN = "False"
ticspeed = 0

    # LOCALISATION
PYFM_TEXT = "PY-FM" ## Rare Use
localisation = {}

    # GUI
setup_open = True
select_resolution = False
fulscreen_option = False
setup_tic_speed = False

mm_open = True
options_open = False

    # FUNCTION VARS
last_menu_open = ""


    # GFX
BG_IMG = pygame.image.load("gfx/background.png")
BUTTON = pygame.image.load("gfx/mm_button.png")
SET_UP_QUIT_BUTTON = pygame.image.load("gfx/stp_quit.png")
SET_UP_LANG_BUTTON = pygame.image.load("gfx/stp_lang_button.png")
BACKGROUND_IMAGE = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))