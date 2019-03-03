import random

def random_player(type_dict):
    return type_dict[int(2 * random.random())]

# This backtracking algorithm only play positive with a enough high max_depth.
def naive_backtracking(quote_type_choice, supposed_type_quotes, end_condition, supposed_player_turn, backtracking_player, depth, max_depth):
    supposed_type_quotes.append(quote_type_choice)
    # Victory condition
    if supposed_type_quotes[-5:] in end_condition and supposed_player_turn == 1 - backtracking_player:
        return True
    elif depth == max_depth:
        return False
    else:
        if supposed_type_quotes[-3:] in [["negative"]*3, ["positive"]*3]:
            naive_backtracking("neutral", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth+1, max_depth)
        else:
            if not naive_backtracking("positive", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth+1, max_depth):
                return naive_backtracking("negative", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth+1, max_depth) # Negative
            else:
                return True # Positive

# This algorithm count the number of defeat and victory but cut the tree when it found one so it is very unefficient.
def count_backtracking(quote_type_choice, supposed_type_quotes, end_condition, supposed_player_turn, backtracking_player, depth, max_depth):
    supposed_type_quotes.append(quote_type_choice)
    more = 0
    # Victory condition
    if supposed_type_quotes[-5:] in end_condition and supposed_player_turn == 1 - backtracking_player:
        more = 1 # Win
    if supposed_type_quotes[-5:] in end_condition and supposed_player_turn == backtracking_player:
        more = -1 # Loss
    elif depth >= max_depth:
        return 0 # Draw

    if supposed_type_quotes[-3:] in [["negative"]*3, ["positive"]*3]:
        return more + count_backtracking("neutral", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth + 1, max_depth)
    else:
        return more + count_backtracking("positive", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth + 1, max_depth) + count_backtracking("negative", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth + 1, max_depth)

# This algorithm count the proximity to the nearest victory
def near_backtracking(quote_type_choice, supposed_type_quotes, end_condition, supposed_player_turn, backtracking_player, depth, max_depth, near_type):
    supposed_type_quotes.append(quote_type_choice)
    more = 0
    # Victory condition
    if supposed_type_quotes[-5:] in end_condition and supposed_player_turn == 1 - backtracking_player:
        if near_type == "win": # Win
            return depth
        else:
            return max_depth
    if supposed_type_quotes[-5:] in end_condition and supposed_player_turn == backtracking_player:
        if near_type == "defeat": # Loss
            return depth
        else:
            return max_depth
    elif depth == max_depth:
        return max_depth # Draw
    else:
        if supposed_type_quotes[-3:] in [["negative"]*3, ["positive"]*3]:
            return near_backtracking("neutral", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth+1, max_depth, near_type)
        else:
            pos_depth = near_backtracking("positive", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth + 1, max_depth, near_type)
            neg_depth = near_backtracking("negative", supposed_type_quotes, end_condition, 1 - supposed_player_turn, backtracking_player, depth + 1, max_depth, near_type)
            if pos_depth < neg_depth:
                return pos_depth
            else:
                return neg_depth

def backtracking_player(backtracking_type, backtracking_player, played_type_quotes, end_condition, type_dict, max_depth, near_type):
    if backtracking_type == "naive":
        if naive_backtracking("positive", played_type_quotes.copy(), end_condition, backtracking_player, backtracking_player, 0, max_depth):
            quote_type_choice = "positive"
        elif naive_backtracking("negative", played_type_quotes.copy(), end_condition, backtracking_player, backtracking_player, 0, max_depth):
            quote_type_choice = "negative"
        else:
            quote_type_choice = random_player(type_dict)
    elif backtracking_type == "count":
        positive_res = count_backtracking("positive", played_type_quotes.copy(), end_condition, backtracking_player, backtracking_player, 0, max_depth)
        negative_res = count_backtracking("negative", played_type_quotes.copy(), end_condition, backtracking_player, backtracking_player, 0, max_depth)
        # print("neg %s pos %s" %(negative_res, positive_res))
        if negative_res < positive_res:
            quote_type_choice = "positive"
        elif negative_res > positive_res:
            quote_type_choice = "negative"
        else:
            quote_type_choice = random_player(type_dict)
    elif backtracking_type == "near":
        positive_res = near_backtracking("positive", played_type_quotes.copy(), end_condition, backtracking_player, backtracking_player, 0, max_depth, near_type)
        negative_res = near_backtracking("negative", played_type_quotes.copy(), end_condition, backtracking_player, backtracking_player, 0, max_depth, near_type)
        # print("neg %s pos %s" %(negative_res, positive_res))
        if negative_res == positive_res:
            quote_type_choice = random_player(type_dict)
        elif near_type == "win":
            if negative_res < positive_res:
                quote_type_choice = "negative"
            elif negative_res > positive_res:
                quote_type_choice = "positive"
        elif near_type == "defeat":
            if negative_res > positive_res:
                quote_type_choice = "negative"
            elif negative_res < positive_res:
                quote_type_choice = "positive"
    return quote_type_choice
