import pygame
import sys

class timer_count():
    '''
    this class used for game pause screen
    '''
    def __init__(self,duration):   
        super().__init__()
        self.dur = duration
    
    def start_timer(self):
        start_ticks=pygame.time.get_ticks()
        while True: # mainloop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()

            sec=(pygame.time.get_ticks()-start_ticks)/1000 
            if sec == self.dur:
                break