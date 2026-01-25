import random
import Characters as c
def Play(number, name):
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
            if player.Spe>enemy.Spe:
                print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
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
            elif enemy.Spe>player.Spe:
                EnemyTurn(player, enemy)
                if player.H <= 0:
                    if player.PlayerType == 'Warrior':
                        if player.Gaurdian == 1:
                            player.Gaurdian = 0
                            player.H = 1
                            print("Your Gaurdian Angel Saved you")
                if player.H<=0 or enemy.H<=0:
                    continue
                print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
                PlayerTurn(player, enemy)
            else:
                x = random.randint(0,1)
                if x == 1:
                    print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
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
                else:
                    EnemyTurn(player, enemy)
                    if player.H <= 0:
                        if player.PlayerType == 'Warrior':
                            if player.Gaurdian == 1:
                                player.Gaurdian = 0
                                player.H = 1
                                print("Your Gaurdian Angel Saved you")
                    if player.H<=0 or enemy.H<=0:
                        continue
                    print(f"Player Health:{player.H}/{player.MaxH}\nPlayer Mana:{player.MP}/{player.MaxMP}\n\nEnemy Health:{enemy.H}/{enemy.MaxH}\nEnemy Mana:{enemy.MP}/{enemy.MaxMP}\n")
                    PlayerTurn(player, enemy)
        if player.PlayerType == "Warrior":
            player.Att = OrgAtt
        if player.H <= 0:
            if player.PlayerType == "Warrior":
                file = open("LeaderboardW.txt", 'a')
                file.write(f"{name} {Round}\n")
                resetstats(c.Warrior, c.SetWarrior)
            elif player.PlayerType == "Mage":
                file = open("LeaderboardM.txt", 'a')
                file.write(f"{name} {Round}\n")
                resetstats(c.Mage, c.SetMage)
            else:
                file = open("LeaderboardR.txt", 'a')
                file.write(f"{name} {Round}\n")
                resetstats(c.Rouge, c.SetRouge)
            resetstats(c.Skeleton_Mage, c.SetSkeleton_Mage)
            resetstats(c.Ogre, c.SetOgre)
            resetstats(c.Zombie_Dog, c.SetZombie_Dog)
            print("You Lose :(")
            break
        else:
            Round += 1
        if enemy.EnemyType == "Skeletion Mage":
            x = random.randint(1,2)
            if x == 1:
                enemy.MaxH = enemy.MaxH + 1
            elif x == 2:
                enemy.MaxMp = enemy.MaxMP + 1
            print("The Skeletion Mage has grown Stronger")
        elif enemy.EnemyType == "Ogre":
            x = random.randint(1,3)
            enemy.MaxH = enemy.MaxH + 1
            print("The Ogre has grown Stronger")
        else:
            x = random.randint(1,2)
            if x == 1:
                enemy.MaxH = enemy.MaxH + 1
            elif x == 2:
                enemy.Spe = enemy.Spe + 1
            print("The Zombie Dog has grown Stronger")
        enemy.H = enemy.MaxH
        enemy.MP = enemy.MaxMP
        print("You Win\n\n")
        if Round%4 == 0:
            Shop(player, enemy)
        print("1.Will you now Rest(Restore Health) or 2.Meditate (Restore Mana)\n")
        ans = int(input())
        y = random.randint(1,3)
        while ans !=1 and ans !=2:
            print("Invald input try again")
            x = int(input())
        if ans == 1:
            player.H = player.MaxH
        else:
            player.MP = player.MaxMP
        print(f"You are now moving on to round {Round}")
def Shop(player, enemy):
    print("Along your path to the next battle you come acoss a shop\nAs you walk in the shopkeeper hears of your work killing mosters and offers you one upgrade\n\n")
    print("1.Enhanced Weapon(Attack up)\n2.Enhanced Armor(Defense up)\n3.Growth Potion(Max Health up)\n4.Magic Tomb(Max Mana up)\n5.Lighted Armor(Speed Up)\n6.Holy Book(Resets Last Resort Ability)")
    x = int(input())
    while x !=1 and x !=2 and x !=3 and x !=4 and x !=5 and x!=6:
        print("Invald input try again")
        x = int(input())
    if x == 1:
        player.Att = player.Att + 1
    elif x == 2:
        player.Def = player.Def +1
    elif x == 3:
        player.MaxH = player.MaxH + 3
        player.H = player.H + 3
    elif x == 4:
        player.MaxMP = player.MaxMP + 2
        player.MP = player.MP + 2
    elif x == 5:
        player.Spe = player.Spe + 1
    elif x == 6:
        player.Gaurdian = 1
    print("All enemies have also gotten stronger")
    enemy = c.Skeleton_Mage
    x = random.randint(1,4)
    if x == 1:
        enemy.MaxH = enemy.MaxH + 2
    elif x == 2:
        enemy.MaxMp = enemy.MaxMP + 2
    elif x == 3:
        enemy.Att = enemy.Att + 1
    else:
        enemy.Def = enemy.Def + 1
    enemy.H = enemy.MaxH
    enemy.MP = enemy.MaxMP
    enemy = c.Ogre
    x = random.randint(1,3)
    if x == 1:
        enemy.MaxH = enemy.MaxH + 3
    elif x == 2:
        enemy.Att = enemy.Att + 1
    else:
        enemy.Def = enemy.Def + 1
    enemy.H = enemy.MaxH
    enemy.MP = enemy.MaxMP
    enemy = c.Zombie_Dog
    x = random.randint(2,4)
    if x == 1:
        enemy.MaxH = enemy.MaxH + 2
    elif x == 2:
        enemy.Spe = enemy.Spe + 1
    elif x == 3:
        enemy.Att = enemy.Att + 1
    else:
        enemy.Def = enemy.Def + 1
    enemy.H = enemy.MaxH
    enemy.MP = enemy.MaxMP
def PlayerTurn(player, enemy):
    if player.Stun > 0:
        player.Stun = player.Stun - 1
    else:
        player.Block = 0
        if player.PlayerType == "Mage" and player.MP <= 1:
            player.MP = int(((player.MaxMP/2)//1))
            player.Gaurdian = 0
            print("Last Reserves:\nYour Willpower pushes your body beyond its limit gaining half your mana back")
        if player.PlayerType == "Rouge":
            player.Eva = 25
        print("Your Turn\n1:Attack\n2:Special Attack\n3:Heal\n4:Block")
        x = int(input())
        while x !=1 and x !=2 and x !=3 and x !=4:
            print("Invald input try again")
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
            if enemy.H <= int((enemy.MaxH*.3)//1) and enemy.MP >= 4:
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
            if enemy.H <= int((enemy.MaxH*.5)//1) and enemy.H > 4:
                enemy.SA(player)
            else:
                enemy.Damage(player)
        elif enemy.EnemyType == "Zombie Dog":
            if enemy.H <= int((enemy.MaxH*.3)//1) and enemy.MP > 0:
                enemy.SA(player)
            else:
                x = random.randint(0,2)
                if x == 0:
                    enemy.Block = 1
                    print("Enemy Blocked\n")
                else:
                    enemy.Damage(player)
def resetstats(char, Org):
    #Resets stats of Characters
    char.MaxH = Org.MaxH
    char.H = Org.H
    char.MaxMP = Org.MaxMP
    char.MP = Org.MP
    char.Att = Org.Att
    char.Def = Org.Def
    char.Spe = Org.Spe
