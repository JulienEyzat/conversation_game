# conversation_game

A very simple game with backtracking IAs.

The rules of the game:
- Each turn, a player choose a quote which can be positive, negative or neutral.
- On a normal turn, a player can only say a positive or negative quote.
- If three quotes of the same type are said in a row, the player has to play a neutral one.
- If the next player say a quote from the same type of the three before, he loses the game.

For humans, this game have an interest with time limit and quotes from human memory, but, here, I just use it to test some simple heuristics on backtracking algorithm.

The heuristics of the backtracking algorithms:
- "naive" : Returns true when it find a victory condition. With an enough high max depth, it is only playing the first type of quote tested. So, this one is very weak, it loses more than the random algorithm.
- "count" : It counts the number of victories and defeats on each type of quotes and play the one with the best ratio victories/defeats. With a max depth set to 1, it will never lose because it will just avoid the loosing side when it has to play after a neutral play. It is very dependent of the max depth, efficient with 5 but not with 6 for instance.
- "near win" : Returns the depth of the nearest win. This one became very efficient when the max depth is high. This one is definitely the most interesting one.
- "near defeat" : This one return the depth of the nearest defeat. It avoid the defeat, so it never loses but it does a lot of draws.
