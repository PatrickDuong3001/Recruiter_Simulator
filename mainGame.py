import pygame
import os
import sys
import configparser
import argparse

#config = configparser.ConfigParser()
#config.read("data/game_variables.ini")

WIDTH = 900
HEIGHT = 500
FPS = 60
pygame.init()
speed = pygame.time.Clock()

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
ingame_song = pygame.mixer.Sound("data/ingame_song.mp3")
ingame_song.set_volume(0.1)

#start game screen setup
start_image = pygame.image.load("data/start_screen.png").convert()
start_screen = True
start_button = pygame.image.load("data/start_button.png").convert_alpha()
guide_button = pygame.image.load("data/guide_button.png").convert_alpha()
setting_button = pygame.image.load("data/setting_button.png").convert_alpha()
info = pygame.font.Font("data/arial.TTF",15)
name = info.render("Patrick & Quan",False,"White")
title_start = pygame.font.Font("data/animation.TTF",40)
title = title_start.render("Recruiter Simulator",False,"#48dcff")

#choose mode screen set up
startup_image = pygame.image.load("data/pingpong.jpg").convert_alpha()
big_tect_image = pygame.image.load("data/big_tech.jpg").convert_alpha()
title_mode = pygame.font.Font("data/animation.TTF",48)
title_mode_screen = title_mode.render("Choose Your Company!",False,"White")
startup_bigtech_font = pygame.font.Font("data/animation.TTF",25)
startup_text = startup_bigtech_font.render("Start-Up",False,"White")
bigtech_text = startup_bigtech_font.render("Big Tech",False,"White")
bigtech_money = pygame.image.load("data/big_stack.png")
startup_money = pygame.image.load("data/small_stack.png")
budget_font = pygame.font.Font("data/animation.TTF",16)
budget_text_bigtech = budget_font.render("Budget: 250,000",False,"White")
budget_text_startup = budget_font.render("Budget: 85,000",False,"White")
inputed = False
user_font = pygame.font.Font("data/arial.TTF",20)
user_text = ''
input_window = pygame.Rect(450,423,140,32)
user_require_font = pygame.font.Font("data/animation.TTF",20)
user_require = user_require_font.render("Name: ",False,"White")
message_font = pygame.font.Font("data/arial.TTF",20)
message = message_font.render("The company only allows you to work after knowing your name!",True,"White")

#ingame screen setup, phase 1
ingame = False
startup_thread = False
bigtech_thread = False
start_up_environment = pygame.image.load("data/office.png")
big_tech_environment = pygame.image.load("data/office_2.png")


#control panel
game_activate = False
game_run = True

while game_run:    #game_loop    
    while start_screen == True:

        screen.blit(start_image,(0,0))
        start_button_rect = screen.blit(start_button,(300,80))
        guide_button_rect = screen.blit(guide_button,(450,80))
        setting_button_rect = screen.blit(setting_button,(850,450))
        
        screen.blit(name,(310,470))
        screen.blit(title,(160,20))
        
        pygame.display.update()
        intro_song.play(-1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    #quit game
                sys.exit()
            if event.type  == pygame.MOUSEBUTTONDOWN:       #all click event happens here
                if start_button_rect.collidepoint(event.pos):     #click on Start button
                    start_screen = False
                    game_activate = True
                elif guide_button_rect.collidepoint(event.pos):   #click in Guide button
                    print("Hello")
                    pygame.quit()    #quit game
                    sys.exit()
                elif setting_button_rect.collidepoint(event.pos):
                    print("Hello")
                    pygame.quit()    #quit game
                    sys.exit()
    while game_activate:        
        screen.fill("#48dcff")
        startup_rect= screen.blit(startup_image,(175,165))
        bigtech_rect = screen.blit(big_tect_image,(475,165))
        pygame.draw.rect(screen,pygame.Color("#ADD8E6"),input_window)
        screen.blit(user_require,(360,430))
        screen.blit(title_mode_screen,(65,40))
        screen.blit(startup_text,(220,120))
        screen.blit(bigtech_text,(520,120))
        screen.blit(bigtech_money,(675,360))
        screen.blit(budget_text_bigtech,(480,380))
        screen.blit(budget_text_startup,(190,380))
        screen.blit(startup_money,(370,370))
        screen.blit(message,(170,475))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    #quit game
                sys.exit()                
            if event.type  == pygame.MOUSEBUTTONDOWN:       #all click event happens here
                inputed = False
                if startup_rect.collidepoint(event.pos):     #click on Start button
                    if len(user_text) != 0:
                        game_activate = False
                        ingame = True
                        startup_thread = True
                elif bigtech_rect.collidepoint(event.pos):   #click in Guide button
                    if len(user_text) == 0:
                        pass
                    else:  
                        game_activate = False
                        ingame = True
                        bigtech_thread = True
                elif input_window.collidepoint(event.pos):
                    inputed = True
                    
            if event.type == pygame.KEYDOWN:
                if inputed == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    if len(user_text) == 13:
                        inputed = False
        pygame.draw.rect(screen,pygame.Color("#ADD8E6"),input_window)
        text_surface = user_font.render(user_text,True,(255,255,255))
        input_window.w = max(100,text_surface.get_width()+5)
        screen.blit(text_surface,(input_window.x + 5, input_window.y + 5))
        pygame.display.update(input_window)
                        
    while ingame:
        intro_song.stop()
        ingame_song.play(-1)        
        
        if startup_thread == True: 
            screen.blit(start_up_environment,(0,0))
            pygame.display.update()
        elif bigtech_thread == True:
            screen.blit(big_tech_environment,(0,0))
            pygame.display.update()
            
            
    speed.tick(FPS)
            
