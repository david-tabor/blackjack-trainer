
# Define allowed player and dealer hands
player_hands = ['5-8', '9', '10', '11', '12', '13', '14', '15', '16', '17+']
dealer_hands = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A']

# Initailze table of correct plays
correct_plays = {}
for player_hand in player_hands:
    d = {}
    for dealer_hand in dealer_hands:
        d[dealer_hand] = 'Undefined'
    correct_plays[player_hand] = d

# Populate correct plays: Stand on 17+
p_hand = '17+'
correct_play = 'STAND'
for d_hand in correct_plays[p_hand].keys():
    correct_plays[p_hand][d_hand] = correct_play

# Populate correct plays: Stand on 12+ when dealer is weak
p_hands = ['12', '13', '14', '15', '16']
d_hands = ['2', '3', '4', '5', '6']
correct_play = 'STAND'
for p_hand in p_hands:
    for d_hand in d_hands:
        correct_plays[p_hand][d_hand] = correct_play

# Populate correct plays: Stand on 12+ when dealer is strong
p_hands = ['12', '13', '14', '15', '16']
d_hands = ['7', '8', '9', '10', 'A']
correct_play = 'HIT'
for p_hand in p_hands:
    for d_hand in d_hands:
        correct_plays[p_hand][d_hand] = correct_play

# Populate correct plays: Double on 10 or 11
p_hands = ['10', '11']
d_hands = correct_plays[p_hand].keys()
correct_play = 'DOUBLE'
for p_hand in p_hands:
    for d_hand in d_hands:
        correct_plays[p_hand][d_hand] = correct_play

# Populate correct plays: Hit on 9 or less
p_hands = ['5-8', '9']
d_hands = correct_plays[p_hand].keys()
correct_play = 'HIT'
for p_hand in p_hands:
    for d_hand in d_hands:
        correct_plays[p_hand][d_hand] = correct_play

# Define main GUI iterator
def run_hand(player_hand, dealer_hand):
    print('Welcome to Blackjack Trainer v0.1\n')
    print('Player has {p}.  Dealer showing {d}.'.format(p = player_hand, d = dealer_hand))
    print('Options are (s)tand, (h)it, or (d)ouble.')
    for _ in range(35):
        print('')
    user_input = input()
    print('Welcome to Blackjack Trainer v0.1\n')
    print('Player has {p}.  Dealer showing {d}.'.format(p = player_hand, d = dealer_hand))

    user_play = 'Bad input!'
    if (user_input=='s'): user_play='STAND'
    if (user_input=='h'): user_play='HIT'
    if (user_input=='d'): user_play='DOUBLE'
    print('You chose to {s}.'.format(s = user_play))
    correct_play = correct_plays[player_hand][dealer_hand]
    print('The correct play is {x}.'.format(x = correct_play))
    print('')
    outcome = 'WRONG'
    if (user_play == correct_play) : outcome='CORRECT'
    print('You were {outcome}!'.format(outcome=outcome))
    for _ in range(31):
        print('')
    print('Options are (q)uit or any other key to continue.')
    return input()

import random
ph = random.choice(player_hands)
dh = random.choice(dealer_hands)

# Call GUI iterator
user_input = ''
while (user_input != 'q'):

    ph = random.choice(player_hands)
    dh = random.choice(dealer_hands)


    user_input = run_hand(player_hand = ph, dealer_hand=dh)

print('Thank you for using Blackjack Trainer v0.1!')
for _ in range(38):
    print('')

