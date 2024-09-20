

import os
import time
import Shop as shp
import Dungeon as dng

inv= shp.Inventory()
player = shp.Player(inv.inv, player = True)

class Action:
    shop = shp.Shop(inv.money)
    def buy():
        
        print(f'''Welcome to My Shop
Your money: {Action.shop.money} gold
Shop: 
      class : {Action.shop.items[0]["class"]} , item : {Action.shop.items[0]["item"]} ,  cost : {Action.shop.items[0]["cost"]},  power : {Action.shop.items[0]["power"]} 
      class : {Action.shop.items[1]["class"]} , item : {Action.shop.items[1]["item"]} ,  cost : {Action.shop.items[1]["cost"]},  power : {Action.shop.items[1]["power"]} 
      class : {Action.shop.items[2]["class"]} , item : {Action.shop.items[2]["item"]} ,  cost : {Action.shop.items[2]["cost"]},  power : {Action.shop.items[2]["power"]} 
      class : {Action.shop.items[3]["class"]} , item : {Action.shop.items[3]["item"]},  cost : {Action.shop.items[3]["cost"]},  health : {Action.shop.items[3]["health"]} 
      class : {Action.shop.items[4]["class"]} , item : {Action.shop.items[4]["item"]},  cost : {Action.shop.items[4]["cost"]},  health : {Action.shop.items[4]["health"]} 
      class : {Action.shop.items[5]["class"]} , item : {Action.shop.items[5]["item"]},  cost :{Action.shop.items[5]["cost"]},  health : {Action.shop.items[5]["health"]} 
      class : {Action.shop.items[6]["class"]} , item : {Action.shop.items[6]["item"]} ,  cost : {Action.shop.items[6]["cost"]},  power : {Action.shop.items[6]["power"]} 
      class : {Action.shop.items[7]["class"]} , item : {Action.shop.items[7]["item"]} ,  cost : {Action.shop.items[7]["cost"]},  health : {Action.shop.items[7]["health"]}
      class : {Action.shop.items[8]["class"]} , item : {Action.shop.items[8]["item"]} ,  cost : {Action.shop.items[8]["cost"]},  speed : {Action.shop.items[8]["speed"]}
      class : {Action.shop.items[9]["class"]} , item : {Action.shop.items[9]["item"]} ,  cost : {Action.shop.items[9]["cost"]},  crit : {Action.shop.items[9]["crit"]}
    ''')
        item_buy = (input("What do you want to buy? (enter item's name) "))
        try:
            quantity = int(input("How much? "))
        except ValueError:
            quantity = 1
        for i in range(0,quantity):
            item = Action.shop.buy(item_buy)
            if not item:
                inv.money = Action.shop.money
                return None
            elif item["class"] == "stat":
                player.add_stat(item)
            else:
                inv.add_inv(item)
        inv.money = Action.shop.money
        Action.check_inv()
       
       
    
    def sell():
        Action.check_inv()
        item_sell = inv.sell()
        print(item_sell)
        print(inv.money)
    
    def check_inv():
        print("Here's is your inventory:")
        if inv.inv == []:
            print("None")
        else:
            for item in inv.inv:
                print(item)
        print(f'''  
            
              Health: {player.total_health}  
              Attack: {player.total_attack} 
              Speed: {player.speed} 
              Critical: {player.crit}
              ''')
        print(f"{inv.money} gold")

    def player_equip():
        Action.check_inv()
        player.equip()
        print(f'''You are currently equipped {player.equip_weapons["item"] if player.equip_weapons else None}
              and {player.equip_armors["item"] if player.equip_armors else None}''')
        return inv.inv
    
    def player_unequip():
        choice = input("Weapon or armor?")
        if choice == "weapon":
            player.unequip_weapon()
        elif choice == "armor":
            player.unequip_armor()
        print("Successfully unequipped")
            
              
    def do_dungeon():
        dung = dng.Dungeon(player)
        print("*"*50)
        print("Welcome to MY DUNGEON! ")
        print("*"*50)
        
        y = True
        while y:
            #time.sleep(1)
            dung.room()
            #1time.sleep(2)
            x = True
            print(f"Enemies health: {dung.mob.total_health} and damage: {dung.mob.total_attack}")
            print(f"Your health: {dung.player.total_health} and damage: {dung.player.total_attack}")
            while x:
                x = dung.fight()
                if x == None:
                    inv.money += dung.rewards
                    Action.shop.money = inv.money
                    print(inv.money)
                    return None
                else:
                    print(f"Enemies health: {dung.mob.total_health} and damage: {dung.mob.total_attack}")
                    print(f"Your health: {dung.player.total_health} and damage: {dung.player.total_attack}") 
                    if not player.check_death():
                        inv.money += dung.rewards
                        Action.shop.money = inv.money
                        print(inv.money)
                    y = dung.check_win()  
    

        
        
    
class Game:    
    print("*"*50)
    print("Welcome to MY RPG GAME!")
    print("*"*50)
    while True:
        print('''Please choose from the following action:
              1. Buy items
              2. Sell items
              3. Check inventory
              4. Equip items
              5. Unequip items
              6. Do Dungeon
              7. Exit''')
    
        option = input("Enter your choice (number): ")
        if option == "1":
            Action.buy()
        elif option == "2":
            Action.sell()
        elif option == "3":
            Action.check_inv()
        elif option == "4":
            Action.player_equip()
        elif option == "5":
            Action.player_unequip()
        elif option == "6":
            Action.do_dungeon()
        elif option == "7":
            print("Exiting...")
            time.sleep(5)
            os.system('cls')
            break
        else:
            print("You bozo")



