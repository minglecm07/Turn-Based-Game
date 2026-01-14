import random
import Characters as c
def Play(number):
    if number == 1:
        player = c.Warrior
    elif number == 2:
        player = c.Mage
    else:
        player = c.Rouge
    print(f"Your journey is begining young {player.PlayerType}")
    Round = 1
    while True:
        y = random.randint(1,3)
        if y == 1:
            enemy = c.Skeleton_Mage
        elif y == 2:
            enemy = c.Ogre
        else:
            enemy = c.Zombie_Dog
        print(f"You are now facing the {enemy.EnemyType}")
        while player.H>0 and enemy.H>0:
            if player.PlayerType == "Warrior":
                OrgAtt = player.Att
            print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
            if player.Spe>enemy.Spe:
                PlayerTurn(player, enemy)
                if player.H<=0 or enemy.H<=0:
                    continue
                EnemyTurn(player, enemy)
                if player.H <= 0:
                    if player.PlayerType == 'Warrior':
                        if player.Gaurdian == 1:
                            player.Gaurdian = 0
                            player.H = 1
                            print("Your Gaurdian Angel Saved you")
                print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
            elif enemy.Spe>player.Spe:
                EnemyTurn(player, enemy)
                if player.H <= 0:
                    if player.PlayerType == 'Warrior':
                        if player.Gaurdian == 1:
                            player.Gaurdian = 0
                            player.H = 1
                            print("Your Gaurdian Angel Saved you")
                print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
                if player.H<=0 or enemy.H<=0:
                    continue
                PlayerTurn(player, enemy)
            else:
                x = random.randint(0,1)
                if x == 1:
                    PlayerTurn(player, enemy)
                    if player.H<=0 or enemy.H<=0:
                        continue
                    EnemyTurn(player, enemy)
                    if player.H <= 0:
                        if player.PlayerType == 'Warrior':
                            if player.Gaurdian == 1:
                                player.Gaurdian = 0
                                player.H = 1
                                print("Your Gaurdian Angel Saved you")
                    print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
                else:
                    EnemyTurn(player, enemy)
                    if player.H <= 0:
                        if player.PlayerType == 'Warrior':
                            if player.Gaurdian == 1:
                                player.Gaurdian = 0
                                player.H = 1
                                print("Your Gaurdian Angel Saved you")
                    print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
                    if player.H<=0 or enemy.H<=0:
                        continue
                    PlayerTurn(player, enemy)
        if player.H <= 0:
            file = open("Leaderboard.txt", 'a')
            file.write(f"{m.Name} Round:{Round} Character:{player.PlayerType}")
            print("You Lose :(")
            break
        else:
            Round += 1
        if player.PlayerType == "Warrior":
            player.Att = OrgAtt
        if enemy.EnemyType == "Skeletion Mage":
            x = random.randint(1,4)
            if x == 1:
                enemy.MaxH = enemy.MaxH + 2
            elif x == 2:
                enemy.MaxMp = enemy.MaxMP + 2
            elif x == 3:
                enemy.Att = enemy.Att + 1
            else:
                enemy.Def = enemy.Def + 1
            print("The Skeletion Mage has grown Stronger")
        elif enemy.EnemyType == "Ogre":
            x = random.randint(1,3)
            if x == 1:
                enemy.MaxH = enemy.MaxH + 3
            elif x == 2:
                enemy.Att = enemy.Att + 1
            else:
                enemy.Def = enemy.Def + 1
            print("The Ogre has grown Stronger")
        else:
            x = random.randint(1,4)
            if x == 1:
                enemy.MaxH = enemy.MaxH + 2
            elif x == 2:
                enemy.Spe = enemy.Spe + 1
            elif x == 3:
                enemy.Att = enemy.Att + 1
            else:
                enemy.Def = enemy.Def + 1
            print("The Zombie Dog has grown Stronger")
        enemy.H = enemy.MaxH
        enemy.MP = enemy.MaxMP
        print("You Win\n\n")
        if Round%3 == 0:
            Shop()
        print("1.Will you now Rest(Restore Health) or 2.Meditate (Restore Mana)\n")
        ans = int(input())
        if ans == 1:
            player.H = player.MaxH
        else:
            player.MP = player.MaxMP
        print(f"You are now moving on to round {Round}")
