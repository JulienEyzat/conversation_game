import csv
import random

import ia

def get_quotes_from_db():
    positive_quotes = []
    neutral_quotes = []
    negative_quotes = []
    with open('data.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[0] == "positive":
                positive_quotes.append(row[1])
            elif row[0] == "neutral":
                neutral_quotes.append(row[1])
            elif row[0] == "negative":
                negative_quotes.append(row[1])
    return positive_quotes, neutral_quotes, negative_quotes

def end_game(end_type, winner, played_quotes, played_type_quotes):
    if end_type == "victory":
        print("The player %s win" %(winner))
    elif end_type == "draw":
        print("Draw")
    print("The quotes played are :")
    player=0
    for quote in played_quotes:
        print("Player %s : %s" %(player, quote))
        player = 1 - player
    print("The type of quotes played are :")
    player=0
    for type in played_type_quotes:
        print("Player %s : %s" %(player, type))
        player = 1 - player

def game(verbose, ia_chosen, max_backtracking_depth = 5):
    positive_quotes, neutral_quotes, negative_quotes = get_quotes_from_db()

    # Define the end condition of the game
    end_negative_condition = ["negative", "negative", "negative", "neutral", "negative"]
    end_positive_condition = ["positive", "positive", "positive", "neutral", "positive"]
    end_condition = [end_negative_condition, end_positive_condition]

    player_turn = 0
    type_dict = {0: "positive", 1: "negative", 2: "neutral"}
    played_type_quotes = [] # Positive, negative or neutral
    played_quotes = []
    while True:
        # If the player must put a neutral quote
        if played_type_quotes[-3:] in [["negative"]*3, ["positive"]*3]:
            quote_type_choice = "neutral"
            quote_choice = random.choice(neutral_quotes)
            neutral_quotes.remove(quote_choice)
        # Backtracking player
        else:
            if player_turn == 0:
                quote_type_choice = ia.backtracking_player(ia_chosen, player_turn, played_type_quotes, end_condition, type_dict, max_backtracking_depth)
            else:
                quote_type_choice = ia.random_player(type_dict) # x = 0 ou x = 1

            if quote_type_choice == "positive":
                quote_choice = random.choice(positive_quotes)
                positive_quotes.remove(quote_choice)
            elif quote_type_choice == "negative":
                quote_choice = random.choice(negative_quotes)
                negative_quotes.remove(quote_choice)

        # Add the quote played to the game
        played_type_quotes.append(quote_type_choice)
        played_quotes.append(quote_choice)

        # End the game with victory
        if played_type_quotes[-5:] in end_condition:
            winner = 1 - player_turn
            if verbose:
                end_game("victory", winner, played_quotes, played_type_quotes)
            return winner, played_quotes, played_type_quotes

        # End the game with draw
        if not positive_quotes or not negative_quotes:
            if verbose:
                end_game("draw", 2, played_quotes, played_type_quotes)
            return 2, played_quotes, played_type_quotes

        # New turn
        player_turn = 1 - player_turn

if __name__ == "__main__":
    game(verbose="True", ia_chosen="count")
