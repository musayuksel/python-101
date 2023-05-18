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

class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f"{self.name} has {self.score} points"



print("Welcome to Rock, Paper, Scissors game!")
print("You will be playing against the computer.")
print("Enter your name to begin:")
player_name = input()
player = Player(player_name)
computer = Player("Computer")

print(f"Hello {player.name}! Let's begin!")
  