import Game as g
import Characters as c
def main():
    print("Welcome to the Turn-Based Game\n")
    while True:
        print("1.Start\n2.Leaderboard\n3.First Time Info\n4:Exit")
        x = int(input())
        while x !=1 and x !=2 and x !=3 and x !=4:
            print("Invald input try again")
            x = int(input())
        if x == 1:
            print("Enter your username")
            Name = input()
            print("Choose Chacater:\n1:Warrior:\nSpecializes in high Health and Damage but has lower Defence and Speed\n\nSpecial Move: All IN \nUses 4 Mana does double damage but for the rest of the match damage is cut in half\n\nLast Resort: Guardian Angel: /nWhen the Warrior Health hits zero it is replaced with 1\n\n")
            print("2:Mage\nWell rounded stats with high Mana\n\nSpecial Move: Rock Slam\nUse 2 mana to slam a rock on the enemy stuning them a turn, but dealing only half damage\n\nLast Resort: Last Reserves: \nIf Mana is zero it will increase to half of your max Mana\n\n")
            print("3:Rouge\nExtremely high damage and speed with low defence and health\n\nSpecial Move: Speed Blitz\nUse 2 mana to boost your speed to catch an enemy off guard dealing 25% more damage and doubling your evaision the next turn\n\nLast Resort: Too Fast: \nIf an enemy dodges an attack you will still attack them\n")
            x = int(input())
            g.Play(x)
        elif x == 2:
            file = open("Leaderboard.txt", 'r')
            text = file.read()
            print(text)
        elif x == 3:
            print("")
        else:
            break
main()
