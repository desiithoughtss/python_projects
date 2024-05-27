import random

top_of_range = int(input("Type a number: "))
random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Please type a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time: ")
        continue
    
    if user_guess == random_number:
        print("You got it right")
        break
    elif user_guess > random_number:
            print("You were above the number")
    else:
        print("You were below the number ")
        
print(f"You got it in {guesses} guesses")