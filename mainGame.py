import pygame
import os
import sys

WIDTH = 900
HEIGHT = 500
pygame.init()

#game variables initiate
budget = 0
years_of_experience = 0
pay_type = [0,1,2,3]      #will influence number of job apps
job_type = [0,1,2]
evil_score = 0

#screen window setup
pygame.display.set_caption('Become a Recruiter')  #set the title for the game
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #create the game screen

#all songs
intro_song = pygame.mixer.Sound("data/intro_song.mp3")
intro_song.set_volume(0.1)

#start game screen setup
start_image = pygame.image.load("data/start_screen.png").convert()
start_screen = True
start_button = pygame.image.load("data/start_button.png").convert_alpha()
guide_button = pygame.image.load("data/guide_button.png").convert_alpha()
setting_button = pygame.image.load("data/setting_button.png").convert_alpha()
info = pygame.font.Font("data/arial.TTF",15)
name = info.render("Patrick & Quan",False,"White")
title_start = pygame.font.Font("data/arial.TTF",50)
title = title_start.render("Recruiter Simulator",False,"#48dcff")

#main game screen set up


#control panel
game_activate = False
game_run = True

while game_run:    #game_loop    
    while start_screen == True:
        pos = pygame.mouse.get_pos()

        screen.blit(start_image,(0,0))
        start_button_rect = screen.blit(start_button,(300,80))
        guide_button_rect = screen.blit(guide_button,(450,80))
        setting_button_rect = screen.blit(setting_button,(850,450))
        
        screen.blit(name,(310,470))
        screen.blit(title,(230,0))
        
        pygame.display.update()
        intro_song.play(-1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    #quit game
                sys.exit()
            if event.type  == pygame.MOUSEBUTTONDOWN:       #all click event happens here
                if start_button_rect.collidepoint(pos):     #click on Start button
                    start_screen = False
                    game_activate = True
                elif guide_button_rect.collidepoint(pos):   #click in Guide button
                    print("Hello")
                    pygame.quit()    #quit game
                    sys.exit()
                elif setting_button_rect.collidepoint(pos):
                    print("Hello")
                    pygame.quit()    #quit game
                    sys.exit()
    while game_activate:
        pos = pygame.mouse.get_pos()

