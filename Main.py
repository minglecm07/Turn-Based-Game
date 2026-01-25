import Game as g
import Characters as c
def sortscoreboard(file):
    Names = []
    Scores = []
    Scores2 = []
    Scores3 = []
    infile = open(file, 'r')
    text = infile.read()
    words = text.split()
    for i in range(2,len(words)):
        if i%2 == 1:
            Scores.append(words[i])
        else:
            Names.append(words[i])
    a = Scores.index(max(Scores))
    for i in range(len(Scores)):
        if i != a:
            Scores2.append(Scores[i])
    b = Scores.index(max(Scores2))
    for i in range(len(Scores2)):
        if i != b:
            Scores3.append(Scores2[i])
    c = Scores.index(max(Scores3))
    Infile = open(file,'w')
    header = ["Username", "Score"]
    infile.close()
    Infile.write(f"{header[0]:<10} {header[1]:<15}\n{Names[a]:<10} {Scores[a]:<15}\n{Names[b]:<10} {Scores[b]:<15}\n{Names[c]:<10} {Scores[c]:<15}")
def main():
    sortscoreboard("LeaderboardM.txt")
    sortscoreboard("LeaderboardR.txt")
    sortscoreboard("LeaderboardW.txt")
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
            print("Choose Chacater:\n1:Warrior:\nSpecializes in high Health and Damage but has lower Defence and Speed\n\nSpecial Move: All IN \nUses 4 Mana does double damage but for the rest of the match damage is cut in half\n\nLast Resort: Guardian Angel: \nWhen the Warrior Health hits zero it is replaced with 1\n\n")
            print("2:Mage\nWell rounded stats with high Mana\n\nSpecial Move: Rock Slam\nUse 2 mana to slam a rock on the enemy stuning them a turn, but dealing only half damage\n\nLast Resort: Last Reserves: \nIf Mana is zero it will increase to half of your max Mana\n\n")
            print("3:Rouge\nExtremely high damage and speed with low defence and health\n\nSpecial Move: Speed Blitz\nUse 2 mana to boost your speed to catch an enemy off guard dealing 25% more damage and doubling your evaision the next turn\n\nLast Resort: Too Fast: \nIf an enemy dodges an attack you will still attack them\n")
            x = int(input())
            while x !=1 and x !=2 and x !=3:
                print("Invald input try again")
                x = int(input())
            g.Play(x, Name)
        elif x == 2:
            print("    Warrior")
            file = open("LeaderboardW.txt", 'r')
            text = file.read()
            print(text)
            print("    Mage")
            file = open("LeaderboardM.txt", 'r')
            text = file.read()
            print(text)
            print("    Rouge")
            file = open("LeaderboardR.txt", 'r')
            text = file.read()
            print(text)
        elif x == 3:
            print("This is a turn based game with three different playable characters and three different enemys all with unique AI and Stats.Your goal is to get the highest round possible.\nGood luck\n")
        else:
            break
main()   
