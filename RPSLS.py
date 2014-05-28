# An implementation of "Rock-Paper-Scissors-Lizard-Spock"
# By Brian Dau

import sys, random
from collections import Counter
from operator import itemgetter


class Player:
    """The user playing the computer"""
    
    def __init__(self, name):
        self.username = name
        self.gamesplayed = 0
        self.totalwins = 0
        self.totallosses = 0
        self.totalties = 0
        self.cursor = 0
        self.wins = 0
        self.weapon = ""
        self.choice = ""
        self.movelist = []
        if self.username in Data.playerdata:
            self.cursor = Data.playerdata.index(self.username)
            self.gamesplayed = Data.playerdata[self.cursor + 1]
            self.totalwins = Data.playerdata[self.cursor + 2]
            self.totalties = Data.playerdata[self.cursor + 3]
            self.totallosses = self.gamesplayed - (self.totalwins + self.totalties)
            print('Player "%s" loaded!' % self.username)
        else:
            Data.playerdata.extend((self.username, 0, 0, 0))
            self.cursor = Data.playerdata.index(self.username)
            self.gamesplayed = Data.playerdata[self.cursor + 1]
            self.totalwins = Data.playerdata[self.cursor + 2]
            self.totalties = Data.playerdata[self.cursor + 3]
            self.totallosses = self.gamesplayed - (self.totalwins + self.totalties)
            print('Player "%s" created!' % self.username)

    def pickWeapon(self):
        self.weapon = ""
        while self.weapon not in Game.weapons.values():
            if self.weapon == 'q' or self.weapon == 'quit':
                self.gamenum = 0
                self.wins = 0
                Computer.wins = 0
                main()
            else:
                self.weapon = str.lower(input("Select your weapon(or [q]uit): "))
        self.movelist.append(self.weapon)
        return self.weapon

    def playerWins():
        self.wins += 1
        Game.gamenum += 1
        self.gamesplayed += 1
        self.totalwins += 1
        print("Current score is %s: %s and Computer: %s" % (self.username, self.wins, Computer.wins))


