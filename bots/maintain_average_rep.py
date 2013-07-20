REP_MULTIPLIER = 1.25

def hunt_choices(round_number, current_food, current_reputation, m,
                 player_reputations):

    avg_reputation = float(sum(player_reputations))/len(player_reputations)
    players_to_trust = min(REP_MULTIPLIER * (avg_reputation * len(player_reputations)), len(player_reputations))

    reps = list(player_reputations)
    reps.sort(reverse=True)
    rep_to_trust = reps[int(players_to_trust-1)]
    num_above_rep_to_trust = len([r for r in reps if r > rep_to_trust])
    num_equal_rep_to_trust = players_to_trust - num_above_rep_to_trust

    hunt_decisions = list()
    for reputation in player_reputations:
        if reputation > rep_to_trust:
            hunt_decisions.append('h')
        elif reputation == rep_to_trust and num_equal_rep_to_trust > 0:
            hunt_decisions.append('h')
            num_equal_rep_to_trust -= 1
        else:
            hunt_decisions.append('s')
    return hunt_decisions

def hunt_outcomes(food_earnings):
    pass # do nothing

def round_end(award, m, number_hunters):
    pass # do nothing
