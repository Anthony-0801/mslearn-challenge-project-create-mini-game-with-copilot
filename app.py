#Develop a simple rock papers scissors game using python
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    clear()
    print("Welcome to Rock, Paper, Scissors")
    print("Please enter the number of your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    player = int(input("Enter your choice: "))
    computer = random.randint(1,3)

    #Add validation that when the user enter a string the program should prompt the user to enter a valid number
    while player not in [1, 2, 3]:
        player = int(input("Invalid choice! Please enter a valid number: "))

    print(f"Computer chose: {computer}")
    print(f"You chose: {player}")
    

    if player == computer:
        print("It's a tie!")
    elif player == 1:
        if computer == 2:
            print("Computer wins!")
        else:
            print("You win!")
    elif player == 2:
        if computer == 3:
            print("Computer wins!")
        else:
            print("You win!")
    elif player == 3:
        if computer == 1:
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid choice!")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        game()
    else:
        print("Thanks for playing!")
    
game()
