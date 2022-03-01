import pygame
import sys
from timer import timer_count
from setting_menu import settings

class warn_countdowner():
    def __init__(self,scr,snd):  
        super().__init__()
        self.screen = scr
        self.song = snd
        self.setting = settings(self.screen,self.song)
        
        self.sound_1 = pygame.mixer.Sound("data/countdown_1.mp3")
        self.sound_2 = pygame.mixer.Sound("data/countdown_2.mp3")
        
        self.warn_1 = pygame.image.load("data/warn_1.png").convert_alpha()
        self.warn_2 = pygame.image.load("data/warn_2.png").convert_alpha()
        self.warn_3 = pygame.image.load("data/warn_3.png").convert_alpha()
        self.warn_4 = pygame.image.load("data/warn_4.png").convert_alpha()
        self.warn_5 = pygame.image.load("data/warn_5.png").convert_alpha()
        self.warn_6 = pygame.image.load("data/warn_6.png").convert_alpha()
        self.active = True
        #270,250
        
    def start_warn_counter(self):
        while self.active:
            warn_rect = self.screen.blit(self.warn_1,(290,200))
            pygame.display.update(warn_rect)
            timer_count(3).start_timer()
            
            self.screen.blit(self.warn_2,(290,200))
            pygame.display.update(warn_rect)
            timer_count(3).start_timer()
            
            pygame.mixer.Channel(1).set_volume(self.setting.get_volume())
            pygame.mixer.Channel(1).play(self.sound_1)
            self.screen.blit(self.warn_3,(290,200))
            pygame.display.update(warn_rect)
            timer_count(1).start_timer()
            
            pygame.mixer.Channel(1).set_volume(self.setting.get_volume())
            pygame.mixer.Channel(1).play(self.sound_1)
            self.screen.blit(self.warn_4,(290,200))
            pygame.display.update(warn_rect)
            timer_count(1).start_timer()
            
            pygame.mixer.Channel(1).set_volume(self.setting.get_volume())
            pygame.mixer.Channel(1).play(self.sound_1)
            self.screen.blit(self.warn_5,(290,200))
            pygame.display.update(warn_rect)
            timer_count(1).start_timer()
            
            pygame.mixer.Channel(1).set_volume(self.setting.get_volume())
            pygame.mixer.Channel(1).play(self.sound_2)
            self.screen.blit(self.warn_6,(290,200))
            pygame.display.update(warn_rect)
            timer_count(1).start_timer()
            self.active = False
            
            
            
            
            