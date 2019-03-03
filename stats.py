import conversation_game as cg

def test_ia(nb_games, ia):
    nb_backtracking_victories = 0
    nb_backtracking_defeats = 0
    nb_draw = 0

    for i in range(nb_games):
        winner, played_quotes, played_type_quotes = cg.game(verbose=False, ia_chosen=ia)
        if winner == 0:
            nb_backtracking_victories += 1
        elif winner == 1:
            nb_backtracking_defeats += 1
        elif winner == 2:
            nb_draw += 1

    print("Ia : %s" %(ia))
    print("Backtracking victories : %s / %s" %(nb_backtracking_victories, nb_games))
    print("Backtracking defeats : %s / %s" %(nb_backtracking_defeats, nb_games))
    print("Draws : %s / %s" %(nb_draw, nb_games))

nb_games = 1000
ias = ["naive", "count", "near"]

for ia in ias:
    test_ia(nb_games, ia)
