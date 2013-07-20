#! /usr/bin/python

import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bots import always_hunt
from bots import never_hunt


class Player(object):
    def __init__(self, hunt_choices, hunt_outcomes, round_end,
                 initialFood, name):
        self.hunt_choices = hunt_choices
        self.hunt_outcomes = hunt_outcomes
        self.round_end = round_end
        self.food = initialFood
        self.h = 0
        self.s = 0
        self.name = name # For reporting purposes

    def reputation(self):
        # Initially 0
        if self.h+self.s == 0:
            return 0
        else:
            return float(self.h) / float(self.h+self.s)


INITIAL_PLAYERS = [(5, always_hunt, "ALWAYS_HUNT"),
                   (0, never_hunt, "NEVER_HUNT")]
MAX_ROUNDS = 100000

roundNumber = 1
players = []

def initGame():
    totalPlayers = sum(map(lambda tup: tup[0], INITIAL_PLAYERS))
    for num, module, name in INITIAL_PLAYERS:
        for i in xrange(num):
            players.append(Player(module.hunt_choices,
                                  module.hunt_outcomes,
                                  module.round_end,
                                  300*(totalPlayers-1),
                                  '%s_%s' % (name, i)))

    assert totalPlayers == len(players)


if __name__ == "__main__":
    initGame()

    # Main loop
    while players and len(players)>1 and roundNumber != MAX_ROUNDS:
        if roundNumber % 1000 == 0:
            print "Round " + str(roundNumber)

        choices = []

        # Generate threshold
        m = random.randint(1, len(players)*(len(players)-1)-1)

        for i, p in enumerate(players):
            # Random list of other players
            other = [j for j in xrange(len(players)) if j != i]
            random.shuffle(other)
            # Choices dict holds a tuple for each entry:
            # Player choices, other player indices
            choices.append((p.hunt_choices(
                        roundNumber, p.food, p.reputation(), m,
                        [players[o].reputation() for o in other]),
                            other))

        totalHunts = 0
        awards = []

        for i, p in enumerate(players):
            foodEarnings = []
            # Compute earnings
            player_choices, other = choices[i]
            for j, choice in zip(other, player_choices):
                other_choices, other_other = choices[j]
                other_choice = other_choices[other_other.index(i)]
                
                # Only update the current player, the other player will be
                # updated when we loop to them (slow, but we don't care)
                foodDiff = 0
                if choice == 'h':
                    totalHunts += 1
                    foodDiff -= 6
                    p.h += 1
                    if other_choice == 'h':
                        foodDiff += 6
                    else:
                        foodDiff += 3
                else:
                    foodDiff -= 2
                    p.s += 1
                    if other_choice == 'h':
                        foodDiff += 3
                    else:
                        pass
                foodEarnings.append(foodDiff)
            # Report hunt outcomes for this player
            p.hunt_outcomes(foodEarnings)
            awards.append(sum(foodEarnings))

        # Check total hunts
        if totalHunts >= m:
            for i in xrange(len(players)):
                awards[i] += 2*(len(players)-1)
        
        # Call round_end and kill players
        next_players = []
        for i, p in enumerate(players):
            p.food += awards[i]
            p.round_end(awards[i], m, totalHunts)
            if p.food > 0:
                next_players.append(p)
        players = next_players

        roundNumber += 1

    print "Game over after %s rounds!" % (roundNumber)
    print "Players left alive:"
    for p in players:
        print "Player: %s -- FOOD[%s] REPUTATION[%s]" % (p.name, p.food, p.reputation())