def Shop(player, enemy):
    print("Along your path to the next battle you come acoss a shop\nAs you walk in the shopkeeper hears of your work killing mosters and offers you one upgrade\n\n")
    print("1.Enhanced Weapon(Attack up)\n2.Enhanced Armor(Defense up)\n3.Growth Potion(Max Health up)\n4.Magic Tomb(Max Mana up)\n5.Lighted Armor(Speed Up)\n6.Holy Book(Resets Guardian Ability)")
    x = int(input())
    if x == 1:
        player.Att = player.Att + 1
    elif x == 2:
        player.Def = player.Def +1
    elif x == 3:
        player.MaxHP = player.MaxHP + 2
        player.HP = player.HP + 2
    elif x == 4:
        player.MaxMP = player.MaxMP + 1
        player.MP = player.MP + 1
    elif x == 5:
        player.Speed = player.Speed + 1
    elif x == 6:
        player.Gaurdian = 1
    print("All enemies have also gotten stronger")
    enemy.EnemyType == "Skeletion Mage"
    x = random.randint(1,4)
    if x == 1:
        enemy.MaxH = enemy.MaxH + 2
    elif x == 2:
        enemy.MaxMp = enemy.MaxMP + 2
    elif x == 3:
        enemy.Att = enemy.Att + 1
    else:
        enemy.Def = enemy.Def + 1
    enemy.EnemyType == "Ogre"
    x = random.randint(1,3)
    if x == 1:
        enemy.MaxH = enemy.MaxH + 3
    elif x == 2:
        enemy.Att = enemy.Att + 1
    else:
        enemy.Def = enemy.Def + 1
    enemy.EnemyType == "Zombie Dog"
    x = random.randint(1,4)
    if x == 1:
        enemy.MaxH = enemy.MaxH + 2
    elif x == 2:
        enemy.Spe = enemy.Spe + 1
    elif x == 3:
        enemy.Att = enemy.Att + 1
    else:
        enemy.Def = enemy.Def + 1
def PlayerTurn(player, enemy):
    if player.Stun > 0:
        player.Stun = player.Stun - 1
    else:
        player.Block = 0
        if player.PlayerType == "Mage" and player.MP <= 1:
            player.MP = ((player.MaxMP/2)//1)
            player.Gaurdian = 0
            print("Your Guardian Angel has given you half your Mana back make the most of it")
        if player.PlayerType == "Rouge":
            player.Eva = 25
        print("Your Turn\n1:Attack\n2:Special Attack\n3:Heal\n4:Block")
        x = int(input())
        if x == 1:
            player.Damage(enemy)
        elif x == 2:
            player.SA(enemy)
        elif x == 3:
            player.Heal()
        else:
            player.Block = 1
def EnemyTurn(player, enemy):
    enemy.Block = 0
    if enemy.Stun > 0:
        enemy.Stun = enemy.Stun-1
    else:
        if enemy.EnemyType == "Skeletion Mage":
            if enemy.H <= int((enemy.MaxH*.2)//1) and enemy.MP >= 4:
                enemy.SA(player)
            elif player.H < int(((player.MaxH*.20)//1)):
                enemy.Damage(player)     
            elif enemy.H < int(((enemy.MaxH*.35)//1)) and enemy.MP >= 2:
                enemy.Heal()
            else:
                x = random.randint(0,4)
                if x == 0:
                    print("Enemy Blocked\n")
                    enemy.Block = 1
                else:
                    enemy.Damage(player)
        elif enemy.EnemyType == "Ogre":
            if enemy.H < int((enemy.H*.5)//1) and enemy.H > 7:
                enemy.SA(player)
            else:
                enemy.Damage(player)
        elif enemy.EnemyType == "Zombie Dog":
            if enemy.H < int((enemy.H*.3)//1) and enemy.MP > 0:
                enemy.SA(Player)
            else:
                x = random.randint(0,2)
                if x == 0:
                    enemy.Block = 1
                    print("Enemy Blocked\n")
                else:
                    enemy.Damage(player)
