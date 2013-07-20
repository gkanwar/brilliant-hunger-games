def hunt_choices(round_number, current_food, current_reputation, m,
            player_reputations):

    avg_reputation = float(sum(player_reputations))/len(player_reputations)

    reps = list(player_reputations)
    reps.sort()
    sucker = reps[int(0.9 * len(player_reputations))]
    
    hunt_decisions = list()
    for reputation in player_reputations:
        if reputation >= sucker:
            hunt_decisions.append('s')
        if reputation >= avg_reputation:
            hunt_decisions.append('h')
        else:
            hunt_decisions.append('s')
    return hunt_decisions

def hunt_outcomes(food_earnings):
    pass # do nothing

def round_end(award, m, number_hunters):
    pass # do nothing
