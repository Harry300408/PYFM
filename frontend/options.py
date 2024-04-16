import sys
sys.path.append("./")

from vars import variables as var
from backend.functions import getfont as gtf, last_menu_open as Lmo, save_settings as Ss, load_settings as Ls
from frontend import mainmenu as Mm
from classes import button as b
from configparser import ConfigParser

import pygame, yaml

settings = ConfigParser()

def options_page(loc) -> None:
    while var.options_open:
        ## SETUP ##

        var.SCREEN.blit(var.BACKGROUND_IMAGE, (0, 0))
        var.MOUSE_POS = pygame.mouse.get_pos()

        ## TEXT ##

        GAMENAME = gtf.get_font(100).render(var.PYFM_TEXT, True, "white")
        GAMENAME_RECT = GAMENAME.get_rect(center=(var.WIDTH / 2, 50))
        var.SCREEN.blit(GAMENAME, GAMENAME_RECT)
        
        SETTINGS_TEXT = gtf.get_font(30).render(loc["options"], True, "white")
        SETTINGS_TEXT_RECT = SETTINGS_TEXT.get_rect(center=(var.WIDTH / 2, 100))
        var.SCREEN.blit(SETTINGS_TEXT, SETTINGS_TEXT_RECT)

        LANG_TEXT = gtf.get_font(30).render(loc["lang"], True, "white")
        LANG_TEXT_RECT = LANG_TEXT.get_rect(center=(160, 130))
        var.SCREEN.blit(LANG_TEXT, LANG_TEXT_RECT)

        SELECT_RESOLUTION_TEXT = gtf.get_font(30).render(loc["resolution"], True, "white")
        SELECT_RESOLUTION_TEXT_RECT = SELECT_RESOLUTION_TEXT.get_rect(center=(450, 130))
        var.SCREEN.blit(SELECT_RESOLUTION_TEXT, SELECT_RESOLUTION_TEXT_RECT)
        
        
        
        ## BOTTOM TEXT ##
        
        MORE_LANGS_TO_COME = gtf.get_font(20).render("More Languages To Come!", True, "white")
        MORE_LANGS_TO_COME_RECT = MORE_LANGS_TO_COME.get_rect(center=(var.WIDTH / 2, var.HEIGHT - 40))
        var.SCREEN.blit(MORE_LANGS_TO_COME, MORE_LANGS_TO_COME_RECT)

        LANGS_NOT_ACURATE = gtf.get_font(20).render("Language Translations May Not Be 100% Accurate! (So Please Help With Translations)", True, "white")
        LANGS_NOT_ACURATE_RECT = LANGS_NOT_ACURATE.get_rect(center=(var.WIDTH / 2, var.HEIGHT - 15))
        var.SCREEN.blit(LANGS_NOT_ACURATE, LANGS_NOT_ACURATE_RECT)

        ## BUTTONS ##

        BACK_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(80, var.HEIGHT - 35), 
                            text_input=loc["back"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        BACK_BUTTON.changeColor(var.MOUSE_POS)
        BACK_BUTTON.update(var.SCREEN)

        SAVE_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH - 80, var.HEIGHT - 35), 
                            text_input=loc["save"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        SAVE_BUTTON.changeColor(var.MOUSE_POS)
        SAVE_BUTTON.update(var.SCREEN)

            ## RESOLUTION 
        
        SvnTwntyPButton = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(450, 180), 
                            text_input="1280 x 720p", font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        SvnTwntyPButton.changeColor(var.MOUSE_POS)
        SvnTwntyPButton.update(var.SCREEN)

        TenEtyPButton = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(450, 250), 
                            text_input="1920 x 1080p", font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        TenEtyPButton.changeColor(var.MOUSE_POS)
        TenEtyPButton.update(var.SCREEN)

        FourKButton = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(450, 320), 
                            text_input="3840 x 2160p", font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        FourKButton.changeColor(var.MOUSE_POS)
        FourKButton.update(var.SCREEN)
            
            ## LANGUAGE

        ENGLISH_LANG_SELECT = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(80, 180), 
                            text_input="English", font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        ENGLISH_LANG_SELECT.changeColor(var.MOUSE_POS)
        ENGLISH_LANG_SELECT.update(var.SCREEN)

        FRENCH_LANG_SELECT = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(240, 180), 
                            text_input="Français", font=gtf.get_font(38), base_color="white", hovering_color="yellow")
        FRENCH_LANG_SELECT.changeColor(var.MOUSE_POS)
        FRENCH_LANG_SELECT.update(var.SCREEN)

        ## FUNCTIONALITY ##

        for i in [BACK_BUTTON, SAVE_BUTTON, ENGLISH_LANG_SELECT, FRENCH_LANG_SELECT]:
            i.changeColor(var.MOUSE_POS)
            i.update(var.SCREEN)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if pygame.mouse.get_pressed()[0]:

                    if ENGLISH_LANG_SELECT.checkForInput(var.MOUSE_POS):
                        with open("langs/english_loc.yaml", "r", -1, var.encoding) as locf:
                            var.LANG = "english"
                            var.localisation = yaml.safe_load(locf)
                            options_page(var.localisation)
                    
                    if FRENCH_LANG_SELECT.checkForInput(var.MOUSE_POS):
                        with open("langs/french_loc.yaml", "r", -1, var.encoding) as locf:
                            var.LANG = "french"
                            var.localisation = yaml.safe_load(locf)
                            options_page(var.localisation)

                    if SvnTwntyPButton.checkForInput(var.MOUSE_POS):
                        pass
                    
                    if TenEtyPButton.checkForInput(var.MOUSE_POS):
                        pass

                    if FourKButton.checkForInput(var.MOUSE_POS):
                        pass
                
                    if BACK_BUTTON.checkForInput(var.MOUSE_POS):
                        var.options_open = False
                        Ls.load_settings()
                        Lmo.last_menu_open(var.localisation)

                    if SAVE_BUTTON.checkForInput(var.MOUSE_POS):
                        Ss.save_settings(var.LANG, var.WIDTH, var.HEIGHT, var.IS_FULLSCREEN, var.ticspeed)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        pygame.display.update()
