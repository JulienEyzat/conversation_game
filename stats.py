import conversation_game as cg

def test_ia(nb_games, ia, max_depth, near_type=None):
    nb_backtracking_victories = 0
    nb_backtracking_defeats = 0
    nb_draw = 0

    for i in range(nb_games):
        winner, played_quotes, played_type_quotes = cg.game(verbose=False, ia_chosen=ia, near_type=near_type, max_backtracking_depth=max_depth)
        if winner == 0:
            nb_backtracking_victories += 1
        elif winner == 1:
            nb_backtracking_defeats += 1
        elif winner == 2:
            nb_draw += 1

    if near_type:
        print("Ia : %s %s" %(ia, near_type))
    else:
        print("Ia : %s" %(ia))
    print("Backtracking victories : %s / %s" %(nb_backtracking_victories, nb_games))
    print("Backtracking defeats : %s / %s" %(nb_backtracking_defeats, nb_games))
    print("Draws : %s / %s" %(nb_draw, nb_games))

nb_games = 1000
ias = ["naive", "count", "near"]
near_types = ["win", "defeat"]
max_depth = 8

for ia in ias:
    if ia == "near":
        for near_type in near_types:
            test_ia(nb_games, ia, max_depth, near_type)
    else:
        test_ia(nb_games, ia, max_depth)
