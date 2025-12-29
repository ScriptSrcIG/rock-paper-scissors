import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "R" and p2_play == "S") or \
             (p1_play == "P" and p2_play == "R") or \
             (p1_play == "S" and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        else:
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results["p1"]
    win_rate = games_won / num_games * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return win_rate


def quincy(prev_play, counter=[0]):
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    if len(opponent_history) < 10:
        return random.choice(["R", "P", "S"])
    most_common = max(set(opponent_history[-10:]), key=opponent_history[-10:].count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]


def kris(prev_play):
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    return {"R": "P", "P": "S", "S": "R"}[prev_play]


def abbey(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    if len(opponent_history) < 2:
        return random.choice(["R", "P", "S"])
    last_two = opponent_history[-2:]
    return random.choice(last_two)
  
