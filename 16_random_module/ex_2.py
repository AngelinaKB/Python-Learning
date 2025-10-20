import random

options = ("Rock", "Paper", "Scissors")
player = None
computer = random.choice(options)

while player not in options:
    player =  input("Enter a choice (Rock, Paper, Scissors): ")



print(f"Player: {player.capitalize()}")
print(f"Computer : {computer}")

if player == computer:
    print("It's a tie!")
elif player == "Rock" and computer == "Scissors":
    print("You win!")
