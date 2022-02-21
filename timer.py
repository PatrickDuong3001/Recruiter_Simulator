import pygame

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
            sec=(pygame.time.get_ticks()-start_ticks)/1000 
            if sec == self.dur:
                break