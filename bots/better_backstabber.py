ROUND_THRESHOLD = 1000
REPUTATION_THRESHOLD = 0.55
REP_MULTIPLIER = 1.0
SUCKERS = 0.2

def hunt_choices(round_number, current_food, current_reputation, m,
                 player_reputations):

    avg_reputation = float(sum(player_reputations))/len(player_reputations)
    if round_number <= ROUND_THRESHOLD:
        avg_reputation = max(avg_reputation, REPUTATION_THRESHOLD)
    players_to_trust = REP_MULTIPLIER * (avg_reputation * len(player_reputations))
    players_to_backstab = SUCKERS * len(player_reputations)
    lower_bound = int(min(players_to_backstab, len(player_reputations)-1))
    upper_bound = int(min(players_to_trust+players_to_backstab, len(player_reputations)))
    
    reps = zip(range(len(player_reputations)), list(player_reputations))
    reps.sort(key=lambda tup: tup[1], reverse=True)
    anti_suckers = [r[0] for r in reps[lower_bound:upper_bound]]

    if round_number == 200:
        print "avg_reputation", avg_reputation
        print "players_to_trust", players_to_trust
        print "players_to_backstab", players_to_backstab
        print anti_suckers
    
    hunt_decisions = list()
    for i in xrange(len(player_reputations)):
        if i in anti_suckers:
            hunt_decisions.append('h')
        else:
            hunt_decisions.append('s')
    return hunt_decisions

def hunt_outcomes(food_earnings):
    pass # do nothing

def round_end(award, m, number_hunters):
    pass # do nothing
