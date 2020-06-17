import json
import glob
import random
title = """
███████  █████  ████████ ████████ ██    ██ ███    ███  ██████  ███    ██     
██      ██   ██    ██       ██     ██  ██  ████  ████ ██    ██ ████   ██     
█████   ███████    ██       ██      ████   ██ ████ ██ ██    ██ ██ ██  ██     
██      ██   ██    ██       ██       ██    ██  ██  ██ ██    ██ ██  ██ ██     
██      ██   ██    ██       ██       ██    ██      ██  ██████  ██   ████     
                                                                             
Like pokemon but with out-of-shape software engineers
                                                                            """

def load_fattys():
    fatty_list = []
    template_list = glob.glob("fatemon/*")
    for template in template_list:
        with open(template) as json_file:
            data = json.load(json_file)
            fatemon = data['fatemon']['name']
            fatty_list.append(fatemon)
    return(fatty_list)

class Fatemon:
    def __init__(self, name):
        self.name = name
        self.desc = ""
        self.hit_points = 0
        self.defence = 0
        self.attack = 0
        self.moves = []

    def load_info(self):
        file = ("fatemon/" + self.name + '.json')
        with open(file) as json_file:
            data = json.load(json_file)
            self.desc = data['fatemon']['desc']
            self.hit_points = data['fatemon']['hit_points']
            self.defence = data['fatemon']['defence']
            self.attack = data['fatemon']['attack']
    
    def load_moves(self):
        file = ("fatemon/" + self.name + '.json')
        with open(file) as json_file:
            data = json.load(json_file)
            move_data = data['fatemon']['moves'][0]
            self.Move_1 = Move(move_data['name'], move_data['description'], move_data['attack'], move_data['type'], move_data['hp'], move_data['def'], move_data['atk'] ) 
            move_data = data['fatemon']['moves'][1]
            self.Move_2 = Move(move_data['name'], move_data['description'], move_data['attack'], move_data['type'], move_data['hp'], move_data['def'], move_data['atk'] ) 
            move_data = data['fatemon']['moves'][2]
            self.Move_3 = Move(move_data['name'], move_data['description'], move_data['attack'], move_data['type'], move_data['hp'], move_data['def'], move_data['atk'] ) 
            move_data = data['fatemon']['moves'][3]
            self.Move_4 = Move(move_data['name'], move_data['description'], move_data['attack'], move_data['type'], move_data['hp'], move_data['def'], move_data['atk'] ) 
        self.moves = [self.Move_1.name, self.Move_2.name, self.Move_3.name, self.Move_4.name]
    
    def yell(self):
        print("You picked", self.name)
        print(self.desc)

    def describe(self):
        print("name:", self.name)
        print("description:", self.desc)
        print("Hit Points:", self.hit_points)
        print("Moves:", self.moves)
    
    def combat_dmg(self, dmg):
        if self.defence*0.1 > dmg:
            pass
        else:
            self.hit_points -= (dmg - 0.1*self.defence)

    def combat_buff(self, heal, buff_atk, buff_def):
        self.hit_points += heal
        self.attack += buff_atk
        self.defence += buff_def

class Move:
    def __init__(self, name, desc, atk, type, hp, buff_def, buff_atk):
        self.name = name
        self.description = desc
        self.attack = atk
        self.type = type
        self.hp = hp
        self.buff_def = buff_def
        self.buff_atk = buff_atk


    def combat(self):
        if self.type == "attack":
            dmg = self.attack * random.randrange(700, 1300, 100)
            print(self.description)
            return([dmg//1000, 0 , 0, 0])
        elif self.type == "buff":
            dmg = self.attack * random.randrange(700, 1300, 100)
            return([dmg//1000, self.hp, self.buff_atk, self.buff_def])
            
    

print(title)

selection = input("[1]Fight Computer\n[2]Take a fat nap\nMake your choice:")

if selection == '1':
    print("fight computer")
    fatlist = load_fattys()
    fat_len = len(fatlist)
    for i in range(len(fatlist)):
        print('['+str(i)+']', fatlist[i])
    selection = input('Pick a beast:')
    players_beast = Fatemon(fatlist[int(selection)])
    players_beast.load_info()
    players_beast.load_moves()

    computers_beast = Fatemon(fatlist[2])
    computers_beast.load_info()
    computers_beast.load_moves()

    # battle sequence
    print(players_beast.name, "versus", computers_beast.name)


    while (computers_beast.hit_points > 0) and (players_beast.hit_points > 0):
        print("computers", computers_beast.name, "\nHit points:", computers_beast.hit_points)
        print("players", players_beast.name, "\nHit points:", players_beast.hit_points)
        print("[1]", players_beast.Move_1.name)
        print("[2]", players_beast.Move_2.name)
        print("[3]", players_beast.Move_3.name)
        print("[4]", players_beast.Move_4.name)
        selection = input("select a move:")

        if selection == '1':
            damage = players_beast.Move_1.combat()
            computers_beast.combat_dmg(damage[0])
            players_beast.combat_buff(damage[1], damage[2], damage[3])
            print("players", players_beast.name, "hit for", damage, '!')
            print("players def", players_beast.defence)
        elif selection == '2':
            damage = players_beast.Move_2.combat()
            computers_beast.combat_dmg(damage[0])
            players_beast.combat_buff(damage[1], damage[2], damage[3])
            print("players", players_beast.name, "hit for", damage, '!')
        elif selection == '3':
            damage = players_beast.Move_3.combat()
            computers_beast.combat_dmg(damage[0])
            players_beast.combat_buff(damage[1], damage[2], damage[3])
            print("players", players_beast.name, "hit for", damage, '!')
        elif selection == '4':
            damage = players_beast.Move_4.combat()
            computers_beast.combat_dmg(damage[0])
            players_beast.combat_buff(damage[1], damage[2], damage[3])
            print("players", players_beast.name, "hit for", damage, '!')
        
        if (computers_beast.hit_points < 0):
            print("player won!")


        comp_selection = str(random.randrange(1, 5, 1))
        if comp_selection == '1':
            damage = computers_beast.Move_1.combat()
            players_beast.combat_dmg(damage[0])
            computers_beast.combat_buff(damage[1], damage[2], damage[3])
            print("computers", computers_beast.name, "hit for", damage, '!')
        elif comp_selection == '2':
            damage = computers_beast.Move_2.combat()
            players_beast.combat_dmg(damage[0])
            computers_beast.combat_buff(damage[1], damage[2], damage[3])
            print("computers", computers_beast.name, "hit for", damage, '!')
        elif comp_selection == '3':
            damage = computers_beast.Move_3.combat()
            players_beast.combat_dmg(damage[0])
            computers_beast.combat_buff(damage[1], damage[2], damage[3])
            print("computers", computers_beast.name, "hit for", damage, '!')
        elif comp_selection == '4':
            damage = computers_beast.Move_4.combat()
            players_beast.combat_dmg(damage[0])
            computers_beast.combat_buff(damage[1], damage[2], damage[3])
            print("computers", computers_beast.name, "hit for", damage, '!')

        if (players_beast.hit_points < 0):
            print("computer won!")


elif selection == '2':
    print("enjoy your nap, fatty")
else:
    print("what are you, stupid? Try again!")
