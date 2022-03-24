import time
import random

# defining of classes
# Basic class for enemies

class base:

    def __init__(self, attack_choice):

        self.__attack_choice = attack_choice


    def attack(self):

        if self.__attack_choice == 1:
            attack_points = random.randint(18,25)
            return attack_points

        elif self.__attack_choice == 2:
            attack_points = random.randint(10,35)
            return attack_points

        else:
            print(character.Name,"flinched and lost their turn!")

    def heal(self):

        heal_points = random.randint(18,25)
        return heal_points    


class monster:
    
    def __init__(monster, Name, Level, HP,):
        monster.Name = Name
        monster.Level = Level
        monster.HP = HP
        Level == random.randint(1, 15)
        
    def stats(monster):
        print("Name:", monster.Name)
        print("Level:", monster.Level)
        print("HP:", monster.HP)
        
    def appear(monster):  
        print("A",monster.Name,"has appeared from the depths!")
        print()
        time.sleep(1)


        
#Player's characters
class character:
    
    def __init__(character, Name, Level, HP,):
        character.Name =  Name
        character.Level =  Level
        character.HP = HP

    def stats(character):
        print("Name:", character.Name)
        print("Level:", character.Level)
        print("HP:", character.HP)

#Defining of functions
# One of the game's main mechanics
def Venture():
    with open("Zone1.json") as dex:
        entries = dex.readlines()
        search =(random.choice(entries))
        entry = search.strip('\n')
    enemy = monster(2, 2, 5)
    
    enemy.appear()
    enemy.stats()
    battle_continue = True
    while battle_continue == True:
        print("\nATTACKS\n1. Close range attack\n2. Far range attack\n3. Heal")
        attack_choice = eval(input("\nSelect an attack: "))

        # monster selects an attack, but focuses on attacking if health is full.  
        if monster.HP == 100:
            monster_choice = random.randint(1,2)

        else:
            monster_choice = random.randint(1,3)

        monster = base(monster_choice)
        character = base(attack_choice)
        

        if attack_choice == 1 or attack_choice == 2:
            damage_to_monster = character_pokemon.attack()
            heal_self = 0
            print("You dealt",damage_to_monster,"damage.")

        if monster_choice == 1 or monster_choice ==2:
            damage_to_character = monster.attack()
            heal_monster = 0
            print("monster dealt", damage_to_character, "damage.")

        if attack_choice == 3:
            heal_self = character_pokemon.heal()
            damage_to_monster = 0
            print("You healed",heal_self,"health points.")

        if monster_choice == 3:
            heal_monster = monster.heal()
            damage_to_character = 0
            print("monster healed", heal_monster, "health points.")

        character_health = character_health - damage_to_character + heal_self
        monster_health = monster_health - damage_to_monster + heal_monster

        # Pokemon health points are limited by a min of 0 and a max of 100.
        if character_health > 100:
            character_health = 100

        elif character_health <= 0:
            character_health = 0
            battle_continue = False

        if monster_health > 100:
            monster_health = 100

        elif monster_health <= 0:
            monster_health = 0
            battle_continue = False

        print("Your current health is", character_health)
        print("monster's current health is", monster_health)


       
Venture()    
#input('Press ENTER to exit')

#TDL
#- Party
#- 
#- 
