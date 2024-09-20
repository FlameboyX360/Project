# -*- coding: utf-8 -*-"
"""
Created on Sat Jul  6 10:00:16 2024

@author: chris
"""
import Shop as shp
#import time

class Dungeon:
    
    def __init__(self, player):
        self.mob = shp.Player()
        self.player = player
        self.player_max_hp = self.player.total_health
        self.r_number = 1
        self.rewards = 0
    
    def room(self):
        print()
        print("*"*20)
        print("ROOM ", str(self.r_number))
        print("*"*20)
        print()
        if self.r_number % 25 == 0:
            print("ALERT! BOSS HAS ARRIVED!!!")
            self.mob.total_health = round((80*(1.15**self.r_number)) + self.mob.health)
            self.mob.total_attack = round((8*(1.115**self.r_number)) + self.mob.attack)
            self.mob.speed = 20
            self.crit = 20
        elif self.r_number % 5 == 0:
            print("ALERT! MINI BOSS!!!")
            self.mob.total_health = round((40*(1.15**self.r_number)) + self.mob.health)
            self.mob.total_attack = round((4*(1.115**self.r_number)) + self.mob.attack)   
        else:
            self.mob.total_health = round((20*(1.15**self.r_number)) + self.mob.health)
            self.mob.total_attack = round((2*(1.115**self.r_number)) + self.mob.attack)
    
    def check_win(self):
        if not self.mob.check_death():
            print("Enemy has been killed!")
            print("You win!")
            self.reward()
            self.r_number += 1
            self.player.total_health = self.player_max_hp
            return True
        elif not self.player.check_death():
            print("You have been killed!")
            print("You lose!")
            self.player.total_health = self.player_max_hp
            return False
        
    def fight(self):
        print("")
        #time.sleep(1)
        player_choice = input("Roll? (Y/N) ")
        if player_choice.lower() == "n" or player_choice.lower() == "no":
            return None
        else:
            player_roll = self.player.roll()
        mob_roll = self.mob.roll()
        print(f"You rolled {player_roll} and enemy rolled {mob_roll}")
        if player_roll >= mob_roll:
            print("You attack!")
            crit  = self.player.critical()
            dodge = self.mob.dodge()
            #time.sleep(1)
            if dodge:
                print("DODGE!")
                print("")
                return dodge
            elif crit:
                print("CRIT!")
                #time.sleep(1)
                print(" ")
                self.mob.total_health -= 2*self.player.total_attack
                return self.mob.check_death()
            else:
                print(" ")
                self.mob.total_health -= self.player.total_attack
                return self.mob.check_death()
        else:
            print("Enemy attacks!")
            dodge = self.player.dodge()
            crit = self.mob.critical()
            #time.sleep(1)
            if dodge:
                return dodge
            elif crit:
                print("CRIT!")
                #time.sleep(1)
                print("")
                self.player.total_health -= 2*self.mob.total_attack
                return self.player.check_death()
            else:
                print("")
                self.player.total_health -= self.mob.total_attack
                return self.player.check_death()
            
    def reward(self):
        reward = 0
        
            
        if  self.r_number <= 25:
            reward = round( 2 * ( self.r_number ** 1.6) + 100)
        elif self.r_number <=50:
            reward = round( 3 * ( self.r_number ** 1.75))
        elif  self.r_number <=75:
            reward = round( 3 * ( self.r_number ** 1.85))
        elif  self.r_number <= 90:
            reward = round( 4 * ( self.r_number ** 2.1))
        elif self.r_number <=100:
            reward = round( 5 * ( self.r_number ** 2.25))
        else:
            reward = round( 7 * ( self.r_number ** 2.5))
        
        if self.r_number % 25 == 0:
            reward += round(reward*1.25)
            
        if  self.r_number % 5 == 0:
            reward += round(reward*0.75)
            
        print("Gain", reward, "gold")
        self.rewards += reward
        
  
        