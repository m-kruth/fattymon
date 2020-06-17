import json
import glob
import random
import time
from rich import print
from rich.console import Console
from rich.table import Column, Table
from rich.columns import Columns
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

title_table = Table(show_header=True, header_style="bold magenta")


title_table.add_column("""
███████  █████  ████████ ████████ ██    ██ ███    ███  ██████  ███    ██     
██      ██   ██    ██       ██     ██  ██  ████  ████ ██    ██ ████   ██     
█████   ███████    ██       ██      ████   ██ ████ ██ ██    ██ ██ ██  ██     
██      ██   ██    ██       ██       ██    ██  ██  ██ ██    ██ ██  ██ ██     
██      ██   ██    ██       ██       ██    ██      ██  ██████  ██   ████     
                                                                             
Like pokemon but with out-of-shape software engineers
                                                                            """)

title_table.add_row("Press 1 to Fight Computer | Press 2 to take a fat nap")


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
            print(self.description)
            return([dmg//1000, self.hp, self.buff_atk, self.buff_def])
            
    

console.print(title_table)

selection = input()

if selection == '1':
    # print("fight computer")
    fatlist = load_fattys()
    fat_len = len(fatlist)
    renderlist = fatlist.copy()
    for i in range(len(renderlist)):
        renderlist[i] = Panel(renderlist[i] + ' | ' + str(i))
    print(Columns(renderlist))
    selection = input('Pick a beast:')
    players_beast = Fatemon(fatlist[int(selection)])
    players_beast.load_info()
    players_beast.load_moves()

    computers_beast = Fatemon(fatlist[2])
    computers_beast.load_info()
    computers_beast.load_moves()

    # battle sequence
    battle_start = Markdown("# " + players_beast.name + "(player) versus " + computers_beast.name + "(computer)", style="bold red")

    console.print(battle_start)

    computers_beast_og_hp = computers_beast.hit_points
    players_beast_og_hp = players_beast.hit_points
    players_moves = players_beast.moves
    for i in range(len(players_moves)):
        players_moves[i] = Panel(players_moves[i] + ' | ' + str(i))
        


    while (computers_beast.hit_points > 0) and (players_beast.hit_points > 0):
        
        print("computers", computers_beast.name, "\nHit points:", computers_beast.hit_points)
        diff = computers_beast_og_hp - computers_beast.hit_points
        print("|" + "-"*(int(computers_beast.hit_points/10)) + " "*(int(diff/10)) + "|")
        print("players", players_beast.name, "\nHit points:", players_beast.hit_points)
        diff = players_beast_og_hp - players_beast.hit_points
        print("|" + "-"*(int(players_beast.hit_points/10)) + " "*(int(diff/10)) + "|")
        print(Columns(players_moves))
        selection = input("select a move:")
        time.sleep(1)
        if selection == '1':
            damage = players_beast.Move_1.combat()
            computers_beast.combat_dmg(damage[0])
            players_beast.combat_buff(damage[1], damage[2], damage[3])
            print("players", players_beast.name, "hit for", damage, '!')
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
