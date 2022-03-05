import pygame
import sys
from setting_menu import settings
from configparser import ConfigParser
from timer import timer_count

class fast_forward_animation_2(pygame.sprite.Sprite):
    def __init__(self,scr,clk,fast,eff):
        super().__init__()
        self.screen = scr
        self.click = clk  
        self.fast_clock = fast
        self.effect = eff
        self.control = settings(self.screen,self.click)
        
        self.config = ConfigParser()
        self.config.read("data/game_variables.cfg")
        self.startup_status = self.config.get("saved_session","startup")
        self.bigtech_status = self.config.get("saved_session","bigtech")
        
        self.tablet_swipe = pygame.image.load("data/tablet_swipe.png").convert_alpha()
        self.pos_y_tab = -15
                
        self.fast_arrow = pygame.image.load("data/forward.png").convert_alpha()
        self.forward_font = pygame.font.Font("data/animation.TTF",50)
        self.forward_title = self.forward_font.render("Fast-forward >>>",False,"White")
        self.announce = self.forward_font.render("1 eternity later...",False,"White")
        self.pos_x_arrow = -200
        
        self.office_1 =  pygame.image.load("data/office.png").convert_alpha()
        self.office_2 =  pygame.image.load("data/office_2.jpg").convert_alpha()
        self.setting = pygame.image.load("data/setting_button.png").convert_alpha()
        self.bubble = pygame.image.load("data/bubble_3.png").convert_alpha()
        
        self.thought_font = pygame.font.Font("data/arial.TTF",25)
        self.thought_1 = self.thought_font.render("Finally done!",True,"Black")
        self.thought_2 = self.thought_font.render("That's all for today",True,"Black")
        self.thought_3 = self.thought_font.render("Let's invite them to interviews",True,"Black")
        self.thought_4 = self.thought_font.render("when I feel like talking to them",True,"Black")

    def redraw_arr(self,pos_x):
        self.screen.blit(self.fast_arrow,(pos_x,150))
        
    def run_fast_forward_2(self):
        forward_active = True
        wait_active = True
        tablet_move = True
        bubble_active = False
        bubble_2_active = True
        fast_forward_active = False
        switch_screen = False
        
        if self.control.get_music_status() == False: 
            self.fast_clock.set_volume(0.1)
            self.effect.set_volume(0.1)
        else: 
            self.fast_clock.set_volume(0)
            self.effect.set_volume(0)
            
        while forward_active:
            
            while tablet_move:
                
                if self.startup_status == "True" and self.bigtech_status == "False":
                    self.screen.blit(self.office_1,(0,0))
                elif self.startup_status == "False" and self.bigtech_status == "True":
                    self.screen.blit(self.office_2,(0,0))
                    
                self.screen.blit(self.tablet_swipe,(0,self.pos_y_tab))
                self.screen.blit(self.setting,(850,10))
                
                if wait_active:
                    timer_count(1).start_timer()
                    wait_active = False
                
                self.pos_y_tab += 0.1   
                pygame.display.update()
                
                if int(self.pos_y_tab) == 500:
                    tablet_move = False
                    bubble_active = True
                    self.kill()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()    #quit game
                        sys.exit()
                        
            while bubble_active:
                if self.startup_status == "True" and self.bigtech_status == "False":
                    self.screen.blit(self.office_1,(0,0))
                elif self.startup_status == "False" and self.bigtech_status == "True":
                    self.screen.blit(self.office_2,(0,0))
                
                self.bubble_rect = self.screen.blit(self.bubble,(230,0))
                self.screen.blit(self.thought_1,(390,100))
                self.screen.blit(self.thought_2,(370,170))
                self.control_rect = self.screen.blit(self.setting,(850,10))
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()    #quit game
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.control_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(self.control.get_volume())
                            pygame.mixer.Channel(0).play(self.click)
                            self.control.run_setting()
                        elif self.bubble_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(self.control.get_volume())
                            pygame.mixer.Channel(0).play(self.click)
                            
                            while bubble_2_active:
                                self.bubble_rect_2 = self.screen.blit(self.bubble,(230,0))
                                self.screen.blit(self.thought_3,(300,100))
                                self.screen.blit(self.thought_4,(300,170))
                                pygame.display.update()
                               
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()    #quit game
                                        sys.exit()
                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                        if self.bubble_rect_2.collidepoint(event.pos):
                                            pygame.mixer.Channel(0).set_volume(self.control.get_volume())
                                            pygame.mixer.Channel(0).play(self.click)
                                            bubble_2_active = False
                                            bubble_active = False
                                            fast_forward_active = True
                                            start_timer = pygame.time.get_ticks() 
                                            self.fast_clock.play(-1)    
                                        elif self.control_rect.collidepoint(event.pos):
                                            pygame.mixer.Channel(0).set_volume(self.control.get_volume())
                                            pygame.mixer.Channel(0).play(self.click)
                                            self.control.run_setting()   
                                            if self.startup_status == "True" and self.bigtech_status == "False":
                                                self.screen.blit(self.office_1,(0,0))
                                            elif self.startup_status == "False" and self.bigtech_status == "True":
                                                self.screen.blit(self.office_2,(0,0))  
                                            self.screen.blit(self.setting,(850,10))
                                                                              
            while fast_forward_active:
                if self.control.get_music_status() == False: 
                    self.fast_clock.set_volume(0.1)
                    self.effect.set_volume(0.1)
                else: 
                    self.fast_clock.set_volume(0)
                    self.effect.set_volume(0)
                    
                dur = (pygame.time.get_ticks()-start_timer)/1000  #duration in seconds
                self.screen.fill("Black")
                self.screen.blit(self.forward_title,(140,20))
                self.redraw_arr(self.pos_x_arrow)
                self.pos_x_arrow += 0.12
                pygame.display.update()
                
                if dur > 5:
                    self.fast_clock.stop()
                    self.kill()
                    switch_screen = True
                    fast_forward_active = False
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()    #quit game
                        sys.exit()                
            
            while switch_screen: 
                self.screen.fill("Black")
                pygame.display.update()
                timer_count(2).start_timer()
                self.effect.play()
                self.screen.blit(self.announce,(120,160))
                pygame.display.update()
                timer_count(2).start_timer()
                self.screen.fill("Black")
                pygame.display.update()
                timer_count(2).start_timer()
                switch_screen = False
                forward_active = False
            
            