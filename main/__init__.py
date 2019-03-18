from main.Fighters import Fighter, fight
'''
Created on Feb 27, 2019

@author: cdwli
''' 
# name, age, damage, defence, speed maxHp
test = Fighter("test", 1, 8, 2, 8, 2)

player = Fighter

points = 20
damage = 0
defence = 0
speed = 0
maxHp = 0

def setup():
    name = input("Who are you?")
    age = input("How old are you?")
    global player, points, damage, defence, speed, maxHP

    damage = setStat("Damage")
    points = points - damage
    defence = setStat("Defence")
    points = points - defence
    speed = setStat("Speed")
    points = points - speed
    maxHp = setStat("Max HP")
    points = points - maxHp

    player = Fighter(name, age, damage, defence, speed, maxHp)


def setStat(statName):
    print("------------------")
    print("Damage: "+ str(damage))
    print("Defence: "+ str(defence))
    print("Speed: "+ str(speed))
    print("Max HP: "+ str(maxHp))
    print("------------------")
    print("You have "+ str(points) +" points remaining")
    stat = input(statName+"?")
    return int(stat)

def brawl():

    paladin = Fighter("Pally", 28, 2, 8, 2, 8)
    rogue = Fighter("Speedy-boy", 17, 8, 2, 8, 2)

    answer = input("Fight a paladin or a rogue?")
    if answer in ["paladin", "Paladin", "p", "P"]:
        fight(player, paladin)
        player.modGold(45)
    if answer in ["rogue", "Rogue", "r", "R"]:
        fight(player, rogue)
        player.modGold(60)
    play()

def shop():

    while True:
        answer = input("You can heal or leave")
        if answer in ["heal", "Heal", "h", "H"]:
            answer = input("How much would you like to heal?")
            if player.gold >= int(answer):
                player.modHealth( int(answer) )
                player.modGold( -int(answer) )
            else:
                print("Get more money and come back")
                
        elif answer in ["leave", "Leave","l","L"]:
            print ("You leave the shop")
            break;
    play()

def play():
    if player.health > 0:
        player.display()
        answer = input("Would you like to shop or brawl?")
        if answer in ["shop", "Shop","s","S"]:
            shop()
        elif answer in ["brawl", "Brawl","b","B"]:
            brawl()
    else:
        print("You loose")  
def main():
    setup()
    play()

if __name__ == '__main__':
    main()
    