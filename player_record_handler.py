from configparser import ConfigParser

class player_recorder():
    def __init__(self):   
        super().__init__()
        self.config = ConfigParser()
        self.config.read("data/game_variables.cfg")
                    
    def get_player_name(self,index):
        '''
        show the name of the requested player on the player's record slot
        '''
        return self.config.get(f"player_{index}","name")

    def get_player_score(self,index):
        '''
        show the final score of the requested player on the player's record slot
        '''
        return self.config.get(f"player_{index}","final_score")
        
    def set_player(self,name,score):
        '''
        set current player's name and score to an appropriate player's record slot
        '''
        counter = 0
        for x in range(1,4):
            player_name = self.get_player_name(x)
            if player_name == "":
                self.config.set(f"player_{x}","name",str(name))
                self.config.set(f"player_{x}","final_score",str(score))
                with open("data/game_variables.cfg","w") as configfile:
                    self.config.write(configfile)
                break
            counter += 1
            
        if counter == 3: #happens when the player's record is full
            #every slot in the record will be shifted down by 1 slot
            self.config.set("player_3","name",self.config.get("player_2","name"))
            self.config.set("player_3","final_score",self.config.get("player_2","final_score"))
            self.config.set("player_2","name",self.config.set("player_1","name"))
            self.config.set("player_2","final_score",self.config.get("player_1","final_score"))
            self.config.set("player_1","name",str(name))
            self.config.set("player_1","final_score",str(score))
            with open("data/game_variables.cfg","w") as configfile:
                self.config.write(configfile)