class Computer:
    """The player's challenger"""
    smart = True
    stupidgamesplayed = 0
    smartgamesplayed = 0
    stupidwins = 0
    stupidlosses = 0
    stupidties = 0
    smartwins = 0
    smartlosses = 0
    smartties = 0
    wins = 0
    selector = 0
    weapon = ""
    choice = ""
    counting = []
    playermoves = []
    playerfav = ""
    playerfavtie = ""

    def __init__():
        Computer.stupidgamesplayed = Data.computerdata[1]
        Computer.stupidwins = Data.computerdata[2]
        Computer.stupidties = Data.computerdata[3]
        Computer.smartgamesplayed = Data.computerdata[4]
        Computer.smartwins = Data.computerdata[5]
        Computer.smartties = Data.computerdata[6]
    
    def pickWeapon():
        if Computer.smart == False:
            Computer.selector = random.randint(0, 4)
            Computer.weapon = Game.weapons[Computer.selector]
            return Computer.weapon
        else:
            if len(user.movelist) == 1:
                Computer.selector = random.randint(0, 4)
                Computer.weapon = Game.weapons[Computer.selector]
                return Computer.weapon
            else:
                Computer.counting = list(Counter(user.movelist).items())
                Computer.playermoves = sorted(Computer.counting, key=itemgetter(1), reverse=True)
                if len(Computer.playermoves) == 1:
                    Computer.playerfav = Computer.playermoves[0][0]
                    Computer.weapon = Computer.counterPick(self, Computer.playerfav)
                    return Computer.weapon
                elif Computer.playermoves[0][1] == Computer.playermoves[1][1]:
                    Computer.playerfav = Computer.playermoves[0][0]
                    Computer.playerfavtie = Computer.playermoves[1][0]
                    Computer.weapon = Computer.counterPickTie(self, Computer.playerfav, Computer.playerfavtie)
                    return Computer.weapon
                else:
                    Computer.playerfav = Computer.playermoves[0][0]
                    Computer.weapon = Computer.counterPick(self, Computer.playerfav)
                    return Computer.weapon

    def counterPick(self, pick):
        self.pick = pick
        self.countervariable = random.randint(0, 1)
        if self.pick == 'scissors':
            if self.countervariable == 0:
                return 'rock'
            else:
                return 'spock'
        elif self.pick == 'paper':
            if self.countervariable == 0:
                return 'scissors'
            else:
                return 'lizard'
        elif self.pick == 'rock':
            if self.countervariable == 0:
                return 'paper'
            else:
                return 'spock'
        elif self.pick == 'lizard':
            if self.countervariable == 0:
                return 'rock'
            else:
                return 'scissors'
        elif self.pick == 'spock':
            if self.countervariable == 0:
                return 'paper'
            else:
                return 'lizard'

    def counterPickTie(self, pick1, pick2):
        self.picklist = [pick1, pick2]
        if 'scissors' in self.picklist and 'rock' in self.picklist:
            return 'spock'
        elif 'paper' in self.picklist and 'lizard' in self.picklist:
            return 'scissors'
        elif 'spock' in self.picklist and 'rock' in self.picklist:
            return 'paper'
        elif 'scissors' in self.picklist and 'lizard' in self.picklist:
            return 'rock'
        elif 'spock' in self.picklist and 'paper' in self.picklist:
            return 'lizard'
        elif 'scissors' in self.picklist and 'paper' in self.picklist:
            return 'scissors'
        elif 'paper' in self.picklist and 'rock' in self.picklist:
            return 'paper'
        elif 'rock' in self.picklist and 'lizard' in self.picklist:
            return 'rock'
        elif 'lizard' in self.picklist and 'spock' in self.picklist:
            return 'lizard'
        elif 'spock' in self.picklist and 'scissors' in self.picklist:
            return 'spock'
        

    def computerWins():
        if Computer.smart == False:
            Computer.wins += 1
            Game.gamenum += 1
            Computer.stupidwins += 1
            Computer.stupidgamesplayed += 1
            print("Current score is %s: %s and Computer: %s" % (user.username, user.wins, Computer.wins))
        else:
            Computer.wins += 1
            Game.gamenum += 1
            Computer.smartwins += 1
            Computer.smartgamesplayed += 1
            print("Current score is %s: %s and Computer: %s" % (user.username, user.wins, Computer.wins))

