import random
#Computer randomly choose the number between 1 and 10
computer_choice = random.choice([1, 10])

#Taking input from users
user_choice = int(input("Enter your choice (1 or 10): "))

#Display user and computer choices 
print(f"You chose {user_choice} and the computer chose {computer_choice}.")

#condition for result
if computer_choice == user_choice:
    print("Congratulations! You won.")
else:
    print("Sorry! You lost.")
