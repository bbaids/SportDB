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
gameJSON = client.getPlayerGamelogs(playerstats=statString)

print('Completed GET')

##Create the header list
headers = ['game_id', 'team_id', 'player_id']
headers.extend(statList)

with open('game_2016_2017_regular.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    file.writerow(headers)

    for gamePlayer in gameJSON['playergamelogs']['gamelogs']:
        keys = [gamePlayer['game']['id'], gamePlayer['team']['ID'], gamePlayer['player']['ID']]
        row = keys
        for stat in statList:
            row.append(gamePlayer['stats'][stat]['#text'])
        file.writerow(row)

print('Write Complete')