class Game:
    """Runs the game"""
    prompt = ""
    playto = 0
    gamenum = 0
    weapons = {0: 'rock',
               1: 'paper',
               2: 'scissors',
               3: 'lizard',
               4: 'spock'}
    messages = {0: 'Scissors cut paper',
                1: 'Paper covers rock',
                2: 'Rock crushes lizard',
                3: 'Lizard poisons Spock',
                4: 'Spock smashes scissors',
                5: 'Scissors decapitate lizard',
                6: 'Lizard eats paper',
                7: 'Paper disproves Spock',
                8: 'Spock vaporizes rock',
                9: 'Rock crushes scissors'}
    pchoice = ""
    cchoice = ""
    
    def __init__(self, playto = -1):
        Game.playto = playto
        while Game.gamenum < Game.playto:
            user.choice = user.pickWeapon()
            Computer.choice = Computer.pickWeapon()
            print("%s picks: %s." % (user.username, user.choice))
            print("Computer picks: %s." % Computer.choice)
            if user.choice == Computer.choice:
                print("It's a draw! Starting round over...")
                user.totalties += 1
                if Computer.smart:
                    Computer.smartties += 1
                else:
                    Computer.stupidties += 1
            else:
                Game.decideWinner(self, user.choice, Computer.choice)
        if user.wins > Computer.wins:
            print("Game over. %s won the game!" % user.username)
        elif Computer.wins > user.wins:
            print("Game over. Computer won the game!")
        else:
            print("It's a draw. Play an odd number of games to avoid this embarrassment.")
        print("---------------------------------------------------------------------------")
        print("Showing statistics for %s." % user.username)
        print("Games played: %s. Record: %s-%s-%s." % (user.gamesplayed, user.totalwins, user.totallosses, user.totalties))
        print("Win percentage: %s percent" % ((user.totalwins // user.gamesplayed) * 100))
        print("Showing statistics for Smart AI.")
        print("Games played: %s. Record: %s-%s-%s." % (Computer.smartgamesplayed, Computer.smartwins, Computer.smartlosses, Computer.smartties))
        if Computer.smartgamesplayed != 0:
            print("Win percentage: %s percent" % ((Computer.smartwins // Computer.smartgamesplayed) * 100))
        print("Showing statistics for Stupid AI.")
        print("Games played: %s. Record: %s-%s-%s." % (Computer.stupidgamesplayed, Computer.stupidwins, Computer.stupidlosses, Computer.stupidties))
        if Computer.stupidgamesplayed != 0:
            print("Win percentage: %s percent" % ((Computer.stupidwins // Computer.stupidgamesplayed) * 100))
        print("---------------------------------------------------------------------------")
        self.end = str.lower(input("Would you like to play again? y/n: "))
        if self.end == 'n':
            main()
        else:
            Game.gamenum = 0
            user.wins = 0
            Computer.wins = 0
            user.movelist = []
            self.play = Game(int(input("Enter number of rounds to play or press return to play forever: ")))
    
    def decideWinner(self, playerchoice, computerchoice):
        self.pchoice = playerchoice
        self.cchoice = computerchoice
        if self.pchoice == 'scissors':
            if self.cchoice == 'paper':
                print("%s. %s wins!" % (Game.messages[0], user.username))
                user.playerWins()
            elif self.cchoice == 'lizard':
                print("%s. %s wins!" % (Game.messages[5], user.username))
                user.playerWins()
            elif self.cchoice == 'rock':
                print("%s. Computer wins!" % Game.messages[9])
                Computer.computerWins()
            elif self.cchoice == 'spock':
                print("%s. Computer wins!" % Game.messages[4])
                Computer.computerWins()
        elif self.pchoice == 'paper':
            if self.cchoice == 'spock':
                print("%s. %s wins!" % (Game.messages[7], user.username))
                user.playerWins()
            elif self.cchoice == 'rock':
                print("%s. %s wins!" % (Game.messages[1], user.username))
                user.playerWins()
            elif self.cchoice == 'scissors':
                print("%s. Computer wins!" % Game.messages[0])
                Computer.computerWins()
            elif self.cchoice == 'lizard':
                print("%s. Computer wins!" % Game.messages[6])
                Computer.computerWins()
        elif self.pchoice == 'rock':
            if self.cchoice == 'scissors':
                print("%s. %s wins!" % (Game.messages[9], user.username))
                user.playerWins()
            elif self.cchoice == 'lizard':
                print("%s. %s wins!" % (Game.messages[2], user.username))
                user.playerWins()
            elif self.cchoice == 'paper':
                print("%s. Computer wins!" % Game.messages[1])
                Computer.computerWins()
            elif self.cchoice == 'spock':
                print("%s. Computer wins!" % Game.messages[8])
                Computer.computerWins()
        elif self.pchoice == 'lizard':
            if self.cchoice == 'paper':
                print("%s. %s wins!" % (Game.messages[6], user.username))
                user.playerWins()
            elif self.cchoice == 'spock':
                print("%s. %s wins!" % (Game.messages[3], user.username))
                user.playerWins()
            elif self.cchoice == 'scissors':
                print("%s. Computer wins!" % Game.messages[5])
                Computer.computerWins()
            elif self.cchoice == 'rock':
                print("%s. Computer wins!" % Game.messages[2])
                Computer.computerWins()
        elif self.pchoice == 'spock': 
            if self.cchoice == 'scissors':
                print("%s. %s wins!" % (Game.messages[4], user.username))
                user.playerWins()
            elif self.cchoice == 'rock':
                print("%s. %s wins!" % (Game.messages[8], user.username))
                user.playerWins()
            elif self.cchoice == 'paper':
                print("%s. Computer wins!" % Game.messages[7])
                Computer.computerWins()
            elif self.cchoice == 'lizard':
                print("%s. Computer wins!" % Game.messages[3])
                Computer.computerWins()

    def quitgame():
        data.saveData()
        print("Thanks for playing!")
        sys.exit()


class Data:
    """Handles data.txt file"""
    # playerdata is a list of players created, each followed by
    # three integers: gamesplayed, totalwins, and totalties
    # [0] of playerdata is 'players'
    # computerdata is a list where [0] is 'statistics' followed by
    # six integers: stupidgamesplayed, stupidwins, stupidties,
    # smartgamesplayed, smartwins, smartties
    filedata = []
    playerdata = []
    computerdata = []
    splitter = 0

    def __init__():
        with open('data', 'r') as self.f:
            self.filedata = self.f.read().split('\n')
        self.splitter = self.filedata.index("statistics")
        self.playerdata = self.filedata[:self.splitter]
        self.computerdata = self.filedata[self.splitter:]

    def saveData():
        Data.playerdata[user.cursor + 1] = user.gamesplayed
        Data.playerdata[user.cursor + 2] = user.totalwins
        Data.playerdata[user.cursor + 3] = user.totalties
        Data.computerdata[1] = Computer.stupidgamesplayed
        Data.computerdata[2] = Computer.stupidwins
        Data.computerdata[3] = Computer.stupidties
        Data.computerdata[4] = Computer.smartgamesplayed
        Data.computerdata[5] = Computer.smartwins
        Data.computerdata[6] = Computer.smartties
        self.filedata = self.playerdata + self.computerdata
        with open('data', 'w') as self.f:
            for item in self.filedata:
                self.f.write("%s\n" % item)

def main():
    menuprompt = ""
    nametest = ""
    playerloaded = False
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    print("Please select a menu option below.")
    showHelp()
    while True:
        menuprompt = str.lower(input("> "))
        if menuprompt == '1' or menuprompt == 'p':
            nametest = input("Enter your name: ")
            if nametest == 'players' or nametest == 'statistics':
                print("Very good, Mr. Bond. But I won't let you break my program so easily.")
                print("Returning to main menu.")
            else:
                user = Player(nametest)
                playerloaded = True
        elif menuprompt == '2' or menuprompt == 'g':
            if playerloaded:
                menuprompt = str.lower(input("Play [s]mart AI or [r]andom AI: "))
                if menuprompt == 's' or menuprompt == 'smart':
                    Computer.smart = True
                elif menuprompt == 'r' or menuprompt == 'random':
                    Computer.smart = False
                else:
                    print("Command not recognized, returning to main menu")
                    showHelp()
                play = Game(int(input("Enter number of rounds to play or press return to play forever: ")))
            else:
                print("No player loaded, returning to main menu.")
        elif menuprompt == '3' or menuprompt == 's':
            if playerloaded:
                print("Showing statistics for %s:" % user.username)
                print("Games played: %s. Record: %s-%s-%s." % (user.gamesplayed, user.totalwins, user.totallosses, user.totalties))
                if user.gamesplayed != 0:
                    print("Win percentage: %s percent" % ((user.totalwins // user.gamesplayed) * 100))
            else:
                print("No player loaded.")
            print("Showing statistics for Smart AI:")
            print("Games played: %s. Record: %s-%s-%s." % (Computer.smartgamesplayed, Computer.smartwins, Computer.smartlosses, Computer.smartties))
            if Computer.smartgamesplayed != 0:
                print("Win percentage: %s percent" % ((Computer.smartwins // Computer.smartgamesplayed) * 100))
            print("Showing statistics for Stupid AI:")
            print("Games played: %s. Record: %s-%s-%s." % (Computer.stupidgamesplayed, Computer.stupidwins, Computer.stupidlosses, Computer.stupidties))
            if Computer.stupidgamesplayed != 0:
                print("Win percentage: %s percent" % ((Computer.stupidwins // Computer.stupidgamesplayed) * 100))
        elif menuprompt == '4' or menuprompt == 'o':
            showHelp()
        elif menuprompt == '5' or menuprompt == 'q':
            Data.saveData()
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Command not recognized, try again.")
            

def showHelp():
    print("1. Create or load a [p]layer.")
    print("2. Start a new [g]ame.")
    print("3. View [s]tatistics.")
    print("4. Show [o]ptions again.")
    print("5. [Q]uit game.")

data = Data
main()
