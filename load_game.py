from configparser import ConfigParser
import pygame
import sys

class game_loading():
    '''
    this class helps load saved game
    '''
    def __init__(self,scr):  
        super().__init__()
        self.screen = scr
        self.config = ConfigParser()
        self.config.read("data/game_variables.cfg")
        self.phase_1_load = pygame.image.load("data/office_load.png").convert_alpha()
        self.phases_font = pygame.font.Font("data/arial.TTF",30)
        self.load_font = pygame.font.Font("data/arial.TTF",50)
        self.load_title = self.load_font.render("Saved Games",True,"Yellow")
        
        self.phase_1_option = self.phases_font.render("Load Phase 1",True,"White")
        self.phase_2_option = self.phases_font.render("Load Phase 2",True,"White")
        self.phase_3_option = self.phases_font.render("Load Phase 3",True,"White")
        #self.phase_2_load = pygame.image.load("data/office_2.png").convert_alpha()
        #self.phase_2_load = pygame.image.load("data/office_2.png").convert_alpha()
        self.load_activate = True
        
    def run_loading(self):
        while self.load_activate:
            self.screen.fill("#48dcff")
            self.phase_1_load_rect = self.screen.blit(self.phase_1_load,(300,80))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
    
    