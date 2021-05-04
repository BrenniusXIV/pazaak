def start_game():
    choice = input("Would you like to play against the computer, or against a friend?").lower()
    if choice == "computer":
        game_against_computer()
    elif choice == "friend":
        game_against_friend()
    else: 
        print("Please type either 'computer' or 'friend' into the console.")

def game_against_computer():
    print('There will be a program here for the computer - stay tuned')

def game_against_friend():
    print('There will be a program here for a friend - stay tuned')

start_game()