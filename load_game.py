from configparser import ConfigParser
from setting_menu import settings
import pygame
import sys
import timer

class game_loading():
    '''
    this class helps load saved game
    '''
    def __init__(self,scr,snd):  
        super().__init__()
        self.screen = scr
        self.sound = snd
        self.phase = 0
        self.back_status = False
        self.config = ConfigParser()
        self.phase_check = 0
        self.timer = timer.timer_count(1)
        self.config.read("data/game_variables.cfg")
        self.phase_1_load = pygame.image.load("data/office_load.jpg").convert_alpha()
        
        #the snapshot of phase 2 and 3 will be added after those phases are implemented
        #these are just placeholders
        self.phase_2_load = pygame.image.load("data/tablet_load.png").convert_alpha()
        self.phase_3_load = pygame.image.load("data/office_load.jpg").convert_alpha()
        
        
        self.exit_button = pygame.image.load("data/back_button_guide.png").convert_alpha()
        self.phases_font = pygame.font.Font("data/arial.TTF",30)
        self.load_font = pygame.font.Font("data/animation.TTF",50)
        self.load_title = self.load_font.render("Saved Games",False,"Orange")
        self.warn_text = pygame.image.load("data/warn.png").convert_alpha()
        
        self.phase_1_option = self.phases_font.render("Load Phase 1",True,"White")
        self.phase_2_option = self.phases_font.render("Load Phase 2",True,"White")
        self.phase_3_option = self.phases_font.render("Load Phase 3",True,"White")
        #self.phase_2_load = pygame.image.load("data/office_2.png").convert_alpha()
        #self.phase_2_load = pygame.image.load("data/office_2.png").convert_alpha()
        self.load_activate = True
        
    def run_loading(self):
        while self.load_activate:
            self.screen.fill("#48dcff")
            self.screen.blit(self.load_title,(230,10))
            self.phase_1_load_rect = self.screen.blit(self.phase_1_load,(540,80))
            self.phase_2_load_rect = self.screen.blit(self.phase_2_load,(540,230))
            self.phase_3_load_rect = self.screen.blit(self.phase_3_load,(540,380))
            self.exit_button_rect = self.screen.blit(self.exit_button,(10,10))
            self.screen.blit(self.phase_1_option,(200,110))
            self.screen.blit(self.phase_2_option,(200,260))
            self.screen.blit(self.phase_3_option,(200,410))
            self.phase_check = int(self.config.get("saved_session","phase"))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(settings(self.screen,self.sound).get_volume())
                        pygame.mixer.Channel(0).play(self.sound)
                        self.back_status = True
                        self.load_activate = False
                    if self.phase_1_load_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(settings(self.screen,self.sound).get_volume())
                        pygame.mixer.Channel(0).play(self.sound)
                        if self.phase_check < 1:
                            self.display_error_message()
                        else: 
                            self.phase = 1
                            self.load_activate = False
                    if self.phase_2_load_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(settings(self.screen,self.sound).get_volume())
                        pygame.mixer.Channel(0).play(self.sound)
                        if self.phase_check < 2:
                            self.display_error_message()
                        else: 
                            self.phase = 2
                            self.load_activate = False
    
    def get_startup_status(self):
        status = self.config.get("saved_session","startup")
        if status == "True":
            return True
        return False
    
    def get_bigtech_status(self):
        status = self.config.get("saved_session","bigtech")
        if status == "True":
            return True
        return False
    
    def get_initial_budget(self):
        return int(self.config.get("saved_session","initial_budget"))
    
    def get_current_budget(self):
        return int(self.config.get("saved_session","money"))

    def get_phase(self):
        return self.phase
    
    def get_back_status(self):
        return self.back_status
    
    def get_level(self):
        return self.config.get("saved_session","level")

    def get_salary(self):
        return self.config.get("saved_session","pay")
    
    def get_skills(self):
        return self.config.get("saved_session","skills")

    def get_num_app(self):
        return self.config.get("saved_session","num_app")
    
    def get_finalist_name(self,index):
        return self.config.get(f"finalist_{index}","name")
    
    def get_finalist_skills(self,index):
        return self.config.get(f"finalist_{index}","skills")

    def get_finalist_exp(self,index):
        return self.config.get(f"finalist_{index}","exp")
    
    def get_finalist_character(self,index):
        return self.config.get(f"finalist_{index}","character")
        
    def display_error_message(self):
        #display an error whenever an unavailable game session is chosen
        warn_rect = self.screen.blit(self.warn_text,(270,150))
        pygame.display.update(warn_rect)
        self.timer.start_timer()
        