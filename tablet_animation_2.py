import pygame
import sys
from configparser import ConfigParser
from load_game import game_loading

class tablet_animator(pygame.sprite.Sprite):
    def __init__(self,scr,snd,can_no): 
        super().__init__()
        self.screen = scr
        self.sound = snd  
        self.candidate_no = can_no
        
        self.config = ConfigParser()
        self.config.read("data/game_variables.cfg")
        self.startup_status = self.config.get("saved_session","startup")
        self.bigtech_status = self.config.get("saved_session","bigtech") 
        
        self.load = game_loading(self.screen,self.sound)
        
        self.pos_y = -15
        self.tablet = pygame.image.load("data/tablet_swipe.png").convert_alpha()
        self.office_1 =  pygame.image.load("data/office.png").convert_alpha()
        self.office_2 =  pygame.image.load("data/office_2.jpg").convert_alpha()
        self.setting = pygame.image.load("data/setting_button.png").convert_alpha()
        
        self.title_font = pygame.font.Font("data/arial.TTF",20)
        self.text_font = pygame.font.Font("data/arial.TTF",17)
        
        self.tablet_active = True
        self.review_profile = False
    
    def tablet_move(self):
        move_down = False
        while self.tablet_active:
            if self.startup_status == "True" and self.bigtech_status == "False":
                self.screen.blit(self.office_1,(0,0))
            elif self.startup_status == "False" and self.bigtech_status == "True":
                self.screen.blit(self.office_2,(0,0))
                
            self.screen.blit(self.setting,(850,10))
            self.screen.blit(self.tablet,(0,self.pos_y))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
            
            while move_down: 
                self.screen.blit(self.setting,(850,10))
                self.screen.blit(self.tablet,(0,self.pos_y))
                self.pos_y += 0.1
                
                pygame.display.update()
            
                if int(self.pos_y)  == 500:
                    self.kill()
                    move_down = False
                    self.tablet_active = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()    #quit game
                        sys.exit()
                                           
    
        
        