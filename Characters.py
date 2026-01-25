import random
class Player:
    def __init__(self, MaxH, H, MaxMP, MP, Att, Def, Spe, Eva, Block, Stun, PlayerType, Gaurdian):
        self.MaxH = MaxH
        self.H = H
        self.MaxMP = MaxMP
        self.MP = MP
        self.Att = Att
        self.Def = Def
        self.Spe = Spe
        self.Eva = Eva
        self.Block = Block
        self.Stun = Stun
        self.PlayerType = PlayerType
        self.Gaurdian = Gaurdian
    def Damage(self, EnemyN):
        if random.randint(1,100) <= EnemyN.Eva:
            if self.PlayerType == "Rouge" and self.Gaurdian == 1:
                damage = random.randint((self.Att-2),(self.Att+2))
                if EnemyN.Block == 1:
                    block = ((int(EnemyN.Def*1.5)//1))
                    block = random.randint((block-1),(block+1))
                else:
                    block = EnemyN.Def
                    block = random.randint((block-1),(block+1))
                TrueDamage = damage-block
                if TrueDamage > 0:
                    EnemyN.H = (EnemyN.H-TrueDamage)
                    print(f"You did {TrueDamage} damage\n")
                else:
                    print(f"You did 0 damage\n")
                self.Gaurdian = 0
            else:    
                print("Enemy dodged the attack")
        else:
            damage = random.randint((self.Att-2),(self.Att+2))
            if EnemyN.Block == 1:
                block = ((int(EnemyN.Def*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = EnemyN.Def
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            if TrueDamage > 0:
                EnemyN.H = (EnemyN.H-TrueDamage)
                print(f"You did {TrueDamage} damage\n")
            else:
                print(f"You did 0 damage\n")
    def Heal(self):
        if self.MP >= 2:
            self.MP = self.MP - 2
            self.H = self.H + int(((self.MaxH*.4)//1))
            if self.H > self.MaxH:
                self.H = self.MaxH
                print("You healed to max health")
            else:
                print(f"You healed {int(((self.MaxH*.35)//1))} health")
        else:
            print("Not enough Mana lose your turn")
    def SA(self, EnemyN):
        if self.PlayerType == "Warrior":
            self.MP = multi
            self.MP = 0
            damage = ((random.randint((self.Att),(self.Att+3)))*(multi*.65)//1)
            if EnemyN.Block == 1:
                block = ((int(EnemyN.Def*1.5)//1))
                block = random.randint((block-1),(block))
            else:
                block = EnemyN.Def
                block = random.randint((block-1),(block))
            TrueDamage = damage-block
            if TrueDamage < 0:
                TrueDamage = 0
            EnemyN.H = (EnemyN.H-TrueDamage)
            print(f"You use all you power for one attack dealing {TrueDamage} damage but your attack has been halfed\n")
            self.Att= int(self.Att/2)
        elif self.PlayerType == "Mage" and self.MP>=2:
            self.MP = self.MP - 3
            damage = int((((random.randint((self.Att),(self.Att+2)))*.75)//1))
            if EnemyN.Block == 1:
                block = ((int(EnemyN.Def*1.5)//1))
                block = random.randint((block-1),(block))
            else:
                block = EnemyN.Def
                block = random.randint((block-1),(block))
            TrueDamage = damage-block
            if TrueDamage < 0:
                TrueDamage = 0
            EnemyN.H = (EnemyN.H-TrueDamage)
            print(f"You lift a rock launching it at the enemy dealing {TrueDamage} damage, and stunning the enemy for a turn\n")
            EnemyN.Stun = 1
        elif self.PlayerType == "Rouge" and self.MP>=2:
            self.MP = self.MP - 2
            damage = int((((random.randint((self.Att),(self.Att+2)))*1.25)//1))
            TrueDamage = damage
            if TrueDamage < 0:
                TrueDamage = 0
            EnemyN.H = (EnemyN.H-TrueDamage)
            print(f"You dash past the enemy catching them off guard dealing {TrueDamage} damage and doubling your evasion\n")
            self.Eva = int(self.Eva*2)
        else:
            print('Not enough mana lose your turn')
class Enemy:
    def __init__(self, MaxH, H, MaxMP, MP, Att, Def, Spe, Eva, Block, Stun, EnemyType,):
        self.MaxH = MaxH
        self.H = H
        self.MaxMP = MaxMP
        self.MP = MP
        self.Att = Att
        self.Def = Def
        self.Spe = Spe
        self.Eva = Eva
        self.Block = Block
        self.Stun = Stun
        self.EnemyType = EnemyType
    def SA(self, PlayerN):
        if self.EnemyType == "Skeletion Mage":
            self.MP = self.MP - 4
            self.H = self.MaxH
            print("The Skeletion Mage used a forbidon necromancy tomb to heal himself to full health")
        elif self.EnemyType == "Ogre":
            self.H = self.H-7
            damage = random.randint((self.Att-2),(self.Att+2)*1.5)
            if PlayerN.Block == 1:
                block = ((int(PlayerN.Def*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = PlayerN.Def
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            if TrueDamage < 0:
                TrueDamage = 0
            PlayerN.H = (PlayerN.H-TrueDamage)
            x = random.randint(1,2)
            if x == 1:
                PlayerN.Stun == 1
                print(f"The Ogre slammed the ground in rage dealing {TrueDamage} damage and stunning you for one turn")
            else:
                print(f"The Ogre slammed the ground in rage dealing {TrueDamage} Damage")
        elif self.EnemyType == "Zombie Dog":
            multi = self.MP
            self.MP = 0
            damage = random.randint(((self.Att-2),(self.Att+2)*(.1*multi))//1)
            if PlayerN.Block == 1:
                block = ((int(PlayerN.Def*1.5)//1))
                block = random.randint((block-2),(block))
            else:
                block = PlayerN.Def
                block = random.randint((block-2),(block))
            TrueDamage = damage-block
            if TrueDamage < 0:
                TrueDamage = 0
            PlayerN.H = (PlayerN.H-TrueDamage)
            print(f"The Zombie Dog in a desperate attempt to survive used all its mana to attack you dealing {TrueDamage} damage")
    def Damage(self, PlayerN):
        if random.randint(1,100) <= PlayerN.Eva:
            print("You dodged the attack")
        else:
            damage = random.randint((self.Att-2),(self.Att+2))
            if PlayerN.Block == 1:
                block = ((int(PlayerN.Def*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = PlayerN.Def
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            if TrueDamage > 0:
                PlayerN.H = (PlayerN.H-TrueDamage)
                print(f"Enemy did {TrueDamage} damage\n")
            else:
                print(f"Enemy did 0 damage\n")
    def Heal(self):
        self.MP = self.MP - 2
        self.H = self.H + int(((self.MaxH*.4)//1))
        print(f"Enemy healed {int(((self.MaxH*.35)//1))} health")
#All stats in order
#MaxH, H, MaxMP, MP, Att, Def, Spe, Eva, Block, Stun, PlayerType, Gaurdian
Warrior =       Player(13,13,4, 4, 4,2,3,5,0,0,"Warrior",1)
Mage =          Player(10,10,10,10,3,3,4,10,0,0,"Mage",1)
Rouge =         Player(8, 8, 4, 4, 5,1,8,25,0,0,"Rouge",1)
Skeleton_Mage = Enemy(12, 12,6, 6, 3,1,3,8,0,0,"Skeletion Mage")
Ogre =          Enemy(17, 17,0, 0, 3,1,0,3,0,0,"Ogre")
Zombie_Dog =    Enemy(7,  7, 4, 4, 4,0,7,20,0,0,"Zombie Dog")

