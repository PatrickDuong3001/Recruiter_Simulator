import pygame
import random
import names

skills = ["Docker","SQL","AWS","Android","Java","JavaScript","PHP","Python","HTML","VHDL","C/C++","CSS","MongoDB","React","Git","Jenkins","Selenium","MATLAB"]
characters = ["hard-working","handsome","creative","teamwork","research","documentation","muscular","innovative","honest","obedient","strong focus","detail-oriented","team player","leadership","mentorship"]
experience = ["software engineer","SDET","web developer","software developer","automation engineer","QA analyst","cashier","receptionist","tester","test engineer","business analyst","system engineer","engineer","hardware engineer","DevOps engineer","writer","programmer","data engineer","cloud engineer"]

class resume_generator():
    def __init__(self,how_many):
        super().__init__()
        self.how_many = how_many
        self.names = []
        
        self.person_0 = []
        self.person_1 = [] 
        self.person_2 = [] 
        self.person_3 = [] 
        self.person_4 = [] 
        self.person_5 = [] 
        self.person_6 = [] 
        self.person_7 = [] 
        self.person_8 = [] 
        self.person_9 = [] 
        self.person_10 = [] 
        self.person_11 = [] 
        self.person_12 = [] 
        self.person_13 = [] 
        self.person_14 = [] 
        self.person_15 = [] 
        self.person_16 = [] 
        self.person_17 = [] 
        self.person_18 = [] 
        self.person_19 = [] 
        self.person_20 = [] 
        self.person_21 = [] 
        self.person_22 = [] 
        self.person_23 = [] 
        self.person_24 = [] 
        self.person_25 = [] 
        self.person_26 = [] 
        self.person_27 = [] 
        self.person_28 = [] 
        self.person_29 = [] 
        self.person_30 = [] 
        self.person_31 = [] 
        self.person_32 = [] 
        self.person_33 = [] 
        self.person_34 = [] 
        self.person_35 = [] 
        self.person_36 = [] 
        self.person_37 = [] 
        self.person_38 = [] 
        self.person_39 = [] 
        self.person_40 = [] 
        self.person_41 = [] 
        self.person_42 = [] 
        self.person_43 = [] 
        self.person_44 = [] 
        self.person_45 = [] 
        self.person_46 = [] 
        self.person_47 = [] 
        self.person_48 = [] 
        self.person_49 = [] 
        self.person_50 = [] 
        self.person_51 = [] 
        self.person_52 = [] 
        self.person_53 = [] 
        self.person_54 = [] 
        self.person_55 = [] 
        self.person_56 = [] 
        self.person_57 = [] 
        self.person_58 = [] 
        self.person_59 = [] 
        self.person_60 = [] 
        self.person_61 = [] 
        self.person_62 = [] 
        self.person_63 = [] 
        self.person_64 = [] 
        self.person_65 = [] 
        self.person_66 = [] 
        self.person_67 = [] 
        self.person_68 = [] 
        self.person_69 = [] 
        self.person_70 = [] 
        self.person_71 = [] 
        self.person_72 = [] 
        self.person_73 = [] 
        self.person_74 = [] 
        self.person_75 = [] 
        self.person_76 = [] 
        self.person_77 = [] 
        self.person_78 = [] 
        self.person_79 = [] 
        self.person_80 = [] 
        self.person_81 = [] 
        self.person_82 = [] 
        self.person_83 = [] 
        self.person_84 = [] 
        self.person_85 = [] 
        self.person_86 = [] 
        self.person_87 = [] 
        self.person_88 = [] 
        self.person_89 = [] 
        self.person_90 = [] 
        self.person_91 = [] 
        self.person_92 = [] 
        self.person_93 = [] 
        self.person_94 = [] 
        self.person_95 = [] 
        self.person_96 = [] 
        self.person_97 = [] 
        self.person_98 = [] 
        self.person_99 = [] 
        self.person_100 = [] 

        self.char_person_0 = []
        self.char_person_1 = [] 
        self.char_person_2 = [] 
        self.char_person_3 = [] 
        self.char_person_4 = [] 
        self.char_person_5 = [] 
        self.char_person_6 = [] 
        self.char_person_7 = [] 
        self.char_person_8 = [] 
        self.char_person_9 = [] 
        self.char_person_10 = [] 
        self.char_person_11 = [] 
        self.char_person_12 = [] 
        self.char_person_13 = [] 
        self.char_person_14 = [] 
        self.char_person_15 = [] 
        self.char_person_16 = [] 
        self.char_person_17 = [] 
        self.char_person_18 = [] 
        self.char_person_19 = [] 
        self.char_person_20 = [] 
        self.char_person_21 = [] 
        self.char_person_22 = [] 
        self.char_person_23 = [] 
        self.char_person_24 = [] 
        self.char_person_25 = [] 
        self.char_person_26 = [] 
        self.char_person_27 = [] 
        self.char_person_28 = [] 
        self.char_person_29 = [] 
        self.char_person_30 = [] 
        self.char_person_31 = [] 
        self.char_person_32 = [] 
        self.char_person_33 = [] 
        self.char_person_34 = [] 
        self.char_person_35 = [] 
        self.char_person_36 = [] 
        self.char_person_37 = [] 
        self.char_person_38 = [] 
        self.char_person_39 = [] 
        self.char_person_40 = [] 
        self.char_person_41 = [] 
        self.char_person_42 = [] 
        self.char_person_43 = [] 
        self.char_person_44 = [] 
        self.char_person_45 = [] 
        self.char_person_46 = [] 
        self.char_person_47 = [] 
        self.char_person_48 = [] 
        self.char_person_49 = [] 
        self.char_person_50 = [] 
        self.char_person_51 = [] 
        self.char_person_52 = [] 
        self.char_person_53 = [] 
        self.char_person_54 = [] 
        self.char_person_55 = [] 
        self.char_person_56 = [] 
        self.char_person_57 = [] 
        self.char_person_58 = [] 
        self.char_person_59 = [] 
        self.char_person_60 = [] 
        self.char_person_61 = [] 
        self.char_person_62 = [] 
        self.char_person_63 = [] 
        self.char_person_64 = [] 
        self.char_person_65 = [] 
        self.char_person_66 = [] 
        self.char_person_67 = [] 
        self.char_person_68 = [] 
        self.char_person_69 = [] 
        self.char_person_70 = [] 
        self.char_person_71 = [] 
        self.char_person_72 = [] 
        self.char_person_73 = [] 
        self.char_person_74 = [] 
        self.char_person_75 = [] 
        self.char_person_76 = [] 
        self.char_person_77 = [] 
        self.char_person_78 = [] 
        self.char_person_79 = [] 
        self.char_person_80 = [] 
        self.char_person_81 = [] 
        self.char_person_82 = [] 
        self.char_person_83 = [] 
        self.char_person_84 = [] 
        self.char_person_85 = [] 
        self.char_person_86 = [] 
        self.char_person_87 = [] 
        self.char_person_88 = [] 
        self.char_person_89 = [] 
        self.char_person_90 = [] 
        self.char_person_91 = [] 
        self.char_person_92 = [] 
        self.char_person_93 = [] 
        self.char_person_94 = [] 
        self.char_person_95 = [] 
        self.char_person_96 = [] 
        self.char_person_97 = [] 
        self.char_person_98 = [] 
        self.char_person_99 = [] 
        self.char_person_100 = [] 
        
        self.skills_person_0 = []
        self.skills_person_1 = [] 
        self.skills_person_2 = [] 
        self.skills_person_3 = [] 
        self.skills_person_4 = [] 
        self.skills_person_5 = [] 
        self.skills_person_6 = [] 
        self.skills_person_7 = [] 
        self.skills_person_8 = [] 
        self.skills_person_9 = [] 
        self.skills_person_10 = [] 
        self.skills_person_11 = [] 
        self.skills_person_12 = [] 
        self.skills_person_13 = [] 
        self.skills_person_14 = [] 
        self.skills_person_15 = [] 
        self.skills_person_16 = [] 
        self.skills_person_17 = [] 
        self.skills_person_18 = [] 
        self.skills_person_19 = [] 
        self.skills_person_20 = [] 
        self.skills_person_21 = [] 
        self.skills_person_22 = [] 
        self.skills_person_23 = [] 
        self.skills_person_24 = [] 
        self.skills_person_25 = [] 
        self.skills_person_26 = [] 
        self.skills_person_27 = [] 
        self.skills_person_28 = [] 
        self.skills_person_29 = [] 
        self.skills_person_30 = [] 
        self.skills_person_31 = [] 
        self.skills_person_32 = [] 
        self.skills_person_33 = [] 
        self.skills_person_34 = [] 
        self.skills_person_35 = [] 
        self.skills_person_36 = [] 
        self.skills_person_37 = [] 
        self.skills_person_38 = [] 
        self.skills_person_39 = [] 
        self.skills_person_40 = [] 
        self.skills_person_41 = [] 
        self.skills_person_42 = [] 
        self.skills_person_43 = [] 
        self.skills_person_44 = [] 
        self.skills_person_45 = [] 
        self.skills_person_46 = [] 
        self.skills_person_47 = [] 
        self.skills_person_48 = [] 
        self.skills_person_49 = [] 
        self.skills_person_50 = [] 
        self.skills_person_51 = [] 
        self.skills_person_52 = [] 
        self.skills_person_53 = [] 
        self.skills_person_54 = [] 
        self.skills_person_55 = [] 
        self.skills_person_56 = [] 
        self.skills_person_57 = [] 
        self.skills_person_58 = [] 
        self.skills_person_59 = [] 
        self.skills_person_60 = [] 
        self.skills_person_61 = [] 
        self.skills_person_62 = [] 
        self.skills_person_63 = [] 
        self.skills_person_64 = [] 
        self.skills_person_65 = [] 
        self.skills_person_66 = [] 
        self.skills_person_67 = [] 
        self.skills_person_68 = [] 
        self.skills_person_69 = [] 
        self.skills_person_70 = [] 
        self.skills_person_71 = [] 
        self.skills_person_72 = [] 
        self.skills_person_73 = [] 
        self.skills_person_74 = [] 
        self.skills_person_75 = [] 
        self.skills_person_76 = [] 
        self.skills_person_77 = [] 
        self.skills_person_78 = [] 
        self.skills_person_79 = [] 
        self.skills_person_80 = [] 
        self.skills_person_81 = [] 
        self.skills_person_82 = [] 
        self.skills_person_83 = [] 
        self.skills_person_84 = [] 
        self.skills_person_85 = [] 
        self.skills_person_86 = [] 
        self.skills_person_87 = [] 
        self.skills_person_88 = [] 
        self.skills_person_89 = [] 
        self.skills_person_90 = [] 
        self.skills_person_91 = [] 
        self.skills_person_92 = [] 
        self.skills_person_93 = [] 
        self.skills_person_94 = [] 
        self.skills_person_95 = [] 
        self.skills_person_96 = [] 
        self.skills_person_97 = [] 
        self.skills_person_98 = [] 
        self.skills_person_99 = [] 
        self.skills_person_100 = [] 

        self.exp_person_0 = []
        self.exp_person_1 = [] 
        self.exp_person_2 = [] 
        self.exp_person_3 = [] 
        self.exp_person_4 = [] 
        self.exp_person_5 = [] 
        self.exp_person_6 = [] 
        self.exp_person_7 = [] 
        self.exp_person_8 = [] 
        self.exp_person_9 = [] 
        self.exp_person_10 = [] 
        self.exp_person_11 = [] 
        self.exp_person_12 = [] 
        self.exp_person_13 = [] 
        self.exp_person_14 = [] 
        self.exp_person_15 = [] 
        self.exp_person_16 = [] 
        self.exp_person_17 = [] 
        self.exp_person_18 = [] 
        self.exp_person_19 = [] 
        self.exp_person_20 = [] 
        self.exp_person_21 = [] 
        self.exp_person_22 = [] 
        self.exp_person_23 = [] 
        self.exp_person_24 = [] 
        self.exp_person_25 = [] 
        self.exp_person_26 = [] 
        self.exp_person_27 = [] 
        self.exp_person_28 = [] 
        self.exp_person_29 = [] 
        self.exp_person_30 = [] 
        self.exp_person_31 = [] 
        self.exp_person_32 = [] 
        self.exp_person_33 = [] 
        self.exp_person_34 = [] 
        self.exp_person_35 = [] 
        self.exp_person_36 = [] 
        self.exp_person_37 = [] 
        self.exp_person_38 = [] 
        self.exp_person_39 = [] 
        self.exp_person_40 = [] 
        self.exp_person_41 = [] 
        self.exp_person_42 = [] 
        self.exp_person_43 = [] 
        self.exp_person_44 = [] 
        self.exp_person_45 = [] 
        self.exp_person_46 = [] 
        self.exp_person_47 = [] 
        self.exp_person_48 = [] 
        self.exp_person_49 = [] 
        self.exp_person_50 = [] 
        self.exp_person_51 = [] 
        self.exp_person_52 = [] 
        self.exp_person_53 = [] 
        self.exp_person_54 = [] 
        self.exp_person_55 = [] 
        self.exp_person_56 = [] 
        self.exp_person_57 = [] 
        self.exp_person_58 = [] 
        self.exp_person_59 = [] 
        self.exp_person_60 = [] 
        self.exp_person_61 = [] 
        self.exp_person_62 = [] 
        self.exp_person_63 = [] 
        self.exp_person_64 = [] 
        self.exp_person_65 = [] 
        self.exp_person_66 = [] 
        self.exp_person_67 = [] 
        self.exp_person_68 = [] 
        self.exp_person_69 = [] 
        self.exp_person_70 = [] 
        self.exp_person_71 = [] 
        self.exp_person_72 = [] 
        self.exp_person_73 = [] 
        self.exp_person_74 = [] 
        self.exp_person_75 = [] 
        self.exp_person_76 = [] 
        self.exp_person_77 = [] 
        self.exp_person_78 = [] 
        self.exp_person_79 = [] 
        self.exp_person_80 = [] 
        self.exp_person_81 = [] 
        self.exp_person_82 = [] 
        self.exp_person_83 = [] 
        self.exp_person_84 = [] 
        self.exp_person_85 = [] 
        self.exp_person_86 = [] 
        self.exp_person_87 = [] 
        self.exp_person_88 = [] 
        self.exp_person_89 = [] 
        self.exp_person_90 = [] 
        self.exp_person_91 = [] 
        self.exp_person_92 = [] 
        self.exp_person_93 = [] 
        self.exp_person_94 = [] 
        self.exp_person_95 = [] 
        self.exp_person_96 = [] 
        self.exp_person_97 = [] 
        self.exp_person_98 = [] 
        self.exp_person_99 = [] 
        self.exp_person_100 = [] 

        self.all_persons = []

    def generate_names(self):    
        '''
        generate names for resumes
        '''
        for x in range(self.how_many):
            self.names.append(names.get_full_name())
    
    def set_names(self,index):
        if index == 0:
            self.person_0.append(self.names[index])
        elif index == 1: 
            self.person_1.append(self.names[index])
        elif index == 2: 
            self.person_2.append(self.names[index]) 
        elif index == 3:
            self.person_3.append(self.names[index]) 
        elif index == 4: 
            self.person_4.append(self.names[index]) 
        elif index == 5: 
            self.person_5.append(self.names[index]) 
        elif index == 6: 
            self.person_6.append(self.names[index]) 
        elif index == 7: 
            self.person_7.append(self.names[index]) 
        elif index == 8: 
            self.person_8.append(self.names[index]) 
        elif index == 9: 
            self.person_9.append(self.names[index]) 
        elif index == 10: 
            self.person_10.append(self.names[index]) 
        elif index == 11: 
            self.person_11.append(self.names[index]) 
        elif index == 12: 
            self.person_12.append(self.names[index]) 
        elif index == 13: 
            self.person_13.append(self.names[index]) 
        elif index == 14: 
            self.person_14.append(self.names[index]) 
        elif index == 15: 
            self.person_15.append(self.names[index]) 
        elif index == 16: 
            self.person_16.append(self.names[index]) 
        elif index == 17: 
            self.person_17.append(self.names[index]) 
        elif index == 18: 
            self.person_18.append(self.names[index]) 
        elif index == 19: 
            self.person_19.append(self.names[index]) 
        elif index == 20: 
            self.person_20.append(self.names[index]) 
        elif index == 21: 
            self.person_21.append(self.names[index]) 
        elif index == 22: 
            self.person_22.append(self.names[index]) 
        elif index == 23: 
            self.person_23.append(self.names[index]) 
        elif index == 24: 
            self.person_24.append(self.names[index]) 
        elif index == 25: 
            self.person_25.append(self.names[index]) 
        elif index == 26: 
            self.person_26.append(self.names[index]) 
        elif index == 27: 
            self.person_27.append(self.names[index]) 
        elif index == 28: 
            self.person_28.append(self.names[index]) 
        elif index == 29: 
            self.person_29.append(self.names[index]) 
        elif index == 30: 
            self.person_30.append(self.names[index]) 
        elif index == 31: 
            self.person_31.append(self.names[index]) 
        elif index == 32: 
            self.person_32.append(self.names[index]) 
        elif index == 33: 
            self.person_33.append(self.names[index]) 
        elif index == 34: 
            self.person_34.append(self.names[index]) 
        elif index == 35: 
            self.person_35.append(self.names[index]) 
        elif index == 36: 
            self.person_36.append(self.names[index]) 
        elif index == 37: 
            self.person_37.append(self.names[index]) 
        elif index == 38: 
            self.person_38.append(self.names[index]) 
        elif index == 39: 
            self.person_39.append(self.names[index]) 
        elif index == 40: 
            self.person_40.append(self.names[index]) 
        elif index == 41: 
            self.person_41.append(self.names[index]) 
        elif index == 42: 
            self.person_42.append(self.names[index]) 
        elif index == 43: 
            self.person_43.append(self.names[index]) 
        elif index == 44: 
            self.person_44.append(self.names[index]) 
        elif index == 45: 
            self.person_45.append(self.names[index]) 
        elif index == 46: 
            self.person_46.append(self.names[index]) 
        elif index == 47: 
            self.person_47.append(self.names[index]) 
        elif index == 48: 
            self.person_48.append(self.names[index]) 
        elif index == 49: 
            self.person_49.append(self.names[index]) 
        elif index == 50: 
            self.person_50.append(self.names[index]) 
        elif index == 51: 
            self.person_51.append(self.names[index]) 
        elif index == 52: 
            self.person_52.append(self.names[index]) 
        elif index == 53: 
            self.person_53.append(self.names[index]) 
        elif index == 54: 
            self.person_54.append(self.names[index]) 
        elif index == 55: 
            self.person_55.append(self.names[index]) 
        elif index == 56: 
            self.person_56.append(self.names[index]) 
        elif index == 57: 
            self.person_57.append(self.names[index]) 
        elif index == 58: 
            self.person_58.append(self.names[index]) 
        elif index == 59: 
            self.person_59.append(self.names[index]) 
        elif index == 60: 
            self.person_60.append(self.names[index]) 
        elif index == 61: 
            self.person_61.append(self.names[index]) 
        elif index == 62: 
            self.person_62.append(self.names[index]) 
        elif index == 63: 
            self.person_63.append(self.names[index]) 
        elif index == 64: 
            self.person_64.append(self.names[index]) 
        elif index == 65: 
            self.person_65.append(self.names[index]) 
        elif index == 66: 
            self.person_66.append(self.names[index]) 
        elif index == 67: 
            self.person_67.append(self.names[index]) 
        elif index == 68: 
            self.person_68.append(self.names[index]) 
        elif index == 69: 
            self.person_69.append(self.names[index]) 
        elif index == 70: 
            self.person_70.append(self.names[index]) 
        elif index == 71: 
            self.person_71.append(self.names[index]) 
        elif index == 72: 
            self.person_72.append(self.names[index]) 
        elif index == 73: 
            self.person_73.append(self.names[index]) 
        elif index == 74: 
            self.person_74.append(self.names[index]) 
        elif index == 75: 
            self.person_75.append(self.names[index]) 
        elif index == 76: 
            self.person_76.append(self.names[index]) 
        elif index == 77: 
            self.person_77.append(self.names[index]) 
        elif index == 78: 
            self.person_78.append(self.names[index]) 
        elif index == 79: 
            self.person_79.append(self.names[index]) 
        elif index == 80: 
            self.person_80.append(self.names[index]) 
        elif index == 81: 
            self.person_81.append(self.names[index]) 
        elif index == 82: 
            self.person_82.append(self.names[index]) 
        elif index == 83: 
            self.person_83.append(self.names[index]) 
        elif index == 84: 
            self.person_84.append(self.names[index]) 
        elif index == 85: 
            self.person_85.append(self.names[index]) 
        elif index == 86: 
            self.person_86.append(self.names[index]) 
        elif index == 87: 
            self.person_87.append(self.names[index]) 
        elif index == 88: 
            self.person_88.append(self.names[index]) 
        elif index == 89: 
            self.person_89.append(self.names[index]) 
        elif index == 90: 
            self.person_90.append(self.names[index]) 
        elif index == 91: 
            self.person_91.append(self.names[index]) 
        elif index == 92: 
            self.person_92.append(self.names[index]) 
        elif index == 93: 
            self.person_93.append(self.names[index]) 
        elif index == 94: 
            self.person_94.append(self.names[index]) 
        elif index == 95: 
            self.person_95.append(self.names[index]) 
        elif index == 96: 
            self.person_96.append(self.names[index]) 
        elif index == 97: 
            self.person_97.append(self.names[index]) 
        elif index == 98: 
            self.person_98.append(self.names[index]) 
        elif index == 99: 
            self.person_99.append(self.names[index]) 
        elif index == 100: 
            self.person_100.append(self.names[index]) 
    
    def set_skills(self,index):
        '''
        set up skills for a candidate
        '''
        num_skills = random.randint(2,5)   #number of skills on resume is random
        random_skill = None
        temp_skill_set = []
        
        for x in range(num_skills):
            random_skill = random.choice(skills)
            if index == 0:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 1:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 2:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 3:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 4:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 5:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 6:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 7:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 8:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 9:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 10:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 11:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 12:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 13:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 14:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 15:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 16:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 17:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 18:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 19:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 20:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 21:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 22:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 23:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 24:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 25:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 26:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 27:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 28:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 29:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 30:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 31:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 32:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 33:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 34:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 35:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 36:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 37:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 38:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 39:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 40:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 41:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 42:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 43:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 44:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 45:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 46:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 47:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 48:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 49:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 50:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 51:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 52:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 53:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 54:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 55:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 56:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 57:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 58:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 59:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 60:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 61:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 62:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 63:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 64:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 65:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 66:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 67:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 68:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 69:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 70:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 71:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 72:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 73:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 74:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 75:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 76:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 77:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 78:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 79:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 80:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 81:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 82:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 83:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 84:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 85:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 86:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 87:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 88:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 89:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 90:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 91:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 92:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 93:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 94:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 95:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 96:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 97:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 98:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 99:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)
            elif index == 100:
                if random_skill in temp_skill_set:
                    random_skill = random.choice(skills)
                temp_skill_set.append(random_skill)      
        
        if index == 0:
            self.person_0.append(", ".join(temp_skill_set))
        elif index == 1:
            self.person_1.append(', '.join(temp_skill_set))
        elif index == 2:
            self.person_2.append(', '.join(temp_skill_set))
        elif index == 3:
            self.person_3.append(', '.join(temp_skill_set))
        elif index == 4:
            self.person_4.append(', '.join(temp_skill_set))
        elif index == 5:
            self.person_5.append(', '.join(temp_skill_set))
        elif index == 6:
            self.person_6.append(', '.join(temp_skill_set))
        elif index == 7:
            self.person_7.append(', '.join(temp_skill_set))
        elif index == 8:
            self.person_8.append(', '.join(temp_skill_set))
        elif index == 9:
            self.person_9.append(', '.join(temp_skill_set))
        elif index == 10:
            self.person_10.append(', '.join(temp_skill_set))
        elif index == 11:
            self.person_11.append(', '.join(temp_skill_set))
        elif index == 12:
            self.person_12.append(', '.join(temp_skill_set))
        elif index == 13:
            self.person_13.append(', '.join(temp_skill_set))
        elif index == 14:
            self.person_14.append(', '.join(temp_skill_set))
        elif index == 15:
            self.person_15.append(', '.join(temp_skill_set))
        elif index == 16:
            self.person_16.append(', '.join(temp_skill_set))
        elif index == 17:
            self.person_17.append(', '.join(temp_skill_set))
        elif index == 18:
            self.person_18.append(', '.join(temp_skill_set))
        elif index == 19:
            self.person_19.append(', '.join(temp_skill_set))
        elif index == 20:
            self.person_20.append(', '.join(temp_skill_set))
        elif index == 21:
            self.person_21.append(', '.join(temp_skill_set))
        elif index == 22:
            self.person_22.append(', '.join(temp_skill_set))
        elif index == 23:
            self.person_23.append(', '.join(temp_skill_set))
        elif index == 24:
            self.person_24.append(', '.join(temp_skill_set))
        elif index == 25:
            self.person_25.append(', '.join(temp_skill_set))
        elif index == 26:
            self.person_26.append(', '.join(temp_skill_set))
        elif index == 27:
            self.person_27.append(', '.join(temp_skill_set))
        elif index == 28:
            self.person_28.append(', '.join(temp_skill_set))
        elif index == 29:
            self.person_29.append(', '.join(temp_skill_set))
        elif index == 30:
            self.person_30.append(', '.join(temp_skill_set))
        elif index == 31:
            self.person_31.append(', '.join(temp_skill_set))
        elif index == 32:
            self.person_32.append(', '.join(temp_skill_set))
        elif index == 33:
            self.person_33.append(', '.join(temp_skill_set))
        elif index == 34:
            self.person_34.append(', '.join(temp_skill_set))
        elif index == 35:
            self.person_35.append(', '.join(temp_skill_set))
        elif index == 36:
            self.person_36.append(', '.join(temp_skill_set))
        elif index == 37:
            self.person_37.append(', '.join(temp_skill_set))
        elif index == 38:
            self.person_38.append(', '.join(temp_skill_set))
        elif index == 39:
            self.person_39.append(', '.join(temp_skill_set))
        elif index == 40:
            self.person_40.append(', '.join(temp_skill_set))
        elif index == 41:
            self.person_41.append(', '.join(temp_skill_set))
        elif index == 42:
            self.person_42.append(', '.join(temp_skill_set))
        elif index == 43:
            self.person_43.append(', '.join(temp_skill_set))
        elif index == 44:
            self.person_44.append(', '.join(temp_skill_set))
        elif index == 45:
            self.person_45.append(', '.join(temp_skill_set))
        elif index == 46:
            self.person_46.append(', '.join(temp_skill_set))
        elif index == 47:
            self.person_47.append(', '.join(temp_skill_set))
        elif index == 48:
            self.person_48.append(', '.join(temp_skill_set))
        elif index == 49:
            self.person_49.append(', '.join(temp_skill_set))
        elif index == 50:
            self.person_50.append(', '.join(temp_skill_set))
        elif index == 51:
            self.person_51.append(', '.join(temp_skill_set))
        elif index == 52:
            self.person_52.append(', '.join(temp_skill_set))
        elif index == 53:
            self.person_53.append(', '.join(temp_skill_set))
        elif index == 54:
            self.person_54.append(', '.join(temp_skill_set))
        elif index == 55:
            self.person_55.append(', '.join(temp_skill_set))
        elif index == 56:
            self.person_56.append(', '.join(temp_skill_set))
        elif index == 57:
            self.person_57.append(', '.join(temp_skill_set))
        elif index == 58:
            self.person_58.append(', '.join(temp_skill_set))
        elif index == 59:
            self.person_59.append(', '.join(temp_skill_set))
        elif index == 60:
            self.person_60.append(', '.join(temp_skill_set))
        elif index == 61:
            self.person_61.append(', '.join(temp_skill_set))
        elif index == 62:
            self.person_62.append(', '.join(temp_skill_set))
        elif index == 63:
            self.person_63.append(', '.join(temp_skill_set))
        elif index == 64:
            self.person_64.append(', '.join(temp_skill_set))
        elif index == 65:
            self.person_65.append(', '.join(temp_skill_set))
        elif index == 66:
            self.person_66.append(', '.join(temp_skill_set))
        elif index == 67:
            self.person_67.append(', '.join(temp_skill_set))
        elif index == 68:
            self.person_68.append(', '.join(temp_skill_set))
        elif index == 69:
            self.person_69.append(', '.join(temp_skill_set))
        elif index == 70:
            self.person_70.append(', '.join(temp_skill_set))
        elif index == 71:
            self.person_71.append(', '.join(temp_skill_set))
        elif index == 72:
            self.person_72.append(', '.join(temp_skill_set))
        elif index == 73:
            self.person_73.append(', '.join(temp_skill_set))
        elif index == 74:
            self.person_74.append(', '.join(temp_skill_set))
        elif index == 75:
            self.person_75.append(', '.join(temp_skill_set))
        elif index == 76:
            self.person_76.append(', '.join(temp_skill_set))
        elif index == 77:
            self.person_77.append(', '.join(temp_skill_set))
        elif index == 78:
            self.person_78.append(', '.join(temp_skill_set))
        elif index == 79:
            self.person_79.append(', '.join(temp_skill_set))
        elif index == 80:
            self.person_80.append(', '.join(temp_skill_set))
        elif index == 81:
            self.person_81.append(', '.join(temp_skill_set))
        elif index == 82:
            self.person_82.append(', '.join(temp_skill_set))
        elif index == 83:
            self.person_83.append(', '.join(temp_skill_set))
        elif index == 84:
            self.person_84.append(', '.join(temp_skill_set))
        elif index == 85:
            self.person_85.append(', '.join(temp_skill_set))
        elif index == 86:
            self.person_86.append(', '.join(temp_skill_set))
        elif index == 87:
            self.person_87.append(', '.join(temp_skill_set))
        elif index == 88:
            self.person_88.append(', '.join(temp_skill_set))
        elif index == 89:
            self.person_89.append(', '.join(temp_skill_set))
        elif index == 90:
            self.person_90.append(', '.join(temp_skill_set))
        elif index == 91:
            self.person_91.append(', '.join(temp_skill_set))
        elif index == 92:
            self.person_92.append(', '.join(temp_skill_set))
        elif index == 93:
            self.person_93.append(', '.join(temp_skill_set))
        elif index == 94:
            self.person_94.append(', '.join(temp_skill_set))
        elif index == 95:
            self.person_95.append(', '.join(temp_skill_set))
        elif index == 96:
            self.person_96.append(', '.join(temp_skill_set))
        elif index == 97:
            self.person_97.append(', '.join(temp_skill_set))
        elif index == 98:
            self.person_98.append(', '.join(temp_skill_set))
        elif index == 99:
            self.person_99.append(', '.join(temp_skill_set))
        elif index == 100:
            self.person_100.append(', '.join(temp_skill_set))

    def set_characters(self,index):
        '''
        set up characters for a candidate
        '''
        num_chars = random.randint(1,3)   #number of skills on resume is random
        random_char = None
        temp_char_set = []
        
        for x in range(num_chars):
            random_char = random.choice(characters)
            if index == 0:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 1:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 2:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 3:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 4:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 5:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 6:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 7:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 8:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 9:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 10:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 11:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 12:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 13:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 14:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 15:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 16:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 17:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 18:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 19:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 20:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 21:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 22:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 23:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 24:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 25:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 26:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 27:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 28:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 29:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 30:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 31:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 32:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 33:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 34:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 35:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 36:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 37:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 38:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 39:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 40:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 41:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 42:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 43:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 44:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 45:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 46:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 47:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 48:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 49:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 50:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 51:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 52:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 53:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 54:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 55:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 56:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 57:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 58:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 59:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 60:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 61:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 62:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 63:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 64:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 65:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 66:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 67:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 68:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 69:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 70:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 71:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 72:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 73:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 74:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 75:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 76:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 77:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 78:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 79:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 80:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 81:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 82:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 83:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 84:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 85:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 86:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 87:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 88:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 89:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 90:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 91:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 92:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 93:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 94:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 95:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 96:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 97:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 98:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 99:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
            elif index == 100:
                if random_char in temp_char_set:
                    random_char = random.choice(characters)
                temp_char_set.append(random_char)
        
        if index == 0:
            self.person_0.append(', '.join(temp_char_set))
        elif index == 1:
            self.person_1.append(', '.join(temp_char_set))
        elif index == 2:
            self.person_2.append(', '.join(temp_char_set))
        elif index == 3:
            self.person_3.append(', '.join(temp_char_set))
        elif index == 4:
            self.person_4.append(', '.join(temp_char_set))
        elif index == 5:
            self.person_5.append(', '.join(temp_char_set))
        elif index == 6:
            self.person_6.append(', '.join(temp_char_set))
        elif index == 7:
            self.person_7.append(', '.join(temp_char_set))
        elif index == 8:
            self.person_8.append(', '.join(temp_char_set))
        elif index == 9:
            self.person_9.append(', '.join(temp_char_set))
        elif index == 10:
            self.person_10.append(', '.join(temp_char_set))
        elif index == 11:
            self.person_11.append(', '.join(temp_char_set))
        elif index == 12:
            self.person_12.append(', '.join(temp_char_set))
        elif index == 13:
            self.person_13.append(', '.join(temp_char_set))
        elif index == 14:
            self.person_14.append(', '.join(temp_char_set))
        elif index == 15:
            self.person_15.append(', '.join(temp_char_set))
        elif index == 16:
            self.person_16.append(', '.join(temp_char_set))
        elif index == 17:
            self.person_17.append(', '.join(temp_char_set))
        elif index == 18:
            self.person_18.append(', '.join(temp_char_set))
        elif index == 19:
            self.person_19.append(', '.join(temp_char_set))
        elif index == 20:
            self.person_20.append(', '.join(temp_char_set))
        elif index == 21:
            self.person_21.append(', '.join(temp_char_set))
        elif index == 22:
            self.person_22.append(', '.join(temp_char_set))
        elif index == 23:
            self.person_23.append(', '.join(temp_char_set))
        elif index == 24:
            self.person_24.append(', '.join(temp_char_set))
        elif index == 25:
            self.person_25.append(', '.join(temp_char_set))
        elif index == 26:
            self.person_26.append(', '.join(temp_char_set))
        elif index == 27:
            self.person_27.append(', '.join(temp_char_set))
        elif index == 28:
            self.person_28.append(', '.join(temp_char_set))
        elif index == 29:
            self.person_29.append(', '.join(temp_char_set))
        elif index == 30:
            self.person_30.append(', '.join(temp_char_set))
        elif index == 31:
            self.person_31.append(', '.join(temp_char_set))
        elif index == 32:
            self.person_32.append(', '.join(temp_char_set))
        elif index == 33:
            self.person_33.append(', '.join(temp_char_set))
        elif index == 34:
            self.person_34.append(', '.join(temp_char_set))
        elif index == 35:
            self.person_35.append(', '.join(temp_char_set))
        elif index == 36:
            self.person_36.append(', '.join(temp_char_set))
        elif index == 37:
            self.person_37.append(', '.join(temp_char_set))
        elif index == 38:
            self.person_38.append(', '.join(temp_char_set))
        elif index == 39:
            self.person_39.append(', '.join(temp_char_set))
        elif index == 40:
            self.person_40.append(', '.join(temp_char_set))
        elif index == 41:
            self.person_41.append(', '.join(temp_char_set))
        elif index == 42:
            self.person_42.append(', '.join(temp_char_set))
        elif index == 43:
            self.person_43.append(', '.join(temp_char_set))
        elif index == 44:
            self.person_44.append(', '.join(temp_char_set))
        elif index == 45:
            self.person_45.append(', '.join(temp_char_set))
        elif index == 46:
            self.person_46.append(', '.join(temp_char_set))
        elif index == 47:
            self.person_47.append(', '.join(temp_char_set))
        elif index == 48:
            self.person_48.append(', '.join(temp_char_set))
        elif index == 49:
            self.person_49.append(', '.join(temp_char_set))
        elif index == 50:
            self.person_50.append(', '.join(temp_char_set))
        elif index == 51:
            self.person_51.append(', '.join(temp_char_set))
        elif index == 52:
            self.person_52.append(', '.join(temp_char_set))
        elif index == 53:
            self.person_53.append(', '.join(temp_char_set))
        elif index == 54:
            self.person_54.append(', '.join(temp_char_set))
        elif index == 55:
            self.person_55.append(', '.join(temp_char_set))
        elif index == 56:
            self.person_56.append(', '.join(temp_char_set))
        elif index == 57:
            self.person_57.append(', '.join(temp_char_set))
        elif index == 58:
            self.person_58.append(', '.join(temp_char_set))
        elif index == 59:
            self.person_59.append(', '.join(temp_char_set))
        elif index == 60:
            self.person_60.append(', '.join(temp_char_set))
        elif index == 61:
            self.person_61.append(', '.join(temp_char_set))
        elif index == 62:
            self.person_62.append(', '.join(temp_char_set))
        elif index == 63:
            self.person_63.append(', '.join(temp_char_set))
        elif index == 64:
            self.person_64.append(', '.join(temp_char_set))
        elif index == 65:
            self.person_65.append(', '.join(temp_char_set))
        elif index == 66:
            self.person_66.append(', '.join(temp_char_set))
        elif index == 67:
            self.person_67.append(', '.join(temp_char_set))
        elif index == 68:
            self.person_68.append(', '.join(temp_char_set))
        elif index == 69:
            self.person_69.append(', '.join(temp_char_set))
        elif index == 70:
            self.person_70.append(', '.join(temp_char_set))
        elif index == 71:
            self.person_71.append(', '.join(temp_char_set))
        elif index == 72:
            self.person_72.append(', '.join(temp_char_set))
        elif index == 73:
            self.person_73.append(', '.join(temp_char_set))
        elif index == 74:
            self.person_74.append(', '.join(temp_char_set))
        elif index == 75:
            self.person_75.append(', '.join(temp_char_set))
        elif index == 76:
            self.person_76.append(', '.join(temp_char_set))
        elif index == 77:
            self.person_77.append(', '.join(temp_char_set))
        elif index == 78:
            self.person_78.append(', '.join(temp_char_set))
        elif index == 79:
            self.person_79.append(', '.join(temp_char_set))
        elif index == 80:
            self.person_80.append(', '.join(temp_char_set))
        elif index == 81:
            self.person_81.append(', '.join(temp_char_set))
        elif index == 82:
            self.person_82.append(', '.join(temp_char_set))
        elif index == 83:
            self.person_83.append(', '.join(temp_char_set))
        elif index == 84:
            self.person_84.append(', '.join(temp_char_set))
        elif index == 85:
            self.person_85.append(', '.join(temp_char_set))
        elif index == 86:
            self.person_86.append(', '.join(temp_char_set))
        elif index == 87:
            self.person_87.append(', '.join(temp_char_set))
        elif index == 88:
            self.person_88.append(', '.join(temp_char_set))
        elif index == 89:
            self.person_89.append(', '.join(temp_char_set))
        elif index == 90:
            self.person_90.append(', '.join(temp_char_set))
        elif index == 91:
            self.person_91.append(', '.join(temp_char_set))
        elif index == 92:
            self.person_92.append(', '.join(temp_char_set))
        elif index == 93:
            self.person_93.append(', '.join(temp_char_set))
        elif index == 94:
            self.person_94.append(', '.join(temp_char_set))
        elif index == 95:
            self.person_95.append(', '.join(temp_char_set))
        elif index == 96:
            self.person_96.append(', '.join(temp_char_set))
        elif index == 97:
            self.person_97.append(', '.join(temp_char_set))
        elif index == 98:
            self.person_98.append(', '.join(temp_char_set))
        elif index == 99:
            self.person_99.append(', '.join(temp_char_set))
        elif index == 100:
            self.person_100.append(', '.join(temp_char_set))

    def set_exp(self,index):
        '''
        set up experience for a candidate
        '''
        num_exp = random.randint(1,2)
        random_exp = None
        temp_exp_set = []
        
        for x in range(num_exp):
            random_exp = random.choice(experience)
            if index == 0:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 1:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 2:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 3:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 4:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 5:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 6:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 7:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 8:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 9:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 10:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 11:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 12:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 13:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 14:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 15:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 16:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 17:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 18:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 19:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 20:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 21:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 22:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 23:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 24:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 25:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 26:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 27:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 28:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 29:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 30:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 31:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 32:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 33:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 34:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 35:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 36:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 37:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 38:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 39:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 40:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 41:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 42:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 43:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 44:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 45:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 46:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 47:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 48:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 49:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 50:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 51:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 52:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 53:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 54:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 55:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 56:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 57:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 58:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 59:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 60:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 61:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 62:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 63:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 64:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 65:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 66:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 67:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 68:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 69:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 70:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 71:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 72:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 73:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 74:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 75:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 76:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 77:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 78:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 79:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 80:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 81:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 82:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 83:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 84:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 85:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 86:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 87:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 88:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 89:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 90:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 91:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 92:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 93:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 94:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 95:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 96:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 97:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 98:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 99:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
            elif index == 100:
                if random_exp in temp_exp_set:
                    random_exp = random.choice(experience)
                temp_exp_set.append(random_exp)
        
        if index == 0:
            self.person_0.append(', '.join(temp_exp_set))
        elif index == 1:
            self.person_1.append(', '.join(temp_exp_set))
        elif index == 2:
            self.person_2.append(', '.join(temp_exp_set))
        elif index == 3:
            self.person_3.append(', '.join(temp_exp_set))
        elif index == 4:
            self.person_4.append(', '.join(temp_exp_set))
        elif index == 5:
            self.person_5.append(', '.join(temp_exp_set))
        elif index == 6:
            self.person_6.append(', '.join(temp_exp_set))
        elif index == 7:
            self.person_7.append(', '.join(temp_exp_set))
        elif index == 8:
            self.person_8.append(', '.join(temp_exp_set))
        elif index == 9:
            self.person_9.append(', '.join(temp_exp_set))
        elif index == 10:
            self.person_10.append(', '.join(temp_exp_set))
        elif index == 11:
            self.person_11.append(', '.join(temp_exp_set))
        elif index == 12:
            self.person_12.append(', '.join(temp_exp_set))
        elif index == 13:
            self.person_13.append(', '.join(temp_exp_set))
        elif index == 14:
            self.person_14.append(', '.join(temp_exp_set))
        elif index == 15:
            self.person_15.append(', '.join(temp_exp_set))
        elif index == 16:
            self.person_16.append(', '.join(temp_exp_set))
        elif index == 17:
            self.person_17.append(', '.join(temp_exp_set))
        elif index == 18:
            self.person_18.append(', '.join(temp_exp_set))
        elif index == 19:
            self.person_19.append(', '.join(temp_exp_set))
        elif index == 20:
            self.person_20.append(', '.join(temp_exp_set))
        elif index == 21:
            self.person_21.append(', '.join(temp_exp_set))
        elif index == 22:
            self.person_22.append(', '.join(temp_exp_set))
        elif index == 23:
            self.person_23.append(', '.join(temp_exp_set))
        elif index == 24:
            self.person_24.append(', '.join(temp_exp_set))
        elif index == 25:
            self.person_25.append(', '.join(temp_exp_set))
        elif index == 26:
            self.person_26.append(', '.join(temp_exp_set))
        elif index == 27:
            self.person_27.append(', '.join(temp_exp_set))
        elif index == 28:
            self.person_28.append(', '.join(temp_exp_set))
        elif index == 29:
            self.person_29.append(', '.join(temp_exp_set))
        elif index == 30:
            self.person_30.append(', '.join(temp_exp_set))
        elif index == 31:
            self.person_31.append(', '.join(temp_exp_set))
        elif index == 32:
            self.person_32.append(', '.join(temp_exp_set))
        elif index == 33:
            self.person_33.append(', '.join(temp_exp_set))
        elif index == 34:
            self.person_34.append(', '.join(temp_exp_set))
        elif index == 35:
            self.person_35.append(', '.join(temp_exp_set))
        elif index == 36:
            self.person_36.append(', '.join(temp_exp_set))
        elif index == 37:
            self.person_37.append(', '.join(temp_exp_set))
        elif index == 38:
            self.person_38.append(', '.join(temp_exp_set))
        elif index == 39:
            self.person_39.append(', '.join(temp_exp_set))
        elif index == 40:
            self.person_40.append(', '.join(temp_exp_set))
        elif index == 41:
            self.person_41.append(', '.join(temp_exp_set))
        elif index == 42:
            self.person_42.append(', '.join(temp_exp_set))
        elif index == 43:
            self.person_43.append(', '.join(temp_exp_set))
        elif index == 44:
            self.person_44.append(', '.join(temp_exp_set))
        elif index == 45:
            self.person_45.append(', '.join(temp_exp_set))
        elif index == 46:
            self.person_46.append(', '.join(temp_exp_set))
        elif index == 47:
            self.person_47.append(', '.join(temp_exp_set))
        elif index == 48:
            self.person_48.append(', '.join(temp_exp_set))
        elif index == 49:
            self.person_49.append(', '.join(temp_exp_set))
        elif index == 50:
            self.person_50.append(', '.join(temp_exp_set))
        elif index == 51:
            self.person_51.append(', '.join(temp_exp_set))
        elif index == 52:
            self.person_52.append(', '.join(temp_exp_set))
        elif index == 53:
            self.person_53.append(', '.join(temp_exp_set))
        elif index == 54:
            self.person_54.append(', '.join(temp_exp_set))
        elif index == 55:
            self.person_55.append(', '.join(temp_exp_set))
        elif index == 56:
            self.person_56.append(', '.join(temp_exp_set))
        elif index == 57:
            self.person_57.append(', '.join(temp_exp_set))
        elif index == 58:
            self.person_58.append(', '.join(temp_exp_set))
        elif index == 59:
            self.person_59.append(', '.join(temp_exp_set))
        elif index == 60:
            self.person_60.append(', '.join(temp_exp_set))
        elif index == 61:
            self.person_61.append(', '.join(temp_exp_set))
        elif index == 62:
            self.person_62.append(', '.join(temp_exp_set))
        elif index == 63:
            self.person_63.append(', '.join(temp_exp_set))
        elif index == 64:
            self.person_64.append(', '.join(temp_exp_set))
        elif index == 65:
            self.person_65.append(', '.join(temp_exp_set))
        elif index == 66:
            self.person_66.append(', '.join(temp_exp_set))
        elif index == 67:
            self.person_67.append(', '.join(temp_exp_set))
        elif index == 68:
            self.person_68.append(', '.join(temp_exp_set))
        elif index == 69:
            self.person_69.append(', '.join(temp_exp_set))
        elif index == 70:
            self.person_70.append(', '.join(temp_exp_set))
        elif index == 71:
            self.person_71.append(', '.join(temp_exp_set))
        elif index == 72:
            self.person_72.append(', '.join(temp_exp_set))
        elif index == 73:
            self.person_73.append(', '.join(temp_exp_set))
        elif index == 74:
            self.person_74.append(', '.join(temp_exp_set))
        elif index == 75:
            self.person_75.append(', '.join(temp_exp_set))
        elif index == 76:
            self.person_76.append(', '.join(temp_exp_set))
        elif index == 77:
            self.person_77.append(', '.join(temp_exp_set))
        elif index == 78:
            self.person_78.append(', '.join(temp_exp_set))
        elif index == 79:
            self.person_79.append(', '.join(temp_exp_set))
        elif index == 80:
            self.person_80.append(', '.join(temp_exp_set))
        elif index == 81:
            self.person_81.append(', '.join(temp_exp_set))
        elif index == 82:
            self.person_82.append(', '.join(temp_exp_set))
        elif index == 83:
            self.person_83.append(', '.join(temp_exp_set))
        elif index == 84:
            self.person_84.append(', '.join(temp_exp_set))
        elif index == 85:
            self.person_85.append(', '.join(temp_exp_set))
        elif index == 86:
            self.person_86.append(', '.join(temp_exp_set))
        elif index == 87:
            self.person_87.append(', '.join(temp_exp_set))
        elif index == 88:
            self.person_88.append(', '.join(temp_exp_set))
        elif index == 89:
            self.person_89.append(', '.join(temp_exp_set))
        elif index == 90:
            self.person_90.append(', '.join(temp_exp_set))
        elif index == 91:
            self.person_91.append(', '.join(temp_exp_set))
        elif index == 92:
            self.person_92.append(', '.join(temp_exp_set))
        elif index == 93:
            self.person_93.append(', '.join(temp_exp_set))
        elif index == 94:
            self.person_94.append(', '.join(temp_exp_set))
        elif index == 95:
            self.person_95.append(', '.join(temp_exp_set))
        elif index == 96:
            self.person_96.append(', '.join(temp_exp_set))
        elif index == 97:
            self.person_97.append(', '.join(temp_exp_set))
        elif index == 98:
            self.person_98.append(', '.join(temp_exp_set))
        elif index == 99:
            self.person_99.append(', '.join(temp_exp_set))
        elif index == 100:
            self.person_100.append(', '.join(temp_exp_set))
    
    def set_person(self,index):
        if index == 0:
            self.all_persons.append(self.person_0)
        elif index == 1:
            self.all_persons.append(self.person_1)
        elif index == 2:
            self.all_persons.append(self.person_2)
        elif index == 3:
            self.all_persons.append(self.person_3)
        elif index == 4:
            self.all_persons.append(self.person_4)
        elif index == 5:
            self.all_persons.append(self.person_5)
        elif index == 6:
            self.all_persons.append(self.person_6)
        elif index == 7:
            self.all_persons.append(self.person_7)
        elif index == 8:
            self.all_persons.append(self.person_8)
        elif index == 9:
            self.all_persons.append(self.person_9)
        elif index == 10:
            self.all_persons.append(self.person_10)
        elif index == 11:
            self.all_persons.append(self.person_11)
        elif index == 12:
            self.all_persons.append(self.person_12)
        elif index == 13:
            self.all_persons.append(self.person_13)
        elif index == 14:
            self.all_persons.append(self.person_14)
        elif index == 15:
            self.all_persons.append(self.person_15)
        elif index == 16:
            self.all_persons.append(self.person_16)
        elif index == 17:
            self.all_persons.append(self.person_17)
        elif index == 18:
            self.all_persons.append(self.person_18)
        elif index == 19:
            self.all_persons.append(self.person_19)
        elif index == 20:
            self.all_persons.append(self.person_20)
        elif index == 21:
            self.all_persons.append(self.person_21)
        elif index == 22:
            self.all_persons.append(self.person_22)
        elif index == 23:
            self.all_persons.append(self.person_23)
        elif index == 24:
            self.all_persons.append(self.person_24)
        elif index == 25:
            self.all_persons.append(self.person_25)
        elif index == 26:
            self.all_persons.append(self.person_26)
        elif index == 27:
            self.all_persons.append(self.person_27)
        elif index == 28:
            self.all_persons.append(self.person_28)
        elif index == 29:
            self.all_persons.append(self.person_29)
        elif index == 30:
            self.all_persons.append(self.person_30)
        elif index == 31:
            self.all_persons.append(self.person_31)
        elif index == 32:
            self.all_persons.append(self.person_32)
        elif index == 33:
            self.all_persons.append(self.person_33)
        elif index == 34:
            self.all_persons.append(self.person_34)
        elif index == 35:
            self.all_persons.append(self.person_35)
        elif index == 36:
            self.all_persons.append(self.person_36)
        elif index == 37:
            self.all_persons.append(self.person_37)
        elif index == 38:
            self.all_persons.append(self.person_38)
        elif index == 39:
            self.all_persons.append(self.person_39)
        elif index == 40:
            self.all_persons.append(self.person_40)
        elif index == 41:
            self.all_persons.append(self.person_41)
        elif index == 42:
            self.all_persons.append(self.person_42)
        elif index == 43:
            self.all_persons.append(self.person_43)
        elif index == 44:
            self.all_persons.append(self.person_44)
        elif index == 45:
            self.all_persons.append(self.person_45)
        elif index == 46:
            self.all_persons.append(self.person_46)
        elif index == 47:
            self.all_persons.append(self.person_47)
        elif index == 48:
            self.all_persons.append(self.person_48)
        elif index == 49:
            self.all_persons.append(self.person_49)
        elif index == 50:
            self.all_persons.append(self.person_50)
        elif index == 51:
            self.all_persons.append(self.person_51)
        elif index == 52:
            self.all_persons.append(self.person_52)
        elif index == 53:
            self.all_persons.append(self.person_53)
        elif index == 54:
            self.all_persons.append(self.person_54)
        elif index == 55:
            self.all_persons.append(self.person_55)
        elif index == 56:
            self.all_persons.append(self.person_56)
        elif index == 57:
            self.all_persons.append(self.person_57)
        elif index == 58:
            self.all_persons.append(self.person_58)
        elif index == 59:
            self.all_persons.append(self.person_59)
        elif index == 60:
            self.all_persons.append(self.person_60)
        elif index == 61:
            self.all_persons.append(self.person_61)
        elif index == 62:
            self.all_persons.append(self.person_62)
        elif index == 63:
            self.all_persons.append(self.person_63)
        elif index == 64:
            self.all_persons.append(self.person_64)
        elif index == 65:
            self.all_persons.append(self.person_65)
        elif index == 66:
            self.all_persons.append(self.person_66)
        elif index == 67:
            self.all_persons.append(self.person_67)
        elif index == 68:
            self.all_persons.append(self.person_68)
        elif index == 69:
            self.all_persons.append(self.person_69)
        elif index == 70:
            self.all_persons.append(self.person_70)
        elif index == 71:
            self.all_persons.append(self.person_71)
        elif index == 72:
            self.all_persons.append(self.person_72)
        elif index == 73:
            self.all_persons.append(self.person_73)
        elif index == 74:
            self.all_persons.append(self.person_74)
        elif index == 75:
            self.all_persons.append(self.person_75)
        elif index == 76:
            self.all_persons.append(self.person_76)
        elif index == 77:
            self.all_persons.append(self.person_77)
        elif index == 78:
            self.all_persons.append(self.person_78)
        elif index == 79:
            self.all_persons.append(self.person_79)
        elif index == 80:
            self.all_persons.append(self.person_80)
        elif index == 81:
            self.all_persons.append(self.person_81)
        elif index == 82:
            self.all_persons.append(self.person_82)
        elif index == 83:
            self.all_persons.append(self.person_83)
        elif index == 84:
            self.all_persons.append(self.person_84)
        elif index == 85:
            self.all_persons.append(self.person_85)
        elif index == 86:
            self.all_persons.append(self.person_86)
        elif index == 87:
            self.all_persons.append(self.person_87)
        elif index == 88:
            self.all_persons.append(self.person_88)
        elif index == 89:
            self.all_persons.append(self.person_89)
        elif index == 90:
            self.all_persons.append(self.person_90)
        elif index == 91:
            self.all_persons.append(self.person_91)
        elif index == 92:
            self.all_persons.append(self.person_92)
        elif index == 93:
            self.all_persons.append(self.person_93)
        elif index == 94:
            self.all_persons.append(self.person_94)
        elif index == 95:
            self.all_persons.append(self.person_95)
        elif index == 96:
            self.all_persons.append(self.person_96)
        elif index == 97:
            self.all_persons.append(self.person_97)
        elif index == 98:
            self.all_persons.append(self.person_98)
        elif index == 99:
            self.all_persons.append(self.person_99)
        elif index == 100:
            self.all_persons.append(self.person_100)
    
    def set_success_rate(self,index):
        rand_rate = random.randint(0,10)  #rate > 4 means guarantee good performance
        if index == 0:
            self.person_0.append(rand_rate)
        elif index == 1:
            self.person_1.append(rand_rate)
        elif index == 2:
            self.person_2.append(rand_rate)
        elif index == 3:
            self.person_3.append(rand_rate)
        elif index == 4:
            self.person_4.append(rand_rate)
        elif index == 5:
            self.person_5.append(rand_rate)
        elif index == 6:
            self.person_6.append(rand_rate)
        elif index == 7:
            self.person_7.append(rand_rate)
        elif index == 8:
            self.person_8.append(rand_rate)
        elif index == 9:
            self.person_9.append(rand_rate)
        elif index == 10:
            self.person_10.append(rand_rate)
        elif index == 11:
            self.person_11.append(rand_rate)
        elif index == 12:
            self.person_12.append(rand_rate)
        elif index == 13:
            self.person_13.append(rand_rate)
        elif index == 14:
            self.person_14.append(rand_rate)
        elif index == 15:
            self.person_15.append(rand_rate)
        elif index == 16:
            self.person_16.append(rand_rate)
        elif index == 17:
            self.person_17.append(rand_rate)
        elif index == 18:
            self.person_18.append(rand_rate)
        elif index == 19:
            self.person_19.append(rand_rate)
        elif index == 20:
            self.person_20.append(rand_rate)
        elif index == 21:
            self.person_21.append(rand_rate)
        elif index == 22:
            self.person_22.append(rand_rate)
        elif index == 23:
            self.person_23.append(rand_rate)
        elif index == 24:
            self.person_24.append(rand_rate)
        elif index == 25:
            self.person_25.append(rand_rate)
        elif index == 26:
            self.person_26.append(rand_rate)
        elif index == 27:
            self.person_27.append(rand_rate)
        elif index == 28:
            self.person_28.append(rand_rate)
        elif index == 29:
            self.person_29.append(rand_rate)
        elif index == 30:
            self.person_30.append(rand_rate)
        elif index == 31:
            self.person_31.append(rand_rate)
        elif index == 32:
            self.person_32.append(rand_rate)
        elif index == 33:
            self.person_33.append(rand_rate)
        elif index == 34:
            self.person_34.append(rand_rate)
        elif index == 35:
            self.person_35.append(rand_rate)
        elif index == 36:
            self.person_36.append(rand_rate)
        elif index == 37:
            self.person_37.append(rand_rate)
        elif index == 38:
            self.person_38.append(rand_rate)
        elif index == 39:
            self.person_39.append(rand_rate)
        elif index == 40:
            self.person_40.append(rand_rate)
        elif index == 41:
            self.person_41.append(rand_rate)
        elif index == 42:
            self.person_42.append(rand_rate)
        elif index == 43:
            self.person_43.append(rand_rate)
        elif index == 44:
            self.person_44.append(rand_rate)
        elif index == 45:
            self.person_45.append(rand_rate)
        elif index == 46:
            self.person_46.append(rand_rate)
        elif index == 47:
            self.person_47.append(rand_rate)
        elif index == 48:
            self.person_48.append(rand_rate)
        elif index == 49:
            self.person_49.append(rand_rate)
        elif index == 50:
            self.person_50.append(rand_rate)
        elif index == 51:
            self.person_51.append(rand_rate)
        elif index == 52:
            self.person_52.append(rand_rate)
        elif index == 53:
            self.person_53.append(rand_rate)
        elif index == 54:
            self.person_54.append(rand_rate)
        elif index == 55:
            self.person_55.append(rand_rate)
        elif index == 56:
            self.person_56.append(rand_rate)
        elif index == 57:
            self.person_57.append(rand_rate)
        elif index == 58:
            self.person_58.append(rand_rate)
        elif index == 59:
            self.person_59.append(rand_rate)
        elif index == 60:
            self.person_60.append(rand_rate)
        elif index == 61:
            self.person_61.append(rand_rate)
        elif index == 62:
            self.person_62.append(rand_rate)
        elif index == 63:
            self.person_63.append(rand_rate)
        elif index == 64:
            self.person_64.append(rand_rate)
        elif index == 65:
            self.person_65.append(rand_rate)
        elif index == 66:
            self.person_66.append(rand_rate)
        elif index == 67:
            self.person_67.append(rand_rate)
        elif index == 68:
            self.person_68.append(rand_rate)
        elif index == 69:
            self.person_69.append(rand_rate)
        elif index == 70:
            self.person_70.append(rand_rate)
        elif index == 71:
            self.person_71.append(rand_rate)
        elif index == 72:
            self.person_72.append(rand_rate)
        elif index == 73:
            self.person_73.append(rand_rate)
        elif index == 74:
            self.person_74.append(rand_rate)
        elif index == 75:
            self.person_75.append(rand_rate)
        elif index == 76:
            self.person_76.append(rand_rate)
        elif index == 77:
            self.person_77.append(rand_rate)
        elif index == 78:
            self.person_78.append(rand_rate)
        elif index == 79:
            self.person_79.append(rand_rate)
        elif index == 80:
            self.person_80.append(rand_rate)
        elif index == 81:
            self.person_81.append(rand_rate)
        elif index == 82:
            self.person_82.append(rand_rate)
        elif index == 83:
            self.person_83.append(rand_rate)
        elif index == 84:
            self.person_84.append(rand_rate)
        elif index == 85:
            self.person_85.append(rand_rate)
        elif index == 86:
            self.person_86.append(rand_rate)
        elif index == 87:
            self.person_87.append(rand_rate)
        elif index == 88:
            self.person_88.append(rand_rate)
        elif index == 89:
            self.person_89.append(rand_rate)
        elif index == 90:
            self.person_90.append(rand_rate)
        elif index == 91:
            self.person_91.append(rand_rate)
        elif index == 92:
            self.person_92.append(rand_rate)
        elif index == 93:
            self.person_93.append(rand_rate)
        elif index == 94:
            self.person_94.append(rand_rate)
        elif index == 95:
            self.person_95.append(rand_rate)
        elif index == 96:
            self.person_96.append(rand_rate)
        elif index == 97:
            self.person_97.append(rand_rate)
        elif index == 98:
            self.person_98.append(rand_rate)
        elif index == 99:
            self.person_99.append(rand_rate)
        elif index == 100:
            self.person_100.append(rand_rate)

    
    def build_profiles(self):
        '''
        build complete profiles for the candidates
        '''
        for x in range(self.how_many):
            self.set_names(x)
            self.set_skills(x)
            self.set_characters(x)
            self.set_exp(x)
            self.set_success_rate(x)
            self.set_person(x)
            
    def get_name(self,person_index):
        #print(self.all_persons[person_index][0])
        return self.all_persons[person_index][0]

    def get_skills(self,person_index):
        #print(self.all_persons[person_index][1])
        return self.all_persons[person_index][1]
    
    def get_characters(self,person_index):
        return self.all_persons[person_index][2]
    
    def get_exp(self,person_index):
        return self.all_persons[person_index][3]
    
    def get_success_rate(self,person_index):
        return self.all_persons[person_index][4]
    
   
#order to randomly build profiles
if __name__ == "__main__":
    my_test = resume_generator(10)
    my_test.generate_names()
    my_test.build_profiles()
    #my_test.get_name(0)
    #my_test.get_skills(4)
    

