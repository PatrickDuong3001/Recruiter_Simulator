import pygame
import sys
from configparser import ConfigParser

class tablet_animation():
    def __init__(self,scr,snd): 
        super().__init__()
        self.screen = scr
        self.sound = snd   
        
        self.config = ConfigParser()
        self.config.read("data/game_variables.cfg")
        self.startup_status = self.config.get("saved_session","startup")
        self.bigtech_status = self.config.get("saved_session","bigtech") 
        
        self.pos_y = 500
        self.tablet = pygame.image.load("data/tablet_linked.png").convert_alpha()
        self.office_1 =  pygame.image.load("data/office.png").convert_alpha()
        self.office_2 =  pygame.image.load("data/office_2.jpg").convert_alpha()
        self.setting = pygame.image.load("data/setting_button.png").convert_alpha()
                
    def tablet_move(self):
        while True: 
            if self.startup_status == "True" and self.bigtech_status == "False":
                self.screen.blit(self.office_1,(0,0))
            elif self.startup_status == "False" and self.bigtech_status == "True":
                self.screen.blit(self.office_2,(0,0))
                
            self.screen.blit(self.setting,(850,10))
            self.screen.blit(self.tablet,(0,self.pos_y))
            self.pos_y -= 0.1
            pygame.display.update()
            if int(self.pos_y) == -15:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()