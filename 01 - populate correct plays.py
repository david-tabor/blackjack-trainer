
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


# Illustrate access
print('STAND ON 17+')
p_hand = '17+'
d_hand = '6'
correct_play = correct_plays[p_hand][d_hand]
print('Player has {p}.  Dealer showing {d}.'.format(p = p_hand, d = d_hand))
print('The correct play is {x}.'.format(x = correct_play))
print('')
input()

print('STAND ON 12+ WHEN DEALER WEAK')
p_hand = '13'
d_hand = '6'
correct_play = correct_plays[p_hand][d_hand]
print('Player has {p}.  Dealer showing {d}.'.format(p = p_hand, d = d_hand))
print('The correct play is {x}.'.format(x = correct_play))
print('')
input()

print('HIT ON 12+ WHEN DEALER STRONG')
p_hand = '13'
d_hand = '7'
correct_play = correct_plays[p_hand][d_hand]
print('Player has {p}.  Dealer showing {d}.'.format(p = p_hand, d = d_hand))
print('The correct play is {x}.'.format(x = correct_play))
print('')
input()

print('DOUBLE ON 10 OR 11')
p_hand = '10'
d_hand = '10'
correct_play = correct_plays[p_hand][d_hand]
print('Player has {p}.  Dealer showing {d}.'.format(p = p_hand, d = d_hand))
print('The correct play is {x}.'.format(x = correct_play))
print('')
input()

print('HIT ON 9 OR LESS')
p_hand = '5-8'
d_hand = '6'
correct_play = correct_plays[p_hand][d_hand]
print('Player has {p}.  Dealer showing {d}.'.format(p = p_hand, d = d_hand))
print('The correct play is {x}.'.format(x = correct_play))
print('')
input()
