import pygame
import sys

music_status = [False]
sfx_status  = [False]
volume = [0.8]

class settings():
    '''
    this class will handle all the setting choices made by the users
    '''
    def __init__(self,scr,snd):   
        super().__init__()
        self.screen = scr
        self.sound = snd
        self.music = pygame.image.load("data/music.png").convert_alpha()
        self.music_dis = pygame.image.load("data/music_disabled.png").convert_alpha()
        self.sfx = pygame.image.load("data/sfx.png").convert_alpha()
        self.sfx_dis = pygame.image.load("data/sfx_disabled.png").convert_alpha()
        self.title_font = pygame.font.Font("data/animation.TTF",50)
        self.title = self.title_font.render("Settings",False,"White")
        self.common_font = pygame.font.Font("data/animation.TTF",25)
        self.exit = self.common_font.render("Exit",False,"White")
        self.music_title = self.common_font.render("Music:",False,"White")
        self.sfx_title = self.common_font.render("SFX:",False,"White")
        self.music_rect = None
        self.sfx_rect = None
        self.music_disable = music_status[0]
        self.sfx_disable = sfx_status[0]
        self.setting_run = True
        self.volume_channel = volume[0]
            
    def run_setting(self):
        while self.setting_run:
            self.screen.fill("#48dcff")
            self.screen.blit(self.title,(290,10))
            self.screen.blit(self.music_title,(350,150))
            self.screen.blit(self.sfx_title,(380,250))
            self.exit_rect = self.screen.blit(self.exit,(400,350))
            #self.music_dis_rect = self.screen.blit(self.music_dis,(470,140))
            #self.sfx_dis_rect = self.screen.blit(self.sfx_dis,(470,180))
            
            if self.music_disable:
                self.music_rect = self.screen.blit(self.music_dis,(470,140))
            else: 
                self.music_rect = self.screen.blit(self.music,(470,140))
            
            if self.sfx_disable:
                self.sfx_rect = self.screen.blit(self.sfx_dis,(470,240))
            else: 
                self.sfx_rect = self.screen.blit(self.sfx,(470,240))
                            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music_rect.collidepoint(event.pos):
                        if self.music_disable == False:
                            self.music_disable = True
                            music_status[0] = self.music_disable
                            self.sound.set_volume(0)
                        else:
                            self.music_disable = False
                            music_status[0] = self.music_disable
                            self.sound.set_volume(0.1)
                    elif self.sfx_rect.collidepoint(event.pos):
                        if self.sfx_disable == False:
                            self.sfx_disable = True 
                            sfx_status[0] = self.sfx_disable
                            self.volume_channel = 0
                            volume[0] = self.volume_channel
                        else:
                            self.sfx_disable = False
                            sfx_status[0] = self.sfx_disable
                            self.volume_channel = 0.5
                            volume[0] = self.volume_channel
                    elif self.exit_rect.collidepoint(event.pos):
                        self.setting_run = False
                        
    def get_volume(self):
        return self.volume_channel
    
    def get_music_status(self):
        return music_status[0]
    
    def get_sfx_status(self):
        return sfx_status[0]
                                               
    