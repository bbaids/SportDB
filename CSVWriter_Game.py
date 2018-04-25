import csv
from APIController import APIController

client = APIController('nba', '2016-2017-regular')

print('Initiated Controller')

##read the file of desired fields and put it in a list and string.
statList = []
statString = ''
with open('desired_stats.csv', 'r') as statFile:
    f = csv.reader(statFile, delimiter=',', lineterminator='\n')
    for row in f:
        statString = statString + ',' + row[1]
        statList.append(row[0])

##Trimming leading comma
statString = statString[1:]

##Making API call
gameJSON = client.getPlayerGamelogs(team='bos', date='20161026', playerstats=statString)

print('Completed GET')

f = open('output.txt', 'w')
f.write(str(gameJSON))
f.close()

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
