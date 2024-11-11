# Importing the random module to generate random numbers between -1 and 1
import random

# definition of funtion
def snake_water_gun_game():
    # Print the game title and instructions
    print("*** SNAKE WATER GUN GAME ***\n")
    print("S for Snake\nW for Water\nG for Gun")
    
    # Randomly select the computer's choice from -1 (Water), 0 (Gun), 1 (Snake)
    computer_choice = random.choice([-1, 0, 1])
    
    # Get user's choice and convert it to lowercase
    user_choice = input("\nEnter Your Choice: ").lower()

    # Dictionary to map user input to game values
    snake_water_gun_dict = {'s': 1, 'w': -1, 'g': 0}
    # Dictionary to show the choices in a readable format
    for_show_choices = {1: 'Snake', -1: 'Water', 0: 'Gun'}

    # Get the user's choice in game value
    show_user_choice = snake_water_gun_dict[user_choice]

    # Display the choices made by the user and the computer
    print(f"Your choice is : {for_show_choices[show_user_choice]}\nAnd Computer Choice is : {for_show_choices[computer_choice]}")

    # Check for a draw
    if computer_choice == show_user_choice:
        print("\nNo Woories\nits a Draw\n")
    else:
        # Determine the winner based on the choices
        if computer_choice == -1 and show_user_choice == 1:
            print(f"\nCongratulations!!!\nYou Won the Game\n")
        elif computer_choice == -1 and show_user_choice == 0:
            print(f"\nOPPPPSSS!!\nYou Lost The Game\n")
        elif computer_choice == 1 and show_user_choice == -1:
            print(f"\nOPPPPSSS!!\nYou Lost The Game\n")
        elif computer_choice == 1 and show_user_choice == 0:
            print(f"\nCongratulations!!!\nYou Won the Game\n")
        elif computer_choice == 0 and show_user_choice == -1:
            print(f"\nCongratulations!!!\nYou Won the Game\n")
        elif computer_choice == 0 and show_user_choice == 1:
            print(f"\nOPPPPSSS!!\nYou Lost The Game\n")
        else:
            print("Try Again with S, W, or G")

# Calling the function to run the game for the first time
snake_water_gun_game()

# Loop for replaying the game or exiting
while True:
    play_or_not = int(input("Enter 1 for Play Again and 2 for Exit: "))

    if play_or_not == 1:
        snake_water_gun_game()  # Calling the function to play again
    if play_or_not == 2:
        print("Game is Closed\nTHANK YOU!")
        break