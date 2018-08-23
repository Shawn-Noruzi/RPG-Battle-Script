from classes.game import Person
from classes import magic
from colorama import init
from colorama import Fore
from colorama import Style
from classes.magic import spell
from classes.inventory import Item
import random
init()


#create black magic
fire = spell("Fire", 15, 600, "black")
thunder = spell("Thunder", 15, 600, "black")
blizzard = spell("Blizzard", 15, 600, "black")
meteor = spell("Meteor", 50, 1200, "black")
quake = spell("Quake", 30, 940, "black")

#create white magic
cure = spell("Cure", 12, 620, "white")
cura = spell("Cura", 20, 1540, "white")


#creat some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of 1 party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 dmg", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, cure]

player_items = [{"Item" : potion, "Quantity": 15},
                {"Item" : hipotion, "Quantity": 5},
                {"Item" : superpotion, "Quantity": 3},
                {"Item" : elixer, "Quantity": 2},
                {"Item" : hielixer, "Quantity": 1},
                {"Item" : grenade, "Quantity": 5}]

#Instantiate People
player1 = Person(" Batman", 3260, 165, 300, 34, player_spells, player_items)
player2 = Person(" Walrus", 4160, 105, 200, 34, player_spells, player_items)
player3 = Person(" Noodle", 3000, 265, 150, 34, player_spells, player_items)

players = [player1, player2, player3]



enemy1 = Person(" Agumon", 2060, 500, 300, 325, enemy_spells, [])
enemy2 = Person(" Pukmon", 5260, 621, 300, 225, enemy_spells, [])
enemy3 = Person(" Lulmon", 3060, 600, 300, 125, enemy_spells, [])
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print("\n")
print(f"     {Fore.RED} You're being Attacked! {Style.RESET_ALL}")

while running:
    print("      ==========================")

    print("\n\n")
        
    for player in players:
        player.get_stats()
        print("\n")


    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_dmg()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_dmg(dmg)
            print("\n")
            print("           You attacked" + enemies[enemy].name + "for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ","") + "has been killed!")
                del enemies[enemy]
        elif index == 1: 
            player.choose_magic()
            magic_choice = int(input("    Choose Magic:"))-1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_dmg()

            current_mp = player.get_mp()
       
            if spell.cost > current_mp:
                       print(f"           {Fore.RED} Not enough MP! {Style.RESET_ALL}")
                       continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(f"           {Fore.GREEN}" + "\n" + spell.name + " heals for", str(magic_dmg), "HP. ")
                print(f"{Style.RESET_ALL}")

            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(magic_dmg)


                print(f"{Fore.BLUE}")
                print('\n           ' + player.name + " used " + spell.name + ' deals', str(magic_dmg), 'points of damage to' + enemies[enemy].name)
                print(f"{Style.RESET_ALL}")
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ","") + "has been killed!")
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1 

            if item_choice == -1:
                continue

            item = player.items[item_choice]["Item"]

            if player.items[item_choice]["Quantity"] == 0:
                print(f"{Fore.RED}")
                print('           None left...')
                print(f"{Style.RESET_ALL}")
                continue

            player.items[item_choice]["Quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(f"{Fore.GREEN}")
                print('\n           ' + item.name + ' heals for', str(item.prop), 'HP')
                print(f"{Style.RESET_ALL}")

            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp

                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(f"{Fore.GREEN}")
                print('\n           ' + item.name + ' Fully Restores HP/MP')
                print(f"{Style.RESET_ALL}")

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(item.prop)

                print(f"{Fore.RED}")
                print('\n           ' + item.name + ' deals for', str(item.prop), 'points of dmg to ' + enemies[enemy].name)
                print(f"{Style.RESET_ALL}")
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ","") + "has been killed!")
                    del enemies[enemy]

    #check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies +=1

    for player in players:
        if player.get_hp() == 0:
            defeated_players +=1

    #check if player has won
    if defeated_enemies == 2:
        print(f"           {Fore.GREEN} You Win! {Style.RESET_ALL}")
        running = False

    #check if enemy won
    elif defeated_players == 2:
        print(f"           {Fore.GREEN} Your enemies have defeated you! {Style.RESET_ALL}")
        running = False

    #enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0,3)
        print(enemy_choice)

        if enemy_choice == 0:
            #choose attack
            target = random.randrange(0,3)
            enemy_dmg = enemies[0].generate_dmg()
            players[target].take_dmg(enemy_dmg)
            print(enemy.name.replace(" ","") + "           attacks" + players[target].name.replace(" ","") + "for", enemy_dmg)
            print(f"{Style.RESET_ALL}")
        
