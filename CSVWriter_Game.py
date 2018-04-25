import csv
from APIController import APIController

client = APIController('nba', '2016-2017-regular')

print('Initiated Controller')

gameJSON = client.getPlayerGamelogs(player='isaiah-thomas', date='20161026')

print('Completed GET')

##f = open('output.txt', 'w')
##f.write(str(gameJSON))
##f.close()

with open('available_stats.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter='c', lineterminator='\n')
    for stat in gameJSON['playergamelogs']['gamelogs'][0]['stats']:
        file.writerow([str(stat)])

##print('Wrote to file')

##with open('schedule_2017_playoff.csv', 'w') as csvfile:
##    file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
##    file.writerow(['ID', 'Date', 'AwayTeamID', 'AwayTeamCity', 'AwayTeamName', 'AwayTeamAbbrev', 'HomeTeamID', 'HomeTeamCity', 'HomeTeamName', 'HomeTeamAbbrev'])
##
##    for game in scheduleJSON['fullgameschedule']['gameentry']:
##        file.writerow([game['id'],
##                        game['date'],
##                        game['awayTeam']['ID'],
##                        game['awayTeam']['City'],
##                        game['awayTeam']['Name'],
##                        game['awayTeam']['Abbreviation'],
##                        game['homeTeam']['ID'],
##                        game['homeTeam']['City'],
##                        game['homeTeam']['Name'],
##                        game['homeTeam']['Abbreviation']
##                       ])
##
##print('Write Complete')
