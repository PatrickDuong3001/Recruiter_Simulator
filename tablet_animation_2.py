import pygame
import sys
from configparser import ConfigParser
from load_game import game_loading
from timer import timer_count
from setting_menu import settings

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
        self.office_1_near = pygame.image.load("data/desk_2.jpg").convert_alpha()
        self.office_2_near = pygame.image.load("data/desk_1.jpg").convert_alpha()
        self.setting = pygame.image.load("data/setting_button.png").convert_alpha()
        self.begin = pygame.image.load("data/begin_interview.png").convert_alpha()
        
        self.title_font = pygame.font.Font("data/arial.TTF",20)
        self.text_font = pygame.font.Font("data/arial.TTF",17)
        
        self.tablet_active = True
        self.review_profile = False
    
    def redraw_screen(self):
        if self.startup_status == "True" and self.bigtech_status == "False":
            self.screen.blit(self.office_1,(0,0))
        elif self.startup_status == "False" and self.bigtech_status == "True":
            self.screen.blit(self.office_2,(0,0))
        self.screen.blit(self.setting,(850,10))
    
    def fadeout_screen(self,width,height):
        '''
        fadeout effect for the game screen
        '''
        fade = pygame.Surface((width,height))
        fade.fill((0,0,0))
        for alpha in range(0,300):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
                    
            fade.set_alpha(alpha)
            self.redraw_screen()
            self.screen.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(5)
        timer_count(1).start_timer()
            

    def tablet_move(self):
        tablet_still = True
        tablet_move = True
        title_text = self.title_font.render(f"Candidate {self.candidate_no}",True,"Black")
        name_text = self.text_font.render(f"{self.load.get_finalist_name(1)}",True,"Black")
        skill_text = self.text_font.render(f"{self.load.get_finalist_skills(1)}",True,"Black")
        char_text = self.text_font.render(f"{self.load.get_finalist_character(1)}",True,"Black")
        exp_text = self.text_font.render(f"{self.load.get_finalist_exp(1)}",True,"Black")
        
        while tablet_still:
            control = settings(self.screen,self.sound)
            
            if self.startup_status == "True" and self.bigtech_status == "False":
                self.screen.blit(self.office_1_near,(0,0))
            elif self.startup_status == "False" and self.bigtech_status == "True":
                self.screen.blit(self.office_2_near,(0,0))
                
            self.screen.blit(self.setting,(850,10))
            self.screen.blit(self.tablet,(0,self.pos_y))
            self.screen.blit(title_text,(410,110))
            self.screen.blit(name_text,(280,158))
            self.screen.blit(skill_text,(270,220))
            self.screen.blit(char_text,(330,288))
            self.screen.blit(exp_text,(335,358))
            begin_rect = self.screen.blit(self.begin,(400,20))
            setting_rect = self.screen.blit(self.setting,(850,10))
            pygame.display.update() 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if setting_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(control.get_volume())
                        pygame.mixer.Channel(0).play(self.sound)
                        control.run_setting()
                    elif begin_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(control.get_volume())
                        pygame.mixer.Channel(0).play(self.sound)
                        tablet_still = False
                
        while tablet_move:
            if self.startup_status == "True" and self.bigtech_status == "False":
                self.screen.blit(self.office_1_near,(0,0))
            elif self.startup_status == "False" and self.bigtech_status == "True":
                self.screen.blit(self.office_2_near,(0,0))
                
            self.screen.blit(self.setting,(850,10))
            self.screen.blit(self.tablet,(0,self.pos_y))
            self.pos_y += 0.1
            pygame.display.update()
            
            if int(self.pos_y)  == 500:
                self.kill()
                tablet_move = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
                                           
    
        
        