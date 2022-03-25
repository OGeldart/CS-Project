import time
import random
import json
from abc import ABCMeta, abstractmethod
import pygame


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
            
#Defining of functions
# One of the game's main mechanics
def venture():

    with open("zone1.json") as text:
        entries = text.readlines()
        search =json.loads(random.choice(entries))
    monster = character(search[0], search[1], search[2], )
    monster.stats()
    print()
    print(monster._name,"has appeared from the depths!")
    print()

while True:
    while True:   
        venture()
        reset = input("Press any key to reset...")
        break

