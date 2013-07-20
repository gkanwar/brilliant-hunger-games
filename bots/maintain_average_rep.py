def hunt_choices(round_number, current_food, current_reputation, m,
            player_reputations):

    avg_reputation = float(sum(player_reputations))/len(player_reputations)
    players_to_trust = avg_reputation * len(player_reputations)

    reps = list(player_reputations)
    reps.sort()
    rep_to_trust = reps[players_to_trust]
    
    hunt_decisions = list()
    for reputation in player_reputations:
        if reputation >= rep_to_trust:
            hunt_decisions.append('h')
        else:
            hunt_decisions.append('s')
    return hunt_decisions

def hunt_outcomes(food_earnings):
    pass # do nothing

def round_end(award, m, number_hunters):
    pass # do nothing
