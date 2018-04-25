import csv
from APIController import APIController

client = APIController('nba', '2016-2017-regular')

print('Initiated Controller')

gameJSON = client.getPlayerGamelogs(player='isaiah-thomas', date='20161026')

print('Completed GET')

##print(gameJSON['playergamelogs']['gamelogs'][0]['stats']['Fg2PtAtt'])

availableStats = []
for stat in gameJSON['playergamelogs']['gamelogs'][0]['stats']:
        availableStats.append(stat)

print(availableStats)

with open('available_stats.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for stat in availableStats:
        file.writerow([stat, gameJSON['playergamelogs']['gamelogs'][0]['stats'][stat]['@abbreviation']])
