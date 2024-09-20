# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random


dice = []
for i in range(1, 13):
    dice.append(i)


class Inventory:
    def __init__(self):
        self.inv = []
        self.money = 100

    def add_inv(self, item):
        if item == None:
            pass
        else:
            self.inv.append(item)
        return self.inv

    def sell(self):
        sell = input('What do you want to sell?')
        for item in self.inv:
            if sell == item["item"]:
                self.inv.remove(item)
                self.money += item["cost"]/2
        return self.inv


class Shop:

    def __init__(self, money):
        self.money = money
        self.items = [
            {"class": "weapon", "item": "sword", "cost": 100, "power": 10},
            {"class": "weapon", "item": "bow", "cost": 1200, "power": 200},
            {"class": "weapon", "item": "spear", "cost": 5000, "power": 1000},
            {"class": "armor", "item": "leather armor", "cost": 100, "health": 100},
            {"class": "armor", "item": "iron armor", "cost": 1200, "health": 2000},
            {"class": "armor", "item": "diamond armor","cost": 5000, "health": 12000},
            {"class": "stat", "item": "attack", "cost": 10000, "power": 2300},
            {"class": "stat", "item": "health", "cost": 10000, "health": 28000},
            {"class": "stat", "item": "speed", "cost": 10000, "speed": 8},
            {"class": "stat", "item": "critical", "cost": 10000, "crit": 7}
        ]

    def buy(self, item_buy):
        for position in range (0,len(self.items)):
            if item_buy == self.items[position]["item"]:
                if self.items[position]["cost"] > self.money:
                    print("You don't have enough money!")
                    return None
                else:
                    self.money -= self.items[position]["cost"]
                    if self.items[position]["class"] == "stat":
                        self.items[position]["cost"] += 3000
                    return self.items[position]


class Player:

    def __init__(self, inv=[], player=False):
        self.player = player
        if player:
            self.health = 150
            self.attack = 15
            self.speed = 10
            self.crit = 10
        else:
            self.health = 100
            self.attack = 5
            self.speed = 5
            self.crit = 5

        self.inv = inv
        self.equip_weapons = []
        self.equip_armors = []
        self.total_attack = self.attack
        self.total_health = self.health
        self.speed_chance = []
        self.crit_chance = []
        for i in range(1, 101):
            self.crit_chance.append(i)
            self.speed_chance.append(i)

    def unequip_weapon(self):
        if self.equip_weapons != []:
            self.inv.append(self.equip_weapons)
            self.total_attack -= self.equip_weapons["power"]
            self.equip_weapons = []

    def unequip_armor(self):
        if self.equip_armors != []:
            self.inv.append(self.equip_armors)
            self.total_health -= self.equip_armors["health"]
            self.equip_armors = []

    def equip(self):
        if not self.player or self.inv == []:
            print("You don't have any item")
            return None
        try:
            equip = int(input("Choose which item you want to equip (position, i.e. 1,2,3)"))
        except ValueError:
            equip = 1
        if self.inv[equip - 1]["class"] == "weapon":
            self.unequip_weapon()
            self.equip_weapons = self.inv[equip - 1]
            self.inv.pop(equip - 1)
            self.total_attack = self.attack + self.equip_weapons["power"]

        else:
            self.unequip_armor()
            self.equip_armors = self.inv[equip - 1]
            self.inv.pop(equip - 1)
            self.total_health = self.health + self.equip_armors["health"]

    def add_stat(self, stat):
        if stat["item"] == "attack":
            self.attack += stat["power"]
            if self.equip_weapons == []:
                self.total_attack = self.attack
            else:
                self.total_attack = self.attack + self.equip_weapons["power"]
            

        elif stat["item"] == "health":
            self.health += stat["health"]
            if self.equip_armors == []:
                self.total_health = self.health
            else:
                self.total_health = self.health + self.equip_armors["health"]
            

        elif stat["item"] == "speed":
            self.speed += stat["speed"]

        elif stat["item"] == "critical":
            self.crit += stat["crit"]

    def roll(self):
        roll = random.choice(dice)
        return roll

    def check_death(self):
        if self.total_health <= 0:
            return False
        else:
            return True

    def dodge(self):
        dodge_chance = random.choice(self.speed_chance)
        raw_speed = (1 - (1.01)**(-self.speed))*100
        if self.player:
            print(raw_speed, "speed")
            
        if raw_speed >= dodge_chance:
            print("")
            return True

    def critical(self):
        critical = random.choice(self.crit_chance)
        raw_crit = (1-(1.05)**(-self.crit))*100
        if self.player:
            print(raw_crit, "crit")
            
        if raw_crit >= critical:
            print("")
            return True
