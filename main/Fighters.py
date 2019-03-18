import random

'''
Created on Feb 26, 2019

@author: cdwli
'''

def fight(fighter1, fighter2):
    '''
    This is where the fighters fight
    '''
    print("Fight!")
    
    turn = 0
    while fighter1.health > 0 and fighter2.health > 0:
        turn+=1
        
        if flipSpeed(fighter1.speed) == 0:
            fighter1.attack(fighter2)
        elif turn % flipSpeed(fighter1.speed) == 0:
            fighter1.attack(fighter2)
            
        if fighter2.health > 0:
            if flipSpeed(fighter2.speed) == 0:
                fighter2.attack(fighter1)
            elif turn % flipSpeed(fighter2.speed) == 0:
                fighter2.attack(fighter1)

    if fighter1.health <= 0:
        print (fighter1.name +" died!")
        print (fighter2.name + " has "+ str(fighter2.health)+"/"+str(fighter2.maxHealth)+" health.")
    elif fighter2.health <= 0:
        print (fighter2.name +" died!")
        print (fighter1.name + " has "+ str(fighter1.health)+"/"+str(fighter1.maxHealth)+" health.")

def flipSpeed(speed):
    flip = ( 10 * round((1 - speed/10 )))
    return flip

class Fighter(object):
    '''
    Fighters are made here. Its a fighter factory
    '''
    def __init__(self, name, age, damage, defence, speed, maxHealth):
        self.name = name
        self.age = age
        self.damage = damage
        self.defence = defence
        self.speed = speed
        self.maxHealth = maxHealth*25 + 50
        self.health = maxHealth*25 + 50
        self.gold = 10
        
    def attack(self, enemy):
        dam = (self.damage*(random.randint(1,self.damage)/self.damage))
        
        if enemy.defence > 0:
            hit =  dam - (dam * ((enemy.defence) / 11))
        else:
            hit =  dam
            
        enemy.health = enemy.health - hit
        print (self.name+ " attacked " +enemy.name+ " for "+ str(hit)+" damage!")

    def defend(self):
        return self.defence
    
    def modGold(self, mod):
        self.gold += mod
    
    def getGold(self):
        return self.gold
    
    def modHealth(self, mod):
        self.health += mod
    
    def display(self):
        print("------------------")
        print("Damage: "+ str(self.damage))
        print("Defence: "+ str(self.defence))
        print("Speed: "+ str(self.speed))
        print("HP: "+ str(self.health)+"/"+str(self.maxHealth))
        print("Gold: "+ str(self.gold))
        print("------------------")