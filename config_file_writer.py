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
    