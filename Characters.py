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
            self.H = self.H + int(((self.MaxH*.35)//1))
            if self.H > self.MaxH:
                self.H = self.MaxH
                print("You healed to max health")
            else:
                print(f"You healed {int(((self.MaxH*.35)//1))} health")
        else:
            print("Not enough Mana lose your turn")
    def SA(self, EnemyN):
        if self.PlayerType == "Warrior":
            self.MP = self.MP - 4
            damage = (random.randint((self.Att),(self.Att+2)))*2
            if EnemyN.Block == 1:
                block = ((int(EnemyN.Def*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = EnemyN.Def
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            Enemy.H = (Enemy.H-TrueDamage)
            print(f"You use all you power for one attack dealing {TrueDamage} damage but your attack has been halfed\n")
            self.Att= int(self.Att/2)
        elif self.PlayerType == "Mage":
            self.MP = self.MP - 2
            damage = int((((random.randint((self.Att-2),(self.Att+2)))*.5)//1))
            if EnemyN.Block == 1:
                block = ((int(EnemyN.Def*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = EnemyN.Def
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            Enemy.H = (Enemy.H-TrueDamage)
            print(f"You lift a rock launching it at the enemy dealing {TrueDamage} damage, and stunning the enemy for a turn\n")
            Enemy.Stun = 1
        elif self.PlayerType == "Rouge":
            self.MP = self.MP - 2
            damage = int((((random.randint((self.Att),(self.Att+2)))*1.25)//1))
            if EnemyN.Block == 1:
                block = ((int(EnemyN.Def*1.5)//1))
                block = random.randint((block-1),(block+1))
            else:
                block = EnemyN.Def
                block = random.randint((block-1),(block+1))
            TrueDamage = damage-block
            Enemy.H = (Enemy.H-TrueDamage)
            print(f"You dash past the enemy catching them off guard dealing {TrueDamage} damage and doubling your evasion\n")
            self.Eva = int(self.Eva*2)
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
                PlayerN.H = (Player.H-TrueDamage)
                print(f"Enemy did {TrueDamage} damage\n")
            else:
                print(f"Enemy did 0 damage\n")
    def Heal(self):
        self.MP = self.MP - 2
        self.H = self.H + int(((self.MaxH*.35)//1))
        print(f"Enemy healed {int(((self.MaxH*.35)//1))} health")

Warrior = Player(15,15,4,4,6,1,3,5,0,0,"Warrior",1)
Mage = Player(10,10,10,10,3,3,4,10,0,0,"Mage",1)
Rouge = Player(8,8,4,4,7,1,8,25,0,0,"Rouge",1)
Skeleton_Mage = Enemy(15,15,4,4,6,1,3,8,0,0,"Skeletion Mage")
Ogre = Enemy(20,20,0,0,5,2,0,3,0,0,"Ogre")
Zombie_Dog = Enemy(7,7,4,4,6,1,7,20,0,0,"Zombie Dog")

