def adventure_game():
    name = input("Enter your name: ").strip()
    print(f"Welcome, {name}, to the Enchanted Forest!")

    answer = input("You find yourself at the edge of an enchanted forest. Do you enter or stay where you are? Type 'enter' to enter the forest or 'stay' to stay where you are: ").strip().lower()

    if answer == "enter":
        answer = input("You step into the forest and hear a rustling in the bushes. Do you investigate or ignore it? Type 'investigate' to investigate the sound or 'ignore' to keep walking: ").strip().lower()

        if answer == "investigate":
            print("You carefully approach the bushes and find a magical creature who offers you a choice of three items: a sword, a shield, or a potion.")
            item = input("Which item do you choose? Type 'sword' for the sword, 'shield' for the shield, or 'potion' for the potion: ").strip().lower()
            
            if item == "sword":
                print("You take the sword and continue your journey. You come across a dragon blocking your path. You bravely fight the dragon with your sword and win! You are a hero!")
            elif item == "shield":
                print("You take the shield and continue your journey. You come across a band of thieves. With the shield's protection, you defend yourself and scare them away! You are safe!")
            elif item == "potion":
                print("You take the potion and continue your journey. You come across a wounded traveler. You give them the potion, and they thank you by guiding you to a hidden treasure! You are rich!")
            else:
                print("Invalid option. You wander aimlessly and get lost in the forest. You lose!")
        elif answer == "ignore":
            print("You ignore the sound and keep walking. Suddenly, you fall into a hidden pit and find yourself in an underground cave.")
            answer = input("In the cave, you see two tunnels. One is dark and the other is lit by glowing mushrooms. Do you take the 'dark' tunnel or the 'glowing' tunnel? ").strip().lower()
            
            if answer == "dark":
                print("You bravely enter the dark tunnel, but it's too dark to see. You stumble and fall into a deep chasm. You lose!")
            elif answer == "glowing":
                print("You walk through the glowing tunnel and find an underground garden filled with rare and magical plants. You collect some and become a famous botanist! You win!")
            else:
                print("Invalid option. You wander aimlessly in the cave and get lost. You lose!")
        else:
            print("Invalid option. You get lost in the forest. You lose!")

    elif answer == "stay":
        answer = input("You decide to stay and explore the area around the forest. You find a hidden path that leads to a mysterious castle. Do you enter the castle or camp outside? Type 'enter' to enter the castle or 'camp' to set up camp outside: ").strip().lower()

        if answer == "enter":
            print("You enter the castle and find it filled with ancient artifacts and a magical library. You become a renowned scholar! You win!")
        elif answer == "camp":
            print("You set up camp outside the castle. During the night, you are visited by a ghost who reveals the secrets of the castle to you. You become a master storyteller! You win!")
        else:
            print("Invalid option. You get lost and never find your way back. You lose!")
    
    else:
        print("Not a valid option. You get lost and never find your way back. You lose!")


adventure_game()
