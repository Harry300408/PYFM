import sys
sys.path.append("././")

from vars import variables as var
from classes import button as b
from backend.functions import getfont as gtf, save_settings as Ss
from frontend import mainmenu as Mm

import pygame, pygame_gui, yaml

def tic_speed(loc) -> None:
    while var.setup_tic_speed:
        ## SETUP ##

        var.SCREEN.blit(var.BACKGROUND_IMAGE, (0, 0))
        var.MOUSE_POS = pygame.mouse.get_pos()

        ## TEXT ##

        GAMENAME = gtf.get_font(100).render(var.PYFM_TEXT, True, "white")
        GAMENAME_RECT = GAMENAME.get_rect(center=(var.WIDTH / 2, 50))
        var.SCREEN.blit(GAMENAME, GAMENAME_RECT)
        
        SET_UP_TEXT = gtf.get_font(30).render(loc["setup"], True, "white")
        SET_UP_TEXT_RECT = SET_UP_TEXT.get_rect(center=(var.WIDTH / 2, 100))
        var.SCREEN.blit(SET_UP_TEXT, SET_UP_TEXT_RECT)

        SELECT_TICK_SPEED_TEXT = gtf.get_font(30).render(loc["select_tick_speed"], True, "white")
        SELECT_TICK_SPEED_TEXT_RECT = SELECT_TICK_SPEED_TEXT.get_rect(center=(var.WIDTH / 2, var.HEIGHT / 2 - 210))
        var.SCREEN.blit(SELECT_TICK_SPEED_TEXT, SELECT_TICK_SPEED_TEXT_RECT)

        SELECT_TICK_SPEED_DEF_TEXT = gtf.get_font(20).render(loc["select_tick_speed_def"], True, "white")
        SELECT_TICK_SPEED_DEF_TEXT_RECT = SELECT_TICK_SPEED_DEF_TEXT.get_rect(center=(var.WIDTH / 2, var.HEIGHT / 2 + 90))
        var.SCREEN.blit(SELECT_TICK_SPEED_DEF_TEXT, SELECT_TICK_SPEED_DEF_TEXT_RECT)

        ## BUTTONS ##

        QUIT_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(80, var.HEIGHT - 35), 
                            text_input=loc["quit"], font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        QUIT_BUTTON.changeColor(var.MOUSE_POS)
        QUIT_BUTTON.update(var.SCREEN)
        
        ZERO_S_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 - 120, var.HEIGHT / 2 - 150), 
                            text_input=loc["0s"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        ZERO_S_BUTTON.changeColor(var.MOUSE_POS)
        ZERO_S_BUTTON.update(var.SCREEN)

        ONE_S_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 + 120, var.HEIGHT / 2 - 150), 
                            text_input=loc["1s"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        ONE_S_BUTTON.changeColor(var.MOUSE_POS)
        ONE_S_BUTTON.update(var.SCREEN)

        TWO_S_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 - 120, var.HEIGHT / 2 - 70), 
                            text_input=loc["2s"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        TWO_S_BUTTON.changeColor(var.MOUSE_POS)
        TWO_S_BUTTON.update(var.SCREEN)

        THREE_S_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 + 120, var.HEIGHT / 2 - 70), 
                            text_input=loc["3s"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        THREE_S_BUTTON.changeColor(var.MOUSE_POS)
        THREE_S_BUTTON.update(var.SCREEN)

        FOUR_S_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2, var.HEIGHT / 2 + 10), 
                            text_input=loc["4s"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        FOUR_S_BUTTON.changeColor(var.MOUSE_POS)
        FOUR_S_BUTTON.update(var.SCREEN)


        ## FUNCTIONALITY ##

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed()[0]:

                    if QUIT_BUTTON.checkForInput(var.MOUSE_POS):
                        pygame.quit()
                        sys.exit()

                    if ZERO_S_BUTTON.checkForInput(var.MOUSE_POS):
                        var.ticspeed = 0
                        var.setup_tic_speed = False
                        var.mm_open = True
                        Ss.save_settings(var.LANG, var.WIDTH, var.HEIGHT, var.IS_FULLSCREEN, var.ticspeed)
                        Mm.main_menu(loc)

                    if ONE_S_BUTTON.checkForInput(var.MOUSE_POS):
                        var.ticspeed = 1
                        var.setup_tic_speed = False
                        var.mm_open = True
                        Ss.save_settings(var.LANG, var.WIDTH, var.HEIGHT, var.IS_FULLSCREEN, var.ticspeed)
                        Mm.main_menu(loc)
                
                    if TWO_S_BUTTON.checkForInput(var.MOUSE_POS):
                        var.ticspeed = 2
                        var.setup_tic_speed = False
                        var.mm_open = True
                        Ss.save_settings(var.LANG, var.WIDTH, var.HEIGHT, var.IS_FULLSCREEN, var.ticspeed)
                        Mm.main_menu(loc)
                
                    if THREE_S_BUTTON.checkForInput(var.MOUSE_POS):
                        var.ticspeed = 3
                        var.setup_tic_speed = False
                        var.mm_open = True
                        Ss.save_settings(var.LANG, var.WIDTH, var.HEIGHT, var.IS_FULLSCREEN, var.ticspeed)
                        Mm.main_menu(loc)

                    if FOUR_S_BUTTON.checkForInput(var.MOUSE_POS):
                        var.ticspeed = 4
                        var.setup_tic_speed = False
                        var.mm_open = True
                        Ss.save_settings(var.LANG, var.WIDTH, var.HEIGHT, var.IS_FULLSCREEN, var.ticspeed)
                        Mm.main_menu(loc)
                    
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        pygame.display.update()

def fullsceen_or_window(loc) -> None:
    while var.fulscreen_option:
        ## SETUP ##

        var.SCREEN.blit(var.BACKGROUND_IMAGE, (0, 0))
        var.MOUSE_POS = pygame.mouse.get_pos()

        ## TEXT ##

        GAMENAME = gtf.get_font(100).render(var.PYFM_TEXT, True, "white")
        GAMENAME_RECT = GAMENAME.get_rect(center=(var.WIDTH / 2, 50))
        var.SCREEN.blit(GAMENAME, GAMENAME_RECT)
        
        SET_UP_TEXT = gtf.get_font(30).render(loc["setup"], True, "white")
        SET_UP_TEXT_RECT = SET_UP_TEXT.get_rect(center=(var.WIDTH / 2, 100))
        var.SCREEN.blit(SET_UP_TEXT, SET_UP_TEXT_RECT)
    
        ## BUTTONS ##

        QUIT_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(80, var.HEIGHT - 35), 
                            text_input=loc["quit"], font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        QUIT_BUTTON.changeColor(var.MOUSE_POS)
        QUIT_BUTTON.update(var.SCREEN)

        FULLSCREEN_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 - 120, var.HEIGHT / 2 - 150), 
                            text_input=loc["fullscreen"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        FULLSCREEN_BUTTON.changeColor(var.MOUSE_POS)
        FULLSCREEN_BUTTON.update(var.SCREEN)

        WINDOWED_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 + 120, var.HEIGHT / 2 - 150), 
                            text_input=loc["windowed"], font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        WINDOWED_BUTTON.changeColor(var.MOUSE_POS)
        WINDOWED_BUTTON.update(var.SCREEN)
        

        ## FUNCTIONALITY ##

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed()[0]:

                    if QUIT_BUTTON.checkForInput(var.MOUSE_POS):
                        pygame.quit()
                        sys.exit()

                    if FULLSCREEN_BUTTON.checkForInput(var.MOUSE_POS):
                        var.IS_FULLSCREEN = "true"
                        var.SCREEN = pygame.display.set_mode((var.WIDTH, var.HEIGHT), pygame.FULLSCREEN)
                        var.fulscreen_option = False
                        var.setup_tic_speed = True
                        tic_speed(loc)
                
                    if WINDOWED_BUTTON.checkForInput(var.MOUSE_POS):
                        var.IS_FULLSCREEN = "false"
                        var.SCREEN = pygame.display.set_mode((var.WIDTH, var.HEIGHT))
                        var.fulscreen_option = False
                        var.setup_tic_speed = True
                        tic_speed(loc)
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
        
        pygame.display.update()

