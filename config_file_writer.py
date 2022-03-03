from configparser import ConfigParser

class config_write(): 
    '''
    this class helps save game, load game, and display most recent players
    '''
    def __init__(self):   
        super().__init__()
        self.config = ConfigParser()
        self.config.read("data/game_variables.cfg")
        
    def set_current_name(self,name):              
        '''
        write the name of current player to config file
        '''
        self.config.set("saved_session","name",str(name)) 
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_current_budget(self,budget):
        '''
        write the current-state budget to the config file
        '''
        self.config.set("saved_session","money",str(budget))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_current_phase(self,phase):
        '''
        write the current phase of recruitment to the config file
        '''
        self.config.set("saved_session","phase",str(phase))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_current_evil_meter(self,evil):
        '''
        write the current evil meter of recruitment to the config file
        '''
        self.config.set("saved_session","evil_meter",str(evil))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
            
    def set_current_skills(self,skills):
        '''
        write the current skill list of recruitment to the config file
        '''
        self.config.set("saved_session","skills",str(skills))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
        
    def set_initial_budget(self,initial): 
        '''
        write the initial budget of recruitment to the config file
        '''
        self.config.set("saved_session","initial_budget",str(initial))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
            
    def choose_startup(self): 
        '''
        if the user chooses startup, then reflect that in the config file
        '''
        self.config.set("saved_session","startup","True")
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def choose_bigtech(self):
        '''
        if the user chooses bigtech, then reflec that in the config file
        '''
        self.config.set("saved_session","bigtech","True")
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)

    def set_num_app(self,num):
        '''
        set number of applicants
        '''
        self.config.set("saved_session","num_app",str(num))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_current_level(self,level):
        '''
        set number of applicants
        '''
        level_set = ""
        if level == 0:
            level_set = "intern"
        elif level == 1:
            level_set = "mid"
        elif level == 2:
            level_set = "senior"
        self.config.set("saved_session","level",level_set)
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_current_pay(self,com_type,level,pay_type):
        '''
        set the current salary you choose to offer
        '''
        if com_type == 0:     #startup
            if level == 0:    #intern
                if pay_type == 0: #unpaid
                    self.config.set("saved_session","pay","exposure")
                elif pay_type == 1:  #low
                    self.config.set("saved_session","pay","$10/h")
                elif pay_type == 2:  #high
                    self.config.set("saved_session","pay","$50/h")
            elif level == 1:    #mid-level
                if pay_type == 0:  
                    self.config.set("saved_session","pay","exposure")
                elif pay_type == 1:
                    self.config.set("saved_session","pay","$20/h")
                elif pay_type == 2:
                    self.config.set("saved_session","pay","$60/h")
            elif level == 2:    #senior
                if pay_type == 0:  
                    self.config.set("saved_session","pay","exposure")
                elif pay_type == 1:
                    self.config.set("saved_session","pay","$30/h")
                elif pay_type == 2:
                    self.config.set("saved_session","pay","$70/h")
        elif com_type == 1:
            if level == 0:    #intern
                if pay_type == 0: #unpaid
                    self.config.set("saved_session","pay","exposure")
                elif pay_type == 1:  #low
                    self.config.set("saved_session","pay","$25/h")
                elif pay_type == 2:  #high
                    self.config.set("saved_session","pay","$80/h")
            elif level == 1:   #mid-level
                if pay_type == 0:  
                    self.config.set("saved_session","pay","exposure")
                elif pay_type == 1:
                    self.config.set("saved_session","pay","$35/h")
                elif pay_type == 2:
                    self.config.set("saved_session","pay","$90/h")
            elif level == 2:    #senior
                if pay_type == 0:  
                    self.config.set("saved_session","pay","exposure")
                elif pay_type == 1:
                    self.config.set("saved_session","pay","$45/h")
                elif pay_type == 2:
                    self.config.set("saved_session","pay","$100/h")
        
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
            
    def set_finalist_name(self,which,name):
        '''
        set name of the chosen candidates
        '''
        self.config.set(f"finalist_{which}","name",name)
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_finalist_skills(self,which,skills):
        '''
        set skills of the chosen candidate
        '''
        self.config.set(f"finalist_{which}","skills",skills)
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def set_finalist_exp(self,which,exp):
        '''
        set experience of the chosen candidate
        '''
        self.config.set(f"finalist_{which}","exp",str(exp))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
            
    def set_finalist_character(self,which,character):
        '''
        set character of the chosen candidate
        '''
        self.config.set(f"finalist_{which}","character",character)
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
            
    def set_finalist_success_rate(self,which, rate):
        '''
        set success rate of chosen candidate
        '''
        self.config.set(f"finalist_{which}","success_rate",str(rate))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
    
    def delete_all_saved_data(self):
        '''
        set all the variables inside 'saved session' to default values
        '''
        self.config.set("saved_session","name","")
        self.config.set("saved_session","initial_budget",str(0))
        self.config.set("saved_session","evil_meter",str(0))
        self.config.set("saved_session","phase",str(0))
        self.config.set("saved_session","job_type",str(0))
        self.config.set("saved_session","startup","False")
        self.config.set("saved_session","bigtech","False")
        self.config.set("saved_session","pay",str(0))
        self.config.set("saved_session","num_app",str(0))
        self.config.set("saved_session","skills","")
        self.config.set("saved_session","final_score",str(0))
        with open("data/game_variables.cfg","w") as configfile:
            self.config.write(configfile)
        
    