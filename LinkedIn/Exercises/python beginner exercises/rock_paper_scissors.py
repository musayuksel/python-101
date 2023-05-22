# Rock paper scissors is a hand game for two or more players. Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock, a piece of paper, or a pair of scissors. The rules are straightforward:
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

# We’d like you to replicate this game using Python! Requirements:
# Allow user to choose Rock, Paper or Scissors
# Allow the computer to randomly generate a response
# Determine who wins the game
# This can be done in any way that is comfortable with you but we would like to see you demonstrate the various concepts learnt through the courses already.

# Bonus points 👀
# Extend the playability by allowing the user to play several games in a row (user input for how many games to play in a row)
# Improve the readability of the code using Enums and functions
# Add additional features to increase the overall experience of the game.
import random
from enum import Enum

class Move(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

class Winner:
    winner_move="rock-scissors, scissors-paper, paper-rock"
class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.move = None

    def choose_move(self,move):
        self.move = move.lower()

    def __str__(self):
        return f"{self.name} has {self.score} points and chose {self.move} "

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rounds = []

    def play_round(self):

        if self.player1.move == self.player2.move:
            print("It's a tie!")
        elif   f'{self.player1.move}-{self.player2.move}' in Winner.winner_move:
            print(f"{self.player1.name} wins this round!")
            self.player1.score += 1
        elif f'{self.player2.move}-{self.player1.move}' in Winner.winner_move:
            print(f"{self.player2.name} wins this round!")
            self.player2.score += 1
        else:
            print("Something went wrong!")
    def __str__(self) -> str:
        return f"{self.player1} vs {self.player2} in {len(self.rounds)} rounds" 

print("Welcome to Rock, Paper, Scissors game!")
print("You will be playing against the computer.")
player_name = input("Enter your name to begin:")
player = Player(player_name)
computer = Player("Computer")
game = Game(player, computer)


print(game)
print(f"Hello {player.name}! Let's begin!")
round_count = int(input("How many rounds would you like to play?"))
for round in range(round_count):
    print(f"Round {round + 1}")
    # player chooses move
    player_move = input("Choose your move: Rock, Paper or Scissors:")  
    player.choose_move(player_move)
    # computer chooses random move
    computer.choose_move(random.choice(["rock", "paper", "scissors"]))
    print(f"Computer choses {computer.move}")
    game.play_round()
