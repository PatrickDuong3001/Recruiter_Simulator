from random import randint

class num_applicant_generator():
    #evil score is 0 initially, but will be calculated and returned differently
    def __init__(self,num_exp,pay_amount,job_type,evil_score):   
        super().__init__()
        self.exp = num_exp
        self.pay = pay_amount
        self.job = job_type
        self.evil = evil_score
    
    def return_num_of_applicants(self):   
        #comprehensively set number of applicants
        #in mainGame, call this before evil_result()
        if self.job == 0:    #internship
            if self.pay == 0:     #unpaid. 
                if self.exp < 1:
                    self.evil += 5
                    return randint(20,40)
                elif self.exp >= 1 and self.exp < 4: 
                    self.evil += 6
                    return randint(0,5)
                elif self.exp >= 4: 
                    self.evil += 7
                    return 0
            elif self.pay == 1:   #low-ball pay. evil + 3
                self.evil += 3
                if self.exp < 1:
                    self.evil += 3
                    return randint(41,60)
                elif self.exp >= 1 and self.exp < 4: 
                    self.evil += 4
                    return randint(10,20)
                elif self.exp >= 4: 
                    self.evil += 5
                    return randint(0,5)   #why some people still apply? lol
            elif self.pay == 2:   #good pay. evil - 3
                if self.exp < 1: 
                    self.evil -= 3
                    return randint(61,100)
                elif self.exp >= 1 and self.exp < 4:
                    self.evil -= 2
                    return randint(20,30)
                elif self.exp >= 4:
                    self.evil -= 1
                    return randint(5,10)
        elif self.job == 1:   #mid-level job
            if self.pay == 0:     #unpaid. level + 8
                self.evil += 8
                return 0       #obviously
            elif self.pay == 1:   #low-ball pay. level + 5
                if self.exp < 4: 
                    self.evil += 5
                    return randint(6,15)
                elif self.exp >= 4: 
                    self.evil += 6
                    return randint(0,5)   
            elif self.pay == 2:   #good pay. level - 4
                if self.exp < 4:
                    self.evil -= 4
                    return randint(51,100)
                elif self.exp >= 4:
                    self.evil -= 3
                    return randint(40,50)
        else:                   #senior-level job
            if self.pay == 0:     #unpaid. level + 12
                self.evil += 12
                return 0       #obviously
            elif self.pay == 1:   #low-ball pay. level + 8
                self.evil += 8
                return 0  
            elif self.pay == 2:   #good pay. level - 1
                if self.exp < 4:
                    self.evil -= 2 
                    return randint(40,60)
                elif self.exp >= 4:
                    self.evil -= 1
                    return randint(15,30)
                    
    def evil_result(self):
        return self.evil          
    
            
            
        
             