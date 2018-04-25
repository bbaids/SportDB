import csv
from APIController import APIController

client = APIController('nba', '2016-2017-regular')

print('Initiated Controller')

gameJSON = client.getPlayerGamelogs(player='isaiah-thomas', date='20161026')

print('Completed GET')

with open('available_stats.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter='c', lineterminator='\n')
    for stat in gameJSON['playergamelogs']['gamelogs'][0]['stats']:
        file.writerow([str(stat)])
