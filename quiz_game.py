print("Welcome to my computer quiz")
score = 0
while True:
    
    playing = input("Do you want to play: ").strip().lower()
    if playing == "yes":
        print("Okay, let's play")
        answer = input("What does CPU stand for? ").strip().lower()
        if answer =="central processing unit":
            print("You got your answer correct")
            score +=1 
        else:
            print("Incorrect")
            
        answer = input("What does GPU stand for? ").strip().lower()
        if answer =="graphics processing unit":
            print("You got your answer correct")
            score +=1 
        else:
            print("Incorrect")
            
        answer = input("What does RAM stand for? ").strip().lower()
        if answer =="random access memory":
            print("You got your answer correct")
            score +=1 
        else:
            print("Incorrect")
            
        answer = input("What does PSU stand for? ").strip().lower()
        if answer =="power supply unit":
            print("You got your answer correct")
            score +=1 
        else:
            print("Incorrect")
            
        answer = input("What does SSD stand for? ").strip().lower()
        if answer =="solid state drive":
            print("You got your answer correct")
            score +=1 
        else:
            print("Incorrect")
        break
    elif playing == "no":
        quit()
    else:
        print("Invalid input, print yes or no")
        
print(f"Your score is {score}")