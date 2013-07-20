def hunt_choices(round_number, current_food, current_reputation, m,
            player_reputations):
    
    hunt_decisions = list()
    for reputation in player_reputations:
        if reputation > 0.5:
            hunt_decisions.append('h')
        else:
            hunt_decisions.append('s')
    return hunt_decisions

def hunt_outcomes(food_earnings):
    pass # do nothing

def round_end(award, m, number_hunters):
    pass # do nothing
