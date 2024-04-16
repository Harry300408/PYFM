import sys
sys.path.append("././")

from frontend import mainmenu as Mm
from vars import variables as var

def last_menu_open(loc):
    lmo = var.last_menu_open

    if lmo.lower() == "main" or lmo.lower() == "main menu":
        var.mm_open = True
        Mm.main_menu(loc)

    return lmo