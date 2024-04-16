from openpyxl import Workbook, load_workbook
from backend.functions import load_settings as LdaS
from vars import variables as var
from frontend import options as Opt, play as Ply, mainmenu as Mm
from backend.functions import getfont as Gtf, setup as Stp
from configparser import ConfigParser as ConPar
import pygame, pygame_gui
import yaml
import time

if __name__ == '__main__': # Just makes sure it's running right
    settings = ConPar()

    pygame.init()
    pygame.display.set_caption("PYFM")
    pygame.display.set_icon(var.ICON)

    with open("settings.ini", "r") as sf: ## Cheking Settings File
        settings.read_file(sf)
        no_settings_saved = settings.get("SETTINGS", "NoSettings")
        
        if no_settings_saved.lower() == "true":
            Stp.setup_settings()
        
        elif no_settings_saved.lower() == "false":
            LdaS.load_settings()
            Mm.main_menu(var.localisation)


## FOR CENTER ALIGNING USE f'{var:^int}'
## IF CHAR TO FIL SPACE WANTED DO f'{var:char^int}'
## ADD ANY TEXT BEFORE OR AFTER IF NEEDED
    