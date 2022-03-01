import pygame
import sys
from timer import timer_count
from setting_menu import settings

class fast_forward_animation(pygame.sprite.Sprite):
    def __init__(self,scr,snd,eff):
        super().__init__()
        self.screen = scr
        self.sound = snd       
        self.effect = eff
        self.control = settings(self.screen,self.sound)
        self.pos_x = -200
        self.fast_arrow = pygame.image.load("data/forward.png").convert_alpha()
        self.forward_font = pygame.font.Font("data/animation.TTF",55)
        self.forward_title = self.forward_font.render("Fast-forward >>>",False,"White")
        self.announce = self.forward_font.render("3 weeks later...",False,"White")
        
    def redraw(self,pos_x):
        self.screen.blit(self.fast_arrow,(pos_x,150))
    
    def run_fast_forward(self):
        if self.control.get_music_status() == False: 
            self.sound.set_volume(0.1)
            self.effect.set_volume(0.1)
        else: 
            self.sound.set_volume(0)
            self.effect.set_volume(0)
            
        start_timer = pygame.time.get_ticks() 
        self.sound.play(-1)
        while True: 
            dur = (pygame.time.get_ticks()-start_timer)/1000  #duration in seconds
            self.screen.fill("Black")
            self.screen.blit(self.forward_title,(120,20))
            self.redraw(self.pos_x)
            self.pos_x += 0.12
            pygame.display.update()
            if dur > 6:
                self.sound.stop()
                self.kill()
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
        self.screen.fill("Black")
        pygame.display.update()
        timer_count(2).start_timer()
        self.effect.play()
        self.screen.blit(self.announce,(130,160))
        pygame.display.update()
        timer_count(2).start_timer()
        self.screen.fill("Black")
        pygame.display.update()
        timer_count(2).start_timer()
            
        