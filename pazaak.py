import random

def start_game():
    opponent_choice = input("Would you like to play against the computer, or against a friend? ").lower()
    if opponent_choice == "computer":
        game_against_computer()
    elif opponent_choice == "friend":
        game_against_friend()
    else: 
        print("Please type either 'computer' or 'friend' into the console.")

main_deck = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4}

def deck_choice():
    return int(random.randint(1, 10))

def game_against_computer():
    turn_count = 0
    wager = input("Please enter how many credits you want to wager on the game: ")
    print("Wager for this match: " + wager)
    turn_count += 1
    print(f"Turn #{turn_count}:")
    choice_1 = deck_choice()
    print(f"Player draws {choice_1} from the main deck.")



def game_against_friend():
    print('There will be a program here for a friend - stay tuned')

start_game()