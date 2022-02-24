import pygame
import sys
import config_file_writer
from setting_menu import settings
from timer import timer_count
from game_engine import num_applicant_generator

#initiate pygame session
WIDTH = 900
HEIGHT = 500
FPS = 60
pygame.init()
speed = pygame.time.Clock()
config_writer = config_file_writer.config_write()

#game variables initiate
#may need resetting when the game ends
budget = 0
years_of_experience = None
pay_type = None #[0,1,2,3]      #will influence number of job apps
job_type = None #[0,1,2]
required_skills = []
evil_score = 0              #evil score will affect the final score and dialogue choice during the interviews
num_app = 0                 #number of applicants

#screen window setup
pygame.display.set_caption('Become a Recruiter')  #set the title for the game
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #create the game screen

#all songs
intro_song = pygame.mixer.Sound("data/intro_song.mp3")
intro_song.set_volume(0.1)
ingame_song = pygame.mixer.Sound("data/ingame_song.mp3")
ingame_song.set_volume(0.1)

#all sound effects:
click_sound = pygame.mixer.Sound("data/click_effect.mp3")

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
startup_thread = False
bigtech_thread = False
start_up_environment = pygame.image.load("data/office.png")
big_tech_environment = pygame.image.load("data/office_2.jpg")
thought_1 = pygame.image.load("data/bubble_1.png").convert_alpha()
text_phase_1_font = pygame.font.Font("data/arial.TTF",20)
text_phase_1 = text_phase_1_font.render("So, this is my INNOVATIVE office!",True,"Black")
text_phase_1_1 = text_phase_1_font.render("Amazing!",True,"Black")
text_message_font = pygame.font.Font("data/arial.TTF",10)
text_message_phase_1 = text_message_font.render("click here",True,"Black")
text_phase_1_2 = text_phase_1_font.render("Let's recruit a ROCKSTAR employee!",True,"Black")
text_phase_1_3 = text_phase_1_font.render("Now, post a job on LinkedOut.",True,"Black")
bigtech_computer_rect = pygame.Rect(495,230,180,110)
instr_bubble = pygame.image.load("data/instruction_bubble.png").convert_alpha()
linkedout_ins = pygame.font.Font("data/arial.TTF",15).render("LinkedOut",True,"Black")
computer_screen = pygame.image.load("data/desktop_linked.png").convert_alpha()
desk_zoom_in_1 = pygame.image.load("data/desk_1.jpg").convert_alpha()
desk_zoom_in_2 = pygame.image.load("data/desk_2.jpg").convert_alpha()
exit_icon = pygame.image.load("data/exit_icon.png").convert_alpha()
post_button = pygame.image.load("data/post.png").convert_alpha()
desktop_blank = pygame.image.load("data/desktop_blank.png").convert_alpha()
desktop_white = pygame.image.load("data/desktop_white.png").convert_alpha()
back_button = pygame.image.load("data/back_button.png").convert_alpha()

#choose job types and salary set up
intern_button = pygame.image.load("data/intern.png").convert_alpha()
intern_unpaid = pygame.image.load("data/unpaid_intern.png").convert_alpha()
intern_lowpaid = pygame.image.load("data/low_paid_intern.png").convert_alpha()
intern_highpaid = pygame.image.load("data/high_paid_intern.png").convert_alpha()
mid_button = pygame.image.load("data/mid.png").convert_alpha()
senior_button = pygame.image.load("data/senior.png").convert_alpha()
desktop_intern = pygame.image.load("data/desktop_intern.png").convert_alpha()
intern_year_0 = pygame.image.load("data/0_year.png").convert_alpha()
intern_year_1_4 = pygame.image.load("data/1_4_year.png").convert_alpha()
intern_year_4 = pygame.image.load("data/4_year.png").convert_alpha()
c = pygame.image.load("data/c.png").convert_alpha()
css = pygame.image.load("data/css.png").convert_alpha()
html = pygame.image.load("data/html.png").convert_alpha()
java = pygame.image.load("data/java.png").convert_alpha()
jvs = pygame.image.load("data/jvs.png").convert_alpha()
mongo = pygame.image.load("data/mongo.png").convert_alpha()
python = pygame.image.load("data/python.png").convert_alpha()
vhdl = pygame.image.load("data/vhdl.png").convert_alpha()
intern_unpaid_shade = pygame.image.load("data/unpaid_intern_shade.png").convert_alpha()
intern_low_shade = pygame.image.load("data/low_paid_intern_shade.png").convert_alpha()
intern_high_shade = pygame.image.load("data/high_paid_intern_shade.png").convert_alpha()
exp_0_shade = pygame.image.load("data/0_year_shade.png").convert_alpha()
exp_1_4_shade = pygame.image.load("data/1_4_year_shade.png").convert_alpha()
exp_4_shade = pygame.image.load("data/4_year_shade.png").convert_alpha()
c_shade = pygame.image.load("data/c_shade.png").convert_alpha()
css_shade = pygame.image.load("data/css_shade.png").convert_alpha()
html_shade = pygame.image.load("data/html_shade.png").convert_alpha()
java_shade = pygame.image.load("data/java_shade.png").convert_alpha()
jvs_shade = pygame.image.load("data/jvs_shade.png").convert_alpha()
mongo_shade = pygame.image.load("data/mongo_shade.png").convert_alpha()
python_shade = pygame.image.load("data/python_shade.png").convert_alpha()
vhdl_shade = pygame.image.load("data/vhdl_shade.png").convert_alpha()
submit = pygame.image.load("data/submit.png").convert_alpha()
submit_rect = submit.get_rect()

