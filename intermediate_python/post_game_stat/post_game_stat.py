players = [
    {
        'name': 'Arrascaeta', 'position': 'Meio-campo',
        'shirt_number': 10, 'goals': 6
    },
    {
        'name': 'Léo Ortiz', 'position': 'Zagueiro',
        'shirt_number': 3, 'goals': 1
    },
    {
        'name': 'Pedro', 'position': 'Atacante',
        'shirt_number': 9, 'goals': 10
    },
]

names = [player['name'] for player in players]
print('Players name:', names)

position = [position['position'] for position in players]
print('Position of players', position)

# update stat
players[0]['goals'] += 3
players[2]['goals'] += 5

# average
goal_average = sum(player['goals'] for player in players) / len(players)
print('Average goals:', goal_average)
