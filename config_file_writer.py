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
        
        
    