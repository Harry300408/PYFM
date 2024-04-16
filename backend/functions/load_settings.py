import sys
sys.path.append("././")

from configparser import ConfigParser
from vars import variables as var
import yaml, pygame

def load_settings() -> ConfigParser:
    with open("settings.ini", "r") as Sf:
        settings = ConfigParser()
        settings.read_file(Sf)

        var.LANG = settings.get("SETTINGS", "language")

        if var.LANG.lower() == "english":
            with open("langs/english_loc.yaml", "r", -1, var.encoding) as locf:
                var.localisation = yaml.safe_load(locf)

        elif var.LANG.lower() == "french":
            with open("langs/french_loc.yaml", "r", -1, var.encoding) as locf:
                var.localisation = yaml.safe_load(locf)

        height = settings.get("SETTINGS", "height")
        width = settings.get("SETTINGS", "width")
        var.HEIGHT = int(height)
        var.WIDTH = int(width)
        var.SCREEN = pygame.display.set_mode((var.WIDTH,var.HEIGHT))
        var.BACKGROUND_IMAGE = pygame.transform.scale(var.BG_IMG, (var.WIDTH, var.HEIGHT))
                    

        var.IS_FULLSCREEN = settings.get("SETTINGS", "is_fullscreen")
        if var.IS_FULLSCREEN.lower() == "true":
            var.SCREEN = pygame.display.set_mode((var.WIDTH, var.HEIGHT), pygame.FULLSCREEN)

        elif var.IS_FULLSCREEN.lower() == "false":
            var.SCREEN = pygame.display.set_mode((var.WIDTH, var.HEIGHT))

        var.ticspeed = int(settings.get("SETTINGS", "ticspeed"))
            

