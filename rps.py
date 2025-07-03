import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

print('rock, paper, scissors game')
while player not in options:
    player = input('Enter your choice: ')

print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It is a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print('You win!')
else:
    print('You lost!')