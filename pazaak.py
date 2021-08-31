import random
import sys

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

    def draw(self):
        deck_choice = int(random.randint(1, 10))
        while not self.has_card(deck_choice):
            deck_choice = int(random.randint(1,10))
        self.contents[deck_choice] -= 1
        self.counter += 1
        return deck_choice
        
class Player:
    def __init__(self, name, credits=1000):
        self.player_name = name
        self.credit_total = credits
        self.card_count = 0
        self.card_value = 0
        self.is_standing = False

    def change_card_value(self, card):
        self.card_value += card
        self.card_count += 1
        return self.card_value
    
    def get_card_value(self):
        return self.card_value
    
    def change_credit_value(self, value):
        self.credit_total += value
        return self.credit_total
    
    def get_credit_value(self):
        return self.credit_total

class PazaakGame:
    def __init__(self, wager, player1="Player 1", player2="computer", cpu=True):
        self.wager = wager
        self.opponent_is_computer = cpu
        self.main_deck = PazaakMainDeck()
        self.round_count = 0
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.game_is_over = False

    
    def cycle_round(self):
        print(f"Wager for this match: {self.wager}")
        self.round_count += 1
        print(f"Round #{self.round_count}:")
    
    # Player turns could be refactored to one function to be DRY, but there will only ever be 2 players, so for now having two turn functions is acceptable.
    def player1_turn(self):
        print(f"{self.player1.player_name}'s turn:\n")
        if not self.player1.is_standing:
            card_drawn = self.main_deck.draw()
            print(f"{self.player1.player_name} draws {card_drawn} from the main deck.")
            self.player1.change_card_value(card_drawn)
            player1_choice = input("Stand, End Turn, or Forfeit?").lower()
            if player1_choice == "stand":
                self.player1.is_standing = True
                print(f"{self.player1.player_name} is standing with {self.player1.get_card_value()}.")
            elif player1_choice == "forfeit":
                sys.exit(f"{self.player1.player_name} has forfeited. \n {self.player2.player_name} wins with {self.player2.get_card_value()}!")
            else:
                print(f"{self.player1.player_name} ends their turn with {self.player1.get_card_value()}.")
        else:
            print(f"{self.player1.player_name} is standing with {self.player1.get_card_value()}.")
    
    def player2_turn(self):
        print(f"{self.player2.player_name}'s turn:\n")
        if not self.player2.is_standing:
            card_drawn = self.main_deck.draw()
            print(f"{self.player2.player_name} draws {card_drawn} from the main deck.")
            self.player2.change_card_value(card_drawn)
            player2_choice = input("Stand, End Turn, or Forfeit?").lower()
            if player2_choice == "stand":
                self.player2.is_standing = True
                print(f"{self.player2.player_name} is standing with {self.player2.get_card_value()}.")
            elif player2_choice == "forfeit":
                sys.exit(f"{self.player2.player_name} has forfeited. \n {self.player1.player_name} wins with {self.player2.get_card_value()}!")
            else:
                print(f"{self.player2.player_name} ends their turn with {self.player2.get_card_value()}.")
        else:
            print(f"{self.player2.player_name} is standing with {self.player2.get_card_value()}.")

    def win_condition_to_print(self):
        player1_value = self.player1.get_card_value()
        player2_value = self.player2.get_card_value()

        if player1_value == 20 and player2_value != 20:
            return f"{self.player1.player_name} wins with 20!"
        elif player2_value == 20 and player1_value != 20:
            return f"{self.player2.player_name} wins with 20!"
        elif player1_value > player2_value and self.player2.is_standing:
            return f"{self.player1.player_name} wins with {player1_value} against {self.player2.player_name}'s standing {player2_value}."
        elif player2_value > player1_value and self.player1.is_standing:
            return f"{self.player2.player_name} wins with {player2_value} against {self.player1.player_name}'s standing {player1_value}."
        elif player1_value > 20:
            return f"{self.player1.player_name} has busted out. {self.player2.player_name} wins with {player2_value}."
        elif player2_value > 20:
            return f"{self.player2.player_name} has busted out. {self.player1.player_name} wins with {player1_value}."
        else:
            return f"Current scores: \n {self.player1.player_name}: {player1_value} \n {self.player2.player_name}: {player2_value} "
        
    def evaluate_score(self):
        string_to_print = self.win_condition_to_print()
        if "Current scores" not in string_to_print:
            self.game_is_over = True
            print(string_to_print)
        else:
            self.cycle_round()

   

def game_against_computer():
    main_deck = PazaakMainDeck()
    turn_count = 0
    wager = input("Please enter how many credits you want to wager on the game: ")
    def cycle_turn():
        # nonlocal is like global, but grabs values from the enclosing scope
        nonlocal turn_count
        print(f"Wager for this match: {wager}")
        turn_count += 1
        print(f"Turn #{turn_count}:")
    cycle_turn()
    choice_1 = main_deck.draw()
    print(f"Player draws {choice_1} from the main deck.")



def game_against_friend():
    print('There will be a program here for playing with a friend - stay tuned')

start_game()