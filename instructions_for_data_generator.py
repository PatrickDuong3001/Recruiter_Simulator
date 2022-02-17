import random
import pygame

#There are many methods to do this task. Below are just for pure python programming

#In the terminal, type in this line to work with pygame:
#pip install pygame

#In the terminal, type in these command lines to help generate random first and last names to form full names. 
#pip install wheel
#pip install names

#You can use it with SQL or read predefined files from Excel/csv files for this step. 
#predefined lists of values
Names = []    #use https://moonbooks.org/Articles/How-to-generate-random-names-first-and-last-names-with-python-/ to generate random names

Skills = ["Java","C++","Python","VHDL",...]  #as many as possible
 
characteristic = ["hard-wording","handsome","can-do attitude",...] #as many as possible. If too much work, can ignore this

experience_job_title = ["software engineer","software engineer intern",...] #as many as possible. 



#more than 100 empty lists: 
person_1= []
person_2 = []
...

#more than 100 empty joined characteristics
character_for_person_1 = []
character_for_person_2 = []
...

#more than 100 empty joined skills 
skills_for_person_1 = []
skills_for_person_2 = []
...

#more than 100 empty joined experience:
experience_for_person_1 = []
experience_for_person_2 = []
...

#an empty list to contain persons later: 
all_persons = []


class Generate()
    def __init__(self,argument_1,argument_2):
        #start generating names here when the class is called and put these names into 'Names' list.
        
        #start appending/adding values to character_for_person lists. Each character_for_person list has a random length with random(). Max: 5
        #use choice() in python to choose characters from above predefined list to increase random. 
        character_for_person_1 = ["hardworking","handsome"]
        character_for_person_2=  ["hardworking","handsome","can-do"]
        ...
        
        #start appending/adding values to skills_for_person lists. Each skills_for_person list has a random length with random(). Max: 5
        #use choice() in python to choose skills from above predefined list to increase random. 
        skills_for_person_1 = ["java","python"]
        kills_for_person_2 = ["C++"]
        ...
        
        #start appending/adding values to experience_for_person lists. Each experience_for_person list has a random length with random(). Max: 5
        #use choice() in python to choose experience from above predefined list to increase random. 
        experience_for_person_1 = ["software engineer", "intern"]
        experience_for_person_2 = ["IT intern"]
        ...
        
        
        #start appending or adding vavlues into person arrays.
        #then, put all the 'skills', 'characteristics','experience_job_title' lists into those persons lists
        #to increase randomness of choice of skills and characteristics and job_experience, use choice() in python
        person_1 = ["Name",skills_for_person_1, experience_for_person_1, character_for_person_1,random.randint(0,100)]
        person_2 = ["name",skills_for_person_2, experience_for_person_2, character_for_person_2,random.randint(0,100)]
        ...
        #last index in person list is the success_rate. This will not be shown on resume, but will decide if the admitted 
        #person fail the job or not.  
        
        
        #then have one array for persons:
        all_persons = [person_1,person_2,...]
    
    def return_name(person_index):
        return all_persons[person_index][1]
    
    def return_skills(person_index):
        string = ",".join(all_persons[person_index][2]) #create a long string so that it will be displayed on the front-end resume
        return string
    
    def return_exp(person_index):
        string = ",".join(all_persons[person_index][3]) #create a long string so that it will be displayed on the front-end resume
        return string
    
    def return_characters(person_index):
        string = ",".join(all_persons[person_index][4]) #create a long string so that it will be displayed on the front-end resume
        return string