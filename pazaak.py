import random

def start_game():
    opponent_choice = input("Would you like to play against the computer, or against a friend? ").lower()
    if opponent_choice == "computer":
        game_against_computer()
    elif opponent_choice == "friend":
        game_against_friend()
    else: 
        print("Please type either 'computer' or 'friend' into the console.")


class PazaakMainDeck:
    def __init__(self):
        self.counter = 0
        self.contents = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4}
    
    def reset_main_deck(self):
        self.contents = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4}
        self.counter = 0
        print("Main deck reset.")

    def has_card(self, key):
        if self.contents[key] > 0:
            return True
        else:
            return False

    def choose(self):
        deck_choice = int(random.randint(1, 10))
        while not self.has_card(deck_choice):
            deck_choice = int(random.randint(1,10))
        self.contents[deck_choice] -= 1
        self.counter += 1
        return deck_choice
        




   

def game_against_computer():
    turn_count = 0
    wager = input("Please enter how many credits you want to wager on the game: ")
    def cycle_turn():
        # nonlocal is like global, but grabs values from the enclosing scope
        nonlocal turn_count
        print(f"Wager for this match: {wager}")
        turn_count += 1
        print(f"Turn #{turn_count}:")
    cycle_turn()
    choice_1 = deck_choice()
    print(f"Player draws {choice_1} from the main deck.")



def game_against_friend():
    print('There will be a program here for playing with a friend - stay tuned')

start_game()