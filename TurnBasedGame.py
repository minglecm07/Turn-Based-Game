import random
player = {'Hmax':0, 'H': 15, 'MPmax': 4, 'MP': 4, 'Att': 6, 'Def': 2, 'Spe': 3,'Block':0,'PlayerType':'','Gaurdian':1}
enemy = {'Hmax':10, 'H': 10, 'MPmax': 8, 'MP': 8, 'Att': 4, 'Def': 4, 'Spe': 4,'Block':0, 'EnemyType':''}
def WSA():
    player['MP'] = player['MP'] - 4
    damage = (random.randint((player['Att']-2),(player['Att']+2)))*2
    if enemy['Block'] == 1:
        block = ((int(enemy['Def']*1.5)//1))
        block = random.randint((block-1),(block+1))
    else:
        block = enemy['Def']
        block = random.randint((block-1),(block+1))
    TrueDamage = damage-block
    enemy['H'] = (enemy['H']-TrueDamage)
    print(f"You did {TrueDamage} Damage\n")
    player['Att']= int(player['Att']/2)
def main():
    print("Welcome to the Turn-Based Game\n")
    print("Choose Chacater:\n1:Warrior:Specializes in high Health and Damage but has lower Defence and Speed\nSpecial Move: All IN \nUses 4 Mana does double damage but for the rest of the match damage is cut in half\nGaurdian Angel: When the Warrior Health hits zero it is replaced with 1")
    print("2:Mage\nWell rounded stats with high Mana")
    print("3:Rouge\nExtremely high damage and speed with low defence and health")
    x = int(input())
    if x == 1:
        player['Hmax'] =15
        player['H'] = 15
        player['MPmax'] = 4
        player['MP'] = 4
        player['Att'] = 6
        player['Def'] = 1
        player['Spe'] = 3
        player['Block'] = 0,
        player['PlayerType'] = 'Warrior'
        player['Gaurdian'] = 1
    elif x == 2:
        player['Hmax'] =10
        player['H'] = 10
        player['MPmax'] = 10
        player['MP'] = 10
        player['Att'] = 3
        player['Def'] = 3
        player['Spe'] = 4
        player['Block'] = 0,
        player['PlayerType'] = 'Mage'
        player['Gaurdian'] = 1
    elif x == 3:
        player['Hmax'] = 8
        player['H'] = 8
        player['MPmax'] = 4
        player['MP'] = 4
        player['Att'] = 7
        player['Def'] = 1
        player['Spe'] = 8
        player['Block'] = 0,
        player['PlayerType'] = 'Rouge'
        player['Gaurdian'] = 1
    y = random.randint(1,3)
    if y == 1:
        enemy['Hmax'] = 10
        enemy['H'] = 10
        enemy['MPmax'] = 8
        enemy['MP'] = 8
        enemy['Att'] = 4
        enemy['Def'] = 3
        enemy['Spe'] = 4
        enemy['Block'] = 0
        enemy['EnemyType'] = 'Skeleton Mage'
        print("You are against the Skeleton Mage\nHe has aveage stats and plays defencive")
    elif y == 2:
        enemy['Hmax'] = 20
        enemy['H'] = 20
        enemy['MPmax'] = 0
        enemy['MP'] = 0
        enemy['Att'] = 5
        enemy['Def'] = 2
        enemy['Spe'] = 0
        enemy['Block'] = 0
        enemy['EnemyType'] = 'Ogre'
        print("You are against the Ogre\nHe plans to slowly crush you with his high health")
    elif y == 3:
        enemy['Hmax'] = 7
        enemy['H'] = 7
        enemy['MPmax'] = 4
        enemy['MP'] = 4
        enemy['Att'] = 6
        enemy['Def'] = 1
        enemy['Spe'] = 7
        enemy['Block'] = 0
        enemy['EnemyType'] = 'Zombie Dog'
        print("You are agaisnt the Zombie Dog\nHis high attack compliments his extreme aggrestion")
    Game()
def PlayerTurn():
    player['Block'] = 0
    print("Your Turn\n1:Attack\n2:Special Attack\n3:Heal\n4:Block")
    x = int(input())
    if x == 1:
        damage = random.randint((player['Att']-2),(player['Att']+2))
        if enemy['Block'] == 1:
            block = ((int(enemy['Def']*1.5)//1))
            block = random.randint((block-1),(block+1))
        else:
            block = enemy['Def']
            block = random.randint((block-1),(block+1))
        TrueDamage = damage-block
        if TrueDamage > 0:
            enemy['H'] = (enemy['H']-TrueDamage)
            print(f"You did {TrueDamage} Damage\n")
        else:
            print(f"You did 0 Damage\n")
    elif x == 2:
        if player['PlayerType'] == 'Warrior' and player['MP'] >= 4:
            WSA()
    elif x == 3:
        if player['MP'] >= 2:
            player['MP'] = player['MP'] - 2
            player['H'] = player['H'] + int(((player['Hmax']*.35)//1))
            
            if player['H'] > player['Hmax']:
                player['H'] = player['Hmax']
                print("You healed to max Health")
            else:
                print(f"You Healed {int(((player['Hmax']*.35)//1))} Health")
        else:
            print("Not enough Mana lose your turn")
    else:
        player['Block'] = 1
def EnemyTurn():
    enemy['Block'] = 0
    if player['H'] < int(((player['Hmax']*.20)//1)):
        print("Enemy Attacked")
        damage = random.randint((enemy['Att']-2),(enemy['Att']+2))
        if player['Block'] == 1:
            block = ((int(player['Def']*1.5)//1))
            block = random.randint((block-1),(block+1))
        else:
            block = player['Def']
            block = random.randint((block-1),(block+1))
        TrueDamage = damage-block
        if player['PlayerType'] == 'Rouge':
            x = random.randint(1,4)
            if x == 1:
                print("You dodged the attack")
                TrueDamage = 0
        if TrueDamage > 0:
            player['H'] = (player['H']-TrueDamage)
            print(f"Enemy did {TrueDamage} Damage\n")
        else:
            print(f"Enemy did 0 Damage\n")
    elif enemy['H'] < int(((enemy['Hmax']*.35)//1)) and enemy['MP'] >= 2:
        enemy['MP'] = enemy['MP']-2
        enemy['H'] = enemy['H'] + int(((enemy['Hmax']*.75)//1))
        print(f"Enemy Healed {int(((enemy['Hmax']*.75)//1))} Health")
    else:
        x = random.randint(0,3)
        if x == 0:
            print("Enemy Blocked\n")
            enemy['Block'] = 1
        else:
            print("Enemy Attacked")
            damage = random.randint((enemy['Att']-2),(enemy['Att']+2))
            if player['Block'] == 1:
                block = ((int(player['Def']*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = player['Def']
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            if player['PlayerType'] == 'Rouge':
                x = random.randint(1,4)
                if x == 1:
                    print("You dodged the attack")
                    TrueDamage = 0
            if TrueDamage > 0:
                player['H'] = (player['H']-TrueDamage)
                print(f"Enemy did {TrueDamage} Damage\n")
            else:
                print(f"Enemy did 0 Damage\n")
def Game():
    while player['H']>0 and enemy['H']>0:
        print(f"Player Health:{player['H']}/{player['Hmax']}\nPlayer Mana:{player['MP']}/{player['MPmax']}\n\nEnemy Health:{enemy['H']}/{enemy['Hmax']}\nEnemy Mana:{enemy['MP']}/{enemy['MPmax']}\n")
        if player['Spe']>enemy['Spe']:
            PlayerTurn()
            print(f"Player Health:{player['H']}/{player['Hmax']}\nPlayer Mana:{player['MP']}/{player['MPmax']}\n\nEnemy Health:{enemy['H']}/{enemy['Hmax']}\nEnemy Mana:{enemy['MP']}/{enemy['MPmax']}\n")
            if player['H']<0 or enemy['H']<0:
                continue
            EnemyTurn()
            if player['H'] <= 0:
                if player['PlayerType'] == 'Warrior':
                    if player['Gaurdian'] == 1:
                        player['Gaurdian'] = 0
                        player['H'] = 1
                        print("Your Gaurdian Angel Saved you")
        elif enemy['Spe']>player['Spe']:
            EnemyTurn()
            if player['H'] <= 0:
                if player['PlayerType'] == 'Warrior':
                    if player['Gaurdian'] == 1:
                        player['Gaurdian'] = 0
                        player['H'] = 1
                        print("Your Gaurdian Angel Saved you")
            print(f"Player Health:{player['H']}/{player['Hmax']}\nPlayer Mana:{player['MP']}/{player['MPmax']}\n\nEnemy Health:{enemy['H']}/{enemy['Hmax']}\nEnemy Mana:{enemy['MP']}/{enemy['MPmax']}\n")
            if player['H']<0 or enemy['H']<0:
                continue
            PlayerTurn()
        else:
            x = random.randint(0,1)
            if x == 1:
                PlayerTurn()
                print(f"Player Health:{player['H']}/{player['Hmax']}\nPlayer Mana:{player['MP']}/{player['MPmax']}\n\nEnemy Health:{enemy['H']}/{enemy['Hmax']}\nEnemy Mana:{enemy['MP']}/{enemy['MPmax']}\n")
                if player['H']<0 or enemy['H']<0:
                    continue
                EnemyTurn()
                if player['H'] <= 0:
                    if player['PlayerType'] == 'Warrior':
                        if player['Gaurdian'] == 1:
                            player['Gaurdian'] = 0
                            player['H'] = 1
                            print("Your Gaurdian Angel Saved you")
            else:
                EnemyTurn()
                if player['H'] <= 0:
                    if player['PlayerType'] == 'Warrior':
                        if player['Gaurdian'] == 1:
                            player['Gaurdian'] = 0
                            player['H'] = 1
                            print("Your Gaurdian Angel Saved you")
                print(f"Player Health:{player['H']}/{player['Hmax']}\nPlayer Mana:{player['MP']}/{player['MPmax']}\n\nEnemy Health:{enemy['H']}/{enemy['Hmax']}\nEnemy Mana:{enemy['MP']}/{enemy['MPmax']}\n")
                if player['H']<0 or enemy['H']<0:
                    continue
                PlayerTurn()
    if player['H'] <= 0:
        print("You Lose :(")
    else:
        print("You Win :)")
main()
            
