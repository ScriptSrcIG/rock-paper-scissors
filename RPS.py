import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return "R"

    beats = {"R": "P", "P": "S", "S": "R"}

    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1

    most_common = max(counts, key=counts.get)
    counter_freq = beats[most_common]

    if len(opponent_history) >= 3:
        last_three = opponent_history[-3:]
        if last_three.count(last_three[-1]) == 3:
            return beats[last_three[-1]]

    counter_last = beats[opponent_history[-1]]

    return random.choice([counter_freq, counter_last])
  
