# An implementation of "rock-paper-scissors-lizard-Spock"
# By Brian Dau

import sys, random

class Player:
    """The user playing the computer"""
    username = ""
    wins = 0
    weapon = ""
    choice = ""
    def __init__(self, name):
        Player.username = name

    def pickWeapon():
        Player.weapon = ""
        while Player.weapon not in Game.weapons.values():
            if Player.weapon == 'q' or Player.weapon == 'quit':
                Game.quitgame()
            else:
                Player.weapon = str.lower(input("Select your weapon(or [q]uit): "))
        return Player.weapon

    def playerWins():
        Player.wins += 1
        Game.gamenum += 1
        print("Current score is %s: %s and Computer: %s" % (Player.username, Player.wins, Computer.wins))


class Computer:
    """The player's challenger"""
    wins = 0
    selector = 0
    weapon = ""
    choice = ""
    def pickWeapon():
         Computer.selector = random.randint(0, 4)
         Computer.weapon = Game.weapons[Computer.selector]
         return Computer.weapon

    def computerWins():
        Computer.wins += 1
        Game.gamenum += 1
        print("Current score is %s: %s and Computer: %s" % (Player.username, Player.wins, Computer.wins))

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
            Player.choice = Player.pickWeapon()
            Computer.choice = Computer.pickWeapon()
            print("%s picks: %s." % (Player.username, Player.choice))
            print("Computer picks: %s." % Computer.choice)
            if Player.choice == Computer.choice:
                print("It's a draw! Starting round over...")
            else:
                Game.decideWinner(self, Player.choice, Computer.choice)
        if Player.wins > Computer.wins:
            print("Game over. %s won the game!" % Player.username)
        else:
            print("Game over. Computer won the game!")
        self.end = str.lower(input("Would you like to play again? y/n: "))
        if self.end == 'n':
            Game.quitgame()
        else:
            Game.gamenum = 0
            Player.wins = 0
            Computer.wins = 0
            self.play = Game(int(input("Enter number of rounds to play or press return to play forever: ")))
    
    def decideWinner(self, playerchoice, computerchoice):
        self.pchoice = playerchoice
        self.cchoice = computerchoice
        if self.pchoice == 'scissors':
            if self.cchoice == 'paper':
                print("%s. %s wins!" % (Game.messages[0], Player.username))
                Player.playerWins()
            elif self.cchoice == 'lizard':
                print("%s. %s wins!" % (Game.messages[5], Player.username))
                Player.playerWins()
            elif self.cchoice == 'rock':
                print("%s. Computer wins!" % Game.messages[9])
                Computer.computerWins()
            elif self.cchoice == 'spock':
                print("%s. Computer wins!" % Game.messages[4])
                Computer.computerWins()
        elif self.pchoice == 'paper':
            if self.cchoice == 'spock':
                print("%s. %s wins!" % (Game.messages[7], Player.username))
                Player.playerWins()
            elif self.cchoice == 'rock':
                print("%s. %s wins!" % (Game.messages[1], Player.username))
                Player.playerWins()
            elif self.cchoice == 'scissors':
                print("%s. Computer wins!" % Game.messages[0])
                Computer.computerWins()
            elif self.cchoice == 'lizard':
                print("%s. Computer wins!" % Game.messages[6])
                Computer.computerWins()
        elif self.pchoice == 'rock':
            if self.cchoice == 'scissors':
                print("%s. %s wins!" % (Game.messages[9], Player.username))
                Player.playerWins()
            elif self.cchoice == 'lizard':
                print("%s. %s wins!" % (Game.messages[2], Player.username))
                Player.playerWins()
            elif self.cchoice == 'paper':
                print("%s. Computer wins!" % Game.messages[1])
                Computer.computerWins()
            elif self.cchoice == 'spock':
                print("%s. Computer wins!" % Game.messages[8])
                Computer.computerWins()
        elif self.pchoice == 'lizard':
            if self.cchoice == 'paper':
                print("%s. %s wins!" % (Game.messages[6], Player.username))
                Player.playerWins()
            elif self.cchoice == 'spock':
                print("%s. %s wins!" % (Game.messages[3], Player.username))
                Player.playerWins()
            elif self.cchoice == 'scissors':
                print("%s. Computer wins!" % Game.messages[5])
                Computer.computerWins()
            elif self.cchoice == 'rock':
                print("%s. Computer wins!" % Game.messages[2])
                Computer.computerWins()
        elif self.pchoice == 'spock': 
            if self.cchoice == 'scissors':
                print("%s. %s wins!" % (Game.messages[4], Player.username))
                Player.playerWins()
            elif self.cchoice == 'rock':
                print("%s. %s wins!" % (Game.messages[8], Player.username))
                Player.playerWins()
            elif self.cchoice == 'paper':
                print("%s. Computer wins!" % Game.messages[7])
                Computer.computerWins()
            elif self.cchoice == 'lizard':
                print("%s. Computer wins!" % Game.messages[3])
                Computer.computerWins()

    def quitgame():
        print("Thanks for playing!")
        sys.exit()
    
def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    user = Player(input("Enter your name: "))
    play = Game(int(input("Enter number of rounds to play or press return to play forever: ")))

main()
