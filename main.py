# write a game
# the game is called rock, paper, scissors
# the game will be played between the user and the computer
# the computer will randomly select rock, paper, or scissors
# the user will be prompted to select rock, paper, or scissors
# the winner will be determined by the following rules:
# rock beats scissors
# scissors beats paper
# paper beats rock
# the game will be best of 3
# the game will display the winner at the end of the game
# the game will display the score at the end of the game
# the game will ask the user if they want to play again
# if the user selects yes, the game will start over
# if the user selects no, the game will end

import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are simple:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("The game will be best of 3")
    print("Let's get started!")

    play_game() # call the play_game function   
    
def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0
    while rounds < 3:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = input("Enter rock, paper, or scissors: ")
        if user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            user_score += 1
        elif user_choice == computer_choice:
            print("It's a tie!")
        else:
            print("You lose!")
            computer_score += 1
        rounds += 1
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("You lose the game!")
    else:
        print("It's a tie!")
    print("User score:", user_score)
    print("Computer score:", computer_score)
    play_again = input("Do you want to play again? (yes or no): ")
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# call the main function
if __name__ == "__main__":
    main() 
