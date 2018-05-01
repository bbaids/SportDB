import csv
from APIController import APIController

def csvWriter_Game(season):
    client = APIController('nba', season)
    print('Initiated Controller For ' + season)

    #Read stats and abbreviations from file
    statString, statList = getStats()
    
    #Create the header list and add it to a new file
    headers = ['game_id', 'team_id', 'player_id']
    headers.extend(statList)

    teamList = getTeams(season)

    with open('game_' + season + '.csv', 'w') as csvfile:
        file = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        file.writerow(headers)

    for team in teamList:
        print('Making GET call for ' + team)
        gameJSON = client.getPlayerGamelogs(team=team,playerstats=statString)

        with open('game_' + season + '.csv', 'a') as csvfile:
            file = csv.writer(csvfile, delimiter=',', lineterminator='\n')

            for gamePlayer in gameJSON['playergamelogs']['gamelogs']:
                row = [gamePlayer['game']['id'], gamePlayer['team']['ID'], gamePlayer['player']['ID']]
                for stat in statList:
                    row.append(gamePlayer['stats'][stat]['#text'])
                file.writerow(row)

        print('Write Complete for ' + team)
    print('Write Complete for ' + season)

#read the file of desired fields and put it in a list and string.
def getStats():
    statList = []
    statString = ''
    with open('stat_list.csv', 'r') as statFile:
        f = csv.reader(statFile, delimiter=',', lineterminator='\n')
        for statRow in f:
            statString = statString + ',' + statRow[1]
            statList.append(statRow[2])

    #Trimming leading comma
    statString = statString[1:]
    return statString, statList

#read the file of teams and put it in a list.
def getTeams(season):
    teamList = []
    with open('team_list_' + season + '.csv', 'r') as teamFile:
        f = csv.reader(teamFile, delimiter=',', lineterminator='\n')
        for teamRow in f:
            teamList.append(teamRow[0])
            
    return teamList

seasonList = ['2016-2017-regular', '2017-2018-regular']
for season in seasonList:
    csvWriter_Game(season)
