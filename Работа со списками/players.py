players = ['charles', 'martina', 'micheal', 'florence', 'elli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])


players = ['charles', 'martina', 'micheal', 'florence', 'elli']

print("Here are the first three players on my team:")
for players in players[:3]:
    print(players.title())

