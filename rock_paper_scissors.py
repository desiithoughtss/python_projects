import random

user_wins = 0
computer_wins = 0 

options = {"r": "rock", "p": "paper", "s": "scissors"}
winning_combinations = {"r": "s", "p": "r", "s": "p"}

while True:
    user_input = input("Type R/P/S for rock, paper, scissors or Q to quit: ").strip().lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Invalid input, please try again.")
        continue
    
    computer_pick = random.choice(list(options.keys()))
    print(f"Computer pick is {options[computer_pick]}")
    
    if winning_combinations[user_input] == computer_pick:
        print("You win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost.")
        computer_wins += 1
    
print(f"You won {user_wins} times") 
print(f"Computer won {computer_wins} times")