def select_resolution(loc) -> None:
    while var.select_resolution:
        ## SETUP ##

        var.SCREEN.blit(var.BACKGROUND_IMAGE, (0, 0))
        var.MOUSE_POS = pygame.mouse.get_pos()

        ## TEXT ##

        GAMENAME = gtf.get_font(100).render(var.PYFM_TEXT, True, "white")
        GAMENAME_RECT = GAMENAME.get_rect(center=(var.WIDTH / 2, 50))
        var.SCREEN.blit(GAMENAME, GAMENAME_RECT)
        
        SET_UP_TEXT = gtf.get_font(30).render(loc["setup"], True, "white")
        SET_UP_TEXT_RECT = SET_UP_TEXT.get_rect(center=(var.WIDTH / 2, 100))
        var.SCREEN.blit(SET_UP_TEXT, SET_UP_TEXT_RECT)

        SELECT_RESOLUTION_TEXT = gtf.get_font(30).render(loc["select_resolution"], True, "white")
        SELECT_RESOLUTION_TEXT_RECT = SELECT_RESOLUTION_TEXT.get_rect(center=(var.WIDTH / 2, var.HEIGHT / 2 - 210))
        var.SCREEN.blit(SELECT_RESOLUTION_TEXT, SELECT_RESOLUTION_TEXT_RECT)

        ## BUTTONS ##

        QUIT_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(80, var.HEIGHT - 35), 
                            text_input=loc["quit"], font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        QUIT_BUTTON.changeColor(var.MOUSE_POS)
        QUIT_BUTTON.update(var.SCREEN)

        SvnTwntyPButton = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 - 120, var.HEIGHT / 2 - 150), 
                            text_input="1280 x 720p", font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        SvnTwntyPButton.changeColor(var.MOUSE_POS)
        SvnTwntyPButton.update(var.SCREEN)

        TenEtyPButton = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2 + 120, var.HEIGHT / 2 - 150), 
                            text_input="1920 x 1080p", font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        TenEtyPButton.changeColor(var.MOUSE_POS)
        TenEtyPButton.update(var.SCREEN)

        FourKButton = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(var.WIDTH / 2, var.HEIGHT / 2 - 50), 
                            text_input="3840 x 2160p", font=gtf.get_font(25), base_color="white", hovering_color="yellow")
        FourKButton.changeColor(var.MOUSE_POS)
        FourKButton.update(var.SCREEN)

        

        ## FUNCTIONALITY ##

        for i in [QUIT_BUTTON, SvnTwntyPButton, TenEtyPButton]:
            i.changeColor(var.MOUSE_POS)
            i.update(var.SCREEN)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed()[0]:

                    if QUIT_BUTTON.checkForInput(var.MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                
                    if SvnTwntyPButton.checkForInput(var.MOUSE_POS):
                        var.WIDTH = 1280
                        var.HEIGHT = 720
                        var.SCREEN = pygame.display.set_mode((var.WIDTH,var.HEIGHT))
                        var.BACKGROUND_IMAGE = pygame.transform.scale(var.BG_IMG, (var.WIDTH, var.HEIGHT))
                        var.select_resolution = False
                        var.fulscreen_option = True
                        fullsceen_or_window(loc)
                
                    if TenEtyPButton.checkForInput(var.MOUSE_POS):
                        var.WIDTH = 1920
                        var.HEIGHT = 1080
                        var.SCREEN = pygame.display.set_mode((var.WIDTH,var.HEIGHT))
                        var.BACKGROUND_IMAGE = pygame.transform.scale(var.BG_IMG, (var.WIDTH, var.HEIGHT))
                        var.select_resolution = False
                        var.fulscreen_option = True
                        fullsceen_or_window(loc)

                    if FourKButton.checkForInput(var.MOUSE_POS):
                        var.WIDTH = 3840
                        var.HEIGHT = 2160
                        var.SCREEN = pygame.display.set_mode((var.WIDTH,var.HEIGHT))
                        var.BACKGROUND_IMAGE = pygame.transform.scale(var.BG_IMG, (var.WIDTH, var.HEIGHT))
                        var.select_resolution = False
                        var.fulscreen_option = True
                        fullsceen_or_window(loc)
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        pygame.display.update()

def setup_settings() -> None:
    while var.setup_open:

        ## SETUP ##

        var.SCREEN.blit(var.BACKGROUND_IMAGE, (0, 0))
        var.MOUSE_POS = pygame.mouse.get_pos()
        
        ## TEXT ##

        GAMENAME = gtf.get_font(100).render(var.PYFM_TEXT, True, "white")
        GAMENAME_RECT = GAMENAME.get_rect(center=(var.WIDTH / 2, 50))
        var.SCREEN.blit(GAMENAME, GAMENAME_RECT)
        
        SET_UP_TEXT = gtf.get_font(30).render("Setup", True, "white")
        SET_UP_TEXT_RECT = SET_UP_TEXT.get_rect(center=(var.WIDTH / 2, 100))
        var.SCREEN.blit(SET_UP_TEXT, SET_UP_TEXT_RECT)

        MORE_LANGS_TO_COME = gtf.get_font(20).render("More Languages To Come!", True, "white")
        MORE_LANGS_TO_COME_RECT = MORE_LANGS_TO_COME.get_rect(center=(var.WIDTH / 2, var.HEIGHT - 40))
        var.SCREEN.blit(MORE_LANGS_TO_COME, MORE_LANGS_TO_COME_RECT)

        LANGS_NOT_ACURATE = gtf.get_font(20).render("Language Translations May Not Be 100% Accurate! (So Please Help With Translations)", True, "white")
        LANGS_NOT_ACURATE_RECT = LANGS_NOT_ACURATE.get_rect(center=(var.WIDTH / 2, var.HEIGHT - 15))
        var.SCREEN.blit(LANGS_NOT_ACURATE, LANGS_NOT_ACURATE_RECT)

        ## BUTTONS ##

        QUIT_BUTTON = b.Button(image=var.SET_UP_QUIT_BUTTON, pos=(80, var.HEIGHT - 35), 
                            text_input="Quit", font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        QUIT_BUTTON.changeColor(var.MOUSE_POS)
        QUIT_BUTTON.update(var.SCREEN)

        ENGLISH_LANG_SELECT = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(var.WIDTH / 2 - 120, var.HEIGHT / 2 - 200), 
                            text_input="English", font=gtf.get_font(40), base_color="white", hovering_color="yellow")
        ENGLISH_LANG_SELECT.changeColor(var.MOUSE_POS)
        ENGLISH_LANG_SELECT.update(var.SCREEN)

        FRENCH_LANG_SELECT = b.Button(image=var.SET_UP_LANG_BUTTON, pos=(var.WIDTH / 2 + 120, var.HEIGHT / 2 - 200), 
                            text_input="Français", font=gtf.get_font(38), base_color="white", hovering_color="yellow")
        FRENCH_LANG_SELECT.changeColor(var.MOUSE_POS)
        FRENCH_LANG_SELECT.update(var.SCREEN)

        ## FUNCTIONALITY ##

        for i in [QUIT_BUTTON, ENGLISH_LANG_SELECT,FRENCH_LANG_SELECT]:
            i.changeColor(var.MOUSE_POS)
            i.update(var.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.key == pygame.BUTTON_LEFT:
                
                if pygame.mouse.get_pressed()[0]:
                
                    if QUIT_BUTTON.checkForInput(var.MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    
                    if ENGLISH_LANG_SELECT.checkForInput(var.MOUSE_POS):
                        with open("langs/english_loc.yaml", "r", -1, var.encoding) as locf:
                            var.localisation = yaml.safe_load(locf)
                            var.LANG = "english"
                            var.select_resolution = True
                            var.setup_open = False
                            select_resolution(var.localisation)

                    if FRENCH_LANG_SELECT.checkForInput(var.MOUSE_POS):
                        with open("langs/french_loc.yaml", "r", -1, var.encoding) as locf:
                            var.localisation = yaml.safe_load(locf)
                            var.LANG = "french"
                            var.select_resolution = True
                            var.setup_open = False
                            select_resolution(var.localisation)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
        
        pygame.display.update()

