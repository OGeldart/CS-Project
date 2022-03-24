import time
import random
import json
from abc import ABCMeta, abstractmethod


#main class
class character(metaclass=ABCMeta):

    def __init__(self, name, lvl, hp):
        self._name = name
        self._lvl = lvl
        self._hp = hp
    
    def stats(self):
        print("Name:", self._name)
        print("Level:", self._lvl)
        print("HP:", self._hp)
            
    def attackChoice(self, attack_choice):
        self.__attack_choice = attack_choice
    
    def attack(self):

        if self.__attack_choice == 1:
            attack_points = 5
            return attack_points

        elif self.__attack_choice == 2:
            attack_points = 10
            return attack_points

        else:
            print(character.Name,"flinched and lost their turn!")

    def heal(self):

        heal_points = random.randint(18,25)
        return heal_points

#Defining of functions
def party():
    with open("party.json") as text:
        entries = text.readlines()
        members =json.loads(entries)
   # member1 = character(members[0][0], members[0][1], members[0][2], )
    #member2 = character(members[1][0], members[1][1], members[1][2], )
    #member3 = character(members[2][0], members[2][1], members[2][2], )
    #member1.stats()
    #member2.stats()
    #member3.stats()
    print("worked")
    
def venture():

    with open("Zone1.json") as text:
        entries = text.readlines()
        search =json.loads(random.choice(entries))
    monster = character(search[0], search[1], search[2], )
    monster.stats()
    print()
    print("A",monster._name,"has appeared from the depths!")
    print()

#def battle():


#venture()
party()

#TDL
#- Attack system
#- Party
#- Bags
#- 
