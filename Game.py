import random
import Characters as c
import Main as m
if m.x == 1:
    player = c.Warrior
elif m.x == 2:
    player = c.Mage
else:
    player = c.Rouge
print(f"Your journey is begining young {player.PlayerType}")
Round = 0
def PlayerTurn():
    if player.Stun > 0:
        player.Stun = player.Stun - 1
    else:
        player['Block'] = 0
        if player.PlayerType == "Rouge":
            player.Eva = 25
        print("Your Turn\n1:Attack\n2:Special Attack\n3:Heal\n4:Block")
        x = int(input())
        if x == 1:
            c.player.Damage(enemy)
        elif x == 2:
            c.player.SA(enemy)
        elif x == 3:
            c.player.Heal()
        else:
            player.Block = 1
def EnemyTurn():
    enemy.Block = 0
    if player.H < int(((player.Hmax*.20)//1)):
        c.enemy.Damage(Player)     
    elif enemy.H < int(((enemy.Hmax*.35)//1)) and enemy.MP >= 2:
        c.enemy.Heal()
    else:
        x = random.randint(0,3)
        if x == 0:
            print("Enemy Blocked\n")
            enemy['Block'] = 1
        else:
            c.enemy.Damage(Player)
while True:
    x = random.randint(1,3)
    if m.x == 1:
        enemy = c.Skeleton_Mage
    elif m.x == 2:
        enemy = c.Ogre
    else:
        enemy = c.Zombie_Dog
    print(f"You are now facing the {enemy.EnemyType}")
    while player.H>0 and enemy.H>0:
        print(f"Player Health:{player.H}/{player.Hmax}\nPlayer Mana:{player.MP}/{player.MPmax}\n\nEnemy Health:{enemy.H}/{enemy.Hmax}\nEnemy Mana:{enemy.MP}/{enemy.MPmax}\n")
        if player.Spe>enemy.Spe:
            PlayerTurn()
            if player.H<0 or enemy.H<0:
                continue
            EnemyTurn()
            if player.H <= 0:
                if player.PlayerType == 'Warrior':
                    if player.Gaurdian == 1:
                        player.Gaurdian = 0
                        player.H = 1
                        print("Your Gaurdian Angel Saved you")
            print(f"Player Health:{player.H}/{player.Hmax}\nPlayer Mana:{player.MP}/{player.MPmax}\n\nEnemy Health:{enemy.H}/{enemy.Hmax}\nEnemy Mana:{enemy.MP}/{enemy.MPmax}\n")
        elif enemy.Spe>player.Spe:
            EnemyTurn()
            if player.H <= 0:
                if player.PlayerType == 'Warrior':
                    if player.Gaurdian == 1:
                        player.Gaurdian = 0
                        player.H = 1
                        print("Your Gaurdian Angel Saved you")
            print(f"Player Health:{player.H}/{player.Hmax}\nPlayer Mana:{player.MP}/{player.MPmax}\n\nEnemy Health:{enemy.H}/{enemy.Hmax}\nEnemy Mana:{enemy.MP}/{enemy.MPmax}\n")
            if player.H<0 or enemy.H<0:
                continue
            PlayerTurn()
        else:
            x = random.randint(0,1)
            if x == 1:
                PlayerTurn()
                if player.H<0 or enemy.H<0:
                    continue
                EnemyTurn()
                if player.H <= 0:
                    if player.PlayerType == 'Warrior':
                        if player.Gaurdian == 1:
                            player.Gaurdian = 0
                            player.H = 1
                            print("Your Gaurdian Angel Saved you")
                print(f"Player Health:{player.H}/{player.Hmax}\nPlayer Mana:{player.MP}/{player.MPmax}\n\nEnemy Health:{enemy.H}/{enemy.Hmax}\nEnemy Mana:{enemy.MP}/{enemy.MPmax}\n")
            else:
                EnemyTurn()
                if player.H <= 0:
                    if player.PlayerType == 'Warrior':
                        if player.Gaurdian == 1:
                            player.Gaurdian = 0
                            player.H = 1
                            print("Your Gaurdian Angel Saved you")
                print(f"Player Health:{player.H}/{player.Hmax}\nPlayer Mana:{player.MP}/{player.MPmax}\n\nEnemy Health:{enemy.H}/{enemy.Hmax}\nEnemy Mana:{enemy.MP}/{enemy.MPmax}\n")
                if player.H<0 or enemy.H<0:
                    continue
                PlayerTurn()
    if player.H <= 0:
        print("You Lose :(")
        break
    else:
        Round += 1
        print("You Win ")
    print(f"You are now moving on to round {round}")