#control panels may need to be reset after game ends
#control panel phase 0
game_activate = False
game_run = True
music_active = False
phase = 0   #phase of recruitment

#control panel phase 1
bubble_1_active = True
instr_linkedout_active = False
desktop_active = False
post_transition = True
choose_position_active = False
intern_thread = False
mid_level_thread = False
senior_thread = False
white_transition = True
pay_count = False
exp_count = False
skills_count = 0
unpaid_press_intern = False
lowpaid_press_intern = False
highpaid_press_intern = False
exp_0_press = False
exp_1_4_press = False
exp_4_press = False
css_press = False
java_press = False
jvs_press = False
mongo_press = False
python_press = False
c_press = False
vhdl_press = False
html_press = False

while game_run:    #game_loop    
    while start_screen:
        setting = settings(screen,intro_song)
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
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    start_screen = False
                    game_activate = True
                elif guide_button_rect.collidepoint(event.pos):   #click in Guide button
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    print("Hello")
                    pygame.quit()    #quit game
                    sys.exit()
                elif setting_button_rect.collidepoint(event.pos):
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    setting.run_setting()                 
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
                if startup_rect.collidepoint(event.pos):   
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    if len(user_text) != 0:
                        budget = 85000  
                        config_writer.set_current_budget(budget)
                        config_writer.set_current_name(user_text)
                        game_activate = False
                        phase = 1
                        startup_thread = True
                        screen.blit(start_up_environment,(0,0))
                        screen.blit(setting_button,(850,10))
                        intro_song.fadeout(3000)
                        pygame.display.update()
                        timer_count(3).start_timer()
                        intro_song.stop()    #just in case fadeout doesn't stop music completely
                elif bigtech_rect.collidepoint(event.pos):   
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    if len(user_text) != 0:
                        budget = 250000  
                        config_writer.set_current_budget(budget)
                        config_writer.set_current_name(user_text)
                        game_activate = False
                        phase = 1
                        bigtech_thread = True
                        screen.blit(big_tech_environment,(0,0))
                        screen.blit(setting_button,(850,10))
                        intro_song.fadeout(3000)
                        pygame.display.update()
                        timer_count(3).start_timer()
                        intro_song.stop()      #just in case fadeout doesn't stop music completely
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
    
    ##########job posting phase of the game - phase 1##########
    while phase == 1:                                   
        config_writer.set_current_phase(phase)    #remember the current phase
        setting = settings(screen,ingame_song)
        ingame_song.play(-1,fade_ms=1000)
        
        if setting.get_music_status() == False: 
            ingame_song.set_volume(0.1)
        else: 
            ingame_song.set_volume(0)
        
        if startup_thread == True: 
            screen.blit(start_up_environment,(0,0))
        elif bigtech_thread == True:
            screen.blit(big_tech_environment,(0,0))
        
        if bubble_1_active:
            thought_bubble_1_rect = screen.blit(thought_1,(230,0))
            screen.blit(text_phase_1,(300,100))
            screen.blit(text_phase_1_1,(420,150))
            screen.blit(text_message_phase_1,(360,240))
            
        if instr_linkedout_active:
            screen.blit(instr_bubble,(600,170))
            screen.blit(linkedout_ins,(610,185))
            
        setting_button_rect = screen.blit(setting_button,(850,10))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    #quit game
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if setting_button_rect.collidepoint(event.pos):
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    setting.run_setting()   
                if thought_bubble_1_rect.collidepoint(event.pos) and bubble_1_active == True:
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    while bubble_1_active:
                        screen.blit(text_phase_1_2,(280,100))
                        screen.blit(text_phase_1_3,(320,150))
                        screen.blit(text_message_phase_1,(360,240))
                        pygame.display.update(thought_bubble_1_rect)
                        screen.blit(thought_1,(230,0))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()    #quit game
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if thought_bubble_1_rect.collidepoint(event.pos):
                                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                    pygame.mixer.Channel(0).play(click_sound)
                                    bubble_1_active = False
                                    instr_linkedout_active = True
                if bigtech_computer_rect.collidepoint(event.pos) and instr_linkedout_active==True:
                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                    pygame.mixer.Channel(0).play(click_sound)
                    desktop_active = True
        while desktop_active:                                             ###open laptop
            if bigtech_thread:
                screen.blit(desk_zoom_in_1,(0,0))
            elif startup_thread:
                screen.blit(desk_zoom_in_2,(0,0))
            computer_screen_rect = screen.blit(computer_screen,(150,40))
            exit_icon_rect= screen.blit(exit_icon,(682,85))
            if post_transition == False: 
                post_button_rect = screen.blit(post_button,(408,250))
            
            pygame.display.update()
            
            while post_transition:    #fancy fade in post button
                timer_count(1).start_timer()
                post_button_rect = screen.blit(post_button,(408,250))
                pygame.display.update(post_button_rect)
                post_transition = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    #quit game
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_icon_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(setting.get_volume())
                        pygame.mixer.Channel(0).play(click_sound)
                        desktop_active = False
                    if post_button_rect.collidepoint(event.pos):
                        pygame.mixer.Channel(0).set_volume(setting.get_volume())
                        pygame.mixer.Channel(0).play(click_sound)
                        choose_position_active = True
                        
            while choose_position_active:                               ###choose positions to recruit
                screen.blit(desktop_blank,(150,40))
                back_button_rect = screen.blit(back_button,(200,85))
                intern_button_rect = screen.blit(intern_button,(300,285))
                mid_button_rect = screen.blit(mid_button,(410,285))
                senior_button_rect = screen.blit(senior_button,(520,285))
                screen.blit(exit_icon,(682,85))
                pygame.display.update(computer_screen_rect)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()    #quit game
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if intern_button_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(setting.get_volume())
                            pygame.mixer.Channel(0).play(click_sound)
                            intern_thread = True
                        if mid_button_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(setting.get_volume())
                            pygame.mixer.Channel(0).play(click_sound)
                            mid_level_thread = True
                        if senior_button_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(setting.get_volume())
                            pygame.mixer.Channel(0).play(click_sound)
                            senior_thread = True
                        if back_button_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(setting.get_volume())
                            pygame.mixer.Channel(0).play(click_sound)
                            choose_position_active = False
                        if exit_icon_rect.collidepoint(event.pos):
                            pygame.mixer.Channel(0).set_volume(setting.get_volume())
                            pygame.mixer.Channel(0).play(click_sound)
                            choose_position_active = False
                            desktop_active = False
                            
                while intern_thread:                            #intern thread to set up job requirements and generate number of applicants
                    skills_count = len(required_skills)
                    screen.blit(desktop_intern,(150,40))
                    screen.blit(back_button,(200,85))
                    screen.blit(exit_icon,(682,85))
                    intern_unpaid_rect = screen.blit(intern_unpaid,(350,110))
                    intern_lowpaid_rect = screen.blit(intern_lowpaid,(450,110))
                    intern_highpaid_rect = screen.blit(intern_highpaid,(550,110))
                    intern_year_0_rect = screen.blit(intern_year_0,(350,195))
                    intern_year_1_4_rect = screen.blit(intern_year_1_4,(450,195))
                    intern_year_4_rect = screen.blit(intern_year_4,(550,195))
                    css_rect = screen.blit(css,(300,250))
                    vhdl_rect = screen.blit(vhdl,(400,250))
                    html_rect = screen.blit(html,(500,250))
                    java_rect = screen.blit(java,(600,250))
                    c_rect = screen.blit(c,(300,300))
                    jvs_rect = screen.blit(jvs,(400,300))
                    mongo_rect = screen.blit(mongo,(500,300))
                    python_rect = screen.blit(python,(600,300))
                    
                    if pay_count:
                        if unpaid_press_intern:
                            screen.blit(intern_unpaid_shade,(350,110))
                        elif lowpaid_press_intern:
                            screen.blit(intern_low_shade,(450,110))
                        elif highpaid_press_intern:
                            screen.blit(intern_high_shade,(550,110))
                    
                    if exp_count:
                        if exp_0_press:
                            screen.blit(exp_0_shade,(350,195))
                        elif exp_1_4_press:
                            screen.blit(exp_1_4_shade,(450,195))
                        elif exp_4_press:
                            screen.blit(exp_4_shade,(550,195))
                    
                    if c_press: 
                        screen.blit(c_shade,(300,300))
                    if css_press:
                        screen.blit(css_shade,(300,250))
                    if html_press:
                        screen.blit(html_shade,(500,250))
                    if java_press:
                        screen.blit(java_shade,(600,250))
                    if jvs_press:
                        screen.blit(jvs_shade,(400,300))
                    if mongo_press:
                        screen.blit(mongo_shade,(500,300))
                    if python_press:
                        screen.blit(python_shade,(600,300))
                    if vhdl_press:
                        screen.blit(vhdl_shade,(400,250))
                    if exp_count == True and pay_count == True and skills_count != 0:
                        submit_rect = screen.blit(submit,(250,85))
                        
                    pygame.display.update(computer_screen_rect)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()    #quit game
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if back_button_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                intern_thread = False
                            if exit_icon_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                intern_thread = False
                                choose_position_active = False
                                desktop_active = False
                            if intern_unpaid_rect.collidepoint(event.pos) and pay_count == False:
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                job_type = 0
                                pay_type = 0
                                pay_count = True
                                unpaid_press_intern = True
                            if intern_lowpaid_rect.collidepoint(event.pos) and pay_count == False:
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                job_type = 0
                                pay_type = 1
                                pay_count = True
                                lowpaid_press_intern = True
                            if intern_highpaid_rect.collidepoint(event.pos) and pay_count == False:
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                job_type = 0
                                pay_type = 2
                                pay_count = True
                                highpaid_press_intern = True                             
                            if intern_year_0_rect.collidepoint(event.pos) and exp_count == False:
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                exp_0_press = True 
                                exp_count = True
                                years_of_experience = 0
                            if intern_year_1_4_rect.collidepoint(event.pos) and exp_count == False:
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                exp_1_4_press = True 
                                exp_count = True
                                years_of_experience = 2
                            if intern_year_4_rect.collidepoint(event.pos) and exp_count == False:
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                exp_4_press = True 
                                exp_count = True
                                years_of_experience = 6
                            if css_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                css_press = True
                                required_skills.append("css")
                            if c_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                c_press = True                 
                                required_skills.append("C/C++")
                            if java_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                java_press = True          
                                required_skills.append("Java")
                            if html_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                html_press = True
                                required_skills.append("HTML")
                            if jvs_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                jvs_press = True              
                                required_skills.append("JavaScript") 
                            if vhdl_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                vhdl_press = True   
                                required_skills.append("VHDL")
                            if python_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                python_press = True              
                                required_skills.append("Python")
                            if mongo_rect.collidepoint(event.pos):
                                pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                pygame.mixer.Channel(0).play(click_sound)
                                mongo_press = True
                                required_skills.append("MongoDB")
                            
                            if exp_count == True and pay_count == True and skills_count != 0:
                                if submit_rect.collidepoint(event.pos):
                                    pygame.mixer.Channel(0).set_volume(setting.get_volume())
                                    pygame.mixer.Channel(0).play(click_sound)
                                    num_app = num_applicant_generator(years_of_experience,pay_type,job_type,evil_score)
                                   
                                    print(num_app.return_num_of_applicants())
                                    print(num_app.evil_result())
                                    
                            
    speed.tick(FPS)
            
