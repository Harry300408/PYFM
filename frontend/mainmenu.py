import sys
import os
sys.path.append("./")

from vars import variables as var
from backend.functions import getfont as gtf, setup as Stp,  load_db as LDB
from frontend import options as Opts
from classes.button import Button
import pygame, pygame_gui

## Main Menu Screen

def main_menu(loc) -> None:
    while var.mm_open:
        ## SETUP ##

        var.SCREEN.blit(var.BACKGROUND_IMAGE, (0, 0))
        var.MOUSE_POS = pygame.mouse.get_pos()

        ## TEXT ## 

        MENU_TEXT = gtf.get_font(100).render(var.PYFM_TEXT, True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(var.WIDTH / 2, 50))

        MAIN_MENU_TEXT = gtf.get_font(30).render(loc["mainmenu"], True, "white")
        MAIN_MENU_TEXT_RECT = MAIN_MENU_TEXT.get_rect(center=(var.WIDTH / 2, 100))
        var.SCREEN.blit(MAIN_MENU_TEXT, MAIN_MENU_TEXT_RECT)

        ## BUTTONS ##

        PLAY_BUTTON = Button(image=var.BUTTON, pos=(var.WIDTH / 2, var.HEIGHT / 2 - 140), 
                            text_input=loc["play"], font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        
        OPTIONS_BUTTON = Button(image=var.BUTTON, pos=(var.WIDTH / 2, var.HEIGHT / 2 + 10), 
                            text_input=loc["options"], font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        
        QUIT_BUTTON = Button(image=var.BUTTON, pos=(var.WIDTH / 2, var.HEIGHT / 2 + 160), 
                            text_input=loc["quit"], font=gtf.get_font(40), base_color="white", hovering_color="yellow")

        var.SCREEN.blit(MENU_TEXT, MENU_RECT)

        ## FUNCTIONALITY ##

        for i in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            i.changeColor(var.MOUSE_POS)
            i.update(var.SCREEN)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if pygame.mouse.get_pressed()[0]:
                
                    if PLAY_BUTTON.checkForInput(var.MOUSE_POS):
                        LDB.load_db()

                    if OPTIONS_BUTTON.checkForInput(var.MOUSE_POS):
                        var.mm_open = False
                        var.options_open = True
                        var.last_menu_open = "main menu"
                        Opts.options_page(loc)

                    if QUIT_BUTTON.checkForInput(var.MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
                


        pygame.display.update()


