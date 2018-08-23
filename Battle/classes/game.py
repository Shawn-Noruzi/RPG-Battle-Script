import random
from classes.magic import spell
from colorama import Fore
from colorama import Style
from colorama import init
import pprint 
init()


class Person: 
    def __init__(self, name, hp,mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp 
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items =  items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]
    
    def generate_dmg(self):
        return random.randrange(self.atkl,self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 :
            self.hp = 0
            return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp


    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i=1
        print("\n" + "   " + f"{Style.BRIGHT}" + self.name + f"{Style.RESET_ALL}")
        print(f"     {Fore.CYAN} Actions {Style.RESET_ALL}")
        for item in self.actions:
            print("       " + str(i) + "." , item)
            i += 1
        print("\n")


    def choose_magic(self):
        i=1
        print("\n")
        print(f"    {Fore.BLUE} Magic {Style.RESET_ALL}")
        for spell in self.magic:
            print("      " + str(i) + "." , spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print("\n")    
        

    def choose_item(self):
        i=1
        print("\n")
        print(f"    {Fore.GREEN} Items {Style.RESET_ALL}")
        for item in self.items:
            print("      " + str(i) + "." , item["Item"].name, ":", item["Item"].description, "("+ str(item["Quantity"]) + "x)")
            i += 1
        print("\n")


    def choose_target(self, enemies):
        i = 1
        print("\n" + f"{Style.BRIGHT} TARGET: {Style.RESET_ALL}" )
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("       " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose Target: ")) - 1
        return choice


    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0: 
            hp_bar += "█"
            bar_ticks -= 1
        
        while len(hp_bar) < 50: 
            hp_bar += " "
        
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0: 
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else: 
            current_hp = hp_string
        
        print("                                    HP                                    ")
        print("                                    __________________________________________________")
        print( str(self.name) + "                   " + current_hp + f"|{Fore.RED}" + hp_bar + f"{Style.RESET_ALL}|")


    def get_stats(self):
        hp_bar = ""
        hp_ticks = ( self.hp / self.maxhp ) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while hp_ticks >= 0:
            hp_bar += "█"
            hp_ticks -= 1
        
        #white space
        while len(hp_bar) < 26:
            hp_bar += " "
        
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "
        
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0: 
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else: 
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0: 
                current_mp += " "
                decreased -= 1
            
            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                                    HP                                     MP")
        print("                                    __________________________             __________")
        print( str(self.name) + "                   " + current_hp + f"|{Fore.GREEN}" + hp_bar + f"{Style.RESET_ALL}|    " + current_mp + f"|{Fore.BLUE}"+ mp_bar + f"{Style.RESET_ALL}|")
